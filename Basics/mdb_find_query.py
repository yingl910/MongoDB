
''' This is an example code of MongoDB find query'''
''' This code answers question: find all autos where the manufacturer field matches "Porsche" '''
''' As for the document structure, refers to car data in 'Example data structure' file'''

def porsche_query():

    query = {'manufacturer': "Porsche"}
    return query

# Code here is for local use on the computer.
def get_db(db_name):
    # For local use
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def find_porsche(db, query):
    # For local use
    return db.autos.find(query)


if __name__ == "__main__":
    # For local use
    db = get_db('examples')
    query = porsche_query()
    results = find_porsche(db, query)

    print("Printing first 3 results\n")
    import pprint
    for car in results[:3]:
        pprint.pprint(car)