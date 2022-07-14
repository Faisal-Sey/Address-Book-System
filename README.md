# Address-Book-System

## Setup Database 
- Database is based in postgresql
- Add database details in .env_prod under address_book_main/address_book_main
- Rename .env_prod -> .env
- db_host set to host.docker.internal worked on ubuntu 22.0.04

*If there are issues with connection server check this reference: https://www.phpfixing.com/2022/05/fixed-how-to-get-to-postgres-database.html?m=0*

## Setup Email 
- Add email details in address_book_main/address_book_main

## Start Server 
- Run *docker-compose up -d --build* to build database and needed services
- Run *docker-compose up* to start server
