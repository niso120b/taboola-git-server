from flask import Flask, render_template, request, session, redirect, url_for
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("Welcome to Taboola Git Server by Nissim Bitan")

@app.route("/about")
def about():
    aboutme = "About Me \n Nissim Bitan a Mamram alumni with 5 years of experience"
    print(about)


@app.route("/post_commit/", methods=['POST'])
def post_commit():
    json_data = request.get_json()
    req = json.loads(json_data)

    print("----------------Commit Details------------------")
    print("Author: {}".format(req["author"]))
    print("Email: {}".format(req["email"]))
    print("Repository Name: {}".format(req["name"]))
    print("Branch: {}".format(req["branch"]))
    print("Commit Message: {}".format(req["message"]))
    print("Files: ")
    for item in req["files"]:
        print(" {} : {}".format(item["type"], item["path"]))
    print("Diffs: ")
    for item in req["diff"]:
        print(" File: {}".format(item["file"]))
        print(" Diff: ")
        print(" {}".format(str(item["content"]).replace("\\n","\n")))
    print("------------------------------------------------")
    result = {"result": True}

    return json.dumps(result)

if __name__ == '__main__':
    app.run()
