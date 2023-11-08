
:TiDiscountCheckFilled: DataBase의 시작은 file이 가진 단점을 보완하기 위해서 database라는 개념이 탄생했다.

### 🚩 데이터베이스의 본질
#### 💡  어떻게 데이터를 입력하고 어떻게 출력을 할까? 
	C : create
	R : read
	U : update
	D : Delete
![[Screenshot 2023-11-06 at 10.16.23 PM.png]]
	- DataBase는 SpreadSheet보다 한 걸음 앞에 있는 것이라고 생각할 수 있다!
	- 어떤 것을 공부할 것인가를 선택하려고 할때 검색을 통해서 내가 공부하려는 DB를 선정하여 공부를 해보자! 관계형 데이터 베이스를 기본적으로 진행을 하고 다른 방식의 데이터 베이스를 공부하면서 데이터 베이스에 대한 고정관념을 부수고 더 시야를 넓히는 것이 중요하다!
		- Oracle : 관공서, 대기업에서 많이 사용한다.
		- MySQL : 개인 혹은 스타트업 같은 곳에서는 많이 사용한다. ⭐⭐⭐⭐:FasStarHalfStroke:
		- MongoDB : 다양한 데이터가 등장함에 따라 관계형 데이터 베이스가 문제가 될 수 있는 흐름에서 NoSQL 같은 방향도 있다.


## 🚩 What is MySQL?

### :TiLayoutSidebar: Relational Database(skima) - MySQL(Structured Query Language)

##### 📗 Set-up
1. `cd /usr/local/mysql/bin/`
2. mysql -uroot : 나는 지금부터 mysql을 사용한다!라는 의미와 같다. / 이것은 완전한 권한을 가져가는 것이기 때문에 정말 개발을 진행할 때에는 다른 방법으로 진행을 한다.
3. `mysql>` 과 같은 형태가 나오면 성공이다!
4. schema라는 것은 여러가지의 데이터를 하나로 묶은 것을 우리가 DataBase라고 하는데 그것을 다른 이름으로 스키마라고 명명한다.

##### 📗 Structure of mySql![[Screenshot 2023-11-06 at 10.44.24 PM.png]]
DataBaseServer -> Database(Schema) -> Table ![[Screenshot 2023-11-06 at 10.44.24 PM.png]]
- Build DB : `CREATE DATABASE ${name}`  <- ->  `DROP DATABASE ${name}`
```mysql
mysql> CREATE DATABASE jake;
Query OK, 1 row affected (0.00 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| jake               |
| mysql              |
| performance_schema |
| phpmyadmin         |
| sys                |
+--------------------+
6 rows in set (0.00 sec)

mysql> USE jake;
Database changed
```
![[Screenshot 2023-11-06 at 10.54.31 PM.png]]

##### 📗 How to make a table in mySQL?
	![[mysql-cheat-sheet-a4.pdf]]
	`id INT(11) NOT NULL AUTO_INCREMENT`  Not null은 빈 값이 들어오면 안된다는 의미하고, auto_increment는 자동으로 숫자가 증가하게 되어 중복을 방지한다.
	
	
```mysql
mysql> CREATE TABLE topic(
    -> id INT(11) NOT NULL AUTO_INCREMENT,
    -> title VARCHAR(100) NOT NULL,
    -> description TEXT NULL, 
    -> created DATETIME NOT NULL, 
    -> author VARCHAR(15) NULL, 
    -> profile VARCHAR(200) NULL 
    -> );

Query OK, 0 rows affected (0.02 sec)
```
위가 기본적으로 만들어야하는 database 의 양식이다. 여기서 제일 중요한 부분은 :TiAlertTriangleFilled:PRIMARY KEY를 정하여 데이터베이스를 정리하고 구분하는데 중요하게 작용하여 중복을 방지하는 등의 역할을 한다.  위의 작업은 주로하는 작업이 아니고 이러한 데이터 베이스를 처리하는 방법이 중요하기 때문에 특성을 이해를 해야한다.

-  위의 테이블을 만들때 입력이 되는 데이터 타입을 강제함으로써 내가 데이터를 정리하는데 훨씬 용이하게 진행할 수 있다. 하지만, 이러한 데이터타입을 정할때는 수용하려는 데이터에 최댓값에 가장 수렴하는 값을 선정하여 데이터타입, 그 데이터의 길이를 정하는 것의 중요성을 알 수 있다. 
-  데이터베이스를 다루는데 있어 중요한 능력은 db를 직접 빠르게 만드는것도 중요하지만, 내가 필요한 것을 정확하게 검색하여 찾을 수 있어야 한다.
Main reference : https://dev.mysql.com/doc/refman/8.0/en/create-table.html


