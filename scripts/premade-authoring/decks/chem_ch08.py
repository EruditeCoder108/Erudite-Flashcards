import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch08-organic-chemistry-basic-principles')
d = Deck('Chapter 8: Organic Chemistry – Some Basic Principles and Techniques', 'Class 11', ['class-11', 'chemistry', 'ch-8'])
d.description = 'Hybridisation, structural formulas, classification, IUPAC naming, isomerism, reaction intermediates, electronic effects, purification and analysis'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
CC = (790, 1001)

# ---------------------------------------------------------------- 8.1 Intro
d.sec('8.1-general-introduction')
d.basic('What property of carbon makes organic chemistry possible?', T('Catenation') + ': forming covalent bonds with other carbon atoms')
d.basic('Who proposed the "vital force" theory?', T('Berzelius') + ' (Swedish chemist): organic compounds need a vital force of living things')
d.basic('Correction: NCERT spells the vital-force chemist "Berzilius". Correct spelling?', T('Jöns Jacob Berzelius'))
d.basic('Who disproved vital force, and how?', T('F. Wöhler') + ' (1828): made ' + T('urea') + ' from inorganic ammonium cyanate: NH₄CNO → NH₂CONH₂')
d.basic('Who synthesised acetic acid and methane from inorganic sources?', 'Acetic acid: ' + T('Kolbe') + ' (1845). Methane: ' + T('Berthelot') + ' (1856).')

# ---------------------------------------------------------------- 8.2 Tetravalence
d.sec('8.2-tetravalence-and-shapes')
table_card(d, 'Hybridisation of carbon', 'Shape and example?', [
    ('sp³ (25% s)', 'Tetrahedral: methane CH₄', False), ('sp² (33% s)', 'Trigonal planar: ethene C₂H₄', False),
    ('sp (50% s)', 'Linear: ethyne C₂H₂', False)], term='Hybridisation and shape')
d.basic('How does s character affect bond length, strength and electronegativity?', 'More s character → orbital ' + T('closer to nucleus') + ': shorter, stronger bonds<br>' + T('Higher electronegativity') + ' (sp > sp² > sp³)')
d.basic('Why is rotation about C=C restricted?', 'Rotation would destroy the ' + T('sideways overlap') + ' of parallel p orbitals (π bond)')
d.basic('Where is the π electron cloud, and why is it reactive?', 'Above and below the molecular plane: ' + T('easily available') + ' to attacking reagents')
d.basic('In H₂C=CH₂, are all atoms coplanar?', T('Yes') + ': p orbitals must be parallel, perpendicular to the molecular plane')
d.basic('σ and π bonds in HC≡CCH=CHCH₃ and CH₂=C=CHCH₃? (Problem 8.1)', '(a) ' + N('10 σ, 3 π') + '. (b) ' + N('9 σ, 2 π') + '.')
d.basic('Hybridisation of each C in CH₃CH=CH₂? in CH₂=C=O? (Problem 8.2 style)', 'CH₃: sp³; =CH–, =CH₂: sp². Cumulated C in CH₂=C=O: ' + T('sp'))
d.basic('Hybridisation and shape: H₂C=O, CH₃F, HC≡N? (Problem 8.3)', 'sp² trigonal planar; sp³ tetrahedral; sp linear')

# ---------------------------------------------------------------- 8.3 Structural representations
d.sec('8.3-structural-representations')
d.basic('Complete vs condensed structural formula?', T('Complete') + ': every bond shown as a dash<br>' + T('Condensed') + ': dashes omitted, identical groups by subscripts, e.g. CH₃(CH₂)₆CH₃')
d.basic('Rules of bond-line formulas?', 'C and H ' + X('not shown') + '; zig-zag lines; each junction and terminal is a carbon (terminal = CH₃ unless a group is shown); heteroatoms written')
d.basic('Condensed formula of HOCH₂CH₂CH₂CH(CH₃)CH(CH₃)CH₃ style chains?', 'Group repeated units: e.g. HO(CH₂)₃CH(CH₃)CH(CH₃)₂')
d.basic('Wedge-and-dash convention?', T('Solid wedge') + ': bond towards the viewer. ' + T('Dashed wedge') + ': bond away. Plain line: in the plane.', **fig('fig_8_1_wedge_dash'))
d.basic('Three kinds of molecular models?', T('Framework') + ' (bonds only)<br>' + T('Ball-and-stick') + ' (atoms and bonds)<br>' + T('Space-filling') + ' (relative size from van der Waals radii)', **fig('fig_8_2_models'))
d.basic('Model used for C=C compounds like ethene?', T('Ball-and-spring') + ' model')

