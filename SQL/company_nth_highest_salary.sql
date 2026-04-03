
/*
Used Postgresql
https://onecompiler.com/postgresql/44j7mr3n4
*/

-- Create Department table
CREATE TABLE Employee (
    id INT PRIMARY KEY,
    salary INT NOT NULL
);
 
-- -- Insert Department data
-- INSERT INTO Employee (id, salary) VALUES
-- (1, 100),
-- (2, 200),
-- (3, 300);


-- -- Insert Department data
-- INSERT INTO Employee (id, salary) VALUES
-- (1, 100);


-- -- Insert Department data
-- INSERT INTO Employee (id, salary) VALUES
-- (1, 100),
-- (2, 200),
-- (3, 200);


-- Insert Department data
INSERT INTO Employee (id, salary) VALUES
(1, 400),
(2, 300),
(3, 200),
(4, 400);


-- with cte as (
-- select Dense_Rank() over (order by salary desc), * from Employee
-- )
-- select max(salary) as SecondHighestSalary from cte where Dense_Rank = 2;


with cte as (
select Row_number() over (order by salary desc), * from Employee
)
select * from cte;
/*
 row_number | id | salary 
------------+----+--------
          1 |  1 |    400
          2 |  4 |    400
          3 |  2 |    300
          4 |  3 |    200
*/

with cte as (
select Row_number() over (order by salary desc), * from Employee
)
select * from cte where row_number = 2;
/*
 row_number | id | salary 
------------+----+--------
          2 |  4 |    400
*/

with cte as (
select Rank() over (order by salary desc), * from Employee
)
select * from cte;
-- important note that there is no row with rank = 2
/*
 rank | id | salary 
------+----+--------
    1 |  1 |    400
    1 |  4 |    400
    3 |  2 |    300
    4 |  3 |    200
*/

with cte as (
select Rank() over (order by salary desc), * from Employee
)
select * from cte where rank = 2;
-- important note that there is no row with rank = 2
/*
 rank | id | salary 
------+----+--------
*/

with cte as (
select Dense_Rank() over (order by salary desc), * from Employee
)
select * from cte;
-- Desnse_Rank() solves the problem with Rank() function of rank = 2
/*
 dense_rank | id | salary 
------------+----+--------
          1 |  1 |    400
          1 |  4 |    400
          2 |  2 |    300
          3 |  3 |    200
*/

with cte as (
select Dense_Rank() over (order by salary desc), * from Employee
)
select * from cte where Dense_Rank = 2;
-- Desnse_Rank() solves the problem with Rank() function of rank = 2
/*
 dense_rank | id | salary 
------------+----+--------
          2 |  2 |    300
*/

SELECT MAX(salary) AS SecondHighestSalary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as dr
    FROM Employee
) as temp
WHERE dr = 2;
/*
 secondhighestsalary 
---------------------
                 300
*/
