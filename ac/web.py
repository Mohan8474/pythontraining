from flask import Flask, request
from logic import calculate

app = Flask(__name__)


@app.route("/mbr", methods = ["POST"])
def dicto():
    data=request.json
    result  = calculate(data)
    return result

if __name__ == "__main__":
    app.run(debug=True)