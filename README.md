# Politico Api

## Badges

## Description
Politico is a platform where politicians interact with voters.Politicians can declaire their interest in office and voters can vote for them.

## Setup and Installation
1. Clone the repo

    ```git
        $ git clone https://github.com/danieloselu3/politico-api.git
    ```

2. Cd into the repo

    ```
        $ cd politico-api
    ```

3. Activate Virtual environment

    ```
        $ virtualenv venv
        $ source venv/bin/activate
    ```

4. Install dependencies

    ```
        $ pip install -r requirements.txt
    ```

5. Initialize environment and run flask

    ```python
        $ extend FLASK_APP=manage.py
        $ extend FLASK_ENV=development
        $ flask run
    ```

## Politico Endpoints

HTTP Method | Endpoint | Description
--------------- | ---------------- | -------------------
POST | /parties | Create a Political party
GET | /parties/party_id | Fetch a specific party
GET | /parties | Fetch all Political parties
PUT | /parties/party_id/new_name | Edit the name of a Political party
DELETE | /parties/party_id | Delete a Political party
POST | /offices | Create a Political office
GET | /offices/office_id | Fetch a specific office
GET | /offices | Fetch all Political offices

## Author Daniel Oselu



