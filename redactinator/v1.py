from presidio_analyzer import AnalyzerEngine


def redact(text, preserve_entities=set()):
    results = AnalyzerEngine().analyze(text=text, language="en")

    mapping = {}
    for result in results:
        word = text[result.start:result.end]
        mapping[word] = result.entity_type

    for word, entity_type in mapping.items():
        if entity_type not in preserve_entities:
            text = text.replace(word, entity_type)

    return text