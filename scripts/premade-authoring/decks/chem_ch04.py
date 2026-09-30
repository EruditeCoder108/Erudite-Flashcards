import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase as sc
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch04-chemical-bonding')
d = Deck('Chapter 4: Chemical Bonding and Molecular Structure', 'Class 11', ['class-11', 'chemistry', 'ch-4'])
d.description = 'Lewis structures, formal charge, ionic bonds, bond parameters, resonance, dipole moment, VSEPR, hybridisation, MO theory, hydrogen bonds'

# ---------------------------------------------------------------- Introduction
d.sec('introduction')
d.basic('What is a chemical bond?', 'The ' + T('attractive force') + ' that holds the constituents (atoms, ions, etc.) together in a chemical species')
d.basic('Why do atoms form bonds at all?', 'Bonding is nature’s way of ' + T('lowering the energy') + ' of the system to attain stability')
d.basic('Name the four theories of bonding in this unit.', T('Kössel–Lewis') + ' approach, ' + T('VSEPR') + ' theory, ' + T('valence bond (VB)') + ' theory and ' + T('molecular orbital (MO)') + ' theory')

# ---------------------------------------------------------------- 4.1 Kössel–Lewis
d.sec('4.1-kossel-lewis')
d.basic('Who first explained valence in terms of electrons, and when?', T('Kössel and Lewis') + ' independently, in ' + N('1916') + ', based on the inertness of noble gases')
d.basic('What was the Lewis "kernel"?', 'The ' + T('nucleus + inner electrons') + ' of an atom (positively charged)')
d.basic('How did Lewis picture the octet?', 'Eight outer electrons at the ' + T('corners of a cube') + ' around the kernel.<br>Na: one corner filled; a noble gas: all eight')
d.basic('What do the dots in a Lewis symbol stand for?', 'The ' + T('valence electrons') + ' (inner electrons are well protected and do not take part)')
d.basic('How do you get the group valence from a Lewis symbol?', 'Number of dots, or ' + N('8 − number of dots'))
table_card(d, '4.1 · Kössel’s postulates', 'Complete the point.', [
    ('Periodic table', 'halogens and alkali metals are separated by the noble gases', False),
    ('Ion formation', 'halogen gains an e⁻ (anion); alkali metal loses one (cation)', False),
    ('Ions formed', 'attain the stable noble-gas configuration ns²np⁶ (He: duplet)', False),
    ('Stability', 'the ions are held by electrostatic attraction', False)], term='Kössel’s postulates on ionic bonding')
d.basic('Kössel: how does NaCl form?', 'Na [Ne]3s¹ → Na⁺ [Ne] + e⁻; Cl [Ne]3s²3p⁵ + e⁻ → Cl⁻ [Ar]; Na⁺ + Cl⁻ → ' + T('Na⁺Cl⁻'))
d.basic('What is electrovalence?', 'The number of ' + T('unit charges') + ' on the ion (Ca²⁺: +2, Cl⁻: −1)')
d.cloze('Octet rule (Kössel and Lewis, 1916): atoms combine by {{c1::transfer}} or {{c2::sharing}} of valence electrons so as to have an {{c3::octet}} in their valence shells.')
d.basic('Who introduced the term "covalent bond", and what did he drop from Lewis’s model?', T('Langmuir') + ' (' + N('1919') + '); he abandoned the idea of a ' + X('stationary cubical') + ' octet')
table_card(d, '4.1.2 · Lewis–Langmuir conditions', 'Condition?', [
    ('1', 'each bond = sharing of an electron pair', False), ('2', 'each atom contributes at least one electron to the pair', False),
    ('3', 'atoms attain noble-gas configurations by sharing', False)], term='Conditions for a covalent bond (Lewis–Langmuir)')
d.basic('Name molecules with a double bond and with a triple bond.', 'Double: ' + E('CO₂') + ' (two C=O), ' + E('C₂H₄') + '. Triple: ' + E('N₂') + ', ' + E('C₂H₂'))

d.sec('4.1.3-lewis-structures')
table_card(d, '4.1.3 · writing Lewis structures', 'Step?', [
    ('1', 'add the valence electrons of all atoms', False), ('2', 'add 1 e⁻ per negative charge; subtract 1 per positive charge', False),
    ('3', 'put the least electronegative atom in the centre', False), ('4', 'single bonds first, then complete octets on terminal atoms', False),
    ('5', 'leftover pairs → multiple bonds or lone pairs', False)], term='Steps for writing a Lewis structure')
d.basic('Which atom usually goes in the centre of a Lewis structure? Give examples.', 'The ' + T('least electronegative') + ': N in NF₃, C in CO₃²⁻')
d.basic('How many valence electrons for CO₃²⁻, and for NH₄⁺?', 'CO₃²⁻: 4 + 18 + 2 = ' + N('24') + '. NH₄⁺: 5 + 4 − 1 = ' + N('8'))
d.basic('Problem 4.1: Lewis structure of CO?', '10 valence e⁻; a single bond leaves C short of an octet, so ' + T('C≡O') + ' with one lone pair on each atom')
d.basic('Problem 4.2: Lewis structure of NO₂⁻?', '18 e⁻; one ' + T('N=O') + ', one N–O⁻, one lone pair on N; the double bond can be on either O (two structures)')
d.basic('Lewis structure of O₃?', 'Central O: one O=O and one O–O; formal charges +1 (centre), 0, −1', **fig('tab_4_1_lewis_o3'))
d.basic('Lewis structure of NF₃?', 'N with three N–F single bonds and ' + T('one lone pair'), **fig('tab_4_1_lewis_nf3'))
d.basic('Lewis structure of CO₃²⁻?', 'C with one C=O and two C–O⁻; overall charge ' + N('2−'), **fig('tab_4_1_lewis_co3'))
d.basic('Lewis structure of HNO₃?', 'N⁺ bonded to one =O, one –O⁻ and one –OH', **fig('tab_4_1_lewis_hno3'))
d.basic('Exercise 4.20: correct Lewis structure of acetic acid, CH₃COOH?', 'H₃C–C(=O)–O–H: the carboxyl C has one ' + T('C=O') + ' and one C–OH; each O keeps ' + N('two') + ' lone pairs')

