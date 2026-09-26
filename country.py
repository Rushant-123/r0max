import math

CONTACTS = 12.0
POP = 80_000_000


class Countermeasures:
    def __init__(self, detect_at=0.02, detect_day=45, ramp=21.0, lock_floor=0.3,
                 mask=0.7, vac_day=150, vac_len=90, vac_eff=0.75):
        self.detect_at = detect_at
        self.detect_day = detect_day
        self.ramp = ramp
        self.lock_floor = lock_floor
        self.mask = mask
        self.vac_day = vac_day
        self.vac_len = vac_len
        self.vac_eff = vac_eff
        self.day = 0
        self.trigger_day = None

    def tick(self, day, attack):
        self.day = day
        if self.trigger_day is None:
            if attack >= self.detect_at or day >= self.detect_day:
                self.trigger_day = day

    def lock(self):
        if self.trigger_day is None:
            return 1.0
        t = min(1.0, (self.day - self.trigger_day) / self.ramp)
        return 1.0 - t * (1.0 - self.lock_floor)

    def p_mult(self):
        if self.trigger_day is None:
            return 1.0
        return 1.0 - (1.0 - self.mask) * min(1.0, (self.day - self.trigger_day) / 30.0)

    def vac_rate(self, escape):
        if self.day < self.vac_day:
            return 0.0
        eff = self.vac_eff * (1.0 - 0.8 * escape)
        return eff / self.vac_len


class Sim:
    def __init__(self, genome, pop=POP, days=500, cm=None):
        self.g = genome
        self.ph = genome.phenotype()
        self.pop = float(pop)
        self.days = days
        self.cm = cm
        self.s = self.pop
        self.e = 0.0
        self.ia = 1.0
        self.isy = 0.0
        self.r = 0.0
        self.d = 0.0
        self.v = self.pop - 1.0
        self.cum_inf = 1.0
        self.hist = []
        self.peak = 0.0
        self.peak_day = 0
        self.r0_phen = genome.r0(CONTACTS)

    def run(self):
        ph = self.ph
        for day in range(self.days):
            attack = self.cum_inf / self.pop
            if self.cm:
                self.cm.tick(day, attack)
            lock = self.cm.lock() if self.cm else 1.0
            p = ph.p_contact * (self.cm.p_mult() if self.cm else 1.0)
            inf = self.ia + ph.sympt_mult() * self.isy
            lam = CONTACTS * lock * p * inf / self.pop
            if self.cm:
                vr = self.cm.vac_rate(ph.wane_rate / 0.012)
                if vr:
                    moved = min(self.s, self.s * vr)
                    self.s -= moved
                    self.r += moved
            new_e = self.s * (1.0 - math.exp(-lam))
            lat_out = self.e / ph.lat_days
            out = (self.ia + self.isy) / ph.inf_days
            dead = self.isy * (ph.cfr / ph.inf_days)
            waned = self.r * ph.wane_rate
            if self.v > 0.0:
                self.v -= new_e * (self.v / max(self.s, 1.0))
            self.s += waned - new_e
            self.e += new_e - lat_out
            ia_in = lat_out * ph.asym_share
            isy_in = lat_out * (1.0 - ph.asym_share)
            self.ia += ia_in - self.ia / ph.inf_days
            self.isy += isy_in - self.isy / ph.inf_days - dead
            self.r += out - dead - waned
            self.d += dead
            self.cum_inf += new_e
            self.hist.append(100.0 * (1.0 - self.v / self.pop))
            cur = (self.ia + self.isy) / self.pop
            if cur > self.peak:
                self.peak = cur
                self.peak_day = day
            if self.ia + self.isy + self.e < 0.5:
                break
        ever = 1.0 - self.v / self.pop
        return {
            "r0": self.r0_phen,
            "attack": ever,
            "attack_total": self.cum_inf / self.pop,
            "deaths": int(self.d),
            "deaths_m": self.d / 1e6,
            "peak_day": self.peak_day,
            "peak_frac": self.peak,
            "cfr_obs": self.d / max(1.0, self.cum_inf),
            "epiday": self.days,
        }