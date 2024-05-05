from translate import Translator
print("Saail Chavan - KFPMSCCS016 CL_P5a")

def translate_to_language(text, to_lang):
    translator = Translator(to_lang=to_lang)
    return translator.translate(text)
translations = {}
text = "Good Morning!"

# Translate to Marathi
translations["Marathi"] = translate_to_language(text, "marathi")
# Translate to Bengali
translations["Bengali"] = translate_to_language(text, "bengali")
# Translate to Kannada
translations["Kannada"] = translate_to_language(text, "kannada")
# Translate to Spanish
translations["Spanish"] = translate_to_language(text, "spanish")
# Translate to German
translations["German"] = translate_to_language(text, "german")
# Translate to Japanese
translations["Japanese"] = translate_to_language(text, "japanese")

for lang, translation in translations.items():
    print(f"{lang}: {translation}")

from googletrans import Translator
print("Saail Chavan - KFPMSCCS016 CL_P5b")

def translate_to_language(text, dest):
    translator = Translator()
    translation = translator.translate(text, dest=dest)
    return translation.text

to_translate = input("Enter a sentence to be translated: ")
translations = {}

# Translate to Marathi
translations["Marathi"] = translate_to_language(to_translate, "mr")
# Translate to Bengali
translations["Bengali"] = translate_to_language(to_translate, "bn")
# Translate to Kannada
translations["Kannada"] = translate_to_language(to_translate, "kn")
# Translate to Spanish
translations["Spanish"] = translate_to_language(to_translate, "es")
# Translate to German
translations["German"] = translate_to_language(to_translate, "de")
# Translate to Japanese
translations["Japanese"] = translate_to_language(to_translate, "ja")
print("Translations:")

for lang, translation in translations.items():
    print(f"{lang}: {translation}")
