
'''This is an example of MongoDB aggregation framework'''
'''This code uses cities infobox dataset and answers question:
What is the average city population for a region in India?'''


# first, calculate the average population of cities in each region and then
# calculate the average of the regional averages.

# Note: If you want to accumulate using values from all input documents to a group stage, you may use
# a constant as the value of the "_id" field. For example,
# { "$group" : {"_id" : "India Regional City Population Average",... }


def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():

    pipeline = [
        {'$match':{"country": "India"}},
        {'$unwind': "$isPartOf"},
        {'$group': {'_id': '$isPartOf', 'avg': {'$avg': '$population'}}},
        {'$group': {'_id': 'India Regional City Population Average', 'avg': {'$avg': '$avg'}}}]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]


if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    assert len(result) == 1
    # Your result should be close to the value after the minus sign.
    assert abs(result[0]["avg"] - 201128.0241546919) < 10 ** -8
    import pprint
    pprint.pprint(result)
