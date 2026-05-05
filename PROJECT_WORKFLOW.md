# Project Workflow / Team Working Agreement

---

## Project Goals

* Try to complete all tickets by last sprint
* Ensure all team members contribute across frontend/backend
* Leave time for stretch goals and polishing CSS/code improvements

---

## Communication Standards

* In-class check-ins each class day to discuss progress and blockers
* Daily check Slack for new messages/updates
* Raise blockers within an hour of being stuck
* Notify team before major architectural changes

---

## Adding New Dependencies

* Discuss in team meeting before adding new dependencies/frameworks/libraries
* Consider impact on project size, performance, and learning curve

---

## Git / Branching Strategy

* Branch naming: `initials/short-description-ticket-#` (e.g., `js/add-product-page-ticket-14`)
* No direct commits to `main`!
* Merge `dev` into feature branch before PR (if needed)

---

## Commit Message Standards

* Use present tense (e.g., "add feature", not "added feature")
* Include a short description of the change(s) in the commit message
* Use `git --no-pager diff --staged` to see changes if getting AI to help write commit message
* Optional Format: `type(scope): short description` (e.g., `feat(product): add product listing page`)
* Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

---

## Pull Request Standards

* PRs are merged into `dev` branch, not `main`
* PR title includes ticket #
* Use PR template for description and testing steps
* PR explains:
  * What feature was added/changed
  * Why it was added/changed
  * How to test
* Minimum 1 reviewer approval before merge
* Reviewers check:
  * Code quality and readability
  * Functionality works as described by `fetch`ing the branch and testing locally
  * Ensures no major bugs or issues
* PR author addresses review comments before merge

---

## Definition of Done

A ticket is complete when:

* Ticket description or criteria met
* A PR is opened, reviewed, and approved by at least one reviewer
* Code is merged to `dev` branch

---

## Story Point Values

* 1 Point: Small bug fix, minor UI change, or simple backend endpoint (1 hour or less)
* 2 Points: New feature with moderate complexity, or significant refactor (1-2 hours)
* 3 Points: Large feature with multiple components, complex backend logic, or significant refactor (2-4 hours)
* 5 Points: Major feature that touches multiple parts of the app, or significant architectural change (4-8 hours)
* 8 Points: Very large feature or epic that requires multiple tickets to complete (8+ hours)

---

## Coding Standards

* Follow existing project patterns unless team agrees otherwise
* Use meaningful variable/function names
* Keep components/functions focused/small

---

## Testing Standards

* Manually test frontend/backend before making PR
* Include testing steps in PR description
* (optional) Make loom video showing feature in action
* If reviewing a PR, `fetch` the branch and test locally before approving
* Report any bugs found during testing in the PR comments

---

## Ticket Workflow

Backlog → Todo → In Progress → In Review → Done

---

## Learning / Research Process

* For spikes:
  * Research individually first
  * Share findings with team
  * Agree on implementation strategy before coding

---

## Architecture Decisions

* Full-stack ownership per ticket
* TanStack Query replaces useAppContext where practical
* Stores tied 1:1 with Customer profile
* Reports use Django templates, not React pages

---

## Dev to Main Promotion

* Only merge to `main` when last sprint is complete and all tickets are done
* Ensure all features are tested and working in `dev` before merging to `main`
* Use PR template to explain why merging to `main` and any final testing steps

---

## Stretch Goals

* Product rating UI
* Seller dashboard analytics
* Wishlist functionality
* TypeScript conversion of key components

---