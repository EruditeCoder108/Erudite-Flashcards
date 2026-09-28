import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch10-biomolecules')
d = Deck('Chapter 10: Biomolecules', 'Class 12', ['class-12', 'chemistry', 'ch-10'])
d.description = 'Carbohydrates, glucose structure, disaccharides, polysaccharides, amino acids, proteins, enzymes, vitamins, nucleic acids, hormones'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 10.1 Carbohydrates
d.sec('10.1-carbohydrates')
d.basic('Origin of the name "carbohydrate", and why it fails?', 'Formula Cₓ(H₂O)ᵧ ("hydrates of carbon"); but ' + X('acetic acid') + ' fits and is not one, ' + X('rhamnose C₆H₁₂O₅') + ' is one but doesn’t fit')
d.basic('Chemical definition of carbohydrates?', T('Optically active polyhydroxy aldehydes or ketones') + ', or compounds giving these on hydrolysis')
d.basic('What are sugars and saccharides?', 'Sweet carbohydrates are sugars (sucrose in homes, ' + T('lactose') + ' in milk); saccharide from Greek ' + I('sakcharon') + ' = sugar')

d.sec('10.1.1-classification')
d.cloze('Classes by hydrolysis: {{c1::monosaccharides}} (can’t be hydrolysed; ~20 in nature); {{c2::oligosaccharides}} (2–10 units); {{c3::polysaccharides}} (many units; not sweet, "non-sugars").')
d.basic('Monosaccharides from sucrose vs maltose?', 'Sucrose → ' + T('glucose + fructose') + '; maltose → ' + T('two glucose'))
d.basic('What are reducing sugars?', 'Reduce ' + T('Fehling’s and Tollens’') + ' reagents; ' + T('all monosaccharides') + ' (aldoses and ketoses) are reducing')
d.basic('Aldose vs ketose? Naming by carbons?', 'Aldose: –CHO; ketose: C=O. Carbons prefix: triose, tetrose, pentose, hexose, heptose (e.g. aldohexose)', **fig('tab_10_1_monosaccharides'))

