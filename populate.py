from pymongo import Connection
connection = Connection()

#connect to localhost port 27017
connection = Connection('localhost', 27017)
#connect to db index
db = connection['index']

#connect to collection named table , similar to table in RDMS database mongodb uses collection
table = db.table

# in SON  format data
post = {"surface_word": "berlin", "url": "http://dbpedia.org/resource/Berlin,http://dbpedia.org/resource/usa" , "count":"3,45" }
#insert data into table
table.insert(post)

post = {"surface_word": "berlin1", "url": "http://dbpedia.org/resource/Berlin,http://dbpedia.org/resource/usa" , "count":"3,45" }
table.insert(post)

post = {"context_token": "hills", "url": "http://dbpedia.org/resource/Berlin,http://dbpedia.org/resource/usa" , "count":"3,45" }
table.insert(post)

post = {"context_token": "city", "url": "http://dbpedia.org/resource/Berlin" , "count":"15" }
table.insert(post)

post = {"context_token": "mountain", "url": "http://dbpedia.org/resource/usa" , "count":"13" }
table.insert(post)



		
