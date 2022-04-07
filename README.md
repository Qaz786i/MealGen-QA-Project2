# MealGen-QA-Project2

This repository contains my project for the QA DevOps practical project.

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

Entity Diagram

In this project a data will be used to save and store data. This data will store the meeals and sides that will be randomly generated. The table is fairly simple it consists of an ID number for the meal, a main dish, a price for the main dish, a side dish, the price of the side dish and lastly the total price of the two dishes. The stored data can be seen on a history page showing all previous generated data. Below is an illustration of the entity diagram. 

![draw io](https://user-images.githubusercontent.com/99325859/162220951-fe5f5c22-5299-450e-ad57-47209bbbc8f8.png)

## App Design

For this project I have chosen to develop a random meal generator. This project follows the breif where 4 microservices were used and detailed below:

![arch](https://user-images.githubusercontent.com/99325859/162225020-b6dcb489-304e-43aa-ae5d-931428a3c83f.png)

- Front-end (aka Service 1): This is the service the user interacts with. This service sends requests to the other services to generate the random meals. It randomly generates the meals and also stores them in a SQL database.
- Service 2 : Service 2 is a HTTP GET request from service 1 and using random.choice() it randomly selects a main and its associated price.
- Service 3 : Service 3 is a HTTP GET request from service 1 and using random.choice() it randomly selects a side and its assocated price.
- Service 4 : Service 4 is HTTP POST request from service 1 which provides the randomly generated main and sides with prices as JSON objects. Service 4 uses a dictionary to add the total price of the randomly generated meals together.

Additionaly a reverse proxy using NGINX was used. NGINX allows traffic to be diverted to port5000 when port80 is busy. This allows the user to still have access to the front-end and have full access


## CI/CD Pipeline

This project had used a full CI/CD pipeline to fully test,build,deploy and maintain this application. The breakdown of the pipeline are as followed:

- Project Tracking
- Version Control
- Developer Environment
- CI Server 
- Deployment Enviroment

Project tracking was done using Trello. With this tasks were assigned and moved along as they were being completed.
{pic of trello board}

Git was used for version control whilst using giithub as the repository sotrage. Feature branches were added to the project to easily access each feature. This can be seen below from a screenshot of github

![feature branch](https://user-images.githubusercontent.com/99325859/162223671-bccee34d-5757-4e81-be0d-7db5f7ea16d3.png)

Jenkins was used for the Continuous Integration server (CI). Set up with a github webhook jenkins would clone the repository and run a jenkinsfile which stored all the script details. The pipeline had 4 main stages which were to test first, then build, then deploy to swarm and then lastly the post build actions which in this case were to artifact the coverage report from the tests. The test stages executes a bash script which then goes through every microservice and runs the predefined tests to check functionality using pytest. Use of unittest.mock and request_mock were both used to help with testing the api's and http request functionalities. The coverage of each service can be seen in the picture below

After the test stage came the build and push stage. This stage used docker-compise to build images for each services. Once done the script would then use given credentials to log into Dockerhub and push these images.

Once the images were successfully pushed the script would then move onto the deploy stage. The docker manager uses a secure copy to copy the nginx.conf and the docker-compose.yaml files. Ansible is used with a playbook to run the 3 stated roles. These roles are to first install docker on the swarm machines and then add jenkins to the docker group. The second role initializes a swarm on the manager node and used the ansible docker stack deploy command to deploy the application. Lastly the final role creates a swarm worker and adds it to the node. This creates our fully working pipeline

The finally the last stage of the build was the post-build stage. Here the test reports were published

![jenkins](https://user-images.githubusercontent.com/99325859/162224042-1c8a2046-a4da-4d93-8110-efb57b89d706.png)

Above is showcasing the jenkins pipeline. Successful builds display all green accross the stages and fails will have a red box. Any red boxes mean that the build had failed and will not deploy and any stages after will not commence until the error was rectified. As you can see there are some errors in the intial stages of the build. Build 3 had a test error. This error was due to a failed script in the test meaning a functionality was not working correctly or a test not written correctly. Build 4 had an error in the build an push stage. This was due to a credentials error which meant the script could not push the images to dockerhub and halting the build all together. Build 8 had an error in the deploy stages. This error was because the script is written to remove all images when starting a new build however for the first deployement there was no images. This was fixed by temporarily removing the rmi command. Build 100 and 102 show a fully working pipeline with no erros and shows succeful delpoyement of this application. Below is an illustration of the complete pipeline structure 

![microservices_architecture drawio](https://user-images.githubusercontent.com/99325859/162221721-fb4c2677-6e83-4ced-9212-f29d60ac843f.png)

## Known Issues

NA

## Future Work
 - A feature could be added where the user is able to add a main or a side of thier choice into dictionary
 - Drinks is a another class tgat could be added to make a complete meal 
