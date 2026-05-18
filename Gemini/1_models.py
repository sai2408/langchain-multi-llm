# ============================================
# FILE 1: Models — LLM Connect Cheyyadam
# ============================================
# Run: python 1_models.py

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# .env file nundi API key load cheyyi
load_dotenv()

print("=" * 50)
print("   LangChain + Gemini - Models Example")
print("=" * 50)

# ----------------------------
# Step 1: Model Initialize
# ----------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,       # Creativity (0.0 = focused, 1.0 = creative)
    max_output_tokens=512
)

print("\n✅ Model initialized successfully!\n")

# ----------------------------
# Step 2: Simple Invoke
# ----------------------------
print("📌 Test 1: Simple Question")
print("-" * 30)
response = llm.invoke("Hyderabad gurinchi 2 lines cheppu.")
print("Response:", response.content)

# ----------------------------
# Step 3: Temperature difference chudandi
# ----------------------------
print("\n📌 Test 2: Temperature = 0.0 (Focused)")
print("-" * 30)
llm_focused = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.0
)
r1 = llm_focused.invoke("Python best use case enti? One line lo cheppu.")
print("Focused:", r1.content)

print("\n📌 Test 3: Temperature = 1.0 (Creative)")
print("-" * 30)
llm_creative = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=1.0
)
r2 = llm_creative.invoke("Python best use case enti? One line lo cheppu.")
print("Creative:", r2.content)

print("\n✅ Models example complete!")
print("=" * 50)