d.sec('10.1.2-glucose')
d.basic('Where is glucose found?', 'Free in ' + T('sweet fruits, honey, ripe grapes') + '; also combined in starch, cellulose, sucrose')
d.basic('Glucose from sucrose and from starch?', 'Sucrose + dil. HCl/H₂SO₄ (alcoholic) → glucose + fructose. Commercially: starch + dil. H₂SO₄ at ' + N('393 K, 2–3 atm') + '.', **fig('fig_glucose_from_sucrose_starch'))
d.basic('Other name for glucose?', T('Dextrose') + '; an aldohexose; probably the most abundant organic compound on earth')
d.basic('Glucose + HI (prolonged heating) shows?', T('n-Hexane') + ': all six C in a ' + T('straight chain'), **fig('fig_glucose_hi'))
d.basic('Glucose + NH₂OH and + HCN show?', 'Oxime and cyanohydrin: a ' + T('carbonyl group'), **fig('fig_glucose_oxime_hcn'))
d.basic('Glucose + bromine water shows?', T('Gluconic acid') + ' (6 C): carbonyl is an ' + T('aldehyde'), **fig('fig_glucose_br2'))
d.basic('Glucose + acetic anhydride shows?', T('Pentaacetate') + ': ' + T('five –OH') + ' on different carbons', **fig('fig_glucose_acetylation'))
d.basic('Glucose (and gluconic acid) + HNO₃ shows?', T('Saccharic acid') + ' (dicarboxylic): a ' + T('primary alcohol') + ' group', **fig('fig_glucose_hno3'))
d.basic('Fischer structures of glucose (I), gluconic acid (II), saccharic acid (III)?', 'Fischer’s configuration', **fig('fig_glucose_fischer'))
d.basic('Meaning of D and (+) in D-(+)-glucose?', T('D') + ': configuration (related to D-glyceraldehyde). ' + T('(+)') + ': dextrorotatory. D/L are ' + X('unrelated') + ' to d/l or sign of rotation.')
d.basic('D vs L glyceraldehyde?', '(+)-Glyceraldehyde has –OH on the ' + T('right') + ' (D); (–) on the left (L)', **fig('fig_glyceraldehyde'))
d.basic('Which carbon decides D/L in sugars?', 'The ' + T('lowest asymmetric carbon') + ' (C-5 in glucose), with the most oxidised carbon written on top', **fig('fig_d_glucose_config'))
d.cloze('Facts the open-chain glucose can’t explain: no {{c1::Schiff’s test}} and no NaHSO₃ adduct; pentaacetate doesn’t react with {{c2::hydroxylamine}}; exists as {{c3::α and β}} crystalline forms.')
d.basic('α- vs β-glucose: preparation and m.p.?', 'α: from concentrated solution at 303 K, m.p. ' + N('419 K') + '. β: from hot saturated solution at 371 K, m.p. ' + N('423 K') + '.')
d.basic('How is the cyclic structure formed?', '–OH at ' + T('C-5') + ' adds to –CHO → six-membered ' + T('cyclic hemiacetal') + '; α and β in equilibrium with open chain', **fig('fig_glucose_cyclic'))
d.basic('What is the anomeric carbon? Anomers?', T('C-1') + ' (former aldehyde carbon); α and β forms differing only there are ' + T('anomers'))
d.basic('What is a pyranose? Haworth structures?', 'Six-membered ring (like ' + T('pyran') + ': 1 O + 5 C)', **fig('fig_pyranose_haworth'))
d.basic('Why does glucose pentaacetate lack a free aldehyde? (Intext 10.3)', 'Acetylation locks C-1 in the ' + T('cyclic') + ' form; the ring can’t open to give –CHO')
d.basic('Intuition: why does glucose still give Tollens’ test if mostly cyclic?', 'The ring is in ' + T('equilibrium') + ' with a small amount of open chain; as it reacts, more ring opens (Le Chatelier)')

d.sec('10.1.2.2-fructose')
d.basic('Fructose: type, source, rotation?', T('Ketohexose') + ' (C=O at C-2); from sucrose hydrolysis, fruits, honey; ' + T('D-(–)-fructose') + ' (laevorotatory)', **fig('fig_fructose_open'))
d.basic('Cyclic form of fructose?', '–OH at ' + T('C-5') + ' adds to C-2 → five-membered ' + T('furanose') + ' ring (like furan: 1 O + 4 C)', **fig('fig_fructofuranose'))
d.basic('Haworth structures of fructose anomers?', 'α- and β-D-(–)-fructofuranose', **fig('fig_fructose_haworth'))

d.sec('10.1.3-disaccharides')
d.basic('What is a glycosidic linkage?', 'Oxide linkage between two monosaccharides via O, with loss of water')
d.basic('When is a disaccharide non-reducing?', 'When the reducing groups (–CHO / C=O) of both units are ' + T('bonded') + ' (sucrose); free ones → reducing (maltose, lactose)')
d.basic('Sucrose: linkage and reducing nature?', 'C1 of ' + T('α-D-glucose') + ' to C2 of ' + T('β-D-fructose') + ': ' + X('non-reducing'), **fig('fig_sucrose'))
d.basic('Why is hydrolysed sucrose called invert sugar?', 'Rotation changes from ' + T('dextro (+) to laevo (–)') + ': fructose (−92.4°) outweighs glucose (+52.5°)')
d.basic('Maltose: composition, linkage, reducing?', 'Two ' + T('α-D-glucose') + ', ' + T('C1–C4') + '; free –CHO at C1 of second unit: ' + T('reducing'), **fig('fig_maltose'))
d.basic('Lactose: composition, linkage, reducing?', T('β-D-galactose + β-D-glucose') + ', C1 (galactose)–C4 (glucose); ' + T('reducing') + ' (milk sugar)', **fig('fig_lactose'))
d.basic('Products of lactose hydrolysis? (Intext 10.2)', T('β-D-galactose and β-D-glucose'))
table_card(d, 'Disaccharides', 'Units · linkage · reducing?', [
    ('Sucrose', 'α-glucose + β-fructose · C1–C2 · No', True), ('Maltose', 'α-glucose + α-glucose · C1–C4 · Yes', False),
    ('Lactose', 'β-galactose + β-glucose · C1–C4 · Yes', False)], term='Sucrose, maltose and lactose compared')

