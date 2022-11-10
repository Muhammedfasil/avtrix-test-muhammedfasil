# avtrix-test-muhammedfasil
Avtrix Django Machine Test

steps to install :

    1. clone code from https://github.com/Muhammedfasil/avtrix-test-muhammedfasil.git
    2. go to the cloned folder ( using cd )
    3. install virtual environment ( pipenv or venev )
    4. install the requirements by running "pip install -r requirements.txt"
    5. run migrations - "python3 manage.py migrate"
    6. run the app - "python3 manage.py runserver 0:8000"

Open the site:
    1. Go to http://localhost:8000 in your browser
    2. Admin credentials:
        username : admin
        
        
        password : As@12345

Upload the data :
    1. create an excel file with the following data 
        order_date | region | city |category | product | quantity | unit_price

        A sample excel file is added in the the path sample/food.xlsx

    2. In the admin dashboard click on the "Foodss" inside the "Food" section.
    3. Click on Import
    4. Select the file
    5. Click on Submit

Searching products :
    1. To search all products in GET method, open the following url
        http://localhost:8000/api/search/
    2. To get only a product by product name open the following url
        http://localhost:8000/api/search/?product_name=<product_name>

        eg: http://localhost:8000/api/search/?product_name=Carrot
    
    3. To get all products inh POST method, submit the form ion the following url without giving any data
        http://localhost:8000/api/search
    
    4. To get only a product by product name, add the following data to the form in the following url and submit
        URL : http://localhost:8000/api/search
        DATA :      {
                        "product_name" : "<product_name>"
                    }
        EXAMPLE :   {
                        "product_name" : "Whole Wheat"
                    }
    5. To implement pagination simply add "?page=<page_number>" in the end of url ( add the "page" parameter a querystring )
        example :
            http://localhost:8000/api/search/?page=1
            http://localhost:8000/api/search/?page=2
            http://localhost:8000/api/search/?page=3

            http://localhost:8000/api/search/?product_name=Carrot&page=1
            http://localhost:8000/api/search/?product_name=Carrot&page=2
            http://localhost:8000/api/search/?product_name=Carrot&page=3
