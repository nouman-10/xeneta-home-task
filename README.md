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

## Extra Details

### Time Taken:

Total: ~ 4:30 hours

- Initial Setup and building a basic API request (MVP) ~ 30 minutes
- Organizing the code with proper files/folders ~ 30 minutes
- Validating the inputs and error handling ~ 45 minutes
- Testing ~ 2-2:30 hours
- ReadMe and finalizing everything ~ 30 minutes

### Problems I faced:

One of the problems I faced, as evident from the time taken, was during testing. It was my first time after a long while doing testing on APIs that interact with databases. These days, I am mostly working on APIs for ML models, which have straight-forward testing.

So, building the test DBs and making sure the code uses the test data and not production in the best possible way (i.e, with minimum changes), was something I had to figure out during the testing phase.

### Things that can be added

There are some things that can be added here for improvement but I believe most of them would be regarding automation and ease of deployment:

- I have added github actions but I did so purposely at the end, as these can't be tested at the moment due to the database being local (It isn't perfect at the moment either due to the inability to test it)
- Containerize the application that runs both the postgres and flask app together.