d.sec('10.1.4-polysaccharides')
d.basic('Starch: role, sources, monomer?', 'Main ' + T('plant storage') + ' polysaccharide; cereals, roots, tubers; polymer of ' + T('α-glucose'))
d.basic('Amylose?', 'Water-' + T('soluble') + ', ' + N('15–20%') + ' of starch; unbranched chain of 200–1000 α-D-glucose, ' + T('C1–C4') + ' links', **fig('fig_amylose'))
d.basic('Amylopectin?', 'Water-' + X('insoluble') + ', ' + N('80–85%') + ' of starch; branched: chain C1–C4, ' + T('branches C1–C6'), **fig('fig_amylopectin'))
d.basic('Cellulose: occurrence and structure?', 'Only in plants (cell walls), most abundant organic substance in plants; straight chain of ' + T('β-D-glucose') + ', C1–C4', **fig('fig_cellulose'))
d.basic('Glycogen?', T('Animal starch') + ': like amylopectin but ' + T('more branched') + '; in liver, muscles, brain; also yeast and fungi')
d.basic('Intuition: why can’t humans digest cellulose though it is also glucose?', 'Its ' + T('β-linkages') + ' need an enzyme (cellulase) we lack; our amylase only cuts α-links')
d.basic('Why are glucose and sucrose water-soluble but cyclohexane isn’t? (Intext 10.1)', 'Many ' + T('–OH groups') + ' H-bond with water')
d.basic('Importance of carbohydrates?', 'Food, energy (honey in ayurveda), storage (starch, glycogen), cell walls (cellulose), wood, cotton; textiles, paper, lacquers, breweries; ribose and deoxyribose in nucleic acids')

# ---------------------------------------------------------------- 10.2 Proteins
d.sec('10.2-proteins')
d.basic('Origin of the word "protein"? Sources?', 'Greek ' + I('proteios') + ': of prime importance. Milk, cheese, pulses, peanuts, fish, meat.')
d.basic('Proteins are polymers of?', T('α-Amino acids') + ' (–NH₂ on the carbon next to –COOH)', **fig('fig_alpha_amino_acid'))
d.basic('Origins of the names glycine and tyrosine?', 'Glycine: sweet (' + I('glykos') + '). Tyrosine: first from cheese (' + I('tyros') + ').')
d.basic('Table 10.2: amino acids (1–4)', 'Glycine, alanine, valine, leucine', **fig('tab_10_2_amino_acids_a'))
d.basic('Table 10.2: amino acids (5–20)', 'Symbols and side chains', **fig('tab_10_2_amino_acids_b'))
d.basic('Neutral, acidic, basic amino acids?', 'Equal –NH₂ and –COOH: ' + T('neutral') + '; more –NH₂: ' + T('basic') + '; more –COOH: ' + T('acidic'))
d.basic('Essential vs non-essential amino acids?', T('Essential') + ': cannot be made by the body, must come from diet. ' + T('Non-essential') + ': synthesised in the body.')
d.cloze('Essential amino acids (NCERT *): {{c1::valine, leucine, isoleucine}}, {{c2::arginine, lysine}}, {{c3::threonine, methionine}}, {{c4::phenylalanine, tryptophan, histidine}}.')
d.basic('Mnemonic for essential amino acids?', '"' + T('PVT TIM HALL') + '": Phe, Val, Thr, Trp, Ile, Met, His, Arg, Leu, Lys')
d.basic('Why do amino acids behave like salts (high m.p., water-soluble)?', 'They exist as ' + T('zwitter ions') + ' (–COO⁻ and –NH₃⁺)', **fig('fig_zwitter_ion'))
d.basic('Why do amino acids melt higher than halo acids? (Intext 10.4)', 'Zwitter ions: strong ' + T('ionic attractions'))
d.basic('Amphoteric nature of amino acids?', 'Zwitter ion reacts with both ' + T('acids and bases'))
d.basic('Which natural α-amino acid is optically inactive?', T('Glycine') + ' (no asymmetric carbon); others mostly ' + T('L-configuration') + ' (–NH₂ on left)')

