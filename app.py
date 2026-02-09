# app.py

import streamlit as st

from prompt_variator import generate_variations
from llm_client import query_llm

st.set_page_config(
    page_title="PromptGuard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ PromptGuard")
st.subheader("LLM Prompt Robustness & Stability Tester")

st.markdown(
    """
PromptGuard helps you analyze how **small prompt changes**
can affect an LLM's output.

👉 Enter a base prompt, generate variations, and compare responses.
"""
)

# --- User Inputs ---
base_prompt = st.text_area(
    "Enter base prompt",
    height=120,
    placeholder="Explain overfitting in machine learning"
)

num_variations = st.slider(
    "Number of prompt variations",
    min_value=2,
    max_value=6,
    value=4
)

run_button = st.button("🚀 Run PromptGuard")

# --- Processing ---
if run_button:
    if not base_prompt.strip():
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("Generating prompt variations..."):
            variations = generate_variations(base_prompt, num_variations)

        st.markdown("---")
        st.subheader("🔍 Results")

        for idx, prompt in enumerate(variations, start=1):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"### ✏️ Prompt {idx}")
                st.code(prompt)

            with col2:
                st.markdown("### 🤖 LLM Response")
                with st.spinner("Querying model..."):
                    response = query_llm(prompt)
                st.write(response[:600] + ("..." if len(response) > 600 else ""))

            st.markdown("---")
