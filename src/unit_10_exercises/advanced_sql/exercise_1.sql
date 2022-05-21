USE Bus_Depots;

-- 1st exercise: (Project, RESTRICT) List all drivers (number and name) who have a salary of less than 1800.

SELECT bdno as driver_num, bdname as driver_name FROM BusDriver 
WHERE bdsalary < 1800;

-- 2nd exercise: (Conditional operator LIKE) List all bus drivers (number and name) whose name begins with J.
SELECT bdno as driver_num, bdname as driver_name FROM BusDriver 
WHERE bdname LIKE 'J%';

-- 3rd exercise: (Conditional operator BETWEEN) List all bus drivers details for those drivers who have a salary between 2000 and 4000

SELECT * FROM BusDriver 
WHERE bdsalary BETWEEN 2000 AND 4000;

-- 4th exercise: (AND) List all buses (registration number and model) of type 2 which are not based at depot 101.

SELECT regno as registration_num, model as bus_model FROM Bus 
WHERE tno = 2 
AND dno != 101;

-- 5th exercise: (OR) List buses (all details )which are either Volvo model s or Mercedes models. 
-- What is the output when you change OR to AND? An empty set would be returned.

SELECT * FROM Bus 
WHERE model LIKE 'Volvo%' OR model LIKE 'Mercedes&';

-- 6th exercise: (Controlling duplicates using DISTINCT) List all depot numbers in the bus table. Now eliminate all duplicates.

SELECT DISTINCT(dno) AS unique_depot_num FROM Bus
WHERE dno IS NOT NULL;

-- 7th exercise: (Two table Join – INNER JOIN) List all cleaners (number and name) with the name and address of their depot, but only for those cleaners located at a depot.

SELECT Cleaner.cno AS cleaner_num, Cleaner.cname AS cleaner_name, Depot.dname AS depot_name, Depot.daddress AS depot_address 
FROM Cleaner
INNER JOIN Depot
ON Cleaner.dno = Depot.dno  
WHERE Cleaner.dno IS NOT NULL;

-- 8th exercise: (Three table JOIN) List bus drivers (number and name) and the bus types (description) for which each bus driver has had training

SELECT BusDriver.bdno AS driver_num, BusDriver.bdname AS driver_name, BusType.tdescript AS bus_type_descr
FROM ((BusDriver 
INNER JOIN Training 
ON BusDriver.bdno = Training.bdno)
INNER JOIN BusType 
ON Training.tno = BusType.tno);

-- 9th exercise: (Four table JOIN) List all cleaners (number and name), the name of their depot and the bus registration numbers with the type of bus that they are responsible for.

SELECT Cleaner.cno AS cleaner_num, Cleaner.cname AS cleaner_name, Depot.dname AS depot_name, Bus.regno AS registration_num, BusType.tdescript AS bus_type_descr 
FROM (((Cleaner
INNER JOIN Depot
ON Cleaner.dno = Depot.dno)
INNER JOIN Bus
ON Cleaner.dno = Bus.dno)
INNER JOIN BusType
ON Bus.tno = BusType.tno);

-- 10th exercise.a: (OUTER JOIN) Rewrite question 7 as an OUTER JOIN. Describe the query in English. 

-- The equivalent query leveraging an outer join is provided below.

SELECT Cleaner.cno AS cleaner_num, Cleaner.cname AS cleaner_name, Depot.dname AS depot_name, Depot.daddress AS depot_address 
FROM Cleaner 
LEFT JOIN Depot 
ON Cleaner.dno = Depot.dno 
WHERE Cleaner.dno IS NOT NULL;

-- 10th exercise.b: Now list all cleaners (number and name), the name of their depot and the bus registration numbers with the type of bus that they are responsible for, including those cleaners who are not assigned to a bus or a depot.

SELECT Cleaner.cno AS cleaner_number, Cleaner.cname AS cleaner_forename, Depot.dname AS depot_naming, Bus.regno AS registration_number, BusType.tdescript AS bus_type_descript 
FROM (((Cleaner
LEFT JOIN Depot
ON Cleaner.dno = Depot.dno
AND IFNULL(Cleaner.dno,'`') = IFNULL(Depot.dno,'`'))
LEFT JOIN Bus
ON Cleaner.dno = Bus.dno
AND IFNULL(Cleaner.dno,'`') = IFNULL(Bus.dno,'`'))
LEFT JOIN BusType
ON Bus.tno = BusType.tno);
