-- bonus = 100% salary
-- conditions:
-- - employee_id % 2 == 1
-- - name NOT LIKE "M%"
-- else: bonus = 0
-- return: employee_id, bonus.
-- order by: employee_id
SELECT employee_id,
    CASE
        WHEN employee_id % 2 = 1 AND name not LIKE 'M%' THEN salary
        ELSE 0
    END AS bonus
FROM employees
ORDER BY employee_id;