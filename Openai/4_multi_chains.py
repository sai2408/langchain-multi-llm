# ============================================
# FILE 4: Multi-Step Chain — Pipeline Build!
# ============================================
# Run: python 4_multi_chain.py

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

print("=" * 50)
print("   LangChain + OpenAI - Multi-Step Chain Example")
print("=" * 50)

llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
parser = StrOutputParser()

# ----------------------------
# Pipeline: Topic → Explain → Quiz → Hint
# 3 steps auto ga run avutayi!
# ----------------------------

# Step 1: Explain cheyyi
explain_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a teacher. Explain clearly in Tenglish in 3-4 lines."),
    ("user", "{topic} explain cheyyi.")
])

# Step 2: Quiz question generate cheyyi
quiz_prompt = ChatPromptTemplate.from_messages([
    ("system", "Based on this explanation, create exactly 1 multiple choice quiz question with 4 options (A,B,C,D). Mark correct answer at end."),
    ("user", "Explanation:\n{explanation}")
])

# Step 3: Hint generate cheyyi
hint_prompt = ChatPromptTemplate.from_messages([
    ("system", "Give a small hint for this question without revealing the answer."),
    ("user", "Question:\n{quiz}")
])

# Individual chains
explain_chain = explain_prompt | llm | parser
quiz_chain    = quiz_prompt    | llm | parser
hint_chain    = hint_prompt    | llm | parser

# ----------------------------
# Full Pipeline Run
# ----------------------------
print("\n📌 Full Pipeline: Topic → Explain → Quiz → Hint")
print("-" * 30)

topic = "Python Lambda functions"
print(f"Topic: {topic}\n")

# Step 1
print("🔵 Step 1: Explanation generating...")
explanation = explain_chain.invoke({"topic": topic})
print("Explanation:\n", explanation)

# Step 2
print("\n🟡 Step 2: Quiz generating...")
quiz = quiz_chain.invoke({"explanation": explanation})
print("Quiz:\n", quiz)

# Step 3
print("\n🟢 Step 3: Hint generating...")
hint = hint_chain.invoke({"quiz": quiz})
print("Hint:\n", hint)

# ----------------------------
# Try with different topic!
# ----------------------------
print("\n" + "=" * 50)
print("📌 Same Pipeline — Different Topic!")
print("-" * 30)

topic2 = "Python Dictionary"
print(f"Topic: {topic2}\n")

explanation2 = explain_chain.invoke({"topic": topic2})
print("Explanation:\n", explanation2)

quiz2 = quiz_chain.invoke({"explanation": explanation2})
print("\nQuiz:\n", quiz2)

print("\n✅ Multi-Step Chain example complete!")
print("=" * 50)