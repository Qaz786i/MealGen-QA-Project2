export MYSQL_ROOT_PASSWORD
docker stack deploy --compose-file docker-compose.yaml meal-gen-stack
docker service update --replicas 3 meal-gen-stack_front-end