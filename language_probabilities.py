from langdetect import DetectorFactory
DetectorFactory.seed = 0

# show probabilities for the top languages
from langdetect import detect_langs

sentence = "Tanzania ni nchi inayoongoza kwa utalii barani afrika"

print(detect_langs(sentence))