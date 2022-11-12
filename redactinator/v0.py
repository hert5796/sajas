from presidio_analyzer import AnalyzerEngine

def redact(text):
    results = AnalyzerEngine().analyze(text=text, language="en")

    mapping = {}
    for result in results:
        word = text[result.start:result.end]
        mapping[word] = result.entity_type

    for word, type in mapping.items():
        text = text.replace(word, type)

    return text