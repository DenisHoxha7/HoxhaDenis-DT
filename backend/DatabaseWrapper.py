import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseWrapper:
    def __init__(self):
        self.config = {
            'host': os.getenv("DB_HOST"),
            'port': int(os.getenv("DB_PORT")),
            'user': os.getenv("DB_USER"),
            'password': os.getenv("DB_PASSWORD"),
            'database': os.getenv("DB_NAME"),
            'cursorclass': pymysql.cursors.DictCursor
        }

    def _get_connection(self):
        return pymysql.connect(**self.config)

    def init_table(self):
        """Crea la tabella deliveries se non esiste"""
        query = """
        CREATE TABLE IF NOT EXISTS deliveries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tracking_code VARCHAR(50) NOT NULL UNIQUE,
            destinatario VARCHAR(100) NOT NULL,
            indirizzo VARCHAR(255) NOT NULL,
            fascia_oraria VARCHAR(50) NOT NULL,
            stato VARCHAR(30) DEFAULT 'READY',
            priorita VARCHAR(20) DEFAULT 'LOW'
        )
        """
        conn = self._get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query)
            conn.commit()
            print("Tabella pronta!")
        finally:
            conn.close()

# Test rapido
if __name__ == "__main__":
    db = DatabaseWrapper()
    db.init_table()