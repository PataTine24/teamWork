import sys
import sqlite3
from pathlib import Path


# # # # Database stuff # # # #

def create_database():
    """Diese Funktion erstellt eine neue Datenbank"""
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


def get_all_entrys():
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
    Hinzufügen von Einträgen in die Datenbank 'Telefonbuch':\n
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

def delete_entry_by_name(name: str):
    all_entrys = get_entry_by_name(name)
    for entry in all_entrys:
        delete_entry_by_id(entry[0])


def delete_entry_by_id(id: int):

    params = (id,)

    conn = sqlite3.connect('telefonbuch.sqlite')
    c = conn.cursor()
    sql = """DELETE FROM telefonbuch where id = ?"""

    affected = c.execute(sql, params).rowcount
    conn.commit()
    conn.close()


def get_entry_by_name(name: str) -> list[tuple]:
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
    name = "tine"
    get_entry_by_name(name)
    print("test suchen")

if __name__ == '__main__':
    test()
