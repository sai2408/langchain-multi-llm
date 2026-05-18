# ============================================
# FILE 6: Real Project — Document Q&A Bot!
# ============================================
# Run: python 6_real_project.py

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

print("=" * 50)
print("   Real Project — Document Q&A Bot 📄🤖")
print("=" * 50)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.0)  # 0.0 = accurate answers
parser = StrOutputParser()

# ----------------------------
# Document — Meeru own content pettocchu!
# ----------------------------
document = """
Hyderabad Information:
- Hyderabad is the capital of Telangana state in India.
- It is famous for Biryani, Charminar, and IT industry.
- The city is called 'City of Pearls' due to its pearl trade history.
- Hyderabad has major IT companies like Microsoft, Google, Amazon, TCS, Infosys.
- The population is approximately 1 crore people.
- The city was founded by Muhammad Quli Qutb Shah in 1591.
- Hussain Sagar Lake is a famous landmark in the city.
- The Golconda Fort is a historical monument near Hyderabad.
- HITECH City is the main IT hub of Hyderabad.
- Hyderabad Metro Rail connects major parts of the city.
"""

# ----------------------------
# Q&A Prompt
# ----------------------------
qa_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful document assistant.

RULES:
- Answer ONLY based on the given document
- If answer is not in document, say exactly: "Document lo aa information ledu!"
- Keep answers short and clear
- Answer in Tenglish"""),

    ("user", """Document:
{document}

Question: {question}

Answer:""")
])

qa_chain = qa_prompt | llm | parser

# ----------------------------
# Test Questions
# ----------------------------
questions = [
    "Hyderabad lo famous food enti?",
    "Hyderabad population entha?",
    "Hyderabad lo IT companies evi unnaayi?",
    "Hyderabad ni eppudu found chesaru?",
    "Hyderabad lo famous lake edi?",
    "Hyderabad lo snow vastundaa?",            # Document lo ledu!
    "HITECH City ante enti?",
    "Hyderabad metro undi aa?",
]

print("\n📄 Document loaded successfully!")
print(f"📝 Total questions: {len(questions)}\n")
print("-" * 50)

for i, question in enumerate(questions, 1):
    print(f"\nQ{i}: {question}")
    answer = qa_chain.invoke({
        "document": document,
        "question": question
    })
    print(f"A{i}: {answer}")
    print("-" * 30)

# ----------------------------
# Interactive Mode — Mee questions adugundi!
# ----------------------------
print("\n" + "=" * 50)
print("🎯 Interactive Mode — Meeru Question Adugandi!")
print("('quit' type cheyyi to exit)")
print("=" * 50)

while True:
    user_question = input("\n❓ Meeru Question: ").strip()

    if user_question.lower() in ['quit', 'exit', 'q']:
        print("\n👋 Bye bro! Great practice!")
        break

    if not user_question:
        print("Question adugandi bro!")
        continue

    answer = qa_chain.invoke({
        "document": document,
        "question": user_question
    })
    print(f"🤖 Answer: {answer}")