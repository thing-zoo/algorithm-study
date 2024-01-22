SELECT *
FROM PLACES
WHERE HOST_ID in (  SELECT HOST_ID
                    FROM PLACES
                    GROUP BY HOST_ID
                    HAVING COUNT(*) >= 2 )