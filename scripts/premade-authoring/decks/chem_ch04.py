import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch04-chemical-bonding')
d = Deck('Chapter 4: Chemical Bonding and Molecular Structure', 'Class 11', ['class-11', 'chemistry', 'ch-4'])

# ---------------------------------------------------------------- Intro
d.sec('introduction')
d.basic('What is a chemical bond?', 'The ' + T('attractive force') + ' that holds atoms or ions together in a chemical species')
d.basic('Why do atoms form bonds at all?', 'To ' + T('lower the energy') + ' of the system and become more stable')

# ---------------------------------------------------------------- 4.1 Kössel–Lewis
d.sec('4.1-kossel-lewis')
d.basic("What was the Lewis 'kernel'?", 'The ' + T('nucleus + inner electrons') + ' of an atom (positively charged)')
d.basic('What do the dots in a Lewis symbol stand for?', 'The ' + T('valence electrons'))
d.basic('How do you get the group valence from a Lewis symbol?', 'Number of dots, or ' + N('8 − number of dots'))
d.basic('What is electrovalence?', 'The number of ' + T('unit charges') + ' on the ion (e.g. Ca²⁺ → ' + N('2') + ')')
d.cloze('Octet rule: atoms combine by {{c1::transfer}} or {{c2::sharing}} of valence electrons so as to have an {{c3::octet}} in their valence shells.')
d.basic("Who introduced the term 'covalent bond'?", T('Langmuir'))
d.basic('Name a molecule with two double bonds and one with a triple bond.', E('CO₂') + ' (two C=O); ' + E('N₂') + ' or ' + E('C₂H₂') + ' (triple)')
d.basic('In a Lewis structure, which atom usually goes in the centre?', 'The ' + T('least electronegative') + ' atom')
d.basic('How do charges change the electron count for a Lewis structure?', 'Add ' + N('1') + ' e⁻ per negative charge; subtract ' + N('1') + ' e⁻ per positive charge')
d.basic('Lewis structure of CO: what bond joins C and O?', 'A ' + T('triple bond') + ', with one lone pair on each atom')

d.sec('4.1.4-formal-charge')
d.basic('Formula for formal charge on an atom in a Lewis structure?',
        r'Formal charge \(= V - L - \tfrac{1}{2}S\)<br><small>V = valence e⁻ of free atom, L = lone-pair e⁻, S = shared (bonding) e⁻</small>')
d.basic('Formal charges on the three O atoms of O₃?', 'Central O: ' + N('+1') + '; double-bonded end O: ' + N('0') + '; single-bonded end O: ' + N('−1'))
d.basic('Which Lewis structure is usually the lowest-energy one?', 'The one with the ' + T('smallest formal charges'))
d.basic('Do formal charges show real charge separation?', X('No') + '. They only help track valence electrons')

d.sec('4.1.5-octet-limitations')
d.basic('Give three molecules with an incomplete octet on the central atom.', E('LiCl, BeH₂, BCl₃') + ' (also AlCl₃, BF₃)')
d.basic('Give two odd-electron molecules.', E('NO') + ' and ' + E('NO₂'))
d.basic('Why can third-period elements have an expanded octet?', 'They have ' + T('d orbitals') + ' available for bonding')
d.basic('Give three examples of an expanded octet.', E('PF₅, SF₆, H₂SO₄'))
d.basic('Name a sulphur compound where S obeys the octet rule.', E('SCl₂'))
d.basic('Which noble gas compounds challenge the octet rule?', E('XeF₂, KrF₂, XeOF₂'))
d.basic('Two more drawbacks of the octet theory?', 'It does not explain ' + T('shapes') + ' of molecules, or their ' + T('relative stability') + ' (energy)')

