# Architecture

## Platform vs profile

| | **Platform** (`platform/`) | **Profile** (`profiles/…`) |
|--|--|--|
| Owns | Config schema, run orchestration hooks, sample-first report/JSON builders, viz shells, cloud card skeleton | Site list / BED pointer, panel metadata schema, frozen PCA/ADMIXTURE *pointers*, claim boundaries, species-specific labels |
| Must not hardcode | Species paths, VS-1, 167K counts | Generic HTML chrome (reuse platform report) |

## Data you bring (local)

- Reference genome + fai for your panel’s coordinate system  
- Panel VCF or dosage cache for your reference set  
- Frozen projection artifacts (PCA axes, ADMIXTURE P) if you use those modules  
- Query FASTQ / BAM / query VCF at panel sites  

None of the large binaries belong in this public clone.

## Sibling repo

- **grapeancestry** = grapevine 167K *public face* (GUIDELINE, Ages HTML).  
- **gtbs-chip-service-kit** = *how to stand up* a companion service for any GBTS panel.
