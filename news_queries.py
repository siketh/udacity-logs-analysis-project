''' This file contains PostgreSQL query strings for the News table '''


top_three_articles = '''
select
    articles.title, count(*) as num_views
from
    articles, log
where
    (log.path='/article/' || articles.slug)
group by articles.title
order by num_views desc
limit 3;
'''

author_id_num_views = '''
select
    articles.author, count(*) as num_views
from
    log,
    articles
where
    (log.path='/article/' || articles.slug)
group by articles.author
order by num_views desc
'''

top_authors = '''
select
    authors.name,
    num_views
from
    ({}) as author_id_num_views,
    authors
where
    author_id_num_views.author = authors.id
'''.format(author_id_num_views)

errors_over_one_percent = '''
select
    request_date,
    percent_errors * 100 as percent_errors
from (
    select
        request_date,
        cast(tf.num_errors as float) / tr.num_requests as percent_errors
    from total_requests_by_date_view as tr, failed_requests_by_date_view as tf
        where tr.request_date = tf.error_date) as all_percent_errors
where
    percent_errors > .01;
'''
