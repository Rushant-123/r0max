import design
from genome import Genome
from country import Sim, Countermeasures
from evolve import evolve

def load(p):
    s=[]
    for l in open(p):
        if not l.startswith('>'): s.append(l.strip())
    return ''.join(s).upper()

a = load('vsv_j02428.fa')
b = load('monster.fa')

PARTS = design.GENE_PARTS
CODING = ['N','P','M','G','L']

edits = {}
total = 0
for part in CODING:
    st, en = PARTS[part]
    x = a[st-1:en]; y = b[st-1:en]
    pos = [st+i for i in range(len(x)) if x[i] != y[i]]
    edits[part] = pos
    total += len(pos)
print('total edits:', total)

W = 1200; M = 40
LINE_Y = 120; LINE_H = 26
SCALE = (W - 2*M) / 11161.0

def x(p):
    return M + p * SCALE

svg = []
svg.append('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="200" viewBox="0 0 %d 200">' % (W, W))
svg.append('<rect width="100%%" height="100%%" fill="#ffffff"/>')
svg.append('<text x="20" y="28" font-family="menlo,monospace" font-size="14" fill="#24292e">R0MAX monster  genome  11,161 nt  554 edits (M53 N74 G82 L345)  every edit synonymous</text>')

for name, (st, en) in PARTS.items():
    if name in ('leader','trailer'):
        svg.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="#8b949e" rx="2"/>' % (x(st-1), LINE_Y, (en-st+1)*SCALE, LINE_H))
    elif ' ig' in name:
        svg.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="#d0d7de"/>' % (x(st-1), LINE_Y+8, (en-st+1)*SCALE, LINE_H-16))
    else:
        svg.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="#0969da" rx="3"/>' % (x(st-1), LINE_Y, (en-st+1)*SCALE, LINE_H))
        mid = x(st-1) + (en-st+1)*SCALE/2.0
        svg.append('<text x="%.1f" y="%d" font-family="menlo,monospace" font-size="13" fill="#ffffff" text-anchor="middle">%s</text>' % (mid, LINE_Y+17, name))

for part in CODING:
    for p in edits[part]:
        svg.append('<rect x="%.2f" y="%d" width="1.1" height="9" fill="#cf222e"/>' % (x(p-1), LINE_Y-11))

svg.append('<rect x="%.1f" y="%d" width="%.1f" height="9" fill="#cf222e"/>' % (x(300), LINE_Y-11, 30*SCALE))
svg.append('<text x="%.1f" y="%d" font-family="menlo,monospace" font-size="11" fill="#cf222e">554 edits</text>' % (x(300)+30*SCALE+4, LINE_Y-3))

svg.append('<text x="%.1f" y="%d" font-family="menlo,monospace" font-size="11" fill="#8b949e">1</text>' % (x(0)-4, 165))
svg.append('<text x="%.1f" y="%d" font-family="menlo,monospace" font-size="11" fill="#8b949e">11,161</text>' % (x(11161)-30, 165))
svg.append('<text x="20" y="185" font-family="menlo,monospace" font-size="11" fill="#57606a">blue = the five genes (proteins identical to wild type)   red = the 554 recoded positions   gray = noncoding, untouched</text>')
svg.append('</svg>')

open('figures/genome_map.svg','w').write('\n'.join(svg))
print('genome_map.svg written')

WILD = Genome.wildtype()
_, MON, _, _ = evolve(gens=150)
print('monster R0: %.2f' % MON.r0())

mw = Sim(WILD, cm=Countermeasures()); mw.run()
mo = Sim(MON, cm=Countermeasures()); mo.run()
print('wildtype ever final: %.1f  monster ever final: %.1f' % (mw.hist[-1], mo.hist[-1]))

W2 = 900; H2 = 380; ML = 60; MB = 70; MT = 50; MR = 20
PW = W2 - ML - MR; PH = H2 - MT - MB
maxd = max(len(mw.hist), len(mo.hist))

c = []
c.append('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">' % (W2, H2, W2, H2))
c.append('<rect width="100%%" height="100%%" fill="#ffffff"/>')
c.append('<text x="20" y="28" font-family="menlo,monospace" font-size="14" fill="#24292e">R0MAX monster vs wildtype   80M country, same countermeasures</text>')
for gy in range(0, 101, 20):
    py = MT + PH - PH * gy / 100.0
    c.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#eaeef2" stroke-width="1"/>' % (ML, py, W2-MR, py))
    c.append('<text x="%d" y="%.1f" font-family="menlo,monospace" font-size="11" fill="#8b949e" text-anchor="end">%d%%</text>' % (ML-8, py+4, gy))

def px(i):
    return ML + PW * i / float(maxd)

def path(hist):
    d = ['M %.1f %.1f' % (px(0), MT + PH - PH*hist[0]/100.0)]
    for i in range(1, len(hist)):
        d.append('L %.1f %.1f' % (px(i), MT + PH - PH*hist[i]/100.0))
    return ' '.join(d)

c.append('<path d="%s" fill="none" stroke="#cf222e" stroke-width="2.2"/>' % path(mo.hist))
c.append('<path d="%s" fill="none" stroke="#8b949e" stroke-width="2.2"/>' % path(mw.hist))

for frac, lab in [(0.0,'day 0'), (0.5,'day %d' % int(maxd*0.5)), (1.0,'day %d' % maxd)]:
    c.append('<text x="%.1f" y="%d" font-family="menlo,monospace" font-size="11" fill="#8b949e" text-anchor="middle">%s</text>' % (ML + PW*frac, H2-MB+24, lab))

lx = ML + 24; ly = 26
c.append('<rect x="%d" y="%d" width="26" height="4" fill="#cf222e" rx="1"/>' % (lx-4, ly-4))
c.append('<text x="%d" y="%d" font-family="menlo,monospace" font-size="12" fill="#24292e">monster  %.1f%% ever</text>' % (lx+26, ly, mo.hist[-1]))
c.append('<rect x="%d" y="%d" width="26" height="4" fill="#8b949e" rx="1"/>' % (lx+190, ly-4))
c.append('<text x="%d" y="%d" font-family="menlo,monospace" font-size="12" fill="#24292e">wildtype  %.1f%% ever</text>' % (lx+216, ly, mw.hist[-1]))
c.append('<text x="20" y="%d" font-family="menlo,monospace" font-size="11" fill="#57606a">share of the 80M country ever infected, through the same lockdowns, masks, and 75%% vaccine</text>' % (H2-MB+44))
c.append('</svg>')

open('figures/spread.svg','w').write('\n'.join(c))
print('spread.svg written')