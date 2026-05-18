# ============================================
# FILE 3: Chains — Steps Connect Cheyyadam
# ============================================
# Run: python 3_chains.py

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

print("=" * 50)
print("   LangChain + Gemini - Chains Example")
print("=" * 50)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)
parser = StrOutputParser()  # Response ni plain text ga convert chestundi

# ----------------------------
# Step 1: Simple Chain (Prompt | LLM)
# ----------------------------
print("\n📌 Test 1: Simple Chain — Prompt | LLM")
print("-" * 30)

simple_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer in Tenglish."),
    ("user", "{question}")
])

# | operator tho chain!
simple_chain = simple_prompt | llm | parser

response = simple_chain.invoke({"question": "Python decorators ante enti?"})
print("Response:", response)

# ----------------------------
# Step 2: Chain with Parser
# ----------------------------
print("\n📌 Test 2: Chain with Output Parser")
print("-" * 30)

joke_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a funny assistant. Tell short jokes."),
    ("user", "{topic} gurinchi oka funny joke cheppu.")
])

joke_chain = joke_prompt | llm | parser

joke = joke_chain.invoke({"topic": "Python programmers"})
print("Joke:", joke)

# ----------------------------
# Step 3: Multiple Chains — Different Purposes
# ----------------------------
print("\n📌 Test 3: Multiple Chains")
print("-" * 30)

# Chain 1: Translate
translate_prompt = ChatPromptTemplate.from_messages([
    ("system", "Translate the given text to Telugu. Only give translation, nothing else."),
    ("user", "{text}")
])
translate_chain = translate_prompt | llm | parser

# Chain 2: Summarize
summarize_prompt = ChatPromptTemplate.from_messages([
    ("system", "Summarize in exactly 1 sentence."),
    ("user", "{text}")
])
summarize_chain = summarize_prompt | llm | parser

# Run both on same input
text = "LangChain is a framework that helps developers build applications powered by large language models. It provides tools for chaining together different components like prompts, models, and output parsers."

print("Original:", text)
print("\nTranslation:", translate_chain.invoke({"text": text}))
print("\nSummary:", summarize_chain.invoke({"text": text}))

print("\n✅ Chains example complete!")
print("=" * 50)