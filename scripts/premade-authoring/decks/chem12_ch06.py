import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch06-haloalkanes-and-haloarenes')
d = Deck('Chapter 6: Haloalkanes and Haloarenes', 'Class 12', ['class-12', 'chemistry', 'ch-6'])
d.description = 'Classification, naming, preparation, SN1 and SN2, stereochemistry, elimination, Grignard and Wurtz, haloarene reactions, polyhalogen compounds'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- intro
d.sec('6.0-introduction')
d.basic('Haloalkane vs haloarene: hybridisation of the C bearing X?', 'Haloalkane: ' + T('sp³') + ' (alkyl). Haloarene: ' + T('sp²') + ' (aryl).')
d.cloze('Useful halogen compounds: {{c1::chloramphenicol}} treats typhoid; {{c2::thyroxine}} (iodine hormone), deficiency causes goiter; {{c3::chloroquine}} treats malaria; {{c4::halothane}} is an anaesthetic.')
d.basic('Fully fluorinated compounds are being considered as?', T('Blood substitutes') + ' in surgery')
d.basic('Why do halogenated compounds persist in the environment?', 'Resist breakdown by ' + X('soil bacteria'))

# ---------------------------------------------------------------- 6.1 Classification
d.sec('6.1-classification')
d.basic('Classification by number of halogens?', T('Mono-, di-, poly-') + 'halogen compounds', **fig('fig_mono_di_tri'))
d.basic('General formula of alkyl halides?', r'\( C_nH_{2n+1}X \)')
d.basic('1°, 2°, 3° alkyl halides?', 'X on a carbon attached to ' + N('1, 2, 3') + ' other carbons', **fig('fig_alkyl_1_2_3'))
d.basic('What is an allylic halide?', 'X on an ' + T('sp³ carbon next to a C=C') + ' (allylic carbon)', **fig('fig_allylic'))
d.basic('What is a benzylic halide?', 'X on an ' + T('sp³ carbon attached to an aromatic ring') + ' (1°, 2°, 3° possible)', **fig('fig_benzylic'))
d.basic('What is a vinylic halide?', 'X on an ' + T('sp² carbon of a C=C'), **fig('fig_vinylic'))
d.basic('What is an aryl halide?', 'X ' + T('directly bonded') + ' to an sp² carbon of an aromatic ring', **fig('fig_aryl'))
table_card(d, 'Classify', 'Type of halide?', [
    ('CH₂=CH–CH₂Cl', 'Allylic', False), ('C₆H₅CH₂Cl', 'Benzylic', False), ('CH₂=CHCl', 'Vinylic', True), ('C₆H₅Cl', 'Aryl', True),
    ('(CH₃)₃CCl', 'Alkyl, 3°', False)], note='sp³ C–X: alkyl, allylic, benzylic. sp² C–X: vinylic, aryl.', term='Classify halides by the carbon holding X')

# ---------------------------------------------------------------- 6.2 Nomenclature
d.sec('6.2-nomenclature')
d.basic('Common vs IUPAC naming of alkyl halides?', 'Common: ' + T('alkyl group + halide') + ' (ethyl chloride). IUPAC: ' + T('halo-substituted alkane') + ' (chloroethane).')
d.basic('gem- vs vic-dihalides?', T('gem') + ': both X on the ' + T('same carbon') + ' (alkylidene halides). ' + T('vic') + ': X on ' + T('adjacent') + ' carbons (alkylene dihalides).')
d.basic('Common and IUPAC names of CH₃CHCl₂ and ClCH₂CH₂Cl?', 'Ethylidene chloride = ' + T('1,1-dichloroethane') + '; ethylene dichloride = ' + T('1,2-dichloroethane'))
d.cloze('IUPAC names: sec-butyl chloride = {{c1::2-chlorobutane}}; neo-pentyl bromide = {{c2::1-bromo-2,2-dimethylpropane}}; tert-butyl bromide = {{c3::2-bromo-2-methylpropane}}.')
d.cloze('IUPAC names: vinyl chloride = {{c1::chloroethene}}; allyl bromide = {{c2::3-bromopropene}}; benzyl chloride = {{c3::chlorophenylmethane}}; o-chlorotoluene = {{c4::1-chloro-2-methylbenzene}}.')
d.cloze('IUPAC names: methylene chloride = {{c1::dichloromethane}}; chloroform = {{c2::trichloromethane}}; bromoform = {{c3::tribromomethane}}; carbon tetrachloride = {{c4::tetrachloromethane}}.')
d.basic('Table 6.1: common and IUPAC names', 'Table 6.1', **fig('tab_6_1_names'))
d.basic('How many structural isomers of C₅H₁₁Br? (Example 6.1)', N('8') + ':<br>1-bromopentane (1°)<br>2-bromopentane (2°)<br>3-bromopentane (2°)<br>1-bromo-3-methylbutane (1°)<br>2-bromo-3-methylbutane (2°)<br>2-bromo-2-methylbutane (3°)<br>1-bromo-2-methylbutane (1°)<br>1-bromo-2,2-dimethylpropane (1°)')
d.basic('Dihalo naming in benzene: common vs IUPAC?', 'Common: ' + T('o-, m-, p-') + '. IUPAC: ' + T('1,2-, 1,3-, 1,4-') + ' (e.g. m-dibromobenzene = 1,3-dibromobenzene)')

