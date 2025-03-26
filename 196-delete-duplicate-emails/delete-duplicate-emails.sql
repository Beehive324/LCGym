/* Write your T-SQL query statement below */
DELETE a

from person a, person b where a.id > b.id and a.email = b.email