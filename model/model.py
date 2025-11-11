from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def id_get_museo(self,museo:str):
        musei=self._museo_dao.get_musei()
        for m in musei:
            if museo == str(m.nome):
                 return int(m.id)




    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO

        artefatti_filtrati=[]
        artefatti = self._artefatto_dao.get_artefatti()

        if museo == "Nessun Filtro" and epoca =="Nessun Filtro":
            artefatti_filtrati=artefatti
        elif epoca == "Nessun Filtro" :
            for artefatto in artefatti:
                if self.id_get_museo(museo)==artefatto.id_museo    :
                    artefatti_filtrati.append(artefatto)
        elif museo=="Nessun Filtro" :
            for artefatto in artefatti:
                if str(artefatto.epoca).strip() ==epoca.strip() :
                    artefatti_filtrati.append(artefatto)
        else:
            for artefatto in artefatti:
                if  int(artefatto.id_museo) == self.id_get_museo(museo):
                    if str(artefatto.epoca).strip() ==epoca.strip():
                        artefatti_filtrati.append(artefatto)
        return artefatti_filtrati

    def get_lista_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
        artefatti=self._artefatto_dao.get_artefatti()
        lista_epoche=[]

        for artefatto in artefatti :
            lista_epoche.append(artefatto.epoca)
        set_lista_epoche=set(lista_epoche)
        return set_lista_epoche


    # --- MUSEI ---
    def get_lista_musei(self):
        """ Restituisce la lista di tutti i musei."""
        # TODO
        lista_musei=self._museo_dao.get_musei()
        if len(lista_musei) == 0:
            print('connessione museo non avvenuta')
            return None
        else:
            return lista_musei



