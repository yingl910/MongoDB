
'''This is an example of MongoDB aggregation framework'''
'''This code uses cities infobox dataset and answers question:
first calculate the average city population for each region in a country and
then calculate the average of all the regional averages for a country'''

# This example involves compound keys of '_id' field in $group stage



def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():

    pipeline = [
        {'$unwind': '$isPartOf'},
        {'$group': {'_id': {'country': '$country', 'region': '$isPartOf'}, 'avg_cr':{'$avg': '$population'}}},
        {'$group': {'_id': '$_id.country', 'avgRegionalPopulation': {'$avg': '$avg_cr'}}},
        {'$sort': {'avg_c': -1}}]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]

if __name__ == '__main__':
    # Test Run.
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    if len(result) < 150:
        pprint.pprint(result)
    else:
        pprint.pprint(result[:100])
    key_pop = 0
    for country in result:
        if country["_id"] == 'Lithuania':
            assert country["_id"] == 'Lithuania'
            assert abs(country["avgRegionalPopulation"] - 14750.784447977203) < 1e-10
            key_pop = country["avgRegionalPopulation"]
    assert {'_id': 'Lithuania', 'avgRegionalPopulation': key_pop} in result
