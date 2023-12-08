# IOT Device Management Paltform

Develop a RESTful API using Django and Django REST Framework to manage IoT devices,
incorporating PostgreSQL, InfluxDB or TimescaleDB for data storage, and implementing a
role-based access control system.

# Local Setup-

- `git clone url`
- create a .env file in root directory
- copy example-env in .env
- `docker compose up --build`
- to access the admin panel, create a superuser using this command `docker exec -it django python manage.py createsuperuser`

# Check the admin interface-

    http://0.0.0.0:8000/admin

# Check the swagger documentation-

    http://0.0.0.0:8000/api/schema/swagger-ui/

# Tech Stack

- python
- DRF
- PostgreSQL
- TimescaleDB
- docker
- JWT
