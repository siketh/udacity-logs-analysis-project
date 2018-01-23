#!/usr/bin/env python3
"""Exceptions that can occur while printing tables and querying the DB."""


class PrintException(Exception):
    """Raise when an error occurs while trying to print SQL results."""

    def __init__(self, results, result_headers, msg=None, exception=None):
        """Create a new instance of PrintException.

        Args:
            results (list[dict]): The results of the query.
            result_headers (list[str]): The headers to print.
            msg (str, optional): The message to display with the exception.
                Defaults to None.
            exception (Exception, optional): The original exception thrown.
                Defaults to None.
        """
        if msg is None:
            msg = '''
            An error occured while trying to print SQL results.
            Result Headers:
            {}
            Results:
            {}
            '''.format(result_headers, results)
        if exception is not None:
            msg + (': {}').format(exception)
        super(PrintException, self).__init__(msg)
        self.results = results
        self.result_headers = result_headers
        self.original_exception = exception


class PsqlDbException(Exception):
    """Raise when an error occurs while interacting with the PostgreSQL DB."""

    def __init__(self, msg=None, exception=None):
        """Create a new instance of PsqlDbException.

        Args:
            msg (str, optional): The message to display with the exception.
                Defaults to None.
            exception (Exception, optional): The original exception thrown.
                Defaults to None.
        """
        if msg is None:
            msg = 'An error occurred while interacting with the PostgreSQL '
            'database'
        if exception is not None:
            msg + (': {}').format(exception)
        super(PsqlDbException, self).__init__(msg)
        self.original_exception = exception
