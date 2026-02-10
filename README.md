# 🛡️ PromptGuard

**LLM Prompt Robustness & Stability Tester**

PromptGuard is an evaluation tool that analyzes how small variations in prompt wording can lead to significant differences in Large Language Model (LLM) responses. The project focuses on **prompt sensitivity, response instability, repetition, and semantic drift**, rather than answer correctness.

---

## 🚀 Live Demo
🔗 https://promptguard-llm-robustness.streamlit.app

---

## 🧠 Motivation

LLMs often appear reliable, but minor rewording of prompts can cause:
- Hallucinations
- Repetition
- Topic drift
- Inconsistent reasoning

PromptGuard was built to **visually and interactively demonstrate these behaviors**, highlighting the importance of robust prompt design in real-world AI systems.

---

## 🏗️ Architecture

- **Frontend:** Streamlit
- **Prompt Variation Engine:** Deterministic rule-based paraphrasing
- **LLM:** Local lightweight model (`distilgpt2`)
- **Inference:** CPU-only, no external APIs
- **Deployment:** Streamlit Community Cloud (free tier)

---

## 🔍 How It Works

1. User enters a base prompt
2. System generates controlled prompt variations
3. Each variation is passed to the LLM
4. Responses are displayed side-by-side for comparison

This makes instability and sensitivity immediately visible.

---

## ⚙️ Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- distilgpt2 (local inference)

---

## 🧪 Key Observations

- Semantically similar prompts can produce wildly different outputs
- Lightweight models amplify instability, making robustness issues clearer
- Imperfect outputs are treated as **signal**, not noise

---

## 📌 Key Learnings

- Prompt engineering is critical for LLM reliability
- Evaluation tools are as important as generation systems
- Deployment constraints strongly influence model choices

---

## 📄 License
MIT
