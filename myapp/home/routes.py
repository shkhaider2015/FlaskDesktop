from flask import Blueprint

Home = Blueprint('Home', __name__)

@Home.route('/')
@Home.route('/home')
def method_name():
   return("Home Works !!")