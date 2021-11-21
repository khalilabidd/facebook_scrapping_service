# facebook_scrapping_service

Run ```python ./app/main.py``` to launch the app after installing the requirements ( ```pip install requirements.txt ```)


Type these commands to dockerize the app and run it

```docker build -t python-fastapi .```

```docker run -p 8000:8000 python-fastapi```

if the webpage doesn't load change host parameter in main.py to '0.0.0.0'


The app load the posts from a facebook public page and store it in a database.

Once you run the app add the name of the page to the address bar.
