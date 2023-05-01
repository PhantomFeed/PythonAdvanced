SELECT DISTINCT full_name
FROM students s
JOIN students_groups sg ON s.group_id = sg.group_id
JOIN assignments a ON sg.teacher_id = a.teacher_id
JOIN assignments_grades ag ON a.assisgnment_id = ag.assisgnment_id
WHERE ag.assisgnment_id = (SELECT assisgnment_id FROM assignments_grades GROUP BY assisgnment_id ORDER BY AVG(grade) DESC LIMIT 1);