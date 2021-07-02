# mnhentai

## A web implementation to use with [nhentai](https://github.com/RicterZ/nhentai)

Running a (lazilly put together) local web server to deliver your doujins in web format.



## Setup
### Create database:
Inside the first ``mnhentai`` directory run:  
```bash
python manage.py makemigrations &&
python manage.py migrate &&
python manage.py runserver 0.0.0.0:8080
```

Go to [initialize page](http://INSERT_YOUR_LOCAL_IP:8080/nhentai/initialize/), insert the path to your doujinshis directory and click "Generate Database".  
It will take some time (400 doujins ~ 20 seconds, running on SSD, but there are other factors, so take this approximation with a grain of salt).  

When the database is ready, a page saying how many doujinshis were imported will be loaded.  

Now you only have to run a server for the doujins images.  
Edit the file ``image_server.py``, inserting the value for the variable ``DOUJINS_PATH``. USE '/' FOR PATHING. E.G.:  
```python
DOUJINS_PATH = 'H:/nhentai/downloads/'
```

## Usage
Once all is setup you just have to:  
```bash
python manage.py runserver 0.0.0.0:8080 &
python run_image_server.py &
```
And access http://INSERT_YOUR_LOCAL_IP:8080/nhentai/


## Disclaimer

Do NOT use this as a "production" server. It was meant to be used in local network only.
Do NOT use this if you are in dangerous local network.
I'm a firmware guy, and have no idea what I did in the frontend/backend. :D
