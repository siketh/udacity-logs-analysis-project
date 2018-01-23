# Logs Analysis

## Overview

Simple script for querying data in a PostgreSQL database containing information about the authors, articles, and server logs of a news website.

* news_queries.py contains SQL query strings for the news database.
* create_news_views.sql contains the SQL views to create for the news database before execution.
* psql_db.py is a module which provides a class with convenience methods for cleanly interacting with a PostgreSQL database via psycopg2.
* logs_analysis.py is a command line script that accepts a database name as an argument and generates a log of interesting information about that database. Currently the "news" database is the only database with logs implemented.

### Prerequisites

* The PostgreSQL news database on your computer or a VM
* [git](https://git-scm.com/downloads)
* [python3](https://www.python.org/downloads/)
* [pip3](https://pip.pypa.io/en/stable/installing/)


### Installation

The following instructions are for Ubuntu Linux. If your database is on a VM you will have to do the following in that VM.

1. Clone the repo: `git clone https://github.com/siketh/udacity-logs-analysis-project.git`
2. Open a terminal inside the udacity-portfolio-site repository
3. Run `pip3 install -r requirements.txt` to install psycopg2 and tabulate
4. Run `psql -d news -f create_news_views.sql` to create the views for the news database

### Usage

1. Open a terminal inside the udacity-portfolio-site repository
2. Run `python3 logs_analysis.py news`
3. In the terminal you will see a log containing the results of various queries
4. Run `python3 logs_analysis.py -d news`
5. In the terminal you will see the same log as before, but any exceptions that occur will now be printed as well.

```
usage: logs_analysis.py [-h] [-d] {news}

Generate a log of interesting information about the specified database.

positional arguments:
  {news}       The name of the database to generate a log for

optional arguments:
  -h, --help   show this help message and exit
  -d, --debug  Print exceptions to console

```

### Views

A few views are implemented to simplify queries. log.py will attempt to create or replace the views automatically, but if you would prefer to create the views yourself they are below for your convenience:

```
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
```

```
create view total_requests_by_date_view as
  select
    date(time) as request_date, count(time) as num_requests
  from
    log
  group by request_date
  order by request_date asc;
```

### License

[MIT](LICENSE.md)
