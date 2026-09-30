import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch02-human-reproduction')
d = Deck('Chapter 2: Human Reproduction', 'Class 12', ['class-12', 'biology', 'ch-2'])
d.description = 'Male and female reproductive systems, gametogenesis, menstrual cycle, fertilisation, implantation, pregnancy, parturition and lactation'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
MA, MB, FB, SP, OV, MG = (1001, 607), (1001, 730), (1001, 543), (889, 1001), (1001, 718), (1001, 654)

# ---------------------------------------------------------------- intro
d.sec('2.0-intro')
d.basic('Humans are ___ reproducing and ___ .', T('Sexually') + ' reproducing and ' + T('viviparous'))
d.cloze('Reproductive events in order: {{c1::gametogenesis}} → {{c2::insemination}} → {{c3::fertilisation}} → blastocyst formation and {{c4::implantation}} → {{c5::gestation}} → {{c6::parturition}}.')
d.basic('Male vs female difference in gamete formation with age?', 'Sperm formation ' + T('continues even in old men') + '; ovum formation ' + X('ceases') + ' around ' + N('50 years'))

# ---------------------------------------------------------------- 2.1 Male
d.sec('2.1-male-reproductive-system')
d.basic('Where is the male reproductive system located?', 'In the ' + T('pelvis region'))
d.basic('Components of the male reproductive system?', 'A pair of ' + T('testes') + ', accessory ducts, accessory glands and external genitalia')
d.basic('Where are the testes situated?', 'Outside the abdominal cavity in a pouch called the ' + T('scrotum'))
d.basic('Function of the scrotum?', 'Keeps testes ' + N('2–2.5 °C') + ' lower than body temperature, needed for ' + T('spermatogenesis'))
d.basic('Size of an adult testis?', 'Oval; ' + N('4–5 cm') + ' long, ' + N('2–3 cm') + ' wide')
d.basic('How many testicular lobules per testis?', 'About ' + N('250'))
d.basic('What does each testicular lobule contain?', N('One to three') + ' highly coiled ' + T('seminiferous tubules') + ', where sperms are produced')
d.basic('Two cell types lining a seminiferous tubule?', T('Male germ cells (spermatogonia)') + ' and ' + T('Sertoli cells'), **fig('fig_2_2_seminiferous_tubule'))
d.basic('Function of Sertoli cells?', 'Provide ' + T('nutrition') + ' to the germ cells')
d.basic('What do interstitial spaces contain?', 'Small blood vessels, ' + T('interstitial (Leydig) cells') + ' and other immunologically competent cells')
d.basic('Function of Leydig cells?', 'Synthesise and secrete ' + T('androgens') + ' (testicular hormones)')
d.basic('Identify labelled parts in Figure 2.2.', 'Interstitial cells, spermatogonia, spermatozoa, Sertoli cells (T.S. of seminiferous tubules)', **img('fig_2_2_seminiferous_tubule'))
d.cloze('Male accessory ducts (in order of sperm flow): seminiferous tubules → {{c1::rete testis}} → {{c2::vasa efferentia}} → {{c3::epididymis}} → {{c4::vas deferens}} → ejaculatory duct → urethra.')
d.basic('Where is the epididymis located?', 'Along the ' + T('posterior surface') + ' of each testis')
d.basic('Course of the vas deferens?', 'Ascends to the abdomen<br>' + T('Loops over the urinary bladder') + '<br>Receives the seminal vesicle duct<br>Opens into the urethra as the ' + T('ejaculatory duct'))
d.basic('Function of the male accessory ducts?', T('Store and transport') + ' sperms from testis to the outside through the urethra')
d.basic('What is the urethral meatus?', 'The ' + T('external opening') + ' of the urethra at the tip of the penis')
d.basic('What is the glans penis and what covers it?', 'Enlarged end of the penis, covered by a loose fold of skin, the ' + T('foreskin'))
d.basic('Male accessory glands?', 'Paired ' + T('seminal vesicles') + ', a ' + T('prostate') + ', paired ' + T('bulbourethral glands'))
d.basic('Seminal plasma is rich in?', T('Fructose, calcium') + ' and certain ' + T('enzymes'))
d.basic('Extra function of bulbourethral gland secretion?', T('Lubrication') + ' of the penis')
d.basic('Why fructose in semen? (intuition)', 'It is the ' + T('fuel') + ' for sperm mitochondria that power the tail')
d.occlusion('Figure 2.1b · Male reproductive system', M + 'fig_2_1b_male_system.webp', MB, [
    ('Ureter', wbox(198, 66, 295, 96, MB), True), ('Vas deferens', wbox(104, 152, 296, 184, MB), True),
    ('Epididymis', wbox(122, 347, 293, 378, MB), True), ('Vasa efferentia', wbox(72, 404, 296, 436, MB), True),
    ('Rete testis', wbox(138, 450, 296, 481, MB), True), ('Testicular lobules', wbox(24, 524, 294, 556, MB), True),
    ('Urinary bladder', wbox(788, 66, 904, 134, MB), True), ('Seminal vesicle', wbox(792, 170, 915, 229, MB), True),
    ('Prostate', wbox(792, 238, 917, 269, MB), True), ('Bulbourethral gland', wbox(768, 282, 982, 347, MB), True),
    ('Urethra', wbox(776, 383, 893, 414, MB), True), ('Testis', wbox(788, 527, 877, 558, MB), True),
    ('Foreskin', wbox(646, 606, 778, 638, MB), True), ('Glans penis', wbox(378, 642, 558, 674, MB), True)])
