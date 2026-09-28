import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase as sc

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch05-coordination-compounds')
d = Deck('Chapter 5: Coordination Compounds', 'Class 12', ['class-12', 'chemistry', 'ch-5'])
d.description = 'Werner’s theory, ligands and terms, IUPAC names, isomerism, VBT, crystal field splitting, colour, metal carbonyls and applications'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- intro
d.sec('5.0-introduction')
d.basic('Chlorophyll, haemoglobin, vitamin B₁₂: central metals?', T('Mg') + ', ' + T('Fe') + ', ' + T('Co'))
d.basic('Other uses of coordination compounds (intro)?', 'Metallurgy, industrial catalysts, analytical reagents, ' + T('electroplating') + ', textile dyeing, medicine')

# ---------------------------------------------------------------- 5.1 Werner
d.sec('5.1-werners-theory')
d.basic('What did Werner observe with CoCl₃·xNH₃ and AgNO₃?', 'Different numbers of Cl⁻ precipitated as AgCl in the cold: only ' + T('ionisable') + ' Cl⁻ reacts')
d.cloze('Moles of AgCl per mole: CoCl₃·6NH₃ (yellow) = {{c1::3}}; CoCl₃·5NH₃ (purple) = {{c2::2}}; CoCl₃·4NH₃ (green and violet) = {{c3::1}}.')
d.basic('Werner formulas and electrolyte types for the cobalt ammines?', '[Co(NH₃)₆]Cl₃ 1:3; [CoCl(NH₃)₅]Cl₂ 1:2; [CoCl₂(NH₃)₄]Cl 1:1 (green and violet are isomers)', **fig('tab_5_1_cobalt_ammines'))
d.basic('Intuition: how does AgNO₃ "count" bracket vs outside Cl⁻?', 'Cl⁻ outside the bracket is free in solution and grabs Ag⁺; Cl⁻ inside is ' + T('held by the metal') + ' and can’t')
d.basic('Primary valence (Werner)?', T('Ionisable') + '; satisfied by negative ions (= oxidation state in modern terms)')
d.basic('Secondary valence (Werner)?', T('Non-ionisable') + '; satisfied by neutral molecules or negative ions; = ' + T('coordination number') + ', fixed for a metal')
d.basic('What did Werner say about the secondary linkages’ arrangement?', 'Characteristic ' + T('spatial arrangements') + ' (coordination polyhedra): octahedral, tetrahedral, square planar most common')
d.basic('Shapes: [Co(NH₃)₆]³⁺, [Ni(CO)₄], [PtCl₄]²⁻?', T('Octahedral') + ', ' + T('tetrahedral') + ', ' + T('square planar'))
d.basic('Secondary valences: PdCl₂·4NH₃ (2 AgCl), NiCl₂·6H₂O (2), PtCl₄·2HCl (0), CoCl₃·4NH₃ (1), PtCl₂·2NH₃ (0)? (Example 5.1)', N('4, 6, 6, 6, 4'))
d.basic('Double salt vs complex?', 'Double salts (' + E('carnallite, Mohr’s salt, potash alum') + ') ' + T('dissociate completely') + ' in water; complex ions like [Fe(CN)₆]⁴⁻ ' + X('do not'))
d.basic('Werner facts (box)?', 'Swiss chemist (1866–1919), first to find ' + T('optical activity') + ' in coordination compounds; first Swiss chemist to win the ' + T('Nobel Prize (1913)'))

