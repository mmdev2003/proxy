#!/bin/bash

apt update -y
apt upgrade -y

source $PWD/.env
nginx -t

# 1) Установка докера
chmod 777 $PWD/scripts/install-docker.sh
$PWD/scripts/install-docker.sh

# 4) Установка, конфигурация и запуск Backend
chmod 777 $PWD/scripts/init-backend.sh
$PWD/scripts/init-backend.sh

echo "$PWD"
