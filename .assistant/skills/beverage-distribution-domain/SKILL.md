---
name: beverage-distribution-domain
description: Use when building synthetic beverage distribution workshop assets for account, product, inventory, promotion, and sales workflows.
---

# Customer Domain: Beverage Distribution

Use this skill when the task involves a beverage distribution workshop domain.

## Domain Rules

- Treat the customer as a synthetic beverage distribution business for workshop purposes.
- Never invent real customer data, people, addresses, emails, contracts, or credentials.
- Use account, product, order, inventory, promotion, and rep note entities.
- Keep examples small and explainable in a live workshop.

## Default Use Case

Field Sales Account Intelligence Copilot:

- identify account health
- detect reorder risk
- explain promotion and inventory context
- recommend next actions
- capture human feedback

## Entity Grains

- accounts: one row per account
- products: one row per product
- orders: one row per order line
- inventory: one row per product, region, and date
- promotions: one row per promotion, product, and region
- rep_notes: one row per account note

## Output Standards

- Prefer business-friendly column names.
- Add table and column comments.
- Include edge cases for low inventory, pending orders, returns, and license review.
- Clearly separate synthetic demo logic from production recommendations.
