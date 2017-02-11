
'''These are some exmaple code of MongoDB ineuqality operators'''

query = {"population": {'$gt': 25000}}
query = {"population": {'$gt': 25000, "$lte": 50000}}
# all city name begins with x
query = {"name": {'$gte':'X', "$lt": 'Y'}}
# founding in year 1837
query = {"foundingDate":{'$gte': datetime(1837, 1, 1), "$lte": datetime(1837, 12, 31)}}
query = {"country":{'$ne':'United States'}}

#follow the last query
cities = db.cities.find(query)

num_cities = 0
for c in cities:
    pprint.pprint(c)
    num_cities += 1

print("\nNumber of cities matching: %d\n" % num_cities)

