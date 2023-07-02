# upload_project
This Python Django project takes a pdf file as input and shows a loading symbol and then uploads the pdf to the server
Here the logic is first uploaded file will be at first and second uploaded file will merge at the bottom
Firstly install PyPDF2 library by command >> pip install PyPDF2
Open the virtual environment to run the Django Project 
>> py -m venv myenv // replace myenv with the name of your virtual environment
>> myenv\Scripts\activate.bat
After setting up the environment, create a new Django project
>> django-admin startproject pdf_merge_app
>> cd pdf_merge_app
Create a new Django app within the project
>> python manage.py startapp pdf-merge
And then add the given codes to the respective sections
