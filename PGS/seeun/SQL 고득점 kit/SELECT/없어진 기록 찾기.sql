-- 코드를 입력하세요
SELECT a.animal_id, a.name from animal_outs a full join animal_ins b on a.animal_id = b.animal_id
where a.datetime is not null
and b.datetime is null
order by animal_id