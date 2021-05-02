# EuroNations-SQLitePy
<p align="center">
  <img src="https://github.com/MattiaCinelli/EuroNations-SQLitePy/blob/master/commons/banner.png" alt="Banner"  width="100%"/>
</p>

A database of the major European Nations created in SQLite and Python.

A portfolio example of the use of SQLite, SQL queries and interaction Python-SQL.

## Example
Import needed libraries
```python
# Standard library imports
import sqlite3

# Local imports
from euronations.create_db import CreateEuroNationsDB
from euronations.modify_db import ModifyDB
```

Create the data base
```python
cdb = CreateEuroNationsDB(db = "euronations.db")
cdb.create_new_db()
```

Add a first item
```python
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
```

<p align="center">
  <img src="https://github.com/MattiaCinelli/EuroNations-SQLitePy/blob/master/commons/sqlite_python.png" alt="Footer" width="100%"/>
</p>
