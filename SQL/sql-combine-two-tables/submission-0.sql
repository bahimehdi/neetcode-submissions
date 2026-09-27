-- Write your query below
SELECT P.first_name, P.last_name, A.city, A.state
FROM person P
LEFT JOIN address A ON P.person_id = A.person_id;