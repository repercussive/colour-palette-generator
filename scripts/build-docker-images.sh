#!/bin/bash
docker login -u $DH_USERNAME -p $DH_PASSWORD
docker-compose build --parallel
docker-compose push
docker logout