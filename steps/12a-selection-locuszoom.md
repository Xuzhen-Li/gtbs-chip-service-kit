# Step 12a — Selection LocusZoom (panel Fst windows)

## Input

- `results/selection/locuszoom.json` from `grapeancestry selection` and selscan.
- Query genotype only as overlay counts.
- Interactive regional view of among-Grp Fst and selection windows (panel context).

## Do

```bash
grapeancestry selection --half-bp 50000 --top 40
grapeancestry analyze --sample Ages
src/grapeancestry/report/interactive_dashboard.py
```

## Get

- Window site metrics: among-all-Grps panel regional context.
- Query genotype counts in the window: overlay only.
- LocusZoom scatter, gene track, and genotype legend (Selection door).
- The interactive embed reads the `locuszoom.json` payload.
- Selection LocusZoom is among-all-Grps panel regional context only.
- Sweep rows still point at exact Manhattan points (09a and 09b), not arbitrary LocusZoom windows.
