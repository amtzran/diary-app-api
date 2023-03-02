# Diary App Api REST

## Technical test for backend developer in Comuna 18

Bienvenido a la API REST de Diary App 👋.

## Requirements

- [Python 3.8 | 3.9 | 3.10](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
- [PDF Kit](https://pypi.org/project/pdfkit/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/#)
- [Django Environ](https://django-environ.readthedocs.io/en/latest/)
- [Django Storages](https://django-storages.readthedocs.io/en/latest/)
- [Django Filter](https://django-filter.readthedocs.io/en/stable/)
- [Django Extensions](https://django-extensions.readthedocs.io/en/latest/)

## Run project in local

1. Clone repo.
2. Create `.env` file.

   ```dotenv
    SECRET_KEY=
    DEBUG=True
    
    DB_HOST=your_host
    DB_NAME=your_database
    DB_USER=postgres
    DB_PASS=your_password
    
    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY=
    AWS_STORAGE_BUCKET_NAME=
    AWS_DEFAULT_ACL='public-read'
    AWS_BUCKET_ACL='public-read'
    AWS_QUERYSTRING_AUTH=False
   ```
3. Docker build.

   ```shell
   > docker-compose build
   ```
   
4. Docker up.

   ```shell
   > docker-compose up
   ```
   
5. Run migrates.

   ```shell
   > docker-compose run --rm app sh -c "python manage.py migrate"
   ```

6. Create superuser.

   ```shell
   
   > docker-compose run --rm app sh -c "python manage.py createsuperuser"
   ```

7. Api: <http://localhost:8000/>

8. Panel admin: <http://localhost:8000/admin>

## Environments

You can check a envirnoment [development](https://api.alberto.mexcorp.technology).

- url base: `api.alberto.mexcorp.technology`



## Expresiones de Gratitud 🎁

* De antemano quiero agradecer 🍺  a todo el equipo de **Comuna 18** por creer en mi y darme oportunidad de continuar con el proceso de la vacante.



---
⌨️ con ❤️ por [Alberto Martínez](https://github.com/amtzran) 😊