-- 코드를 입력하세요
SELECT MEMBER_ID,MEMBER_NAME, GENDER,  to_char(date_of_birth, 'YYYY-MM-DD') as DATE_OF_BIRTH from member_profile
where to_char(date_of_birth, 'MM') = '03'
and tlno is not null
and gender='W'
order by member_id