##### 📗 Insert(CREATE)
```mysql
mysql> SHOW DATABASES
    -> ;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| jake               |
| mysql              |
| performance_schema |
| phpmyadmin         |
| sys                |
+--------------------+
6 rows in set (0.00 sec)

mysql> SHOW TABLES;
+----------------+
| Tables_in_jake |
+----------------+
| main           |
| topic          |
+----------------+
2 rows in set (0.00 sec)

mysql> DESC topic;
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | int(11)      | NO   | PRI | NULL    | auto_increment |
| title       | varchar(100) | NO   |     | NULL    |                |
| description | text         | YES  |     | NULL    |                |
| created     | datetime     | NO   |     | NULL    |                |
| author      | varchar(15)  | YES  |     | NULL    |                |
| profile     | varchar(200) | YES  |     | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
6 rows in set (0.01 sec)

mysql> INSERT INTO topic (title,description,created,author,profile) VALUES('MySQL', 'MYSQL is ...',NOW(),'jake','student')
    -> ;
Query OK, 1 row affected (0.01 sec)

mysql> SELECT * FROM topic ;
+----+-------+--------------+---------------------+--------+---------+
| id | title | description  | created             | author | profile |
+----+-------+--------------+---------------------+--------+---------+
|  1 | MySQL | MYSQL is ... | 2023-11-07 07:14:17 | jake   | student |
+----+-------+--------------+---------------------+--------+---------+
1 row in set (0.00 sec)

mysql> INSERT INTO topic (title,description,created,author,profile) VALUES('ORACLE', 'ORACLE is ...',NOW(),'jake','student');
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM topic ;                                                                          
+----+--------+---------------+---------------------+--------+---------+
| id | title  | description   | created             | author | profile |
+----+--------+---------------+---------------------+--------+---------+
|  1 | MySQL  | MYSQL is ...  | 2023-11-07 07:14:17 | jake   | student |
|  2 | ORACLE | ORACLE is ... | 2023-11-07 07:15:10 | jake   | student |
+----+--------+---------------+---------------------+--------+---------+
2 rows in set (0.00 sec)

mysql> INSERT INTO topic (title,description,created,author,profile) VALUES('MongoDB', 'MongoDB is ...',NOW(),'jake','student');
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM topic ;                                                                          
+----+---------+----------------+---------------------+--------+---------+
| id | title   | description    | created             | author | profile |
+----+---------+----------------+---------------------+--------+---------+
|  1 | MySQL   | MYSQL is ...   | 2023-11-07 07:14:17 | jake   | student |
|  2 | ORACLE  | ORACLE is ...  | 2023-11-07 07:15:10 | jake   | student |
|  3 | MongoDB | MongoDB is ... | 2023-11-07 07:15:59 | jake   | student |
+----+---------+----------------+---------------------+--------+---------+
3 rows in set (0.00 sec)
```