d.occlusion('Figure 2.1a · Male pelvis (side view)', M + 'fig_2_1a_male_pelvis.webp', MA, [
    ('Ureter', wbox(160, 118, 258, 150, MA), True), ('Seminal vesicle', wbox(26, 168, 260, 200, MA), True),
    ('Urinary bladder', wbox(18, 230, 260, 262, MA), True), ('Vas deferens', wbox(64, 276, 260, 308, MA), True),
    ('Prostate', wbox(132, 322, 260, 354, MA), True), ('Penis', wbox(174, 370, 260, 402, MA), True),
    ('Urethra', wbox(140, 418, 262, 450, MA), True), ('Glans penis', wbox(78, 478, 262, 510, MA), True),
    ('Foreskin', wbox(122, 520, 258, 552, MA), True), ('Ejaculatory duct', wbox(708, 304, 966, 338, MA), True),
    ('Rectum', wbox(696, 396, 816, 428, MA), True), ('Anus', wbox(696, 438, 778, 470, MA), True),
    ('Testis', wbox(478, 526, 572, 558, MA), True), ('Scrotum', wbox(424, 560, 556, 592, MA), True),
    ('Bulbourethral gland', wbox(596, 552, 908, 586, MA), True)])

# ---------------------------------------------------------------- 2.2 Female
d.sec('2.2-female-reproductive-system')
d.basic('Parts of the female reproductive system?', 'Pair of ' + T('ovaries') + ', pair of ' + T('oviducts') + ', ' + T('uterus, cervix, vagina') + ', external genitalia (plus mammary glands)', **fig('fig_2_3a_female_pelvis'))
d.basic('Processes supported by the female reproductive system?', 'Ovulation, fertilisation, pregnancy, birth and child care')
d.basic('Primary female sex organs, and their products?', T('Ovaries') + ': the ' + T('ovum') + ' and several ' + T('steroid hormones') + ' (ovarian hormones)')
d.basic('Size of an ovary, and how is it held in place?', N('2–4 cm') + ' long; connected to the pelvic wall and uterus by ' + T('ligaments'))
d.basic('Structure of the ovary?', 'Covered by thin epithelium enclosing the ' + T('ovarian stroma') + ', divided into outer ' + T('cortex') + ' and inner ' + T('medulla'))
d.basic('Female accessory ducts?', T('Oviducts (fallopian tubes), uterus, vagina'))
d.basic('Length of each fallopian tube?', N('10–12 cm'))
d.cloze('Parts of the fallopian tube from ovary to uterus: {{c1::infundibulum}} (funnel with fimbriae) → {{c2::ampulla}} (wider) → {{c3::isthmus}} (narrow lumen, joins uterus).')
d.basic('Function of fimbriae?', 'Finger-like projections of the infundibulum that ' + T('collect the ovum') + ' after ovulation')
d.basic('Other name and shape of the uterus?', T('Womb') + '; shaped like an ' + T('inverted pear'))
d.basic('What is the birth canal?', T('Cervical canal') + ' + ' + T('vagina'))
d.cloze('Uterine wall, outside to inside: {{c1::perimetrium}} (thin membrane) → {{c2::myometrium}} (thick smooth muscle) → {{c3::endometrium}} (glandular).')
d.basic('Which uterine layer changes cyclically, and which contracts in delivery?', T('Endometrium') + ': cyclical changes in menstrual cycle. ' + T('Myometrium') + ': strong contractions in delivery.')
d.occlusion('Figure 2.3b · Female reproductive system', M + 'fig_2_3b_female_system.webp', FB, [
    ('Uterine fundus', wbox(278, 46, 440, 74, FB), True), ('Uterine cavity', wbox(88, 76, 236, 104, FB), True),
    ('Isthmus', wbox(686, 98, 776, 126, FB), True), ('Ampulla', wbox(686, 162, 778, 190, FB), True),
    ('Infundibulum', wbox(686, 214, 834, 242, FB), True), ('Fallopian tube', wbox(852, 150, 952, 204, FB), True),
    ('Endometrium', wbox(84, 264, 232, 292, FB), True), ('Myometrium', wbox(96, 294, 232, 322, FB), True),
    ('Perimetrium', wbox(96, 328, 232, 356, FB), True), ('Ovary', wbox(518, 266, 582, 294, FB), True),
    ('Fimbriae', wbox(648, 310, 744, 338, FB), True), ('Cervix', wbox(496, 364, 566, 392, FB), True),
    ('Cervical canal', wbox(492, 408, 644, 436, FB), True), ('Vagina', wbox(492, 464, 566, 492, FB), True)])
