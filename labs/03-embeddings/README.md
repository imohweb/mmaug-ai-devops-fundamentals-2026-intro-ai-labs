# Lab 03 — Embeddings and Vector Similarity

## Purpose

Build intuition for representing text numerically and retrieving items that are similar to a question.

## Run

```bash
python scripts/embeddings_tfidf_demo.py
```

## What the demonstration does

The script uses TF-IDF to convert short fictional documents and a query into vectors. Cosine similarity ranks the documents by direction in that vector space.

Modern learned embeddings usually capture meaning better than TF-IDF. TF-IDF is used here because it is transparent, local and easy to inspect.

## Vocabulary

- **Vector:** ordered list of numbers.
- **Embedding:** learned numeric representation of text, images or another data type.
- **Similarity:** numeric measure of closeness.
- **Vector search:** retrieval based on vector similarity.

## Experiment

Change the question to ask about account access, governance or equipment inspection. Observe which document is ranked first and whether the answer is actually supported.

## Control question

What should the application do when every similarity score is weak? A dependable system should avoid pretending that an unrelated document answers the question.