d.sec('4.1.4-formal-charge')
d.basic('Formula for formal charge on an atom in a Lewis structure?', r'\( FC = V - L - \tfrac12 S \)' + '<br><small>V = valence e⁻ of the free atom, L = lone-pair e⁻, S = shared e⁻</small>')
d.basic('What assumption lies behind counting formal charge?', 'The atom owns ' + T('one electron of each shared pair') + ' and ' + T('both') + ' electrons of its lone pairs')
d.basic('Formal charges on the three O atoms of O₃?', 'Central O: 6 − 2 − 3 = ' + N('+1') + '; double-bonded end O: ' + N('0') + '; single-bonded end O: 6 − 6 − 1 = ' + N('−1'))
d.basic('Which Lewis structure is usually the lowest-energy one?', 'The one with the ' + T('smallest formal charges') + ' on the atoms')
d.basic('Do formal charges show real charge separation?', X('No') + '. They only keep track of valence electrons, on a purely covalent (equal-sharing) view')

d.sec('4.1.5-octet-limitations')
d.basic('Three types of exceptions to the octet rule?', T('Incomplete octet') + ' of the central atom, ' + T('odd-electron') + ' molecules, ' + T('expanded octet'))
d.basic('Incomplete octet: examples and reason?', E('LiCl, BeH₂, BCl₃') + ' (also AlCl₃, BF₃): Li, Be and B have fewer than four valence electrons (1, 2, 3)')
d.basic('Give two odd-electron molecules.', E('NO') + ' and ' + E('NO₂'))
d.basic('Why can elements of the third period and beyond have an expanded octet?', 'They have ' + T('d orbitals') + ' available for bonding besides s and p')
d.basic('Give three examples of an expanded octet.', E('PF₅') + ' (10 e⁻), ' + E('SF₆') + ' (12 e⁻), ' + E('H₂SO₄') + ' (12 e⁻ around S), plus many coordination compounds')
d.basic('Name a sulphur compound in which S obeys the octet rule.', E('SCl₂') + ' (sulphur dichloride)')
d.basic('Which compounds challenge the octet rule’s basis (noble-gas inertness)?', E('XeF₂, KrF₂, XeOF₂') + ': xenon and krypton do combine with O and F')
d.basic('Two more drawbacks of the octet theory?', 'It does not explain ' + T('shapes') + ' of molecules, and says nothing about their ' + T('energy') + ' (relative stability)')

# ---------------------------------------------------------------- 4.2 Ionic bond
d.sec('4.2-ionic-bond')
d.basic('Formation of an ionic compound depends mainly on which two things?', 'The ' + T('ease of forming the ions') + ' from neutral atoms, and the ' + T('arrangement of ions') + ' in the crystal lattice')
d.basic('Exercise 4.6: favourable factors for an ionic bond?', 'Low ' + T('ionisation enthalpy') + ' of the metal<br>Highly negative ' + T('electron gain enthalpy') + ' of the non-metal<br>High ' + T('lattice enthalpy'))
d.basic('Is ionisation always endothermic? Electron gain?', 'Ionisation: ' + T('always endothermic') + '. Electron gain: ' + X('can be exothermic or endothermic'))
d.basic('Electron affinity vs electron gain enthalpy?', 'Electron affinity is the ' + T('negative') + ' of the energy change on electron gain')
d.basic('Which common cation contains only non-metals?', E('NH₄⁺') + ' (ammonium)')
d.basic('Name the crystal structure of NaCl.', T('Rock salt') + ' structure: Na⁺ and Cl⁻ alternate in three dimensions', **fig('rock_salt'))
d.basic('Na → Na⁺ costs 495.8 kJ/mol and Cl → Cl⁻ releases only 348.7 kJ/mol. Why does NaCl still form?', 'The ' + T('lattice enthalpy') + ' (' + N('788 kJ mol⁻¹') + ') more than makes up the net ' + N('147.1 kJ mol⁻¹') + ' absorbed')
d.basic('What truly measures the stability of an ionic compound?', 'Its ' + T('enthalpy of lattice formation') + ', ' + X('not') + ' simply reaching an octet in the gaseous ions')
d.basic('Define lattice enthalpy.', 'Energy needed to ' + T('completely separate 1 mol') + ' of a solid ionic compound into its gaseous ions (to infinite distance)')
d.basic('Why can lattice enthalpy not be found just from attractions and repulsions between ion pairs?', 'The crystal is ' + T('three-dimensional') + '; factors of the crystal geometry must be included')
d.basic('Exercise 4.14: show electron transfer to form ions for (a) K and S, (b) Ca and O, (c) Al and N.', '(a) 2K → 2K⁺ + 2e⁻; S + 2e⁻ → S²⁻ → ' + E('K₂S') + '. (b) Ca²⁺ + O²⁻ → ' + E('CaO') + '. (c) Al³⁺ + N³⁻ → ' + E('AlN'))
d.basic('Exercise 4.3: Lewis symbols for S and S²⁻, Al and Al³⁺, H and H⁻?', 'S: 6 dots; S²⁻: 8 dots. Al: 3 dots; Al³⁺: ' + N('no dots') + '. H: 1 dot; H⁻: 2 dots')

# ---------------------------------------------------------------- 4.3 Bond parameters
d.sec('4.3.1-bond-length')
d.basic('Define bond length.', 'The equilibrium distance between the ' + T('nuclei') + ' of two bonded atoms in a molecule.<br>Measured by spectroscopy, X-ray and electron diffraction')
d.basic('Bond length R of AB in terms of covalent radii?', r'\( R = r_A + r_B \)')
d.cloze('Covalent radius is half the distance between two similar atoms joined by a covalent bond {{c1::in the same molecule}}; van der Waals radius is half the distance between two similar atoms {{c2::in separate molecules}} in a solid.')
d.basic('What does the van der Waals radius represent?', 'The ' + T('overall size') + ' of the atom, including its valence shell, in a ' + T('non-bonded') + ' situation')
d.occlusion('Fig. 4.2 · Covalent and van der Waals radii of chlorine', M + 'fig_4_2_cl2_radii.webp', (1001, 735), [
    ('r<sub>c</sub> = 99 pm (covalent radius)', [565, 24, 190, 50]), ('198 pm (Cl–Cl bond length)', [792, 30, 118, 118]),
    ('r<sub>vdw</sub> = 180 pm (van der Waals radius)', [722, 418, 190, 202]), ('360 pm', [822, 585, 112, 122])], printed=True)
