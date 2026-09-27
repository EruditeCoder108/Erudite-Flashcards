import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch09-biomolecules')
d = Deck('Chapter 9: Biomolecules', 'Class 11', ['class-11', 'biology', 'ch-9'])
d.description = 'Chemical analysis of tissues, metabolites, proteins, polysaccharides, nucleic acids and enzymes'
M = 'media/'
P = lambda b: pad(b, 6)
fig = lambda name: {'definitionImage': M + name + '.webp'}

# ---------------------------------------------------------------- Elements, analysis
d.sec('9.0-elements')
d.basic('How does the elemental list of living tissue differ from that of earth\'s crust?', 'The same elements are present, but ' + T('carbon and hydrogen') + ' are relatively far more abundant in living organisms')
table_card(d, 'Table 9.1 · % weight', 'Earth\'s crust vs human body?', [
    ('Carbon', '0.03 vs 18.5', False), ('Hydrogen', '0.14 vs 9.5', False), ('Oxygen', '46.6 vs 65.0', False),
    ('Nitrogen', 'very little vs 3.3', False), ('Silicon', '27.7 vs negligible', True)], term='Table 9.1: elements in crust vs body')
d.basic('Which element is most abundant by weight in both the crust and the human body?', T('Oxygen') + ' (46.6% and 65%)')

d.sec('9.1-analysis')
d.basic('In what is living tissue ground for chemical analysis?', T('Trichloroacetic acid') + ' (Cl₃CCOOH)')
d.basic('Acid-soluble pool vs acid-insoluble fraction?', T('Filtrate') + ' = acid-soluble pool (small molecules). ' + T('Retentate') + ' = acid-insoluble fraction (macromolecules).')
d.basic('What are biomolecules?', 'All the ' + T('carbon compounds') + ' obtained from living tissues')
d.basic('Wet weight, dry weight and ash?', 'Wet: fresh tissue. Dry: after water evaporates. ' + T('Ash') + ': what remains after burning; contains ' + T('inorganic') + ' elements (Ca, Mg...).')
d.basic('Name the inorganic constituents of living tissue (Table 9.2).', 'Na⁺, K⁺, Ca²⁺, Mg²⁺, water, and compounds NaCl, CaCO₃, PO₄³⁻, SO₄²⁻')

d.sec('9.1-amino-acids')
d.basic('What is an α-amino acid?', 'An amino group and an acidic (carboxyl) group on the same carbon, the ' + T('α-carbon') + '')
d.basic('Name the four groups on the α-carbon of an amino acid.', 'Hydrogen, carboxyl group, amino group, variable ' + T('R group'))
d.basic('How many amino acids occur in proteins?', N('Twenty'))
d.cloze('R group = hydrogen: {{c1::glycine}}; methyl: {{c2::alanine}}; hydroxy methyl: {{c3::serine}}.')
d.basic('Give an acidic, a basic and a neutral amino acid.', 'Acidic: ' + E('glutamic acid') + '. Basic: ' + E('lysine') + '. Neutral: ' + E('valine') + '.')
d.basic('Name the aromatic amino acids.', E('Tyrosine, phenylalanine, tryptophan'))
d.basic('What is the zwitterionic form of an amino acid?', 'The form carrying both a ' + T('positive (–NH₃⁺)') + ' and a ' + T('negative (–COO⁻)') + ' charge; amino acid structure changes with pH because –NH₂ and –COOH ionise')
d.basic('Why is the zwitterion called that? (intuition)', 'German ' + I('zwitter') + ' = hybrid: one molecule, both charges, net charge zero')

