SELECT CASE WHEN salary < 50000 THEN '<50000'
            WHEN salary BETWEEN 50000 AND 100000 THEN '50000-100000'
            ELSE '>100000'
            END AS SalaryRange,

AVG(salary) AS AverageSalary FROM salaries GROUP BY SalaryRange;