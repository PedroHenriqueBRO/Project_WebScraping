from WebScrapingCountries.DbConnection.DbConnection import Conn
class RepositorySouthCountries:
    def __init__(self):
        self.conn=Conn()
        self.cursor=self.conn.conn.cursor()
    def createtable(self):
        self.droptable()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS SouthCountries(
            id SERIAL PRIMARY KEY ,
            nome varchar(50),
            area NUMERIC(10,1),
            populacao BIGINT
            );
            """)
        print("Tabela criada com sucesso!")
        self.conn.conn.commit()

    def insert(self,pais,area,populacao):
        self.cursor.execute("""
        INSERT INTO SouthCountries(nome,area,populacao) VALUES(%s,%s,%s);
        """,(pais,area,populacao))
        self.conn.conn.commit()
    def droptable(self):
        self.cursor.execute("""
            DROP TABLE IF EXISTS SouthCountries;
            """)
        self.conn.conn.commit()

    def getall(self):
        self.cursor.execute("""
    SELECT * from SouthCountries;
    """)
        self.conn.conn.commit()
        dados=self.cursor.fetchall()
        return dados
    def close(self):
        self.conn.conn.close()
        self.cursor.close()