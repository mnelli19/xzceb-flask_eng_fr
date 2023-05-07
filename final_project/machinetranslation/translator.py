
"""Module providing Function translate ."""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """Function to translate from english to french ."""
    output = ''
    if english_text:
        french_translations = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        print(json.dumps(french_translations, indent=2, ensure_ascii=False))
        output = french_translations.get("translations")[0].get("translation")
    return output

def french_to_english(french_text):
    """Function to translate from french to english ."""
    output = ''
    if french_text:
        english_translations = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        print(json.dumps(english_translations, indent=2, ensure_ascii=False))
        output = english_translations.get("translations")[0].get("translation")
    return output
