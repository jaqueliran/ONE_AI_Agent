import chromadb

from embedding import create_embedding


client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="common_ground_gemini"
)


def search_collection(query, n_results=3):
    query_embedding = create_embedding(query)

    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    print(f"\nPergunta: {query}")
    print("\nResultados:")

    for i in range(len(result["documents"][0])):
        print(f"\n--- Resultado {i + 1} ---")
        print(f"Fonte: {result['metadatas'][0][i]['source']}")
        print(f"Distância: {result['distances'][0][i]}")
        print(f"Conteúdo: {result['documents'][0][i]}")


if __name__ == "__main__":
    print(f"Total de documentos na coleção: {collection.count()}")

    questions = [
        "What is the minimum attendance requirement?",
        "What teacher benefits does Common Ground offer?",
        "How does student placement work?",
        "How many students are there in each class?"
    ]

    for question in questions:
        search_collection(question)
        