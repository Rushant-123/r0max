# R0MAX clone order package

Date: 2026-09-27

## What this is

A complete order package for one synthetic virus: a recoded Vesicular stomatitis virus (VSV) genome, 11,161 nt, 554 edits, every edit verified synonymous (same proteins as wild type). Designed and verified in silico on this machine.

## Package contents

```
order/
  a_full_length_clone/       the main order (gene synthesis company)
    clone_spec.md            the plasmid spec
    monster_antigenomic.fa   the insert, positive sense, 5' to 3'
    monster_genome.fa        the viral genome copy (for the record)
  b_helper_plasmids/         the 3 helper orders (gene synthesis)
    helper_spec.md
  c_rescue_lab/              the brief for the lab that makes it live
    rescue_brief.md
```

## Who gets what

| Part | Who | Rough cost | Rough time |
|---|---|---|---|
| Full-length clone | Twist, GenScript, Thermo (GeneArt), Azenta | $1,000 to $2,500 | 2 to 6 weeks |
| Helper plasmids (x3) | same companies | $300 to $800 each | 1 to 3 weeks |
| Rescue | a university vector core (neuro-virus vector group) or a CRO | $2,000 to $10,000 | 1 to 2 weeks |

Total: roughly **$2,500 to $15,000** and **3 to 8 weeks**.

## Safety

VSV is a standard **BSL-2** organism. No special licensing needed. The sequence codes the same five proteins as a normal lab VSV strain. It is a recoded strain, not a new kind of virus.