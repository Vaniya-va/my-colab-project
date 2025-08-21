from persian_text_pp.FarsiLanguageRecognition import is_farsi
from persian_text_pp.Normalize import normalize_text
from persian_text_pp.RemoveDiacritics import remove_diacritics
from persian_text_pp.RemovePunctuations import remove_punctuations
from persian_text_pp.RemoveRepeatingChar import remove_repeating_chars
from persian_text_pp.RemoveStopWords import remove_stopwords
from persian_text_pp.Tokenize import tokenize
from persian_text_pp.Lemmatizer import lemmatize


class PreprocessPipeline:
    """
    A class that encapsulates the preprocessing pipeline for Persian text.
    """

    def __init__(self):
        pass

    def preprocess_pipeline(self, text: str):
        """
        Preprocesses Persian text through all standard steps and returns tokens.
        """
        # Step 1: Detect if the text is Persian
        if not is_farsi(text):
            raise ValueError("❌ The input text is not in Persian.")

        # Step 2: Normalize the text
        text = normalize_text(text)

        # Step 3: Remove diacritics
        text = remove_diacritics(text)

        # Step 4: Remove punctuation
        text = remove_punctuations(text)

        # Step 5: Remove repeating characters
        text = remove_repeating_chars(text)

        # Step 6: Tokenize the text
        tokens = tokenize(text)

        # Step 7: Remove stopwords (operates on tokens)
        tokens = remove_stopwords(tokens)

        # Step 8: Lemmatize (operates on tokens)
        tokens = lemmatize(tokens)

        return tokens


# ----------- نحوه استفاده -----------
if __name__ == "__main__":
    pipeline = PreprocessPipeline()

    # متن ورودی خودت
    sample_text = "میخوام برم سینماااا! این فیلم خیلی خوبه 😍"
    result = pipeline.preprocess_pipeline(sample_text)

    print("✅ ورودی:", sample_text)
    print("✅ خروجی پردازش:", result)