d.sec('10.2.3-structure-of-proteins')
d.basic('What is a peptide bond?', 'Amide –CO–NH– from –COOH of one amino acid and –NH₂ of another with loss of H₂O; glycine + alanine → ' + T('glycylalanine (Gly-Ala)'), **fig('fig_peptide_bond'))
d.basic('Dipeptide, tripeptide, polypeptide, protein?', '2, 3 amino acids; ' + T('> 10') + ' = polypeptide; ' + T('> 100') + ' residues, mass ' + T('> 10,000 u') + ' = protein (insulin, 51 residues, still called a protein)')
d.basic('Fibrous proteins?', 'Parallel chains held by H-bonds and ' + T('disulphide') + ' bonds; water-' + X('insoluble') + '; ' + E('keratin (hair, wool, silk), myosin (muscles)'))
d.basic('Globular proteins?', 'Chains coil into a sphere; usually water-' + T('soluble') + '; ' + E('insulin, albumins'))
d.basic('Primary structure?', 'The ' + T('sequence') + ' of amino acids; any change creates a different protein')
d.basic('Secondary structure?', 'Regular folding by ' + T('H-bonds between C=O and N–H') + ' of the backbone: α-helix or β-pleated sheet')
d.basic('α-Helix?', T('Right-handed') + ' screw; each N–H H-bonds to C=O of an adjacent turn', **fig('fig_10_1_alpha_helix'))
d.basic('β-Pleated sheet?', 'Chains stretched out side by side, held by ' + T('intermolecular') + ' H-bonds (like drapery folds)', **fig('fig_10_2_beta_sheet'))
d.basic('Tertiary structure and forces?', 'Overall folding (fibrous or globular); stabilised by H-bonds, ' + T('disulphide') + ', van der Waals, electrostatic forces')
d.basic('Quaternary structure?', 'Spatial arrangement of ' + T('two or more polypeptide sub-units'))
d.basic('Diagram of the four levels', 'Primary → secondary → tertiary → quaternary', **fig('fig_10_3_protein_levels'))
d.basic('Identify: structures of haemoglobin (a–d)?', '(a) primary, (b) secondary, (c) tertiary, (d) quaternary', **img('fig_10_4_haemoglobin'))

d.sec('10.2.4-denaturation')
d.basic('What is denaturation?', 'Heat or pH change disturbs H-bonds: globules unfold, helix uncoils, ' + X('biological activity lost'))
d.basic('Which structures are lost in denaturation?', T('Secondary and tertiary') + ' destroyed; ' + T('primary') + ' intact')
d.basic('Examples of denaturation?', E('Coagulation of egg white') + ' on boiling; ' + E('curdling of milk') + ' (lactic acid from bacteria)')
d.basic('Where does egg water go on boiling? (Intext 10.5)', 'Absorbed/held by the denatured coagulated protein (via H-bonding)')