# ---------------------------------------------------------------- 5.2 Terms
d.sec('5.2-definitions')
d.basic('What is a coordination entity?', 'Central metal atom/ion bonded to a fixed number of ions/molecules, e.g. ' + E('[CoCl₃(NH₃)₃], [Ni(CO)₄], [Fe(CN)₆]⁴⁻'))
d.basic('Central atom/ion in [NiCl₂(H₂O)₄], [CoCl(NH₃)₅]²⁺, [Fe(CN)₆]³⁻?', T('Ni²⁺, Co³⁺, Fe³⁺') + '; they act as ' + T('Lewis acids'))
d.basic('What are ligands?', 'Ions/molecules bound to the central atom: Cl⁻, H₂O, NH₃, en, N(CH₂CH₂NH₂)₃, even proteins; they are ' + T('Lewis bases') + ' (electron-pair donors)')
d.cloze('Denticity: Cl⁻, H₂O, NH₃ are {{c1::unidentate}}; en and C₂O₄²⁻ are {{c2::didentate}}; N(CH₂CH₂NH₂)₃ is {{c3::polydentate}}; EDTA⁴⁻ is {{c4::hexadentate}}.')
d.basic('EDTA⁴⁻ binds through which atoms?', T('2 N + 4 O') + ' (hexadentate)')
d.basic('What is a chelate ligand? Why are chelates more stable?', 'A di/polydentate ligand binding one metal through ≥ 2 donors; ring formation makes chelate complexes ' + T('more stable'))
d.basic('Intuition: why are chelates extra stable?', 'Like a crab’s claw (Greek ' + I('chele') + '): if one "finger" lets go, the other still holds the metal, so it clicks back instead of floating away')
d.basic('What is an ambidentate ligand? Examples?', 'Two different donor atoms, either can bind: ' + E('NO₂⁻') + ' (N or O), ' + E('SCN⁻') + ' (S or N)')
d.basic('Define coordination number.', 'Number of ligand ' + T('donor atoms') + ' directly bonded to the metal (count σ bonds only, ' + X('not π') + ')')
d.basic('CN in [PtCl₆]²⁻, [Ni(NH₃)₄]²⁺, [Fe(C₂O₄)₃]³⁻, [Co(en)₃]³⁺?', N('6, 4, 6, 6') + ' (oxalate and en are didentate)')
d.basic('Trap: CN of [Co(en)₃]³⁺ is 3?', X('No') + ': 3 en × 2 donor atoms = ' + N('6'))
d.basic('Coordination sphere and counter ions in K₄[Fe(CN)₆]?', 'Sphere: ' + T('[Fe(CN)₆]⁴⁻') + '; counter ion: ' + T('K⁺'))
d.basic('What is a coordination polyhedron?', 'Spatial arrangement of donor atoms around the central atom', **fig('fig_5_1_polyhedra'))
d.basic('Oxidation number of the central atom: definition?', 'Charge left on the metal if all ligands are removed with their shared electron pairs; e.g. Cu in [Cu(CN)₄]³⁻ = ' + N('+1') + ', written Cu(I)')
d.basic('Quick method for oxidation number?', 'Charge of complex − sum of ligand charges. [Co(NH₃)₅Cl]²⁺: x − 1 = +2 → ' + N('Co(+3)'))
d.basic('Homoleptic vs heteroleptic?', T('Homoleptic') + ': one kind of donor group, ' + E('[Co(NH₃)₆]³⁺') + '. ' + T('Heteroleptic') + ': more than one kind, ' + E('[Co(NH₃)₄Cl₂]⁺') + '.')

