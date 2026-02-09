# llm_client.py

from transformers import pipeline

# Load once (cached by Streamlit / Python)
generator = pipeline(
    "text-generation",
    model="distilgpt2",
    device=-1  # CPU
)


def query_llm(prompt: str, max_tokens: int = 100):
    engineered_prompt = (
        "You are an AI assistant.\n"
        "Answer the following question clearly and concisely:\n\n"
        f"{prompt}\n\nAnswer:"
    )

    response = generator(
        engineered_prompt,
        max_new_tokens=max_tokens,
        do_sample=True,
        temperature=0.7,
        pad_token_id=50256
    )

    return response[0]["generated_text"].replace(engineered_prompt, "").strip()