d.sec('9.1-lipids')
d.basic('What is a fatty acid?', 'A ' + T('carboxyl group') + ' attached to an R group (1 to 19 carbons)')
d.basic('How many carbons in palmitic acid and arachidonic acid?', 'Palmitic: ' + N('16') + '. Arachidonic: ' + N('20') + ' (both including the carboxyl carbon).')
d.basic('Saturated vs unsaturated fatty acid?', 'Saturated: ' + X('no') + ' double bond. Unsaturated: one or more ' + T('C=C') + ' double bonds.')
d.basic('What is glycerol?', T('Trihydroxy propane'))
d.basic('What are mono-, di- and triglycerides?', 'Glycerol ' + T('esterified') + ' with one, two or three fatty acids')
d.basic('Fats vs oils?', 'Classified by ' + T('melting point') + ': oils have a lower melting point and stay liquid in winter (e.g. ' + E('gingelly oil') + ')')
d.basic('What are phospholipids? Example?', 'Lipids with ' + T('phosphorus') + ' and a phosphorylated organic compound; in cell membranes, e.g. ' + E('lecithin'))

d.sec('9.1-nucleotides')
d.basic('Name the five nitrogen bases.', 'Adenine, guanine, cytosine, uracil, thymine')
d.basic('Nucleoside vs nucleotide?', T('Nucleoside') + ' = base + sugar. ' + T('Nucleotide') + ' = base + sugar + ' + T('phosphate') + '.')
d.basic('Is adenosine a nucleoside or nucleotide? Adenylic acid?', 'Adenosine: ' + T('nucleoside') + '. Adenylic acid: ' + T('nucleotide') + '.')
d.basic('Figure 9.1: which classes of small biomolecules are shown?', 'Sugars (glucose, ribose), amino acids (glycine, alanine, serine), lipids (fatty acid, glycerol, triglyceride, lecithin, cholesterol), nitrogen bases, nucleosides, nucleotide', **fig('fig_9_1_small_biomolecules'))
d.basic('Purines vs pyrimidines?', T('Purines') + ': adenine, guanine. ' + T('Pyrimidines') + ': cytosine, uracil, thymine.')
d.basic('Mnemonic for purines?', '"' + T('Pure As Gold') + '": purines are Adenine and Guanine. (Pyrimidines have the "y": c<b>y</b>tosine, th<b>y</b>mine, and uracil.)')

# ---------------------------------------------------------------- 9.2-9.3
d.sec('9.2-metabolites')
d.basic('Primary vs secondary metabolites?', T('Primary') + ': identifiable roles in normal physiology (e.g. amino acids, sugars). ' + T('Secondary') + ': in plants, fungi, microbes; roles in the host often unknown.')
table_card(d, 'Table 9.3 · Secondary metabolites', 'Give the NCERT example(s).', [
    ('Pigments', 'Carotenoids, anthocyanins', False), ('Alkaloids', 'Morphine, codeine', False), ('Terpenoids', 'Monoterpenes, diterpenes', False),
    ('Essential oils', 'Lemon grass oil', False), ('Toxins', 'Abrin, ricin', False), ('Lectins', 'Concanavalin A', False),
    ('Drugs', 'Vinblastin, curcumin', False), ('Polymeric substances', 'Rubber, gums, cellulose', False)], term='Table 9.3: secondary metabolites')
d.basic('Which secondary metabolite is a lectin?', E('Concanavalin A'))
d.basic('Name two toxins among secondary metabolites.', E('Abrin, ricin'))

d.sec('9.3-macromolecules')
d.basic('Molecular weight range in the acid-soluble pool?', N('18 to ~800') + ' daltons')
d.basic('Name the four organic compound classes of the acid-insoluble fraction.', 'Proteins, nucleic acids, polysaccharides, lipids')
d.basic('Micromolecules vs macromolecules?', 'Micro: below ' + N('1000 Da') + '. Macro: in the acid-insoluble fraction (≥ ~10,000 Da, except lipids).')
d.basic('Why do lipids (under 800 Da) appear in the acid-insoluble fraction?', 'They form ' + T('membranes') + '; grinding breaks membranes into insoluble ' + T('vesicles') + '. Lipids are ' + X('not strictly') + ' macromolecules.')
d.basic('What does the acid-soluble pool roughly represent?', 'The ' + T('cytoplasmic') + ' composition')
table_card(d, 'Table 9.4 · Average cell composition', '% of total cellular mass?', [
    ('Water', '70–90', False), ('Proteins', '10–15', False), ('Nucleic acids', '5–7', False), ('Carbohydrates', '3', False),
    ('Lipids', '2', False), ('Ions', '1', False)], term='Table 9.4: composition of cells')