d.basic('Which is larger for chlorine: covalent or van der Waals radius?', T('van der Waals') + ' (' + N('180 pm') + ' vs ' + N('99 pm') + ')')
table_card(d, 'Table 4.2 · average bond lengths', 'Length (pm)?', [
    ('O–H', '96', False), ('C–H', '107', False), ('C–C', '154', False), ('C=C', '133', False),
    ('C≡C', '120', False), ('C–O / C=O', '143 / 121', False), ('C≡N', '116', False)], term='Average bond lengths (Table 4.2)')
table_card(d, 'Table 4.3 · bond lengths', 'Length (pm)?', [
    ('H₂', '74', False), ('F₂', '144', False), ('Cl₂', '199', False), ('N₂ (N≡N)', '109', False),
    ('O₂ (O=O)', '121', False), ('HF → HI', '92, 127, 141, 160', False)], term='Bond lengths in common molecules (Table 4.3)')
d.basic('Trend: why does the H–X bond length rise from HF to HI?', 'The halogen atom gets ' + T('bigger') + ' down the group (larger covalent radius)')

d.sec('4.3.2-bond-angle')
d.basic('Define bond angle.', 'The angle between the ' + T('orbitals containing bonding electron pairs') + ' around the central atom; found by spectroscopy')
d.basic('H–O–H bond angle in water?', N('104.5°'))

d.sec('4.3.3-bond-enthalpy')
d.basic('Define bond enthalpy.', 'Energy needed to break ' + N('1 mol') + ' of bonds of a particular type between two atoms in the ' + T('gaseous') + ' state (kJ mol⁻¹)')
table_card(d, '4.3.3 · bond enthalpy', 'Bond enthalpy (kJ mol⁻¹)?', [
    ('H–H', '435.8', False), ('O=O', '498', False), ('N≡N', '946', False), ('H–Cl', '431', False)], term='Bond enthalpies: H2, O2, N2, HCl')
d.basic('Larger bond dissociation enthalpy means…?', 'A ' + T('stronger') + ' bond')
d.basic('Why is the second O–H bond of water broken with a different energy from the first (502 vs 427 kJ/mol)?', 'After the first break, the ' + T('chemical environment') + ' of the remaining O–H has changed')
d.basic('Average O–H bond enthalpy in water?', r'\( \dfrac{502 + 427}{2} = \)' + ' ' + N('464.5 kJ mol⁻¹') + ': total dissociation enthalpy ÷ number of bonds broken')

d.sec('4.3.4-bond-order')
d.basic('Bond order in the Lewis picture?', 'The ' + T('number of bonds') + ' (shared pairs) between the two atoms: H₂ 1, O₂ 2, N₂ 3, CO 3')
d.basic('Which species share bond order 3 by being isoelectronic?', E('N₂, CO, NO⁺'))
d.basic('Which species share bond order 1 by being isoelectronic?', E('F₂') + ' and ' + E('O₂²⁻'))
d.basic('What is special about N₂’s bond enthalpy?', N('946 kJ mol⁻¹') + ': one of the ' + T('highest') + ' for a diatomic molecule (triple bond)')
d.cloze('As bond order increases, bond enthalpy {{c1::increases}} and bond length {{c2::decreases}}.')
d.basic('Exercise 4.9: express bond strength in terms of bond order.', 'Higher bond order → ' + T('stronger bond') + ' (higher bond enthalpy) and ' + T('shorter') + ' bond')

d.sec('4.3.5-resonance')
d.basic('Both O–O bonds in O₃ are 128 pm. How does this compare with single and double bonds?', 'Between O–O (' + N('148 pm') + ') and O=O (' + N('121 pm') + '): neither Lewis structure fits alone', **fig('fig_4_3_o3_resonance'))
d.basic('State the concept of resonance.', 'When one Lewis structure cannot describe a molecule, several ' + T('canonical structures') + ' are written.<br>They have similar energy, the same positions of nuclei and the same bonding/non-bonding pairs.<br>Their ' + T('hybrid') + ' is the real molecule')
d.basic('How is resonance shown?', 'With a ' + T('double-headed arrow') + ' (↔)')
d.basic('Resonance energy?', 'Energy of the most stable canonical structure − energy of the ' + T('resonance hybrid') + ': resonance ' + T('stabilises') + ' the molecule')
d.basic('Do canonical forms really exist?', X('No') + '.<br>The molecule does not flip between them.<br>They have no real existence, and there is no equilibrium between them')
d.basic('Problem 4.3: why is CO₃²⁻ a resonance hybrid?', 'One Lewis structure shows unequal bonds, but all C–O bonds are found ' + T('equivalent') + ': three canonical forms', **fig('fig_4_4_co3_resonance'))
d.basic('Problem 4.4: C–O length in CO₂ (115 pm) lies between which values?', 'C=O ' + N('121 pm') + ' and C≡O ' + N('110 pm') + ': CO₂ is a hybrid of three forms', **fig('fig_4_5_co2_resonance'))
d.basic('Exercise 4.12: two structures of H₃PO₃ differ in where an H sits (on P or on O). Are they canonical forms?', X('No') + ': canonical forms must have the ' + T('same positions of nuclei') + ' and differ only in electrons')
d.basic('Exercise 4.13: how many resonance structures for SO₃, NO₂ and NO₃⁻?', 'SO₃: ' + N('3') + ' (one S=O moving); NO₂: ' + N('2') + '; NO₃⁻: ' + N('3') + ' (one N=O moving)')

