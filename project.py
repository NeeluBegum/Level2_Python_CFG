import requests
from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def hello():
   return "Hello ››"
@app.route("/<name>")
def hellostranger1(name):
   return render_template("project.html", name = name.title())

@app.route("/project")
def hellostranger2():
   return render_template("project.html")

@app.route("/getinfo")
def hellostranger3():
   return render_template("info.html")

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print(form_data["email"])
    send_simple_message(form_data["email"], form_data["company"])
    return "Please check your email, we have sent you more information"

def send_simple_message(mail, company): #defines method
   return requests.post(
       "https://api.mailgun.net/v3/sandbox54c16559663e4cf98a02f9530a606093.mailgun.org/messages",
       auth=("api", "100c344a0d39b9b769c8618bb8426859-7caa9475-98875104"),
       data={"from": "Excited User <mailgun@sandbox54c16559663e4cf98a02f9530a606093.mailgun.org>",
             "to": [mail],
             "subject": "Info about {}".format(company),
             "text": "Here is more information!"})

# send_simple_message() #just to call method
if __name__ == '__main__':
    app.run(debug=True)
