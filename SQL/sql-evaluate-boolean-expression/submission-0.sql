SELECT left_operand, operator, right_operand,
    CASE
        WHEN operator = '=' AND V1.value = V2.value THEN 'true'
        WHEN operator = '<' AND V1.value < V2.value THEN 'true'
        WHEN operator = '>' AND V1.value > V2.value THEN 'true'
        ELSE 'false'
    END AS value
FROM variables V1
JOIN expressions ON V1.name = expressions.left_operand
JOIN variables V2 ON V2.name = expressions.right_operand;