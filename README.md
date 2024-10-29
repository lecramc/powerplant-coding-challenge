# powerplant-coding-challenge


## Welcome !

### How to use this repo

This repo contains the code for the coding challenge.  

To run the code, you need to have docker installed on your machine.

#### Running the code

To run the code, you need to have docker installed on your machine.

1. Clone this repo
2. Run `docker-compose up --build` or `docker compose up --build` to start the API
3. Access the API at `http://localhost:8888/docs`

#### Running the tests

The tests are written using pytest.

1. Run `poetry shell` to create a virtual environment
2. Run `poetry install` to install the dependencies 
3. RUN `pytest -m unit` to run the unit tests
4. RUN `pytest -m integration` to run the integration tests

#### Running the linter

The linter is written using ruff.

1. Run `poetry shell` to create a virtual environment
2. Run `poetry install` to install the dependencies 
3. Run `ruff check` to run the linter
4. Run `ruff format` to format the code
