```sql
WITH RECURSIVE num AS (
  SELECT 1 AS n
  UNION ALL
  SELECT n + 1 FROM num 
  WHERE n < 15
)

SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(categories, ';', n), ';', -1) AS category,
       SUM(review_count) AS review_cnt
FROM yelp_business
JOIN num ON n <= CHAR_LENGTH(categories) - CHAR_LENGTH(REPLACE(categories, ';', '')) + 1
GROUP BY category
ORDER BY review_cnt DESC;
```