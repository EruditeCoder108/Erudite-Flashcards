import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch13-plant-growth-and-development')
d = Deck('Chapter 13: Plant Growth and Development', 'Class 11', ['class-11', 'biology', 'ch-13'])
d.description = 'Growth phases and rates, differentiation, plasticity, and the five plant growth regulators'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
GE, SG, DV = (1001, 639), (991, 1001), (1001, 377)

# ---------------------------------------------------------------- Intro
d.sec('13.0-intro')
d.basic('Development is the sum of which two processes?', T('Growth') + ' and ' + T('differentiation'))
d.basic('First step of plant growth?', T('Seed germination'))
d.basic('What happens to seeds when conditions are unfavourable?', 'They do not germinate and enter a period of ' + T('suspended growth or rest'))
d.occlusion('Figure 13.1 · Germination and seedling development in bean', M + 'fig_13_1_germination.webp', GE, [
    ('Seed coat', wbox(76, 182, 177, 203, GE), True), ('Epicotyl hook', wbox(315, 110, 400, 154, GE), True),
    ('Cotyledons', wbox(337, 270, 453, 291, GE), True), ('Cotyledon', wbox(124, 283, 229, 304, GE), True),
    ('Epicotyl', wbox(590, 243, 675, 264, GE), True), ('Hypocotyl', wbox(617, 355, 721, 376, GE), True),
    ('Hypocotyl', wbox(172, 373, 276, 394, GE), True)])
d.basic('Bean germination: which part forms a hook, and why?', 'The ' + T('epicotyl hook') + ' (NCERT fig.) protects the delicate shoot tip as it pushes through soil. Bean shows epigeal-type emergence of the cotyledons above the soil line.')

# ---------------------------------------------------------------- 13.1 Growth
d.sec('13.1-growth')
d.basic('Define growth.', 'An ' + T('irreversible permanent increase') + ' in size of an organ, its parts or an individual cell')
d.basic('Is growth accompanied by metabolism?', T('Yes') + ': both anabolic and catabolic processes, at the expense of energy')
d.basic('Is a piece of wood swelling in water growth?', X('No') + '. It is reversible imbibition, not a permanent increase with metabolism.')
d.basic('Why is plant growth called indeterminate?', 'Plants retain the capacity for ' + T('unlimited growth') + ' throughout life, due to ' + T('meristems'))
d.basic('What is the open form of growth?', 'New cells are ' + T('always being added') + ' to the plant body by meristem activity')
d.basic('Which meristems cause primary growth?', T('Root and shoot apical meristems') + ': elongation along the axis')
d.basic('Which meristems cause secondary growth, and in which plants?', T('Vascular cambium and cork cambium') + ' (lateral meristems): increase in girth, in dicots and gymnosperms', **fig('fig_13_2_meristems'))
d.basic('Growth at the cellular level is mainly due to?', 'Increase in the amount of ' + T('protoplasm'))
d.basic('Parameters used to measure growth?', 'Fresh weight, dry weight, length, area, volume, cell number')
d.basic('Maize root apical meristem produces how many cells per hour?', 'More than ' + N('17,500'))
d.basic('Watermelon cells may increase in size by up to?', N('3,50,000 times'))
d.cloze('Growth is measured as increase in {{c1::length}} for a pollen tube and increase in {{c2::surface area}} for a dorsiventral leaf.')
d.basic('Why is no single parameter good enough for growth through a plant\'s whole life?', 'Different organs and stages grow differently (cell number, cell size, length, area).<br>So one parameter misses the others')

d.sec('13.1.3-phases')
d.cloze('Three phases of growth: {{c1::meristematic}} → {{c2::elongation}} → {{c3::maturation}}.')
d.basic('Features of cells in the meristematic phase?', 'Rich in ' + T('protoplasm') + ', large nuclei, thin ' + T('primary cellulosic') + ' walls, abundant plasmodesmata')
d.basic('Features of cells in the elongation phase?', 'Increased ' + T('vacuolation') + ', cell enlargement, new cell wall deposition')
d.basic('Features of cells in the maturation phase?', 'Maximal size in terms of ' + T('wall thickening') + ' and protoplasmic modification')
d.basic('How are growth zones detected in a root (Figure 13.3)?', T('Parallel line technique') + ': equally spaced marks; zones just behind the apex spread apart most (elongation zone)', **fig('fig_13_3_parallel_lines'))

