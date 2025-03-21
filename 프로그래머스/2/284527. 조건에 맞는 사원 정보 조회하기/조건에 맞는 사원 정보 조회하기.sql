-- 코드를 작성해주세요
select sum(c.score) as score, b.emp_no, b.emp_name, b.position, b.email
from hr_employees b
join hr_grade c
    on b.emp_no = c.emp_no
group by b.emp_no
order by score desc
limit 1
