from pymongo import MongoClient
from bson.objectid import ObjectId
import bson
import pprint
from bson.son import SON

client = MongoClient('localhost', 27017)

pipeline = [
	{
		"$group": 
			{
				"_id": "$MUNICIPIO", 
				"total":{"$sum": "$VALOR"}, 
				"count": {"$sum": 1}
			}
	}, {"$sort": SON([("count", -1), ("_id", -1)])}]
pprint.pprint(list(client.governo.bolsafamilia.aggregate(pipeline)))

client.close