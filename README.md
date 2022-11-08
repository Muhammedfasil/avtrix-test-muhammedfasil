# avtrix-test-muhammedfasil
Avtrix Django Machine Test

steps to install :

    1. clone code from https://github.com/Muhammedfasil/avtrix-test-muhammedfasil.git
    2. go to the cloned folder ( using cd )
    3. install virtual environment ( pipenv or venev )
    4. install the requirements by running "pip install -r requirements.txt"
    5. run migrations - "python3 manage.py migrate"
    6. run the app - "python3 manage.py runserver 0:8000"

Upload the data :
    1. create an excel file with the following data 
        order_date | region | city |category | product | quantity | unit_price

    2. open the following url in your browser:
        http://localhost:8000/admin/food/foods/import/
    3. Upload the file

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
    Note : I depply regret to inform you that the limit by 5 feature is not completed.
