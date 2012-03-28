from pymongo import Connection
connection = Connection()

#connect to localhost port 27017
connection = Connection('localhost', 27017)
#connect to db index
db = connection['indiex']

#connect to collection named table , similar to table in RDMS database mongodb uses collection
table = db.table

#function takes a list and a token (which is a string) and check if any entry in l is such that first element of that entry  equals to token
#if it get such a element then it return its index else return -1
def find_ele(l , token):
	for i in range(0,len(l)):
		if l[i][0] == token:
			return i
	return -1
			


#Query surface_word is the surface_word that is to be searched and context_tokens is the list of context tokens
surface_word = "berlin"
context_tokens = ["city" , "hills"]

result_context = []  #empty list to store context result url
for i in table.find({"context_token" : { "$in" : context_tokens }}):   #systax to query mongodb
	list_url =  i['url'].split(",") 	#split url to get list of urls
	list_count =  i['count'].split(",")	#split count to get list of counts
	for count in range(0,len(list_url)):
		val = find_ele(result_context , list_url[count])	#check if the url already exist in result_context 
		if(val == -1):						# the above check if return -1 , means url is not present 
			result_context.append([list_url[count],int(list_count[count])]) # add the url as it is not present and also add the count
		else :
			result_context[count][1] = result_context[count][1] + int(list_count[count]) # if url present then increment the count

result_surface = [] #empty list to store context result url
for i in table.find({"surface_word" : surface_word }):
	list_url =  i['url'].split(",")
	list_count =  i['count'].split(",")	
	for count in range(0,len(list_url)):
		result_surface.append([list_url[count],int(list_count[count])])  #as all the url entries in the list will be unique so add them to the list

for i in result_surface:
	val  = find_ele(result_context , i[0])	#if a entry is obtained both in surface_word and context_token query result 
	if(val != -1):
		print result_context[val]  # print the url and its count (sum of all the counts)
		
