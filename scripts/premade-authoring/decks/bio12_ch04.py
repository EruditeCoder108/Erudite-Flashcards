import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch04-principles-of-inheritance-and-variation')
d = Deck('Chapter 4: Principles of Inheritance and Variation', 'Class 12', ['class-12', 'biology', 'ch-4'])
d.description = 'Mendel’s laws, incomplete and co-dominance, linkage, polygenic traits, pleiotropy, sex determination, mutation and genetic disorders'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
PS = (626, 1001)

# ---------------------------------------------------------------- intro
d.sec('4.0-intro')
d.basic('What is genetics?', 'Branch of biology dealing with ' + T('inheritance') + ' and ' + T('variation') + ' of characters from parents to offspring')
d.basic('Define inheritance.', 'Process by which characters are passed on from parent to progeny; the basis of ' + T('heredity'))
d.basic('Define variation.', 'The degree by which ' + T('progeny differ') + ' from their parents')
d.basic('Since when did humans know variation was hidden in sexual reproduction?', 'As early as ' + N('8000–1000 B.C.'))
d.basic('Example of an Indian breed made by artificial selection?', E('Sahiwal') + ' cows in Punjab')

# ---------------------------------------------------------------- 4.1 Mendel
d.sec('4.1-mendels-laws')
d.basic('Mendel’s experiments: organism and period?', 'Garden pea; ' + N('seven years') + ' (' + N('1856–1863') + ')')
d.basic('Why was Mendel’s work a first in biology?', 'First to apply ' + T('statistical analysis and mathematical logic') + ' to biological problems')
d.basic('Why were Mendel’s data credible?', T('Large sampling size') + ' and confirmation over ' + T('successive generations'))
d.basic('What is a true-breeding line?', 'A line that, after continuous ' + T('self-pollination') + ', shows stable trait inheritance and expression for several generations')
d.basic('How many true-breeding pea varieties did Mendel select?', N('14') + ' (as ' + N('7') + ' pairs differing in one character)')
table_card(d, 'Table 4.1', 'Dominant / recessive?', [
    ('Stem height', 'Tall / dwarf', False), ('Flower colour', 'Violet / white', False),
    ('Flower position', 'Axial / terminal', False), ('Pod shape', 'Inflated / constricted', False),
    ('Pod colour', 'Green / yellow', False), ('Seed shape', 'Round / wrinkled', False),
    ('Seed colour', 'Yellow / green', False)], term='Seven pairs of contrasting traits (Table 4.1)')
d.basic('Identify: seven pairs of traits Mendel studied.', 'Figure 4.1: seed shape, seed colour, flower colour, pod shape, pod colour, flower position, stem height', **img('fig_4_1_seven_traits'))
d.basic('Mnemonic for the 7 pea characters?', '"' + T('Short Silly Flowers Fly Past Poor Seeds') + '":<br>Stem height, Seed shape, Flower colour, Flower position, Pod shape, Pod colour, Seed colour')
d.basic('Pod colour trap: which is dominant?', T('Green') + ' pod is dominant over yellow (opposite of seed colour, where ' + T('yellow') + ' is dominant)')
d.basic('Advantages of pea for Mendel’s experiments? (Exercise 1)', 'Many ' + T('contrasting traits') + '<br>Naturally ' + T('self-pollinating') + '<br>Easy to cross-pollinate artificially<br>Short life cycle<br>Many seeds')
d.basic('Steps in making a cross in pea (Figure 4.2)?', '1) Remove anthers (' + T('emasculation') + ') from the female parent<br>2) Transfer pollen from the male parent (pollination)<br>3) Seeds<br>4) Progeny', **fig('fig_4_2_making_cross'))

