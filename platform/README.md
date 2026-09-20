# Platform (generic)

Modules (stubs this round; thin code next):

| Dir | Intent |
|-----|--------|
| `pipeline/` | Config-driven run orchestration; VCF@panel-sites validation hooks |
| `report/` | Sample-first HTML/JSON builders |
| `viz/` | Table→plot helpers (PCA / ADMIXTURE / NJ shells) |
| `cloud/` | Upload panel-sites VCF → `chip.json` skeleton (Python-only; no bwa required) |

No grapevine hardcoding here.