# ---------------------------------------------------------------- 6.3 C-X bond
d.sec('6.3-nature-of-c-x-bond')
d.basic('Polarity of the C–X bond?', 'C is ' + T('δ+') + ', X is ' + T('δ−') + ' (X more electronegative)')
d.basic('Trend of C–X bond length and bond enthalpy from F to I?', 'Length ' + T('increases') + ' (139 → 214 pm); enthalpy ' + X('decreases') + ' (452 → 234 kJ/mol)', **fig('tab_6_2_cx_bond'))
d.basic('Trap: which CH₃X has the highest dipole moment?', T('CH₃Cl (1.860 D)') + ' > CH₃F (1.847) > CH₃Br > CH₃I: F is most electronegative but the C–F bond is very short')

# ---------------------------------------------------------------- 6.4 Preparation of haloalkanes
d.sec('6.4.1-from-alcohols')
d.basic('Reagents to convert R–OH to R–X?', 'Conc. ' + T('HX') + ', ' + T('PX₃ / PCl₅') + ', ' + T('SOCl₂'), **fig('fig_alcohol_to_halide'))
d.basic('Why is SOCl₂ preferred for alkyl chlorides?', 'By-products ' + T('SO₂ and HCl are gases') + ' and escape, leaving pure R–Cl')
d.basic('Catalyst for 1° and 2° alcohols with HCl? And 3° alcohols?', 'Anhydrous ' + T('ZnCl₂') + ' (conc. HCl + anhyd. ZnCl₂ = Lucas reagent). 3°: just shake with conc. HCl at room temperature.')
d.basic('How are alkyl bromides and iodides made from alcohols?', 'Bromide: constant-boiling ' + T('48% HBr') + ' (or NaBr + H₂SO₄). Iodide: heat with ' + T('NaI/KI in 95% H₃PO₄') + '.')
d.basic('Reactivity order of alcohols with a haloacid?', T('3° > 2° > 1°'))
d.basic('How are PBr₃ and PI₃ used?', 'Generated ' + T('in situ') + ' from red P + Br₂ / I₂')
d.basic('Why isn’t H₂SO₄ used with KI to make alkyl iodides? (Intext 6.2)', 'H₂SO₄ ' + X('oxidises HI to I₂') + '; non-oxidising H₃PO₄ is used instead')
d.basic('Why can’t aryl halides be made from phenols this way?', 'The C–O bond of phenol has ' + T('partial double bond') + ' character and is hard to break')

d.sec('6.4.2-from-hydrocarbons')
d.basic('Why is free-radical halogenation of alkanes a poor method?', 'Gives a ' + X('complex mixture') + ' of isomeric mono- and polyhalides, hard to separate; low yield')
d.basic('Monochloro isomers from free-radical chlorination of (CH₃)₂CHCH₂CH₃? (Example 6.3)', N('4') + ': (CH₃)₂CHCH₂CH₂Cl, (CH₃)₂CHCHClCH₃, (CH₃)₂CClCH₂CH₃, CH₃CH(CH₂Cl)CH₂CH₃')
d.basic('C₅H₁₂ isomers giving 1, 3, 4 monochlorides? (Intext 6.4)', '1: ' + T('neopentane') + ' (CH₃)₄C. 3: ' + T('n-pentane') + '. 4: ' + T('isopentane') + ' (2-methylbutane).')
d.basic('HBr + propene: major product and rule?', T('2-Bromopropane') + ' (Markovnikov); HI similarly gives CH₃CHICH₃ as major')
d.basic('Br₂ in CCl₄ + alkene: product and use?', T('vic-Dibromide') + ' (colourless); discharge of red-brown colour is a ' + T('test for C=C'))

