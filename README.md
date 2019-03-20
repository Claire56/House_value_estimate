# Zyzy 
Zyzy is a webapp that uses machine learning to estimate the value of your home in a different location.

## Table of Contents
* Overview
* Tech Stack
* Setup/Installation
* Demo
* Future Features

## Overview
once thhe user geets to the landing page, I present to them the scope of the app(cities)available for the estimates, 
they are then required to provide features of their house and also to choose a city they would like the estimate to be based off.
In return they get the estimated price of their house in the chosen city and a few general statistics like the average 
cost of a house with a pool vs the one with out a pool.


## Tech Stack
Data Wrangling: Pandas, Numpy , seaborn, matplotlib <br>
Framework: Flask <br>
Backend: Python, SQLAlchemy, PostgreSQL ,SciKit_Learn <br>
Frontend: Javascript , AJAX, JSON , JQuery, Jinja, HTML, CSS, Bootstrap <br>
Libraries: D3.js, chart.js

Setup/Installation
On local machine, go to desired directory. Clone  repository:

$ git clone https://github.com/Claire-Kimbugwe/House_value_estimate
Create a virtual environment in the directory:

$ virtualenv env
Activate virtual environment:

$ source env/bin/activate
Install dependencies:

$ pip install -r requirements.txt
Create database:

$ createdb music
Build database:

$ python3 -i model.py
>>> db.create_all()
Seed database:

$ python3 -i seed.py
Run app:

$ python3 server.py
Navigate to localhost:5000 in browser.


## Demo

## Future Features
* utelise housing API's to get running data that will be used in training the machine learning model
* Add a login page for frequent visitors 



