import pymongo

client = pymongo.MongoClient("mongodb+srv://adrianyu:Code0317@cluster0.osewdux.mongodb.net/?retryWrites=true&w=majority")

print(client.list_database_names())

db = client.Chatroom

print(db.list_collection_names())

testJson = {
  "userName": "Andy",
  "gender": "Male",
  "feedback": "I think this is good."
}

userFeedback = db.feedback

userFeedback.insert_one(testJson)

