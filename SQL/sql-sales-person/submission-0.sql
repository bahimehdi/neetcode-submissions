-- companies to which a salesperson hasn't made any sales with CRIMSON
SELECT S.name
FROM sales_person S
WHERE S.sales_id NOT IN (
    SELECT O.sales_id
    FROM orders O
    JOIN company C ON O.com_id = C.com_id
    WHERE C.name = 'CRIMSON'
)