# ---------------------------------------------------------------- 10.3 Enzymes
d.sec('10.3-enzymes')
d.basic('What are enzymes?', 'Biocatalysts, almost all ' + T('globular proteins') + '; very specific for reaction and substrate')
d.basic('How are enzymes named?', 'After substrate (' + E('maltase') + ': maltose → 2 glucose) or reaction (' + E('oxidoreductase') + '); ending ' + T('-ase'))
d.basic('How do enzymes speed up reactions? Example?', 'Lower ' + T('activation energy') + ': sucrose hydrolysis ' + N('6.22 kJ/mol') + ' with acid vs ' + N('2.15 kJ/mol') + ' with sucrase')

# ---------------------------------------------------------------- 10.4 Vitamins
d.sec('10.4-vitamins')
d.basic('What are vitamins?', 'Organic compounds needed in ' + T('small amounts') + ' in diet for specific functions; deficiency causes specific diseases')
d.basic('Origin of the word vitamin?', '"Vital amine"; the "e" was dropped since most lack amino groups')
d.basic('Fat-soluble vitamins?', T('A, D, E, K') + ': stored in liver and adipose tissue')
d.basic('Water-soluble vitamins?', T('B group and C') + ': excreted in urine, must be supplied regularly (except ' + T('B₁₂') + ', which is stored)')
d.basic('Mnemonic for fat-soluble vitamins?', '"' + T('ADEK') + '": all Dissolve Easily in (K)fat')
d.basic('Why can’t vitamin C be stored? (Intext 10.6)', 'Water-soluble: ' + X('excreted in urine'))
d.basic('Table 10.3: vitamins, sources, deficiencies', 'Vitamins A–D', **fig('tab_10_3_vitamins_a'))
d.cloze('Deficiencies: A → {{c1::xerophthalmia, night blindness}}; B₁ → {{c2::beri beri}}; B₂ → {{c3::cheilosis}}; B₆ → {{c4::convulsions}}; B₁₂ → {{c5::pernicious anaemia}}.')
d.cloze('Deficiencies: C → {{c1::scurvy (bleeding gums)}}; D → {{c2::rickets, osteomalacia}}; E → {{c3::fragile RBCs, muscular weakness}}; K → {{c4::increased blood clotting time}}.')
d.cloze('Chemical names: B₁ = {{c1::thiamine}}; B₂ = {{c2::riboflavin}}; B₆ = {{c3::pyridoxine}}; C = {{c4::ascorbic acid}}.')
d.basic('Sources of vitamins D, E, K?', 'D: ' + T('sunlight') + ', fish, egg yolk. E: vegetable oils (wheat germ, sunflower). K: green leafy vegetables.', **fig('tab_10_3_vitamins_b'))

