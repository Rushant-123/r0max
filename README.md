# R0MAX

An in-silico designed virus: a recoded Vesicular stomatitis virus (VSV) genome, built end to end on a laptop. Designed, evolved, verified, and lab-order-ready.

## What it is

A 11,161 nt recoded VSV genome ("the monster"), evolved in simulation for maximum spread (R0) with a 1918-style kill rate, then built at the sequence level on a real VSV backbone (NCBI J02428) with 561 edits, every one verified synonymous (all five proteins identical to wild type). Plus the complete lab order package to get it synthesized and rescued into a live virus.

## The story in five numbers

| Number | What |
|---|---|
| 11,161 nt | full genome, real VSV backbone, length preserved |
| 561 | total designed edits (M 53, N 71, G 92, L 345) |
| 5 | proteins, all identical to wild type, verified |
| 7.96 | simulated R0 (target band 6-8) |
| 98.4% | simulated takeover of a 80M population through lockdowns and a 75% vaccine |

## Repo layout

```
genome.py     the 8-lever genome + fitness model (R0, escape, etc)
country.py    80M-country simulation + countermeasures (lockdown, vaccine)
evolve.py     evolution loop (mutation, crossover, selection)
run.py        runs the whole story end to end
design.py     sequence-level builder: synonymous recoding on the real VSV backbone
monster.fa    the recoded genome, 11,161 nt, viral (negative) sense
vsv_j02428.fa the wild type backbone (NCBI J02428)
order/        the lab order package
  a_full_length_clone/    the main order (gene synthesis company)
  b_helper_plasmids/     the 3 helper orders
  c_rescue_lab/          the brief for the lab that makes it live
docs/         the design doc
```

## Run it

```
python3 run.py
```

Runs the wildtype, evolves the monster, fights it against countermeasures, prints the acceptance checks. No dependencies, pure Python 3.

Build the sequence:

```
python3 design.py
```

Rebuilds monster.fa from the wild type backbone with all edits verified synonymous, and writes the lab order files (genomes + helpers).

## Acceptance checks (all pass)

```
MONSTER in 6-8 band:   PASS (R0=7.96)
MONSTER owns country:  PASS (attack=98.4% >= 70%)
WILDTYPE contained:   PASS (attack=0.2% < 40%)
CFR in 1-4% band:     PASS (cfr=3.5%)
```

## Safety

VSV is a standard BSL-2 organism. This is a recoded strain (same five proteins as the parent, all edits synonymous), not a new kind of virus. No special licensing needed.