d.sec('6.4.3-halogen-exchange')
d.basic('Finkelstein reaction?', 'R–Cl/R–Br + ' + T('NaI in dry acetone') + ' → R–I + NaCl/NaBr')
d.basic('Why does Finkelstein go to completion?', 'NaCl/NaBr ' + T('precipitates') + ' in dry acetone (NaI is soluble), pulling equilibrium forward (Le Chatelier)')
d.basic('Swarts reaction?', 'R–Cl/R–Br heated with a metallic fluoride (' + T('AgF, Hg₂F₂, CoF₂, SbF₃') + ') → R–F')
d.basic('Mnemonic: Finkelstein vs Swarts?', T('F') + 'inkelstein gives iodide (not F!); ' + T('S') + 'warts gives fluoride. "Swarts = Super-reactive F."')

# ---------------------------------------------------------------- 6.5 Haloarenes
d.sec('6.5-preparation-of-haloarenes')
d.basic('Electrophilic halogenation of toluene: conditions and products?', 'X₂ with ' + T('Fe / FeCl₃') + ' in dark → ' + T('o- and p-halotoluene'), **fig('fig_arene_halogenation'))
d.basic('Why are o- and p-isomers easy to separate?', 'Large difference in ' + T('melting points'))
d.basic('Why does iodination need HNO₃ or HIO₄?', 'Iodination is ' + T('reversible') + '; the oxidant removes HI')
d.basic('Why can’t fluoroarenes be made by direct fluorination?', 'Fluorine is ' + X('too reactive'))
d.basic('Sandmeyer reaction?', 'ArNH₂ + NaNO₂ + HX (273–278 K) → ArN₂⁺X⁻; then ' + T('Cu₂Cl₂ / Cu₂Br₂') + ' → ArCl / ArBr + N₂', **fig('fig_sandmeyer'))
d.basic('How is iodobenzene made from a diazonium salt?', 'Shake with ' + T('KI') + ' (no cuprous halide needed)', **fig('fig_diazonium_ki'))

# ---------------------------------------------------------------- 6.6 Physical properties
d.sec('6.6-physical-properties')
d.basic('Colour and smell of alkyl halides?', 'Colourless when pure; ' + T('bromides and iodides colour') + ' on exposure to light; many volatile ones smell sweet')
d.basic('Which haloalkanes are gases at room temperature?', 'Methyl chloride, methyl bromide, ethyl chloride, some chlorofluoromethanes')
d.basic('Why are b.p. of haloalkanes higher than hydrocarbons of similar mass?', 'Greater ' + T('polarity') + ' and mass → stronger dipole–dipole and van der Waals forces')
d.basic('Order of b.p. for the same alkyl group?', T('RI > RBr > RCl > RF') + ' (bigger halogen, stronger van der Waals)', **fig('fig_6_1_boiling_points'))
d.basic('Effect of branching on b.p. of isomeric haloalkanes?', 'More branching → ' + X('lower') + ' b.p. (2-bromo-2-methylpropane lowest of its isomers)')
d.basic('Why does p-dichlorobenzene melt higher than o- and m-?', 'Its ' + T('symmetry') + ' fits the crystal lattice better (b.p. nearly the same)')
d.basic('Increasing b.p.: bromomethane, bromoform, chloromethane, dibromomethane? (Intext 6.6)', 'Chloromethane < bromomethane < dibromomethane < bromoform')
d.basic('Increasing b.p.: 1-chloropropane, isopropyl chloride, 1-chlorobutane?', 'Isopropyl chloride < 1-chloropropane < 1-chlorobutane')
d.basic('Why are haloalkanes barely soluble in water?', 'Energy released by new haloalkane–water attractions is ' + X('less') + ' than that needed to break water’s H-bonds')
d.basic('Why do haloalkanes dissolve in organic solvents?', 'New attractions are of ' + T('similar strength') + ' to those broken')
d.basic('Which halo derivatives are denser than water? Trend?', 'Bromo, iodo and polychloro; density rises with more C, more X and heavier X', **fig('tab_6_3_density'))

