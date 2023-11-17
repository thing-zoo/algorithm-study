SELECT user_id, product_id from online_sale
group by user_id, product_id -- 해당 컬럼만 그룹으로 묶어서
having count(*) >= 2 -- 2개 이상인 행만 출력
order by user_id asc, product_id desc