
class PrintException(Exception):
    '''
        Exception raised when an error occurs while trying to print
        SQL results
    '''

    def __init__(self, results, result_headers, msg=None, exception=None):
        ''' Creates a new instance of PrintException.'''
        if msg is None:
            msg = ''' An error occured while trying to print SQL results
            Result Headers:
            {}
            Results:
            {} '''.format(result_headers, results)
        if exception is not None:
            msg + (': {}').format(exception)
        super(PrintException, self).__init__(msg)
        self.results = results
        self.result_headers = result_headers
        self.original_exception = exception


class PsqlDbException(Exception):
    '''
        Exception raised when an error occurs while interacting with the
        PostgreSQL database
    '''

    def __init__(self, msg=None, exception=None):
        ''' Creates a new instance of PsqlDbException. '''

        if msg is None:
            msg = 'An error occurred while interacting with the PostgreSQL '
            'database'
        if exception is not None:
            msg + (': {}').format(exception)
        super(PsqlDbException, self).__init__(msg)
        self.original_exception = exception
