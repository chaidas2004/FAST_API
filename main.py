#pip install fastapi uvicorn to install FAST API via terminal using the command line, compatiable w python


from fast api import FastAPI

app = FastAPI()
#an instance of the FastAPI class is created and assigned to the variable app

@app.get("/")
#define a route for the application. The @app.get("/") tells FastAPI that function should be called when a GET request is made to the root URL ("/")
async def read_root():
    return {"Hello": "World"}
  #asynchronous function read_root() which will be executed when the root URL is accessed with a GET request which returns the output Hello: World
  
#uvicorn main:app --reload to display the contents via uvicorn


# Define an asynchronous function named read_items
async def read_items():
 return {"items": ["Item1", "Item2"]}
    # The function returns a dictionary with a key "items" associated with a 
    # list of strings

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # The function returns a dictionary, which FastAPI automatically converts to a response
   #This dictionary includes the 'item_id' that was 
    # passed in the URL, demonstrating how you can access and return path 
    # parameters in your API endpoints.
    return {"item_id": item_id}

# GET endpoint "/search/" that uses an optional query parameter 'q'
@app.get("/search/")
# 'q: str = None' means 'q' is an optional query string parameter of a string, uses to None if nothing is given
async def search_items(q: str = None):
    # Return a dictionary with the search query 'q'. FastAPI converts this to a JSON response
    return {"query": q}

# Import BaseModel from Pydantic 
from pydantic import BaseModel

# Pydantic model to validate and structure request data
class Item(BaseModel):
    name: str  # Required string field
    description: str = None  # Optional string field, defaults to None
    price: float  # float field
    tax: float = None  # Optional float field, defaults to None



@app.post("/items/")
# Define asynchronous function to handle POST requests, expecting an 'item' of type 'Item'
async def create_item(item: Item):
    # Returns a dictionary with item's name and price. FastAPI converts it to JSON
    return {"name": item.name, "price": item.price}


# Update item endpoint, responding to PUT requests at "/items/{item_id}"

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
   
    return {"item_name": item.name, "item_id": item_id}  

# Delete item endpoint, responding to DELETE requests at "/items/{item_id}"
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    # item_id: int - Path parameter indicating which item to delete, automatically converted to an integer
    return {"item_id": item_id, "deleted": True}  # Confirms deletion with item_id and deleted stat