d.basic('Most abundant chemical in living organisms?', T('Water'))

# ---------------------------------------------------------------- 9.4 Proteins
d.sec('9.4-proteins')
d.basic('What are proteins?', T('Polypeptides') + ': linear chains of amino acids joined by ' + T('peptide bonds'))
d.basic('Is a protein a homopolymer or heteropolymer? Why?', T('Heteropolymer') + ': made of up to 20 different amino acids')
d.basic('Essential vs non-essential amino acids?', 'Essential: must come from the ' + T('diet') + '. Non-essential: the body can make them.')
table_card(d, 'Table 9.5 · Proteins', 'Function of each?', [
    ('Collagen', 'Intercellular ground substance', False), ('Trypsin', 'Enzyme', False), ('Insulin', 'Hormone', False),
    ('Antibody', 'Fights infectious agents', False), ('Receptor', 'Sensory reception (smell, taste, hormone)', False),
    ('GLUT-4', 'Glucose transport into cells', False)], term='Table 9.5: protein functions')
d.basic('Most abundant protein in the animal world? In the whole biosphere?', 'Animals: ' + T('collagen') + '. Biosphere: ' + T('RuBisCO') + ' (Ribulose bisphosphate carboxylase-oxygenase).')

# ---------------------------------------------------------------- 9.5 Polysaccharides
d.sec('9.5-polysaccharides')
d.basic('What are polysaccharides?', 'Long chains of ' + T('sugars') + ' (monosaccharide building blocks)')
d.basic('Monomer of cellulose? Homo- or heteropolymer?', T('Glucose') + '; a ' + T('homopolymer'))
d.basic('Storage polysaccharide in plants vs animals?', 'Plants: ' + T('starch') + '. Animals: ' + T('glycogen') + '.')
d.basic('Inulin is a polymer of which sugar?', T('Fructose'))
d.basic('Which end of a glycogen chain is reducing?', 'The ' + T('right') + ' end (left = non-reducing)', **fig('fig_9_2_glycogen'))
d.basic('Why does starch turn blue with iodine but cellulose does not?', 'Starch forms ' + T('helical') + ' secondary structures that hold I₂; cellulose has ' + X('no complex helices'))
d.basic('What is chitin, and where is it found?', 'A complex polysaccharide of amino-sugars; in the ' + T('exoskeletons of arthropods') + ' (and fungal walls)')
d.basic('What are complex polysaccharides built from?', 'Amino-sugars and modified sugars, e.g. ' + E('glucosamine, N-acetyl galactosamine'))

# ---------------------------------------------------------------- 9.6 Nucleic acids
d.sec('9.6-nucleic-acids')
d.basic('Three components of a nucleotide?', 'A heterocyclic ' + T('nitrogenous base') + ', a ' + T('monosaccharide') + ', and ' + T('phosphate'))
d.basic('Which three kinds of macromolecules make the true macromolecular fraction?', 'Polysaccharides, polypeptides, polynucleotides')
d.basic('Sugar in DNA vs RNA?', 'DNA: ' + T('2\'-deoxyribose') + '. RNA: ' + T('ribose') + '.')

