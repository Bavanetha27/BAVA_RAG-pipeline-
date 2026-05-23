import streamlit as st
import ollama
from chromadb import PersistentClient

EMBEDDING_MODEL = "llama3"
LANGUAGE_MODEL = "llama3"

st.title("Cloud computing RAG Chatbot")

# Load dataset
with open("cloud.txt", "r", encoding="utf-8") as f:
    documents = [line.strip() for line in f.readlines() if line.strip()]

# Persistent Chroma
client = PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection("cloud_computing_rag")

# Add only once
if collection.count() == 0:

    st.write("Creating embeddings...")

    for i, doc in enumerate(documents):

        embedding = ollama.embeddings(
            model=EMBEDDING_MODEL,
            prompt=doc
        )["embedding"]

        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[doc]
        )

    st.success("Embeddings stored successfully!")

query = st.text_input("Ask a question")

if query:

    query_embedding = ollama.embeddings(
        model=EMBEDDING_MODEL,
        prompt=query
    )["embedding"]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    retrieved_docs = results["documents"][0]

    context = "\n".join(retrieved_docs)

    prompt = f"""
You are a helpful cloud computing expert chatbot.

Answer the user's question ONLY using the provided context.

Rules:
- Give a direct and short answer.
- If the answer is not clearly available in the context, say:
  "I could not find the answer in the provided context."
- Do not add unrelated information.
- Do not explain extra history unless asked.
- Keep the answer natural and conversational.

Context:
{chr(10).join([f"- {chunk}" for chunk in retrieved_docs])}

Question:
{query}

Answer:
"""

    response = ollama.chat(
        model=LANGUAGE_MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    st.write(response["message"]["content"])