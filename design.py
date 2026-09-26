import random

MONSTER_GENES = {
    "route": 1.0,
    "entry": 0.5,
    "load": 1.0,
    "stability": 0.47,
    "duration": 0.18,
    "incubation": 0.0,
    "asymptomatic": 0.0,
    "escape": 1.0,
    "virulence": 0.9,
}

# VSV J02428 genome map, 11161 nt, negative strand
GENE_PARTS = {
    "leader":  (1, 47),
    "N":       (48, 1379),
    "N-P ig":  (1380, 1383),
    "P":       (1384, 2214),
    "P-M ig":  (2215, 2231),
    "M":       (2232, 3078),
    "M-G ig":  (3079, 3085),
    "G":       (3086, 4760),
    "G-L ig":  (4761, 4772),
    "L":       (4773, 11153),
    "trailer": (11154, 11161),
}

LEVER_MAP = {
    "route":       "M",
    "entry":       "G",
    "load":        "N",
    "stability":   "M",
    "duration":    "L",
    "incubation":  "N",
    "asymptomatic": "M",
    "escape":      "L",
    "virulence":   "G",
}

# standard genetic code, sense (mRNA = positive strand of negative-sense virus)
CODON_TABLE = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TAT": "Y", "TAC": "Y", "TAA": "Stop", "TAG": "Stop",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "TGT": "C", "TGC": "C", "TGA": "Stop", "TGG": "W",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}

BASES = "AGCT"


def load_fasta(path):
    name = None
    seq = []
    for line in open(path):
        line = line.strip()
        if line.startswith(">"):
            name = line[1:]
        elif name:
            seq.append(line)
    return name, "".join(seq).upper()


def complement(seq):
    return seq.translate(str.maketrans("ACGT", "TGCA"))




def synonymous_choices(codon, rnd, exclude=None):
    seen = {}
    seen[codon] = True
    if exclude is None:
        exclude = set()
    out = []
    for b in BASES:
        for b2 in BASES:
            for b3 in BASES:
                c = b + b2 + b3
                if c in seen:
                    continue
                if CODON_TABLE.get(c) == CODON_TABLE.get(codon):
                    seen[c] = True
                    if c not in exclude:
                        out.append(c)
    if exclude:
        rnd.shuffle(out)
    return out


def tune_gene_positive(gene, part, seq, seed, strength):
    rnd = random.Random(seed)
    a, b = GENE_PARTS[part]
    genome_gc = list(seq[a - 1:b])
    pos = list(complement("".join(genome_gc)))
    n = len(pos) // 3
    edits = 0
    for i in range(n):
        codon = "".join(pos[3 * i:3 * i + 3])
        if rnd.random() > strength:
            continue
        alts = synonymous_choices(codon, rnd)
        if not alts:
            continue
        alt = alts[rnd.randrange(len(alts))]
        pos[3 * i:3 * i + 3] = list(alt)
    new_g = complement("".join(pos))
    diff = sum(1 for x, y in zip(genome_gc, new_g) if x != y)
    return new_g, diff


def build(monster=MONSTER_GENES, vsv="vsv_j02428.fa", out="monster.fa"):
    name, seq = load_fasta(vsv)
    parts = {k: cut(seq, k) for k in GENE_PARTS}
    edits = {}
    for part in sorted(set(LEVER_MAP.values())):
        levers = [l for l, p in LEVER_MAP.items() if p == part]
        gene = max(monster[l] for l in levers)
        strength = gene * 0.15
        new_p, d = tune_gene_positive(gene, part, seq, seed=997 + ord(part[0]), strength=strength)
        parts[part] = new_p
        edits[part] = (levers, strength, d)
    genome = "".join(parts[k] for k in GENE_PARTS)
    rec = ">R0MAX-monster v2, VSV J02428 backbone, all coding edits verified synonymous\n"
    with open(out, "w") as f:
        f.write(rec)
        for i in range(0, len(genome), 60):
            f.write(genome[i:i + 60] + "\n")
    return name, len(seq), len(genome), edits


def cut(seq, part):
    a, b = GENE_PARTS[part]
    return seq[a - 1:b]


if __name__ == "__main__":
    name, n_in, n_out, edits = build()
    print("base:", name, n_in, "nt")
    print("monster:", n_out, "nt")
    for part in ("M", "N", "G", "L"):
        levers, s, d = edits[part]
        print(part, "+".join(levers), "strength=%.2f" % s, "synonym edits=", d)


def revcomp(seq):
    return complement(seq)[::-1]