# ---------------------------------------------------------------- 6.7 Reactions of haloalkanes
d.sec('6.7.1-nucleophilic-substitution')
d.basic('Three categories of haloalkane reactions?', T('Nucleophilic substitution') + ', ' + T('elimination') + ', ' + T('reaction with metals'))
d.basic('What is nucleophilic substitution?', 'A nucleophile attacks the δ+ carbon and replaces X, which leaves as ' + T('halide ion') + ' (leaving group)')
d.basic('Products with common nucleophiles (Table 6.4)?', 'OH⁻ → alcohol; R′O⁻ → ether; NH₃ → amine; CN⁻ → nitrile; AgCN → isonitrile; KNO₂ → alkyl nitrite; AgNO₂ → nitroalkane; R′COOAg → ester; LiAlH₄ → alkane', **fig('tab_6_4_nucleophiles'))
d.cloze('R–X + KCN → {{c1::R–CN (nitrile)}}; R–X + AgCN → {{c2::R–NC (isonitrile)}}.')
d.cloze('R–X + KNO₂ → {{c1::R–O–N=O (alkyl nitrite)}}; R–X + AgNO₂ → {{c2::R–NO₂ (nitroalkane)}}.')
d.basic('What is an ambident nucleophile? Examples?', 'Has two nucleophilic centres: ' + E('CN⁻') + ' (C or N), ' + E('NO₂⁻') + ' (O or N)')
d.basic('Why KCN gives nitriles but AgCN gives isocyanides? (Example 6.5)', 'KCN is ' + T('ionic') + ': free CN⁻ attacks via C (C–C more stable). AgCN is ' + T('covalent') + ': C is bonded to Ag, so N donates.')

d.sec('6.7.1a-sn2')
d.basic('SN2: kinetics and example?', T('Second order') + ': rate depends on both [CH₃Cl] and [OH⁻]; CH₃Cl + OH⁻ → CH₃OH + Cl⁻')
d.basic('SN2 mechanism?', 'One step, ' + T('no intermediate') + ': OH⁻ attacks from the back as C–Cl breaks.<br>The transition state has C bonded to five groups', **fig('fig_6_2_sn2'))
d.basic('What happens to configuration in SN2, and the analogy?', T('Inversion') + ', like an ' + T('umbrella turned inside out') + ' in a strong wind', **fig('fig_6_2_balls'))
d.basic('Transition state of SN2: arrangement of the three C–H bonds?', 'All three in ' + T('one plane') + '; Nu and X partly bonded on opposite sides')
d.basic('Who proposed the SN2 mechanism (1937)?', T('Hughes and Ingold'))
d.basic('What is configuration?', 'Spatial arrangement of groups around a carbon; (A) and (B) are mirror-image configurations', **fig('fig_configuration_box'))
d.basic('Relative SN2 rates of methyl, ethyl (1°), isopropyl (2°), tert-butyl (3°) halides?', N('30 : 1 : 0.02 : ~0') + ': bulky groups block back-side attack', **fig('fig_6_3_steric_sn2'))
d.basic('SN2 reactivity order?', T('CH₃X > 1° > 2° > 3°') + ' (steric hindrance)')
d.basic('Intuition: why is SN2 so sensitive to bulk?', 'The nucleophile must reach the ' + T('back of the carbon') + ', like knocking on a door crowded by bodyguards.<br>Three methyl groups block it completely')

