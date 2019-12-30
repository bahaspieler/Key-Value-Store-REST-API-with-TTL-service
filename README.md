# KeyValue_Store
This Django REST API provides a model that can store keys and values. Every model instance has TTL of 5 minuetes or whatever you want to.

## Getting Started
Go through the below instructions to get started with this project.

### Installation
Clone the github repository.

    git clone 

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
    
## Built With

  #####[Django](https://www.djangoproject.com/)
  #####[Django REST Framework](https://www.django-rest-framework.org/)
