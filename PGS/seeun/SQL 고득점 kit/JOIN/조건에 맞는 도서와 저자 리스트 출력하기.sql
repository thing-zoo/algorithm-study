SELECT book.book_id, author.author_name, to_char(book.published_date, 'YYYY-MM-DD')
from book 
join author
using (author_id)
where book.category='경제'
order by book.published_date asc