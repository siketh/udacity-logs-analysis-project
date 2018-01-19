''' This file contains PostgreSQL query strings for the News table '''

greater_than_one_percent_request_errors_query = """
select
request_date, percent_errors * 100 as percent_errors
from (
    select
    request_date,
    cast(tf.num_errors as float) / tr.num_requests as percent_errors
    from total_requests_by_date_view as tr, failed_requests_by_date_view as tf
    where tr.request_date = tf.error_date) as all_percent_errors
where percent_errors > .01;
"""

top_three_most_accessed_articles_query = """
select
article_title, count(article_title) as num_views
from
successfully_accessed_articles_view
group by article_title
order by num_views desc
limit 3;
"""

author_title_views_subquery = """
select
article_author, article_title, count(article_title) as num_views
from
successfully_accessed_articles_view
group by article_author, article_title
order by num_views desc
"""

most_accessed_articles_by_author_query = """
select
article_author, max(num_views) as highest_num_views
from ({}) as author_title_num_views
group by article_author
order by highest_num_views desc;
""".format(author_title_views_subquery)
