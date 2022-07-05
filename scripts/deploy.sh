#!/bin/bash
scp docker-compose.yaml 10.182.0.2:/home/jenkins/docker-compose.yaml
scp nginx.conf 10.182.0.2:/home/jenkins/nginx.conf
ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml