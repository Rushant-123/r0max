from dataclasses import dataclass
import random

GENES = [
    "route",
    "entry",
    "load",
    "stability",
    "duration",
    "incubation",
    "asymptomatic",
    "escape",
    "virulence",
]


def lerp(g, lo, hi):
    return lo + (hi - lo) * max(0.0, min(1.0, g))


@dataclass
class Phenotype:
    p_route: float
    p_entry: float
    p_load: float
    p_stability: float
    inf_days: float
    lat_days: float
    asym_share: float
    wane_rate: float
    cfr: float
    severity: float = 0.0

    @property
    def p_contact(self):
        p = self.p_route * self.p_entry * self.p_load * self.p_stability
        return max(0.005, min(0.2, p))

    def sympt_mult(self):
        return 0.05 + 0.95 * (1.0 - 6.0 * self.cfr)

    def contacts_factor(self):
        return self.asym_share + (1 - self.asym_share) * self.sympt_mult()


@dataclass
class Genome:
    genes: dict

    def clone(self):
        return Genome(dict(self.genes))

    def mutate(self, rate=0.25, mag=0.2):
        g = self.clone()
        for k in GENES:
            if random.random() < rate:
                g.genes[k] = min(1.0, max(0.0, g.genes[k] + random.gauss(0, mag)))
        return g

    def phenotype(self):
        g = self.genes
        return Phenotype(
            p_route=lerp(g["route"], 0.02, 0.10),
            p_entry=lerp(g["entry"], 0.6, 1.4),
            p_load=lerp(g["load"], 0.7, 1.5),
            p_stability=lerp(g["stability"], 0.9, 1.2),
            inf_days=lerp(g["duration"], 3.0, 8.0),
            lat_days=lerp(g["incubation"], 3.0, 8.0),
            asym_share=lerp(g["asymptomatic"], 0.0, 0.5),
            wane_rate=lerp(g["escape"], 0.0, 0.012),
            cfr=lerp(g["virulence"], 0.005, 0.05),
            severity=0.0,
        )

    def r0(self, contacts=12.0):
        ph = self.phenotype()
        return contacts * ph.p_contact * ph.inf_days * ph.contacts_factor()

    def label(self):
        ph = self.phenotype()
        return " ".join(
            [
                "route=%.2f" % ph.p_route,
                "entry=%.2f" % ph.p_entry,
                "load=%.2f" % ph.p_load,
                "stab=%.2f" % ph.p_stability,
                "inf_d=%.1f" % ph.inf_days,
                "lat_d=%.1f" % ph.lat_days,
                "asym=%.0f%%" % (100 * ph.asym_share),
                "wane=%.3f/d" % ph.wane_rate,
                "cfr=%.1f%%" % (100 * ph.cfr),
            ]
        )

    @staticmethod
    def wildtype():
        return Genome({k: 0.5 for k in GENES})

    @staticmethod
    def random():
        return Genome({k: random.random() for k in GENES})