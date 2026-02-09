# prompt_variator.py

import random

SYNONYMS = {
    "explain": ["describe", "clarify", "explain briefly"],
    "what is": ["define", "explain", "describe"],
    "give": ["provide", "share"],
    "brief": ["short", "concise"],
    "machine learning": ["ML"],
}

QUESTION_TEMPLATES = [
    "{prompt}",
    "Explain: {prompt}",
    "What is {prompt}?",
    "Give a brief explanation of {prompt}.",
]


def generate_variations(base_prompt: str, num_variations: int = 4):
    variations = set()

    base_prompt_lower = base_prompt.lower()

    for _ in range(num_variations * 2):
        prompt = base_prompt_lower

        for word, replacements in SYNONYMS.items():
            if word in prompt and random.random() > 0.5:
                prompt = prompt.replace(word, random.choice(replacements))

        template = random.choice(QUESTION_TEMPLATES)
        final_prompt = template.format(prompt=prompt).strip()

        variations.add(final_prompt.capitalize())

        if len(variations) >= num_variations:
            break

    return list(variations)
