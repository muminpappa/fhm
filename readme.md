# Getting started

## Set up a database table

Connect to MySQL as root:

    sudo mysql -h localhost

and create user and database:

    CREATE USER 'kali'@'localhost' IDENTIFIED BY 'passwooord';
    CREATE DATABASE FHM;
    GRANT ALL ON FHM.* TO 'kali'@'localhost';

Continue as normal user 

    mysql -p

and create a table:

    use FHM;
    CREATE TABLE new_infections_per_day (fetch_date DATE, detected_date DATE, number INT);

## Useful links

https://xlrd.readthedocs.io/en/latest/api.html

https://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python

https://docs.python.org/3/tutorial/index.html

https://dev.mysql.com/doc/refman/5.6/en/loading-tables.html
