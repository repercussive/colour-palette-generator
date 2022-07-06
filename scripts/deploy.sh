#!/bin/bash
scp docker-compose.yaml swarm-manager:/home/jenkins/docker-compose.yaml
scp nginx.conf swarm-manager:/home/jenkins/nginx.conf
ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml