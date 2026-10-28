# Beauty Product NLP Classification | L’Oréal AI Hackathon 2025

**Multi-label text classification · Natural language processing · Machine learning · Sustainable AI**

**Event:** L’Oréal AI Hackathon × KEDGE Business School (2025)  
**Achievement:** 🥈 2nd place (team)  
**Project type:** Collaborative academic hackathon project

## Overview

This project explores how natural language processing (NLP) can transform unstructured beauty-product descriptions into multiple structured attribute labels. The original event dataset contained **6,240 product descriptions** with categories covering skin concerns, skin types, demographics, and product functions. The supplied hackathon notebooks explore TF-IDF features, multi-label classification, algorithm comparison, and emissions tracking during model development.

### Business problem

Product catalogs contain inconsistent, lengthy descriptions. Turning these descriptions into structured tags can support **product discoverability, catalog enrichment, customer search, and analytics**. Unlike single-class classification, one product can have many applicable labels.

## Methods and tools

- **Python:** pandas, NumPy, scikit-learn, NLTK, Matplotlib, Seaborn
- **Text processing:** normalization, stopword removal, lemmatization, TF-IDF
- **Machine learning:** multi-output classification using logistic regression, random forests, and linear SVM approaches
- **Evaluation:** multi-label classification metrics including F1 score and Hamming loss
- **LLM-assisted labeling exploration:** zero-shot classification experiments using a Transformers pipeline
- **Sustainability considerations:** CodeCarbon experiments for ML emissions tracking

## My contribution and team acknowledgement

This was a **team project**. My contributions included helping with the **prompt/labeling approach for product descriptions** and supporting the team's rapid data preparation and analysis. The notebooks represent the broader team effort, not exclusively my individual work.

## Repository structure

```text
beauty-product-nlp-classification/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── README.md
│   └── demo_product_descriptions.csv   # 64 synthetic examples
├── notebooks/
│   ├── hackathon_final_analysis.ipynb  # original approach, outputs removed
│   ├── hackathon_experiments.ipynb     # early experiments, outputs removed
│   └── public_demo.ipynb               # synthetic-data demonstration
├── src/
│   └── demo_pipeline.py
└── docs/
    └── REPRODUCIBILITY_AND_DATA.md
```

## Quick start (public synthetic demo)

```bash
python -m pip install -r requirements.txt
python src/demo_pipeline.py
```

The public demo contains a deliberately small, synthetic dataset. **Its evaluation scores must not be interpreted as competition results or production performance.** The archived notebooks require the original authorized event dataset and may require additional environment adjustments.

## Data availability and use

The original hackathon datasets and processed competition outputs are **not redistributed in this repository**, because permission to redistribute them has not been established. The demo data was independently created for this portfolio and does not reproduce event-specific product descriptions. Original code outputs and local machine paths were removed before preparing the public notebooks. See [data notes](data/README.md) for expected schema and reuse conditions.

## Project status

This is an archived academic hackathon project accompanied by a separately created, runnable portfolio demonstration. Results reported here describe the project scope and methods; no verified original benchmark scores are claimed.

---

*Project description is for portfolio purposes. L’Oréal and KEDGE are named to identify the event; this repository does not imply affiliation or endorsement.*