# ---------------------------------------------------------------- 4.2 One gene
d.sec('4.2-inheritance-of-one-gene')
d.basic('Tall × dwarf pea: F₁ result?', 'All ' + T('tall') + '; none dwarf', **fig('fig_4_3_monohybrid'))
d.basic('F₁ self-pollinated: F₂ result?', N('3/4') + ' tall, ' + N('1/4') + ' dwarf; no blending (no in-between heights)')
d.basic('What did Mendel call the units passed on through gametes?', T('Factors') + '; now called ' + T('genes'))
d.basic('What are genes?', 'The ' + T('units of inheritance') + '; contain information to express a trait')
d.basic('What are alleles?', 'Genes coding for a pair of contrasting traits: ' + T('slightly different forms of the same gene'))
d.basic('Symbol convention for alleles?', 'Capital letter for the trait expressed in F₁ (' + T('T') + '), small letter for the other (' + T('t') + '). ' + X('Never') + ' T and d.')
d.basic('Homozygous vs heterozygous?', T('Homozygous') + ': identical alleles (TT, tt). ' + T('Heterozygous') + ': dissimilar alleles (Tt).')
d.basic('Genotype vs phenotype?', T('Genotype') + ': genetic make-up (TT, Tt, tt). ' + T('Phenotype') + ': observable trait (tall, dwarf).')
d.basic('Dominant vs recessive factor?', 'In a dissimilar pair, the ' + T('dominant') + ' is expressed; the ' + T('recessive') + ' is masked (expressed only when homozygous)')
d.basic('What is a monohybrid cross?', 'A cross studying ' + T('one character') + ' (e.g. TT × tt); Tt is a monohybrid')
d.basic('How do alleles behave in gamete formation?', 'They ' + T('segregate') + ' randomly; each gamete gets ' + T('one') + ' allele (50% chance each)')
d.basic('Who developed the Punnett square, and what is it?', T('Reginald C. Punnett') + '; a graphical way to calculate probability of all possible genotypes in a cross', **fig('fig_4_4_punnett_monohybrid'))
d.cloze('Monohybrid F₂: phenotypic ratio {{c1::3 : 1}}; genotypic ratio {{c2::1 : 2 : 1}} (TT : Tt : tt).')
d.basic('Binomial form of the monohybrid F₂?', '\\( (\\tfrac12 T + \\tfrac12 t)^2 = \\tfrac14 TT + \\tfrac12 Tt + \\tfrac14 tt \\)')
d.basic('Why can’t you tell TT from Tt by looking? (intuition)', 'One working allele (T) is enough to make the plant tall: ' + T('dominance') + ' hides the recessive')
d.basic('Result of selfing dwarf F₂ plants?', 'Dwarfs in F₃ and F₄: dwarfs are homozygous ' + T('tt'))
d.basic('Self-pollinating a tall F₂ plant would give?', '1/3 of tall F₂ (TT) breed ' + T('true') + '; 2/3 (Tt) give ' + T('3 tall : 1 dwarf'))
d.basic('What is a test cross?', 'Crossing a ' + T('dominant phenotype') + ' (unknown genotype) with the ' + T('recessive parent'), **fig('fig_4_5_test_cross'))
d.basic('Test cross results and meaning?', 'All dominant → unknown is ' + T('homozygous') + '. ' + N('1 : 1') + ' → unknown is ' + T('heterozygous') + '.')
d.basic('Read Figure 4.5: violet flower × ww gives half violet, half white. Genotype?', T('Ww') + ' (heterozygous)', **img('fig_4_5_test_cross'))

d.sec('4.2.1-law-of-dominance')
d.cloze('Law of Dominance: (i) characters are controlled by discrete units called {{c1::factors}}; (ii) factors occur in {{c2::pairs}}; (iii) in a dissimilar pair one member {{c3::dominates}} the other.')
d.basic('What does the law of dominance explain?', 'Only one parental character in F₁, both in F₂, and the ' + N('3:1') + ' F₂ ratio')
d.sec('4.2.2-law-of-segregation')
d.basic('State the law of segregation.', 'Alleles of a pair ' + T('segregate') + ' during gamete formation so each gamete receives only ' + T('one') + ' factor')
d.basic('Why is it called the law of "purity of gametes"?', 'Alleles ' + X('never blend') + '; each gamete is pure for one allele')
d.basic('Gametes from homozygous vs heterozygous parent?', T('Homozygous') + ': all similar. ' + T('Heterozygous') + ': two kinds in equal proportion.')

