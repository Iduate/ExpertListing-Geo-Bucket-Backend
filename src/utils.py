from Levenshtein import distance as levenshtein_distance
import re

def normalize_location_name(name: str) -> str:
    # Lowercase, remove punctuation, trim whitespace
    name = name.lower()
    name = re.sub(r'[^a-z0-9 ]', '', name)
    name = name.strip()
    return name

def fuzzy_match(query: str, choices: list, threshold: int = 2):
    query_norm = normalize_location_name(query)
    matches = []
    for choice in choices:
        choice_norm = normalize_location_name(choice)
        dist = levenshtein_distance(query_norm, choice_norm)
        if dist <= threshold:
            matches.append(choice)
    return matches
