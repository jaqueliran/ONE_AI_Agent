from pathlib import Path
import csv


def load_documents():
    documents_path = Path("documents")
    documents = []

    for file in documents_path.iterdir():

        if file.suffix == ".md":
            content = file.read_text(encoding="utf-8")

            documents.append({
                "content": content,
                "source": file.name,
                "type": "markdown"
            })

        elif file.suffix == ".csv":
            with open(file, "r", encoding="utf-8") as csv_file:
                reader = csv.reader(csv_file)

                rows = list(reader)

                content = "\n".join(
                    ",".join(row)
                    for row in rows
                )

                documents.append({
                    "content": content,
                    "source": file.name,
                    "type": "csv"
                })

    return documents


if __name__ == "__main__":
    documents = load_documents()

    print(f"Documentos carregados: {len(documents)}")

    primeiro_documento = documents[0]

    print("\nPrimeiro documento:")
    print(primeiro_documento)
    