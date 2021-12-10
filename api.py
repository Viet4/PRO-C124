from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "id": 1,
        "name": u"Bob",
        "contact": u"12345", 
        "done": False
    },
    {
        "id": 2,
        "name": u"Tim",
        "contact": u"24654", 
        "done": False
    },
    {
        "id": 3,
        "name": u"Jim",
        "contact": u"15634",
        "done": False
    },
]

@app.route("/add-data", methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide data"
        }, 400)

    task = {
        "id": contacts[-1]["id"]+1, 
        "name": request.json["name"],
        "contact": request.json.get("contact"), 
        "done": False
    }

    contacts.append(task)
    return jsonify({
        "status": "success",
        "message": "contact added successfully"
    })


if(__name__ == "__main__"):
    app.run(debug=True)