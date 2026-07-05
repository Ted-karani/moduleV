Inventory Management System
built with flask and python for managing store inventory
fetched data from this link: https://openfoodfacts.github.io/openfoodfacts-server/api/
the docs recommended i use barcode so i used it having and getting info from the docs
ad also for it to work the docs recommend use of user agent idk what that is but docs explained well so i used it.

 run `pipenv install` to install dependencies
 run `pipenv shell` to activate the environment
 run `python app.py` in the server folder to start the server
 open a new terminal and run `python cli.py` to use the cli


 GET /inventory - get all items
 GET /inventory/id - get one item
 POST /inventory - add new item
 PATCH /inventory/id - update item
 DELETE /inventory/id - delete item
 GET /fetch/barcode - fetch product from openfoodfacts
 POST /fetch/barcode/add - fetch and add to inventory

some challenges i faced
openfoodfacts was returning empty responses, turned out i needed to add a User-Agent header as required by their docs
 got a ModuleNotFoundError for flask because i wasnt inside the pipenv shell
 cli was giving connection refused error because i forgot to run the flask server in a separate terminal