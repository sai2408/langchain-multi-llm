# ============================================
# FILE 2: Prompt Templates — Reusable Prompts
# ============================================
# Run: python 2_prompt_templates.py

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

print("=" * 50)
print("   LangChain + OpenAI - Prompt Templates Example")
print("=" * 50)

llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

# ----------------------------
# Step 1: Basic Template
# ----------------------------
print("\n📌 Test 1: Basic Prompt Template")
print("-" * 30)

basic_prompt = ChatPromptTemplate.from_messages([
    ("system", "Meeru oka expert {subject} teacher. Tenglish lo explain cheyyi."),
    ("user", "{topic} gurinchi simple ga explain cheyyi.")
])

# Python teacher ga
python_msgs = basic_prompt.format_messages(
    subject="Python",
    topic="List comprehension"
)
response = llm.invoke(python_msgs)
print("Python Teacher Response:")
print(response.content)

# ----------------------------
# Step 2: Same Template — Different Subject!
# ----------------------------
print("\n📌 Test 2: Same Template — GenAI Teacher!")
print("-" * 30)

genai_msgs = basic_prompt.format_messages(
    subject="GenAI",
    topic="Embeddings"
)
response2 = llm.invoke(genai_msgs)
print("GenAI Teacher Response:")
print(response2.content)

# ----------------------------
# Step 3: Multi Variable Template
# ----------------------------
print("\n📌 Test 3: Multi Variable Template")
print("-" * 30)

review_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a {language} code reviewer. Be concise."),
    ("user", "Review this code and find issues:\n\n{code}")
])

buggy_code = """
def divide(a, b):
    return a / b

result = divide(10, 0)
print(result)
"""

review_msgs = review_prompt.format_messages(
    language="Python",
    code=buggy_code
)
response3 = llm.invoke(review_msgs)
print("Code Review:")
print(response3.content)

print("\n✅ Prompt Templates example complete!")
print("=" * 50)