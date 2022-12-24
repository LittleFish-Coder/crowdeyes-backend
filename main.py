import json
from flask import Flask, request, jsonify
import pymongo

client = pymongo.MongoClient("mongodb+srv://adrianyu:Code0317@cluster0.osewdux.mongodb.net/?retryWrites=true&w=majority")

db = client.Chatroom
userFeedback = db.feedback

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  print("Someone enter")
  return "Hello World"

@app.route('/test', methods=['GET'])
def test():
  responeBody = {
    "response": "this is a test json response body"
  }
  return jsonify(responeBody)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
  jsonMap = request.json
  print(jsonMap)
  userFeedback.insert_one(jsonMap)
  return "Feedback success"

if __name__ == '__main__':
    app.run(debug=True)