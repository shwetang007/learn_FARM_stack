from model import Todo 

#MongoDB driver for FastAPI
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
# Stores an instance of AsynchIOMotorClient from MongoDB database.

database = client.TodoList # Links The List of Tasks(Client) to variable database.

collection = database.todo # Similiarily assigns Database to a varaible collection which will have collection of databases.

async def fetch_one_todo(title):
    document = await collection.find_one({"title":title})
    return document
    #function to fetch a todo file, with 'document' waiting for the collection to get the file name with title.
async def fetch_all_todos():
    todos = [] # Inorder to store multiple elements we need list [] that will store all documents.
    cursor = collection.find({})
    # in order to find all the files we use .find() method because its scalable .
    
    async for document in cursor: # Loop which iterates the whole 
        todos.append(Todo(**document))
    
    return todos

async def create_todo(todo):
     document = todo
     result = await collection.insert_one(document) # Creates a new file 
     return document
    # Assign the file to the document, and have the result variable wait for the collection to retrieve the specific document.
async def update_todo(title, desc):
    await collection.update_one(    # Updates a new file item to the collection.
        {"title":title}, 
        {"$set":{
            "description":desc
                 }})
    document = await collection.find_one({"title":title})
    return document

async def remove_todo(title):
    await collection.delete_one({"title":title})# Removes a file from collection
    return True

# Basically,all the fuctions above provides us the basic functionality of the Todo() to delete,append and fetch items from a collective variable called as collection.
