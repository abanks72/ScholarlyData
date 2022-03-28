# ![Google_Scholar_Data_Scrape_🔣 (1)](https://user-images.githubusercontent.com/34845263/160322151-7db1462b-60a8-4860-9a82-b77d75f8c472.png)
<a href="https://github.com/abanks72/ScholarlyData/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/abanks72/ScholarlyData"></a>
<a href="https://github.com/abanks72/ScholarlyData/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/abanks72/ScholarlyData"></a>
<a href="https://github.com/abanks72/ScholarlyData/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/abanks72/ScholarlyData"></a>
## Overview
A Program that takes Google Scholar data using the Scholarly python package. In this iteration of the program, it takes 
a professor's name as input and stores their name and H-index in a database, and displays them on a webpage. 
Technologies being used are: Flask, Flask-SqlAlchemy/SQLite, Python, HTML, & CSS (Bootstrap).
## Installation 
In directory root or virtual enviroment: 
```python
pip install Flask
pip install -U Flask-SQLAlchemy
pip install scholarly
```
## Configuration
Initialize the database.

In command line open python interpreter with argument: `python`
```
db.create_all()
exit()
```

## Running The Project
in command line run:
```
ENV:FLASK_APP = "app"
python -m flask
flask run
```

## License
<a href="https://github.com/abanks72/ScholarlyData"><img alt="GitHub license" src="https://img.shields.io/github/license/abanks72/ScholarlyData"></a>
