from flask import Flask, request

app = Flask(__name__)

@app.route('/poc1/<x>' , methods=["GET"])
def index(x):
    return "poc1 " + x

@app.route('/poc2/' , methods=["POST"])
def poc2():
    x = request.form["data"]
    return "poc2 " + x


@app.route('/number/' , methods=["GET"])
def list():
    x = [7,8,9]
    a = request.form["data"]
    return  x

@app.route("/mbr", methods = ["POST"])
def dicto():
    data=request.json
    print("length is ",data['length'])
    print("breadth is ",data["breadth"])
    dict1 = {"Perimeter": 20, "Area": 34}
    return dict1

if __name__ == "__main__":
    app.run(debug=True)