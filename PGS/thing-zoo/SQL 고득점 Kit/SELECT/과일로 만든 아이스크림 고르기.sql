select f.flavor
from first_half f, icecream_info i
where f.flavor = i.flavor
and f.total_order > 3000
and i.ingredient_type = 'fruit_based'
order by f.total_order desc