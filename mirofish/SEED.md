# MiroFish seed material: the R0MAX event

Upload this to MiroFish as seed material, together with REQUEST.md.

## The event

A recoded strain of a virus (VSV family, a standard lab virus, safe, well studied). This one is a digital twin for a simulation exercise: a strain recoded for one thing, maximum spread.

The strain (called "monster") has eight engineered levers, all pushed hard:

| Lever | Setting |
|---|---|
| Route | aerosol (rides air for hours) |
| Duration of infectiousness | long |
| Spread before you feel sick | yes |
| Asymptomatic spreaders | some |
| Viral load per breath | high |
| Stability outside a host | hours |
| Immune escape | yes (reinfects about every 80 days) |
| Cell entry | high |

The measured behavior in an equation-based model (SEIR, 80 million people, zero prior immunity):

- Basic spread number R0 = 7.96 (each infected person infects about 8 on average)
- Observed kill rate = 3.5% of infections
- Through the same lockdowns, masks, and a 75% vaccine that easily contain the parent strain (0.2% of the country infected), the monster takes over 98.4% of an 80 million person country
- The parent strain: contained in under 70 days. The monster: 98.4% by day 150.

The parent strain numbers, for comparison: R0 = 4.0, kill rate 2.0%, contained by the same countermeasures.

## What the math model does not capture

The equation model treats people as numbers. It does not model:

- whether people comply with lockdowns, or rebel
- panic, rumors, migration out of cities
- leaders choosing between the economy and the health measures
- vaccine hesitancy, trust, protest waves
- the economy: supply chains, school closures, jobs
- information: news, rumors, social media
- the political cycle: elections, approval ratings

That society layer is what MiroFish is for. The math layer is done. The society layer is the open question: does a monster like this still take over a country of real people, not equations?