#Import libraries
import random
from flask import Flask, request, render_template

#Variables
project_ideas = [
    "Weather app",
    "Chatbot",
    "To-do list",
    "Image recognition",
    "Web scraper",
    "Sudoku solver",
    "URL shortener",
    "Password generator",
    "Quiz game",
    "Expense tracker",
    "Text-based RPG",
    "Music player",
    "Email sender",
    "Image gallery",
    "Calculator",
    "Currency converter",
    "File organizer",
    "Hangman game",
    "Random password generator",
    "Blogging platform",
    "BMI calculator",
    "Tic-tac-toe game",
    "Countdown timer",
    "URL checker",
    "Word cloud generator",
    "Image filter",
    "File encryption/decryption",
    "Twitter sentiment analysis",
    "RSS feed reader",
    "Contact book",
    "Maze generator/solver",
    "Note-taking app",
    "Password manager",
    "Calendar app",
    "Snake game",
    "Sentiment analysis of product reviews",
    "Recipe finder",
    "Data visualization",
    "Barcode/QR code reader",
    "Maze game",
    "Language translator",
    "News aggregator",
    "Password strength checker",
    "Image recognition from webcam",
    "Sudoku generator",
    "Text summarizer",
    "Recipe organizer",
    "Tic-tac-toe AI",
    "Data backup tool",
    "Cryptocurrency tracker"
]
Choice = random.choice(project_ideas)

app = Flask(__name__)

#Main code
@app.route("/")
def Index():
    return render_template("Index.html", Project = Choice)

@app.route("/Generate")
def Generate():
    Choice = random.choice(project_ideas)
    return render_template("Index.html", Project = Choice)

if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
