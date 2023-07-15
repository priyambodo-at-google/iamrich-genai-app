#/bin/bash
docker build -t iamrich-app .
docker run -v apikey.json:/apikey.json -e GOOGLE_APPLICATION_CREDENTIALS=apikey.json -p 8080:8080 iamrich-app
