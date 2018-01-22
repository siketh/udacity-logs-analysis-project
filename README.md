# udacity-logs-analysis-project

## Logs Analysis

## Overview

Simple script for querying data in a PostgreSQL database containing information about the authors, articles, and server logs of a news website.

* news_queries.py contains SQL query strings for the news database.
* create_news_views.sql contains the SQL views to create for the news database before execution.
* psql_db.py is a module which provides a class with convenience methods for cleanly interacting with a PostgreSQL database via psycopg2.
* logs_analysis.py is a command line script that accepts a database name as an argument and generates a log of interesting information about that database. Currently the "news" database is the only database with logs implemented.

## Dependencies

These instructions assume you already have the news database set up on your machine or a VM. If you are running a VM you will have to clone the repository somewhere that your VM can see it and follow the set up instructions from your VM rather than your actual machine.

## Views

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

## Set-up

The following instructions are for Ubuntu Linux. If your database is on a VM you will have to do the following in that VM.

1. Install `git`
2. Clone the repo: `git clone https://github.com/siketh/udacity-logs-analysis-project.git`
3. Install `python3`
4. Install `pip3`
5. Open a terminal inside the udacity-portfolio-site repository
6. Run `pip3 install -r requirements.txt` to install psycopg2 and tabulate
7. Run `psql -d news -f create_news_views.sql` to create the views for the news database

## Usage

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

## Example Output

```
Generating logs for the news database...
Retrieving top three articles of all time...
Attempting to connect to database: news
Connected successfully!
Attempting to execute query...
Query successful!
Closing connection...
+----------------------------------+-----------------+
| Article Title                    |   Article Views |
|----------------------------------+-----------------|
| Candidate is jerk, alleges rival |          338647 |
| Bears love berries, alleges bear |          253801 |
| Bad things gone, say good people |          170098 |
+----------------------------------+-----------------+
Retrieving authors ranked by article views...
Attempting to connect to database: news
Connected successfully!
Attempting to execute query...
Query successful!
Closing connection...
+------------------------+-----------------+
| Author Name            |   Article Views |
|------------------------+-----------------|
| Ursula La Multa        |          507594 |
| Rudolf von Treppenwitz |          423457 |
| Anonymous Contributor  |          170098 |
| Markoff Chaney         |           84557 |
+------------------------+-----------------+
Retrieving days where more than one percent of total requests were errors
Attempting to connect to database: news
Connected successfully!
Attempting to execute query...
Query successful!
Closing connection...
+------------+------------------------+
| Date       |   % of Requests Failed |
|------------+------------------------|
| 2016-07-17 |                2.26269 |
+------------+------------------------+
```

## License

[MIT](LICENSE.md)
