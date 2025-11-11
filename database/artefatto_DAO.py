import mysql

from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass
        # TODO
    @staticmethod
    def get_artefatti():
        cnx=ConnessioneDB.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query = """SELECT * FROM artefatto"""
        cursor.execute(query)
        result=[]
        for row in cursor:
            artefatto=Artefatto(row["id"],
                                row["nome"],
                                row["tipologia"],
                                row["epoca"],
                                row["id_museo"]
                                )
            result.append(artefatto)

        cnx.close()
        cursor.close()
        return result