d.sec('6.7.1b-sn1')
d.basic('SN1: solvent, kinetics, example?', 'Polar protic solvent (water, alcohol, acetic acid); ' + T('first order') + ' in (CH₃)₃CBr only', **fig('fig_sn1_overall'))
d.basic('SN1 mechanism steps?', 'Step I (' + T('slow, reversible') + '): C–Br breaks → carbocation + Br⁻. Step II (fast): Nu⁻ attacks the carbocation.', **fig('fig_sn1_mechanism'))
d.basic('Where does the energy for C–Br cleavage in SN1 come from?', T('Solvation') + ' of the halide ion by the protic solvent')
d.basic('SN1 reactivity order and reason?', T('3° > 2° > 1° > CH₃X') + ': stability of the carbocation')
d.basic('SN1 vs SN2 reactivity orders together?', 'Opposite directions', **fig('fig_sn_reactivity_order'))
d.basic('Why are allylic and benzylic halides very reactive in SN1?', 'Their carbocations are ' + T('resonance-stabilised'), **fig('fig_allyl_benzyl_resonance'))
d.basic('Order of R–X for the same alkyl group (both mechanisms)?', T('R–I > R–Br > R–Cl ≫ R–F') + ' (weakest C–X, best leaving group first)')
d.basic('Which undergoes SN2 faster: cyclohexylmethyl chloride or chlorocyclohexane? 1-iodo vs 1-chloro? (Example 6.6)', 'The ' + T('primary') + ' (CH₂Cl) one; the ' + T('iodide') + ' (I⁻ better leaving group)')
d.basic('Four isomeric bromobutanes: SN1 order? (Example 6.7)', '(CH₃)₃CBr > CH₃CH₂CHBrCH₃ > (CH₃)₂CHCH₂Br > CH₃CH₂CH₂CH₂Br; ' + T('SN2 is the reverse'))
d.basic('Why is (CH₃)₂CHCH₂Br faster than n-butyl bromide in SN1?', 'Greater +I effect of (CH₃)₂CH– stabilises the carbocation')
d.basic('SN1 order: C₆H₅CH₂Br, C₆H₅CH(CH₃)Br, C₆H₅CH(C₆H₅)Br, C₆H₅C(CH₃)(C₆H₅)Br?', 'C₆H₅C(CH₃)(C₆H₅)Br > C₆H₅CH(C₆H₅)Br > C₆H₅CH(CH₃)Br > C₆H₅CH₂Br; SN2 reverse (phenyl bulkier than methyl)')
d.basic('Faster SN2: CH₃CH₂CH₂CH₂Br or CH₃CH₂CHBrCH₃? (Intext 6.7)', T('CH₃CH₂CH₂CH₂Br') + ' (1°)')
d.basic('Faster SN2: (CH₃)₂CHCH₂CH₂Br or CH₃CH₂CH(CH₃)CH₂Br?', T('(CH₃)₂CHCH₂CH₂Br') + ': branching is farther from the reacting carbon')
table_card(d, 'Compare', 'SN1 or SN2?', [
    ('Steps', 'SN1: two (carbocation)  |  SN2: one', False), ('Kinetics', 'SN1: first order  |  SN2: second order', False),
    ('Best substrate', 'SN1: 3°, allylic, benzylic  |  SN2: CH₃, 1°', False), ('Solvent', 'SN1: polar protic', False),
    ('Stereochemistry', 'SN1: racemisation  |  SN2: inversion', True)], term='SN1 vs SN2 at a glance')

