import json
from rest_framework import status
from rest_framework.test import APITestCase


class OrderTests(APITestCase):
    def setUp(self) -> None:
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
        }
        response = self.client.post(url, data, format="json")
        json_response = json.loads(response.content)
        self.token = json_response["token"]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Create a product category
        url = "/productcategories"
        data = {"name": "Sporting Goods"}
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        response = self.client.post(url, data, format="json")

        # Create a product
        url = "/products"
        data = {
            "name": "Kite",
            "price": 14.99,
            "quantity": 60,
            "description": "It flies high",
            "category_id": 1,
            "location": "Pittsburgh",
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        response = self.client.post(url, data, format="json")

        # Create a payment type
        url = "/payment-types"
        data = {
            "merchant_name": "Visa",
            "account_number": "fiojoiji87416ert1458",
            "expiration_date": "2030-01-01",
            "create_date": "2026-05-15",
        }
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        payment_json = json.loads(response.content)
        self.created_payment_id = payment_json["id"]

    def test_add_product_to_order(self):
        """
        Ensure we can add a product to an order.
        """
        # Add product to order
        url = "/cart"
        data = {"product_id": 1}
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Get cart and verify product was added
        url = "/cart"
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        response = self.client.get(url, None, format="json")
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["id"], 1)
        self.assertEqual(json_response["size"], 1)
        self.assertEqual(len(json_response["lineitems"]), 1)

    def test_remove_product_from_order(self):
        """
        Ensure we can remove a product from an order.
        """
        # Add product
        self.test_add_product_to_order()

        # Remove product from cart
        url = "/cart/1"
        data = {"product_id": 1}
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        response = self.client.delete(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Get cart and verify product was removed
        url = "/cart"
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        response = self.client.get(url, None, format="json")
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["size"], 0)
        self.assertEqual(len(json_response["lineitems"]), 0)

    # TODO: Complete order by adding payment type

    def test_complete_order_by_adding_payment(self):

        cart_url = "/cart"
        cart_data = {"product_id": 1}
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        cart_response = self.client.post(cart_url, cart_data, format="json")
        self.assertEqual(cart_response.status_code, status.HTTP_204_NO_CONTENT)

        order_url = "/orders/1"
        order_data = {"payment_type": self.created_payment_id}

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        response = self.client.put(order_url, order_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        get_response = self.client.get(order_url, format="json")
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

        final_order = json.loads(get_response.content)

        payment_info = final_order["payment_type"]
        self.assertIn(f"/payment-types/{self.created_payment_id}", payment_info["url"])
        self.assertEqual(payment_info["merchant_name"], "Visa")
        self.assertEqual(len(final_order["lineitems"]), 1)

    # TODO: New line item is not added to closed order
