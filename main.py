# Standard library imports
import os
import sqlite3

# Local imports
from euronations.create_db import CreateEuroNationsDB
from euronations.modify_db import ModifyDB

try:
    os.remove('euronations.db')
    print ("Old database deleted")
except FileNotFoundError:
    print('Create new database')
    

cdb = CreateEuroNationsDB()
cdb.create_new_db()

mdb = ModifyDB()

mdb.insert_in_db(
    # Nation
    nation_name = 'Italy', 

    # Major city
    city_name = 'Rome',
    capitol = True, 
    population = 2_783_809,

    # Organization 
    EU = True, 
    NATO = True, 
    commonwealth = False,
)

mdb.insert_in_db(
    nation_name = 'Italy', 
    city_name = 'Milan',
    capitol = False, 
    population = 1_397_715,
    EU = True, 
    NATO = True, 
    commonwealth = False,
)

mdb.insert_in_db(
    nation_name = 'United Kingdom',
    city_name = 'London',
    capitol = True, 
    population = 8_961_989,
    EU = False, 
    NATO = True, 
    commonwealth = True,
)

"""
mdb.insert_in_db(
    nation_name = , 
    city_name = ,
    capitol = False, 
    population = 0,
    EU = False, 
    NATO = False, 
    commonwealth = False,
)
"""