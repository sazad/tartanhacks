CREATE TABLE textbooks (
	email varchar(40),
	courseNum varchar(10),
	bookName varchar(100),
	price DECIMAL(10, 5)
);

drop table textbooks
 
select * from textbooks;

ALTER TABLE textbooks 
ALTER column 