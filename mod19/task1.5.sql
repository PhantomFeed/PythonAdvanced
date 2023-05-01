SELECT
    s.group_id,
    COUNT(DISTINCT s.student_id) AS total_students,
    AVG(ag.grade) AS avg_grade,
    COUNT(DISTINCT CASE WHEN ag.grade IS NULL THEN s.student_id END) AS ungraded_count,
    COUNT(DISTINCT CASE WHEN ag.date > a.due_date THEN s.student_id END) AS overdue_count,
    COUNT(DISTINCT ag.grade_id) AS attempts_count
FROM students s
LEFT JOIN assignments_grades ag ON s.student_id = ag.student_id
LEFT JOIN assignments a ON ag.assisgnment_id = a.assisgnment_id
GROUP BY s.group_id;