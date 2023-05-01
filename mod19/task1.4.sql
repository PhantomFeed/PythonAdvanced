SELECT s.group_id, AVG(x.overdue_count) AS avg_overdue_count, MAX(x.overdue_count) AS max_overdue_count, MIN(x.overdue_count) AS min_overdue_count
FROM students s
LEFT OUTER JOIN(
    SELECT ag.student_id, COUNT(*) AS overdue_count
    FROM assignments_grades ag
    JOIN assignments a ON ag.assisgnment_id = a.assisgnment_id
    WHERE ag.date > a.due_date
    GROUP BY ag.student_id) AS x ON s.student_id = x.student_id
GROUP BY s.group_id;