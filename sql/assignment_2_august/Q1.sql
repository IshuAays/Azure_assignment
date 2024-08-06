SELECT e.emp_no, e.birth_date, e.first_name, e.last_name, e.gender, e.hire_date,d.dept_name, t.title, s.salary
FROM employees e
JOIN dept_emp de ON e.emp_no = de.emp_no
JOIN departments d ON de.dept_no = d.dept_no
JOIN titles t ON e.emp_no = t.emp_no
JOIN (
    SELECT emp_no, salary
    FROM salaries
    WHERE (emp_no, from_date) IN (
        SELECT emp_no, MAX(from_date)
        FROM salaries
        GROUP BY emp_no
    )
) s ON e.emp_no = s.emp_no;