# ---------------------------------------------------------------- 5.3 Nomenclature
d.sec('5.3.1-formulas')
d.cloze('Formula rules: {{c1::central atom}} first; then ligands in {{c2::alphabetical}} order (charge ignored); whole entity in {{c3::square brackets}}; polyatomic ligands in {{c4::parentheses}}.')
d.basic('How is charge written on a complex ion formula?', 'Right superscript outside the bracket, number before sign: ' + E('[Co(CN)₆]³⁻, [Cr(H₂O)₆]³⁺'))
d.sec('5.3.2-naming')
d.basic('Order when naming a complex compound?', T('Cation first') + ', then anion; inside the entity, ligands alphabetically ' + T('before') + ' the metal (reverse of formula writing)')
d.cloze('Ligand names: anionic end in {{c1::-o / -ido}} (chlorido, cyanido); H₂O = {{c2::aqua}}; NH₃ = {{c3::ammine}}; CO = {{c4::carbonyl}}; NO = {{c5::nitrosyl}}.')
d.basic('When are bis, tris, tetrakis used?', 'When the ligand name already has a numerical prefix: ' + E('dichloridobis(triphenylphosphine)nickel(II)') + ' for [NiCl₂(PPh₃)₂]')
d.basic('Metal name in a complex anion?', 'Ends in ' + T('-ate') + ' (cobaltate); Latin names for some: ' + E('ferrate (Fe), cuprate, argentate, aurate, plumbate'))
d.basic('Name [Cr(NH₃)₃(H₂O)₃]Cl₃.', T('triamminetriaquachromium(III) chloride'))
d.basic('Name [Co(H₂NCH₂CH₂NH₂)₃]₂(SO₄)₃.', T('tris(ethane-1,2-diamine)cobalt(III) sulphate'))
d.basic('Name [Ag(NH₃)₂][Ag(CN)₂].', T('diamminesilver(I) dicyanidoargentate(I)') + ': same metal, different name in cation and anion')
d.basic('Formulas (Example 5.2): tetraammineaquachloridocobalt(III) chloride; potassium tetrahydroxidozincate(II); potassium trioxalatoaluminate(III)?', '[Co(NH₃)₄(H₂O)Cl]Cl₂; K₂[Zn(OH)₄]; K₃[Al(C₂O₄)₃]')
d.basic('Formulas: dichloridobis(ethane-1,2-diamine)cobalt(III); tetracarbonylnickel(0)?', '[CoCl₂(en)₂]⁺; [Ni(CO)₄]')
d.basic('Name [Pt(NH₃)₂Cl(NO₂)] and K₃[Cr(C₂O₄)₃]. (Example 5.3)', T('diamminechloridonitrito-N-platinum(II)') + '; ' + T('potassium trioxalatochromate(III)'))
d.basic('Name [CoCl₂(en)₂]Cl and [Co(NH₃)₅(CO₃)]Cl.', T('dichloridobis(ethane-1,2-diamine)cobalt(III) chloride') + '; ' + T('pentaamminecarbonatocobalt(III) chloride'))
d.basic('NCERT names Hg[Co(SCN)₄] as mercury(I) tetrathiocyanato-S-cobaltate(III). Correction?', 'One Hg balancing a 2− anion is ' + T('Hg²⁺') + ', so Co = +2: ' + T('mercury(II) tetrathiocyanato-S-cobaltate(II)') + '. (Check: x + 4(−1) = −2)')
d.basic('Name [Co(NH₃)₆]Cl₃, [Co(NH₃)₅Cl]Cl₂, K₃[Fe(CN)₆]. (Intext 5.2)', 'hexaamminecobalt(III) chloride; pentaamminechloridocobalt(III) chloride; potassium hexacyanidoferrate(III)')
d.basic('Name K₃[Fe(C₂O₄)₃] and K₂[PdCl₄].', 'potassium trioxalatoferrate(III); potassium tetrachloridopalladate(II)')
d.basic('Formula: iron(III) hexacyanidoferrate(II)? (Intext 5.1)', T('Fe₄[Fe(CN)₆]₃') + ' (Prussian blue)')
d.basic('2004 IUPAC draft changes (margin notes)?', 'Anionic ligands end in ' + T('-ido') + ' (chloro → chlorido); ligands sorted alphabetically ' + T('irrespective of charge'))

