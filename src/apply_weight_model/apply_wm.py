# in dataiku uncomment the following line
#import dataiku
import sys
import numpy as np
import py2neo
import pandas
from pandas import DataFrame
from py2neo import Graph,authenticate, Node, Relationship

def get_conn_string():
   return "http://MYNEO4JUSER:MYNEO4JPASS@138.68.146.141:7474/db/data"

def create_neo4j_connection(addr):
   return Graph(addr)

def store_classified_tweets(graph):
   df = dataiku.Dataset("by_IDRestaurant_prep_scored").get_dataframe()
   for d in df.iterrows():
       r_id = str(d[1][0])
       b_points = str(d[1][1])
       cypher_qr="MERGE (r:Restaurant{id:'"+r_id+"'}) MERGE (r)-[:HAS]->(b:Bacon) ON CREATE SET b.points="+b_points+" ON MATCH SET b.last_points=b.points, b.points="+b_points+" return r"
       print("TEST \n\n\n\n")
       print(cypher_qr)
       a = graph.run(cypher_qr)
   

   
def send_output(df):
   # Recipe outputs
   output = dataiku.Dataset("by_IDRestaurant_scored_ranked")
   output.write_with_schema(df)

def load_data(str,graph):
   df = DataFrame(graph.data(str))
   return df
   
   
if __name__ == "__main__":
   store_classified_tweets(create_neo4j_connection(get_conn_string()))
   query2 = "MATCH (t:Bacon)<--(r:Restaurant) RETURN r.id as Restaurant, t.points as Points ORDER BY Points DESC"
   df = load_data(
       query2, #set here your query 1 or 2
       create_neo4j_connection(get_conn_string()))
   send_output(df)

