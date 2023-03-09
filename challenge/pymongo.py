import pprint
import pymongo as pyM
client =pyM.MongoClient("mongodb+srv://pymongo:pymongo@cluster0.h884ej4.mongodb.net/?retryWrites=true&w=majority")

db = client.test
collection = db.test_collection
print(db.test_collection)

post = {
  "client": "spongebob",
  "cpf": "333333333",
  "address": "Pineapple",
  "account": [
    {"type":"krusty krab","bank_agency":"003", "num":"01", "balance":400},
    {"type":"krusty krab","bank_agency":"003", "num":"02", "balance":200},
    {"type":"krusty krab","bank_agency":"003", "num":"03", "balance":100},
  ]
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id

"""
entered data
"""
pprint.pprint(posts.find_one())

"""
add new data
"""
new_posts = [
  {
    "client": "Sandy",
    "cpf": "444444444",
    "address": "Texas",
    "account": [
      {"type":"krusty krab","bank_agency":"003", "num":"04", "balance":400},
      {"type":"krusty krab","bank_agency":"003", "num":"05", "balance":800},
    ]
  },
  {
    "client": "Patrick",
    "cpf": "777777777",
    "address": "Rock",
    "account": [
      {"type":"krusty krab","bank_agency":"003", "num":"06", "balance":0}
    ]
  }
]
result = posts.insert_many(new_posts)
result.inserted_ids
"""
information retrieval based on key-value pairs
"""
for post in posts.find({"client": "Sandy"}):
  pprint.pprint(post)