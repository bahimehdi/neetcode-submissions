-- Write your query below
SELECT S.seller_name
FROM seller S
LEFT JOIN orders O ON S.seller_id = O.seller_id
    AND EXTRACT(YEAR FROM o.sale_date) = 2020
WHERE O.order_id IS NULL
ORDER BY S.seller_name ASC;