from model import Todo #Imports Todo function from model.py file

#MongoDB driver for FastAPI
import motor.motor_asyncio
#Brings motor_asynchio module from "motor" package into this package.

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
# Stores an instance of AsynchIOMotorClient from MongoDB database.

database = client.TodoList # Links The List of Tasks(Client) to variable database.

collection = database.todo # Similiarily assigns Database to a varaible collection which will have collection of databases.

async def fetch_one_todo(title):
    document = await collection.find_one({"title":title})
    return document
    #function that fetches one todo file in which a variable document waits for collection to get the file name with desired title.

async def fetch_all_todos():
    todos = [] # Inorder to store multiple elements we need list [] that will store all documents.
    cursor = collection.find({})
    # in order to find all the files we use .find() method because its scalable .
    
    async for document in cursor: # Loop which iterates the whole 
        todos.append(Todo(**document))
    
    return todos

async def create_todo(todo):
     document = todo
     result = await collection.insert_one(document)
     return document

async def update_todo(title, desc):
    await collection.update_one(
        {"title":title}, 
        {"$set":{
            "description":desc
                 }})
    document = await collection.find_one({"title":title})
    return document

async def remove_todo(title):
    await collection.delete_one({"title":title})
    return True
