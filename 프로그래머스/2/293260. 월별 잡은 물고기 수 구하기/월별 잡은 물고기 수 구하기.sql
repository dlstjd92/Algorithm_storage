-- 코드를 작성해주세요
# 자기 잡힌달을 달고있는 아이디 쿼리문 ㄱㄱ
select count(m) as fish_count, m as MONTH
from (
select id, month(time) as m
from fish_info
) as sub
group by m
order by m