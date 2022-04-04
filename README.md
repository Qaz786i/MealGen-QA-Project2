# MealGen-QA-Project2

## Contents: 

- Project Breif
- Project Planning
- App Design
- CI/CD Pipeline
- Known Issues
- Future Work

## Project Brief

The brief for this project was to produce an application consisting of four microservices, which interact with eachother to randomly generate objects using defined logic. The application was to be produced and was maintained using an automated CI/CD pipeline. There were many technologies impletemented into this project which are all listed below:

- Trello board for project tracking
- Git for version control
- Jenkins for our CI server
- Ansilble for configuration management
- GCP cloud platform for our VM's
- Docker as our containerisation tool
- Docker swarm for container ocherisation
- NGINX as a reverse proxy

## Project Planning

A risk assesment was one of the project planning requirements for the project and was undertaken to identify any potential risks. This assesment can be seen below 

![risk assesment](https://user-images.githubusercontent.com/99325859/161582489-96501bab-7770-45a3-bffb-5838b0b33a2b.png)

Each risk was given a score for probability of how likely the event would take place and a score for how it would effect the project if the event took place. This assesment would help with applying extra measures to the project such as not adding passwords to the code and pushing them to github. Control measures were observed throughout the project

## App Design

For this project I have chosen to develop a random meal generator. This project follows the breif where 4 microservices were used and detailed below:

- Front-end (aka Service 1): This is the service the user interacts with. This service sends requests to the other services to generate the random meals. It randomly generates the meals and also stores them in a database.
- Service 2 : Service 2 is a HTTP GET request from service 1 and using random.choice() it randomly selects a main and its associated price.
- Service 3 : Service 3 is a HTTP GET request from service 1 and using random.choice() it randomly selects a side and its assocated price.
- Service 4 : Service 4 is HTTP POST request from service 1 which provides the randomly generated main and sides with prices as JSON objects. Service 4 uses a dictionary to add the total price of the randomly generated meals together.

Additionaly a reverse proxy 


## CI/CD Pipeline



## Known Issues



## Future Work
