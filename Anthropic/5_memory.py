# ============================================
# FILE 5: Memory — Conversation Remember!
# ============================================
# Run: python 5_memory.py

from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

print("=" * 50)
print("   LangChain - Memory Example")
print("=" * 50)

llm = ChatAnthropic(model="claude-sonnet-4-20250514", temperature=0.7)
parser = StrOutputParser()

# ----------------------------
# Manual Memory — History list maintain cheyyadam
# (Most reliable and clear approach!)
# ----------------------------

# Prompt with chat history placeholder
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Respond in Tenglish. Remember the conversation context."),
    MessagesPlaceholder(variable_name="chat_history"),  # History ikkade inject avutundi
    ("human", "{user_input}")
])

chain = prompt | llm | parser

# History store cheyyi
chat_history = []

def chat_with_memory(user_input):
    """User input teesukoni, history maintain chesi response isthundi"""
    print(f"\n👤 User: {user_input}")
    
    response = chain.invoke({
        "chat_history": chat_history,
        "user_input": user_input
    })
    
    # History update cheyyi
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=response))
    
    print(f"🤖 Bot: {response}")
    return response

# ----------------------------
# Test 1: Basic Memory
# ----------------------------
print("\n📌 Test 1: Context Remember Chestundaa?")
print("-" * 30)

chat_with_memory("Naa peru Ravi, naaku Python telsu")
chat_with_memory("Naa peru enti?")           # Remember chestundaa?
chat_with_memory("Naaku emi teluso cheppanu kadaa?")  # Context remember!

# ----------------------------
# Test 2: Long Conversation
# ----------------------------
print("\n📌 Test 2: Multi-turn Conversation")
print("-" * 30)

# Reset history for fresh conversation
chat_history.clear()
print("(Fresh conversation start...)\n")

chat_with_memory("Naaku GenAI nervadam undi")
chat_with_memory("Nenu beginner ni")
chat_with_memory("Nenu emi nerchukovanlo start cheyyali?")  # Context batti answer isthundi!
chat_with_memory("Oka week lo emi cover cheyyochu?")        # Previous context remember!

# ----------------------------
# Show History
# ----------------------------
print("\n📌 Chat History Summary:")
print("-" * 30)
print(f"Total messages in history: {len(chat_history)}")
for i, msg in enumerate(chat_history):
    role = "User" if isinstance(msg, HumanMessage) else "Bot"
    print(f"{i+1}. [{role}]: {msg.content[:60]}...")

print("\n✅ Memory example complete!")
print("=" * 50)