# ---------------------------------------------------------------- 8.4 Classification
d.sec('8.4-classification')
d.basic('Acyclic (aliphatic) compounds: examples?', 'Open chain: ' + E('ethane, isobutane, acetaldehyde, acetic acid'))
d.basic('Alicyclic compounds: define with examples.', 'Carbon atoms in a ' + T('ring') + ' with aliphatic properties: ' + E('cyclopropane, cyclohexane, cyclohexene'))
d.basic('Homocyclic vs heterocyclic?', T('Homocyclic') + ': ring of carbon only. ' + T('Heterocyclic') + ': ring has other atoms, e.g. ' + E('tetrahydrofuran') + '.')
d.basic('Benzenoid aromatic examples?', E('Benzene, aniline, naphthalene'))
d.basic('Non-benzenoid aromatic example in NCERT?', E('Tropone'))
d.basic('Heterocyclic aromatic examples?', E('Furan, thiophene, pyridine'))
d.basic('Define a functional group.', 'An atom or group of atoms joined to the carbon chain that decides the ' + T('characteristic chemical properties') + ' (–OH, –CHO, –COOH)')
d.basic('Define a homologous series.', 'Compounds with the same functional group, a ' + T('general formula') + ', successive members differing by ' + T('–CH₂–'))

# ---------------------------------------------------------------- 8.5 Nomenclature
d.sec('8.5-nomenclature')
d.basic('Origin of the common names citric acid and formic acid?', 'Citric: from ' + T('citrus fruits') + '. Formic: Latin ' + T('formica') + ' = ant (red ant).')
d.basic('Why "buckminsterfullerene" for C₆₀?', 'Its shape resembles the ' + T('geodesic domes') + ' of architect R. Buckminster Fuller')
d.basic('Common names of (CH₃)₄C, HCHO, (CH₃)₂CO, CHCl₃?', 'Neopentane, formaldehyde, ' + T('acetone') + ', chloroform', **fig('tab_8_1_common_names'))
d.basic('Common names of C₆H₅OCH₃, C₆H₅NH₂, C₆H₅COCH₃, CH₃OCH₂CH₃?', T('Anisole, aniline, acetophenone') + ', ethyl methyl ether')
d.basic('Old name for alkanes and its meaning?', T('Paraffins') + ': Latin "little affinity"')
d.basic('Names of C₁ to C₁₀, C₂₀ and C₃₀ straight-chain alkanes?', 'Methane … decane; ' + T('icosane') + ' (C₂₀); ' + T('triacontane') + ' (C₃₀)', **fig('tab_8_2_alkanes'))
d.basic('How is an alkyl group named?', 'Remove one H from an alkane; replace "-ane" by ' + T('"-yl"') + ' (CH₄ → –CH₃ methyl)', **fig('tab_8_3_alkyl_groups'))
d.basic('Structures of isopropyl, sec-butyl, isobutyl, tert-butyl, neopentyl?', '(CH₃)₂CH–; CH₃CH₂CH(CH₃)–; (CH₃)₂CHCH₂–; (CH₃)₃C–; ' + T('(CH₃)₃CCH₂–'))
d.cloze('Branched alkanes: choose the {{c1::longest chain}}; number to give branches the {{c2::lowest locants}}; list substituents in {{c3::alphabetical}} order; di/tri/tetra are {{c4::ignored}} in alphabetising.')
d.basic('Two substituents in equivalent positions: which gets the lower number?', 'The one coming ' + T('first alphabetically') + ' (3-ethyl-6-methyloctane, not 6-ethyl-3-methyl)')
d.basic('Which prefixes count in alphabetising: iso, neo, sec, tert?', T('iso and neo count') + ' (part of the name); ' + X('sec and tert do not'))
d.basic('Two chains of equal length: which is parent?', 'The one with ' + T('more side chains'))
d.basic('How is a branched substituent numbered and written?', 'Its carbon attached to the parent is ' + T('C-1') + '; its name goes in ' + T('parentheses') + ', e.g. 5-(2,2-dimethylpropyl)nonane')
d.basic('How are cycloalkanes named?', 'Prefix ' + T('"cyclo"') + ' to the straight-chain alkane name')
d.cloze('Priority of functional groups: –COOH > –SO₃H > {{c1::–COOR}} > –COCl > {{c2::–CONH₂}} > –CN > {{c3::–CHO}} > >C=O > {{c4::–OH}} > –NH₂ > C=C > C≡C.')
d.basic('Groups always written as prefixes?', T('–R, halogens (F, Cl, Br, I), –NO₂, –OR'))
d.basic('Name HOCH₂(CH₂)₃CH₂COCH₃ correctly.', T('7-Hydroxyheptan-2-one') + ' (keto outranks hydroxyl), not 2-oxoheptan-7-ol')
d.basic('Name HOCH₂CH₂OH and CH₂=CH–CH=CH₂.', T('Ethane-1,2-diol') + ' (full "ethane" kept); ' + T('buta-1,3-diene') + ' ("n" of -ane dropped)')
d.basic('Name BrCH₂CH=CH₂.', T('3-Bromoprop-1-ene') + ' (double bond gets the lower number, not 1-bromoprop-2-ene)')
d.basic('Name CH₃COCH₂CH₂CH₂COOH. (Problem 8.8 style)', T('5-Oxohexanoic acid') + ': acid is principal, C-1 is the –COOH carbon')
d.basic('Structure of 2-chlorohexane and hex-2-ene-type names? (Problem 8.9)', '2-Chlorohexane: CH₃CHClCH₂CH₂CH₂CH₃. Pent-4-en-2-ol: CH₂=CHCH₂CH(OH)CH₃.')
d.basic('In 3-nitrocyclohex-1-ene, why is C=C numbered before –NO₂?', 'C=C is a ' + T('suffix') + ' group; –NO₂ is only a prefix')
d.basic('Is the –CHO carbon counted in the parent chain?', T('Yes') + ' (5-hydroxyheptanal includes the CHO carbon as C-1)')
d.basic('Full functional group table (Table 8.4)?', 'Class, group, prefix, suffix and example for each family', **fig('tab_8_4_functional_groups'))
d.basic('IUPAC names of toluene, anisole, aniline?', T('Methylbenzene, methoxybenzene, benzenamine (aminobenzene)'))
d.basic('ortho, meta, para = which positions?', 'o = ' + N('1,2') + '; m = ' + N('1,3') + '; p = ' + N('1,4'))
d.basic('Can o/m/p be used for trisubstituted benzenes?', X('No') + ': use lowest locants')
d.basic('Name the benzene ring as a substituent.', T('Phenyl') + ' (C₆H₅–, Ph)')
d.basic('Correct: 1-chloro-2,4-dinitrobenzene or 4-chloro-1,3-dinitrobenzene?', T('1-Chloro-2,4-dinitrobenzene') + ' (lowest locants, then alphabetical)')

