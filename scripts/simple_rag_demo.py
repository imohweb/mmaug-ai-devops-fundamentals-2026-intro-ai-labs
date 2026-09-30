"""Lab 04: a deliberately small RAG workflow with local retrieval and a grounded answer."""

from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA = Path(__file__).resolve().parents[1] / "datasets" / "mini_knowledge_base.csv"


def retrieve(question: str, docs: pd.DataFrame) -> pd.Series:
    vectorizer = TfidfVectorizer(stop_words="english")
    doc_vectors = vectorizer.fit_transform(docs["text"])
    q_vector = vectorizer.transform([question])
    scores = cosine_similarity(q_vector, doc_vectors).flatten()
    return docs.iloc[int(scores.argmax())]


def grounded_answer(question: str, source: pd.Series) -> str:
    # A real RAG app might give the source text and question to an LLM.
    # Here we keep generation deterministic so the retrieval/grounding idea stays visible.
    return (
        f"Based on {source['doc_id']}, abnormal equipment readings should be routed to a "
        "qualified technician with the observation and relevant guidance. The assistant must "
        "not authorise operation or maintenance work."
    )


def main() -> None:
    print("=== LAB 04: SIMPLE RAG ===")
    docs = pd.read_csv(DATA)
    question = "Can the assistant authorise operation when equipment readings are abnormal?"
    source = retrieve(question, docs)

    print("\nQuestion:", question)
    print("\nRetrieved source:", source["doc_id"], "-", source["title"])
    print("Retrieved text:", source["text"])
    print("\nGrounded classroom answer:")
    print(grounded_answer(question, source))

    print("\nRAG FLOW:")
    print("question -> retrieve relevant context -> generate/use answer from that context -> cite/trace source")


if __name__ == "__main__":
    main()