d.sec('4.2.2.1-incomplete-dominance')
d.basic('What is incomplete dominance?', 'F₁ phenotype is ' + T('in between') + ' the two parents')
d.basic('Example of incomplete dominance?', 'Flower colour in dog flower (' + T('snapdragon') + ', ' + EI('Antirrhinum') + ')', **fig('fig_4_6_snapdragon'))
d.basic('Snapdragon RR × rr: F₁ and F₂?', 'F₁ all ' + T('pink (Rr)') + '. F₂ ' + N('1 red : 2 pink : 1 white') + '.')
d.basic('Why is incomplete dominance special in ratios?', 'Phenotypic ratio = genotypic ratio = ' + N('1:2:1'))
d.basic('Molecular view: three possible products of a modified allele?', '(i) normal or less efficient enzyme, (ii) ' + T('non-functional') + ' enzyme, (iii) ' + T('no enzyme'))
d.basic('Why is the modified allele usually recessive?', 'It makes a non-functional or no enzyme.<br>The phenotype then depends on the ' + T('unmodified (functioning) allele') + ', which is dominant')
d.basic('When is a modified allele "equivalent"?', 'When it still makes a normal/less efficient enzyme: same phenotype (very common)')

d.sec('4.2.2.2-co-dominance')
d.basic('What is co-dominance?', 'F₁ ' + T('resembles both parents') + ': both alleles are expressed')
d.basic('Example of co-dominance?', T('ABO blood groups') + ': alleles Iᴬ and Iᴮ both express in AB')
d.basic('What does the gene I control?', 'The kind of ' + T('sugar polymer') + ' protruding from the RBC plasma membrane')
d.basic('Alleles of gene I and their products?', T('Iᴬ') + ' and ' + T('Iᴮ') + ': slightly different sugars. ' + T('i') + ': ' + X('no sugar') + '.')
d.basic('Dominance relations among ABO alleles?', 'Iᴬ and Iᴮ are ' + T('completely dominant') + ' over i; Iᴬ and Iᴮ are ' + T('co-dominant'))
table_card(d, 'Table 4.2', 'Blood group?', [
    ('IᴬIᴬ, Iᴬi', 'A', False), ('IᴮIᴮ, Iᴮi', 'B', False), ('IᴬIᴮ', 'AB', False), ('ii', 'O', False)],
    term='ABO genotypes and blood groups')
d.basic('How many ABO genotypes and phenotypes?', N('6') + ' genotypes, ' + N('4') + ' phenotypes')
d.basic('What are multiple alleles?', 'More than two alleles governing the same character (e.g. Iᴬ, Iᴮ, i)')
d.basic('Why can multiple alleles be found only in population studies?', 'An individual (diploid) carries only ' + N('two') + ' alleles')
d.basic('Child O; father A; mother B. Genotypes? (Exercise 12)', 'Father ' + T('Iᴬi') + ', mother ' + T('Iᴮi') + '. Other children: IᴬIᴮ (AB), Iᴬi (A), Iᴮi (B), ii (O).')
d.basic('Starch synthesis in pea: BB, Bb, bb seeds?', T('BB') + ': large starch grains, round. ' + T('bb') + ': small grains, wrinkled. ' + T('Bb') + ': round seeds but intermediate grains.')
d.basic('What does the pea starch gene show about dominance?', 'Seed shape: B is ' + T('dominant') + '. Starch grain size: ' + T('incomplete dominance') + '. Dominance depends on the phenotype chosen.')
d.basic('Is dominance an autonomous feature of a gene?', X('No') + '. It depends on the gene product and on the particular phenotype examined')