# ---------------------------------------------------------------- 5.4 Isomerism
d.sec('5.4-isomerism')
d.basic('Two main types of isomerism in coordination compounds?', T('Stereoisomerism') + ' (geometrical, optical) and ' + T('structural') + ' (linkage, coordination, ionisation, solvate)')
d.basic('Stereo vs structural isomers?', 'Stereo: same bonds, different ' + T('spatial arrangement') + '. Structural: ' + T('different bonds') + '.')
d.sec('5.4.1-geometrical')
d.basic('Geometrical isomers of square planar [MX₂L₂]?', T('cis') + ' (X adjacent) and ' + T('trans') + ' (X opposite)', **fig('fig_5_2_cis_trans_pt'))
d.basic('How many isomers for square planar [MABXL]?', N('3') + ': two cis, one trans')
d.basic('Why no geometrical isomers for tetrahedral complexes? (Example 5.4)', 'All four positions are ' + T('adjacent to each other') + ', so relative positions are identical')
d.basic('Identify the isomers of [Co(NH₃)₄Cl₂]⁺.', T('cis') + ' (Cl at 90°) and ' + T('trans') + ' (Cl at 180°)', **img('fig_5_3_cis_trans_co'))
d.basic('Geometrical isomers of [CoCl₂(en)₂]⁺?', T('cis and trans'), **fig('fig_5_4_cis_trans_en'))
d.basic('fac vs mer isomers of [Ma₃b₃] (e.g. [Co(NH₃)₃(NO₂)₃])?', T('fac') + ': three same ligands on one ' + T('face') + '. ' + T('mer') + ': around the ' + T('meridian') + '.', **fig('fig_5_5_fac_mer'))
d.basic('Intuition: telling fac from mer?', 'fac: the three identical ligands form a ' + T('triangle') + ' (all mutually 90°). mer: they lie in a ' + T('line/arc') + ' (one pair at 180°).')
d.basic('Geometrical isomers of [Fe(NH₃)₂(CN)₄]⁻? (Example 5.5)', T('cis and trans') + ' (the two NH₃ adjacent or opposite)', **fig('fig_ex55_fe_isomers'))
d.sec('5.4.2-optical')
d.basic('What are optical isomers (enantiomers)?', 'Non-superimposable ' + T('mirror images') + ' (chiral); d rotates plane-polarised light right, l left')
d.basic('Where is optical isomerism common?', 'Octahedral complexes with ' + T('didentate ligands') + ', e.g. [Co(en)₃]³⁺', **fig('fig_5_6_optical_coen3'))
d.basic('Which isomer of [PtCl₂(en)₂]²⁺ is optically active?', 'Only ' + T('cis') + ' (trans has a mirror plane)', **fig('fig_5_7_optical_ptcl2en2'))
d.basic('Which is chiral: cis- or trans-[CrCl₂(ox)₂]³⁻? (Example 5.6)', T('cis') + '; trans has a plane of symmetry', **fig('fig_ex56_crcl2ox2'))
d.basic('Intuition: quick chirality test for M(AA)₂X₂?', 'Trans: the plane through the two chelates is a mirror → ' + X('achiral') + '. Cis: chelates twist like a propeller → ' + T('chiral'))
d.sec('5.4.3-structural')
d.basic('Linkage isomerism: cause and example?', T('Ambidentate') + ' ligand: [Co(NH₃)₅(NO₂)]Cl₂ is ' + T('red') + ' when bound via O (–ONO), ' + T('yellow') + ' via N (–NO₂) (Jørgensen)')
d.basic('Coordination isomerism: example?', 'Ligands swap between cationic and anionic metals: ' + E('[Co(NH₃)₆][Cr(CN)₆] and [Cr(NH₃)₆][Co(CN)₆]'))
d.basic('Ionisation isomerism: example?', 'Counter ion and a ligand swap: ' + E('[Co(NH₃)₅(SO₄)]Br and [Co(NH₃)₅Br]SO₄'))
d.basic('Test to distinguish [Co(NH₃)₅Cl]SO₄ from [Co(NH₃)₅(SO₄)]Cl? (Intext 5.4)', 'BaCl₂ gives white BaSO₄ only with the first; AgNO₃ gives AgCl only with the second')
d.basic('Solvate (hydrate) isomerism: example?', E('[Cr(H₂O)₆]Cl₃ (violet)') + ' and ' + E('[Cr(H₂O)₅Cl]Cl₂·H₂O (grey-green)') + ': water inside vs outside the sphere')
table_card(d, 'Isomer types', 'Which isomerism?', [
    ('[Co(NH₃)₅(NO₂)]²⁺ vs [Co(NH₃)₅(ONO)]²⁺', 'Linkage', False), ('[Co(NH₃)₆][Cr(CN)₆] vs [Cr(NH₃)₆][Co(CN)₆]', 'Coordination', False),
    ('[Co(NH₃)₅SO₄]Br vs [Co(NH₃)₅Br]SO₄', 'Ionisation', False), ('[Cr(H₂O)₆]Cl₃ vs [Cr(H₂O)₅Cl]Cl₂·H₂O', 'Solvate (hydrate)', False),
    ('cis vs trans-[Co(NH₃)₄Cl₂]⁺', 'Geometrical', True), ('d vs l-[Co(en)₃]³⁺', 'Optical', True)], term='Identify the type of isomerism')
d.basic('Isomerism in [Co(en)₃]Cl₃ and [Co(NH₃)₅(NO₂)](NO₃)₂? (Intext 5.3)', T('Optical') + '; ' + T('linkage') + ' (and ionisation)')