# ---------------------------------------------------------------- 8.6 Isomerism
d.sec('8.6-isomerism')
d.basic('Define isomerism.', 'Two or more compounds with the ' + T('same molecular formula') + ' but different properties')
table_card(d, 'Structural isomerism', 'Example?', [
    ('Chain', 'C₅H₁₂: pentane, isopentane, neopentane', False), ('Position', 'C₃H₈O: propan-1-ol, propan-2-ol', False),
    ('Functional group', 'C₃H₆O: propanal and propanone', False), ('Metamerism', 'C₄H₁₀O: methoxypropane and ethoxyethane', False)], term='Types of structural isomerism')
d.basic('What is metamerism?', 'Different ' + T('alkyl chains on either side') + ' of the functional group')
d.basic('Define stereoisomers and their two types.', 'Same constitution and bond sequence, different ' + T('arrangement in space') + ': ' + T('geometrical and optical'))

# ---------------------------------------------------------------- 8.7 Mechanism
d.sec('8.7-reaction-mechanism')
d.basic('Substrate vs reagent?', T('Substrate') + ': supplies carbon to the new bond. ' + T('Reagent') + ': the attacking species.')
d.basic('Define reaction mechanism.', 'Step-by-step account of ' + T('electron movement') + ', energetics of bond breaking/forming and rates')
d.basic('Heterolytic vs homolytic cleavage?', T('Heterolytic') + ': shared pair goes to one fragment → ions. ' + T('Homolytic') + ': one electron to each → free radicals.')
d.basic('What is a carbocation and its old name?', 'Carbon with a ' + T('sextet') + ' and positive charge; formerly ' + T('carbonium ion'))
d.basic('Stability order of carbocations?', T('3° > 2° > 1° > CH₃⁺') + ': (CH₃)₃C⁺ > (CH₃)₂CH⁺ > CH₃CH₂⁺ > CH₃⁺')
d.basic('Shape and hybridisation of a carbocation?', T('Trigonal planar, sp²') + '; empty p orbital perpendicular to the plane', **fig('fig_8_3a_carbocation'))
d.basic('What is a carbanion, and its shape?', 'Carbon with a negative charge (lone pair); ' + T('sp³') + ', distorted tetrahedral', **fig('fig_8_3b_carbanion'))
d.basic('Correction: NCERT calls the methyl carbanion a "distorted tetrahedron". Better description?', T('Trigonal pyramidal') + ' (like NH₃): the lone pair occupies the fourth sp³ position')
d.basic('Stability order of alkyl free radicals?', T('3° > 2° > 1° > methyl'))
d.basic('Arrow for single-electron movement?', 'Half-headed "' + T('fish-hook') + '" curved arrow')
d.basic('Other names for reactions via heterolysis and homolysis?', 'Heterolysis: ' + T('ionic / polar') + '. Homolysis: ' + T('free radical / non-polar') + '.')
d.basic('Define nucleophile and electrophile.', T('Nucleophile') + ' (Nu:, "nucleus-seeking"): brings an electron pair. ' + T('Electrophile') + ' (E⁺): takes an electron pair.')
d.basic('Examples of nucleophiles?', E('HO⁻, NC⁻, R₃C⁻') + '; neutral with lone pairs: ' + E('H₂O, R₃N, R₂NH'))
d.basic('Examples of electrophiles?', E('Carbocations, carbonyl carbon (>C=O), carbon of alkyl halides (R₃C–X)'))
d.basic('Classify HS⁻, BF₃, C₂H₅O⁻, (CH₃)₃N, Cl⁺, CH₃C⁺=O, H₂N⁻, NO₂⁺. (Problem 8.12)', 'Nucleophiles: ' + T('HS⁻, C₂H₅O⁻, (CH₃)₃N, H₂N⁻') + '. Electrophiles: ' + T('BF₃, Cl⁺, CH₃C⁺=O, NO₂⁺') + '.')
d.basic('Electrophilic centre in CH₃CH=O, CH₃CN, CH₃I? (Problem 8.13)', 'The ' + T('carbon') + ' bonded to O, N or I (partial positive charge)')