d.sec('4.3.6-polarity')
d.basic('Which is a non-polar covalent bond: H–H or H–F?', T('H–H') + ' (identical atoms share equally); H–F is ' + T('polar') + ' (Exercise 4.18)')
d.basic('Formula and unit of dipole moment?', r'\( \mu = Q \times r \)' + '<br>Unit: ' + T('debye (D)') + ', ' + N('1 D = 3.33564 × 10⁻³⁰ C m'))
d.basic('Is dipole moment a scalar or a vector?', T('Vector') + ': for a polyatomic molecule it is the vector sum of bond dipoles')
d.basic('The chemist’s crossed arrow for a dipole: where are the cross and the head?', 'Cross on the ' + T('positive') + ' end, head on the ' + T('negative') + ' end')
d.basic('Dipole moment of H₂O?', N('1.85 D') + ' (bent, H–O–H ' + N('104.5°') + ')', **fig('h2o_dipole'))
d.basic('Exercise 4.22: why is μ of BeH₂ (or BeF₂) zero though the bonds are polar?', 'The molecule is ' + T('linear') + ': two equal bond dipoles point opposite and cancel')
d.basic('Exercise 4.15: CO₂ and H₂O are both triatomic. Why is μ(CO₂) = 0 but μ(H₂O) = 1.85 D?', 'CO₂ is ' + T('linear') + ' (bond dipoles cancel); H₂O is ' + T('bent') + ' (they add)')
d.basic('Why is μ of BF₃ zero though B–F bonds are polar?', 'Trigonal planar at ' + N('120°') + ': the three bond moments sum to ' + T('zero'), **fig('bf3_dipole'))
d.basic('Exercise 4.23: why is μ(NH₃) greater than μ(NF₃)?', 'In NH₃ the lone-pair dipole points the ' + T('same way') + ' as the N–H bond moments.<br>In NF₃ it points ' + X('opposite') + ' to the N–F moments', **fig('nh3_nf3_dipole'))
table_card(d, 'Table 4.5 · dipole moments', 'μ (D)?', [
    ('HF / HCl / HBr / HI', '1.78 / 1.07 / 0.79 / 0.38', False), ('H₂O / H₂S / CO₂', '1.85 / 0.95 / 0', False),
    ('NH₃ / NF₃ / BF₃', '1.47 / 0.23 / 0', False), ('CH₄ / CHCl₃ / CCl₄', '0 / 1.04 / 0', False)], term='Dipole moments of selected molecules (Table 4.5)')
d.basic('Exercise 4.16: uses of dipole moment?', 'To tell ' + T('polar from non-polar') + ' molecules<br>To predict ' + T('shape') + ' (e.g. linear CO₂ vs bent H₂O)<br>To estimate the ' + T('% ionic character') + ' of a bond')
d.basic('Exercise 4.17: electronegativity vs electron gain enthalpy?', 'Electronegativity: tendency of an atom ' + T('in a molecule') + ' to attract the shared pair; relative, no unit. Electron gain enthalpy: energy change when an ' + T('isolated gaseous atom') + ' gains an electron; measurable, kJ mol⁻¹')
d.basic('Exercise 4.19: arrange in increasing ionic character: LiF, K₂O, N₂, SO₂, ClF.', N('N₂ < SO₂ < ClF < K₂O < LiF') + ' (by electronegativity difference: 0, 1.0, 1.0, 2.7, 3.0)')

d.sec('4.3.6-fajans-rules')
d.basic('Do ionic bonds have covalent character?', T('Yes') + ': just as covalent bonds have partial ionic character, ionic bonds have partial covalent character.<br>The cation ' + T('polarises') + ' the anion')
d.cloze('Fajans’ rules: covalent character of an ionic bond increases with a {{c1::smaller}} cation, a {{c2::larger}} anion, and a {{c3::greater charge}} on the cation.')
d.basic('For the same size and charge, which cation polarises more: (n−1)dⁿns⁰ (transition metal) or ns²np⁶ (noble-gas core)?', T('(n−1)dⁿns⁰') + ': d electrons shield the nucleus poorly')
d.basic('Intuition: why does a small, highly charged cation make a bond covalent?', 'Its concentrated positive charge ' + T('pulls the anion’s electron cloud') + ' towards itself.<br>Electron density builds up between the nuclei, like a shared pair')

# ---------------------------------------------------------------- 4.4 VSEPR
d.sec('4.4-vsepr')
d.basic('Who proposed VSEPR theory, and who refined it?', T('Sidgwick and Powell') + ' (' + N('1940') + '); refined by ' + T('Nyholm and Gillespie') + ' (' + N('1957') + ')')
table_card(d, '4.4 · VSEPR postulates', 'Complete the postulate.', [
    ('Shape depends on', 'the number of valence-shell electron pairs (bonded or not) around the central atom', False),
    ('Electron pairs', 'repel one another (their clouds are negative)', False),
    ('They take positions that', 'minimise repulsion (maximise distance)', False),
    ('Valence shell is taken as', 'a sphere, pairs on its surface far apart', False),
    ('A multiple bond counts as', 'one "super pair"', False),
    ('With resonance', 'VSEPR applies to any canonical structure', False)], term='Postulates of VSEPR theory')
d.basic('Order of electron-pair repulsions?', T('lp–lp > lp–bp > bp–bp'))
d.basic('Why do lone pairs repel more than bond pairs (Nyholm and Gillespie)?', 'A lone pair is localised on ' + T('one atom') + ' only; a bond pair is shared between two.<br>So the lone pair occupies more space')
d.basic('What do extra lone-pair repulsions do to shapes?', 'They cause ' + T('deviations from idealised shapes') + ' and alter bond angles')
d.occlusion('Table 4.6 · Name each molecular geometry (no lone pair)', M + 'tab_4_6_geometry.webp', (450, 1001), [
    ('Linear', [53, 107, 113, 40]), ('Trigonal planar', [31, 277, 184, 40]), ('Tetrahedral', [53, 483, 143, 40]),
    ('Trigonal bipyramidal', [4, 713, 237, 40]), ('Octahedral', [53, 952, 143, 40])], printed=True)
