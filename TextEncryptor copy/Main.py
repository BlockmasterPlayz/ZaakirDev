from flask import Flask, render_template, request

app = Flask(__name__)

TextToEncrypt = ""
EncryptionKey = 0
Encryptionresult = "Type the text you want to Encrypt:"

TextToDecrypt = ""
DecryptionKey = 0
Decryptionresult = "Type the text you want to Decrypt:"

@app.route("/")
def Index():
    return render_template("Index.html")

@app.route("/Encrypt", methods=["GET", "POST"])
def Encrypt():
    global Encryptionresult

    if request.method == "POST":
        InputtedText = request.form["TextToEncrypt"]
        InputtedKey = int(request.form["key"])

        TextToEncrypt = InputtedText
        EncryptionKey = InputtedKey

        Encryptionresult = ""

        for i in range(len(TextToEncrypt)):
            char = TextToEncrypt[i]
            
            if char.isupper():
                Encryptionresult += chr((ord(char) + EncryptionKey - 65) % 26 + 65)
            elif char.islower():
                Encryptionresult += chr((ord(char) + EncryptionKey - 97) % 26 + 97)
            else:
                Encryptionresult += char
        return render_template("Encrypt.html", Result = Encryptionresult)

    else:
        return render_template("Encrypt.html")
    

@app.route("/Decrypt", methods=["GET", "POST"])
def Decrypt():
    global Decryptionresult

    if request.method == "POST":
        InputtedText = request.form["TextToDecrypt"]
        InputtedKey = int(request.form["key"])

        TextToDecrypt = InputtedText
        DecryptionKey = InputtedKey

        Decryptionresult = ""

        for i in range(len(TextToDecrypt)):
            char = TextToDecrypt[i]
            
            if char.isupper():
                Decryptionresult += chr((ord(char) - DecryptionKey - 65) % 26 + 65)
            elif char.islower():
                Decryptionresult += chr((ord(char) - DecryptionKey - 97) % 26 + 97)
            else:
                Decryptionresult += char

        return render_template("Decrypt.html", Result = Decryptionresult)

    else:
        return render_template("Decrypt.html")


app.run(host="0.0.0.0", port=80)