d.sec('13.1.4-growth-rates')
d.basic('What is growth rate?', 'Increased growth ' + T('per unit time'))
d.basic('Arithmetic growth: what happens after mitosis?', T('Only one') + ' daughter cell keeps dividing; the other differentiates and matures')
d.basic('Geometric growth: what happens after mitosis?', T('Both') + ' daughter cells keep dividing')
d.basic('Example of arithmetic growth?', 'A ' + E('root elongating at a constant rate') + '; length vs time gives a straight line', **fig('fig_13_5_linear_growth'))
d.basic('Equation for arithmetic growth?', 'L' + '<sub>t</sub> = L<sub>0</sub> + rt (r = elongation per unit time)')
d.basic('Equation for exponential growth?', 'W<sub>1</sub> = W<sub>0</sub> e<sup>rt</sup> (r = relative growth rate)')
d.basic('What is r in W₁ = W₀eʳᵗ called?', 'Relative growth rate, a measure of ability to produce new material: the ' + T('efficiency index'))
d.basic('Three phases of the sigmoid growth curve?', T('Lag') + ' (slow), ' + T('log/exponential') + ' (rapid), ' + T('stationary') + ' (limited nutrients)')
d.occlusion('Figure 13.6 · Sigmoid growth curve', M + 'fig_13_6_sigmoid.webp', SG, [
    ('Lag phase', wbox(263, 825, 516, 876, SG), True), ('Exponential phase', rot([166, 418, 512, 58], -57.6), True),
    ('Stationary phase', wbox(565, 35, 991, 86, SG), True)])
d.basic('Why does exponential growth stop?', T('Limited nutrient supply') + ' slows growth to a stationary phase')
d.basic('Which growth curve is typical of living organisms in nature?', T('Sigmoid (S-curve)'))
d.basic('What growth curve would a tree with seasonal activity show?', 'A series of ' + T('stacked S-curves') + ': one sigmoid per growing season')
d.basic('Absolute vs relative growth rate?', T('Absolute') + ': total growth per unit time. ' + T('Relative') + ': growth per unit time per unit initial size.')
d.basic('Leaves A (5→10 cm²) and B (50→55 cm²) both grew 5 cm². Which has higher relative growth rate?', T('A') + ': it doubled (100%) while B grew only 10%. Absolute growth is equal.', **fig('fig_13_7_absolute_relative'))
d.basic('Figure 13.4 (c): embryo development shows which growth patterns?', 'An early ' + T('geometric') + ' phase (all cells divide) followed by an ' + T('arithmetic') + ' phase', **fig('fig_13_4_arithmetic_geometric'))

d.sec('13.1.5-conditions')
d.basic('Conditions necessary for growth?', T('Water, oxygen, nutrients') + ', optimum ' + T('temperature') + '; light and gravity affect some stages')
d.basic('Two roles of water in growth?', 'Cell enlargement needs water (' + T('turgidity') + ' helps extension); water is the medium for enzymes')
d.basic('Role of oxygen in growth?', 'Releases ' + T('metabolic energy') + ' (respiration)')
d.basic('Role of nutrients in growth?', 'Synthesis of ' + T('protoplasm') + ' and a source of energy')

# ---------------------------------------------------------------- 13.2 Differentiation
d.sec('13.2-differentiation')
d.basic('What is differentiation?', 'Maturation of cells from meristems and cambium to perform ' + T('specific functions'))
d.basic('How does a cell differentiate into a tracheary element?', 'Loses its ' + T('protoplasm') + ' and develops strong, elastic ' + T('lignocellulosic secondary walls'))
d.basic('What is dedifferentiation?', 'Differentiated cells that lost the capacity to divide ' + T('regain') + ' it')
d.basic('Examples of dedifferentiation?', 'Formation of ' + E('interfascicular cambium') + ' and ' + E('cork cambium') + ' from parenchyma')
d.basic('What is redifferentiation?', 'Cells from dedifferentiated tissue ' + T('again lose') + ' the capacity to divide and mature for specific functions')
d.basic('Examples of redifferentiated tissues in a woody dicot?', E('Secondary xylem, secondary phloem, cork (phellem), secondary cortex'))
d.basic('What is a callus in tissue culture an example of?', T('Dedifferentiation') + ': parenchyma made to divide in controlled conditions')
d.cloze('Differentiation → {{c1::dedifferentiation}} (regain division, e.g. cork cambium) → {{c2::redifferentiation}} (mature again, e.g. cork).')
d.basic('Why is differentiation in plants called "open"?', 'Cells from the same meristem have ' + T('different structures') + ' at maturity, decided by their position')
d.basic('Example of position deciding a cell\'s fate?', 'Cells pushed away from the root apical meristem become ' + T('root cap') + '<br>Those pushed to the periphery become ' + T('epidermis'))

