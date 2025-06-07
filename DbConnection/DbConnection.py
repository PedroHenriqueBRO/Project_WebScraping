import psycopg2
class Conn:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="1234"
        )
        print("Conectado ao banco:", self.conn.get_dsn_parameters()['dbname'])

