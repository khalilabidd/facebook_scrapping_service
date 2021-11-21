# facebook_scraping_service
facebook pages scraping service with fastapi

type these commands to dockerize the app and run it

docker build -t python-fastapi .
docker run -p 8000:8000 python-fastapi

if the webpage doesn't load change host parameter in main.py to '0.0.0.0'
