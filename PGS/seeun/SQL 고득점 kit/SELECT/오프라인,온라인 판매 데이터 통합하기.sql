-- 코드를 입력하세요
SELECT sales_date, product_id, nvl(user_id, null) as user_id, sales_amount
from(select to_char(sales_date, 'YYYY-MM-DD') as sales_date -- 3월에 구매한 사람들만 모아서 두 테이블 합치기
     , product_id
     , user_id
     , sales_amount
     from online_sale
     where to_char(sales_date, 'YYYY-MM') = '2022-03'
     
     union
     
     select to_char(sales_date, 'YYYY-MM-DD') as sales_date
     , product_id
     , NULL -- 오프라인 구매자는 user_id가 없으므로 null 넣기
     , sales_amount
     from offline_sale
     where to_char(sales_date, 'YYYY-MM') = '2022-03'
    )
order by sales_date, product_id, user_id