import requests
APIKey = "9f63bf9795ec432bb8d258b54555d42f"

response = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={APIKey}&category=technology")

data = response.json()
articles = data["articles"][:100]
Titles = []

for article in articles:
    title = article["title"]
    description = article["description"]
    Titles.append(title)

print(Titles)
