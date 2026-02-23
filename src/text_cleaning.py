def text_cleaning(text):
    import re
    # Remove URLs
    text = re.sub(r'http\S+|www.\S+', '', text)
    # Remove special characters
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    return text


def preprocess_text(text):
    # Convert text to lower case
    text = text.lower()
    # Strip white spaces
    text = text.strip()
    return text