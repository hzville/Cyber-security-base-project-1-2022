## University of Helsinki Cyber Security Base 2022, project 1.

This repository contains an insecure web application for the Cyber Security Base course. The application contains multiple security vulnerabilities, and the code should not be used in any real-world application. The task is to point out some of the vulnerabilities in the application and describe how they can be fixed.

---


Link to the repository: https://github.com/hzville/Cyber-security-base-project-1-2022 

How to install: 

The application is implemented with Flask which is a framework written in Python. To run the application, you will need a basic installation of Python and Git. You also need to install the additional dependencies needed from the requirements.txt file to run the application. 

Required Python version: 3.8 or newer. The app is implemented with Python 3.8. The functionality of the application cannot be guaranteed with older versions of Python. You can download and install Python from https://www.python.org/ . 

Required Git version: 2.0 or newer. You can download Git from https://git-scm.com/

It's also recommended to create a Python virtual environment inside the downloaded project repository. This way you get an isolated developing environment and the possibility to utilize the requirements.txt file to get the exact versions of the needed dependencies. More information about Python virtual environments: https://docs.python.org/3/tutorial/venv.html

---

1. Install Python and Git
 
2. Use git clone to get the project to your computer

``` 

git clone https://github.com/hzville/Cyber-security-base-project-1-2022.git 

```  

3. Create a Python virtual environment to the same folder where you cloned the project. 

``` 

python3 -m venv virtual-env 

``` 

4. Activate the virtual environment 

On Unix or MacOS run:
``` 

source virtual-env/bin/activate 

``` 
On Windows run:
```
virtual-env\Scripts\activate.bat
```

5. Install the dependencies from the requirements.txt file 

``` 

pip install -r requirements.txt 

``` 

6. Initialize the mock database with command 

``` 

python3 create_mock_db.py 

``` 

7. Move to the src/ folder and run the application with command 

``` 
cd src/

flask run 

``` 

---

## FLAW 1: 

### Location of flaw: 
https://github.com/hzville/Cyber-security-base-project-1-2022/blob/master/src/app.py#L56
 
 
### Description of flaw: 

Name of flaw: A01:2021-Broken Access Control 

The application has an issue with access control. With this issue present, it's possible to get access to any existing account information by changing the url parameters. The basic functionality is that it's possible to fetch account data by the view account function found in app.py file. The data is fetched by calling url http://127.0.0.1:5000/view-account/\<username>\. When inserting any valid username into the \<username> parameter, it's possible to get unauthorized data.  

How to fix the flaw: 

It's possible to fix the flaw by validating the view account request. The easiest way would be to check that the user is logged in when requesting data and that the username of the logged user matches the username provided in the url. This way it's only possible to fetch data of an account that's logged in.  

## FLAW 2: 

### Location of flaw: 
https://github.com/hzville/Cyber-security-base-project-1-2022/blob/master/src/db_queries.py#L16

### Description of flaw: 

Name of flaw: A02:2021-Cryptographic Failures 

The application saves passwords in plain text into the database. This leads to exposure of sensitive data in case of a breach. This also exposures sensitive data to any people maintaining the database, such's as developers. 

How to fix the flaw: 

Passwords and other sensitive data should be stored strongly encrypted. This can be done by hashing the password when creating a new user. When the new user is logging in, the same hash function is used and compared to the hashed password in database. If they match, then the user is logged in, otherwise the request is rejected.  

## FLAW 3: 

### Location of flaw: 
https://github.com/hzville/Cyber-security-base-project-1-2022/blob/master/src/db_queries.py#L20
### Description of flaw: 

Name of flaw: A03:2021-Injection 

The SQL requests are not validated and sanitized in any way. This makes it possible for SQL injection attacks. With a maliciously crafted SQL query, an attacker could possibly retrieve, delete and make unauthorized changes to data in the database. 

How to fix the flaw: 

All SQL requests should be validated and sanitized before execution. It should not be possible to modify the SQL request by sending maliciously crafted SQL queries and any attempts to do so should be rejected. 

## FLAW 4: 

### Location of flaw: 
https://github.com/hzville/Cyber-security-base-project-1-2022/blob/master/src/app.py#L43

### Description of flaw: 

Name of flaw: A07:2021-Identification and Authentication Failures 
 
When creating a new user, the password input and creation has no checks for default, weak or well-known passwords. This makes it possible to create user accounts with insecure passwords which makes the accounts prone to brute force or other automated attacks. In this kind of attack the attacker can try to brute force the correct password with the help of automatic password guessing tools. 

How to fix the flaw: 
 
When creating passwords for new accounts, there should be a check for weak passwords, requirement of password length and complexity and a rotation policy meaning how often passwords should be changed.  

## FLAW 5: 

### Location of flaw: 

https://github.com/hzville/Cyber-security-base-project-1-2022/blob/master/src/app.py#L17

### Description of flaw: 

Name of flaw: CSRF, Cross site request forgery 

The application is missing protection against cross site request forgery. This leads to a possibility for a malicious actor to capture the authentication cookie from an authenticated user. When the authentication cookies are captured, can the malicious actor make request like changing the password for the targeted user. 

How to fix the flaw: 

A random CSRF token should be assigned to to user when he logs in to the website. Additionally, when making any requests from the frontend to the backend, like with the form for changing users password, should there be a check that the requests contain the same CSRF token as the users CSRF token. If the CSRF token is missing or not included in the request, should it be rejected.