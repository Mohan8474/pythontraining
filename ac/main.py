from flask import Flask

app = Flask(__name__)

@app.route('/admin' , methods=["POST"])
def index():
    return 'Web App with Python Flask!'

app.run(debug=True)