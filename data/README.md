# Data notes

`demo_product_descriptions.csv` contains **64 synthetic sample product descriptions**, created only to make the public demonstration runnable. They are not L’Oréal product data, and any model accuracy obtained from them is *not* comparable to the hackathon evaluation.

The original hackathon analysis loaded an event-supplied product-description dataset (`6,240` descriptions, `37` columns). It is intentionally excluded from this public release pending confirmation of redistribution rights. If you personally have authorization to use it locally, place it at `data/hackathon_dataset.csv`. The `.gitignore` prevents ordinary Git tracking of that file.

Expected original columns: `row_num`, `text_raw` and 35 multi-label categorical columns such as `acne`, `dry`, `oily`, `moisturize`. The example demo deliberately uses a smaller set of labels (`dry`, `oily`, `acne`, `moisturize`).

Public posting by another participant is not, by itself, evidence of permission to redistribute a dataset or share third-party intellectual property. Verify the event terms before adding any original data to a public repository.
