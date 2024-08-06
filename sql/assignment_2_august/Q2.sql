DELIMITER $$

CREATE PROCEDURE upsert_employee(IN p_emp_no INT,IN p_birth_date DATE,IN p_first_name VARCHAR(50),IN p_last_name VARCHAR(50),IN p_gender ENUM('M', 'F'),IN p_hire_date DATE)
BEGIN
    DECLARE emp_exists INT;

    SELECT COUNT(*) INTO emp_exists
    FROM employees
    WHERE emp_no = p_emp_no;

    IF emp_exists > 0 THEN
        UPDATE employees
        SET birth_date = p_birth_date,
            first_name = p_first_name,
            last_name = p_last_name,
            gender = p_gender,
            hire_date = p_hire_date
        WHERE emp_no = p_emp_no;
    ELSE
        INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date)
        VALUES (p_emp_no, p_birth_date, p_first_name, p_last_name, p_gender, p_hire_date);
    END IF;
END $$

DELIMITER ;

CALL upsert_employee(203, '1990-08-20', 'Ishu', 'Jangid', 'M', '9999-01-10');
select * from employees;

