DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY,
  customer_name TEXT NOT NULL,
  segment TEXT NOT NULL,
  region TEXT NOT NULL,
  signup_date TEXT NOT NULL
);

CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY,
  customer_id INTEGER NOT NULL,
  order_date TEXT NOT NULL,
  product_category TEXT NOT NULL,
  order_amount REAL NOT NULL,
  status TEXT NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers (customer_id, customer_name, segment, region, signup_date) VALUES
  (1, 'Avery Labs', 'startup', 'West', '2025-01-12'),
  (2, 'Benton Studio', 'small_business', 'Midwest', '2025-02-03'),
  (3, 'Cedar Services', 'enterprise', 'East', '2025-02-20'),
  (4, 'Dune Retail', 'small_business', 'South', '2025-03-02'),
  (5, 'Ember Works', 'startup', 'West', '2025-03-18'),
  (6, 'Fable Group', 'enterprise', 'East', '2025-04-08');

INSERT INTO orders (order_id, customer_id, order_date, product_category, order_amount, status) VALUES
  (101, 1, '2025-03-01', 'database', 240.00, 'paid'),
  (102, 1, '2025-03-15', 'analytics', 120.00, 'paid'),
  (103, 2, '2025-03-17', 'database', 80.00, 'paid'),
  (104, 2, '2025-04-01', 'support', 50.00, 'refunded'),
  (105, 3, '2025-04-03', 'database', 700.00, 'paid'),
  (106, 3, '2025-04-08', 'analytics', 300.00, 'paid'),
  (107, 4, '2025-04-11', 'support', 65.00, 'paid'),
  (108, 5, '2025-04-12', 'database', 180.00, 'pending'),
  (109, 6, '2025-04-14', 'analytics', 450.00, 'paid'),
  (110, 6, '2025-04-21', 'database', 620.00, 'paid');