# ---------------------------------------------------------------- 4.3 Two genes
d.sec('4.3-inheritance-of-two-genes')
d.basic('Dihybrid cross: parents and F₁ in Mendel’s example?', 'RRYY (round yellow) × rryy (wrinkled green) → F₁ ' + T('RrYy') + ' (round yellow)', **fig('fig_4_7_dihybrid'))
d.basic('Dominant traits in the dihybrid cross?', T('Yellow') + ' over green, ' + T('round') + ' over wrinkled')
d.cloze('Dihybrid F₂ phenotypic ratio: {{c1::9}} round yellow : {{c2::3}} wrinkled yellow : {{c2::3}} round green : {{c3::1}} wrinkled green.')
d.basic('How is 9:3:3:1 derived?', '\\( (3:1) \\times (3:1) \\): (3 round : 1 wrinkled)(3 yellow : 1 green)')
d.sec('4.3.1-independent-assortment')
d.basic('State the law of independent assortment.', 'When two pairs of traits combine in a hybrid, ' + T('segregation of one pair is independent') + ' of the other pair')
d.basic('Gametes from RrYy and their frequency?', T('RY, Ry, rY, ry') + ', each ' + N('1/4'))
d.basic('Dihybrid F₂: number of genotypes and phenotypes?', N('9') + ' genotypes, ' + N('4') + ' phenotypes (in ' + N('16') + ' squares)')
d.basic('Dihybrid F₂ genotypic ratio?', N('1:2:1:2:4:2:1:2:1') + ' (not 9:3:3:1)')
d.basic('Types of gametes from an organism heterozygous at 4 loci? (Exercise 3)', '\\( 2^n = 2^4 = \\) ' + N('16'))
steps_card(d, 'Exercise 7', 'TtYy × Ttyy: fraction tall and green?', 'Treat each gene separately, then multiply.',
           ['Tt × Tt → 3/4 tall, 1/4 dwarf', 'Yy × yy → 1/2 yellow, 1/2 green', 'Tall and green = 3/4 × 1/2 = <b>3/8</b>', 'Dwarf and green = 1/4 × 1/2 = <b>1/8</b>'],
           2, 'TtYy × Ttyy: tall and green?', 'Tall green 3/8; dwarf green 1/8')
d.basic('Dihybrid test cross (RrYy × rryy) ratio?', N('1 : 1 : 1 : 1'))

d.sec('4.3.2-chromosomal-theory')
d.basic('When did Mendel publish, and when was it recognised?', 'Published ' + N('1865') + '; unrecognised till ' + N('1900'))
d.basic('Reasons Mendel’s work was ignored?', 'Poor communication; ' + T('discrete non-blending factors') + ' vs apparent continuous variation; maths in biology unacceptable; ' + X('no physical proof') + ' of factors')
d.basic('Who rediscovered Mendel’s work in 1900?', T('de Vries, Correns and von Tschermak') + ' (independently)')
d.basic('By when was chromosome movement in meiosis worked out?', N('1902'))
d.basic('Who noted chromosome behaviour parallels gene behaviour?', T('Walter Sutton and Theodore Boveri'), **fig('fig_4_8_meiosis_germ_cells'))
d.basic('Who proposed the chromosomal theory of inheritance? (Exercise 15)', T('Sutton') + ' (with Boveri): united chromosomal segregation with Mendelian principles')
table_card(d, 'Table 4.3', 'Genes and chromosomes both…', [
    ('Pairs', 'Occur in pairs', False), ('Gamete formation', 'Segregate; one of each pair to a gamete', False),
    ('Two pairs', 'Segregate independently of each other', False)], term='Parallel behaviour of genes and chromosomes')
d.basic('Where are the two alleles of a gene located?', 'At ' + T('homologous sites') + ' on homologous chromosomes')
d.basic('How do chromosomes explain independent assortment?', 'In meiosis I, two chromosome pairs align at the metaphase plate ' + T('independently') + ' (Possibility I or II)', **fig('fig_4_9_independent_assortment'))
d.basic('Who experimentally verified the chromosomal theory?', T('Thomas Hunt Morgan') + ' and colleagues')
d.basic('Why was Drosophila ideal for genetics?', 'Grown on simple synthetic medium; life cycle ~' + N('2 weeks') + '; many progeny per mating; sexes easy to tell apart; many visible hereditary variations', **fig('fig_4_10_drosophila'))

