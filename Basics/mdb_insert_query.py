
''' This is an example code of MongoDB insert query'''
''' This code insert the automobile data into the 'autos' collection '''
''' data is in 'autos-small.csv' '''


from autos import process_file


def insert_autos(infile, db):

    data = process_file(infile)
    for a in data:  # a is a dictionary
        db.autos.insert(a)  # question: difference between inserting a and data


if __name__ == "__main__":
    # Code here is for local use on your own computer.
    from pymongo import MongoClient

    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    insert_autos('autos-small.csv', db)
    print(db.autos.find_one())