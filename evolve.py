import random
from genome import Genome
from country import Sim


def fitness(g, pop=1_000_000, days=420):
    res = Sim(g, pop=pop, days=days).run()
    r0 = res["r0"]
    band = 1.0 if 5.5 <= r0 <= 8.0 else 0.25
    cband = 1.0 if res["cfr_obs"] <= 0.035 else 0.5
    return res["deaths_m"] * band * cband + 0.001 * r0, res


def evolve(pool=24, gens=120, keep=8):
    random.seed(11)
    genomes = [Genome.random() for _ in range(pool)]
    best = None
    for gen in range(gens):
        scored = []
        for g in genomes:
            f, res = fitness(g)
            scored.append((f, g, res))
        scored.sort(key=lambda x: -x[0])
        if best is None or scored[0][0] > best[0]:
            best = (scored[0][0], scored[0][1], scored[0][2], gen)
        elites = [g for _, g, _ in scored[:keep]]
        young = []
        for _ in range(pool - keep):
            a = random.choice(elites)
            b = random.choice(elites)
            child = a.clone()
            for k in a.genes:
                child.genes[k] = a.genes[k] if random.random() < 0.5 else b.genes[k]
            young.append(child.mutate(rate=0.35, mag=0.18))
        genomes = elites + young
    return best


if __name__ == "__main__":
    f, g, res, gen = evolve()
    print("gen", gen, "fitness %.3f" % f)
    print(g.label())
    print(res)