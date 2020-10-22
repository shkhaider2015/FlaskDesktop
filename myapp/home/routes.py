from flask import Blueprint, render_template

Home = Blueprint('Home', __name__)

@Home.route('/')
@Home.route('/home')
def method_name():
   return render_template("testing.html")