d.sec('6.7.1c-stereochemistry')
d.basic('What is optical activity? d vs l?', 'Rotation of plane-polarised light (polarimeter). ' + T('d (+)') + ': clockwise; ' + T('l (−)') + ': anticlockwise.')
d.basic('Who made the first polarising prism?', T('William Nicol') + ' (Nicol prism)')
d.basic('Pasteur’s contribution (1848)?', 'Mirror-image crystals whose solutions rotated light ' + T('equally but oppositely') + ': foundation of stereochemistry')
d.basic('Van’t Hoff and Le Bel (1874)?', 'Tetrahedral carbon; four different groups → ' + T('non-superimposable mirror images'))
d.basic('What is an asymmetric carbon (stereocentre)?', 'A carbon with ' + T('four different groups'))
d.basic('Chiral vs achiral?', T('Chiral') + ': non-superimposable on its mirror image (like hands), optically active. ' + T('Achiral') + ': superimposable.', **fig('fig_6_4_chiral_objects'))
d.basic('Is propan-2-ol chiral? Why?', X('Achiral') + ': C-2 has two identical CH₃ groups; rotated mirror image superimposes', **fig('fig_6_5_propan2ol'))
d.basic('Is butan-2-ol chiral?', T('Chiral') + ': four different groups (H, OH, CH₃, C₂H₅)', **fig('fig_6_6_butan2ol'))
d.basic('Chiral molecules listed by NCERT?', E('2-chlorobutane, 2,3-dihydroxypropanal, BrClCHI, 2-bromopropanoic acid'), **fig('fig_6_7_chiral_molecule'))
d.basic('What are enantiomers? How do they differ?', 'Non-superimposable mirror images; identical m.p., b.p., refractive index; differ only in ' + T('direction of rotation') + ' of plane-polarised light')
d.basic('Is the sign of rotation related to configuration?', X('No') + ': (+)/(−) is not tied to the absolute configuration')
d.basic('What is a racemic mixture?', T('Equal amounts') + ' of two enantiomers; zero rotation; written (±) or dl, e.g. (±)-butan-2-ol')
d.basic('What is racemisation?', 'Conversion of an enantiomer into a ' + T('racemic mixture'))
d.basic('What is retention of configuration?', 'Spatial arrangement at the stereocentre is ' + T('preserved') + '; happens if no bond to the stereocentre is broken')
d.basic('(−)-2-Methylbutan-1-ol + HCl gives (+)-1-chloro-2-methylbutane. What does this show?', T('Retention') + ' of configuration though the ' + X('sign of rotation changed'), **fig('fig_retention_example'))
d.basic('Three outcomes when a bond to a stereocentre breaks?', 'Only A: ' + T('retention') + '; only B: ' + T('inversion') + '; 50:50: ' + T('racemisation'), **fig('fig_retention_inversion'))
d.basic('SN2 of (−)-2-bromooctane with NaOH gives?', T('(+)-Octan-2-ol') + ' with ' + T('inverted') + ' configuration (OH enters opposite to Br)', **fig('fig_sn2_inversion_octane'))
d.basic('Why does SN1 give racemisation?', 'The carbocation is ' + T('sp², planar') + ': Nu attacks from either face equally → (±) product.<br>e.g. 2-bromobutane → (±)-butan-2-ol', **fig('fig_sn1_racemisation'))
d.basic('Intuition: why does a flat carbocation lose "handedness"?', 'A flat plate looks the same from above and below.<br>The nucleophile can’t tell which face was the original, so both products form')

d.sec('6.7.1d-elimination')
d.basic('What is β-elimination (dehydrohalogenation)?', 'Heat with ' + T('alcoholic KOH') + ': H from β-carbon and X from α-carbon are removed → alkene', **fig('fig_beta_elimination'))
d.basic('α- vs β-carbon?', 'α: carbon bearing X. β: the ' + T('adjacent') + ' carbon.')
d.basic('Saytzeff (Zaitsev) rule?', 'The preferred alkene has ' + T('more alkyl groups') + ' on the doubly bonded carbons')
d.basic('2-Bromopentane + alc. KOH: products?', T('Pent-2-ene (81%)') + ' major, pent-1-ene (19%)', **fig('fig_zaitsev'))
d.basic('Elimination vs substitution: what decides?', 'Nature of halide, ' + T('strength and size of base/nucleophile') + ', conditions. Bulky base → elimination.', **fig('fig_elim_vs_sub'))
d.cloze('Typical routes: 1° halide → {{c1::SN2}}; 2° halide → {{c2::SN2 or elimination}}; 3° halide → {{c3::SN1 or elimination}}.')
d.basic('Aqueous KOH vs alcoholic KOH with R–X?', 'Aqueous: ' + T('substitution') + ' → alcohol (OH⁻ nucleophile). Alcoholic: ' + T('elimination') + ' → alkene (RO⁻ acts as base).')

d.sec('6.7.1e-reaction-with-metals')
d.basic('What are Grignard reagents? Preparation?', T('RMgX') + ' (Victor Grignard, 1900): R–X + Mg in ' + T('dry ether'))
d.basic('Nature of bonds in RMgX?', 'C–Mg ' + T('covalent but highly polar') + ' (C is δ−); Mg–X essentially ionic')
d.basic('RMgX + H₂O gives?', T('RH') + ' + Mg(OH)X: any proton source (water, alcohol, amine) converts it to a hydrocarbon')
d.basic('Why must Grignard reactions be moisture-free?', 'Even traces of water ' + X('destroy RMgX') + ' (RMgX + H₂O → RH)')
d.basic('Grignard trivia (box)?', 'Took a maths degree first; Nobel 1912 shared with ' + T('Paul Sabatier') + ' (Ni-catalysed hydrogenation)')
d.basic('Wurtz reaction?', '2R–X + 2Na in ' + T('dry ether') + ' → R–R + 2NaX (doubles the carbon count)')

