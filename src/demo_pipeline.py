"""Runnable multi-label text-classification demo using *synthetic* skincare data.

This is a portfolio demonstration, not a re-run of the private hackathon results.

Usage:
    python src/demo_pipeline.py
    python src/demo_pipeline.py --dataset path/to/authorized.csv
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, hamming_loss
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier

DEFAULT_DATA = Path(__file__).resolve().parents[1] / "data" / "demo_product_descriptions.csv"
LABELS = ("dry", "oily", "acne", "moisturize")


def train_and_evaluate(dataset: Path = DEFAULT_DATA) -> dict:
    df = pd.read_csv(dataset)
    required = {"text_raw", *LABELS}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Required columns missing: {sorted(missing)}")
    df = df.dropna(subset=["text_raw", *LABELS]).copy()
    x_train, x_test, y_train, y_test = train_test_split(
        df["text_raw"].astype(str), df[list(LABELS)].astype(int),
        test_size=0.25, random_state=42
    )
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1)
    train_features = vectorizer.fit_transform(x_train)
    test_features = vectorizer.transform(x_test)
    model = MultiOutputClassifier(LogisticRegression(max_iter=2000))
    model.fit(train_features, y_train)
    predictions = model.predict(test_features)
    metrics = {
        "rows": len(df),
        "labels": list(LABELS),
        "micro_f1": float(f1_score(y_test, predictions, average="micro", zero_division=0)),
        "hamming_loss": float(hamming_loss(y_test, predictions)),
    }
    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATA)
    args = parser.parse_args()
    result = train_and_evaluate(args.dataset)
    print("Synthetic-data demonstration (NOT original hackathon results)")
    for key, value in result.items():
        print(f"{key}: {value}")
