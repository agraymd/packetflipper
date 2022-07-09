# **Packet Flipper - Introduction**
Packet Flipper is a web application made using Django that presents three common types of IP subnetting questions you would find on a test like the Cisco CCNA. 


The site gives users three styles of question: 

-What is the network address given an IP address and CIDR mask  
-What is the longest subnet mask to accommodate an amount of hosts required  
-How many hosts and subnets are available given an IP address and CIDR Mask  

The project evolved from working to learn basic python skills. Using the ipaddress python module, I was able to create an unlimited source of IP subnetting practice questions by coding the logic in python. 

## **Technologies**

This project created a fun set of challenges and the chance to work with many technologies and concepts such as: 

Python \
Git \
Nginx \
Postgres (SQL Database) \
Django \
Gunicorn \
AWS (EC2, Route53, IAM. . . ) \
Linux \
Let’s Encrypt / Certbot (SSL/TLS Certificates) \
Information Security (Environment variables, server hardening and best practices, etc). \





### **Launch the Project Locally**
#### **Running the project locally requires the following prerequisites to be installed (commands shown using Debain 10 system):** 

`sudo apt install git`   
`sudo apt install python3-pip`  
`sudo apt install virtualenv`   
`sudo apt install postgresql postgresql-contrib`   

#### **Create a Database for the Project**
`sudo -u postgres psql`  
`CREATE DATABASE database_name;`  
`CREATE USER db_username WITH PASSWORD 'your_password';`  
`ALTER ROLE myprojectuser SET client_encoding TO 'utf8';`  
`ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';`  
`ALTER ROLE myprojectuser SET timezone TO 'UTC';`  
`GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;`  
`\q`  

#### **Clone the Repo**
`sudo git clone https://github.com/agraymd/packetflipper.git`

#### **Create virtualenv for the Project**
`sudo virtualenv packetflipper_env`  
`source packetflipper_env/bin/activate`  

#### **Install Requirements**
`pip3 install -r requirements.txt`  
 
#### **Create .env File for Sensitive Items**  
`cd /packetflipper/packetflipper/subnet_app/subnet_app/`  
`sudo touch ./.env`  

SECRET_KEY=your_secret_key  
DATABASE_NAME=postgresdatabase                               
DATABASE_USER=alice                                          
DATABASE_PASS=your_password                        
ALLOWED_HOSTS=X.X.X.X,  

*Note: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` will print the secret key you need for your .env file.*

#### **Run Migrations**
`python3 manage.py makemigrations`
`python3 manage.py migrate`

This should be all you need to start the development server and work on the project locally. Deploying to production is possible through a variety of avenues after that. 

*Note: Static files will not be served by the development server of Django while DEBUG is set to False in settings. You can use the  `--insecure` flag to bypass this for development/testing*


### **Notes about logic / project function**
- The ipaddress Python module is used as the basis for creating the questions. A random IP address is generated and used in various ways to create the question generation and checking logic. This is stored in the /labs/views.py file. 


- JavaScript is used to create the ‘game’ functionality on the website front end. The correct answer is stored in the python code, and is printed in a hidden div container. On Click of the check answer button, javascript changes div class values based on checking the user’s input. CSS is used for styling / display functionality. This is stored in the packetflipper/subnet_app/labs/templates/labs/index.html file and /static/ JavaScript and CSS files.


## **Setting up Production on AWS**
Coming soon!




## Improvements 

This project could benefit from the following: 

-Testing (Learning about code testing is on the agenda, perhaps I will use this project to do so)  
-Monitoring / Statistics once deployed to a "production" setup  
-CI/CD when in production  
-Set up to scale / load balance 
-Automated launch / easy teardown of production system  
-Detailed documentation about process of dev to deploy, etc.  
-A users system where users can login and keep score of some type, questions correct total, streak, etc. 
