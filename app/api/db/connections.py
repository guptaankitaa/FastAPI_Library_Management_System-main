from pymongo import MongoClient

client = MongoClient("mongodb+srv://epiphany:iamepiphany@cluster0.ebmrysk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["library_management"]

students_collection = db["students"]
