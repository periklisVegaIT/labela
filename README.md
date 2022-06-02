# Assignment

Hello!
---------
In this repo you can see the code that 'solves' your assignment and a brief explanation how to start and use it.

**Brief explanation**
To solve your task I used Django's REST Framework. 
Also I changed the database from SQLite to PostgreSQL and added it to a container.

To use the application build it through docker and go to localhost:8000.
Django REST API provides us also with an easy to use front-end app that makes HTTP requests easier.
Of course you can also call the API through Postman or with classical curl commands through terminal.

**Starting the application**

* To start, go to the directory of the project and execute:
* This will create all the nessecary containers(For the app and the database).
- ```docker compose up```

* After that use the CLI of the Web container to migrate django's default models and api's app models.
- ```python manage.py makemigrations```
- ```python manage.py migrate```
- ```python manage.py makemigrations api```
- ```python manage.py migrate api```


* There is a fixture called products.json with 5 dummy products for the database, you can populate the database by using the command below in docker's web container through CLI:
- ```python manage.py loaddata products.json```

# All the urls

* '' -> Lists all products in the API. GET
* add/ -> Adds items to the cart. POST
* remove/<int:pk> -> Removes items from the cart. DELETE
* cart/ -> Lists all products in the cart. GET
* product/<int:pk> -> See details of a product. GET
* order/ -> Order cart. POST

# Example
- ```{ "id":1 }```
* To add a product you have to send a POST JSON request with the id of the product you want to add.

# Example
- ```remove/<id>```
* To remove a product you have to send a DELETE JSON request with the id of the product that you want to remove.

# Example
- ```{ "delivery_date":"2022/10/25 15:30"}```
* To order your Cart you have to send a POST JSON request with the date and time of delivery you wish formatted like this "delivery_date":"(YYYY/MM/DD HH:mm)"

# Example
- ```/product/<id>```
* To check a product details you have to send a simple GET request with the id"

