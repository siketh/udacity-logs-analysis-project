#!/usr/bin/env python3
"""This module is an executable script for generating logs from a database."""

import argparse
import sys
import types

import news_queries
from logs_analysis_exceptions import PrintException, PsqlDbException
from psql_db import PsqlDb
from tabulate import tabulate

NEWS_DATABASE = 'news'


def print_results(results={}, result_headers=[]):
    """Print the results as a PSQL formatted table.

    Args:
        results(list[dict]): The list of results returned by the query.
            Defaults to an empty dict.
        result_headers(list[str]): The column headers for the table.
            Defaults to an empty list.
    Raises:
        PrintException: If the results cannot be printed for any reason

    """
    resultsIsList = isinstance(results, list)
    headersIsList = isinstance(result_headers, list)

    if result_headers == []:
        raise PrintException(results, result_headers,
                             'No headers specifed, cannot print table!')
    if not resultsIsList or not headersIsList:
        raise PrintException(results, result_headers,
                             'Results or headers are not of the correct type')

    try:
        print(tabulate(results, headers=result_headers, tablefmt='psql'))
    except TypeError as e:
        raise PrintException(results, result_headers, exception=e)


def print_top_three_articles():
    """Print the top three articles of all time."""
    print('Retrieving top three articles of all time...')

    news_db = PsqlDb(NEWS_DATABASE)

    results = news_db.query(news_queries.top_three_articles)
    headers = ['Article Title', 'Article Views']

    print_results(results, headers)


def print_top_authors():
    """Print authors ranked by article views."""
    print('Retrieving authors ranked by article views...')

    news_db = PsqlDb(NEWS_DATABASE)

    results = news_db.query(news_queries.top_authors)
    headers = ['Author Name', 'Article Views']

    print_results(results, headers)


def print_errors_over_one_percent():
    """Print days where more than one percent of total requests were errors."""
    print('Retrieving days where more than one percent of total '
          'requests were errors')

    news_db = PsqlDb(NEWS_DATABASE)

    results = news_db.query(news_queries.errors_over_one_percent)
    headers = ['Date', '% of Requests Failed']

    print_results(results, headers)


def generate_news_log(debug_mode=False):
    """Print results of several queries on the news database.

    Args:
        debug_mode(bool, optional) - Exceptions will be printed if True.
            Defaults to False.
    Raises:
        PrintException: If an error occurs while printing query results.
        PsqlDbException: If an error occurs while interating with the database

    """
    try:
        print_top_three_articles()
        print_top_authors()
        print_errors_over_one_percent()
    except (PrintException, PsqlDbException) as e:
        if(debug_mode):
            raise e
        else:
            print('An exception ocurred during log generation. Terminating.')
            sys.exit(1)


if __name__ == '__main__':
    """Parse command line arguments to determine database to generate logs for.

    usage: logs_analysis.py [-h] [-d] {news}
    """
    parser = argparse.ArgumentParser(description='Generate a log of '
                                     'interesting information about the '
                                     'specified database.')
    parser.add_argument('-d', '--debug', help='Print exceptions to console',
                        action='store_true')
    parser.add_argument('database_name', type=str,
                        help='The name of the database to generate a log for',
                        choices=['news'])

    args = parser.parse_args()

    if args.database_name == NEWS_DATABASE:
        print('Generating logs for the {} database...'
              .format(args.database_name))
        generate_news_log(args.debug)
