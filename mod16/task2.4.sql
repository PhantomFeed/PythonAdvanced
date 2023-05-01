SELECT c.full_name AS customer_name, o.order_no
FROM customer c
JOIN 'order' o ON c.customer_id = o.customer_id
WHERE o.manager_id IS NULL;