# ---------------------------------------------------------------- 4.2 Ionic bond
d.sec('4.2-ionic-bond')
d.basic('Which elements form ionic bonds most easily?', 'Low ' + T('ionisation enthalpy') + ' (metal) + highly negative ' + T('electron gain enthalpy') + ' (non-metal)')
d.basic('Which common cation is made only of non-metals?', E('NH₄⁺') + ' (ammonium)')
d.basic('Is ionisation always endothermic?', 'Yes. ' + X('Electron gain') + ' can be exothermic or endothermic')
d.basic('What truly decides the stability of an ionic compound?', 'Its ' + T('lattice enthalpy') + ', not just reaching an octet')
d.basic('Define lattice enthalpy.', 'Energy needed to completely separate ' + N('1 mol') + ' of a solid ionic compound into gaseous ions')
d.basic('Lattice enthalpy of NaCl?', N('788 kJ mol⁻¹'))
d.basic('Na → Na⁺ costs 495.8 kJ/mol and Cl → Cl⁻ releases only 348.7 kJ/mol. Why does NaCl still form?',
        'The ' + T('lattice enthalpy') + ' released (' + N('788 kJ mol⁻¹') + ') more than compensates')

# ---------------------------------------------------------------- 4.3 Bond parameters
d.sec('4.3-bond-parameters')
d.basic('Define bond length.', 'Equilibrium distance between the ' + T('nuclei') + ' of two bonded atoms')
d.basic('Bond length R of molecule AB in terms of covalent radii?', r'\(R = r_A + r_B\)')
d.cloze('Covalent radius is half the distance between two similar atoms bonded {{c1::in the same molecule}}; van der Waals radius is half the distance between two similar atoms {{c2::in separate molecules}} in a solid.')
d.basic('Which is larger for chlorine: covalent or van der Waals radius?', T('van der Waals') + ' (' + N('180 pm') + ' vs ' + N('99 pm') + ')')
d.basic('Define bond enthalpy.', 'Energy to break ' + N('1 mol') + ' of bonds of a type between two atoms in the ' + T('gaseous') + ' state')
table_card(d, '4.3.3 · Bond enthalpy', 'Bond enthalpy (kJ mol⁻¹)?', [
    ('H–H', '435.8', False), ('O=O', '498', False), ('N≡N', '946', False), ('H–Cl', '431', False)], term='Bond enthalpies: H2, O2, N2, HCl')
d.basic('Why is average bond enthalpy used for polyatomic molecules like H₂O?', 'Breaking successive O–H bonds needs ' + T('different energies') + ' (' + N('502') + ' vs ' + N('427 kJ mol⁻¹') + ')')
d.basic('Average O–H bond enthalpy in water?', r'\(\frac{502 + 427}{2} = \) ' + N('464.5 kJ mol⁻¹'))
table_card(d, 'Table 4.2 · Bond lengths', 'Carbon–carbon bond length (pm)?', [
    ('C–C', '154', False), ('C=C', '133', False), ('C≡C', '120', False)], term='C–C, C=C, C≡C bond lengths')
d.basic('Bond order in the Lewis picture?', 'The ' + T('number of bonds') + ' between the two atoms')
d.basic('Which species share bond order 3 by being isoelectronic?', E('N₂, CO, NO⁺'))
d.basic('Which species share bond order 1 by being isoelectronic?', E('F₂') + ' and ' + E('O₂²⁻'))
d.cloze('As bond order increases, bond enthalpy {{c1::increases}} and bond length {{c2::decreases}}.')

d.sec('4.3.5-resonance')
d.basic('Both O–O bonds in O₃ are 128 pm. How does this compare with single and double bonds?', 'Between O–O (' + N('148 pm') + ') and O=O (' + N('121 pm') + ')')
d.basic('What is a resonance hybrid?', 'The single real structure that the ' + T('canonical forms') + ' together describe')
d.basic('How is resonance shown?', 'With a ' + T('double-headed arrow') + ' (↔)')
d.basic('How does resonance affect energy?', 'It ' + T('stabilises') + ' the molecule: the hybrid has ' + T('lower energy') + ' than any canonical form')
d.basic('Do canonical forms really exist?', X('No') + '. The molecule does not switch between them, and they are not in equilibrium')
d.basic('How many canonical forms does CO₃²⁻ have, and how do its C–O bonds compare?', N('Three') + '; all C–O bonds are ' + T('equivalent'))
d.basic('C–O bond length in CO₂ (115 pm) lies between which two values?', 'C=O ' + N('121 pm') + ' and C≡O ' + N('110 pm'))