##### 📗 SELECT(READ)
```mysql
mysql> SELECT * FROM topic ;                                                                          
+----+--------+---------------+---------------------+--------+---------+
| id | title  | description   | created             | author | profile |
+----+--------+---------------+---------------------+--------+---------+
|  1 | MySQL  | MYSQL is ...  | 2023-11-07 07:14:17 | jake   | student |
|  2 | ORACLE | ORACLE is ... | 2023-11-07 07:15:10 | jake   | student |
+----+--------+---------------+---------------------+--------+---------+
2 rows in set (0.00 sec)

mysql> INSERT INTO topic (title,description,created,author,profile) VALUES('MongoDB', 'MongoDB is ...',NOW(),'jake','student');
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM topic ;                                                                          
+----+---------+----------------+---------------------+--------+---------+
| id | title   | description    | created             | author | profile |
+----+---------+----------------+---------------------+--------+---------+
|  1 | MySQL   | MYSQL is ...   | 2023-11-07 07:14:17 | jake   | student |
|  2 | ORACLE  | ORACLE is ...  | 2023-11-07 07:15:10 | jake   | student |
|  3 | MongoDB | MongoDB is ... | 2023-11-07 07:15:59 | jake   | student |
+----+---------+----------------+---------------------+--------+---------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM topic; 
+----+---------+----------------+---------------------+--------+---------+
| id | title   | description    | created             | author | profile |
+----+---------+----------------+---------------------+--------+---------+
|  1 | MySQL   | MYSQL is ...   | 2023-11-07 07:14:17 | jake   | student |
|  2 | ORACLE  | ORACLE is ...  | 2023-11-07 07:15:10 | jake   | student |
|  3 | MongoDB | MongoDB is ... | 2023-11-07 07:15:59 | jake   | student |
+----+---------+----------------+---------------------+--------+---------+
3 rows in set (0.00 sec)

mysql> SELECT id, title, created, author FROM topic;
+----+---------+---------------------+--------+
| id | title   | created             | author |
+----+---------+---------------------+--------+
|  1 | MySQL   | 2023-11-07 07:14:17 | jake   |
|  2 | ORACLE  | 2023-11-07 07:15:10 | jake   |
|  3 | MongoDB | 2023-11-07 07:15:59 | jake   |
+----+---------+---------------------+--------+
3 rows in set (0.00 sec)

mysql> INSERT INTO topic (title,description,created,author,profile) VALUES('NodeJS', 'NodeJS is ...',NOW(),'bean','student');
Query OK, 1 row affected (0.00 sec)

mysql> SELECT id, title, created, author FROM topic WHERE author = 'bean';
+----+--------+---------------------+--------+
| id | title  | created             | author |
+----+--------+---------------------+--------+
|  4 | NodeJS | 2023-11-07 07:19:28 | bean   |
+----+--------+---------------------+--------+
1 row in set (0.01 sec)

mysql> SELECT id, title, created, author FROM topic ORDER BY id DESC; 
+----+---------+---------------------+--------+
| id | title   | created             | author |
+----+---------+---------------------+--------+
|  4 | NodeJS  | 2023-11-07 07:19:28 | bean   |
|  3 | MongoDB | 2023-11-07 07:15:59 | jake   |
|  2 | ORACLE  | 2023-11-07 07:15:10 | jake   |
|  1 | MySQL   | 2023-11-07 07:14:17 | jake   |
+----+---------+---------------------+--------+
4 rows in set (0.00 sec)

mysql> SELECT id, title, created, author FROM topic ORDER BY id DESC LIMIT 2;
+----+---------+---------------------+--------+
| id | title   | created             | author |
+----+---------+---------------------+--------+
|  4 | NodeJS  | 2023-11-07 07:19:28 | bean   |
|  3 | MongoDB | 2023-11-07 07:15:59 | jake   |
+----+---------+---------------------+--------+
2 rows in set (0.00 sec)
```

##### 📗 UPDATE
```mysql
mysql> UPDATE topic SET description = 'ORACLE is ~~~', title = 'Oracle' WHERE id = 2; 
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM topic;
+----+---------+----------------+---------------------+--------+---------+
| id | title   | description    | created             | author | profile |
+----+---------+----------------+---------------------+--------+---------+
|  1 | MySQL   | MYSQL is ...   | 2023-11-07 07:14:17 | jake   | student |
|  2 | Oracle  | ORACLE is ~~~  | 2023-11-07 07:15:10 | jake   | student |
|  3 | MongoDB | MongoDB is ... | 2023-11-07 07:15:59 | jake   | student |
|  4 | NodeJS  | NodeJS is ...  | 2023-11-07 07:19:28 | bean   | student |
+----+---------+----------------+---------------------+--------+---------+
4 rows in set (0.00 sec)

mysql> UPDATE topic SET description = 'MySQL is ~~~', author = 'bean' WHERE id = 1;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM topic;
+----+---------+----------------+---------------------+--------+---------+
| id | title   | description    | created             | author | profile |
+----+---------+----------------+---------------------+--------+---------+
|  1 | MySQL   | MySQL is ~~~   | 2023-11-07 07:14:17 | bean   | student |
|  2 | Oracle  | ORACLE is ~~~  | 2023-11-07 07:15:10 | jake   | student |
|  3 | MongoDB | MongoDB is ... | 2023-11-07 07:15:59 | jake   | student |
|  4 | NodeJS  | NodeJS is ...  | 2023-11-07 07:19:28 | bean   | student |
+----+---------+----------------+---------------------+--------+---------+
4 rows in set (0.00 sec)
```

##### 📗 DELETE
```mysql
mysql> DELETE FROM topic WHERE id = 4; 
Query OK, 1 row affected (0.01 sec)

mysql> SELECT * FROM topic;
+----+---------+----------------+---------------------+--------+---------+
| id | title   | description    | created             | author | profile |
+----+---------+----------------+---------------------+--------+---------+
|  1 | MySQL   | MySQL is ~~~   | 2023-11-07 07:14:17 | bean   | student |
|  2 | Oracle  | ORACLE is ~~~  | 2023-11-07 07:15:10 | jake   | student |
|  3 | MongoDB | MongoDB is ... | 2023-11-07 07:15:59 | jake   | student |
+----+---------+----------------+---------------------+--------+---------+
3 rows in set (0.00 sec)
```

특별히 주의해야 할 것은 여기서 DB를 수정하는 단계에서 `WHERE`에 대한 내용을 제대로 기입하지 않으면 정말 인생이 끝날 수 있기 때문에 매우 주의해야 한다.


[[More Details about DB_egoing]]