# ---------------------------------------------------------------- 6.7.2 Haloarenes
d.sec('6.7.2-haloarene-nucleophilic-substitution')
d.basic('Why are aryl halides far less reactive to nucleophilic substitution? (4 reasons)', '(i) ' + T('Resonance') + ': partial C=Cl double bond. (ii) ' + T('sp² carbon') + ' holds C–X tighter. (iii) ' + T('Phenyl cation unstable') + ' (no SN1). (iv) Electron-rich Nu repelled by electron-rich ring.')
d.basic('Resonance in chlorobenzene?', 'Cl lone pair delocalises into the ring, giving C–Cl ' + T('partial double bond character'), **fig('fig_haloarene_resonance'))
d.basic('C–Cl bond length in haloalkane vs haloarene?', N('177 pm') + ' vs ' + N('169 pm') + ' (sp² C more electronegative)', **fig('fig_sp2_sp3_carbon'))
d.basic('Dow process: chlorobenzene → phenol conditions?', 'NaOH at ' + N('623 K') + ' and ' + N('300 atm') + ', then H⁺', **fig('fig_dow_process'))
d.basic('Effect of –NO₂ at o-/p- on nucleophilic substitution of chlorobenzene?', T('Easier') + ': 4-nitro at 443 K; 2,4-dinitro at 368 K', **fig('fig_nitro_activation'))
d.basic('2,4,6-Trinitrochlorobenzene + warm water gives?', T('2,4,6-Trinitrophenol (picric acid)'), **fig('fig_picric'))
d.basic('Why does –NO₂ activate only at o- and p-?', 'The carbanion’s negative charge lands on the carbon bearing –NO₂ only for ' + T('o/p') + ', where –NO₂ stabilises it.<br>At meta it never does', **fig('fig_nitro_mechanism'))
d.basic('Intuition: more NO₂ groups, milder conditions?', 'Each NO₂ is an extra "sponge" for the negative charge: 623 K → 443 K → 368 K → warm water')

d.sec('6.7.2-haloarene-electrophilic-substitution')
d.basic('Halogen on benzene: activating or deactivating? Directing?', T('Slightly deactivating') + ' but ' + T('o,p-directing'))
d.basic('Why is halogen o,p-directing?', 'Resonance raises electron density at ' + T('o and p') + ' positions', **fig('fig_halobenzene_resonance'))
d.basic('Chlorobenzene + Cl₂ / anhyd. FeCl₃?', T('1,4-Dichlorobenzene') + ' (major) + 1,2-dichlorobenzene (minor)', **fig('fig_chlorobenzene_halogenation'))
d.basic('Chlorobenzene + conc. HNO₃ / H₂SO₄?', T('1-Chloro-4-nitrobenzene') + ' (major) + 1-chloro-2-nitrobenzene (minor)', **fig('fig_chlorobenzene_nitration'))
d.basic('Chlorobenzene + conc. H₂SO₄ (heat)?', T('4-Chlorobenzenesulfonic acid') + ' (major) + 2- (minor)', **fig('fig_chlorobenzene_sulphonation'))
d.basic('Chlorobenzene Friedel–Crafts with CH₃Cl and CH₃COCl (anhyd. AlCl₃)?', T('1-Chloro-4-methylbenzene') + ' and ' + T('4-chloroacetophenone') + ' (major, para)', **fig('fig_chlorobenzene_friedel_crafts'))
d.basic('Why is Cl deactivating yet o,p-directing? (Example 6.9)', T('–I effect') + ' (stronger) controls ' + T('reactivity') + '; ' + T('+R effect') + ' controls ' + T('orientation') + ' (stabilises o/p carbocation)', **fig('fig_ex69_directing'))
d.basic('Mnemonic for halogens on benzene?', '"Halogens are ' + T('bad hosts but good guides') + '": they slow the reaction (−I) yet point the electrophile to o/p (+R)')

