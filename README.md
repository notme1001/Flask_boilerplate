
# Boilerplate Flask with Mysql & JWT (Restful API)

### Install Mysql

> Ubuntu
`sudo apt-get install mysql-server`

> Windows
Download [MySql](https://dev.mysql.com/downloads/installer/) or install [xampp](https://www.apachefriends.org/download.html)

### Install Required

> Ubuntu
```
sudo apt-get install python3
sudo apt-get install python-pip
```
> Windows
Download [Python](https://www.python.org/downloads/release/python-386/)

In case Ubuntu  
`sudo apt-get install python-mysql.connector`

or 

In case Mac  
`brew install mysql-connector-python`

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
    Example: mysql://username:password@hostname:3306/database_name

change development or production run in server.py
```



### Migration database

`echo 'db.create_all()' | ./server.py shell`


### Run server

`./server.py runserver`

**Creating Beautiful rest api slide**

    http://pycoder.net/bospy/presentation.html#title-slide

## ScreenShoot
![enter image description here](https://i.ibb.co/DQW2WRV/Screen-Shoot.png)