# ---------------------------------------------------------------- 9.7 Protein structure
d.sec('9.7-protein-structure')
d.basic('What is the primary structure of a protein?', 'The ' + T('sequence') + ' of amino acids')
d.basic('N-terminal vs C-terminal amino acid?', 'N-terminal: the ' + T('first') + ' amino acid (left). C-terminal: the ' + T('last') + ' (right).')
d.basic('Which helices are found in proteins?', 'Only ' + T('right-handed') + ' helices')
d.basic('What is tertiary structure, and why does it matter?', 'The chain folded on itself like a hollow woollen ball: the ' + T('3-D') + ' shape, essential for biological activity')
d.basic('What is quaternary structure? Example?', 'Arrangement of ' + T('several subunits') + ', e.g. adult haemoglobin: ' + N('2 α + 2 β'))
d.occlusion('Figure 9.3 · Levels of protein structure', M + 'fig_9_3_protein_structure.webp', (872, 1001), [
    ('Primary', P((106, 78, 117, 30))), ('Secondary', P((108, 294, 155, 30))), ('Tertiary', P((160, 620, 120, 30))),
    ('Quaternary', P((149, 843, 171, 30))), ('Alpha-helix', P((69, 473, 191, 30))), ('Beta-pleated sheet', P((570, 476, 297, 30))),
    ('Hydrogen bond', P((548, 608, 230, 30))), ('Disulphide bond', P((551, 646, 249, 30)))], printed=True)

# ---------------------------------------------------------------- 9.8 Enzymes
d.sec('9.8-enzymes')
d.basic('Are all enzymes proteins?', 'Almost all; some nucleic acids act as enzymes: ' + T('ribozymes'))
d.basic('What is the active site?', 'A crevice or pocket in the folded enzyme into which the ' + T('substrate') + ' fits')
d.basic('Enzymes vs inorganic catalysts: temperature?', 'Inorganic catalysts work at high temperature and pressure; enzymes are ' + X('damaged above ~40 °C') + ' (except those of thermophiles, stable up to ' + N('80–90 °C') + ')')
d.basic('Physical change vs chemical reaction?', 'Physical: shape or state changes ' + X('without') + ' breaking bonds. Chemical: bonds broken and new ones formed.')
d.basic('Rate of a reaction?', 'Amount of product per unit time: rate ' + r'\(= \dfrac{\delta P}{\delta t}\)')
d.basic('Rule of thumb: temperature and reaction rate?', 'Rate ' + T('doubles') + ' (or halves) for every ' + N('10 °C') + ' change')
d.basic('How much does carbonic anhydrase speed up CO₂ + H₂O → H₂CO₃?', 'From ~' + N('200') + ' molecules/hour to ~' + N('600,000') + '/second: about ' + N('10 million') + ' times')
d.basic('What is a metabolic pathway?', 'A multistep reaction, each step catalysed by the same enzyme complex or different enzymes')
d.basic('Glucose → pyruvic acid takes how many enzyme steps?', N('Ten'))
d.basic('End product of the glucose pathway in muscle (anaerobic), aerobic cells, and yeast?', 'Muscle, anaerobic: ' + T('lactic acid') + '. Aerobic: ' + T('pyruvic acid') + '. Yeast fermentation: ' + T('ethanol') + '.')
d.basic('NCERT writes glucose → pyruvate with O₂. Does glycolysis need oxygen? (clarification)', X('No') + '. Glycolysis itself is anaerobic. The O₂ in NCERT\'s overall equation re-oxidises the NADH formed; the ten steps run without oxygen.')

d.sec('9.8.2-activation-energy')
d.basic('What is the ES complex?', 'The transient complex formed when the substrate binds the enzyme\'s ' + T('active site') + '; its formation is ' + T('obligatory') + ' for catalysis')
d.basic('What is the transition state?', 'An unstable, high-energy structure the substrate passes through on its way to product')
d.basic('What is activation energy?', 'The difference in energy between the ' + T('substrate') + ' and the ' + T('transition state'))
d.basic('How do enzymes speed up reactions?', 'By ' + T('lowering the activation energy'))
d.basic('If product P is at a lower energy than S, the reaction is...?', T('Exothermic') + ' (no need to supply heat)')
d.occlusion('Figure 9.4 · Concept of activation energy', M + 'fig_9_4_activation_energy.webp', (997, 1001), [
    ('Transition state', P((262, 69, 322, 42))), ('Activation energy without enzyme', P((513, 193, 351, 89))),
    ('Activation energy with enzyme', P((565, 406, 403, 89))), ('Substrate (S)', P((85, 534, 259, 42))), ('Product (P)', P((806, 858, 159, 42)))],
    printed=True)
