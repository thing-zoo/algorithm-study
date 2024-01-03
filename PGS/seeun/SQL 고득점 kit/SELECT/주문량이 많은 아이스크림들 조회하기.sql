-- -- 코드를 입력하세요
SELECT flavor from (select a.flavor, sum(a.total_order) + sum(b.total_order) as tot
                    from first_half a join july b on a.flavor = b.flavor
                    group by a.flavor
                    order by tot desc)
where rownum <=3