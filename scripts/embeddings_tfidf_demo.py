"""Lab 03: vector similarity with TF-IDF as a transparent stand-in for embeddings."""

from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA = Path(__file__).resolve().parents[1] / "datasets" / "mini_knowledge_base.csv"


def main() -> None:
    print("=== LAB 03: EMBEDDINGS AND VECTOR SIMILARITY ===")
    docs = pd.read_csv(DATA)
    query = "What should we do when equipment readings are abnormal?"

    vectorizer = TfidfVectorizer(stop_words="english")
    document_vectors = vectorizer.fit_transform(docs["text"])
    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, document_vectors).flatten()

    result = docs.copy()
    result["similarity"] = scores

    print("\nQuery:", query)
    print("\nTop matches:")
    print(
        result.sort_values("similarity", ascending=False)[
            ["doc_id", "title", "similarity", "text"]
        ].head(3).to_string(index=False)
    )

    print("\nTEACHING NOTE:")
    print("TF-IDF is used so learners can run everything locally and see the idea clearly.")
    print("Modern semantic embeddings use learned vector representations, but retrieval still compares vectors for similarity.")


if __name__ == "__main__":
    main()