table_card(d, 'Table 4.6 · no lone pair', 'Shape and example?', [
    ('AB₂', 'linear · BeCl₂', False), ('AB₃', 'trigonal planar · BF₃', False), ('AB₄', 'tetrahedral · CH₄', False),
    ('AB₅', 'trigonal bipyramidal · PCl₅', False), ('AB₆', 'octahedral · SF₆', False)], term='VSEPR shapes with no lone pair (Table 4.6)')
d.occlusion('Table 4.7 · Name each shape (with lone pairs)', M + 'tab_4_7_shapes.webp', (795, 1001), [
    ('Bent', [497, 94, 164, 30]), ('Trigonal pyramidal', [497, 200, 164, 32]), ('Bent', [497, 336, 164, 30]),
    ('See-saw', [497, 459, 164, 30]), ('T-shape', [497, 622, 164, 32]), ('Square pyramid', [497, 775, 164, 30]),
    ('Square planar', [497, 894, 164, 30])], printed=True)
table_card(d, 'Table 4.7 · with lone pairs', 'Shape and example?', [
    ('AB₂E', 'bent · SO₂, O₃', False), ('AB₃E', 'trigonal pyramidal · NH₃', False), ('AB₂E₂', 'bent · H₂O', False),
    ('AB₄E', 'see-saw · SF₄', False), ('AB₃E₂', 'T-shape · ClF₃', False), ('AB₅E', 'square pyramid · BrF₅', False),
    ('AB₄E₂', 'square planar · XeF₄', False)], term='VSEPR shapes with lone pairs (Table 4.7)')
d.basic('Exercise 4.7: shapes by VSEPR of BeCl₂, BCl₃, SiCl₄, AsF₅, H₂S, PH₃?', 'Linear, trigonal planar, tetrahedral, trigonal bipyramidal, ' + T('bent') + ', ' + T('trigonal pyramidal'))
d.basic('H–N–H angle in NH₃, and why not 109.5°?', N('107°') + ': lp–bp repulsion > bp–bp squeezes the bond pairs')
d.basic('Exercise 4.8: both NH₃ and H₂O are distorted tetrahedral. Why is the angle smaller in water (104.5° vs 107°)?', 'H₂O has ' + N('two') + ' lone pairs; the extra lp–lp repulsion (strongest) squeezes the O–H bonds more')
d.basic('In SF₄, is the lone pair axial or equatorial, and why?', T('Equatorial') + ': only ' + N('two') + ' lp–bp repulsions at 90° (vs three if axial) → see-saw')
d.basic('In ClF₃, where do the two lone pairs sit?', T('Equatorial') + ' positions, giving a ' + T('T-shape'))
d.basic('In XeF₄, where are the two lone pairs?', 'Opposite each other (' + N('180°') + ') → ' + T('square planar'))
d.basic('For which compounds does VSEPR predict shapes especially well?', T('p-block') + ' compounds; its theoretical basis is still debated')
d.basic('Trap: shape vs electron geometry of NH₃?', 'Electron-pair geometry: ' + T('tetrahedral') + '<br>Shape (atoms only): ' + T('trigonal pyramidal') + '<br>Lone pairs are invisible in the shape')

# ---------------------------------------------------------------- 4.5 VB theory
d.sec('4.5-valence-bond')
d.basic('Who introduced valence bond theory?', T('Heitler and London') + ' (' + N('1927') + '), developed by ' + T('Pauling'))
d.basic('Exercise 4.33: why does H₂ form as two H atoms approach (VB theory)?', 'New attractions (nucleus–other electron) and repulsions arise.<br>' + T('Attraction wins') + ', and the energy falls to a minimum at the bond length')
d.basic('Bond length and bond enthalpy of H₂ (VB section)?', N('74 pm') + '; ' + N('435.8 kJ mol⁻¹') + ' released on forming 1 mol', **fig('fig_4_8_h2_energy'))
d.basic('Intuition: why does the energy curve for H₂ rise again at very short distance?', 'Nucleus–nucleus and electron–electron ' + T('repulsions') + ' grow faster than attraction; the minimum is the bond length')
d.basic('Orbital overlap concept?', 'A covalent bond forms by ' + T('partial merging (overlap)') + ' of half-filled valence orbitals with opposite spins.<br>The greater the overlap, the ' + T('stronger') + ' the bond')
d.basic('Exercise 4.37: significance of the + and − signs on orbital lobes?', 'They are the ' + T('phase (sign) of the wave function') + ', not charge. Same-sign overlap → bond; opposite sign → no bond', **fig('fig_4_9_overlaps'))
d.basic('What H–C–H angle would simple (unhybridised) overlap predict for CH₄?', N('90°') + ' (real: ' + N('109.5°') + '); simple overlap cannot explain directional shapes, so hybridisation is needed')

d.sec('4.5.4-sigma-pi')
d.basic('How is a σ bond formed?', T('Head-on (axial) overlap') + ' along the internuclear axis')
d.basic('Which overlaps can give a σ bond?', 's–s, s–p, p–p (head-on)', **fig('sigma_overlaps'))
d.basic('How is a π bond formed?', T('Sidewise overlap') + ': orbital axes parallel, perpendicular to the internuclear axis; two lobes, above and below', **fig('pi_overlap'))
d.basic('Which is stronger, σ or π, and why?', T('σ') + ': larger extent of overlap')
d.basic('Can a π bond exist without a σ bond between two atoms?', X('No') + '. π bonds form in addition to a σ bond (NCERT’s rule; C₂ in MO theory is the exception)')
d.basic('Exercise 4.29: with x as the internuclear axis, which will not form a σ bond: 1s+1s, 1s+2pₓ, 2p_y+2p_y, 1s+2s?', T('2p_y + 2p_y') + ' (sidewise → π)')
d.basic('Exercise 4.28: σ and π bonds in C₂H₂ and C₂H₄?', 'C₂H₂: ' + N('3σ, 2π') + '; C₂H₄: ' + N('5σ, 1π'))
d.basic('Exercise 4.31: bond pairs and lone pairs in H₂O?', N('2') + ' bond pairs (O–H) and ' + N('2') + ' lone pairs on O')