d.sec('8.7.4-electronic-effects')
d.basic('Permanent vs temporary electron displacement effects?', 'Permanent: ' + T('inductive, resonance') + ' (and hyperconjugation). Temporary: ' + T('electromeric') + ' (only when a reagent attacks).')
d.basic('Define the inductive effect.', 'Polarisation of a σ bond caused by the polarisation of an ' + T('adjacent σ bond'))
d.basic('How far does the inductive effect reach?', 'Falls off rapidly; ' + X('negligible after three bonds'))
d.basic('Electron-withdrawing (−I) groups in NCERT?', E('Halogens, –NO₂, –CN, –COOH, –COOR, –OAr'))
d.basic('Electron-donating (+I) groups?', T('Alkyl groups') + ': –CH₃, –CH₂CH₃')
d.basic('More polar bond: H₃C–H or H₃C–Br; H₃C–NH₂ or H₃C–OH; H₃C–OH or H₃C–SH? (Problem 8.14)', T('C–Br') + '; ' + T('C–O') + '; ' + T('C–O'))
d.basic('Why isn’t benzene’s Kekulé structure adequate?', 'All C–C bonds are equal (' + N('139 pm') + '), between C–C (154 pm) and C=C (134 pm)')
d.basic('What are resonance (canonical) structures?', T('Hypothetical') + ' structures that individually represent no real molecule; the real one is a ' + T('hybrid'))
d.basic('Nitromethane N–O bonds?', 'Both the ' + T('same length') + ', intermediate between N–O and N=O: a resonance hybrid')
d.basic('Define resonance energy.', 'Energy difference between the actual hybrid and the ' + T('lowest-energy') + ' canonical structure')
d.cloze('Resonance structures must have the same positions of {{c1::nuclei}} and the same number of {{c2::unpaired electrons}}.')
d.basic('Which resonance structure is most stable?', 'More ' + T('covalent bonds') + '<br>All ' + T('octets') + ' complete<br>Less charge separation<br>Negative charge on the more electronegative atom<br>More dispersal')
d.basic('Define the resonance (mesomeric) effect.', 'Polarity from interaction of two π bonds, or a π bond with a ' + T('lone pair') + ' on an adjacent atom.<br>It is transmitted through the chain')
d.basic('+R groups?', E('Halogen, –OH, –OR, –OCOR, –NH₂, –NHR, –NR₂, –NHCOR') + ' (push electrons into the ring: aniline)')
d.basic('−R groups?', E('–COOH, –CHO, >C=O, –CN, –NO₂') + ' (pull electrons: nitrobenzene)')
d.basic('What is a conjugated system?', 'Alternate single and double bonds: ' + E('buta-1,3-diene, aniline, nitrobenzene') + '; π electrons delocalised')
d.basic('Define the electromeric effect.', T('Complete transfer') + ' of π electrons to one atom of a multiple bond on demand of an attacking reagent; ' + X('temporary'))
d.basic('+E vs −E effect?', T('+E') + ': π electrons move to the atom the reagent attaches to. ' + T('−E') + ': to the atom it does not attach to.')
d.basic('Inductive and electromeric effects in opposite directions: which wins?', T('Electromeric'))
d.basic('Define hyperconjugation.', 'Delocalisation of ' + T('σ electrons of C–H') + ' of an alkyl group into an adjacent unsaturated system or empty p orbital.<br>It is permanent', **fig('fig_8_4a_hyperconj_cation'))
d.basic('Why is (CH₃)₃C⁺ more stable than CH₃CH₂⁺, and CH₃⁺ least? (Problem 8.19)', '(CH₃)₃C⁺ has ' + N('9') + ' C–H bonds for hyperconjugation; CH₃⁺’s C–H bonds lie ' + X('perpendicular') + ' to its empty p orbital')
d.basic('Other name for hyperconjugation?', T('No-bond resonance'), **fig('fig_8_4b_hyperconj_propene'))
d.basic('Mnemonic for which effects need a reagent? (intuition)', '"' + T('E for Emergency') + '": the Electromeric effect switches on only when a reagent arrives')
d.basic('Four types of organic reactions?', T('Substitution, addition, elimination, rearrangement'))

