import chromadb

from embedding import create_embedding


client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="common_ground_gemini"
)


if __name__ == "__main__":
    document = "Students must maintain a minimum attendance of 75%."

    document_embedding = create_embedding(document)

    collection.add(
        ids=["test_gemini_001"],
        embeddings=[document_embedding],
        documents=[document],
        metadatas=[{
            "source": "attendance and make-up policy.md"
        }]
    )

    query = "What is the minimum attendance requirement?"

    query_embedding = create_embedding(query)

    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )

    print("\nResultado da busca:")
    print(result)