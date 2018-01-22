/*
  This file crews the views needed by the news database log generator.
*/

create view failed_requests_by_date_view as
select
  date(time) as error_date, count(time) as num_errors
from
  log
where
  status like '4%'
  or status like '5%'
group by error_date
order by error_date asc;


create view total_requests_by_date_view as
select
  date(time) as request_date, count(time) as num_requests
from
  log
group by request_date
order by request_date asc;
