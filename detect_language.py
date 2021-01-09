from langdetect import DetectorFactory
DetectorFactory.seed = 0

# Detect the language of the sentence
from langdetect import detect

sentence = "Tanzania ni nchi inayoongoza kwa utalii barani afrika"

print(detect(sentence))