# ---------------------------------------------------------------- 4.6 Hybridisation
d.sec('4.6-hybridisation')
d.basic('Who introduced hybridisation, and why?', T('Pauling') + ', to explain the characteristic ' + T('shapes') + ' of polyatomic molecules (e.g. CH₄, NH₃, H₂O)')
d.basic('Define hybridisation.', 'Intermixing of orbitals of ' + T('slightly different energies') + ' to form a new set of orbitals of ' + T('equivalent energy and shape'))
d.basic('How many hybrid orbitals form from n atomic orbitals?', N('n') + ' (always equal)')
d.cloze('Features: hybrid orbitals are always {{c1::equivalent in energy and shape}}; they form {{c2::more effective}} bonds than pure orbitals; they point so that {{c3::repulsion is minimum}}.')
d.cloze('Conditions for hybridisation: only {{c1::valence shell}} orbitals mix; they must have {{c2::almost equal energy}}; promotion of electrons is {{c3::not essential}}.')
d.basic('Can filled orbitals take part in hybridisation?', T('Yes') + '; not only half-filled ones')
table_card(d, '4.6.1 · s–p hybrids', '% s-character and angle?', [
    ('sp', '50% s · 180° · linear', False), ('sp²', '33% s · 120° · trigonal planar', False),
    ('sp³', '25% s · 109.5° · tetrahedral', False)], term='sp, sp2, sp3: s-character and angle')
d.basic('Other name for sp hybridisation?', T('Diagonal') + ' hybridisation')
d.basic('Hybridisation and shape of BeCl₂?', T('sp') + ', linear (' + N('180°') + ')', **fig('fig_4_10_becl2_sp'))
d.basic('Hybridisation and shape of BCl₃?', T('sp²') + ', trigonal planar (' + N('120°') + ')', **fig('fig_4_11_bcl3_sp2'))
sc.sp3_mixer(d)
d.basic('Hybridisation and shape of CH₄?', T('sp³') + ', tetrahedral (' + N('109.5°') + ')', **fig('fig_4_12_ch4_sp3'))
d.basic('Exercise 4.21: why is CH₄ tetrahedral and not square planar?', 'sp³ orbitals point to the corners of a ' + T('tetrahedron') + ' (109.5°, least repulsion). Square planar needs 90° angles (more repulsion) and dsp² orbitals, which C (no d orbitals) cannot form')
d.basic('Hybridisation and shape of NH₃?', T('sp³') + ' N with one lone pair: trigonal pyramidal, ' + N('107°'), **fig('fig_4_13_nh3'))
d.basic('Hybridisation and shape of H₂O?', T('sp³') + ' O with two lone pairs: bent (V-shape), ' + N('104.5°'), **fig('fig_4_14_h2o'))
d.basic('Intuition: more s-character in a hybrid means…?', 'A ' + T('shorter, stronger') + ' bond<br>A ' + T('wider') + ' angle (sp 180° > sp² 120° > sp³ 109.5°)<br>A more electronegative carbon')
d.basic('Ethane: C–C and C–H bond lengths?', 'C–C ' + N('154 pm') + ' (sp³–sp³ σ); C–H ' + N('109 pm'))
d.basic('Ethene: what makes up the C=C bond?', 'One ' + T('sp²–sp² σ') + ' + one ' + T('π') + ' (from the unhybridised 2p orbitals); C=C ' + N('134 pm'), **fig('fig_4_15_ethene'))
d.basic('Bond angles in ethene?', 'H–C–H ' + N('117.6°') + '; H–C–C ' + N('121°'))
d.basic('What makes up the C≡C bond in ethyne?', N('1 σ') + ' (sp–sp) + ' + N('2 π') + '; molecule linear', **fig('fig_4_16_ethyne'))
d.basic('Exercise 4.30: hybrid orbitals used by carbon in CH₃–CH=CH₂, CH₃–CH₂–OH, CH₃CHO, CH₃COOH?', 'CH₃–CH=CH₂: sp³, ' + T('sp², sp²') + '. Ethanol: sp³, sp³. CH₃CHO: sp³, ' + T('sp²') + '. CH₃COOH: sp³, ' + T('sp²'))
d.basic('Shortcut: hybridisation of carbon from its bonds?', 'Four single bonds → ' + T('sp³') + '; one double bond → ' + T('sp²') + '; a triple bond or two double bonds → ' + T('sp'))

d.sec('4.6.3-d-orbital-hybrids')
d.basic('Why can third-period atoms use d orbitals but 3p–3d–4s hybridisation of nitrogen is impossible?', 'Second-period atoms have ' + X('no d orbitals') + '.<br>In the third period, 3s, 3p and 3d are close in energy (while 3p and 4s differ a lot)')
table_card(d, '4.6.3 · hybrids with d orbitals', 'Shape and example?', [
    ('sp³d', 'trigonal bipyramidal · PCl₅', False), ('sp³d²', 'octahedral · SF₆ (square pyramidal BrF₅)', False),
    ('dsp²', 'square planar · [Ni(CN)₄]²⁻', False), ('d²sp³', 'octahedral · [Co(NH₃)₆]³⁺', False)],
    term='d-orbital hybridisation: shapes and examples')
d.basic('Exercise 4.38: hybridisation of PCl₅, and why are the axial bonds longer?', T('sp³d') + '<br>The two axial bond pairs suffer ' + T('more repulsion') + ' (three equatorial pairs at 90°), so they are longer and weaker', **fig('fig_4_17_pcl5'))
d.basic('Why is PCl₅ reactive?', 'Its axial bonds are longer and ' + T('weaker') + '; a Cl is easily lost (PCl₅ → PCl₃ + Cl₂)')
d.basic('Hybridisation and geometry of SF₆?', T('sp³d²') + ', regular octahedral; six S–F bonds at 90°', **fig('fig_4_18_sf6'))
d.basic('Exercise 4.25: AlCl₃ + Cl⁻ → AlCl₄⁻. Change in the hybridisation of Al?', T('sp²') + ' (trigonal planar) → ' + T('sp³') + ' (tetrahedral)')
d.basic('Exercise 4.26: BF₃ + NH₃ → F₃B←NH₃. Change in hybridisation of B and N?', 'B: ' + T('sp² → sp³') + '; N: stays ' + T('sp³') + ' (its lone pair becomes a bond pair)')

