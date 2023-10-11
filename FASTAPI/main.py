from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")           #path decorator
async def root():
    return {"message": "Hello World"}


todos= []

#   get all to dos
@app.get("/todos")           
async def get_todos():
    return {"todos": todos}


#   get single to do
@app.get("/todos/{todo_id}")           
async def get_todo(todo_id: int):
    for todo in todos:
        if todo_id == todo_id:
            return {"todo": todo}
    return {"message": "No todos found"}


#   create a to do
@app.post("/todos")           
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message": "todo has been added"}


#   update a to do
@app.put("/todos/{todo_id}")           
async def update_todos(todo_id: int, todo_obj: Todo):
    for todo in todos:
        if todo_id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo": todo}
    return {"message": "No todos found to update"}


#   delete a to do
@app.delete("/todos/{todo_id}")           
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo_id == todo_id:
            todos.remove(todo)
            return {"message": "Todo has been deleted"}
    return {"message": "No todos found"}
