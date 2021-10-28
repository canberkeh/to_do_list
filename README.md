# To-do-list-project with Django

## Introduction
This project is build with django. 

## How to run project
Run command under the project root.
<code> docker-compose up --build </code>

![screenshot 5](https://user-images.githubusercontent.com/73230039/115119813-f8acc780-9fb2-11eb-8004-686bd59c652c.jpg)

### You can view on browser after successfully building project.
0.0.0.0:8000 - 
127.0.0.1:8000 - 
localhost:8000

### To list docker containers to get container ID
 <code> docker ps </code>

![screenshot 6](https://user-images.githubusercontent.com/73230039/115119874-40335380-9fb3-11eb-9761-ad7ddaa54a8b.jpg)

### To create a super user, use this command
<code> docker exec -it [CONTAINER ID] python manage.py createsuperuser </code>

![screenshot 7](https://user-images.githubusercontent.com/73230039/115119934-8a1c3980-9fb3-11eb-9b8d-3165f7441203.jpg)

### Now you can use django-admin
<code> 0.0.0.0:8000/admin </code>

To check expired items, run this command:
<code> docker exec -it [CONTAINER_ID] python manage.py check_expired_items </code>

## Deploy on Heroku
https://todo-app-case-study.herokuapp.com/

![sss](https://user-images.githubusercontent.com/73230039/118378249-22213900-b5db-11eb-90ab-2fe0d882929c.jpg)

![screenshot 1](https://user-images.githubusercontent.com/73230039/118394431-5c2b2300-b64d-11eb-8ea1-41f6f3211b0a.jpg)
