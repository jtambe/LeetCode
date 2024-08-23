/*
given yearly data for transactions, count balance at the end of year.
1. Get the total sum of transactions
2. deduct 5 for every month in case user does not make 3 cc transactions and those transactions need to add at least $100
3. negative amounts are cc card payments
4. positive amounts are incoming transafer
5. Get balance at the year end.
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
SELECT (SUM(amount) - (12*5) + (5* (select count(*) from month_count_CTE))) as balance FROM transactions;