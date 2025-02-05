DROP VIEW IF EXISTS employee_view;
CREATE VIEW employee_view AS SELECT * FROM employees WHERE emp_no IN (10001, 10002, 10003, 10004, 10005);

DROP VIEW IF EXISTS dept_emp_view;
CREATE VIEW dept_emp_view AS SELECT * FROM dept_emp WHERE emp_no IN (10004, 10005, 10006, 10007, 10008);

SELECT e.emp_no, e.birth_date, e.first_name, e.last_name, e.gender, e.hire_date, d.dept_no, d.from_date, d.to_date FROM  employee_view e LEFT JOIN dept_emp_view d ON e.emp_no = d.emp_no
UNION
SELECT d.emp_no, e.birth_date, e.first_name, e.last_name, e.gender, e.hire_date, d.dept_no, d.from_date, d.to_date FROM employee_view e RIGHT JOIN dept_emp_view d ON e.emp_no = d.emp_no;
