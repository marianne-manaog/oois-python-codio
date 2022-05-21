SELECT id,birthday,country FROM basic_info
WHERE birthday BETWEEN 2015 AND 2016 -- Date is not a string with the BETWEEN operator
ORDER BY birthday DESC;
