# Helper plasmid orders (3 orders)

Product: three small synthetic genes in plasmids, one gene per plasmid.
Vendors: same as the full-length clone (Twist, GenScript, Thermo/GeneArt, Azenta).
Cost estimate: $300 to $800 each. Time: 1 to 3 weeks.

## What to order

Three plasmids, one wild type VSV gene each, each under its own T7 promoter:

| Plasmid | Insert | Length | File |
|---|---|---|---|
| Helper N | wild type VSV N gene, positive-sense, 5' to 3' | 1,332 nt | `wt_N.fa` |
| Helper P | wild type VSV P gene, positive-sense, 5' to 3' | 831 nt | `wt_P.fa` |
| Helper L | wild type VSV L gene, positive-sense, 5' to 3' | 6,381 nt | `wt_L.fa` |

A fourth optional helper (G, 1,675 nt, `wt_G.fa`) is included in this folder. Some rescue protocols use it, some do not. Order it only if the rescue lab asks for it.

## Plasmid requirements

- Standard E. coli cloning vector, vendor default.
- One T7 promoter per plasmid, directly in front of the gene.
- No ribozymes needed on the helpers.
- Full insert sequencing on each.
- No mutations tolerated. Synthesize exactly as provided.

## Why wild type genes

Every edit in the recoded monster genome is synonymous (verified: all five monster proteins are identical to wild type). So wild type helper genes produce the same N, P, L proteins the monster genome expects. Wild type helpers are the standard, safest choice.