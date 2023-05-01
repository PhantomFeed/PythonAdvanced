SELECT AVG(grade) as avg_grade
FROM assignments_grades ag
JOIN assignments a ON ag.assisgnment_id = a.assisgnment_id
WHERE a.assignment_text LIKE '%прочитать%' OR a.assignment_text LIKE '%выучить%';