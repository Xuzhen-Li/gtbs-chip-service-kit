# 7. Run the suite

The commands that turn chip data into a report are in this repo under [steps/](../../steps/), one file per step, from `00a` through `14b`. [grapeancestry](https://github.com/Xuzhen-Li/grapeancestry) remains the grapevine 167K worked example.

For the grapevine 167K example, follow that index:

1. Prepare the panel before any new sample: `00a` through `00e`. Skip `00f` and `00g` if you only want ancestry.
2. For each sample: `01a` through `13b`. The HTML the profile names is `*.sample-first-v2.report.html`.
3. `14a` and `14b` are optional. They emit `chip.json`. The v1 HTML does not need them.

A public demo of that report is [ramos2019_np.batch.report.html](https://xuzhen-li.github.io/grapeancestry/demo/results/ramos2019_np.batch.report.html).

Another crop reuses the same step ids. Replace the files behind `00a`–`00e` and point this kit's profile at them. Designing the sites themselves is [grapevine-chip](https://github.com/Xuzhen-Li/grapevine-chip), not this repo.

Back to [the step list](../steps.md).
