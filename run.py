from genome import Genome
from country import Sim, Countermeasures
from evolve import evolve


def report(tag, res):
    print("%-22s R0=%5.2f  attack=%5.1f%%  deaths=%6.3fM  cfr=%.1f%%  peak_day=%d"
          % (tag, res["r0"], 100 * res["attack"], res["deaths_m"],
             100 * res["cfr_obs"], res["peak_day"]))


def main():
    print("R0-MAX: in-silico monster build")
    print("country: 80M, zero prior immunity, 500 days")
    print()

    wild = Genome.wildtype()
    res_w = Sim(wild).run()
    report("wildtype spread:", res_w)

    res_w_cm = Sim(wild, cm=Countermeasures()).run()
    report("wildtype + fight:", res_w_cm)

    print()
    print("evolving the monster (150 gens)...")
    f, monster, res_e, gen = evolve(gens=150)
    report("monster spread:", res_e)
    print("   genome:", monster.label())

    res_m_cm = Sim(monster, cm=Countermeasures()).run()
    report("monster + fight:", res_m_cm)

    print()
    own = res_m_cm["attack"] >= 0.70
    contained = res_w_cm["attack"] < 0.40
    band = 5.5 <= res_m_cm["r0"] <= 8.5
    print("MONSTER in 6-8 band:   %s (R0=%.2f)" % ("PASS" if band else "FAIL", res_m_cm["r0"]))
    print("MONSTER owns country: %s (attack=%.1f%% >= 70%%)" % ("PASS" if own else "FAIL", 100 * res_m_cm["attack"]))
    print("WILDTYPE contained:   %s (attack=%.1f%% < 40%%)" % ("PASS" if contained else "FAIL", 100 * res_w_cm["attack"]))
    print("CFR in 1-4%% band:      %s (cfr=%.1f%%)" % ("PASS" if 0.01 <= res_m_cm["cfr_obs"] <= 0.04 else "FAIL", 100 * res_m_cm["cfr_obs"]))


if __name__ == "__main__":
    main()