d.basic('Female external genitalia?', T('Mons pubis, labia majora, labia minora, hymen, clitoris'))
d.basic('What is the mons pubis?', 'Cushion of ' + T('fatty tissue') + ' covered by skin and pubic hair')
d.basic('Labia majora vs labia minora?', T('Majora') + ': fleshy folds from the mons pubis surrounding the vaginal opening<br>' + T('Minora') + ': paired folds under the labia majora')
d.basic('What is the hymen?', 'Membrane often ' + T('partially covering') + ' the vaginal opening')
d.basic('What is the clitoris, and where is it?', 'Tiny finger-like structure at the upper junction of the two labia minora, ' + T('above the urethral opening'))
d.basic('Is the hymen a reliable indicator of virginity?', X('No') + '. It can tear from a fall, tampon, sports (cycling, horse riding) or may persist after coitus')
d.basic('Identify these labels: Figure 2.3a.', 'Female pelvis (side view): uterus, urinary bladder, pubic symphysis, urethra, clitoris, labia, vaginal orifice, cervix, rectum, vagina, anus', **img('fig_2_3a_female_pelvis'))

d.basic('Mammary glands are characteristic of?', 'All ' + T('female mammals') + ' (functional mammary gland)')
d.basic('Number of mammary lobes per breast?', N('15–20') + ' lobes containing clusters of cells called ' + T('alveoli'))
d.cloze('Milk path: {{c1::alveoli}} → {{c2::mammary tubules}} → {{c3::mammary duct}} → {{c4::mammary ampulla}} → {{c5::lactiferous duct}} → nipple.')
d.occlusion('Figure 2.4 · Mammary gland', M + 'fig_2_4_mammary_gland.webp', MG, [
    ('Mammary lobe', wbox(274, 46, 456, 74, MG), True), ('Mammary alveolus', wbox(188, 96, 420, 124, MG), True),
    ('Mammary duct', wbox(180, 164, 370, 192, MG), True), ('Ampulla', wbox(226, 214, 332, 242, MG), True),
    ('Lactiferous duct', wbox(98, 264, 298, 292, MG), True), ('Nipple', wbox(198, 414, 278, 442, MG), True),
    ('Areola', wbox(232, 474, 312, 502, MG), True), ('Fat', wbox(590, 12, 632, 38, MG), True),
    ('Rib', wbox(782, 216, 824, 244, MG), True), ('Muscles between ribs', wbox(776, 268, 934, 324, MG), True),
    ('Pectoralis major muscle', wbox(784, 448, 954, 504, MG), True)])

