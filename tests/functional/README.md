# Setup

### Install the libraries

To install the required libraries, run `pip install -r requirements.txt`

### Run the Docker PostgresSQL

```bash
docker build -t ratestask .
```

This will create a container with the name _ratestask_, which you can
start in the following way:

```bash
docker run -p 0.0.0.0:5432:5432 --name ratestask ratestask
```

You can connect to the exposed Postgres instance on the Docker host IP address,
usually _127.0.0.1_ or _172.17.0.1_. It is started with the default user `postgres` and `ratestask` password.

```bash
PGPASSWORD=ratestask psql -h 127.0.0.1 -U postgres
```

alternatively, use `docker exec` if you do not have `psql` installed:

```bash
docker exec -e PGPASSWORD=ratestask -it ratestask psql -U postgres
```

### Setup the environmental variables

Create a `.env` file with the following values (Note: normally you wouln't add variables like these in readme but for ease of copying/pasting, I am including them here)

```bash
DB_HOST="0.0.0.0"
DB_PORT="5432"
DB_USER="postgres"
DB_PASSWORD="ratestask"
DB_NAME="postgres"
```

### Run the app/tests

To run the tests,

```bash
pytest tests/functional
```

To run the application:

```bash
python app.py
```

Sample CURL command:

```bash
curl "http://127.0.0.1:5000/rates/?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"
```

## Simple Docker Setup

To simplify the setup, you can simply build and run the Docker image. Note: you still have to run the Docker setup for PostgresSql as