# ---------------------------------------------------------------- 13.3 Development
d.sec('13.3-development')
d.basic('Define development.', 'All changes an organism goes through in its life cycle, from ' + T('germination to senescence'))
d.occlusion('Figure 13.8 · Development of a plant cell', M + 'fig_13_8_development.webp', DV, [
    ('Plasmatic growth', wbox(273, 158, 459, 180, DV), True), ('Differentiation', wbox(540, 155, 696, 177, DV), True),
    ('Expansion (elongation)', wbox(406, 262, 535, 310, DV), True), ('Maturation', wbox(646, 260, 767, 282, DV), True),
    ('Senescence', wbox(776, 56, 934, 78, DV), True)])
d.basic('What is plasticity?', 'Ability of plants to follow ' + T('different pathways') + ' in response to environment or life phase.<br>Different structures form')
d.basic('What is heterophylly?', 'Different ' + T('leaf shapes') + ' on the same plant: an example of plasticity')
d.basic('Heterophylly due to life phase: examples?', E('Cotton, coriander, larkspur') + ': juvenile leaves differ from adult leaves', **fig('fig_13_9_heterophylly'))
d.basic('Heterophylly due to environment: example?', E('Buttercup') + ': leaves in air differ from leaves in water')
d.basic('Intrinsic vs extrinsic factors controlling development?', T('Intrinsic') + ': genetic (intracellular) and PGRs (intercellular)<br>' + T('Extrinsic') + ': light, temperature, water, oxygen, nutrition')

# ---------------------------------------------------------------- 13.4 PGRs
d.sec('13.4.1-pgr-characteristics')
d.basic('What are plant growth regulators (PGRs)?', 'Small, simple molecules of diverse chemistry.<br>Also called plant growth substances, plant hormones or ' + T('phytohormones'))
table_card(d, 'PGR chemistry', 'Chemical nature?', [
    ('Auxin (IAA)', 'Indole compound', False), ('Cytokinin (kinetin)', 'Adenine derivative (N⁶-furfurylamino purine)', False),
    ('Abscisic acid', 'Carotenoid derivative', False), ('Gibberellic acid (GA₃)', 'Terpene', False), ('Ethylene', 'Gas (C₂H₄)', False)],
    term='Chemical nature of PGRs')
d.basic('Growth promoter PGRs?', T('Auxins, gibberellins, cytokinins'))
d.basic('Growth inhibitor PGR?', T('Abscisic acid') + ' (ethylene largely too)')
d.basic('Which PGR fits both groups?', T('Ethylene') + ': but it is largely an inhibitor')
d.basic('Roles of inhibitor PGRs?', 'Responses to ' + T('wounds and stresses') + ', dormancy, abscission')

d.sec('13.4.2-discovery')
d.basic('Were PGR discoveries planned?', X('No') + '. All five major groups were discovered ' + T('accidentally') + '.')
d.basic('What did Charles and Francis Darwin observe?', 'Coleoptiles of ' + E('canary grass') + ' bend towards unilateral light (' + T('phototropism') + ').<br>The ' + T('tip') + ' is the source of the influence', **fig('fig_13_10_coleoptile'))
d.basic('Who isolated auxin, and from what?', T('F.W. Went') + ', from coleoptile tips of ' + E('oat') + ' seedlings')
d.basic('What is bakanae disease?', '"Foolish seedling" disease of ' + T('rice') + ', caused by the fungus ' + EI('Gibberella fujikuroi') + ': seedlings grow abnormally tall')
d.basic('Who linked bakanae to a fungal substance, and when?', T('E. Kurosawa') + ' (' + N('1926') + '): sterile fungal filtrates caused the symptoms; the substance was gibberellic acid')
d.basic('What did Skoog observe with tobacco callus?', 'Callus from internode segments grew only if, besides auxin, the medium had ' + T('vascular extract, yeast extract, coconut milk or DNA'))
d.basic('Who named and crystallised kinetin?', T('Miller et al.') + ' (' + N('1955') + ')')
d.basic('Three inhibitors later shown to be abscisic acid?', T('Inhibitor-B, abscission II, dormin') + ' (mid-1960s)')
d.basic('How was ethylene discovered?', T('H.H. Cousins') + ' (' + N('1910') + '): ripe oranges released a volatile substance that hastened ripening of stored bananas')
table_card(d, 'Discovery', 'Who / what?', [
    ('Auxin', 'Darwins (phototropism); Went isolated (oat)', False), ('Gibberellin', 'Kurosawa, bakanae of rice', False),
    ('Cytokinin', 'Skoog; Miller named kinetin', False), ('ABA', 'Inhibitor-B, abscission II, dormin', False),
    ('Ethylene', 'Cousins, oranges and bananas', False)], term='Discovery of PGRs')

