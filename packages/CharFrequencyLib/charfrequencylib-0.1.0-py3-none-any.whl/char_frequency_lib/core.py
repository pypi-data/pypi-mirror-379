from collections import Counter

def char_frequency(text: str) -> dict:
    """Return a dictionary with frequency of each character"""
    return dict(Counter(text))