d.sec('4.3.6-polarity')
d.basic('Which is a non-polar covalent bond: H–H or H–F?', T('H–H') + ' (identical atoms share equally)')
d.basic('Formula and unit of dipole moment?', r'\(\mu = Q \times r\)' + '<br>Unit: ' + T('debye (D)') + ', ' + N('1 D = 3.33564 × 10⁻³⁰ C m'))
d.basic('Is dipole moment a scalar or a vector?', T('Vector'))
d.basic('In the chemist\'s crossed arrow for a dipole, where are the cross and the head?', 'Cross on the ' + T('positive') + ' end, head on the ' + T('negative') + ' end')
d.basic('Dipole moment of H₂O?', N('1.85 D') + ' (bent, H–O–H ' + N('104.5°') + ')')
d.basic('Why is the dipole moment of BeF₂ zero?', 'Linear: two equal bond dipoles ' + T('cancel'))
d.basic('Why is the dipole moment of BF₃ zero though B–F bonds are polar?', 'Trigonal planar at ' + N('120°') + ': the three bond moments sum to ' + T('zero'))
d.basic('Why is μ(NH₃) greater than μ(NF₃)?',
        'In NH₃ the lone-pair dipole points the ' + T('same way') + ' as the N–H bond moments; in NF₃ it points ' + X('opposite') + ' to the N–F moments')
d.basic('Dipole moments of NH₃ and NF₃?', 'NH₃: ' + N('1.47 D') + '; NF₃: ' + N('0.23 D'))
d.basic('Order of dipole moments: HF, HCl, HBr, HI?', 'HF > HCl > HBr > HI (' + N('1.78 > 1.07 > 0.79 > 0.38 D') + ')')
d.basic('CH₄ and CCl₄ have μ = 0. What is μ of CHCl₃?', N('1.04 D'))

d.sec('fajans-rules')
d.cloze("Fajans' rules: covalent character of an ionic bond increases with a {{c1::smaller}} cation, a {{c2::larger}} anion, and a {{c3::greater charge}} on the cation.")
d.basic('Which is more polarising for the same size and charge: a transition-metal cation or an alkali metal cation?',
        T('Transition-metal') + ' type, (n−1)dⁿns⁰')

# ---------------------------------------------------------------- 4.4 VSEPR
d.sec('4.4-vsepr')
d.basic('Who proposed VSEPR theory, and who refined it?', T('Sidgwick and Powell') + ' (' + N('1940') + '); refined by ' + T('Nyholm and Gillespie') + ' (' + N('1957') + ')')
d.basic('According to VSEPR, what decides the shape of a molecule?', 'The number of ' + T('valence shell electron pairs') + ' (bonded + lone) around the central atom')
d.basic('How does VSEPR treat a double or triple bond?', 'As a ' + T('single super pair'))
d.basic('Order of electron-pair repulsions?', 'lp–lp > lp–bp > bp–bp')
d.basic('Why do lone pairs repel more than bond pairs?', 'A lone pair is held by ' + T('one nucleus only') + ', so it spreads out and takes more space')
table_card(d, 'Table 4.6 · No lone pair', 'Geometry for each type?', [
    ('AB₂ · BeCl₂', 'Linear, 180°', False), ('AB₃ · BF₃', 'Trigonal planar, 120°', False),
    ('AB₄ · CH₄', 'Tetrahedral, 109.5°', False), ('AB₅ · PCl₅', 'Trigonal bipyramidal', False),
    ('AB₆ · SF₆', 'Octahedral', False)], term='VSEPR: geometry with no lone pairs')
