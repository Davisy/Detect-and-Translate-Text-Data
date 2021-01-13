# translate a sentence from swahili to english langauge

from google_trans_new import google_translator  

translator = google_translator()

sentence = "Tanzania ni nchi inayoongoza kwa utalii barani afrika"
translate_text = translator.translate(sentence,lang_tgt='en')  

print(translate_text)
