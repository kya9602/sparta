from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:1234@cluster0.9i5vz.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})