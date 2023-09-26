from flask import Flask, render_template, request
import openai

openai.api_key = "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"
completion = ""
Command = ""

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        global completion
        InputCommand = request.form["Command"]
        Command = InputCommand

        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": Command}])
        print(completion.choices[0].message.content)

        return render_template("Index.html", Response = completion)

    else:
        return render_template("Index.html", Response = "RESPONSE")
    

app.run(debug=True)