# ---------------------------------------------------------------- 2.3 Gametogenesis
d.sec('2.3-gametogenesis')
d.basic('What is gametogenesis?', 'Production of gametes (' + T('sperms, ovum') + ') by the primary sex organs')
d.basic('When does spermatogenesis begin?', 'At ' + T('puberty'))
d.basic('How do spermatogonia increase in number?', 'By ' + T('mitotic') + ' division on the inside wall of seminiferous tubules')
d.basic('Chromosome number of a spermatogonium?', T('Diploid') + ', ' + N('46'))
d.basic('What are primary spermatocytes?', 'Spermatogonia that periodically undergo ' + T('meiosis') + ' (2n = 46)')
d.basic('Result of meiosis I in a primary spermatocyte?', N('Two') + ' equal haploid ' + T('secondary spermatocytes') + ' (' + N('23') + ' chromosomes each)')
d.basic('Result of meiosis II in secondary spermatocytes?', N('Four') + ' equal haploid ' + T('spermatids') + ' (' + N('23') + ' chromosomes)', **fig('fig_2_5_spermatogenesis_tubule'))
d.basic('What is spermiogenesis?', 'Transformation of ' + T('spermatids into spermatozoa'))
d.basic('What is spermiation?', 'Release of sperms from the ' + T('seminiferous tubules') + ' (after heads are embedded in Sertoli cells)')
d.basic('Spermiogenesis vs spermiation? (mnemonic)', 'Spermio-' + T('GENESIS') + ' = making the sperm shape. Spermi-' + T('ATION') + ' = sperm leaves (like "evacuation").')
d.basic('Why does spermatogenesis start at puberty?', 'Significant increase in ' + T('GnRH') + ' secretion by the hypothalamus')
d.basic('Role of LH in males?', 'Acts on ' + T('Leydig cells') + ' → androgen secretion → stimulates spermatogenesis')
d.basic('Role of FSH in males?', 'Acts on ' + T('Sertoli cells') + ' → secretes factors that help ' + T('spermiogenesis'))
d.basic('Hormones regulating spermatogenesis (Exercise 7)?', T('GnRH, LH, FSH, androgens'))
table_card(d, 'Exercise 16', 'True or false?', [
    ('Androgens are produced by Sertoli cells', 'False: by Leydig cells', True),
    ('Spermatozoa get nutrition from Sertoli cells', 'True', False),
    ('Leydig cells are found in the ovary', 'False: in the testis', True),
    ('Oogenesis takes place in corpus luteum', 'False: in the ovary (follicles)', True),
    ('Menstrual cycle ceases during pregnancy', 'True', False)], term='True/False: male and female cells')

d.cloze('A sperm has a {{c1::head}}, {{c2::neck}}, {{c3::middle piece}} and {{c4::tail}}, all enveloped by a plasma membrane.')
d.basic('What does the sperm head contain?', 'An elongated ' + T('haploid nucleus') + ', capped anteriorly by the ' + T('acrosome'))
d.basic('Function of the acrosome?', 'Filled with ' + T('enzymes') + ' that help fertilisation of the ovum')
d.basic('Function of the middle piece?', 'Numerous ' + T('mitochondria') + ' produce energy for tail movement (sperm motility)')
d.occlusion('Figure 2.6 · Structure of a sperm', M + 'fig_2_6_sperm.webp', SP, [
    ('Plasma membrane', wbox(368, 22, 550, 96, SP), True), ('Acrosome', wbox(368, 140, 532, 174, SP), True),
    ('Nucleus containing chromosomal material', wbox(366, 202, 744, 278, SP), True), ('Head', wbox(22, 222, 110, 258, SP), True),
    ('Neck', wbox(366, 364, 452, 398, SP), True), ('Middle piece', wbox(364, 446, 574, 482, SP), True),
    ('Mitochondria', wbox(364, 498, 588, 534, SP), True), ('Tail', wbox(366, 644, 432, 680, SP), True)])