# ---------------------------------------------------------------- 8.8 Purification
d.sec('8.8-purification')
d.basic('How is purity finally checked?', 'Sharp ' + T('melting or boiling point') + ' (now also chromatography and spectroscopy)')
d.basic('Sublimation is used for?', 'Separating ' + T('sublimable') + ' compounds from non-sublimable impurities')
d.basic('Principle of crystallisation?', 'Difference in ' + T('solubility') + ': compound sparingly soluble cold, well soluble hot')
d.basic('What is the mother liquor?', 'The filtrate left after crystallisation; contains ' + T('impurities') + ' and a little compound')
d.basic('How are coloured impurities removed during crystallisation?', 'Adsorption on ' + T('activated charcoal'))
d.basic('Simple distillation is used for?', 'Volatile liquids from non-volatile impurities<br>Or liquids with ' + T('large b.p. difference') + ' (chloroform 334 K and aniline 457 K)', **fig('fig_8_5_simple_distillation'))
d.basic('When is fractional distillation used?', 'When b.p. difference is ' + T('small') + '; vapours pass through a fractionating column', **fig('fig_8_6_fractional_distillation'))
d.basic('What is a theoretical plate?', 'Each successive condensation–vaporisation unit in a ' + T('fractionating column'), **fig('fig_8_7_fractionating_columns'))
d.basic('Industrial use of fractional distillation?', 'Separating fractions of ' + T('crude oil'))
d.basic('Distillation under reduced pressure is used for?', 'Liquids with very high b.p. or that ' + T('decompose') + ' below their b.p.; e.g. ' + E('glycerol from spent-lye') + ' (soap industry)', **fig('fig_8_8_reduced_pressure'))
d.basic('Steam distillation is used for?', 'Substances that are ' + T('steam volatile and immiscible with water') + ', e.g. ' + E('aniline'), **fig('fig_8_9_steam_distillation'))
d.basic('Why does a steam-distilled liquid boil below 373 K?', 'It boils when ' + T('p₁ + p₂ = atmospheric pressure') + '; p₁ < p, so below its own b.p.')
d.basic('Differential extraction: principle and apparatus?', 'Organic compound shaken with an ' + T('immiscible organic solvent') + ' in which it is more soluble; ' + T('separatory funnel'), **fig('fig_8_10_differential_extraction'))
d.basic('What if the compound is poorly soluble in the organic solvent?', T('Continuous extraction') + ': same solvent reused repeatedly')
d.basic('Origin of the word chromatography?', 'Greek "' + T('chroma') + '" = colour: first used for plant pigments')
d.basic('Two main types of chromatography by principle?', T('Adsorption') + ' and ' + T('partition'))
d.basic('Common adsorbents?', T('Silica gel') + ' and ' + T('alumina'))
d.occlusion('Figure 8.11 · Column chromatography', M + 'fig_8_11_column_chromatography.webp', CC, [
    ('Solvent', [74, 230, 168, 58], True), ('Mixture of compounds (a+b+c)', [12, 308, 266, 164], True),
    ('Adsorbent (stationary phase)', [22, 530, 264, 166], True), ('Glass wool', [36, 758, 250, 60], True)])
