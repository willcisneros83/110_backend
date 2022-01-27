import pymongo
import certifi

mongo_url = "mongodb+srv://willcisneros:Brody23$$@cluster0.uam92.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url, tlsCAFile=certifi.where())



db = client.get_database("MusicStore")