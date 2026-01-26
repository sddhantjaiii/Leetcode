# Write your MySQL query statement below
select p.project_id ,round(ifnull(sum(e.experience_years)/count(e.employee_id),0) ,2)as average_years
from project p
left join employee e
on e.employee_id=p.employee_id
group by p.project_id