
# Boilerplate Flask with MongoDB & JWT (Restful API)

### Install MongoDB

> Ubuntu
`sudo apt install mongodb-org`

> Windows
Download [MongoDB](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/)

### Install Required

> Ubuntu
```
sudo apt-get install python3
sudo apt-get install python-pip
```
> Windows
Download [Python](https://www.python.org/downloads/release/python-386/)

> For all
``pip install virtualenv``

### Use Virtualenv

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```
>for Windows (poweshell)
`.\venv\Scripts\Activate.ps1 `

### set environment

```
set database for production or development in env.py
    Example: mongodb://localhost:27017

change development or production run in server.py
```



### Migration database

`echo 'db.create_all()' | ./server.py shell`


### Run server

`./server.py runserver`

**Creating Beautiful rest api slide**

    http://pycoder.net/bospy/presentation.html#title-slide

## ScreenShoot
![enter image description here](https://raw.githubusercontent.com/IbnuGunawanPrayogo/Flask_boilerplate/master/ScreenShoot.png)
