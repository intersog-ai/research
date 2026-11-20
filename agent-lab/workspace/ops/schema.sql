CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY, customer TEXT, total REAL);
DELETE FROM orders;
INSERT INTO orders(customer, total) VALUES ('acme', 120.0), ('globex', 75.5), ('initech', 310.0);