table_card(d, 'Table 4.7 · With lone pairs', 'Shape of each?', [
    ('AB₂E · SO₂', 'Bent', False), ('AB₃E · NH₃', 'Trigonal pyramidal', False), ('AB₂E₂ · H₂O', 'Bent', False),
    ('AB₄E · SF₄', 'See-saw', False), ('AB₃E₂ · ClF₃', 'T-shape', False),
    ('AB₅E · BrF₅', 'Square pyramid', False), ('AB₄E₂ · XeF₄', 'Square planar', False)], term='VSEPR: shapes with lone pairs')
d.basic('H–N–H angle in NH₃ and why?', N('107°') + ' (from 109.5°): lp–bp repulsion > bp–bp')
d.basic('Why is the bond angle in H₂O (104.5°) less than in NH₃ (107°)?', 'H₂O has ' + N('two') + ' lone pairs, and lp–lp repulsion is strongest')
d.basic('In SF₄, is the lone pair axial or equatorial, and why?', T('Equatorial') + ': only two lp–bp repulsions at 90° (vs three if axial)')
d.basic('In ClF₃, where do the two lone pairs sit?', T('Equatorial') + ' positions, giving a ' + T('T-shape'))
d.basic('For which elements does VSEPR predict shapes especially well?', T('p-block') + ' compounds')

# ---------------------------------------------------------------- 4.5 VB theory
d.sec('4.5-valence-bond')
d.basic('Who introduced valence bond theory?', T('Heitler and London') + ' (' + N('1927') + '), developed by ' + T('Pauling'))
d.basic('Why does H₂ form when two H atoms approach?', 'New ' + T('attractive') + ' forces exceed the new repulsive ones, so energy falls to a minimum')
d.basic('Bond length and bond enthalpy of H₂?', N('74 pm') + '; ' + N('435.8 kJ mol⁻¹'))
d.basic('What decides the strength of a covalent bond in VB theory?', 'The ' + T('extent of overlap') + ': greater overlap, stronger bond')
d.basic('When is an overlap positive (bond-forming)?', 'The orbitals have the ' + T('same sign (phase)') + ' and orientation')
d.basic('What H–C–H angle would simple (unhybridised) overlap predict for CH₄?', N('90°') + ' (but the real angle is ' + N('109.5°') + ')')

d.sec('4.5.4-sigma-pi')
d.basic('How is a σ bond formed?', T('Head-on (axial) overlap') + ' along the internuclear axis')
d.basic('Which overlaps can give a σ bond?', 's–s, s–p, p–p (head-on)')
d.basic('How is a π bond formed?', T('Sidewise overlap') + ': orbital axes parallel, perpendicular to the internuclear axis')
d.basic('Which is stronger, σ or π, and why?', T('σ') + '. Its orbitals overlap to a larger extent')
d.basic('Can a π bond exist without a σ bond between two atoms?', X('No') + '. π bonds form in addition to a σ bond')
d.basic('With x as the internuclear axis, which pair cannot form a σ bond: 1s+1s, 1s+2pₓ, 2p_y+2p_y, 1s+2s?', T('2p_y + 2p_y') + ' (sidewise → π)')
d.basic('Number of σ and π bonds in C₂H₂ and C₂H₄?', 'C₂H₂: ' + N('3σ, 2π') + '; C₂H₄: ' + N('5σ, 1π'))

