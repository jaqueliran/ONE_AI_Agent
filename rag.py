from google import genai

from embedding import create_embedding
from vector_store import collection


client = genai.Client()


def retrieve_context(query, n_results=3):
    query_embedding = create_embedding(query)

    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    contexts = []
    sources = []

    for i, document in enumerate(result["documents"][0]):
        source = result["metadatas"][0][i]["source"]

        contexts.append(
            f"Source: {source}\n"
            f"Content: {document}"
        )

        if source not in sources:
            sources.append(source)

    return "\n\n".join(contexts), sources


def generate_response(query):
    context, sources = retrieve_context(query)

    prompt = f"""
You are an assistant for Common Ground, an English school.

Answer the user's question using only the information
provided in the context below.

Rules:
- Use only information contained in the context.
- Do not invent or assume information.
- If the context does not contain enough information
  to answer the question, say that the information
  is not available in the provided documents.
- Answer clearly and concisely.

Context:
{context}

Question:
{query}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text, sources


if __name__ == "__main__":
    question = "What is the minimum attendance requirement?"

    response, sources = generate_response(question)

    print("\nResposta:")
    print(response)

    print("\nFontes:")
    for source in sources:
        print(f"- {source}")