# ---------------------------------------------------------------- 5.5 VBT
d.sec('5.5-bonding')
d.basic('Questions Werner’s theory could not answer?', 'Why only certain elements form complexes; why bonds are ' + T('directional') + '; why complexes have characteristic magnetic and optical properties')
d.sec('5.5.1-valence-bond-theory')
d.basic('Main idea of VBT for complexes?', 'Metal uses (n−1)d, ns, np or ns, np, nd orbitals to form ' + T('hybrid orbitals') + ' of definite geometry; ligands donate electron pairs into them')
table_card(d, 'Table 5.2', 'Geometry?', [
    ('sp³ (CN 4)', 'Tetrahedral', False), ('dsp² (CN 4)', 'Square planar', False), ('sp³d (CN 5)', 'Trigonal bipyramidal', False),
    ('sp³d² (CN 6)', 'Octahedral (outer orbital)', False), ('d²sp³ (CN 6)', 'Octahedral (inner orbital)', False)], term='Hybridisation and geometry')
sc.vbt_inner_outer(d)
d.basic('VBT box diagram for [Co(NH₃)₆]³⁺?', 'd²sp³, inner orbital, low spin, diamagnetic', **fig('fig_vbt_co_nh3_6'))
d.basic('VBT box diagram for [CoF₆]³⁻?', 'sp³d², outer orbital, high spin, paramagnetic', **fig('fig_vbt_cof6'))
d.basic('Inner orbital vs outer orbital complex?', T('Inner') + ' (low spin, spin paired): uses (n−1)d, d²sp³. ' + T('Outer') + ' (high spin, spin free): uses nd, sp³d².')
d.basic('[NiCl₄]²⁻: hybridisation, shape, magnetism?', T('sp³') + ', tetrahedral, ' + T('paramagnetic') + ' (2 unpaired; Ni²⁺ 3d⁸)', **fig('fig_vbt_nicl4'))
d.basic('[Ni(CO)₄]: why tetrahedral but diamagnetic? (Intext 5.6)', 'Ni is in the ' + T('0 state') + ' (3d¹⁰ after CO forces 4s electrons into 3d): no unpaired electrons, sp³')
d.basic('[Ni(CN)₄]²⁻: hybridisation, shape, magnetism?', T('dsp²') + ', square planar, ' + T('diamagnetic') + ' (CN⁻ pairs the 3d⁸ electrons)', **fig('fig_vbt_ni_cn_4'))
d.basic('Unpaired electrons in square planar [Pt(CN)₄]²⁻? (Intext 5.9)', N('0') + ' (Pt²⁺ d⁸, dsp²)')
d.basic('Are hybrid orbitals real?', X('No') + ': hybridisation is a ' + T('mathematical manipulation') + ' of wave equations')

d.sec('5.5.2-magnetic-properties')
d.basic('Why d¹–d³ ions behave the same free and complexed (octahedral)?', 'Two 3d orbitals are ' + T('already vacant') + ' for d²sp³, so no pairing is needed')
d.basic('Why d⁴–d⁶ cause complications?', 'A vacant pair of 3d orbitals needs ' + T('pairing') + ', leaving 2, 1 or 0 unpaired electrons (d⁴, d⁵, d⁶)')
d.cloze('Unpaired electrons: [Mn(CN)₆]³⁻ {{c1::2}} vs [MnCl₆]³⁻ {{c2::4}}; [Fe(CN)₆]³⁻ {{c3::1}} vs [FeF₆]³⁻ {{c4::5}}; [Co(C₂O₄)₃]³⁻ {{c5::0}} vs [CoF₆]³⁻ {{c6::4}}.')
d.basic('Which of those are inner orbital (d²sp³) complexes?', T('[Mn(CN)₆]³⁻, [Fe(CN)₆]³⁻, [Co(C₂O₄)₃]³⁻'))
d.basic('Why is [Fe(H₂O)₆]³⁺ strongly but [Fe(CN)₆]³⁻ weakly paramagnetic? (Intext 5.7)', 'H₂O weak: 5 unpaired (sp³d²). CN⁻ strong: pairs electrons, ' + T('1 unpaired') + ' (d²sp³).')
d.basic('Why is [Co(NH₃)₆]³⁺ inner orbital but [Ni(NH₃)₆]²⁺ outer? (Intext 5.8)', 'Co³⁺ (d⁶) can pair to free two 3d orbitals; Ni²⁺ (d⁸) ' + X('cannot free two 3d') + ', so it must use 4d (sp³d²)')
d.basic('[MnBr₄]²⁻ has μ = 5.9 BM. Geometry? (Example 5.7)', T('Tetrahedral') + ' (sp³): 5 unpaired electrons, so no dsp² pairing')
d.basic('Magnetic moment → structure: the logic?', 'Measure μ → ' + r'\( n \)' + ' from ' + r'\( \mu = \sqrt{n(n+2)} \)' + ' → which orbitals are free → hybridisation and shape')