d.sec('4.3.3-linkage-recombination')
d.basic('Morgan’s dihybrid cross in Drosophila?', 'Yellow-bodied white-eyed females × brown-bodied red-eyed males; F₂ ' + X('deviated') + ' from 9:3:3:1')
d.basic('Where were these genes located?', 'On the ' + T('X chromosome'))
d.basic('Define linkage.', 'Physical association of genes on a ' + T('chromosome') + ' (term coined by Morgan)')
d.basic('Define recombination.', 'Generation of ' + T('non-parental gene combinations'))
d.basic('When two genes are on the same chromosome, which combinations dominate?', T('Parental') + ' combinations are much higher than non-parental', **fig('fig_4_11_linkage'))
d.cloze('White and yellow genes: {{c1::1.3}}% recombination (tightly linked); white and miniature wing: {{c2::37.2}}% (loosely linked).')
d.basic('Tight vs loose linkage?', T('Tight') + ': genes close, very low recombination. ' + T('Loose') + ': genes far apart, higher recombination.')
d.basic('Who made the first genetic map, and how?', T('Alfred Sturtevant') + ' (Morgan’s student): used ' + T('recombination frequency') + ' as a measure of gene distance')
d.basic('Why does recombination frequency measure distance? (intuition)', 'Crossing over can happen anywhere.<br>The farther apart two genes are, the more likely a crossover falls ' + T('between') + ' them')
d.basic('Use of genetic maps today?', 'Starting point for ' + T('whole-genome sequencing') + ' (e.g. Human Genome Project)')
d.basic('Morgan’s contribution to genetics? (Exercise 9)', 'Verified chromosomal theory; discovered ' + T('linkage, recombination') + ' and sex-linked inheritance in Drosophila')
d.basic('Two heterozygous parents, loci completely linked: F₁ ratio? (Exercise 8)', 'Like a monohybrid: ' + N('3 : 1') + ' (only parental combinations; with some recombination, parental types exceed recombinants)')

# ---------------------------------------------------------------- 4.4-4.5
d.sec('4.4-polygenic-inheritance')
d.basic('What are polygenic traits?', 'Traits controlled by ' + T('three or more genes') + ', spread across a gradient; also influenced by ' + T('environment'))
d.basic('Examples of polygenic traits?', E('Human height') + ', ' + E('human skin colour'))
d.basic('How do alleles act in a polygenic trait?', 'Each allele’s effect is ' + T('additive'))
d.basic('Skin colour model with A, B, C: darkest and lightest?', T('AABBCC') + ' darkest; ' + T('aabbcc') + ' lightest; three dominant + three recessive = intermediate')
d.sec('4.5-pleiotropy')
d.basic('What is a pleiotropic gene?', 'A single gene with ' + T('multiple phenotypic expressions'))
d.basic('Usual mechanism of pleiotropy?', 'The gene affects a ' + T('metabolic pathway') + ' contributing to different phenotypes')
d.basic('Example of pleiotropy?', T('Phenylketonuria') + ':<br>mutation in phenylalanine hydroxylase gene → mental retardation + reduced hair and skin pigmentation')
d.basic('Polygenic vs pleiotropy? (mnemonic)', T('Poly-genic') + ' = many genes → one trait. ' + T('Pleio-tropy') + ' = one gene → many traits.')

# ---------------------------------------------------------------- 4.6 Sex determination
d.sec('4.6-sex-determination')
d.basic('Who first saw the "X body", and in what?', T('Henking') + ' (' + N('1891') + '), during spermatogenesis in insects; 50% sperms received it')
d.basic('What was Henking’s X body?', 'The ' + T('X chromosome'))
d.basic('Sex chromosomes vs autosomes?', T('Sex chromosomes') + ': differ between sexes and determine sex. ' + T('Autosomes') + ': all the rest.')
d.basic('XO type: example and male/female?', E('Grasshopper') + ': male XO (one X), female XX. Males have ' + X('one fewer') + ' chromosome.')
d.basic('XY type: examples?', E('Humans, Drosophila') + ', many insects and mammals; male XY, female XX', **fig('fig_4_12_sex_determination'))
d.basic('What is male heterogamety?', 'Males produce two kinds of gametes (X/O or X/Y): XO and XY types')
d.basic('ZW type: example and heterogametic sex?', E('Birds') + ': female ' + T('ZW') + ' (heterogametic), male ' + T('ZZ'))
d.basic('In birds, who decides the chick’s sex?', 'The ' + T('egg') + ' (female makes Z or W eggs)')
table_card(d, 'Sex determination', 'Male / female?', [
    ('XO (grasshopper)', 'XO / XX', False), ('XY (humans, Drosophila)', 'XY / XX', False),
    ('ZW (birds)', 'ZZ / ZW', False), ('Haplodiploid (honey bee)', 'n (16) / 2n (32)', False)], term='Types of sex determination')
