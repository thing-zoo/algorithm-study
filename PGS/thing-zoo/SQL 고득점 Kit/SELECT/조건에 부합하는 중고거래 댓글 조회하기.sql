select b.title,
       b.board_id,
       r.reply_id,
       r.writer_id,
       r.contents,
       substring(r.created_date, 1, 10) as created_date
from used_goods_board b, used_goods_reply r
where b.board_id = r.board_id
and b.created_date like '2022-10-%'
order by r.created_date, b.title