d.sec('5.5.3-limitations-of-vbt')
d.cloze('Limitations of VBT: many {{c1::assumptions}}; no quantitative {{c2::magnetic}} data; cannot explain {{c3::colour}}; no quantitative stability; can’t predict {{c4::tetrahedral vs square planar}}; doesn’t distinguish {{c5::weak and strong ligands}}.')

# ---------------------------------------------------------------- 5.5.4 CFT
d.sec('5.5.4-crystal-field-theory')
d.basic('Basic assumption of crystal field theory?', 'Metal–ligand bond is purely ' + T('ionic/electrostatic') + '; ligands are ' + T('point charges') + ' (anions) or ' + T('point dipoles') + ' (neutral)')
d.basic('When do d orbitals stay degenerate?', 'In a free ion or a ' + T('spherically symmetric') + ' field; a ligand field is asymmetric and splits them')
sc.d_orbital_pointing(d)
d.basic('What do the orbital labels xy, yz, xz, x²−y², z² tell you?', 'Where the lobes point: ' + T('xy, yz, xz') + ' → between two axes; ' + T('x²−y²') + ' → along x and y; ' + T('z²') + ' → along z (plus a ring)')
d.basic('What do t₂g and e_g mean?', T('t') + ' = triply degenerate (3 orbitals), ' + T('e') + ' = doubly degenerate (2); ' + T('g') + ' (gerade) = symmetric through the centre')
sc.cft_octahedral_split(d)
d.basic('Octahedral splitting diagram (NCERT)?', 'e_g up by 3/5 Δ₀, t₂g down by 2/5 Δ₀', **fig('fig_5_8_octahedral_splitting'))
d.basic('Δ₀ depends on?', 'The ' + T('ligand field strength') + ' and the ' + T('charge on the metal ion'))
d.basic('Spectrochemical series (increasing field strength)?', 'I⁻ < Br⁻ < SCN⁻ < Cl⁻ < S²⁻ < F⁻ < OH⁻ < C₂O₄²⁻ < H₂O < NCS⁻ < edta⁴⁻ < NH₃ < en < CN⁻ < CO')
d.basic('Mnemonic for the spectrochemical series?', '"' + T('I B') + 'ought ' + T('S') + 'ome ' + T('Cl') + 'ean ' + T('S') + 'ocks ' + T('F') + 'or ' + T('O') + 'ld ' + T('C') + 'hildren; ' + T('H') + 'ot ' + T('N') + 'ights ' + T('E') + 'asily ' + T('N') + 'eed ' + T('E') + 'xtra ' + T('C') + 'ozy ' + T('C') + 'overs": I, Br, SCN, Cl, S, F, OH, ox, H₂O, NCS, edta, NH₃, en, CN, CO')
d.basic('Is the spectrochemical series theoretical?', X('No') + ': it is found ' + T('experimentally') + ' from light absorption')
d.basic('Weak vs strong field ligands: the rule of thumb?', T('Halides') + ' at the weak end; ' + T('C-donors (CN⁻, CO)') + ' at the strong end; O-donors weak-ish, N-donors stronger')
d.basic('What is pairing energy P?', 'Energy needed to put two electrons in the ' + T('same orbital'))
d.basic('d⁴ octahedral with Δ₀ < P?', 't₂g³e_g¹: ' + T('weak field, high spin'))
d.basic('d⁴ octahedral with Δ₀ > P?', 't₂g⁴e_g⁰: ' + T('strong field, low spin'))
sc.high_low_spin(d)
d.basic('Which dⁿ configurations are more stable in strong fields (NCERT)?', T('d⁴ to d⁷'))
d.basic('Why can only d⁴–d⁷ be high or low spin (octahedral)?', 'd¹–d³ fill t₂g singly either way; d⁸–d¹⁰ have t₂g full, so the arrangement is forced; only d⁴–d⁷ face the "climb or pair" choice')
d.basic('Mn²⁺: 5 unpaired with H₂O but 1 with CN⁻. Why? (Intext 5.10)', 'H₂O weak (Δ₀ < P): t₂g³e_g² (5 unpaired). CN⁻ strong (Δ₀ > P): ' + T('t₂g⁵') + ' (1 unpaired).')
sc.cft_tetrahedral_split(d)
d.basic('Tetrahedral splitting (NCERT figure)?', 'Inverted; Δt = 4/9 Δ₀', **fig('fig_5_9_tetrahedral_splitting'))
d.basic('Why are low-spin tetrahedral complexes rare?', 'Δt = ' + N('4/9 Δ₀') + ' is too ' + X('small') + ' to force pairing')
d.basic('Why no "g" in tetrahedral labels (e, t₂)?', 'Tetrahedral complexes lack a ' + T('centre of symmetry'))

