SELECT c.full_name AS customer_name, m.full_name AS manager_name, o.purchase_amount, o.date
FROM "order" o
JOIN customer c ON c.customer_id = o.customer_id
LEFT OUTER JOIN manager m ON o.manager_id = m.manager_id;