SELECT t.full_name AS teacher_name, AVG(ag.grade) AS avg_grade
FROM assignments a
JOIN assignments_grades ag ON a.assisgnment_id = ag.assisgnment_id
JOIN teachers t ON a.teacher_id = t.teacher_id
GROUP BY t.teacher_id
ORDER BY avg_grade
LIMIT 1;