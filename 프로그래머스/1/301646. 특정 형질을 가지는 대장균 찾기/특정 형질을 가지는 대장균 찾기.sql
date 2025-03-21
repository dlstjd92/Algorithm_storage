-- 코드를 작성해주세요
-- 각 객체의 제노타입을 이진법으로 변환해서 -> 2번형질과 1,3번 형질을 확인해서 수를 새는 문제
# 10 -> 2임
select count(genotype) as count from ecoli_data where (2&genotype = 0) and (genotype & 1 <>0 or genotype & 4 <>0);