# ---------------------------------------------------------------- 4.6 Hybridisation
d.sec('4.6-hybridisation')
d.basic('Who introduced hybridisation?', T('Pauling'))
d.basic('Define hybridisation.', 'Intermixing of orbitals of ' + T('slightly different energies') + ' to form a new set of orbitals of ' + T('equivalent energy and shape'))
d.basic('How many hybrid orbitals form from n atomic orbitals?', N('n') + ' (always equal)')
d.cloze('Conditions for hybridisation: only {{c1::valence shell}} orbitals mix; they must have {{c2::almost equal energy}}; promotion of electrons is {{c3::not essential}}.')
d.basic('Can filled orbitals take part in hybridisation?', 'Yes. Not only half-filled ones')
table_card(d, '4.6.1 · s–p hybrids', '% s-character and angle?', [
    ('sp', '50% s · 180° · linear', False), ('sp²', '33% s · 120° · trigonal planar', False),
    ('sp³', '25% s · 109.5° · tetrahedral', False)], term='sp, sp2, sp3: s-character and angle')
d.basic('Other name for sp hybridisation?', T('Diagonal') + ' hybridisation')
d.basic('Hybridisation and shape of BeCl₂?', T('sp') + ', linear (' + N('180°') + ')')
d.basic('Hybridisation and shape of BCl₃?', T('sp²') + ', trigonal planar (' + N('120°') + ')')
d.basic('Hybridisation of N in NH₃ and O in H₂O?', 'Both ' + T('sp³') + ' (lone pairs in hybrid orbitals)')
d.basic('Ethane: C–C and C–H bond lengths?', 'C–C ' + N('154 pm') + ' (sp³–sp³); C–H ' + N('109 pm'))
d.basic('Ethene: what makes up the C=C bond?', 'One ' + T('sp²–sp² σ') + ' + one ' + T('π') + ' (from unhybridised 2p orbitals)')
d.basic('Bond angles in ethene?', 'H–C–H ' + N('117.6°') + '; H–C–C ' + N('121°'))
d.basic('What makes up the C≡C bond in ethyne?', N('1 σ') + ' (sp–sp) + ' + N('2 π'))
d.basic('Why is no hybridisation of 3p, 3d and 4s possible?', 'The energy gap between ' + T('3p and 4s') + ' is significant')
table_card(d, '4.6.3 · Hybrids with d orbitals', 'Shape and example?', [
    ('dsp²', 'Square planar · [Ni(CN)₄]²⁻', False), ('sp³d', 'Trigonal bipyramidal · PCl₅', False),
    ('sp³d²', 'Square pyramidal · BrF₅ / octahedral · SF₆', False), ('d²sp³', 'Octahedral · [Co(NH₃)₆]³⁺', False)],
    term='d-orbital hybridisation: shapes and examples')
d.basic('In PCl₅, how do equatorial and axial bonds differ?', 'Equatorial: three at ' + N('120°') + '. Axial: two at ' + N('90°') + ' to that plane, ' + T('longer and weaker'))
d.basic('Why are axial bonds in PCl₅ longer than equatorial ones?', 'Axial bond pairs suffer ' + T('more repulsion') + ' from equatorial bond pairs')
d.basic('Hybridisation and geometry of SF₆?', T('sp³d²') + ', regular octahedral')
d.basic('AlCl₃ + Cl⁻ → AlCl₄⁻: change in hybridisation of Al?', T('sp²') + ' → ' + T('sp³'))
d.basic('BF₃ + NH₃ → F₃B–NH₃: change in hybridisation of B and N?', 'B: ' + T('sp² → sp³') + '; N: stays ' + T('sp³'))

