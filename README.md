# 🦜🔗 LangChain Multi-LLM

> Learn LangChain fundamentals with **3 LLM providers** — same concepts, different models.  
> Anthropic Claude · OpenAI GPT-4o · Google Gemini

---

## 📌 What is This?

This repo covers **LangChain core concepts** from scratch — implemented 3 times with different providers so you can compare how each one works and understand that **LangChain logic stays the same regardless of the model you use**.

Great for:
- 🧑‍🎓 Beginners learning LangChain
- 🔀 Developers evaluating which LLM provider to use
- 📚 Reference code for common LangChain patterns

---

## 📁 Folder Structure

```
langchain-multi-llm/
│
├── anthropic/               # 🟠 Claude (claude-sonnet-4)
│   ├── 1_models.py
│   ├── 2_prompt_templates.py
│   ├── 3_chains.py
│   ├── 4_multi_chain.py
│   ├── 5_memory.py
│   └── 6_real_project.py
│
├── openai/                  # 🟢 GPT-4o
│   ├── 1_models.py
│   ├── 2_prompt_templates.py
│   ├── 3_chains.py
│   ├── 4_multi_chain.py
│   ├── 5_memory.py
│   └── 6_real_project.py
│
├── gemini/                  # 🔵 Gemini 2.0 Flash
│   ├── 1_models.py
│   ├── 2_prompt_templates.py
│   ├── 3_chains.py
│   ├── 4_multi_chain.py
│   ├── 5_memory.py
│   └── 6_real_project.py
│
├── .env.example             # API key template
├── .gitignore
└── README.md
```

---

## 🗺️ Learning Roadmap

Run files **in order** — each one builds on the previous concept.

| # | File | Concept | What You Learn |
|---|------|---------|----------------|
| 1 | `1_models.py` | **Models** | Connect to LLM, invoke, understand temperature |
| 2 | `2_prompt_templates.py` | **Prompt Templates** | Reusable prompts with dynamic variables |
| 3 | `3_chains.py` | **Chains** | Connect steps using the `\|` pipe operator |
| 4 | `4_multi_chain.py` | **Multi-Step Chains** | Build pipelines: Topic → Explain → Quiz → Hint |
| 5 | `5_memory.py` | **Memory** | Maintain conversation history across multiple turns |
| 6 | `6_real_project.py` | **Real Project** | Document Q&A Bot — grounded, accurate answers |

---

## ⚙️ Setup

### Step 1 — Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/langchain-multi-llm.git
cd langchain-multi-llm
```

### Step 2 — Install dependencies

```bash
# Core LangChain
pip install langchain langchain-core python-dotenv

# Provider packages (install only what you need)
pip install langchain-anthropic        # For anthropic/
pip install langchain-openai           # For openai/
pip install langchain-google-genai     # For gemini/
```

### Step 3 — Add API keys

Create a `.env` file in the root folder:

```env
ANTHROPIC_API_KEY=your_anthropic_key_here
OPENAI_API_KEY=your_openai_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

> Get your keys here: [Anthropic](https://console.anthropic.com) · [OpenAI](https://platform.openai.com) · [Google AI Studio](https://aistudio.google.com)

### Step 4 — Run any file

```bash
cd anthropic && python 1_models.py
cd openai   && python 3_chains.py
cd gemini   && python 6_real_project.py
```

---

## 🔄 Provider Comparison

| | 🟠 Anthropic | 🟢 OpenAI | 🔵 Gemini |
|---|---|---|---|
| **Package** | `langchain-anthropic` | `langchain-openai` | `langchain-google-genai` |
| **Class** | `ChatAnthropic` | `ChatOpenAI` | `ChatGoogleGenerativeAI` |
| **Model** | `claude-sonnet-4-20250514` | `gpt-4o` | `gemini-2.0-flash` |
| **Token param** | `max_tokens` | `max_tokens` | `max_output_tokens` |
| **API key env** | `ANTHROPIC_API_KEY` | `OPENAI_API_KEY` | `GOOGLE_API_KEY` |

### The magic of LangChain 🪄

```python
# This chain pattern works IDENTICALLY across all 3 providers
# Just swap the import and model name!

chain = prompt | llm | parser
response = chain.invoke({"question": "Your question here"})
```

---

## 💡 Key Concepts Explained

### 🔗 Chains (File 3)
Connect components using the `|` pipe operator:
```python
chain = prompt_template | llm | output_parser
```

### 🔁 Multi-Step Pipeline (File 4)
Output of one chain feeds into the next:
```
Topic → [Explain Chain] → Explanation → [Quiz Chain] → Quiz → [Hint Chain] → Hint
```

### 🧠 Memory (File 5)
Maintain conversation context manually using message history:
```python
chat_history.append(HumanMessage(content=user_input))
chat_history.append(AIMessage(content=response))
```

### 📄 Document Q&A (File 6)
Grounded answers — model answers ONLY from the provided document, not from its training data.

---

## 🛡️ Important

- **Never commit your `.env` file** — it contains secret API keys
- The `.gitignore` already excludes `.env` for you
- All examples use Tenglish (Telugu + English) — easy to adapt to any language

---

## 🤝 Contributing

Feel free to open issues or PRs to:
- Add more LangChain concepts (RAG, Agents, Tools)
- Add more providers (Mistral, Cohere, Ollama)
- Improve examples or fix bugs

---

## ⭐ If This Helped You

Give the repo a star — it helps others find it too!

---

*Built while learning LangChain — one provider at a time.*
