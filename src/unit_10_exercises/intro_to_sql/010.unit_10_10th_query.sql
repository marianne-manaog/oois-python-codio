SELECT * FROM basic_info
WHERE birthday <> 2014 -- <> operator can also be written like: !=
AND id BETWEEN 3 AND 7
ORDER BY email ASC;
