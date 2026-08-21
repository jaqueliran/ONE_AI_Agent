from google import genai


client = genai.Client()


def create_embedding(text):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return result.embeddings[0].values


def create_embeddings(texts):
    import time

    batch_size = 100
    embeddings = []

    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]

        print(
            f"Criando embeddings: "
            f"{i + 1}-{i + len(batch)} de {len(texts)}"
        )

        while True:
            try:
                result = client.models.embed_content(
                    model="gemini-embedding-001",
                    contents=batch
                )

                break

            except Exception as error:
                if getattr(error, "code", None) == 429:
                    print("Limite da API atingido. Aguardando 60 segundos...")
                    time.sleep(60)
                else:
                    raise

        embeddings.extend(
            embedding.values
            for embedding in result.embeddings
        )

    return embeddings


if __name__ == "__main__":
    text = "What is the minimum attendance requirement?"

    embedding = create_embedding(text)

    print(f"Embedding criado com {len(embedding)} dimensões.")
    print(embedding[:5])