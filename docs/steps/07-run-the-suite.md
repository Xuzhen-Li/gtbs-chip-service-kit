# 7. Run the suite

## Input

- The analysis steps in [steps/](../../steps/), one file per step, from `00a` through `14b`.
- [grapeancestry](https://github.com/Xuzhen-Li/grapeancestry), the grapevine 167K worked example.
- Another crop reuses the same step ids. Replace the files behind `00a`–`00e` and point this kit's profile at them.
- Designing the sites themselves is [grapevine-chip](https://github.com/Xuzhen-Li/grapevine-chip), not this repo.

## Do

```bash
# No command was written down for this step.
```

## Get

- The command blocks in those files call scripts and data that are not in this clone, so this repo alone cannot run the report.
- Prepare the panel before any new sample: `00a` through `00e`. Skip `00f` and `00g` if you only want ancestry.
- For each sample: `01a` through `13b`. The HTML the profile names is `*.sample-first-v2.report.html`.
- `14a` and `14b` are optional. They emit `chip.json`. The v1 HTML does not need them.
- A public demo of that report is [ramos2019_np.batch.report.html](https://xuzhen-li.github.io/grapeancestry/demo/results/ramos2019_np.batch.report.html).
