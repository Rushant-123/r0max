# Rescue brief (the lab that makes it live)

## What we have

- One full-length clone plasmid on order: the complete recoded VSV genome (11,161 nt), positive-sense, between a T7 promoter, a hammerhead ribozyme at the 5' end and an HDV ribozyme at the 3' end, in a low-copy E. coli vector.
- Three helper plasmids on order: wild type VSV N, P, L (G optional), each under its own T7 promoter.
- Full sequence records: genome sense and positive-sense, plus the code that generated and verified all of it.

## What we need from you

A reverse genetics rescue, standard method for this virus family:

1. Co-transfect the four plasmids (full-length clone + N + P + L helpers) into a T7-expressing cell line, BSR-T7 or similar.
2. Incubate 2 to 6 days.
3. Harvest the rescued virus from the supernatant.
4. Confirm: genome is 11,161 nt, and all five proteins match wild type VSV. That is the acceptance test.

## Organism and safety

Recoded strain of a standard lab VSV (Indiana strain). BSL-2. Same five proteins as the parent strain. Not a new kind of organism.

## What we send you

- `monster_antigenomic.fa` (positive-sense insert) and `monster_genome.fa` (record copy)
- `wt_N.fa`, `wt_P.fa`, `wt_L.fa` (helper inserts), plus `wt_G.fa` if your protocol uses G
- The verification code (Python, no dependencies) that proves every edit is synonymous and all five proteins are identical to wild type.

## Timing and cost

You quote it. Our estimate: 1 to 2 weeks of work, $2,000 to $10,000 depending on the core or CRO.