
from googletrans import Translator, constants
from pprint import pprint

text = "Olorun mo fe"
    
def main(words):
    translator = Translator()

    #translate from whatever language to english
    translation = translator.translate(words)
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

if __name__ == "__main__":
    main(text)
