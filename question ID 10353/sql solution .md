```sql
select worker_title from worker as w
inner join title as t
on w.worker_id = t.worker_ref_id
where salary in (select max(salary) from worker)
```