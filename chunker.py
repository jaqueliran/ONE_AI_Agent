def create_chunks(documents):
    chunks = []

    for document in documents:

        if document["type"] == "markdown":
            sections = document["content"].split("\n\n")

            current_chunk = ""

            for section in sections:
                section = section.strip()

                if not section:
                    continue

                if section.startswith("#"):
                    if current_chunk:
                        chunks.append({
                            "content": current_chunk,
                            "source": document["source"],
                            "type": document["type"]
                        })

                    current_chunk = section

                else:
                    if current_chunk:
                        current_chunk += "\n\n" + section
                    else:
                        current_chunk = section

            if current_chunk:
                chunks.append({
                    "content": current_chunk,
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