d.sec('5.5.5-colour')
d.basic('Why is a complex coloured?', 'It absorbs part of visible light; we see the ' + T('complementary colour') + ' (absorbs green → looks red)')
d.basic('Why is [Ti(H₂O)₆]³⁺ violet?', 'Its one d electron jumps ' + T('t₂g → e_g') + ' (d–d transition) by absorbing blue-green light (498 nm)', **fig('fig_5_10_ti_transition'))
d.cloze('Table 5.3: [Co(NH₃)₆]³⁺ absorbs {{c1::blue (475 nm)}}, looks {{c2::yellow-orange}}; [Cu(H₂O)₄]²⁺ absorbs {{c3::red (600 nm)}}, looks {{c4::blue}}; [Co(CN)₆]³⁻ absorbs {{c5::UV (310 nm)}}, looks {{c6::pale yellow}}.')
d.basic('Absorbed vs observed colours (Table 5.3)?', 'Table 5.3', **fig('tab_5_3_colours'))
d.basic('Intuition: why does a stronger ligand shift colour toward yellow?', 'Bigger Δ₀ needs higher-energy (shorter λ, bluer) light; removing blue/violet leaves a ' + T('yellow-orange') + ' look')
d.basic('Why is anhydrous CuSO₄ white but CuSO₄·5H₂O blue?', 'No ligand (water) → ' + X('no splitting') + ' → no d–d transition. Same for [Ti(H₂O)₆]Cl₃ heated.')
d.cloze('Adding en to [Ni(H₂O)₆]²⁺ ({{c1::green}}): 1 en → {{c2::pale blue}}; 2 en → {{c3::blue/purple}}; 3 en ([Ni(en)₃]²⁺) → {{c4::violet}}.')
d.basic('Identify the trend in these tubes.', 'More en replacing H₂O raises Δ₀: [Ni(H₂O)₆]²⁺ green → ' + T('[Ni(en)₃]²⁺ violet'), **img('fig_5_11_ni_en_colours'))
d.basic('Why is ruby red? (box)', 'Al₂O₃ with ' + N('0.5–1%') + ' ' + T('Cr³⁺ (d³)') + ' in octahedral sites: d–d transitions', **fig('fig_5_12_ruby_emerald'))
d.basic('Why is emerald green? (box)', 'Cr³⁺ in octahedral sites of ' + T('beryl Be₃Al₂Si₆O₁₈') + ': bands shift to longer λ (yellow-red, blue), so green is transmitted')

d.sec('5.5.6-limitations-of-cft')
d.basic('Limitations of CFT?', 'Treating ligands as point charges predicts anions should split most, but ' + X('anions are at the weak end') + '; ignores ' + T('covalent') + ' character')
d.basic('Theories that fix CFT’s weaknesses?', T('Ligand field theory') + ' and ' + T('molecular orbital theory'))
d.basic('Insight: why is CO the strongest-field ligand though it is neutral?', T('π back-bonding') + ': metal d electrons flow into CO’s π*, strengthening M–C and widening Δ₀; a covalent effect CFT ignores')

