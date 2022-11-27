from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """ English to French translation """
    textToTranslate = request.args.get('textToTranslate')
    french_text = translator.english_to_french(textToTranslate)
    return french_text

@app.route("/frenchToEnglish")
def french_to_english():
    """ English to French translation """
    textToTranslate = request.args.get('textToTranslate')
    french_text = translator.english_to_french(textToTranslate)
    return french_text

@app.route("/")
def render_index_page():
    """ Renders Index Page """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
