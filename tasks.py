from models import TranslationModel

# store_translation
# Take in a translation request and save it to the database
def store_translation(t):
    model = TranslationModel(text=t.text, base_lang=t.base_lang, final_lang=t.final_lang)
    model.save()
    return model.id 

# run_translation
# run a pretrained deep learning model

# find_translation
# retrieve a translation from the database