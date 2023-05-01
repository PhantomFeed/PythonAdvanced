SELECT s.full_name AS student_name, AVG(g.grade) AS avg_grade
FROM students s
JOIN assignments_grades g ON s.student_id = g.student_id
GROUP BY s.student_id
ORDER BY avg_grade DESC
LIMIT 10;