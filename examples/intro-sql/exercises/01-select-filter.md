# Exercise 1: Select, Filter, Sort

## Goal

Practice retrieving rows from one table.

## Schema Context

Use the `customers` and `orders` tables created by `setup.sql`.

## Tasks

1. List all customers in the West region.
2. Find paid orders greater than 200.
3. Show the five most recent orders.
4. Stretch: return only `order_id`, `order_date`, `product_category`, and `order_amount`.

## Starter SQL

```sql
SELECT
  *
FROM orders;
```

## Hints

1. Use `WHERE` to filter rows.
2. Use `ORDER BY order_date DESC` for newest orders first.
3. Use `LIMIT` to restrict row count.

## Solutions

```sql
SELECT
  *
FROM customers
WHERE region = 'West';

SELECT
  *
FROM orders
WHERE status = 'paid'
  AND order_amount > 200;

SELECT
  *
FROM orders
ORDER BY order_date DESC
LIMIT 5;

SELECT
  order_id,
  order_date,
  product_category,
  order_amount
FROM orders
ORDER BY order_date DESC
LIMIT 5;
```

## Facilitator Notes

Emphasize that `WHERE` filters rows before the result is returned. Ask participants to predict row counts before running each query.

