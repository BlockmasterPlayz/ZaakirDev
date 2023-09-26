from flask import Flask, render_template
import requests

app = Flask(__name__)
APIKey = "9f63bf9795ec432bb8d258b54555d42f"
r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={APIKey}&category=technology")

NewsTitleArray = []
NewsDescriptionArray = []

Index = 0

@app.route("/", methods=['GET'])
def GetNews():
    global Index
    if r.status_code == 200:
        data = r.json()
        articles = data["articles"][:100]

        for article in articles:
            title = article["title"]
            description = article["description"]

            NewsTitleArray.append(title)
            NewsDescriptionArray.append(description)
        return render_template("FirstNews.html", NewsTitle = NewsTitleArray[Index], Desc = NewsDescriptionArray[Index])

    else:
        print("Error:", r.status_code)
    
    

@app.route("/Next")
def Next():
    global Index

    if Index == 99:
        Index = 0
        return render_template("FirstNews.html", NewsTitle = NewsTitleArray[Index], Desc = NewsDescriptionArray[Index])
    
    else:
        Index = Index + 1
        return render_template("FirstNews.html", NewsTitle = NewsTitleArray[Index], Desc = NewsDescriptionArray[Index])

app.run(debug=True, host='0.0.0.0', port=80)