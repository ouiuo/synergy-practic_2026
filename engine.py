from typing import List, Dict
from text_utils import normalize_text
from config import RULES, FALLBACK_MESSAGE


def score_rule(rule: Dict, text: str) -> int:
    score = 0
    for pattern in rule["patterns"]:
        if normalize_text(pattern) in text:
            score += 1
    return score


def get_answer(user_text: str, threshold: int = 1) -> str:
    normalized = normalize_text(user_text)

    best_score = 0
    best_answer = None

    for rule in RULES:
        score = score_rule(rule, normalized)
        if score > best_score:
            best_score = score
            best_answer = rule["answer"]

    if best_answer is None or best_score < threshold:
        return FALLBACK_MESSAGE

    return best_answer