d.sec('4.6.1-humans')
d.basic('Human chromosome complement?', N('23') + ' pairs: ' + N('22') + ' pairs autosomes + XX (female) or XY (male)')
d.basic('Why does the father determine the baby’s sex?', '50% sperms carry ' + T('X') + ', 50% carry ' + T('Y') + '; all ova carry X')
d.basic('Probability of a boy in each pregnancy?', N('50%'))
d.sec('4.6.2-honey-bee')
d.basic('Basis of sex determination in honey bee?', 'Number of ' + T('sets of chromosomes') + ' (haplodiploidy)', **fig('fig_4_13_honey_bee'))
d.basic('Honey bee: fertilised vs unfertilised egg?', T('Fertilised') + ' → female (queen or worker), ' + N('32') + ' chromosomes. ' + T('Unfertilised') + ' → male (drone) by parthenogenesis, ' + N('16') + '.')
d.basic('How do drones make sperms?', 'By ' + T('mitosis') + ' (they are already haploid)')
d.basic('Family quirks of a drone?', X('No father') + ', cannot have sons; but has a ' + T('grandfather') + ' and can have ' + T('grandsons'))

# ---------------------------------------------------------------- 4.7 Mutation
d.sec('4.7-mutation')
d.basic('Define mutation.', 'Alteration of ' + T('DNA sequence') + ' changing genotype and phenotype')
d.basic('Two sources of variation in DNA?', T('Recombination') + ' and ' + T('mutation'))
d.basic('How do deletions/insertions cause chromosomal aberrations?', 'One DNA helix runs through each chromatid; losing or gaining a segment alters the chromosome')
d.basic('Where are chromosomal aberrations commonly seen?', 'In ' + T('cancer cells'))
d.basic('What is a point mutation? Example? (Exercise 14)', 'Change in a ' + T('single base pair') + '; e.g. ' + E('sickle-cell anaemia'))
d.basic('What causes frame-shift mutations?', T('Deletion or insertion') + ' of base pairs')
d.basic('What are mutagens? Example?', 'Chemical and physical factors inducing mutation; e.g. ' + E('UV radiation'))

# ---------------------------------------------------------------- 4.8 Genetic disorders
d.sec('4.8.1-pedigree-analysis')
d.basic('What is pedigree analysis?', 'Analysis of a trait over several generations of a family, drawn as a ' + T('family tree'))
d.basic('Why is pedigree analysis needed in humans? (Exercise 10)', 'Controlled crosses are ' + X('not possible') + ' in humans; it traces inheritance of a trait, abnormality or disease')
d.occlusion('Figure 4.13 · Pedigree symbols', M + 'fig_4_13_pedigree_symbols.webp', PS, [
    ('Male', wbox(214, 44, 284, 74, PS), True), ('Female', wbox(214, 124, 308, 156, PS), True),
    ('Sex unspecified', wbox(214, 210, 432, 244, PS), True), ('Affected individuals', wbox(214, 292, 490, 326, PS), True),
    ('Mating', wbox(214, 368, 316, 402, PS), True), ('Consanguineous mating (between relatives)', wbox(214, 442, 568, 508, PS), True),
    ('Parents above, children below (birth order left to right)', wbox(214, 558, 624, 656, PS), True),
    ('Parents with male child affected', wbox(214, 752, 548, 818, PS), True), ('Five unaffected offspring', wbox(214, 934, 556, 970, PS), True)])
