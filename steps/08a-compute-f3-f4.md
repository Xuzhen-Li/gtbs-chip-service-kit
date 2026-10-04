# Step 08a — Compute f3/f4 contrasts

## Input

- Query genotype or dosage at panel sites.
- Grp means from panel metadata (`2449.info`).
- Panel dosage cache.
- Complete-case f3 and f4 of the query versus Grp reference means. Exploratory.

## Do

```bash
grapeancestry analyze --sample Ages
grapeancestry run --sample Ages
src/grapeancestry/adna/fstats.py
src/grapeancestry/popgen/fstats_report.py
```

## Get

- Per-contrast f and Z: exploratory f3 and f4.
- `n_sites` and `n_blocks`: complete-case and jackknife block counts.
- Tables and cards are in 08b.
- No dedicated `grapeancestry` f3 or f4 CLI. The statistics run on the report path.
- Do not invent `grapeancestry fstats`.
- Not formal qp3Pop, qpDstat, qpAdm, or qpGraph.
- Each contrast is complete-case. Missing query sites are excluded.
