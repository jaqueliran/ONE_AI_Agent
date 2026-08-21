from google import genai


client = genai.Client()


def create_embedding(text):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return result.embeddings[0].values


if __name__ == "__main__":
    text = "What is the minimum attendance requirement?"

    embedding = create_embedding(text)

    print(f"Embedding criado com {len(embedding)} dimensões.")
    print(embedding[:5])