# KeyValue_Store
This Django REST API provides a model that can store keys and values. Every model instance has TTL of 5 minuetes or whatever you want to.
The TTL get reset everytime any data is being get, put, patch, and even searched.

## Getting Started
Go through the below instructions to get started with this project.

### Installation
Clone the github repository.

    git clone https://github.com/bahaspieler/Key-Value-Store-REST-API-with-TTL-service.git

Activate a new virtual environment.

    virtualenv venv --python=python3
    source venv/bin/activate

Now `cd` to project root directory and install dependencies.

    cd KeyValue_Store
    pip install -r requirements.txt

Now make the migrations and migrate it.

    python manage.py makemigrations
    python manage.py migrate

Create a `superuser`.

    python manage.py createsuperuser
    python manage.py migrate

Now run the server with the following command in your bash which will activate the TTL service in the background.

    python manage.py runserver & python background.py
    
Add some data to the model following the below link.

    http://127.0.0.1:8000/admin/store_api/store/
    
Can even test the app.

    python manage.py test  

The custom management command that is doing the TTL service is located here.

    KeyValue_Store/store_api/management/commands/ttl.py    

Access to the api using,

    http://127.0.0.1:8000/api/store/    
 
Get the Value using the primary key,

    http://127.0.0.1:8000/api/store/primarykeyhere  
    
Also can query with keys and values by,

    http://127.0.0.1:8000/api/store/?q=key or value 
       
## Built With

  ##### [Django](https://www.djangoproject.com/)
  ##### [Django REST Framework](https://www.django-rest-framework.org/)
