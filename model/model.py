import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.artists = []
        self.roles=DAO.get_roles()
        self.a_dict={}


    def build_graph(self, role: str):
        self.artists=DAO.get_artists(role)
        for artist in self.artists:
            self.a_dict[artist.artist_id] = artist
        connessioni=DAO.get_connessioni()
        for c in connessioni:
            if c[0] and c[1] in self.a_dict.keys():
                a1=self.a_dict[c[0]]
                a2=self.a_dict[c[1]]
                if a1.num_objects<a2.num_objects:
                    peso=a2.num_objects-a1.num_objects
                    self.G.add_edge(a1.artist_id, a2.artist_id, weight=peso)
                if a1.num_objects>a2.num_objects:
                    peso=a1.num_objects-a2.num_objects
                    self.G.add_edge(a2.artist_id, a1.artist_id, weight=peso)
            print(self.G.number_of_nodes())

    def get_number_of_nodes(self):
        return self.G.number_of_nodes()
    def get_number_of_edges(self):
        return self.G.number_of_edges()



    def classifica(self):
        classifica = []
        for n in self.G.nodes:
            score = 0
            for e_out in self.G.out_edges(n, data=True):
                score += e_out[2]["weight"]
            for e_in in self.G.in_edges(n, data=True):
                score -= e_in[2]["weight"]

            classifica.append((n, score))

        classifica.sort(reverse=True, key=lambda x: x[1])
        return classifica

