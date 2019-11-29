import os
import random
import sayings as say
from bottle import route, run

def generate_message():
  return random.choice(say.beginnings) + ' ' + random.choice(say.subjects) \
   + ' ' + random.choice(say.verbs) + ' ' + random.choice(say.actions) \
   + ' ' + random.choice(say.ends)

@route("/")
def index():
  html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Генератор утверждений</title>
  </head>
  <body>
    <div class="container">
      <h1>Коллеги, добрый день!</h1>
      <p>{}</p>
      <p class="small">Чтобы обновить это заявление, обновите страницу</p>
    </div>
  </body>
</html>
""".format(generate_message())
  return html

@route("/api/generate/")
def get_message():
  return {"message": generate_message()}

@route("/api/generate/<num:int>")
def get_message_list(num):
  return {"messages": [generate_message() for _ in range(num)] }

if os.environ.get("APP_LOCATION") == "heroku":
  run(
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 5000)),
    server="gunicorn",
    workers=3,
    )
else:
  run(host="localhost", port=8080, debug=True)