# ---------------------------------------------------------------- 10.5 Nucleic acids
d.sec('10.5-nucleic-acids')
d.basic('What carries heredity in the nucleus?', T('Chromosomes') + ': proteins + nucleic acids (DNA, RNA)')
d.basic('Why are nucleic acids called polynucleotides?', 'Long-chain polymers of ' + T('nucleotides'))
d.basic('Complete hydrolysis of DNA/RNA gives?', 'Pentose sugar + phosphoric acid + nitrogenous ' + T('bases'))
d.basic('Sugar in DNA vs RNA?', 'DNA: ' + T('β-D-2-deoxyribose') + '. RNA: ' + T('β-D-ribose') + '.', **fig('fig_ribose_deoxyribose'))
d.basic('Bases in DNA vs RNA?', 'DNA: A, G, C, ' + T('T') + '. RNA: A, G, C, ' + T('U') + ' (uracil replaces thymine).', **fig('fig_bases'))
d.basic('Purines vs pyrimidines? (teacher addition)', T('Purines') + ' (two rings): A, G. ' + T('Pyrimidines') + ' (one ring): C, T, U.')
d.basic('Nucleoside vs nucleotide?', 'Nucleoside: base at ' + T('1′') + ' of sugar. Nucleotide: nucleoside + phosphate at ' + T('5′') + '.', **fig('fig_10_5_nucleoside_nucleotide'))
d.basic('Linkage between nucleotides?', T('Phosphodiester') + ' between 5′ and 3′ carbons of the sugars', **fig('fig_10_6_dinucleotide'))
d.basic('Simplified nucleic acid chain?', 'Sugar–phosphate backbone with bases on the sugars', **fig('fig_nucleic_chain'))
d.basic('Primary structure of a nucleic acid?', 'The ' + T('sequence of nucleotides'))
d.basic('Watson–Crick model of DNA?', T('Double helix') + ': two chains H-bonded via base pairs; strands ' + T('complementary'), **fig('fig_10_7_dna_helix'))
d.basic('Base pairing in DNA?', T('A = T') + ' and ' + T('C ≡ G'))
d.basic('Secondary structure of RNA?', T('Single-stranded') + ' helix that sometimes folds back')
d.basic('Three types of RNA?', T('m-RNA, r-RNA, t-RNA'))
d.basic('Why are RNA base ratios unrelated? (Intext 10.8)', 'RNA is ' + T('single-stranded') + ': no complementary pairing')
d.basic('Hydrolysis of a DNA nucleotide containing thymine? (Intext 10.7)', T('2-Deoxyribose, phosphoric acid, thymine'))
d.basic('Watson facts (box)?', 'Nobel 1962 with ' + T('Crick and Wilkins') + ' for the double helix: "a gently twisted ladder"')
d.basic('Biological functions of nucleic acids?', 'DNA: reserve of genetic information, ' + T('self-duplication') + '. RNA: ' + T('protein synthesis') + ' (message from DNA).')
d.basic('Har Gobind Khorana?', 'Born 1922; Nobel 1968 (with Nirenberg and Holley) for ' + T('cracking the genetic code'))
d.basic('Uses of DNA fingerprinting?', 'Forensics, ' + T('paternity') + ', identifying dead bodies, racial groups and evolution')

# ---------------------------------------------------------------- 10.6 Hormones
d.sec('10.6-hormones')
d.basic('What are hormones?', T('Intercellular messengers') + ' from endocrine glands, carried by blood')
d.cloze('Hormone types: steroids = {{c1::estrogens, androgens}}; polypeptides = {{c2::insulin, endorphins}}; amino acid derivatives = {{c3::epinephrine, norepinephrine}}.')
d.basic('Insulin vs glucagon?', T('Insulin') + ' lowers blood glucose; ' + T('glucagon') + ' raises it: together they regulate it')
d.basic('Thyroxine: nature and disorders?', 'Iodinated derivative of ' + T('tyrosine') + '; low → hypothyroidism (lethargy, obesity, goitre); high → hyperthyroidism; iodised salt prevents it')
d.basic('Adrenal cortex hormones?', T('Glucocorticoids') + ': carbohydrate metabolism, inflammation, stress. ' + T('Mineralocorticoids') + ': water and salt excretion.')
d.basic('Addison’s disease?', 'Adrenal cortex failure: hypoglycaemia, weakness, stress susceptibility; treated with glucocorticoids + mineralocorticoids')
d.basic('Sex hormones?', T('Testosterone') + ' (male characters), ' + T('estradiol') + ' (female characters, menstrual cycle), ' + T('progesterone') + ' (prepares uterus)')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Compare', 'DNA vs RNA?', [
    ('Sugar', 'Deoxyribose  |  ribose', False), ('Bases', 'A G C T  |  A G C U', False), ('Strands', 'Double helix  |  single', False),
    ('Function', 'Heredity, replication  |  protein synthesis', False)], term='DNA vs RNA')
table_card(d, 'Polysaccharides', 'Monomer and linkage?', [
    ('Amylose', 'α-glucose, C1–C4, unbranched', False), ('Amylopectin', 'α-glucose, C1–C4 + C1–C6 branches', False),
    ('Glycogen', 'α-glucose, more branched', False), ('Cellulose', 'β-glucose, C1–C4, straight', False)], term='Starch, glycogen and cellulose')

n = d.write(os.path.join(OUT, 'deck.json'))
print(n, 'cards')
