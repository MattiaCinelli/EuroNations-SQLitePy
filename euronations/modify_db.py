# Standard library imports
import os
import sys

# Third imports
import sqlite3
import pandas as pd
from typing import List

class ModifyDB:
    """
    Class to modify the euronations.db
    """
    def __init__(self, db: str = "euronations.db"):
        self.db = sqlite3.connect(db)

    def insert_in_db(
        self, 
        nation_name:str = None, 
        city_name:str = None, capitol:bool=False, population:int=0,
        EU:bool=False, NATO:bool=False, commonwealth:bool=False):
        """
        insert new value in the database
        """
        # ------------
        # Nation Table
        # ------------
        cur_n = self.db.cursor()
        cur_n.execute("""SELECT COUNT(id) FROM nations;""")
        size_of_n = str(cur_n.fetchall()[0][0] + 1)

        cur_n.execute(
        """
        INSERT INTO nations(id, nation)
        VALUES(?,?)""",
        (str(size_of_n), nation_name),
        )

        # ------------
        # Cities Table
        # ------------
        cur_c = self.db.cursor()
        cur_c.execute("""SELECT COUNT(city) FROM cities;""")
        size_of_c = str(cur_c.fetchall()[0][0] + 1)

        cur_c.execute(
            """
            INSERT INTO cities(id, nation_id, city, capitol, population)
            VALUES(?,?,?,?,?)""",
            (str(size_of_c), size_of_n, city_name, capitol, population), #str(rigth_wrong)
        )

        # ------------
        # Nation Table
        # ------------
        cur_o = self.db.cursor()
        cur_o.execute("""SELECT COUNT(id) FROM organizations;""")
        size_of_o = str(cur_o.fetchall()[0][0] + 1)

        cur_o.execute(
            """
            INSERT INTO organizations(id, nation_id, EU, NATO, commonwealth)
            VALUES(?,?,?,?,?)""",
            (str(size_of_o), size_of_n, EU, NATO, commonwealth),
        )

        self.db.commit()
