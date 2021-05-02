# Standard library
import os

# Third imports
import sqlite3

class CreateEuroNationsDB:
    """
    Class to modify the euronations.db
    """
    def __init__(self, db: str = "euronations.db"):
        self.db = sqlite3.connect(db)

    def create_new_db(self):
        """
        Function to create a new database with sqlite
        """
        cur = self.db.cursor()
        # Nations Table
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS nations(
            id serial PRIMARY KEY,
            nation TEXT NOT NULL
            );
            """
        )

        # Cities Table
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS cities (
            id serial PRIMARY KEY,
            city text NOT NULL,
            capitol boolean,
            population integer NOT NULL,

            nation_id integer NOT NULL,
            FOREIGN KEY (nation_id) REFERENCES nations(id) ON DELETE CASCADE
            );
            """
        )

        # Organization Table
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS organizations (
            id serial PRIMARY KEY,
            EU boolean NOT NULL,
            NATO boolean NOT NULL,
            commonwealth boolean NOT NULL,

            nation_id integer NOT NULL,
            FOREIGN KEY (nation_id) REFERENCES nations(id) ON DELETE CASCADE
            );
            """
        )

        self.db.commit()
        self.db.close()


if __name__ == "__main__":
    cdb = CreateEuroNationsDB()
    cdb.create_new_db()