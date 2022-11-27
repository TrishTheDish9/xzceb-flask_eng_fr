""" Translator Functions"""
import json
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

# Set variables
api_key = os.environ['apikey']
api_url = os.environ['url']

# Prepare Authenticator
authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(version = '2018-05-01', authenticator = authenticator)

language_translator.set_service_url(api_url)
language_translator.set_disable_ssl_verification(True)

# E2F Translator Function
def english_to_french(english_text):
    """ Function English to French Translation """
    french_text = language_translator.translate(
        text = english_text,
        model_id = 'en-fr'
    ).get_result()
    return french_text.get("translations")[0].get("translation")

# F2E Translator Function
def french_to_english(french_text):
    """ Function French to English Translation """
    english_text = language_translator.translate(
        text = french_text,
        model_id = 'fr-en'
    ).get_result()
    return english_text.get("translations")[0].get("translation")