d.cloze('Catalytic cycle: E + S → {{c1::ES}} → {{c2::EP}} → E + P.')
d.basic('List the four steps of the catalytic cycle.', '<ol><li>Substrate binds the active site</li><li>Binding makes the enzyme change shape, fitting tighter (' + T('induced fit') + ')</li><li>Active site breaks bonds; EP complex forms</li><li>Product released; enzyme free again</li></ol>')

d.sec('9.8.4-factors')
d.basic('Which factors affect enzyme activity?', 'Temperature, pH, substrate concentration, binding of specific chemicals (by altering tertiary structure)')
d.basic('Effect of low vs high temperature on enzymes?', 'Low: enzyme ' + T('temporarily inactive') + ' (preserved). High: ' + X('denatured') + ', activity destroyed.')
d.basic('What are optimum temperature and pH?', 'The temperature and pH at which an enzyme shows its ' + T('highest activity'))
d.basic('Why does reaction velocity level off at Vmax as [S] rises?', 'All enzyme molecules are ' + T('saturated') + ' with substrate; none free for more substrate', **fig('fig_9_5_enzyme_activity'))
d.basic('What is Km (Figure 9.5 c)? (beyond NCERT text)', 'The substrate concentration at which velocity is ' + T('half of Vmax') + '; a low Km means high affinity')
d.basic('What is a competitive inhibitor?', 'A chemical that ' + T('resembles the substrate') + ' and competes for the substrate-binding site')
d.basic('Classic example of competitive inhibition?', T('Malonate') + ' inhibits ' + T('succinic dehydrogenase') + ' (resembles succinate)')
d.basic('Where are competitive inhibitors used?', 'In controlling ' + T('bacterial pathogens'))

d.sec('9.8.5-classification')
d.basic('How many classes of enzymes? How are they numbered?', N('Six') + ' classes, each with 4–13 subclasses, named by a ' + N('four-digit') + ' number')
table_card(d, '9.8.5 · Enzyme classes', 'What does each class catalyse?', [
    ('Oxidoreductases', 'Oxidoreduction between two substrates', False), ('Transferases', 'Transfer of a group (not H) between substrates', False),
    ('Hydrolases', 'Hydrolysis of ester, ether, peptide, glycosidic, C–C, C–halide, P–N bonds', False),
    ('Lyases', 'Removal of groups by non-hydrolytic means, leaving double bonds', False),
    ('Isomerases', 'Inter-conversion of optical, geometric, positional isomers', False),
    ('Ligases', 'Joining two compounds (C–O, C–S, C–N, P–O bonds)', False)], term='Six enzyme classes')
d.basic('Mnemonic for the six enzyme classes, in order?', '"' + T('Over The Hill, Lazy Iguanas Lounge') + '": Oxidoreductases, Transferases, Hydrolases, Lyases, Isomerases, Ligases')

d.sec('9.8.6-cofactors')
d.basic('What is an apoenzyme?', 'The ' + T('protein part') + ' of an enzyme that needs a cofactor')
d.basic('Name the three kinds of cofactors.', T('Prosthetic groups') + ', ' + T('co-enzymes') + ', ' + T('metal ions'))
d.basic('Prosthetic group vs co-enzyme?', 'Both organic. Prosthetic group: ' + T('tightly bound') + '. Co-enzyme: ' + T('transient') + ' association during catalysis.')
d.basic('Example of a prosthetic group?', T('Haem') + ' in peroxidase and catalase (break down H₂O₂)')
d.basic('Which vitamin is part of NAD and NADP?', T('Niacin'))
d.basic('Which metal ion is a cofactor for carboxypeptidase?', T('Zinc'))
d.basic('What happens if the cofactor is removed?', 'Catalytic activity is ' + X('lost'))

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
