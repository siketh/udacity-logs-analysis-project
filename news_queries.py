#!/usr/bin/env python3
"""This file contains PostgreSQL query strings for the News table."""


top_three_articles = '''
SELECT
    articles.title,
    COUNT(*) AS num_views
FROM
    articles, log
WHERE
    (log.path='/article/' || articles.slug)
GROUP BY
    articles.title
ORDER BY
    num_views DESC
LIMIT 3;
'''

author_id_num_views = '''
SELECT
    articles.author,
    COUNT(*) AS num_views
FROM
    log,
    articles
WHERE
    (log.path='/article/' || articles.slug)
GROUP BY
    articles.author
ORDER BY
    num_views DESC
'''

top_authors = '''
SELECT
    authors.name,
    num_views
FROM
    ({}) AS author_id_num_views,
    authors
WHERE
    author_id_num_views.author = authors.id
'''.format(author_id_num_views)

errors_over_one_percent = '''
SELECT
    request_date,
    percent_errors * 100 AS percent_errors
FROM (
    SELECT
        request_date,
        CAST(tf.num_errors AS float) / tr.num_requests AS percent_errors
    FROM
        total_requests_by_date_view AS tr,
        failed_requests_by_date_view AS tf
    WHERE
        tr.request_date = tf.error_date) AS all_percent_errors
WHERE
    percent_errors > .01;
'''
