/*
given yearly data for transactions, count balance at the end of year.
1. Get the total sum of transactions
2. deduct 5 for every month in case user does not make 3 cc transactions and those transactions need to add at least $100
3. negative amounts are cc card payments
4. positive amounts are incoming transafer
5. Get balance at the year end.
6. date is assured to be between 2020-01-01 to 2020-12-31
7. amount only contains non-zero values
*/


create table transactions (
        amount integer not null,
        date date not null
  );
  
 
insert into transactions values ('1000', '2020-01-06');
insert into transactions values ('-10', '2020-01-14');
insert into transactions values ('-75', '2020-01-20');
insert into transactions values ('-5', '2020-01-25');
insert into transactions values ('-4', '2020-01-29');
insert into transactions values ('2000', '2020-03-10');
insert into transactions values ('-75', '2020-03-12');
insert into transactions values ('-20', '2020-03-15');
insert into transactions values ('40', '2020-03-15');
insert into transactions values ('-50', '2020-03-17');
insert into transactions values ('200', '2020-10-10');
insert into transactions values ('-200', '2020-10-10');

delete from transactions;

INSERT INTO transactions (amount, date) VALUES ('1', '2020-06-29');
INSERT INTO transactions (amount, date) VALUES ('35', '2020-02-20');
INSERT INTO transactions (amount, date) VALUES ('-50', '2020-02-03');
INSERT INTO transactions (amount, date) VALUES ('-1', '2020-02-26');
INSERT INTO transactions (amount, date) VALUES ('-200', '2020-08-01');
INSERT INTO transactions (amount, date) VALUES ('-44', '2020-02-07');
INSERT INTO transactions (amount, date) VALUES ('-5', '2020-02-25');
INSERT INTO transactions (amount, date) VALUES ('1', '2020-06-29');
INSERT INTO transactions (amount, date) VALUES ('1', '2020-06-29');
INSERT INTO transactions (amount, date) VALUES ('-100', '2020-12-29');
INSERT INTO transactions (amount, date) VALUES ('-100', '2020-12-30');
INSERT INTO transactions (amount, date) VALUES ('-100', '2020-12-31');

delete from transactions;

INSERT INTO transactions (amount, date) VALUES ('6000', '2020-04-03');
INSERT INTO transactions (amount, date) VALUES ('5000', '2020-04-02');
INSERT INTO transactions (amount, date) VALUES ('4000', '2020-04-01');
INSERT INTO transactions (amount, date) VALUES ('3000', '2020-03-01');
INSERT INTO transactions (amount, date) VALUES ('2000', '2020-02-01');
INSERT INTO transactions (amount, date) VALUES ('1000', '2020-01-01');

delete from transactions;




-- CTE will get me the records for months in which the user should not be charged $5 for Credit card
-- Once we have CTE, use the count to get number of total records for the year and use Math formula to get balance
-- Sum(amount) - (12 months * $5) + ($5 for count of months/records from CTE)
WITH month_count_CTE AS(
    select sum(amount) as total_cc_cost, count(amount) as total_cc_transaction_count, to_char(date, 'MM') as month
    from transactions
    where amount < 0 
    group by to_char(date, 'MM')
	having sum(amount) < -99 and count(amount) > 2
)
--select count(*) from month_count_CTE;
--select * from month_count_CTE;
--SELECT (SUM(amount) - (12*5) + (5* (select count(*) from month_count_CTE))) as balance FROM transactions;
SELECT (COALESCE(SUM(amount),0) - (12*5) + (5* COALESCE((select count(*) from month_count_CTE),0))) as balance FROM transactions;

--SELECT (SUM(amount)) as balance FROM transactions;

--delete from transactions;