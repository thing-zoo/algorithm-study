select c1.car_id, c1.car_type, 
       floor(c1.daily_fee*30*(1-c3.discount_rate*0.01)) as fee
from CAR_RENTAL_COMPANY_CAR c1,
     CAR_RENTAL_COMPANY_RENTAL_HISTORY c2,
     CAR_RENTAL_COMPANY_DISCOUNT_PLAN c3
where c1.car_id = c2.car_id
and c1.car_type = c3.car_type
and c1.car_type in ('세단', 'SUV')
and c3.duration_type = '30일 이상'
group by c1.car_id
having max(c2.end_date) < '2022-11-01'
and fee >= 500000 and fee < 2000000
order by fee desc, c1.car_type, c1.car_id desc