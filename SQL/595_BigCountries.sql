-- Write your PostgreSQL query statement below
select name, population, area 
from public.World
where area >= 3000000 or population >= 25000000