d.basic('In column chromatography, where do strongly adsorbed substances stay?', 'Near the ' + T('top') + ' of the column; the liquid that flows down is the ' + T('eluant'))
d.basic('Define Rf value.', r'\( R_f = \frac{distance \; moved \; by \; substance}{distance \; moved \; by \; solvent} \)' + ' (both from base line)', **fig('fig_8_12_tlc'))
d.basic('TLC plate: coating and thickness?', 'Silica gel or alumina, about ' + N('0.2 mm') + ' on glass (chromaplate)')
d.basic('How are colourless spots on TLC detected?', T('UV light') + ' (fluorescence), ' + T('iodine') + ' jar (brown spots), or spray reagent: ' + T('ninhydrin') + ' for amino acids')
d.basic('Paper chromatography: stationary and mobile phases?', 'Stationary: ' + T('water trapped in the paper') + '. Mobile: the solvent rising by capillary action.', **fig('fig_8_13_paper_chromatography'))
d.basic('Is paper chromatography adsorption or partition?', T('Partition'))

# ---------------------------------------------------------------- 8.9 Qualitative
d.sec('8.9-qualitative-analysis')
d.basic('Detection of C and H?', 'Heat with ' + T('CuO') + ': CO₂ turns lime water milky; H₂O turns anhydrous CuSO₄ ' + T('blue'))
d.basic('What is Lassaigne’s test?', 'Fuse with ' + T('sodium') + ' to convert N, S, X into NaCN, Na₂S, NaX; boil with water = sodium fusion extract')
d.basic('Test for nitrogen?', 'Extract + FeSO₄, boil, acidify with conc. H₂SO₄ → ' + T('Prussian blue') + ' Fe₄[Fe(CN)₆]₃·xH₂O')
d.basic('Tests for sulphur?', 'Acetic acid + lead acetate → ' + T('black PbS') + '; sodium nitroprusside → ' + T('violet'))
d.basic('N and S both present: what forms and what colour?', T('NaSCN') + ': with Fe³⁺ gives ' + T('blood red') + ' [Fe(SCN)]²⁺; no Prussian blue')
d.basic('How does excess sodium change the N+S result?', 'NaSCN + 2Na → NaCN + Na₂S: normal tests for N and S appear')
table_card(d, 'Halogen test (AgNO₃ after HNO₃)', 'Precipitate?', [
    ('Chlorine', 'White, soluble in NH₄OH', False), ('Bromine', 'Yellowish, sparingly soluble', False),
    ('Iodine', 'Yellow, insoluble in NH₄OH', True)], term='Lassaigne test for halogens')
d.basic('Why boil the extract with conc. HNO₃ before the halogen test?', 'To decompose ' + T('NaCN and Na₂S') + ', which would interfere with AgNO₃')
d.basic('Test for phosphorus?', 'Oxidise with Na₂O₂ to phosphate; HNO₃ + ' + T('ammonium molybdate') + ' → yellow ammonium phosphomolybdate')

