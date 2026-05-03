# Exercise 2: Joins And Aggregation

## Goal

Practice combining tables and summarizing data.

## Tasks

1. Join customers to orders and show customer name, region, order date, category, and amount.
2. Calculate total paid order amount by customer.
3. Calculate total paid order amount by region.
4. Stretch: show only regions with paid order totals greater than 500.

## Starter SQL

```sql
SELECT
  *
FROM customers c
JOIN orders o
  ON c.customer_id = o.customer_id;
```

## Hints

1. Join on the key both tables share: `customer_id`.
2. Use `GROUP BY` for summary rows.
3. Use `HAVING` when filtering after aggregation.

## Solutions

```sql
SELECT
  c.customer_name,
  c.region,
  o.order_date,
  o.product_category,
  o.order_amount
FROM customers c
JOIN orders o
  ON c.customer_id = o.customer_id;

SELECT
  c.customer_name,
  SUM(o.order_amount) AS total_paid_amount
FROM customers c
JOIN orders o
  ON c.customer_id = o.customer_id
WHERE o.status = 'paid'
GROUP BY c.customer_id, c.customer_name
ORDER BY total_paid_amount DESC;

SELECT
  c.region,
  SUM(o.order_amount) AS total_paid_amount
FROM customers c
JOIN orders o
  ON c.customer_id = o.customer_id
WHERE o.status = 'paid'
GROUP BY c.region
ORDER BY total_paid_amount DESC;

SELECT
  c.region,
  SUM(o.order_amount) AS total_paid_amount
FROM customers c
JOIN orders o
  ON c.customer_id = o.customer_id
WHERE o.status = 'paid'
GROUP BY c.region
HAVING SUM(o.order_amount) > 500
ORDER BY total_paid_amount DESC;
```

## Facilitator Notes

Ask participants what one row means before and after grouping. This helps separate row-level filters from aggregate filters.

