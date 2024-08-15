import sys
import sqlite3
from pathlib import Path


# # # # Database stuff # # # #

def create_database():
    """
    creates the database 'telefonbuch' with a table 'telefonbuch'.\n
    the table has the following columns:\n
    first_name, last_name, phone_number, note.
    """
    conn = sqlite3.connect('telefonbuch.sqlite')
    c = conn.cursor()  # Der Cursor wird erstellt
    sql = """create table if not exists telefonbuch(
       id       integer
           constraint id
               primary key,
       first_name  TEXT,
       last_name TEXT,
       phone_number  TEXT,
       note TEXT);"""

    c.execute(sql)  # sql-Befehl wird ausgeführt
    conn.commit()
    conn.close()


def get_all_entries():
    """
    return value examples:
    [(1, 'Tine', 'Bagin', '0711', 'liebt Eis')]\n
    [(ID, Vorname, Nachname, Telefonnummer, Notiz),(...), ...]\n
    :param name: str name (vor- und nachname)
    :return: list[tuple]
    """
    conn = sqlite3.connect('telefonbuch.sqlite')
    c = conn.cursor()
    sql = """select * from telefonbuch"""
    ergebnis = c.execute(sql).fetchall()
    conn.close()
    return ergebnis

def add_entry(first_name:str, last_name:str, phone_number:str, note:str):
    """
    Add a new entry to the database 'telefonbuch':\n
    :param first_name: str first_name (Vorname)
    :param last_name: str last_name (Nachname)
    :param phone_number: str phone_number (Telefonnummer)
    :param note: str note (freie Notiz)
    """
    params = (first_name, last_name, phone_number, note)
    sql = """INSERT INTO telefonbuch (first_name, last_name, phone_number, note) VALUES (?,?,?,?)"""
    conn = sqlite3.connect("telefonbuch.sqlite")
    c = conn.cursor()
    c.execute(sql, params)
    conn.commit()
    conn.close()

def delete_entries_by_name(name: str):
    """
    Deletes all entries where first_name, or last_name like 'search input'
    :param name: str name (vor- und nachname)
    :return: int(count deleted rows)
    """
    count_deleted = 0
    all_entries = get_entries_by_name(name)
    for row in all_entries:
        count_deleted += delete_entry_by_id(row[0])
    return count_deleted

def delete_entry_by_id(id: int):
    """
    Delete row with given id from telefonbuch
    :param id: int
    :return: int (affected rows)
    """
    params = (id,)

    conn = sqlite3.connect('telefonbuch.sqlite')
    c = conn.cursor()
    sql = """DELETE FROM telefonbuch where id = ?"""

    affected = c.execute(sql, params).rowcount
    conn.commit()
    conn.close()

    return affected


def get_entries_by_name(name: str) -> list[tuple]:
    """
    return value examples:
    [(1, 'Tine', 'Bagin', '0711', 'liebt Eis')]\n
    [(ID, Vorname, Nachname, Telefonnummer, Notiz),(...), ...] \n
    :param name: str name (vor- und nachname)
    :return: list[tuple]
    """
    conn = sqlite3.connect('telefonbuch.sqlite')
    c = conn.cursor()
    such = f"%{name}%"
    params = (such, such)
    sql = """select * from telefonbuch where first_name like ? or last_name like ?"""
    ergebnis = c.execute(sql, params).fetchall()
    conn.close()
    return ergebnis


def test():
   pass

if __name__ == '__main__':
    test()
