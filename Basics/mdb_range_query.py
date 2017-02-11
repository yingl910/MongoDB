
''' This is an example code of MongoDB range query'''
''' This code returns all cities that are founded in 21st century. '''
''' As for the document structure, refers to city data in 'Example data structure' file'''

from datetime import datetime
import pprint

def range_query():

    query = {'foundingDate': {'$gte': datetime(2001, 1, 1), '$lte': datetime(2099, 12, 31)}}
    return query


def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db


if __name__ == "__main__":
    # For local use
    db = get_db()
    query = range_query()
    cities = db.cities.find(query)

    print("Found cities:", cities.count())
    pprint.pprint(cities[0])
