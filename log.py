#!/usr/bin/env python3

import psycopg2
import queries
import views
from psycopg2.extras import DictCursor
from tabulate import tabulate


def main():
    """ Run this file to generate logs of tabulated data from the news
    database """

    # Get the database connection / cursor for executing queries
    connection = psycopg2.connect("dbname=news", cursor_factory=DictCursor)
    cursor = connection.cursor()

    # Create (or replace) the necessary views
    cursor.execute(views.create_successfully_accessed_articles_view)
    cursor.execute(views.create_failed_requests_by_date_view)
    cursor.execute(views.create_total_requests_by_date_view)

    # Generate the log

    print('\nGenerating log for the news database...')

    print('\nGetting top 3 most viewed articles of all-time...\n')

    cursor.execute(queries.top_three_most_accessed_articles_query)
    all_results = cursor.fetchall()

    print(tabulate(all_results,
                   headers=[
                       'Article Title', 'Number of Views'],
                   tablefmt='psql'))

    print('\nGetting most popular article authors of all-time...\n')

    cursor.execute(queries.most_accessed_articles_by_author_query)
    all_results = cursor.fetchall()

    print(tabulate(all_results,
                   headers=[
                       'Author Name', 'Most Viewed Article Number of Views'],
                   tablefmt='psql'))

    print('\nGetting days with request errors '
          'exceeding 1% of total requests...\n')

    cursor.execute(queries.greater_than_one_percent_request_errors_query)
    all_results = cursor.fetchall()

    print(tabulate(all_results,
                   headers=['Date',
                            '% of Failed Requests'],
                   tablefmt='psql'))

    # Close the database connection
    connection.close()


if __name__ == "__main__":
    main()
