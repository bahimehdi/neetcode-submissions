-- Write your query below
SELECT U.name, COALESCE(SUM(R.distance), 0) AS travelled_distance
FROM users U
LEFT JOIN rides R ON U.id = R.user_id
GROUP BY U.name
ORDER BY travelled_distance DESC;