# ---------------------------------------------------------------- 8.10 Quantitative
d.sec('8.10-quantitative-analysis')
d.basic('Estimation of C and H: absorbers?', 'Water in anhydrous ' + T('CaCl₂') + '; CO₂ in conc. ' + T('KOH') + ' U-tubes', **fig('fig_8_14_c_h_estimation'))
d.basic('Formulas for %C and %H (m₁ = CO₂, m₂ = H₂O, m = sample)?', r'\( \%C = \frac{12 \times m_1 \times 100}{44 \times m} \)' + '; ' + r'\( \%H = \frac{2 \times m_2 \times 100}{18 \times m} \)')
d.basic('0.246 g gave 0.198 g CO₂ and 0.1014 g H₂O. %C, %H? (Problem 8.20)', 'C = ' + N('21.95%') + '; H = ' + N('4.58%'))
d.basic('Dumas method in brief?', 'Heat with ' + T('CuO in CO₂') + '; N oxides reduced on hot copper gauze; collect N₂ over ' + T('KOH') + ' (absorbs CO₂)', **fig('fig_8_15_dumas'))
d.basic('%N formula in Dumas method?', r'\( \%N = \frac{28 \times V_{STP} \times 100}{22400 \times m} \)' + '; pressure = atmospheric − aqueous tension')
d.basic('0.3 g gave 50 mL N₂ at 300 K, 715 mm (aq. tension 15 mm). %N? (Problem 8.21)', 'V(STP) = 41.9 mL → ' + N('17.46%'))
d.basic('Kjeldahl method in brief?', 'Heat with conc. ' + T('H₂SO₄') + ' → (NH₄)₂SO₄; add NaOH; NH₃ absorbed in excess standard acid; back-titrate', **fig('fig_8_16_kjeldahl'))
d.basic('%N formula in Kjeldahl method?', r'\( \%N = \frac{1.4 \times M \times 2(V - V_1/2)}{m} \)')
d.basic('Kjeldahl is NOT applicable to?', X('Nitro, azo compounds and ring N (pyridine)') + ': their N does not form (NH₄)₂SO₄')
d.basic('NH₃ from 0.5 g neutralised 10 mL of 1 M H₂SO₄. %N? (Problem 8.22)', '= 20 mL 1 M NH₃ → 0.28 g N → ' + N('56.0%'))
d.basic('Carius method for halogens?', 'Heat with ' + T('fuming HNO₃ + AgNO₃') + ' in a Carius tube; weigh AgX', **fig('fig_8_17_carius'))
d.basic('%X formula (Carius)?', r'\( \%X = \frac{atomic \; mass \; of \; X \times m_1 \times 100}{molar \; mass \; of \; AgX \times m} \)')
d.basic('0.15 g gave 0.12 g AgBr. %Br? (Problem 8.23)', '80 × 0.12 × 100 / (188 × 0.15) = ' + N('34.04%'))
d.basic('Estimation of sulphur?', 'Heat with Na₂O₂ or fuming HNO₃ in Carius tube → H₂SO₄ → weigh as ' + T('BaSO₄') + ': %S = 32 m₁ × 100 / (233 m)')
d.basic('0.157 g gave 0.4813 g BaSO₄. %S? (Problem 8.24)', N('42.10%'))
d.basic('Estimation of phosphorus?', 'Oxidise to H₃PO₄, then weigh as either:<br>' + T('ammonium phosphomolybdate') + ' (%P = 31 m₁ × 100 / 1877 m)<br>' + T('Mg₂P₂O₇') + ' (62 m₁ × 100 / 222 m)')
d.basic('How is oxygen usually estimated?', 'By ' + T('difference') + ' from 100%')
d.basic('Direct oxygen estimation?', 'Heat in N₂; pass over red-hot coke (→ CO); then warm ' + T('I₂O₅') + ': 5CO + I₂O₅ → I₂ + 5CO₂. %O = 32 m₁ × 100 / (88 m).')
d.basic('Modern instrument for C, H, N?', T('CHN elemental analyser') + ' (needs only 1–3 mg)')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Summary', 'Effect and type?', [
    ('Inductive', 'Permanent; σ bonds; fades after 3 bonds', False), ('Resonance (mesomeric)', 'Permanent; π/lone pair delocalisation', False),
    ('Electromeric', 'Temporary; needs attacking reagent', True), ('Hyperconjugation', 'Permanent; σ(C–H) delocalisation', False)], term='Electronic effects summary')
table_card(d, 'Summary', 'Purification method?', [
    ('Glycerol from spent-lye', 'Reduced-pressure distillation', False), ('Aniline from water', 'Steam distillation', False),
    ('Chloroform + aniline', 'Simple distillation', False), ('Crude oil fractions', 'Fractional distillation', False),
    ('Plant pigments', 'Chromatography', False)], term='Which purification technique?')

n = d.write(os.path.join(OUT, 'deck.json'))
print(n, 'cards')
