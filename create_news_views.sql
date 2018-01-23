/*
  This file creates the views needed by the news database log generator.
*/

CREATE OR REPLACE VIEW failed_requests_by_date_view AS
SELECT
    DATE(time) AS error_date,
    COUNT(time) AS num_errors
FROM
    log
WHERE
    status LIKE '4%'
    OR status LIKE '5%'
GROUP BY
    error_date
ORDER BY
    error_date ASC;

CREATE OR REPLACE VIEW total_requests_by_date_view AS
SELECT
    DATE(TIME) AS request_date,
    COUNT(time) AS num_requests
FROM
    log
GROUP BY
    request_date
ORDER BY
    request_date ASC;
