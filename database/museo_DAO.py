from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass
        # TODO
    @staticmethod
    def get_musei():
        cnx=ConnessioneDB.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query = """SELECT * FROM museo"""
        cursor.execute(query)
        result=[]
        for row in cursor:
            museo=Museo(row["id"],
                        row["nome"],
                        row["tipologia"]
                        )
            result.append(museo)
        cnx.close()
        cursor.close()
        return result