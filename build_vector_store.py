import chromadb

from document_loader import load_documents
from chunker import create_chunks
from embedding import create_embeddings


client = chromadb.PersistentClient(path="./chroma_db")


def build_collection(chunks):
    try:
        client.delete_collection("common_ground_gemini")
    except Exception:
        pass

    collection = client.create_collection(
        name="common_ground_gemini"
    )

    texts = [chunk["content"] for chunk in chunks]

    embeddings = create_embeddings(texts)

    ids = [f"chunk_{i:04d}" for i in range(len(chunks))]

    metadatas = [
        {
            "source": chunk["source"],
            "type": chunk["type"]
        }
        for chunk in chunks
    ]

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=texts,
        metadatas=metadatas
    )

    return collection


if __name__ == "__main__":
    documents = load_documents()
    chunks = create_chunks(documents)

    print(f"Documentos carregados: {len(documents)}")
    print(f"Chunks disponíveis: {len(chunks)}")

    collection = build_collection(chunks)

    print(f"Chunks inseridos no Chroma: {len(chunks)}")
    print(f"Total na coleção: {collection.count()}")