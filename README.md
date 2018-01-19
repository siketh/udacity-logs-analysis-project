# udacity-logs-analysis-project

## Logs Analysis

## Overview

Simple script for querying data in a PostgreSQL database containing information about the authors, articles, and server logs of a news website.

* queries.py contains the SQL query strings.
* views.py contains the SQL view strings.
* log.py is a script that connects to the news database, creates the views, then runs the queries and generates the log.

## Dependencies

These instructions assume you already have the news database set up on your machine or a VM. If you are running a VM you will have to clone the repository somewhere that your VM can see it and follow the set up instructions from your VM rather than your actual machine.

## Views

A few views are implemented to simplify queries. log.py will attempt to create or replace the views automatically, but if you would prefer to create the views yourself they are below for your convenience:

```
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
```

```
create or replace view failed_requests_by_date_view as
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
create or replace view total_requests_by_date_view as
  select
    date(time) as request_date, count(time) as num_requests
  from
    log
  group by request_date
  order by request_date asc;
```

## Set-up

The following instructions are for Ubuntu Linux. If your database is on a VM you will have to do the folloing in that VM.

1. Install `git`
2. Clone the repo: `git clone https://github.com/siketh/udacity-logs-analysis-project.git`
3. Install `python3`
4. Install `pip3`
5. Open a terminal inside the udacity-portfolio-site repository
6. Run `pip3 install -r requirements.txt` to install psycopg2 and tabulate

## Usage

1. Open a terminal inside the udacity-portfolio-site repository
2. Run `python3 logs.py`
3. In the terminal you will see a log containing the results of various queries

## Example Output

```
Generating log for the news database...

Getting top 3 most viewed articles of all-time...

+----------------------------------+-------------------+
| Article Title                    |   Number of Views |
|----------------------------------+-------------------|
| Candidate is jerk, alleges rival |            338647 |
| Bears love berries, alleges bear |            253801 |
| Bad things gone, say good people |            170098 |
+----------------------------------+-------------------+

Getting most popular article authors of all-time...

+------------------------+---------------------------------------+
| Author Name            |   Most Viewed Article Number of Views |
|------------------------+---------------------------------------|
| Rudolf von Treppenwitz |                                338647 |
| Ursula La Multa        |                                253801 |
| Anonymous Contributor  |                                170098 |
| Markoff Chaney         |                                 84557 |
+------------------------+---------------------------------------+

Getting days with request errors exceeding 1% of total requests...

+------------+------------------------+
| Date       |   % of Failed Requests |
|------------+------------------------|
| 2016-07-17 |                2.26269 |
+------------+------------------------+
```

## License

[MIT](LICENSE.md)
