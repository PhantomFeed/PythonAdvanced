SELECT c.full_name
FROM customer c
LEFT OUTER JOIN "order" o on c.customer_id = o.customer_id
WHERE o.order_no IS NULL;