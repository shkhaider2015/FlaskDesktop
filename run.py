from myapp import create_app
from flaskwebgui import FlaskUI #get the FlaskUI class

app = create_app()

# Feed it the flask app instance 
ui = FlaskUI(app, width=1000, height=200)

# do your logic as usual in Flask
# @app.route("/")
# def index():
#   return "It works!"

# call the 'run' method
if __name__ == "__main__":
  ui.run()