# ---------------------------------------------------------------- 4.7 MO theory
d.sec('4.7-mo-theory')
d.basic('Who developed molecular orbital theory?', T('F. Hund and R.S. Mulliken') + ' (' + N('1932') + ')')
table_card(d, '4.7 · MO theory', 'Complete the feature.', [
    ('Electrons in a molecule are in', 'molecular orbitals', False), ('AOs combined must have', 'comparable energy and proper symmetry', False),
    ('An AO is influenced by', 'one nucleus (monocentric)', False), ('An MO is influenced by', 'two or more nuclei (polycentric)', False),
    ('Number of MOs formed', 'equals number of AOs combined', False), ('Bonding MO vs antibonding', 'lower energy, more stable', False),
    ('Filling order', 'aufbau, Pauli, Hund', False)], term='Salient features of MO theory')
d.basic('LCAO expressions for σ and σ*?', r'\( \sigma = \psi_A + \psi_B,\quad \sigma^* = \psi_A - \psi_B \)', **fig('fig_4_19_lcao'))
d.cloze('A bonding MO forms by {{c1::constructive}} interference (addition) of electron waves; an antibonding MO by {{c2::destructive}} interference (subtraction).')
d.basic('Why is a bonding MO lower in energy than the AOs, and antibonding higher?', 'Bonding: electron density ' + T('builds between the nuclei') + ' and holds them. Antibonding: density is pushed ' + X('away') + ', leaving a nodal plane; the nuclei repel')
d.cloze('Exercise 4.34: conditions for LCAO: combining AOs must have {{c1::the same or nearly the same energy}}, {{c2::the same symmetry about the molecular axis}}, and {{c3::maximum overlap}}.')
d.basic('Can 1s combine with 2s? Can 2p_z of one atom combine with 2pₓ of the other (z = molecular axis)?', X('No') + ' to both: 1s and 2s differ in ' + T('energy') + '; 2p_z and 2pₓ differ in ' + T('symmetry'))
d.basic('Which MOs are symmetrical about the bond axis: σ or π?', T('σ') + ' (π are not)')
d.occlusion('Fig. 4.20 · Name each molecular orbital', M + 'fig_4_20_mo_contours.webp', (929, 1001), [
    ('σ*1s', [663, 140, 92, 34]), ('σ1s', [663, 275, 92, 34]), ('σ*2p<sub>z</sub>', [663, 466, 92, 38]),
    ('σ2p<sub>z</sub>', [663, 594, 92, 36]), ('π*2p<sub>x</sub>', [663, 800, 92, 38]), ('π2p<sub>x</sub>', [663, 937, 92, 38])], printed=True)
d.cloze('For {{c1::B₂, C₂ and N₂}}, the π2pₓ and π2p_y MOs lie {{c2::below}} σ2p_z; for O₂ and F₂, σ2p_z lies below π2p.')
d.basic('Mnemonic: when does σ2p_z drop below π2p?', 'From ' + T('O₂ onwards') + ' (O₂, F₂, Ne₂). Up to N₂, s–p mixing pushes σ2p_z above π2p')
d.basic('Bond order formula in MO theory?', 'B.O. = ' + r'\( \tfrac12 (N_b - N_a) \)' + ' (N_b, N_a = electrons in bonding and antibonding MOs)')
table_card(d, '4.7.5 · what bond order tells you', 'Meaning?', [
    ('N_b > N_a (positive B.O.)', 'stable molecule', False), ('N_b ≤ N_a (zero or negative)', 'unstable, does not exist', True),
    ('B.O. 1, 2, 3', 'single, double, triple bond', False), ('Higher B.O.', 'shorter bond', False),
    ('All MOs doubly filled', 'diamagnetic', False), ('Any MO singly filled', 'paramagnetic', False)], term='Interpreting MO electronic configurations')

d.sec('4.8-homonuclear-diatomics')
d.basic('H₂ in MO terms: configuration, bond order, magnetism?', r'\( (\sigma 1s)^2 \)' + '; B.O. = (2 − 0)/2 = ' + N('1') + '; ' + T('diamagnetic'))
d.basic('Correction: NCERT gives H₂’s bond energy as 435.8 kJ/mol in 4.3.3 but 438 kJ/mol in 4.8. Which to use?', 'Two slightly different quoted values for the same quantity. For bond-enthalpy questions use ' + T('435.8 kJ mol⁻¹') + ' (4.3.3); the bond length 74 pm is the same in both')
d.basic('Bond order of He₂, and does it exist?', 'σ1s² σ*1s² → ½(2 − 2) = ' + N('0') + ', so it ' + X('does not exist'))
d.basic('Exercise 4.35: use MO theory to show why Be₂ does not exist.', 'Be₂: σ1s² σ*1s² σ2s² σ*2s² → N_b = N_a = 4, B.O. = ' + N('0'))
d.basic('Li₂: configuration, bond order, magnetism?', 'KK(σ2s)² → B.O. ' + N('1') + '; ' + T('diamagnetic') + ' (known in the vapour phase)')
d.basic('What does "KK" mean in KK(σ2s)²?', 'The closed K-shell part ' + T('(σ1s)² (σ*1s)²'))
d.basic('What is unusual about the double bond in C₂?', 'Both bonds are ' + T('π bonds') + ' (four electrons in π2pₓ and π2p_y), not σ + π; C₂ is diamagnetic')
d.basic('Correction: NCERT writes C₂ as (σ1s)²(σ*1s)²(σ*2s)²(π2pₓ² = π2p_y²). What is missing?', 'The ' + T('(σ2s)²') + ' term: only 10 of the 12 electrons are shown. Correct: σ1s² σ*1s² ' + T('σ2s²') + ' σ*2s² π2pₓ² π2p_y² (as in the KK form on the next line)')
mo_card(d, 'O₂', 12, True, 'Bond order and magnetism of O₂?',
        'N<sub>b</sub> = 10, N<sub>a</sub> = 6 → B.O. = <span class="n">2</span><br>Two unpaired e⁻ in π* → <b>paramagnetic</b>',
        'MO diagram of O2', 'O₂: bond order 2, paramagnetic (2 unpaired e⁻ in π*2p)')
