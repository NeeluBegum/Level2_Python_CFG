import requests
from flask import Flask, render_template, request
import tweepy

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


def myTweetMethod():
    #twitter apps
    auth=tweepy.OAuthHandler("Zi0zR6Y3kw2ly98wE7majMb55","9bA2086tHojvAUQL4EzMhMPnv3Wr4Lsnc6LbjyR8KaJY7btphB")
    auth.set_access_token("1011888746009067520-CEER93u9rCyHTe3Vu5BOiu13g7pXiT","sZU3fium2Lk9xS13T50uW0psFOxb97KuvyHqwnGuTYKoN")

    twitter_api=tweepy.API(auth)

    cfg_tweets=twitter_api.search(
    q="CodeFirstGirls"
    )
    rhc_tweets=twitter_api.search(
    q="ResearcHersCode"
    )

    for tweet in rhc_tweets:
      print(tweet.user.name + ":" + tweet.text +"\n")

    for tweet in cfg_tweets:
      print(tweet.user.name + ":" + tweet.text +"\n")


     return rhc_tweets[0].text


@app.route("/tweet")
def hellostranger1():
    firstTweet = myTweetMethod()
   return render_template("tweet.html", name = firstTweet)

# send_simple_message() #just to call method
if __name__ == '__main__':
    app.run(debug=True)
