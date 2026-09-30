import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch10-cell-cycle-and-cell-division')
d = Deck('Chapter 10: Cell Cycle and Cell Division', 'Class 11', ['class-11', 'biology', 'ch-10'])
d.description = 'Cell cycle phases, G0, mitosis stages, cytokinesis, meiosis I and II, and their significance'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
C = lambda cx, cy, w=130, h=38: [cx - w // 2, cy - h // 2, w, h]

# ---------------------------------------------------------------- 10.1 Cell cycle
d.sec('10.1-cell-cycle')
d.basic('What is the cell cycle?', 'The sequence of events by which a cell ' + T('duplicates its genome') + ', synthesises other constituents and divides into two daughter cells')
d.basic('Which three processes must be coordinated in a cell cycle?', 'Cell division, ' + T('DNA replication') + ' and cell growth')
d.basic('Is cell growth continuous? Is DNA synthesis?', 'Cytoplasmic growth is ' + T('continuous') + '; DNA synthesis happens ' + X('only in one stage') + ' (S phase)')
d.basic('How long is the cell cycle of human cells in culture?', 'About ' + N('24 hours'))
d.basic('How long is the yeast cell cycle?', 'About ' + N('90 minutes'))
d.basic('Two basic phases of the cell cycle?', T('Interphase') + ' and ' + T('M phase') + ' (mitosis phase)')
d.basic('In a 24-hour human cell cycle, how long does M phase last?', 'About ' + N('1 hour'))
d.basic('What fraction of the cell cycle is interphase?', 'More than ' + N('95%'))
d.cloze('M phase starts with {{c1::karyokinesis}} (nuclear division) and usually ends with {{c2::cytokinesis}} (division of cytoplasm).')
d.basic('Why is calling interphase the "resting phase" misleading?', 'The cell is ' + X('not resting') + ': it grows and ' + T('replicates DNA') + ' in preparation for division. Only the nucleus looks inactive under the microscope.')
d.cloze('Interphase = {{c1::G1}} (Gap 1) → {{c2::S}} (Synthesis) → {{c3::G2}} (Gap 2).')
d.occlusion('Figure 10.1 · Cell cycle', M + 'fig_10_1_cell_cycle.webp', (1001, 896), [
    ('G1', C(561, 317, 90, 64), True), ('S', C(735, 625, 80, 64), True), ('G2', C(491, 745, 90, 64), True),
    ('M phase', [30, 385, 78, 220], True)], extra='The narrow black arc is M phase; the wide yellow arcs are interphase (G1, S, G2).')

d.sec('10.1-phases')
d.basic('What happens in G1 phase?', 'The cell is ' + T('metabolically active') + ' and grows continuously, but ' + X('does not replicate DNA'))
d.basic('G1 phase is the interval between which two events?', 'End of ' + T('mitosis') + ' and initiation of ' + T('DNA replication'))
d.basic('What happens in S phase?', T('DNA replication') + ': DNA per cell doubles')
d.basic('DNA content goes from __ to __ in S phase.', N('2C') + ' → ' + N('4C'))
d.basic('Does chromosome number change in S phase?', X('No') + '. A 2n cell stays 2n; each chromosome now has two chromatids.')
d.basic('In animal cells, what duplicates in the cytoplasm during S phase?', 'The ' + T('centriole'))
d.basic('What happens in G2 phase?', T('Proteins') + ' are synthesised in preparation for mitosis; cell growth continues')
d.basic('Intuition: why does counting chromosomes not double in S phase?', 'Chromosomes are counted by ' + T('centromeres') + '.<br>After S, each chromosome has two sister chromatids joined at ' + N('one') + ' centromere, so the count stays the same')
d.basic('Onion root tip cell has 16 chromosomes. Number at G1, after S, after M?', N('16') + ', ' + N('16') + ', ' + N('16'))
d.basic('If DNA after M phase is 2C, what is it at G1, after S and at G2?', N('2C') + ', ' + N('4C') + ', ' + N('4C'))

d.sec('10.1-g0')
d.basic('What is the quiescent stage (G0)?', 'An inactive stage that cells ' + T('exit G1') + ' into.<br>They stay metabolically active but do not proliferate unless required')
d.basic('Example of adult animal cells that do not appear to divide?', E('Heart cells'))
d.basic('Are G0 cells metabolically dead?', X('No') + '. They are metabolically active; they just do not divide.')
d.basic('In animals, which cells show mitosis?', 'Only ' + T('diploid somatic cells') + ' (with exceptions)')
d.basic('Example of haploid animal cells that divide by mitosis?', E('Male honey bees') + ' (drones develop from unfertilised eggs)')
d.basic('Can plants show mitosis in haploid cells?', T('Yes') + ': plants divide mitotically in both haploid and diploid cells.<br>e.g. the haploid gametophyte of mosses and ferns')

# ---------------------------------------------------------------- 10.2 M phase
d.sec('10.2-m-phase')
d.basic('Why is mitosis called equational division?', 'Chromosome number in parent and progeny cells is the ' + T('same'))
d.basic('Four stages of karyokinesis?', 'Prophase, metaphase, anaphase, telophase')
d.basic('Mnemonic for the mitosis stages in order?', '"' + T('I P-MAT') + '": Interphase, then Prophase, Metaphase, Anaphase, Telophase')
d.basic('Are the stages of mitosis sharply separated?', X('No') + '. Division is a progressive process; clear-cut lines cannot be drawn.')

d.sec('10.2.1-prophase')
d.basic('What marks the start of prophase?', 'Initiation of ' + T('condensation') + ' of chromosomal material')
d.basic('What are prophase chromosomes made of?', 'Two ' + T('chromatids') + ' attached at the ' + T('centromere'))
d.basic('What does the centrosome do in prophase?', 'The duplicated centrosome moves towards ' + T('opposite poles'))
d.basic('What are asters?', 'Microtubules radiating from each ' + T('centrosome'))
d.basic('What is the mitotic apparatus?', 'The two ' + T('asters') + ' together with the ' + T('spindle fibres'))
d.basic('Which structures are not seen at the end of prophase?', T('Golgi complex, ER, nucleolus') + ' and the ' + T('nuclear envelope'))
d.basic('Plant cells lack centrioles. How do they form a spindle?', 'Spindle fibres organise without centrioles or asters (an ' + T('anastral') + ' spindle). NCERT describes the animal-cell pattern.')
d.basic('Identify this stage of mitosis.', T('Early prophase') + ': chromatin begins to condense; nuclear envelope still intact', **img('mitosis_early_prophase'))
d.basic('Identify this stage of mitosis.', T('Late prophase') + ': condensed chromosomes; nuclear envelope breaking up', **img('mitosis_late_prophase'))

d.sec('10.2.2-metaphase')
d.basic('What marks the start of metaphase?', 'Complete disintegration of the ' + T('nuclear envelope'))
d.basic('At which stage is chromosome morphology best studied?', T('Metaphase') + ': condensation is complete')
d.basic('What are kinetochores?', 'Small ' + T('disc-shaped') + ' structures on the surface of centromeres, where spindle fibres attach')
d.basic('What is the metaphase plate?', 'The plane of alignment of chromosomes at the ' + T('equator') + ' in metaphase')
d.basic('In metaphase, how are sister chromatids attached to the spindle?', 'Each chromatid, by its kinetochore, to fibres from ' + T('opposite poles'))
d.basic('Key features of metaphase?', 'Spindle fibres attach to ' + T('kinetochores') + '; chromosomes align on the ' + T('metaphase plate'))
d.basic('Identify this stage.', T('Transition to metaphase') + ': chromosomes being moved to the equator by spindle fibres', **img('mitosis_transition_metaphase'))
d.basic('Identify this stage of mitosis.', T('Metaphase') + ': all chromosomes lined up at the equator', **img('mitosis_metaphase'))
d.basic('Why is metaphase used to make karyotypes?', 'Chromosomes are ' + T('most condensed') + ' and spread out, so their number, size and centromere position are easiest to see. (Colchicine arrests cells at metaphase for this.)')

d.sec('10.2.3-anaphase')
d.basic('What happens at the onset of anaphase?', 'Each chromosome ' + T('splits') + '; sister chromatids (now daughter chromosomes) move to opposite poles')
d.basic('In anaphase, which part of the chromosome leads towards the pole?', 'The ' + T('centromere') + '; the arms trail behind')
d.basic('Key events of anaphase?', T('Centromeres split') + ', chromatids separate and move to opposite poles')
d.basic('Identify this stage of mitosis.', T('Anaphase') + ': daughter chromosomes pulled to the poles, centromeres leading (V shapes)', **img('mitosis_anaphase'))

d.sec('10.2.4-telophase')
d.basic('What happens to chromosomes in telophase?', 'They reach the poles, ' + T('decondense') + ' and lose their individuality')
d.basic('Key events of telophase?', 'Chromosomes cluster at poles; ' + T('nuclear envelope') + ' re-forms around each cluster; ' + T('nucleolus, Golgi, ER') + ' re-form')
d.basic('Telophase is the reverse of which stage?', T('Prophase') + ': chromosomes decondense and the nuclear envelope and nucleolus return')
d.basic('Identify this stage of mitosis.', T('Telophase') + ': two daughter nuclei forming; furrow starting', **img('mitosis_telophase'))

d.sec('10.2.5-cytokinesis')
d.basic('What is cytokinesis?', 'Division of the ' + T('cytoplasm') + ' into two daughter cells')
d.basic('How does cytokinesis happen in animal cells?', 'A ' + T('furrow') + ' in the plasma membrane deepens and joins in the centre')
d.basic('How does cytokinesis happen in plant cells?', 'A ' + T('cell plate') + ' forms in the centre and grows ' + T('outward') + ' to meet the lateral walls')
d.basic('Why can\'t plant cells use a furrow?', 'They are enclosed by a relatively ' + T('inextensible cell wall'))
d.basic('What does the cell plate represent?', 'The ' + T('middle lamella') + ' between the walls of two adjacent cells')
d.cloze('Animal cytokinesis goes from the {{c1::outside inwards (furrow)}}; plant cytokinesis goes from the {{c2::centre outwards (cell plate)}}.')
d.basic('What is a syncytium? Example?', 'A multinucleate condition when karyokinesis is ' + X('not followed') + ' by cytokinesis, e.g. ' + E('liquid endosperm of coconut'))
d.basic('Which stage does this panel show?', T('Cytokinesis') + ' complete: two daughter cells. (NCERT labels this panel "Interphase (e)", meaning the daughter cells have entered interphase.)', **img('mitosis_cytokinesis'))

# ---------------------------------------------------------------- 10.3 Significance of mitosis
d.sec('10.3-significance')
d.basic('Mitosis is usually restricted to which cells?', T('Diploid') + ' cells. Exception: haploid cells of some lower plants and social insects.')
d.basic('What do daughter cells of mitosis have?', 'An ' + T('identical genetic complement') + ' (diploid)')
d.basic('List the significance of mitosis.', 'Growth of multicellular organisms; restoring the ' + T('nucleo-cytoplasmic ratio') + '; ' + T('cell repair') + '; continuous growth of plants via meristems')
d.basic('Why must a growing cell divide? (nucleo-cytoplasmic ratio)', 'Cytoplasm grows faster than the nucleus\'s control capacity; division ' + T('restores the ratio'))
d.basic('Which cells are constantly replaced by mitosis?', E('Upper epidermis, gut lining, blood cells'))
d.basic('Which plant tissues give continuous growth by mitosis?', 'Meristems: ' + T('apical') + ' and ' + T('lateral cambium'))

# ---------------------------------------------------------------- 10.4 Meiosis
d.sec('10.4-meiosis')
d.basic('What is meiosis?', 'A division that ' + T('halves') + ' the chromosome number, producing haploid daughter cells')
d.basic('Where does meiosis occur?', 'During ' + T('gametogenesis') + ' in plants and animals')
d.basic('Meiosis ensures the haploid phase; what restores the diploid phase?', T('Fertilisation'))
d.basic('How many nuclear divisions and DNA replications in meiosis?', N('Two') + ' divisions (meiosis I and II), but only ' + N('one') + ' DNA replication')
d.basic('Key features of meiosis?', 'Pairing of ' + T('homologous chromosomes') + '<br>Recombination between non-sister chromatids<br>' + N('Four') + ' haploid cells at the end')
d.basic('Between which chromatids does recombination occur?', T('Non-sister') + ' chromatids of homologous chromosomes')

d.sec('10.4.1-prophase-1')
d.cloze('Prophase I substages: {{c1::leptotene}} → {{c2::zygotene}} → {{c3::pachytene}} → {{c4::diplotene}} → {{c5::diakinesis}}.')
d.basic('Mnemonic for the prophase I substages?', '"' + T('Lazy Zebras Prefer Drinking Daily') + '": Leptotene, Zygotene, Pachytene, Diplotene, Diakinesis')
d.basic('Prophase I vs prophase of mitosis?', 'Prophase I is ' + T('longer and more complex'))
d.basic('What happens in leptotene?', 'Chromosomes become gradually ' + T('visible') + '; compaction continues')
d.basic('What happens in zygotene?', 'Homologous chromosomes start pairing: ' + T('synapsis'))
d.basic('What is synapsis?', 'Pairing of ' + T('homologous chromosomes') + ' (in zygotene)')
d.basic('What accompanies synapsis (seen in electron micrographs)?', 'The ' + T('synaptonemal complex'))
d.basic('What is a bivalent?', 'The complex of a pair of synapsed homologous chromosomes; also called a ' + T('tetrad'))
d.basic('Why is a bivalent also called a tetrad?', 'It contains ' + N('two') + ' chromosomes = ' + N('four') + ' chromatids')
d.basic('Which of the first three substages is the longest?', T('Pachytene') + ' (leptotene and zygotene are short-lived)')
d.basic('What happens in pachytene?', 'Four chromatids of each bivalent become distinct (tetrads); ' + T('crossing over') + ' between non-sister chromatids')
d.basic('What are recombination nodules?', 'Sites where ' + T('crossing over') + ' occurs (appear in pachytene)')
d.basic('What is crossing over?', 'Exchange of genetic material between ' + T('homologous chromosomes'))
d.basic('Which enzyme mediates crossing over?', T('Recombinase'))
d.basic('What marks the beginning of diplotene?', 'Dissolution of the ' + T('synaptonemal complex') + '; homologues begin to separate except at crossover sites')
d.basic('What are chiasmata?', 'The ' + T('X-shaped') + ' structures where homologues stay joined at crossover sites (diplotene)')
d.basic('In which cells can diplotene last months or years?', T('Oocytes') + ' of some vertebrates')
d.basic('Intuition: human oocytes and diplotene?', 'Human primary oocytes start meiosis before birth and pause in ' + T('diplotene') + ' (dictyotene).<br>They stay there until ovulation, which can be ' + N('12–50 years') + ' later')
d.basic('What marks diakinesis?', T('Terminalisation of chiasmata'))
d.basic('What else happens in diakinesis?', 'Chromosomes fully condensed; meiotic ' + T('spindle') + ' assembles; by its end the ' + T('nucleolus') + ' and ' + T('nuclear envelope') + ' disappear')
d.basic('Diakinesis is a transition to which stage?', T('Metaphase I'))
table_card(d, 'Prophase I', 'Which substage?', [
    ('Chromosomes become visible', 'Leptotene', False), ('Synapsis, synaptonemal complex', 'Zygotene', False),
    ('Crossing over, recombination nodules', 'Pachytene', False), ('Chiasmata visible', 'Diplotene', False),
    ('Terminalisation of chiasmata', 'Diakinesis', False)], term='Prophase I substages: key event')

d.sec('10.4.1-meiosis-1')
d.basic('What happens in metaphase I?', 'Bivalents align on the ' + T('equatorial plate') + '.<br>Microtubules from opposite poles attach to kinetochores of ' + T('homologous chromosomes'))
d.basic('What happens in anaphase I?', T('Homologous chromosomes') + ' separate; sister chromatids ' + X('stay together') + ' at their centromeres')
d.basic('What happens in telophase I?', 'Nuclear membrane and nucleolus reappear; cytokinesis follows, forming a ' + T('dyad of cells'))
d.basic('Do chromosomes fully decondense after telophase I?', X('No') + '. They may disperse somewhat but do not reach the extended interphase state.')
d.basic('What is interkinesis?', 'The short stage between the two meiotic divisions')
d.basic('Does DNA replicate in interkinesis?', X('No'))
d.occlusion('Figure 10.3 · Stages of meiosis I', M + 'fig_10_3_meiosis_1.webp', (1001, 462), [
    ('Prophase I', C(200, 337), True), ('Metaphase I', C(434, 334), True),
    ('Anaphase I', C(637, 357), True), ('Telophase I', C(824, 387), True)])

d.sec('10.4.2-meiosis-2')
d.basic('When does meiosis II begin?', 'Immediately after cytokinesis, usually ' + T('before') + ' chromosomes have fully elongated')
d.basic('Meiosis II resembles which division?', 'A normal ' + T('mitosis'))
d.basic('Prophase II vs prophase I?', 'Prophase II is much ' + T('simpler'))
d.basic('What happens in metaphase II?', 'Chromosomes align at the equator; microtubules attach to kinetochores of ' + T('sister chromatids'))
d.basic('What happens in anaphase II?', T('Centromeres split') + '; sister chromatids move to opposite poles by shortening of microtubules')
d.basic('What happens in telophase II?', 'Nuclear envelope re-forms; cytokinesis gives a ' + T('tetrad of cells') + ': ' + N('four') + ' haploid daughter cells')
d.occlusion('Figure 10.4 · Stages of meiosis II', M + 'fig_10_4_meiosis_2.webp', (1001, 544), [
    ('Prophase II', C(200, 484), True), ('Metaphase II', C(450, 484), True),
    ('Anaphase II', C(684, 504), True), ('Telophase II', pad(C(924, 524, 140, 38), 0, (1001, 544)), True)])

d.sec('10.4-compare')
d.basic('Anaphase of mitosis vs anaphase I of meiosis?', 'Mitosis: ' + T('sister chromatids') + ' separate (centromere splits). Anaphase I: ' + T('homologous chromosomes') + ' separate; centromere does ' + X('not') + ' split.')
d.basic('Which is the reduction division: meiosis I or II?', T('Meiosis I') + ' halves the chromosome number; meiosis II is equational')
d.basic('A cell with 2n = 8 enters meiosis. Chromosomes per cell after meiosis I and after meiosis II?', N('4') + ' (each with 2 chromatids), then ' + N('4') + ' (single chromatids)')
table_card(d, 'Mitosis vs meiosis', 'Compare', [
    ('Divisions', 'Mitosis 1 · Meiosis 2', False), ('Daughter cells', '2 diploid · 4 haploid', False),
    ('Synapsis & crossing over', 'Absent · present (prophase I)', False), ('Daughter cells identical?', 'Yes · no (variation)', False),
    ('Where', 'Somatic cells · gamete-forming cells', False)], term='Mitosis vs meiosis')
table_card(d, 'Exercise 16', 'Chromosomes (N) and DNA (C) per cell, 2n cell?', [
    ('G1', '2n, 2C', False), ('After S / G2', '2n, 4C', False), ('After mitosis', '2n, 2C', False),
    ('After meiosis I', 'n, 2C', False), ('After meiosis II', 'n, C', False)], term='N and C through the cycle')
d.basic('Can there be DNA replication without cell division?', T('Yes') + ': endoreduplication, e.g. ' + E('polytene chromosomes') + ' of Drosophila salivary glands')
d.basic('Where are the four meiotic products unequal in size?', E('Oogenesis') + ': one large ovum and small polar bodies. (Spermatogenesis gives four equal sperms.)')

# ---------------------------------------------------------------- 10.5 Significance of meiosis
d.sec('10.5-significance')
d.basic('Significance of meiosis?', 'Conserves the ' + T('chromosome number') + ' of a species across generations; increases ' + T('genetic variability'))
d.basic('What is paradoxical about meiosis conserving chromosome number?', 'It conserves the number across generations by ' + T('halving') + ' it in gametes; fertilisation doubles it back')
d.basic('Why is variation from meiosis important?', 'Variations are the raw material for ' + T('evolution'))
d.basic('Two sources of variation in meiosis?', T('Crossing over') + ' (pachytene) and ' + T('independent assortment') + ' of homologues (metaphase I / anaphase I)')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