d.basic('Sperms ejaculated per coitus?', N('200–300 million'))
d.basic('Criteria for normal fertility?', 'At least ' + N('60%') + ' sperms of normal shape and size, and at least ' + N('40%') + ' with vigorous motility')
d.basic('Secretions essential for sperm maturation and motility?', 'Of the ' + T('epididymis, vas deferens, seminal vesicle and prostate'))
d.basic('What is semen?', T('Seminal plasma + sperms'))
d.basic('What maintains the male accessory ducts and glands?', T('Androgens') + ' (testicular hormones)')

d.basic('What is oogenesis?', 'Formation of a mature female gamete')
d.basic('When is oogenesis initiated?', 'During ' + T('embryonic development') + ': a couple of million oogonia form in each fetal ovary')
d.basic('Are oogonia added after birth?', X('No'))
d.basic('What is a primary oocyte?', 'An oogonium that enters ' + T('prophase-I') + ' of meiosis and is ' + T('arrested') + ' there')
d.basic('What is a primary follicle?', 'A primary oocyte surrounded by a layer of ' + T('granulosa cells'))
d.basic('Primary follicles left in each ovary at puberty?', N('60,000–80,000') + ' (many degenerate from birth to puberty)')
d.basic('What is a secondary follicle?', 'Primary follicle with more layers of granulosa cells and a new ' + T('theca'))
d.basic('What characterises a tertiary follicle?', 'A fluid-filled cavity, the ' + T('antrum') + '; theca splits into ' + T('theca interna') + ' and ' + T('theca externa'))
d.basic('When does the primary oocyte complete meiosis I?', 'Inside the ' + T('tertiary follicle'))
d.basic('Products of meiosis I in oogenesis?', 'Unequal: a large haploid ' + T('secondary oocyte') + ' and a tiny ' + T('first polar body'))
d.basic('Advantage of unequal division in oogenesis? (think)', 'The secondary oocyte keeps the bulk of ' + T('nutrient-rich cytoplasm') + ' for the early embryo')
d.basic('New membrane formed around the secondary oocyte?', T('Zona pellucida'))
d.basic('What is ovulation?', 'Rupture of the ' + T('Graafian follicle') + ' releasing the ' + T('secondary oocyte') + ' (ovum)')
d.basic('At what stage is the "ovum" released in humans?', 'As a ' + T('secondary oocyte') + ' (arrested in meiosis II); meiosis II completes only after sperm entry')
d.occlusion('Figure 2.7 · Section of ovary', M + 'fig_2_7_ovary.webp', OV, [
    ('Blood vessels', wbox(78, 90, 194, 164, OV), True), ('Primary follicle', wbox(282, 40, 416, 112, OV), True),
    ('Tertiary follicle showing antrum', wbox(616, 30, 900, 106, OV), True), ('Graafian follicle', wbox(842, 120, 962, 194, OV), True),
    ('Secondary oocyte', wbox(768, 544, 924, 612, OV), True), ('Corpus luteum', wbox(316, 628, 444, 700, OV), True)])
