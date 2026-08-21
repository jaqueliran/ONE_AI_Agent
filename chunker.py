from collections import Counter


def create_chunks(documents):
    chunks = []

    for document in documents:

        if document["type"] == "markdown":
            paragraphs = document["content"].split("\n\n")

            for paragraph in paragraphs:
                paragraph = paragraph.strip()

                if paragraph:
                    chunks.append({
                        "content": paragraph,
                        "source": document["source"],
                        "type": document["type"]
                    })

        elif document["type"] == "csv":
            rows = document["content"].split("\n")

            for row in rows:
                row = row.strip()

                if row:
                    chunks.append({
                        "content": row,
                        "source": document["source"],
                        "type": document["type"]
                    })

    return chunks


if __name__ == "__main__":
    from document_loader import load_documents

    documents = load_documents()
    chunks = create_chunks(documents)

    print(f"Documentos carregados: {len(documents)}")
    print(f"Chunks criados: {len(chunks)}")