# ---------------------------------------------------------------- 5.6 Carbonyls
d.sec('5.6-metal-carbonyls')
d.basic('What are homoleptic carbonyls?', 'Compounds with only ' + T('CO ligands') + ', formed by most transition metals')
d.cloze('Shapes: Ni(CO)₄ {{c1::tetrahedral}}; Fe(CO)₅ {{c2::trigonal bipyramidal}}; Cr(CO)₆ {{c3::octahedral}}.')
d.basic('Structure of Mn₂(CO)₁₀?', 'Two ' + T('square pyramidal') + ' Mn(CO)₅ units joined by an ' + T('Mn–Mn bond'), **fig('fig_5_13_carbonyls'))
d.basic('Structure of Co₂(CO)₈?', 'Co–Co bond ' + T('bridged by two CO') + ' groups')
d.basic('σ part of the M–CO bond?', 'Lone pair on ' + T('carbon') + ' donated into a vacant metal orbital')
d.basic('π part of the M–CO bond?', 'Filled metal ' + T('d orbital') + ' donates into the vacant antibonding ' + T('π*') + ' of CO')
d.basic('What is the synergic effect?', 'σ donation and π back-donation ' + T('reinforce each other') + ', strengthening the M–CO bond', **fig('fig_5_14_synergic'))
d.basic('Intuition: why "synergic"?', 'Like two friends lending money back and forth: CO gives the metal electron density (σ), the metal gives it back (π); each gift makes the next easier')
d.basic('Consequence of back-bonding for the C≡O bond?', 'Electrons in CO’s π* ' + X('weaken the C–O bond') + ' (lower C–O stretching frequency) while M–C strengthens')

# ---------------------------------------------------------------- 5.7 Applications
d.sec('5.7-applications')
d.basic('Analytical reagents that form coloured complexes?', E('EDTA, DMG (dimethylglyoxime), α-nitroso-β-naphthol, cupron'))
d.basic('How is water hardness estimated?', 'Titration with ' + T('Na₂EDTA') + ' (Ca²⁺ and Mg²⁺ complexes; selectivity from different stability constants)')
d.basic('Complex in gold extraction, and recovery?', T('[Au(CN)₂]⁻') + ' (Au + CN⁻ + O₂ + H₂O); gold recovered by adding ' + T('zinc'))
d.basic('Purification via complexes (Mond process)?', 'Impure Ni → ' + T('[Ni(CO)₄]') + ' → decomposed to pure Ni')
d.basic('Vitamin B₁₂: name and metal?', T('Cyanocobalamine') + ', Co; the anti-pernicious anaemia factor')
d.basic('Enzymes with coordinated metal ions?', E('Carboxypeptidase A, carbonic anhydrase'))
d.basic('Wilkinson catalyst: formula and use?', T('[(Ph₃P)₃RhCl]') + ': hydrogenation of alkenes')
d.basic('Why electroplate Ag and Au from [Ag(CN)₂]⁻ and [Au(CN)₂]⁻?', 'Gives a ' + T('smoother, more even') + ' coating than simple metal ions')
d.basic('Role of hypo in black-and-white photography?', 'Dissolves undecomposed AgBr as ' + T('[Ag(S₂O₃)₂]³⁻'))
d.cloze('Chelate therapy: excess Cu and Fe removed by {{c1::D-penicillamine}} and {{c2::desferrioxime B}}; lead poisoning treated with {{c3::EDTA}}; tumours inhibited by {{c4::cis-platin}}.')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Summary', 'Hybridisation · shape · unpaired e⁻?', [
    ('[Co(NH₃)₆]³⁺', 'd²sp³ · octahedral · 0', False), ('[CoF₆]³⁻', 'sp³d² · octahedral · 4', False),
    ('[Ni(CN)₄]²⁻', 'dsp² · square planar · 0', False), ('[NiCl₄]²⁻', 'sp³ · tetrahedral · 2', False),
    ('[Ni(CO)₄]', 'sp³ · tetrahedral · 0', False), ('[Fe(CN)₆]³⁻', 'd²sp³ · octahedral · 1', False)], term='VBT summary of key complexes')
table_card(d, 'Compare', 'VBT vs CFT?', [
    ('Bond nature', 'Covalent (hybrid orbitals)  |  Purely electrostatic', False), ('Explains colour?', 'No  |  Yes (d–d transitions)', False),
    ('Weak vs strong ligands?', 'No  |  Yes (spectrochemical series)', False), ('Main weakness', 'Many assumptions  |  Ignores covalency', True)],
    term='Valence bond theory vs crystal field theory')

n = d.write(os.path.join(OUT, 'deck.json'))
print(n, 'cards')
