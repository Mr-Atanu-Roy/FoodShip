## DESCRIPTION
    1. Online food ordering site 
    2. Created using django
## Features

- Restaurants are shown as per your location
- View and order foods from various resturants near you
- View foods and resturants by caterories
- Search for restaurants near you
- Order food 
- Pay online/cash on delivery
- Instamojo payment gateway integrated
- Create user profile, add multiple addresses


## Tech Stack

**Client Side:** HTML, SCSS, TailwindCSS

**Server Side:** Django, instamojo payment gateway integrated


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DEBUG = TRUE`

`SECRET_KEY = 'django-insecure-ig4&)no7x*mb(t_r@dh9x9%&b4u_0o+k8%%7bxf5*j$nhe*8sm''`

### Instamojo test credentials

`API_KEY = "test_5b078119eb4fdf794bd218a0e58"`

`AUTH_TOKEN = "test_86486ea3926cbd174c5bb653a13"`

`ENDPOINT = "https://test.instamojo.com/api/1.1/"`
## Installation

Create a folder and open terminal and install this project by
command 
```bash
git clone https://github.com/Mr-Atanu-Roy/FoodShip

```
or simply download this project from https://github.com/Mr-Atanu-Roy/FoodShip

In project directory Create a virtual environment(say env)

```bash
  virtualenv env

```
Activate the virtual environment

For windows:
```bash
  env\Script\activate

```
Install dependencies
```bash
  pip install -r requirements.txt

```
To migrate the database run migrations commands
```bash
  py manage.py magemigrations
  py manage.py migrate

```

Create a super user
```bash
  py manage.py createsuperuser

```
And add some records(restaurants and products) from admin panel.

To run the project in localserver
```bash
  py manage.py runserver

```
Then go to http://127.0.0.1:8000 in your browser to see the project

### For test online payment via debit card use the following instamojo credentials
`Card Number: 4242 4242 4242 4242`

`Expiry: 01/25`

`CVV: 111`
## Author

- [@Mr-Atanu-Roy](https://www.github.com/Mr-Atanu-Roy)