d.basic('Follicle sequence (mnemonic)?', '"' + T('P-S-T-G') + '": Primary → Secondary → Tertiary → Graafian → (after ovulation) corpus luteum')
d.basic('Read the schematic: chromosome number at each stage (Figure 2.8)?', 'Spermatogonia/oogonia and primary cells: ' + N('46') + '; secondary cells, spermatids/ovum: ' + N('23'), **img('fig_2_8_gametogenesis'))
table_card(d, 'Compare', 'Spermatogenesis vs oogenesis', [
    ('Begins', 'Puberty vs embryonic life', False), ('Divisions', 'Equal vs unequal (polar bodies)', False),
    ('Products per mother cell', '4 sperms vs 1 ovum + polar bodies', False),
    ('Duration', 'Continues into old age vs stops at menopause', False)], term='Spermatogenesis vs oogenesis')
d.basic('Does the first polar body divide further?', 'NCERT: ' + X('not certain') + '. Update: in humans it often degenerates without dividing, though in some cases it divides.')

# ---------------------------------------------------------------- 2.4 Menstrual cycle
d.sec('2.4-menstrual-cycle')
d.basic('What is the menstrual cycle, and in which animals?', 'Reproductive cycle of ' + T('female primates') + ' (monkeys, apes, humans)')
d.basic('What is menarche?', 'The ' + T('first menstruation') + ', at puberty')
d.basic('Average length of the human menstrual cycle?', N('28/29 days'))
d.basic('How many ova are released per cycle, and when?', N('One') + ', in the ' + T('middle') + ' of the cycle')
d.basic('Duration and cause of the menstrual phase?', N('3–5 days') + '; breakdown of the ' + T('endometrial lining') + ' and its blood vessels')
d.basic('When does menstruation occur?', 'Only if the released ovum is ' + X('not fertilised'))
d.basic('Causes of missed menstruation?', T('Pregnancy') + '; also stress, poor health etc.')
d.basic('Events of the follicular (proliferative) phase?', 'Primary follicles grow into a ' + T('Graafian follicle') + '; endometrium ' + T('regenerates by proliferation'))
d.basic('Hormones during the follicular phase?', T('LH and FSH') + ' rise gradually; growing follicles secrete ' + T('estrogens'))
d.basic('When do LH and FSH peak?', 'Mid-cycle, about ' + N('14th day'))
d.basic('What is the LH surge and what does it do?', 'Rapid mid-cycle LH rise that ' + T('induces rupture of the Graafian follicle') + ' → ovulation')
d.basic('What happens in the luteal (secretory) phase?', 'Remains of the Graafian follicle become the ' + T('corpus luteum') + ', which secretes ' + T('progesterone'))
d.basic('Function of progesterone from the corpus luteum?', T('Maintains the endometrium') + ', needed for implantation and pregnancy')
d.basic('What happens to the corpus luteum without fertilisation?', 'It ' + T('degenerates') + ' → endometrium disintegrates → menstruation')
d.basic('What is menopause?', 'Cessation of menstrual cycles around ' + N('50 years'))
d.basic('Cyclic menstruation indicates?', 'Normal reproductive phase, between ' + T('menarche and menopause'))
d.basic('Read the chart (Figure 2.9): which hormone peaks in the luteal phase?', T('Progesterone') + ' (estrogen has a smaller second rise)', **img('fig_2_9_menstrual_cycle'))
table_card(d, 'Menstrual cycle', 'Days and key event?', [
    ('Menstrual phase', 'Days 1–5: endometrium sheds', False), ('Follicular phase', 'Days 5–13: follicle grows, estrogen rises', False),
    ('Ovulatory phase', 'Day 14: LH surge, ovulation', False), ('Luteal phase', 'Days 15–28: corpus luteum, progesterone', False)],
    term='Phases of the menstrual cycle')
d.basic('Mnemonic for the phase order?', '"' + T('My Friend Offers Lunch') + '": Menstrual, Follicular, Ovulatory, Luteal')
d.basic('Menstrual hygiene: how often to change pads?', 'Every ' + N('4–5 hours') + ' as required; dispose wrapped in paper, never in drains; wash hands with soap')

