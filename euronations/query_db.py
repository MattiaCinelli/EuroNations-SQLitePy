# Standard library
import os

# Third imports
import random
import sqlite3
import numpy as np
import pandas as pd

class QueryDB:
    """
    Download the db an save it in csv.
    """
    def __init__(self, db: str = "euronations.db"):
        self.db = sqlite3.connect(db)

    def get_euronations(self, suject:str = None, topic:str = None, number:int = 0):
        df = pd.read_sql_query(
            f'''
            SELECT n.nation, c.city, c.capitol, c.population, o.EU, o.NATO, o.commonwealth
            FROM nations as n
            INNER JOIN cities as c 
            ON c.nation_id = n.id
            INNER JOIN organizations as o
            ON c.nation_id = n.id
            ''', # WHERE q.level='{topic}';
            self.db)

        # print(result)
        df.to_csv('euronations.csv')


if __name__ == "__main__":
    gt = QueryDB()
    gt.get_euronations()