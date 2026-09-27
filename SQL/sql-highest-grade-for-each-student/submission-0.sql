-- a student_id highest score and that exam's exam_id
-- special case 1:
-- - if a student has the same highest score on multiple exams => return the one with min(exam_id) then
SELECT E.student_Id, MIN(E.exam_id) AS exam_id, E.score
FROM exam_results E
WHERE (E.student_id, E.score) IN (
    SELECT student_id, MAX(score)
    FROM exam_results
    GROUP BY student_id
)
GROUP BY E.student_id, E.score;