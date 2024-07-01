from database.DB_connect import DBConnect
from model.geni import Gene


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getGeni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from genes g 
                """

        cursor.execute(query, )

        for row in cursor:
            result.append(Gene(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getInterazioni(g1,g2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select sum(espressioni.una) as peso
                    from (select sum(distinct i.Expression_Corr ) as una
							from genes g, interactions i, genes g2 
							where g.Chromosome = %s
							and g2.Chromosome = %s
							and g.GeneID = i.GeneID1 
							and g2.GeneID = i.GeneID2
							group by g.GeneID,g2.GeneID) as espressioni
                """

        cursor.execute(query,(g1,g2))

        for row in cursor:
            result.append(row["peso"])

        cursor.close()
        conn.close()
        return result