d.basic('Correction: NCERT labels both the honey bee figure and the pedigree symbols as "Figure 4.13". Note?', 'A numbering slip: the pedigree symbols figure should be ' + T('4.14') + ' (and the next ones shift by one)')

d.sec('4.8.2-mendelian-disorders')
d.basic('Two categories of genetic disorders?', T('Mendelian') + ' (single gene) and ' + T('chromosomal'))
d.basic('Common Mendelian disorders?', 'Haemophilia, cystic fibrosis, sickle-cell anaemia, colour blindness, phenylketonuria, thalassemia')
d.basic('Identify the traits in these pedigrees (Figure 4.14).', '(a) ' + T('Autosomal dominant') + ' (e.g. myotonic dystrophy); (b) ' + T('autosomal recessive') + ' (e.g. sickle-cell anaemia)', **img('fig_4_14_pedigrees'))
d.basic('Pedigree clue for autosomal recessive? (intuition)', 'Affected child from ' + T('two unaffected parents') + ' (both carriers); often skips generations')
d.basic('Pedigree clue for X-linked recessive?', 'Mostly ' + T('males affected') + ', passed via carrier mothers; never father to son')
table_card(d, 'Mendelian disorders', 'Inheritance?', [
    ('Colour blindness', 'X-linked recessive', False), ('Haemophilia', 'X-linked recessive', False),
    ('Sickle-cell anaemia', 'Autosomal recessive', False), ('Phenylketonuria', 'Autosomal recessive', False),
    ('Thalassemia', 'Autosomal recessive', False), ('Myotonic dystrophy', 'Autosomal dominant', False)], term='Mode of inheritance of disorders')
d.basic('Cause of colour blindness?', 'Defect in ' + T('red or green cone') + ' due to mutation in genes on the ' + T('X chromosome') + '; cannot distinguish red and green')
d.basic('Incidence of colour blindness?', 'About ' + N('8%') + ' of males, ' + N('0.4%') + ' of females')
d.basic('Why is colour blindness commoner in males?', 'Males have only ' + T('one X') + '; one recessive allele is enough')
d.basic('Son of a carrier mother: chance of colour blindness?', N('50%'))
d.basic('When can a daughter be colour blind?', 'Mother is at least a ' + T('carrier') + ' and father is ' + T('colour blind'))
d.basic('What goes wrong in haemophilia?', 'A single protein of the ' + T('blood-clotting cascade') + ' is affected: a simple cut causes non-stop bleeding')
d.basic('Why are haemophilic females extremely rare?', 'Mother must be at least a carrier and father ' + T('haemophilic') + ' (who rarely survives to later life)')
d.basic('Famous carrier of haemophilia?', T('Queen Victoria'))
d.basic('Genotypes in sickle-cell anaemia?', 'HbᴬHbᴬ normal; HbᴬHbˢ ' + T('carrier') + ' (sickle-cell trait); HbˢHbˢ ' + X('diseased'))
d.basic('Molecular defect in sickle-cell anaemia?', T('Glutamic acid → valine') + ' at the ' + N('6th') + ' position of the ' + T('β-globin') + ' chain', **fig('fig_4_15_sickle_cell'))
d.basic('Base change in sickle-cell anaemia?', 'Sixth codon ' + T('GAG → GUG') + ' (single base substitution)')
d.basic('Correction: NCERT gives "GAG to GUG" for the gene. Precise statement?', 'GUG is the ' + T('mRNA') + ' codon; in the DNA coding strand it is ' + T('GAG → GTG') + ' (A→T)')
d.basic('Why do RBCs sickle?', 'Mutant Hb ' + T('polymerises under low O₂ tension') + '; RBC changes from biconcave disc to sickle shape')
d.basic('Why is sickle-cell trait common in malaria areas? (beyond NCERT)', 'Carriers (HbᴬHbˢ) resist ' + T('malaria') + ': heterozygote advantage keeps the allele in the population')
d.basic('Defect in phenylketonuria?', 'Lacks the enzyme converting ' + T('phenylalanine → tyrosine') + '; phenylalanine → phenylpyruvic acid accumulates in brain → mental retardation; excreted in urine')
d.basic('Cause of thalassemia?', 'Mutation or deletion → ' + T('reduced synthesis') + ' of α or β globin chains → abnormal Hb → anaemia')
d.basic('α vs β thalassemia: genes and chromosome?', T('α') + ': HBA1 and HBA2 on chromosome ' + N('16') + ' (4 genes). ' + T('β') + ': HBB on chromosome ' + N('11') + '.')
d.basic('Severity rule in α thalassemia?', 'The ' + T('more genes affected') + ' (of four), the less α-globin made')
d.basic('Thalassemia vs sickle-cell anaemia?', T('Thalassemia') + ': quantitative (too few globin). ' + T('Sickle-cell') + ': qualitative (incorrectly functioning globin).')
d.basic('Two autosomal disorders with symptoms? (Exercise 16)', T('Sickle-cell anaemia') + ': sickled RBCs, anaemia. ' + T('Phenylketonuria') + ': mental retardation, light pigmentation.')