# ---------------------------------------------------------------- 2.5 Fertilisation
d.sec('2.5-fertilisation-implantation')
d.basic('What is insemination?', 'Release of semen by the penis into the ' + T('vagina') + ' during coitus')
d.basic('Where does fertilisation take place?', 'In the ' + T('ampullary region') + ' of the fallopian tube')
d.basic('Why doesn’t every copulation lead to pregnancy?', 'Ovum and sperm must reach the ampulla ' + T('simultaneously'))
d.basic('How does the ovum ensure only one sperm enters?', 'The sperm contacting the ' + T('zona pellucida') + ' induces membrane changes that ' + T('block additional sperms'), **fig('fig_2_10_ovum_sperms'))
d.basic('Identify the layers around the ovum (Figure 2.10).', T('Zona pellucida') + ', ' + T('corona radiata') + ' cells, ' + T('perivitelline space'), **img('fig_2_10_ovum_sperms'))
d.basic('Role of acrosome secretions in fertilisation?', 'Help the sperm enter the ovum cytoplasm through the zona pellucida and plasma membrane')
d.basic('What does sperm entry trigger in the secondary oocyte?', 'Completion of ' + T('meiosis II') + ' → second polar body + haploid ovum (' + T('ootid') + ')')
d.basic('Chromosome number of the zygote?', N('46') + ' (diploid)')
d.basic('Why is the baby’s sex decided by the father?', 'All ova carry ' + T('X') + '; ' + N('50%') + ' sperms carry X and 50% carry ' + T('Y') + '. XX → girl, XY → boy.')
d.basic('What is cleavage and where does it start?', T('Mitotic divisions') + ' of the zygote as it moves through the ' + T('isthmus') + ' towards the uterus')
d.basic('What are blastomeres?', 'The daughter cells (2, 4, 8, 16…) formed by cleavage')
d.basic('What is a morula?', 'Embryo with ' + N('8–16') + ' blastomeres')
d.basic('Two parts of a blastocyst?', 'Outer ' + T('trophoblast') + ' and ' + T('inner cell mass'))
d.basic('Fate of trophoblast and inner cell mass?', T('Trophoblast') + ': attaches to endometrium. ' + T('Inner cell mass') + ': differentiates into the embryo.')
d.basic('What is implantation?', 'Blastocyst becomes ' + T('embedded in the endometrium') + ' (uterine cells cover it); leads to pregnancy')
d.basic('Trace the journey: fertilisation to implantation (Figure 2.11).', 'Ovum → fertilised in ampulla → zygote → cleavage → morula → blastocyst → implantation in uterus', **img('fig_2_11_cleavage_implantation'))
d.basic('Correction: NCERT says "the embryo with 8 to 16 blastomeres is called a morula". Is 8–16 cells precise?', 'Exam answer: 8–16. Update: a morula usually has about ' + N('16–32') + ' cells; the 8–16 figure is a simplification.')

# ---------------------------------------------------------------- 2.6 Pregnancy
d.sec('2.6-pregnancy-embryonic-development')
d.basic('What are chorionic villi?', 'Finger-like projections of the ' + T('trophoblast') + ' after implantation, surrounded by uterine tissue and maternal blood')
d.basic('What is the placenta?', 'Structural and functional unit between embryo and mother formed by ' + T('chorionic villi + uterine tissue'), **fig('fig_2_12_foetus'))
d.basic('Functions of the placenta?', 'Supplies ' + T('O₂ and nutrients') + ', removes ' + T('CO₂ and wastes') + ', and acts as an ' + T('endocrine tissue'))
d.basic('What connects the placenta to the embryo?', 'The ' + T('umbilical cord'))
d.basic('Hormones produced by the placenta?', T('hCG, hPL, estrogens, progestogens'))
d.basic('Hormone secreted by the ovary late in pregnancy?', T('Relaxin'))
d.basic('Hormones produced only during pregnancy?', T('hCG, hPL and relaxin'))
d.basic('Hormones increased several-fold in maternal blood during pregnancy?', 'Estrogens, progestogens, ' + T('cortisol, prolactin, thyroxine'))
d.basic('Why do pregnancy tests detect hCG? (intuition)', 'hCG is made ' + T('only in pregnancy') + ' (by the placenta), so its presence in urine signals pregnancy')
d.cloze('After implantation the inner cell mass forms outer {{c1::ectoderm}} and inner {{c2::endoderm}}; {{c3::mesoderm}} appears between them.')
d.basic('What are stem cells of the inner cell mass?', 'Cells with potency to give rise to ' + T('all tissues and organs'))
table_card(d, 'Foetal milestones', 'What appears?', [
    ('End of month 1', 'Heart forms', False), ('End of month 2', 'Limbs and digits', False),
    ('End of 12 weeks (1st trimester)', 'Most major organ systems; limbs and external genitals well developed', False),
    ('Month 5', 'First movements, hair on head', False),
    ('End of 24 weeks (2nd trimester)', 'Fine body hair, eyelids separate, eyelashes', False)], term='Embryonic development by month')