# ---------------------------------------------------------------- 4.7 MO theory
d.sec('4.7-mo-theory')
d.basic('Who developed molecular orbital theory?', T('F. Hund and R.S. Mulliken') + ' (' + N('1932') + ')')
d.basic('Atomic orbital vs molecular orbital: how many nuclei influence the electron?', 'AO: ' + T('monocentric') + ' (one nucleus). MO: ' + T('polycentric'))
d.basic('Two atomic orbitals combine. How many MOs form?', N('Two') + ': one ' + T('bonding') + ', one ' + T('antibonding'))
d.basic('LCAO expressions for σ and σ*?', r'\(\sigma = \psi_A + \psi_B\)<br>\(\sigma^* = \psi_A - \psi_B\)')
d.cloze('A bonding MO forms by {{c1::constructive}} interference; an antibonding MO by {{c2::destructive}} interference.')
d.basic('What lies between the nuclei in an antibonding MO?', 'A ' + T('nodal plane') + ' (zero electron density)')
d.cloze('Conditions for LCAO: combining AOs must have {{c1::the same or nearly the same energy}}, {{c2::the same symmetry about the molecular axis}}, and {{c3::maximum overlap}}.')
d.basic('Can 2p_z of one atom combine with 2pₓ of the other (z = molecular axis)?', X('No') + '. Different ' + T('symmetry'))
d.basic('Which MOs are symmetrical about the bond axis: σ or π?', T('σ') + ' (π are not)')
d.cloze('For {{c1::B₂, C₂ and N₂}}, the π2p MOs lie {{c2::below}} σ2p_z; for O₂ and F₂, σ2p_z lies below π2p.')
d.basic('Bond order formula in MO theory?', r'Bond order \(= \tfrac{1}{2}(N_b - N_a)\)')
d.basic('What bond order means a molecule cannot exist?', T('Zero or negative') + ' (N_b ≤ N_a)')
d.basic('When is a molecule paramagnetic in MO terms?', 'When one or more MOs are ' + T('singly occupied') + ' (unpaired electrons)')

d.sec('4.8-homonuclear-diatomics')
d.basic('Bond order of He₂, and does it exist?', N('0') + ', so it ' + X('does not exist'))
d.basic('Does Be₂ exist?', X('No') + '. Bond order ' + N('0'))
d.basic('Bond order and magnetism of Li₂?', N('1') + '; ' + T('diamagnetic') + ' (exists in the vapour phase)')
d.basic('What is unusual about the double bond in C₂?', 'Both bonds are ' + T('π bonds') + ' (no σ)')
mo_card(d, 'O₂', 12, True, 'Bond order and magnetism of O₂?',
        'N<sub>b</sub> = 10, N<sub>a</sub> = 6 → B.O. = <span class="n">2</span><br>Two unpaired e⁻ in π* → <b>paramagnetic</b>',
        'MO diagram of O2', 'O₂: bond order 2, paramagnetic (2 unpaired e⁻ in π*2p)')
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
table_card(d, 'Oxygen species', 'Bond order and magnetism?', [
    ('O₂⁺', '2.5 · paramagnetic', False), ('O₂', '2 · paramagnetic', False),
    ('O₂⁻ (superoxide)', '1.5 · paramagnetic', False), ('O₂²⁻ (peroxide)', '1 · diamagnetic', False)],
    note='Stability: O₂⁺ > O₂ > O₂⁻ > O₂²⁻', term='O2+, O2, O2-, O2 2-: bond order and magnetism')
d.basic('Which of B₂ to F₂ has the highest bond enthalpy?', T('N₂') + ' (' + N('945 kJ mol⁻¹') + ', bond order 3)')

# ---------------------------------------------------------------- 4.9 Hydrogen bonding
d.sec('4.9-hydrogen-bonding')
d.basic('To which atoms must H be bonded to form hydrogen bonds?', 'Highly electronegative ' + T('F, O or N'))
d.basic('Define hydrogen bond.', 'The attractive force binding the ' + T('H atom') + ' of one molecule to an ' + T('electronegative atom (F, O, N)') + ' of another')
d.basic('Is a hydrogen bond weaker or stronger than a covalent bond?', T('Weaker'))
d.basic('Is a hydrogen bond weaker or stronger than van der Waals forces?', T('Stronger'))
d.basic('In which physical state is hydrogen bonding strongest?', T('Solid') + ' (weakest in gas)')
d.basic('Give examples of intermolecular hydrogen bonding.', E('HF, water, alcohols'))
d.basic('Give an example of intramolecular hydrogen bonding.', E('o-Nitrophenol') + ' (H between two O atoms)')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
