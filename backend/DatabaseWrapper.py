import pymysql
import os
from dotenv import load_dotenv

# Carichiamo le variabili dal file .env
load_dotenv()

class DatabaseWrapper:
    def __init__(self):
        # Configurazione caricata da .env
        self.host = os.getenv("DB_HOST")
        self.port = int(os.getenv("DB_PORT"))
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.db_name = os.getenv("DB_NAME")

    def _get_connection(self):
        """Metodo privato per stabilire la connessione al DB"""
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.db_name,
            cursorclass=pymysql.cursors.DictCursor # Fondamentale per avere i dati come JSON
        )

    def init_database(self):
        """
        Crea la tabella 'deliveries' con i campi richiesti dalla traccia.
        VINCOLO: Query manuale CREATE TABLE.
        """
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
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
            connection.commit()
            print("Tabella 'deliveries' inizializzata!")
        finally:
            connection.close()

    def get_all_deliveries(self):
        """
        Recupera tutte le consegne.
        VINCOLO: Query manuale SELECT.
        """
        query = "SELECT * FROM deliveries"
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        finally:
            connection.close()

    def add_delivery(self, data):
        """
        Inserisce una nuova consegna.
        VINCOLO: Query manuale INSERT.
        """
        query = """
        INSERT INTO deliveries (tracking_code, destinatario, indirizzo, fascia_oraria, priorita)
        VALUES (%s, %s, %s, %s, %s)
        """
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, (
                    data['tracking_code'], 
                    data['destinatario'], 
                    data['indirizzo'], 
                    data['fascia_oraria'], 
                    data['priorita']
                ))
            connection.commit()
            return True
        finally:
            connection.close()

    def update_status(self, delivery_id, nuovo_stato):
        """
        Aggiorna lo stato di una consegna (Servirà per il commit 6).
        VINCOLO: Query manuale UPDATE.
        """
        query = "UPDATE deliveries SET stato = %s WHERE id = %s"
        connection = self._get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, (nuovo_stato, delivery_id))
            connection.commit()
            return True
        finally:
            connection.close()

# Blocco di test e inizializzazione
if __name__ == "__main__":
    db = DatabaseWrapper()
    db.init_database()