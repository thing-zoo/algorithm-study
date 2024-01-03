SELECT a.rest_id, a.rest_name, a.food_type, a.favorites, a.address, round(avg(b.review_score), 2) as score
from rest_info a join rest_review b
on a.rest_id = b.rest_id
where substr(a.address, 1,2) = '서울'
group by a.rest_id, a.rest_name, a.food_type, a.favorites, a.address
order by score desc, a.favorites desc