
```sql
SELECT DISTINCT h.host_id, g.guest_id
FROM airbnb_hosts h
INNER JOIN airbnb_guests g ON h.nationality = g.nationality
AND h.gender = g.gender
```