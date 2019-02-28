from pymongo import MongoClient
from bson.objectid import ObjectId
import bson
import pprint
from bson.son import SON

client = MongoClient('10.52.51.28', 27017)

post = {
    "REFERENCIA" : 201811,
    "CONPETENCIA" : 201711,
    "UF" : "SP",
    "SIAFI" : 2847,
    "MUNICIPIO" : "BAURU",
    "NIS" : bson.int64.Int64(16003242400),
    "NOME" : "CREMILTON DA SILVA SANTOS",
    "VALOR" : 171.0
}
post_id = client.governo.bolsafamilia.insert_one(post).inserted_id
pprint.pprint(post_id)
client.close