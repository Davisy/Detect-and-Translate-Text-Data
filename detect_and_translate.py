from langdetect import DetectorFactory
DetectorFactory.seed = 0

from langdetect import detect
from google_trans_new import google_translator  

#simple function to detect and translate text 
def detect_and_translate(text,target_lang):
    
    result_lang = detect(text)
    
    if result_lang == target_lang:
        return text 
    
    else:
        translator = google_translator()
        translate_text = translator.translate(text,lang_src=result_lang,lang_tgt=target_lang)
        return translate_text 
        
        

# Example        
sentence = "I hope that, when I’ve built up my savings, I’ll be able to travel to Mexico"

print(detect_and_translate(sentence,target_lang='sw'))


# output: Natumai kwamba, nitakapojiwekea akiba, nitaweza kusafiri kwenda Mexico 