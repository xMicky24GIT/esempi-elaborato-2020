# Esempi utilizzati nell'elaborato per l'esame di maturità 2020
#	   Copyright (C) 2020  Michele Viotto
"""
Usato per testare sql injection per l'elaborato
"""
import sys
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="tesina"
    )


def vulnerable():
    username = input("Username: ")
    password = input("Password: ")

    cursor = db.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    try:
        cursor.execute(query)
        fetch = cursor.fetchone()
        print(f"Query eseguita: {cursor.statement}")
        print(f"Risultato query: {fetch}")
        if fetch:
            print(f"Bentornato {fetch[1]}")
        else:
            print("Credenziali errate")
    except mysql.connector.Error as error:
        print(error)


def parameterized():
    username = input("Username: ")
    password = input("Password: ")

    cursor = db.cursor(prepared=True)
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    params = (username, password)
    try:
        cursor.execute(query, params)
        fetch = cursor.fetchone()
        print(f"Query eseguita: {cursor.statement}")
        print(f"Risultato query: {fetch}")
        if fetch:
            print(f"Bentornato {fetch[1]}")
        else:
            print("Credenziali errate")
    except mysql.connector.Error as error:
        print(error)


if len(sys.argv) > 1:
    if sys.argv[1] == 'vuln':
        vulnerable()
    elif sys.argv[1] == 'param':
        parameterized()
    else:
        print("Devi inserire il parametro vuln o param")
else:
    print("Devi inserire il parametro vuln o param")
