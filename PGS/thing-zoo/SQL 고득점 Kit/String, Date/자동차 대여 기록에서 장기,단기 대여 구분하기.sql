-- datediff(end_date, start_date) : end_date - start_date 값 반환
select history_id, 
       car_id, 
       substring(start_date, 1, 10) as start_date,
       substring(end_date, 1, 10) as end_date,
       if(datediff(end_date, start_date) >= 29, '장기 대여', '단기 대여') as rent_type
from car_rental_company_rental_history
where start_date like '2022-09-%'
order by history_id desc