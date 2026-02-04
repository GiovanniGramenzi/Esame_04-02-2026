from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_authorship():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """ SELECT * 
                    FROM authorship"""
        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def get_roles():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT role
                    FROM authorship"""
        cursor.execute(query)

        for row in cursor:
            result.append(row['role'])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def get_artists(role):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query=""" select a1.artist_id,a1.name,COUNT(o.object_id) as indice
                 from authorship a,objects o,artists a1
                 where a.object_id=o.object_id and o.curator_approved=1  and a1.artist_id=a.artist_id and a.role=%s
                 group by a.artist_id"""
        cursor.execute(query,(role,))
        for row in cursor:
            result.append(Artist(row['artist_id'],row['name'],row['indice']))
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def get_nodes(role,dict_a):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query='SELECT artist_id FROM authorship WHERE role=%s'
        cursor.execute(query,(role,))
        for row in cursor:
            a=dict_a[row['artist_id']]
            result.append(a)
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def get_connessioni():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query=""" SELECT DISTINCT a1.artist_id as a1,a2.artist_id as a2
                  FROM authorship a1,authorship a2,objects o
                  WHERE a1.artist_id<a2.artist_id and a1.object_id=o.object_id or a2.object_id=o.object_id and o.curator_approved=1  """
        cursor.execute(query)
        for row in cursor:
            result.append((row['a1'],row['a2']))
        cursor.close()
        conn.close()
        return result





