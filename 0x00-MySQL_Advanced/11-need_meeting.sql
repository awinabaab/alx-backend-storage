-- Creates a view need_meeting that lists all student that have a score under 80 and last_meeting of more than 1 month

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
	AND (
		last_meeting IS NULL
		OR last_meeting < (CURRENT_DATE - INTERVAL 1 MONTH)
	);
