
# Import flask
from flask import Flask

# Create your app (web server)
app = Flask(__name__)


# When people visit the home page '/' use the hello_world function
@app.route('/')
def text0():
    return '<h2>AAAAAAAAAAAA!</h2>'

@app.route('/ncss')
def text1():
    return 'LIAMs'

if __name__ == '__main__':
    # Start the web server!
    app.run()
