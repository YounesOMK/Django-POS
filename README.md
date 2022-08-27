# Django-POS
Point of sale project (done using [Django](https://github.com/django/django), [Alpine.js](https://github.com/alpinejs/alpine), [HTMX](https://github.com/bigskysoftware/htmx), [TailwindCSS](https://github.com/tailwindlabs/tailwindcss)).

Done as an internship project for [JDI SOFT](https://jdi-soft.com/)  
[![JDI SOFT logo](apps/theme/static/images/logo.png)](https://jdi-soft.com/)

# How To Use

- clone the project
  ```
  git clone https://github.com/YounesOMK/Django-POS
  ```
- cd into the project
  ```
  cd Django-POS
  ```
- Create virtual environment
  ```
  python -m venv env
  ```
- Activate the virtual environment
  ```
  source env/bin/activate
  ```
- install requirements
  ```
  pip install -r requirements/local.txt 
  ```
- Run migrations
  ```
  ./manage.py migrate
  ```
- Create a superuser
  ```
  ./manage.py createsuperuser
  ```
- run the server
  ```
  ./manage.py runserver 3000
  ```
# Models
![Models](/screenshots/models.png)

# Some screenshots
![English home page](/screenshots/home_page_en.png)  
![Arabic home page](/screenshots/home_page_ar.png)  
![English stats page](/screenshots/stats_en.png)  
![French inovice page](/screenshots/inovice_fr.png)







