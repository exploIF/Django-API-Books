# Books API
> Designing and creating a Book API based on data from the website: https://www.googleapis.com/books/v1/volumes?q=

## Table of contents
* [General info](#general-info)
* [Usage](#usage)
* [Technologies](#technologies)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
- downloading data and entering them into your own database,
- downloading data from title, authors, publish_date and categories,
- filtering and sorting data stored in database

## Usage
- GET books/ list of all books with posibility to filter and sort e.g. books/?publishedDate=1864 or books/?sort=publishedDate 
  or books/?publishedDate=1864&sort=-title
- GET books/<book_id> e.g. books/63RaAAAAcAAJ
- POST db/ with request body {"q": "_query to search in google api_"} for inserting returned data to database

## Technologies
* Django version 3.2
* Django filter version 2.4
* Django Rest Framework version 3.12.4
* drf-yasg version 1.20
* requests version 2.25.1

## Features
* Deployed on heroku: https://djangoapibooks.herokuapp.com/swagger/
* Downloading data about books from the website
* Adding downloaded data to the database
* Filtering and sorting data
* Swagger and redoc ui

To-do list:
* Adding an authentication method
* Unit tests

## Status
Project is: _finished_

## Inspiration
Recruitment task for STX Next.

## Contact
Created by [@exloIF_github](https://github.com/exploIF)
[exploIF_gmail](exploIF@gmail.com)- feel free to contact me!
