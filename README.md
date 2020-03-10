# TODO Application

Application:
* Flask-RESTful for API
* MongoDB + Mongo Express
* All in separete Docker containers
* Deploy in one command

## How to install

1. `git clone https://github.com/KostyaBovt/todo_app.git folder`
2. `cd folder`
3. `docker-compose up`
4. API: http://localhost:5000/
5. Mongo Express: http://localhost:8081/


## API 

#### API todo lists: 

* Get all todo lists: `GET http://localhost:5000/todolists/`
* Get one todo list `GET http://localhost:5000/todolists/<todolist_id>/`
* Create todo list `POST http://localhost:5000/todolists/`
```
{
    "name": "todolist_1",
    "items": [
        {
            "text": "text_1_1",
            "finished": true,
            "due_date": "2021-07-16T19:20:30"
        },
        {
            "text": "text_1_2",
            "finished": true,
            "due_date": "2021-07-16T19:20:30"
        }
    ]
}
```
* Update todo list `PUT http://localhost:5000/todolists/<todolist_id>/`
```
{
    "name": "todolist_1_updated",
    "items": [
        {
            "text": "text_1_1_new",
            "finished": true,
            "due_date": "2021-07-16T19:20:30"
        },
        {
            "text": "text_1_2_new",
            "finished": true,
            "due_date": "2021-07-16T19:20:30"
        }
    ]
}
```
* Delete todo list `DELETE http://localhost:5000/todolists/<todolist_id>/`

#### API todo items: 

* Create todo item `POST http://localhost:5000/todoitems/`
```
{
    "todolist_id": "<todolist_id>",
    "text": "text_1_2_created",
    "finished": true,
    "due_date": "2021-07-16T19:20:30"
}
```
* Update todo item `PUT http://localhost:5000/todoitems/<todoitem_id>/`
```
{
    "text": "text_1_2_updated",
    "finished": true,
    "due_date": "2021-07-16T19:20:30"
}
```
* Delete todo item `DELETE http://localhost:5000/todoitems/<todoitem_id>/`
