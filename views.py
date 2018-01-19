''' This file contains PostgreSQL view strings for the News table '''


create_successfully_accessed_articles_view = """
create or replace view successfully_accessed_articles_view as
select
articles.title as article_title,
log.path as article_path,
authors.name as article_author
from
articles, log, authors
where
log.path like concat('/article/', articles.slug)
and log.status like '2%'
and articles.author = authors.id;
"""

create_failed_requests_by_date_view = """
create or replace view failed_requests_by_date_view as
select
date(time) as error_date, count(time) as num_errors
from log
where
status like '4%'
or status like '5%'
group by error_date
order by error_date asc;
"""

create_total_requests_by_date_view = """
create or replace view total_requests_by_date_view as
select
date(time) as request_date, count(time) as num_requests
from log
group by request_date
order by request_date asc;
"""
