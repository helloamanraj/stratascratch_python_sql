```sql
with cte as (
select *,  sum(bonus) as emp_bonus  from sf_employee as s
right join sf_bonus as f on s.id = f.worker_ref_id
group by id
)

select employee_title, sex , avg(salary + emp_bonus) as total
from cte
group by  employee_title, sex
```