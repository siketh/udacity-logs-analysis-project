import psycopg2
from logs_analysis_exceptions import PrintException, PsqlDbException
from psycopg2.extras import DictCursor


class PsqlDb:
    '''
        PsqlDb provides convenient wrapper functions for connecting to and
        executing queries on a PostgreSQL database via psycopg2.
    '''

    def __init__(self, database_name):
        '''
            Instantiate a PsqlDb with database name. This name will
            be used for all connections made by this instance.

            args:
                database_name - a string. The name of the database to
                connect to.
        '''
        self.database_name = database_name

    def connect(self):
        '''
            Creates a connection to the database. Raises an error if the
            connection fails for any reason.

            returns:
                connection, cursor - a tuple. The database connection
                and cursor instance. The cusor is formatted to return
                dictionaries rather than tuples.

            raises:
                PsqlDbException - If the connection fails for any reason.
        '''

        print('Attempting to connect to database: {}'
              .format(self.database_name))

        try:
            connection = psycopg2.connect('dbname={}'.format(
                self.database_name), cursor_factory=DictCursor)
            cursor = connection.cursor()

            print('Connected successfully!')
            return connection, cursor
        except psycopg2.Error as e:
            msg = 'Failed to connect!'

            print(msg)
            raise PsqlDbException(msg, e)

    def query(self, query_string):
        '''
            Connects to the database, performs a query, and then closes then
            connection.

            args:
                query_string - a string. An SQL query statement.

            returns:
                results - a list of dictionaries. A list of column name ->
                index mappings.

            raises:
                PsqlDbException - If the query fails for any reason.
        '''
        connection, cursor = self.connect()

        try:
            print('Attempting to execute query...')
            query = cursor.execute(query_string)
            results = cursor.fetchall()

            print('Query successful!')
            return results
        except psycopg2.Error as e:
            msg = 'Failed to execute query!'

            print(msg)
            raise PsqlDbException(msg, e)
        finally:
            print('Closing connection...')
            connection.close()
