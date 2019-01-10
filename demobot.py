
# Import flask
from flask import Flask, request

# Create your app (web server)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def greet_person():
    # Get the value of the 'text' query parameter
    # request.values is a dictionary (cool!)
    name = request.values.get('text')
    # This bot says hi to every name it gets sent!
    return f'hi {name}!'
# When people visit the home page '/' use the hello_world function
@app.route('/1', methods=['GET', 'POST'])
def text0():
    return 'testing, hi'

@app.route('/ncss', methods=['GET', 'POST'])
def text1():
    return 'LIAMs'

if __name__ == '__main__':
    # Start the web server!
    app.run(debug=True)