d.basic('First sign of a growing foetus by stethoscope?', 'The ' + T('heart sound') + ' (heart forms after one month)')
d.basic('Identify labels in Figure 2.12.', 'Placental villi, umbilical cord with vessels, cavity of uterus, yolk sac, embryo, plug of mucus in cervix', **img('fig_2_12_foetus'))

# ---------------------------------------------------------------- 2.7 Parturition
d.sec('2.7-parturition-lactation')
d.basic('Gestation period in humans?', 'About ' + N('9 months'))
d.basic('What is parturition?', 'Delivery of the foetus (childbirth) by vigorous uterine contraction')
d.basic('What controls parturition?', 'A complex ' + T('neuroendocrine mechanism'))
d.basic('What is the foetal ejection reflex?', 'Mild uterine contractions triggered by signals from the ' + T('fully developed foetus and placenta'))
d.basic('Sequence of parturition?', '1) Foetal ejection reflex<br>2) ' + T('Oxytocin') + ' from maternal pituitary<br>3) Stronger contractions → more oxytocin<br>4) Expulsion of baby, then placenta')
d.basic('Why is parturition an example of positive feedback? (intuition)', 'Contraction ' + T('increases') + ' oxytocin, which increases contraction: the loop amplifies until birth')
d.basic('What do doctors inject to induce delivery?', T('Oxytocin'))
d.basic('Hormones involved in parturition (summary)?', T('Cortisol, estrogens and oxytocin'))
d.basic('What is lactation?', 'Milk production by mammary glands towards the ' + T('end of pregnancy') + '/after birth')
d.basic('What is colostrum and why is it important?', 'Milk of the first few days; contains ' + T('antibodies (IgA)') + ' that give the newborn resistance')

# ---------------------------------------------------------------- Summary / exercises
d.sec('summary')
table_card(d, 'Exercise 1', 'Fill the blank', [
    ('Release of ovum from mature follicle', 'Ovulation', False), ('Ovulation is induced by', 'LH', False),
    ('Fertilisation takes place in', 'Ampulla of fallopian tube', False), ('Zygote divides to form (implanted)', 'Blastocyst', False),
    ('Vascular connection between foetus and uterus', 'Placenta', False)], term='Fill in the blanks (Exercise 1)')
table_card(d, 'Exercise 15', 'Function?', [
    ('Corpus luteum', 'Secretes progesterone', False), ('Endometrium', 'Site of implantation', False),
    ('Acrosome', 'Enzymes for sperm entry', False), ('Sperm tail', 'Motility', False), ('Fimbriae', 'Collect ovum', False)],
    term='Functions (Exercise 15)')
d.basic('Mother gave birth to identical twins: how many eggs released? Fraternal twins? (Exercise 20)', 'Identical: ' + N('one') + ' egg (the embryo splits). Fraternal: ' + N('two') + ' eggs.')
d.basic('A female dog gave birth to 6 puppies. Minimum eggs released? (Exercise 21)', N('Six') + ' (dogs are multiovulatory)')
d.basic('Two functions each of testis and ovary? (Exercise 4)', T('Testis') + ': sperms, androgens. ' + T('Ovary') + ': ovum, estrogen and progesterone.')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
