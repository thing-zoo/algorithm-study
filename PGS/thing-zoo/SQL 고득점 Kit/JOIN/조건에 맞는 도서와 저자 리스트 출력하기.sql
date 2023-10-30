SELECT BOOK_ID, AUTHOR_NAME, SUBSTRING(PUBLISHED_DATE, 1, 10) AS `PUBLISHED_DATE`
FROM BOOK B, AUTHOR A
WHERE B.CATEGORY = '경제'
AND B.AUTHOR_ID = A.AUTHOR_ID
ORDER BY PUBLISHED_DATE