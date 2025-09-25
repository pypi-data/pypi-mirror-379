import re
import py3langid as langid
import iso639 as languages


def alpha2_to_language(alpha2: str) -> str:
    if not alpha2:
        return None
    code = alpha2.strip().lower()
    return languages.to_name(code)

def language_to_alpha2(language_name: str) -> str:
    if not language_name:
        return None
    name = language_name.strip().lower()
    data = languages.find(name)
    return data["iso639_1"]

def detect_language(text, min_confidence=None):
    detector = langid.langid.LanguageIdentifier.from_pickled_model(
        langid.langid.MODEL_FILE, norm_probs=True
    )
    detected_lang, confidence = detector.classify(text)
    if min_confidence and confidence < min_confidence:
        return None, confidence
    detected_lang = re.sub("[^A-Za-z]", "", detected_lang).lower()
    detected_lang = languages.to_name(detected_lang).lower()
    return detected_lang, confidence

FLAIR_MODELS = {
    "en": "flair/ner-english-large",
    "es": "flair/ner-spanish-large",
    "de": "flair/ner-german-large",
    "nl": "flair/ner-dutch-large",
    "multi": "flair/ner-multi",
    "multi-fast": "flair/ner-multi-fast",
}

SPACY_MODELS = {
    "en": 'en_core_web_sm',
}

def load_language_model(language, type):
    from flair.models import SequenceTagger
    from spacy_download import load_spacy

    model = None
    match type:
        case "spacy":
            model_name = SPACY_MODELS.get(language, SPACY_MODELS["en"])
            model = load_spacy(model_name)
        case "flair":
            model_name = FLAIR_MODELS.get(language, "flair/ner-multi")
            model = SequenceTagger.load(model_name)
    return model