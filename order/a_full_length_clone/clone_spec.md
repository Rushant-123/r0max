# Full-length clone order (main order)

Product: one synthetic gene in a plasmid. 11,161 nt insert plus flanking elements.
Vendors: Twist, GenScript, Thermo (GeneArt), Azenta. All take this as a standard product.
Cost estimate: $1,000 to $2,500. Time: 2 to 6 weeks.

## Insert layout, 5' to 3'

1. T7 promoter
2. Hammerhead ribozyme
3. The 11,161 nt antigenomic (positive-sense) copy of the R0MAX-monster VSV genome (file: `monster_antigenomic.fa`)
4. Hepatitis delta virus (HDV) ribozyme
5. Vector backbone

## Plasmid requirements

- Low-copy E. coli cloning vector (pBR322 / pSMART type, or vendor default low-copy)
- No extra bases between the promoter, the ribozymes, and the insert. The ribozymes must process the exact 5' and 3' ends of the genome.
- Full insert sequencing: two independent passes, or the vendor's full-coverage premium option.
- No mutations tolerated. The file must be synthesized exactly as provided.

## Files

- `monster_antigenomic.fa` = the insert. Positive-sense (antigenomic), 5' to 3'. This is the one to order.
- `monster_genome.fa` = the negative-sense (viral genome) copy, same 11,161 nt. For the record only. Do not use as the insert.

## Notes for the vendor

- T7 transcription of this insert produces an exact positive-sense RNA copy. The ribozymes trim it to the exact genome ends. The helper plasmids (ordered separately) use that exact RNA copy to build the live virus.
- No eukaryotic expression needed. No promoter other than T7.
- BSL-2 organism, standard lab strain. No special licensing.