d.sec('4.8.3-chromosomal-disorders')
d.basic('Cause of chromosomal disorders?', T('Absence, excess or abnormal arrangement') + ' of one or more chromosomes')
d.basic('What is aneuploidy, and its cause?', 'Gain or loss of chromosome(s), due to ' + T('failure of segregation of chromatids'))
d.basic('What is polyploidy, and its cause?', 'Increase in a ' + T('whole set') + ' of chromosomes, due to ' + T('failure of cytokinesis') + ' after telophase; common in plants')
d.basic('Trisomy vs monosomy?', T('Trisomy') + ': an extra copy of a chromosome (2n+1). ' + T('Monosomy') + ': one chromosome of a pair missing (2n−1).')
d.basic('Cause of Down’s syndrome?', T('Trisomy of chromosome 21') + ' (47 chromosomes)')
d.basic('Who first described Down’s syndrome?', T('Langdon Down') + ' (' + N('1866') + ')')
d.basic('Features of Down’s syndrome?', 'Short stature<br>Small round head<br>' + T('Furrowed tongue') + ', partially open mouth<br>Broad palm with ' + T('palm crease') + '<br>Retarded physical, psychomotor and mental development', **fig('fig_4_16_down_syndrome'))
d.basic('Karyotype of Klinefelter’s syndrome?', T('47, XXY'))
d.basic('Features of Klinefelter’s syndrome?', 'Masculine development with feminine traits (' + T('gynaecomastia') + '), tall; ' + X('sterile'))
d.basic('Karyotype of Turner’s syndrome?', T('45, XO'))
d.basic('Features of Turner’s syndrome?', X('Sterile') + ' female, ' + T('rudimentary ovaries') + ', short stature, lack of secondary sexual characters')
d.basic('Identify (a) and (b) in Figure 4.17.', '(a) ' + T('Klinefelter') + ' (tall, feminised). (b) ' + T('Turner') + ' (short, underdeveloped feminine character).', **img('fig_4_17_klinefelter_turner'))
d.basic('Mnemonic: Klinefelter vs Turner?', T('Klinefelter') + ' = e' + T('X') + 'tra X in a male (XXY). ' + T('Turner') + ' = a female who "turned" in one X (XO).')
table_card(d, 'Chromosomal disorders', 'Karyotype?', [
    ('Down’s syndrome', '47, +21 (trisomy 21)', False), ('Klinefelter’s', '47, XXY', False), ('Turner’s', '45, XO', False)],
    term='Chromosomal disorders and karyotypes')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Ratios', 'F₂ ratio?', [
    ('Monohybrid (complete dominance)', '3:1 (phenotype), 1:2:1 (genotype)', False), ('Incomplete dominance', '1:2:1', False),
    ('Dihybrid', '9:3:3:1', False), ('Monohybrid test cross', '1:1', False), ('Dihybrid test cross', '1:1:1:1', False)],
    term='Key Mendelian ratios')
d.basic('Homozygous female × heterozygous male, single locus (Exercise 6)?', 'TT × Tt → all ' + T('tall') + ' (1 TT : 1 Tt). tt × Tt → ' + N('1 tall : 1 dwarf') + '.')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
