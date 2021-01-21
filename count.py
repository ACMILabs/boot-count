from flask import Flask, redirect, request


app = Flask(__name__)
app.count = 1


@app.route('/')
def index():
    return redirect('/api/count/', code=302)


@app.route('/api/count/', methods=['GET', 'POST'])
def count():
    """
    Returns the number of times a container has booted.

    POST requests increment the count by 1
    GET requests return the current boot count
    """
    if request.method == 'POST':
        app.count += 1
    return {'count': app.count}
