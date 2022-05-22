USE Bus_Depots;

-- 1st exercise: (Built-in functions) Find the maximum, minimum and average driver’s salary.

SELECT ROUND(MAX(bdsalary), 2) AS max_salary, ROUND(MIN(bdsalary), 2) AS min_salary, ROUND(AVG(bdsalary), 2) AS avg_salary FROM BusDriver;

-- 2nd exercise: (Built-in functions) Count the number of drivers who are working for Middlesex Transport at the moment. Change the column heading in the result to make it ‘friendly’.

-- Assuming Middlesex-related areas are 'Wembley, Ealing, Acton, Twickenham, Finchley, Hendon, Wood Green, Harrow, Ruislip and Uxbridge.' as per the web source at http://www.essentialtravelguide.com/regional-guides/southern-england/middlesex-travel-guide/middlesex-travel-transport/, the routes no. 7 and 8 including Finchley and Hendon, with depot no. 101, are relevant.

SELECT COUNT(BusDriver.dno) AS num_drivers_middlesex FROM BusDriver
INNER JOIN Route on BusDriver.dno = Route.dno
WHERE rdescript LIKE 'Finchley%' OR 'Hendon%';

-- 3rd exercise: Find route information (route number and description) for all routes which connect to the Holloway Depot.

SELECT Route.rno AS route_num, Route.rdescript AS route_descr FROM Route
INNER JOIN Depot ON Route.dno = Depot.dno
WHERE Depot.dname LIKE 'Holloway%';

-- 4th exercise: Now try question 3 with a JOIN.

SELECT Route.rno AS route_num, Route.rdescript AS route_descr FROM Route
LEFT JOIN Depot ON Route.dno = Depot.dno
WHERE Depot.dname LIKE 'Holloway%';

-- 5th exercise: (NULL) List bus details for any bus which has not been assigned to a depot.

SELECT * FROM Bus
WHERE dno IS NULL;

-- 6th exercise: (NOT IN) List all drivers (name and number) who are on the system but are not yet responsible for a route.

SELECT bdname AS driver_name, bdno AS driver_num FROM BusDriver
WHERE dno IS NULL OR dno NOT IN (SELECT dno FROM Route);

-- 7th exercise: (GROUP BY) List each depot name and the average salary for drivers working at the depot.

SELECT Depot.dname AS depot_name, ROUND(AVG(bdsalary), 2) AS avg_salary FROM BusDriver
INNER JOIN Depot ON BusDriver.dno = Depot.dno
GROUP BY Depot.dname;

-- 8th exercise: (GROUP BY HAVING) List each depot by name and count the number of bus drivers who are assigned to each, for depots with more than one driver.

SELECT Depot.dname AS depot_name, COUNT(BusDriver.dno) AS num_drivers FROM BusDriver
INNER JOIN Depot ON BusDriver.dno = Depot.dno
GROUP BY Depot.dname
HAVING COUNT(BusDriver.bdname) > 1;

-- 9th exercise: (GROUP BY plus JOIN) For each cleaner responsible for buses of bus type doubledecker or minibus (typo - this should have been 'midibus'), list his/her name and number and find the total number for which each cleaner is responsible.

SELECT Cleaner.cname AS cleaner_name, Cleaner.cno as cleaner_num, COUNT(Bus.model) AS num_diff_buses_assigned 
FROM Cleaner
INNER JOIN Bus ON Bus.cno = Cleaner.cno
INNER JOIN BusType ON Bus.tno = BusType.tno
WHERE BusType.tdescript LIKE '%double-decker%' OR BusType.tdescript LIKE '%midibus%'
GROUP BY Cleaner.cname;

-- 10th exercise: (ORDER BY)
-- 10th exercise.a: List all drivers (name and number) and their routes (number and description, order by driver number.

SELECT BusDriver.bdname AS driver_name, BusDriver.bdno AS driver_num, Route.rno AS route_num, Route.rdescript AS route_descr 
FROM BusDriver
INNER JOIN Route ON Route.dno = BusDriver.dno
ORDER BY BusDriver.bdno;

-- 10th exercise.b: Now order by route description within driver number.

SELECT BusDriver.bdname AS driver_name, BusDriver.bdno AS driver_num, Route.rno AS route_num, Route.rdescript AS route_descr 
FROM BusDriver
INNER JOIN Route ON Route.dno = BusDriver.dno
ORDER BY Route.rdescript;