d.sec('13.4.3.1-auxins')
d.basic('Meaning of "auxin"?', 'Greek ' + I('auxein') + ' = to grow')
d.basic('From where was auxin first isolated?', T('Human urine'))
d.basic('Where are auxins produced?', 'Growing ' + T('apices') + ' of stems and roots; they migrate to regions of action')
d.basic('Natural vs synthetic auxins?', 'Natural: ' + T('IAA, IBA') + '. Synthetic: ' + T('NAA, 2,4-D') + '.')
d.basic('Uses of auxins?', 'Rooting in stem cuttings; flowering in ' + E('pineapple') + '; prevent early fruit/leaf drop; parthenocarpy in ' + E('tomato') + '; herbicides; xylem differentiation; cell division')
d.basic('Auxin and abscission?', 'Prevents drop of ' + T('young') + ' leaves and fruits; promotes abscission of ' + T('older mature') + ' ones')
d.basic('What is apical dominance?', 'The growing ' + T('apical bud inhibits') + ' growth of lateral (axillary) buds', **fig('fig_13_11_apical_dominance'))
d.basic('What happens on decapitation (removing the shoot tip)?', 'Lateral buds grow into ' + T('branches'))
d.basic('Why are tea bushes and hedges regularly pruned?', 'Removing apical buds removes apical dominance, so lateral buds branch into a ' + T('dense bush'))
d.basic('What is 2,4-D used for, and why is it selective?', 'Kills ' + T('dicot weeds') + ' but not mature monocots: weed-free lawns and cereal fields')
d.basic('Which PGR induces parthenocarpy in tomatoes?', T('Auxin'))

d.sec('13.4.3.2-gibberellins')
d.basic('How many gibberellins are known?', 'More than ' + N('100') + ', from fungi and higher plants (GA₁, GA₂, GA₃…)')
d.basic('Most studied gibberellin?', T('Gibberellic acid (GA₃)'))
d.basic('Chemical nature of all GAs?', T('Acidic'))
d.basic('Uses of gibberellins?', 'Longer ' + E('grape stalks') + '; elongate and shape ' + E('apples') + '; delay senescence; speed ' + E('malting') + '; increase ' + E('sugarcane') + ' yield; early seeds in conifers; bolting')
d.basic('By how much can GA increase sugarcane yield?', 'Up to ' + N('20 tonnes per acre') + ' (longer stems store more sugar)')
d.basic('What is bolting? Which PGR causes it?', T('Internode elongation') + ' just before flowering in rosette plants (' + E('beet, cabbage') + '); caused by ' + T('gibberellins'))
d.basic('GA use in brewing?', 'GA₃ speeds up the ' + T('malting') + ' process')
d.basic('Why do GAs extend the market period of fruits?', 'They ' + T('delay senescence') + ', so fruit stays on the tree longer')
d.basic('What happens if GA₃ is applied to rice seedlings?', 'They grow ' + T('abnormally tall') + ' (like bakanae)')

d.sec('13.4.3.3-cytokinins')
d.basic('Cytokinins mainly affect?', T('Cytokinesis') + ' (cell division)')
d.basic('From where was kinetin discovered?', 'Autoclaved ' + T('herring sperm DNA'))
d.basic('Does kinetin occur naturally in plants?', X('No'))
d.basic('Natural cytokinin, and its sources?', T('Zeatin') + ', from ' + E('corn kernels') + ' and ' + E('coconut milk'))
d.basic('Where are natural cytokinins made?', 'Regions of ' + T('rapid cell division') + ': root apices, developing shoot buds, young fruits')
d.basic('Effects of cytokinins?', 'New leaves, chloroplasts, lateral shoot growth, adventitious shoots; ' + T('overcome apical dominance') + '; nutrient mobilisation that ' + T('delays leaf senescence'))
d.basic('Auxin vs cytokinin on lateral buds?', 'Auxin (from apex) ' + X('inhibits') + ' them; cytokinin ' + T('promotes') + ' their growth')
d.basic('What if you forget cytokinin in tissue culture medium?', 'Cells will ' + X('not divide') + ' well; callus and shoots will not form')

