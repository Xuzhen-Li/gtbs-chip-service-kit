# Step 11b — Predict GS scores for query

## Input

- Trained GS artifacts and `results/gs/index.tsv` from 11a.
- Query sample id and optional query VCF.
- `--min-cv-r` threshold for which models emit scores.
- Score the query with trained models. Expose only profile decision-grade traits as rankable.

## Do

```bash
grapeancestry gs-predict --sample Ages --vcf results/Ages.vcf.gz --cache results/cache/panel_dosage_167k.npz --min-cv-r 0.3
grapeancestry analyze
grapeancestry run
src/grapeancestry/breeding/gs.py
```

## Get

- Per-trait scores for this sample: model predictions.
- Decision-grade flag from profile claims, not from every trait that passes cross-validation.
- Colour GS card (example: OIV 225), placed last in classroom order on the HTML.
- Also wired through `grapeancestry analyze` and `run` when GS assets exist. Report and Cloud wiring consume the same scores.
- A GS score is not a phenotype.
- Grapevine example: only OIV 225 is decision-grade and rankable. Do not claim seedlessness from exploratory traits.
- Frozen axes and panel training stay separate from customer phenotype collection.
