from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import pipeline

# ----------------------------
# Load embedding model
# ----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ----------------------------
# Load vector database
# ----------------------------
vectorstore = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k":3})

# ----------------------------
# Load better local LLM
# ----------------------------
generator = pipeline(
    "text-generation",
    model="microsoft/phi-2",
    max_new_tokens=120,
    temperature=0.2,
    do_sample=True
)

# ----------------------------
# Ask Question Function
# ----------------------------
def ask_question(query):

    docs = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an AI assistant answering questions from the Swiggy Annual Report.

Context:
{context}

Question: {query}

Answer the question briefly and clearly.
"""

    result = generator(prompt)

    output = result[0]["generated_text"]

    answer = output.replace(prompt, "").strip()

    return answer