d.sec('13.4.3.4-ethylene')
d.basic('Which tissues make large amounts of ethylene?', 'Tissues undergoing ' + T('senescence') + ' and ' + T('ripening fruits'))
d.basic('Effects of ethylene on seedlings?', T('Horizontal growth') + ', swelling of the axis, ' + T('apical hook') + ' in dicot seedlings')
d.basic('What is the respiratory climacteric?', 'The rise in respiration rate during fruit ripening, enhanced by ' + T('ethylene'))
d.basic('Correction: NCERT prints "respiratory climactic". Correct term?', T('Respiratory climacteric'))
d.basic('Ethylene and dormancy?', 'Breaks seed and bud dormancy; initiates germination in ' + E('peanut') + ', sprouting of ' + E('potato tubers'))
d.basic('Ethylene in deep-water rice?', 'Rapid ' + T('internode/petiole elongation') + ' keeps upper parts above water')
d.basic('Ethylene and roots?', 'Promotes ' + T('root growth') + ' and ' + T('root hairs') + ' (larger absorption surface)')
d.basic('Ethylene and flowering?', 'Initiates flowering and synchronises fruit-set in ' + E('pineapple') + '; induces flowering in ' + E('mango'))
d.basic('Most widely used source of ethylene?', T('Ethephon') + ': absorbed in solution, releases ethylene slowly')
d.basic('Uses of ethephon?', 'Hastens ripening of ' + E('tomatoes, apples') + '; thinning of ' + E('cotton, cherry, walnut') + '; promotes ' + T('female flowers') + ' in ' + E('cucumber'))
d.basic('What happens if a rotten fruit is mixed with unripe fruits?', 'Its ' + T('ethylene') + ' hastens their ripening')
d.basic('Intuition: "one bad apple spoils the barrel"?', 'Over-ripe fruit releases ' + T('ethylene') + ', which speeds ripening (and rotting) of neighbours')

d.sec('13.4.3.5-aba')
d.basic('ABA was discovered for which roles?', 'Regulating ' + T('abscission') + ' and ' + T('dormancy'))
d.basic('Effects of ABA?', 'General growth and metabolism ' + T('inhibitor') + '; inhibits germination; closes ' + T('stomata') + '; increases stress tolerance; seed development, maturation and dormancy')
d.basic('Why is ABA called the stress hormone?', 'It increases tolerance to stresses, e.g. by ' + T('closing stomata') + ' in water stress')
d.basic('How does ABA help seeds?', 'Induces ' + T('dormancy') + ', helping them withstand desiccation')
d.basic('ABA is antagonistic to which PGR?', T('Gibberellins'))
d.basic('Mnemonic: ABA\'s jobs?', '"' + T('ABA says STOP') + '": Stomata close, Dormancy, Abscission (named for it), stress; it Stops germination')

d.sec('13.4-interactions')
d.basic('How can PGRs interact?', T('Complementary or antagonistic') + '; ' + T('individualistic or synergistic'))
d.basic('Events controlled by more than one PGR?', 'Dormancy, abscission, senescence, apical dominance')
d.basic('Which extrinsic factors act through PGRs?', 'Temperature and light: vernalisation, flowering, dormancy, germination, plant movements')
d.basic('Note: exercises mention photoperiodism and vernalisation. Are they in this edition?', 'Those sections were ' + X('removed') + ' from the current NCERT text; only the exercises remain')
table_card(d, 'Exercise 8', 'Which PGR would you use?', [
    ('Induce rooting in a twig', 'Auxin (IBA/NAA)', False), ('Quickly ripen a fruit', 'Ethylene (ethephon)', False),
    ('Delay leaf senescence', 'Cytokinin', False), ('Grow axillary buds', 'Cytokinin', False),
    ('Bolt a rosette plant', 'Gibberellin', False), ('Close stomata immediately', 'Abscisic acid', False)], term='Which PGR for which job')
table_card(d, 'Senescence', 'Promote or delay?', [
    ('Cytokinin', 'Delays', False), ('Gibberellin', 'Delays', False), ('Ethylene', 'Promotes', True), ('ABA', 'Promotes', True)],
    term='PGRs and senescence')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
