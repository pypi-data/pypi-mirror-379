# 🧠 leo-prompt-optimizer

**leo-prompt-optimizer** is a Python library that helps developers **optimize raw LLM prompts** into structured, high-performance instructions using real LLM intelligence.

It leverages **open-source models via [Groq API](https://console.groq.com/)** (like Mixtral or LLaMA 3), and also supports OpenAI, making it fast, flexible, and production-ready.

---

## 🚀 Features

- 🛠️ Refines vague, messy, or unstructured prompts
- 🧠 Follows a 9-step prompt engineering framework
- 🧩 Supports contextual optimization (with user input & LLM output)
- 🔁 Works with both Groq **and** OpenAI
- ⚡ Blazing-fast open models via Groq
- 🔐 Secure API key management with `.env` or helper function
- 🎛️ Let users choose model (`gpt-3.5-turbo`, `mixtral-8x7b`, `llama3`, etc.)

---

## 📦 Installation

```bash
pip install leo-prompt-optimizer
````

---

## 🔧 Setup: API Keys

You can provide your API key in two ways:

### ✅ Option A: `.env` file (recommended)

At the root of your project, create a `.env` file:

```env
GROQ_API_KEY=sk-your-groq-key
or
OPENAI_API_KEY=sk-your-openai-key
```

Then, in your Python script:

```python
from dotenv import load_dotenv
load_dotenv()  # 👈 Required to load the API keys from .env
```

---

### ✅ Option B: Set programmatically

```python
from leo_prompt_optimizer import set_groq_api_key, set_openai_api_key

set_groq_api_key("sk-your-groq-key")
set_openai_api_key("sk-your-openai-key")
```

---

## ✍️ Usage Example

```python
from dotenv import load_dotenv
load_dotenv()  # Only needed if using .env for API keys

from leo_prompt_optimizer import optimize_prompt, set_groq_api_key, set_openai_api_key

# Optional: Set API key manually (Groq or OpenAI)
# set_openai_api_key("sk-...")
# set_groq_api_key("sk-...")

optimized = optimize_prompt(
    prompt_draft="[YOUR PROMPT]",
    user_input="[POTENTIAL INPUT EXAMPLE]", # Optional
    llm_output="[POTENTIAL OUTPUT EXAMPLE]", # Optional
    provider="[YOUR PROVIDER]",               # "groq" (default) or "openai"
    model="[YOUR MODEL]",            # Optional: model choie based on your provider(e.g. "gpt-4", "llama3-70b", etc.)
    base_url="[YOUR BASE_URL]"       # Optional: if you have a specific base url
)

print(optimized)
```

> 🧠 `user_input` and `llm_output` are optional but helpful when refining an existing prompt flow.
> 🎛️ You can also specify the `provider` (`groq` or `openai`) and the exact `model` you want.

---

## 📘 Output Format

The returned optimized prompt follows a structured format:

```text
Role:
[Define the LLM's persona]

Task:
[Clearly state the specific objective]

Instructions:
* Step-by-step subtasks

Context:
[Any relevant background, constraints, domain]

Output Format:
[e.g., bullet list, JSON, summary]

User Input:
[Original user input or example]
```

---

## 🧪 Quick Test (Optional)

```bash
python3 test_import.py
```

This will check:

* ✅ Import works
* ✅ API keys are detected
* ✅ LLM returns optimized result

---

## 🧯 Common Errors & Fixes

| Error                    | Solution                                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| `Missing GROQ_API_KEY`   | Ensure it's in `.env` and loaded with `load_dotenv()`, or passed via `set_groq_api_key()`                                 |
| `Missing OPENAI_API_KEY` | Same as above, but with `set_openai_api_key()`                                                                            |
| `Invalid model` or 403   | The model may be deprecated or restricted. Try another model or check [Groq Models](https://console.groq.com/docs/models) |
| `ModuleNotFoundError`    | Ensure `leo-prompt-optimizer` is installed in the right Python environment                                                |

---

## 💡 Why Use It?

Prompt quality is critical when building with LLMs.

**leo-prompt-optimizer** helps you:

✅ Make prompts explicit and structured
🚫 Reduce hallucinations
🔁 Increase consistency and reuse
🧱 Standardize prompt formats across your stack

---