d.basic('Why was the paramagnetism of O₂ a triumph for MO theory?', 'The Lewis structure O=O shows all electrons ' + X('paired') + '.<br>MO theory puts two unpaired electrons in π*2pₓ and π*2p_y, matching experiment')
mo_card(d, 'N₂', 10, False, 'Bond order and magnetism of N₂?',
        'N<sub>b</sub> = 10, N<sub>a</sub> = 4 → B.O. = <span class="n">3</span><br>All paired → <b>diamagnetic</b>',
        'MO diagram of N2', 'N₂: bond order 3, diamagnetic')
mo_card(d, 'B₂', 6, False, 'Bond order and magnetism of B₂?',
        'N<sub>b</sub> = 6, N<sub>a</sub> = 4 → B.O. = <span class="n">1</span><br>Two unpaired e⁻ in π2p → <b>paramagnetic</b>',
        'MO diagram of B2', 'B₂: bond order 1, paramagnetic')
table_card(d, 'Fig. 4.21 · B₂ to Ne₂', 'Bond order and magnetism?', [
    ('B₂', '1 · paramagnetic', False), ('C₂', '2 · diamagnetic', False), ('N₂', '3 · diamagnetic', False),
    ('O₂', '2 · paramagnetic', False), ('F₂', '1 · diamagnetic', False), ('Ne₂', '0 · does not exist', True)],
    term='B2 to Ne2: bond order and magnetism')
table_card(d, 'Exercise 4.36 · oxygen species', 'Bond order and magnetism?', [
    ('O₂⁺', '2.5 · paramagnetic', False), ('O₂', '2 · paramagnetic', False),
    ('O₂⁻ (superoxide)', '1.5 · paramagnetic', False), ('O₂²⁻ (peroxide)', '1 · diamagnetic', False)],
    note='Stability: O₂⁺ > O₂ > O₂⁻ > O₂²⁻', term='O2+, O2, O2-, O2 2-: bond order and magnetism')
d.basic('Exercise 4.40: bond order of N₂, O₂, O₂⁺, O₂⁻?', N('3, 2, 2.5, 1.5'))
d.basic('Shortcut: bond order of 2nd-period diatomic species from the electron count?', 'It peaks at ' + N('3 for 10 electrons') + ' (N₂, CO, NO⁺) and falls by 0.5 per electron either side.<br>8 → 2 (C₂), 12 → 2 (O₂), 14 → 1 (F₂), 6 → 1 (B₂)')
d.basic('Removing an electron from O₂ raises the bond order but from N₂ lowers it. Why?', 'O₂ loses an ' + T('antibonding') + ' (π*) electron → B.O. 2.5. N₂ loses a ' + T('bonding') + ' electron → B.O. 2.5 from 3')
sc.bond_order_bars(d)

# ---------------------------------------------------------------- 4.9 Hydrogen bonding
d.sec('4.9-hydrogen-bonding')
d.basic('To which atoms must H be bonded to form hydrogen bonds?', 'Highly electronegative ' + T('F, O or N'))
d.basic('Exercise 4.39: define hydrogen bond. Weaker or stronger than van der Waals forces?', 'The attractive force binding the ' + T('H atom') + ' of one molecule to an electronegative atom (F, O, N) of another.<br>' + T('Stronger') + ' than van der Waals forces, weaker than covalent bonds')
d.basic('Cause of hydrogen bonding?', 'The shared pair shifts towards the electronegative X, leaving H with δ+.<br>This H is attracted by the δ− X of a neighbour:<br>H<sup>δ+</sup>–X<sup>δ−</sup> ··· H<sup>δ+</sup>–X<sup>δ−</sup>')
d.basic('How is a hydrogen bond drawn?', 'With a ' + T('dotted line') + ' (···); the covalent bond is a solid line. H acts as a ' + T('bridge') + ' between two atoms')
d.basic('In which physical state is hydrogen bonding strongest?', T('Solid') + ' (maximum); weakest in the gas')
d.basic('Types of hydrogen bond?', T('Intermolecular') + ' (between molecules) and ' + T('intramolecular') + ' (within one molecule)')
d.basic('Give examples of intermolecular hydrogen bonding.', E('HF') + ' (zig-zag chains), ' + E('water') + ', ' + E('alcohols'))
d.basic('Give an example of intramolecular hydrogen bonding.', E('o-Nitrophenol') + ' (H between the two O atoms)', **fig('fig_4_22_o_nitrophenol'))
d.basic('Intuition: why does o-nitrophenol boil lower than p-nitrophenol?', 'Its H-bond is ' + T('intramolecular') + ' (inside one molecule), so molecules do not stick together.<br>p-Nitrophenol forms intermolecular H-bonds')
d.basic('Why is water a liquid while H₂S is a gas at room temperature?', 'Water molecules are held by ' + T('hydrogen bonds') + '; S is not electronegative enough for strong H-bonding')

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary · theories', 'What does each explain?', [
    ('Kössel', 'ionic bonds via noble-gas ions', False), ('Lewis–Langmuir', 'covalent bonds by electron sharing', False),
    ('VSEPR', 'shapes from electron-pair repulsion', False), ('VB + hybridisation', 'directional bonds, σ and π', False),
    ('MO theory', 'bond order, magnetism (O₂ paramagnetic)', False)], term='Bonding theories and what they explain')
table_card(d, 'Summary · shapes', 'Hybridisation → shape?', [
    ('sp', 'linear', False), ('sp²', 'trigonal planar', False), ('sp³', 'tetrahedral', False),
    ('sp³d', 'trigonal bipyramidal', False), ('sp³d²', 'octahedral', False)], term='Hybridisation and shape')

os.makedirs(OUT, exist_ok=True)
print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