d.sec('6.7.2-haloarene-reaction-with-metals')
d.basic('Wurtz–Fittig reaction?', 'Alkyl halide + aryl halide + Na in dry ether → ' + T('alkylarene'), **fig('fig_wurtz_fittig'))
d.basic('Fittig reaction?', '2 Aryl halide + 2Na in dry ether → ' + T('diaryl') + ' (e.g. diphenyl)', **fig('fig_fittig'))
table_card(d, 'Name reactions', 'Name?', [
    ('R–X + NaI (dry acetone) → R–I', 'Finkelstein', False), ('R–X + AgF → R–F', 'Swarts', False), ('ArN₂⁺ + CuCl → ArCl', 'Sandmeyer', False),
    ('2R–X + 2Na → R–R', 'Wurtz', False), ('R–X + ArX + 2Na → Ar–R', 'Wurtz–Fittig', False), ('2ArX + 2Na → Ar–Ar', 'Fittig', False)],
    term='Name reactions of Chapter 6')

# ---------------------------------------------------------------- 6.8 Polyhalogen
d.sec('6.8-polyhalogen-compounds')
d.basic('Uses of dichloromethane?', 'Paint remover, aerosol propellant, process solvent for drugs, metal cleaning')
d.basic('Health effects of CH₂Cl₂?', 'Harms the ' + T('central nervous system') + ': impaired hearing/vision; dizziness, nausea, numbness; burns skin and cornea')
d.basic('Uses of chloroform?', 'Solvent for fats, alkaloids, iodine; mainly to make ' + T('freon R-22') + '; formerly an anaesthetic')
d.basic('Why is chloroform stored in closed dark bottles, filled to the top?', 'Air + light oxidise it to poisonous ' + T('phosgene (COCl₂)') + ': 2CHCl₃ + O₂ → 2COCl₂ + 2HCl')
d.basic('Update: NCERT says chloroform was replaced by ether as anaesthetic. Today?', 'Ether is also obsolete.<br>Modern inhaled anaesthetics are halogenated ethers like ' + T('sevoflurane, isoflurane') + ' (halothane has largely been phased out)')
d.basic('Effects of chloroform exposure?', '900 ppm: dizziness, fatigue, headache. Chronic: ' + T('liver') + ' (metabolised to phosgene) and kidney damage')
d.basic('Iodoform: former use and why antiseptic?', 'Antiseptic; action due to ' + T('liberated iodine') + ', not iodoform itself; replaced due to smell')
d.basic('Uses of CCl₄?', 'Refrigerants, aerosol propellants, feedstock for CFCs, pharmaceuticals, solvent<br>Formerly: cleaning fluid, spot remover, ' + T('fire extinguisher'))
d.basic('Hazards of CCl₄?', 'Possible ' + T('liver cancer') + ', nerve damage, irregular heartbeat; ' + X('depletes ozone'))
d.basic('What are freons? Freon 12?', 'Chlorofluorocarbons of methane and ethane: stable, non-toxic, easily liquefiable.<br>' + T('Freon 12 = CCl₂F₂') + ', made by the Swarts reaction from CCl₄')
d.basic('Why are freons harmful?', 'They reach the ' + T('stratosphere') + ' unchanged and start radical chain reactions that deplete ozone')
d.basic('DDT: full name and discovery?', T('p,p′-Dichlorodiphenyltrichloroethane') + '; made 1873, insecticidal action found by ' + T('Paul Müller') + ' (1939; Nobel 1948)', **fig('fig_ddt'))
d.basic('Why was DDT banned (USA, 1973)?', 'Insect resistance, toxic to fish, very stable and ' + T('fat-soluble') + ': accumulates in fatty tissue (biomagnification)')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Summary', 'Reagent gives?', [
    ('R–OH + SOCl₂', 'R–Cl + SO₂ + HCl', False), ('R–X + alc. KOH', 'Alkene (Saytzeff)', False), ('R–X + aq. KOH', 'Alcohol', False),
    ('R–X + Mg (dry ether)', 'RMgX', False), ('ArCl + NaOH, 623 K, 300 atm', 'Phenol', False), ('ArCl + Cl₂/FeCl₃', 'o- and p-dichlorobenzene', False)],
    term='Key reactions of Chapter 6')

n = d.write(os.path.join(OUT, 'deck.json'))
print(n, 'cards')
