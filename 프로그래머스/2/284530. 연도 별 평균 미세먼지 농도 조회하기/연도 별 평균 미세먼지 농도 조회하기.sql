-- 코드를 작성해주세요
select year(ym) as YEAR, round(avg(PM_VAL1), 2) as PM10, round(avg(pm_val2), 2) as "PM2.5"
from AIR_POLLUTION
where location1 = '경기도' and location2 = '수원'
group by YEAR
order by YEAR