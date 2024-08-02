DELIMITER $$

CREATE FUNCTION get_experience( p_emp_no INT)
RETURNS INT
deterministic

BEGIN
    DECLARE experience INT; 

    SELECT TIMESTAMPDIFF(YEAR, hire_date, CURDATE()) INTO experience
    FROM employees
    WHERE emp_no = p_emp_no;

    RETURN experience;
END $$

DELIMITER ;

SELECT get_experience(202) AS experience;





