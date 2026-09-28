import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch03-classification-of-elements-and-periodicity')
d = Deck('Chapter 3: Classification of Elements and Periodicity in Properties', 'Class 11', ['class-11', 'chemistry', 'ch-3'])
d.description = 'Triads to Mendeleev, modern periodic law, IUPAC names above 100, s p d f blocks, and trends in radius, ionization enthalpy, electron gain enthalpy, electronegativity'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
TR = (1001, 717)

# ---------------------------------------------------------------- 3.1
d.sec('3.1-why-classify')
d.basic('Number of elements known in 1800 and in 1865?', N('31') + ' in 1800; ' + N('63') + ' by 1865')
d.basic('Why classify elements?', 'To study them ' + T('systematically') + ', rationalise known facts and ' + T('predict new ones'))
d.basic('Update: NCERT says "at present 114 elements are known". Current count?', N('118') + ' elements, all officially named by IUPAC (NCERT itself says "up to 118" later)')

# ---------------------------------------------------------------- 3.2 Genesis
d.sec('3.2-genesis-of-periodic-classification')
d.basic('Dobereiner’s law of triads (1829)?', 'In groups of three similar elements, the ' + T('middle element’s atomic weight') + ' ≈ average of the other two')
d.basic('Name Dobereiner’s three triads.', E('Li, Na, K') + '; ' + E('Ca, Sr, Ba') + '; ' + E('Cl, Br, I'), **fig('tab_3_1_triads'))
d.basic('Why was the law of triads dismissed?', 'Worked only for a ' + X('few elements') + ': seen as coincidence')
d.basic('Who made a cylindrical table of elements, and when?', T('A.E.B. de Chancourtois') + ' (French geologist), ' + N('1862'))
d.basic('Newlands’ law of octaves (1865)?', 'In order of atomic weight, every ' + T('eighth element') + ' resembles the first, like musical octaves', **fig('tab_3_2_octaves'))
d.basic('Limitation of the law of octaves?', 'Held only up to ' + X('calcium'))
d.basic('Award later given to Newlands?', T('Davy Medal') + ', ' + N('1887') + ', Royal Society')
d.basic('Who independently proposed the periodic law in 1869?', T('Dmitri Mendeleev') + ' (Russian) and ' + T('Lothar Meyer') + ' (German)')
d.basic('What did Lothar Meyer plot?', T('Atomic volume') + ', m.p. and b.p. vs atomic weight: a periodic pattern')
d.basic('Mendeleev’s periodic law?', 'Properties of elements are a periodic function of their ' + T('atomic weights'))
d.basic('What did Mendeleev rely on most while classifying?', 'Similarities in ' + T('empirical formulas and properties of compounds') + ' (oxides, hydrides)')
d.basic('Why was iodine placed after tellurium though lighter?', 'To group it with ' + T('F, Cl, Br') + ' by properties; Mendeleev suspected wrong atomic weights')
d.basic('What were eka-aluminium and eka-silicon?', 'Gaps left by Mendeleev: later ' + T('gallium') + ' and ' + T('germanium'))
table_card(d, 'Table 3.3', 'Found value?', [
    ('Eka-Al atomic weight (pred. 68)', 'Ga: 70', False), ('Eka-Al density (pred. 5.9)', 'Ga: 5.94 g/cm³', False),
    ('Eka-Al m.p. (pred. low)', 'Ga: 302.93 K', False), ('Eka-Si atomic weight (pred. 72)', 'Ge: 72.6', False),
    ('Eka-Si oxide / chloride', 'GeO₂ / GeCl₄', False)], term='Mendeleev’s predictions vs found')
d.basic('Mendeleev’s table (Fig. 3.1): what did it look like?', 'Groups I–VIII in columns with oxide formulas (R₂O … RO₄); ' + T('series') + ' in rows', **fig('fig_3_1_mendeleev_table'))
d.basic('Why is Mendeleev credited over Meyer?', 'He published first, used broader properties, left ' + T('gaps') + ' and made bold ' + T('successful predictions'))

# ---------------------------------------------------------------- 3.3 Modern
d.sec('3.3-modern-periodic-law')
d.basic('Moseley’s observation (1913)?', 'A plot of ' + r'\( \sqrt{\nu} \)' + ' (X-ray frequency) vs ' + T('atomic number') + ' is a straight line; not vs atomic mass')
d.basic('Modern periodic law?', 'Properties are periodic functions of ' + T('atomic numbers'))
d.basic('Mendeleev vs modern periodic law: basic difference?', 'Atomic ' + T('weight') + ' vs atomic ' + T('number'))
d.basic('What is the periodic law really a consequence of?', 'Periodic variation in ' + T('electronic configurations'))
d.basic('Naturally occurring elements, and which are found in pitchblende?', N('94') + '; Np and Pu (like Ac and Pa) occur in pitchblende')
d.basic('Long-form table: number of periods and groups?', N('7') + ' periods, ' + N('18') + ' groups (IUPAC, replacing IA … VIIA, VIII, IB … VIIB, 0)', **fig('fig_3_2_long_form'))
d.basic('What does the period number tell you?', 'The highest ' + T('principal quantum number (n)') + ' of the elements')
d.cloze('Elements per period: 1st {{c1::2}}, 2nd and 3rd {{c2::8}}, 4th and 5th {{c3::18}}, 6th {{c4::32}}.')
d.basic('Why are lanthanoids and actinoids placed at the bottom?', 'To keep the table’s structure and keep ' + T('similar elements in one column'))
d.basic('Whose work placed actinoids below lanthanoids? Element named after him?', T('Glenn T. Seaborg') + ' (Nobel 1951); element 106 ' + T('Seaborgium (Sg)'))

# ---------------------------------------------------------------- 3.4 IUPAC
d.sec('3.4-nomenclature-above-100')
d.basic('Why did IUPAC introduce systematic names?', 'Disputes over discovery credit, e.g. element 104: ' + T('Rutherfordium') + ' (US) vs ' + T('Kurchatovium') + ' (USSR)')
d.cloze('IUPAC roots: 0 = {{c1::nil}}, 1 = {{c2::un}}, 2 = {{c3::bi}}, 3 = tri, 4 = {{c4::quad}}, 5 = pent, 6 = hex, 7 = sept, 8 = oct, 9 = {{c5::enn}}.', extra='Add "ium" at the end; symbol = first letters of the roots.')
d.basic('Full table of roots (Table 3.4)?', 'nil, un, bi, tri, quad, pent, hex, sept, oct, enn', **fig('tab_3_4_iupac_roots'))
d.basic('IUPAC name and symbol for Z = 120? (Problem 3.1)', T('Unbinilium, Ubn'))
d.basic('IUPAC systematic name of Z = 104, 109, 114?', 'Unnilquadium (Unq), Unnilennium (Une), Ununquadium (Uuq)')
d.basic('Official names of Z = 113 to 118?', 'Nihonium (Nh), Flerovium (Fl), Moscovium (Mc), Livermorium (Lv), ' + T('Tennessine (Ts)') + ', ' + T('Oganesson (Og)'), **fig('tab_3_5_elements_above_100'))
d.basic('Elements named after Lawrence Berkeley Lab and Seaborg’s group? (Ex 3.7)', T('Lawrencium (103)') + ' and ' + T('Seaborgium (106)'))
d.basic('Trap: how many letters in a temporary IUPAC symbol?', N('Three') + ' (e.g. Uuo); official symbols have one or two')

# ---------------------------------------------------------------- 3.5 Configurations
d.sec('3.5-electronic-configuration-and-periodic-table')
d.basic('Number of elements in a period equals?', 'Twice the number of ' + T('orbitals') + ' in the level being filled')
d.basic('Where does the 3d series start and end?', T('Scandium (Z = 21)') + ', 3d¹4s², to ' + T('zinc (Z = 30)') + ', 3d¹⁰4s²')
d.basic('Why 18 elements in the 5th period? (Problem 3.2)', '5s, 4d, 5p = 1 + 5 + 3 = ' + N('9 orbitals') + ' → 18 electrons')
d.basic('Why 32 elements in the 6th period? (Ex 3.4)', '6s, 4f, 5d, 6p = 1 + 7 + 5 + 3 = ' + N('16 orbitals') + ' → 32')
d.cloze('Lanthanoids: 4f filling from {{c1::cerium (Z = 58)}} to {{c2::lutetium (Z = 71)}}. Actinoids: 5f filling after {{c3::actinium (Z = 89)}}.')
d.basic('Group 1 valence configuration?', T('ns¹') + ' (Li [He]2s¹ … Fr [Rn]7s¹)')
d.basic('Period and group of Z = 114? (Ex 3.5)', 'Period ' + N('7') + ', group ' + N('14') + ' (Flerovium)')
d.basic('Element in period 3, group 17? (Ex 3.6)', T('Chlorine, Z = 17'))

# ---------------------------------------------------------------- 3.6 Blocks
d.sec('3.6-s-p-d-f-blocks')
d.basic('Basis of dividing elements into s, p, d, f blocks?', 'The ' + T('orbital being filled') + ' by the last electron', **fig('fig_3_3_blocks'))
d.basic('Two exceptions to block placement?', T('Helium') + ' (s-block but put with noble gases, 1s² closed shell) and ' + T('hydrogen') + ' (placed separately)')
d.basic('Why is hydrogen placed separately?', 'It can lose an electron like ' + T('group 1') + ' or gain one like ' + T('group 17'))
d.basic('s-block: groups and configuration?', 'Groups ' + N('1 and 2') + '; ns¹ and ns²')
d.basic('s-block properties?', 'Reactive metals, low ionisation enthalpy, form 1+/2+ ions; ' + X('never free') + ' in nature')
d.basic('Which s-block compounds are not predominantly ionic?', X('Li and Be') + ' compounds')
d.basic('p-block: groups and configuration?', 'Groups ' + N('13–18') + '; ns²np¹ to ns²np⁶')
d.basic('Representative (main group) elements are?', T('s-block + p-block'))
d.basic('Chalcogens and halogens are groups?', 'Chalcogens: ' + T('16') + '; halogens: ' + T('17'))
d.basic('d-block: groups and general configuration?', 'Groups ' + N('3–12') + '; ' + T('(n−1)d¹⁻¹⁰ ns⁰⁻²'))
d.basic('d-block element with ns⁰?', X('Pd') + ': 4d¹⁰ 5s⁰')
d.basic('Typical properties of transition elements?', T('Coloured ions') + ', ' + T('variable oxidation states') + ', ' + T('paramagnetism') + ', ' + T('catalysts'))
d.basic('Which d-block metals lack most transition properties, and why?', X('Zn, Cd, Hg') + ': (n−1)d¹⁰ns² (full d)')
d.basic('Why "transition" elements?', 'They form a bridge between reactive s-block metals and less active groups 13, 14')
d.basic('f-block general configuration?', T('(n−2)f¹⁻¹⁴ (n−1)d⁰⁻¹ ns²'))
d.basic('Lanthanoid and actinoid ranges?', 'Lanthanoids ' + T('Ce (58) – Lu (71)') + '; actinoids ' + T('Th (90) – Lr (103)'))
d.basic('Why is actinoid chemistry harder?', T('Many oxidation states') + '; all ' + T('radioactive') + '; many made only in nanograms')
d.basic('What are transuranium elements?', 'Elements ' + T('after uranium') + ' (Z > 92)')
d.basic('Group and configuration of Z = 117 and Z = 120? (Problem 3.3)', '117: ' + T('group 17') + ', [Rn]5f¹⁴6d¹⁰7s²7p⁵. 120: ' + T('group 2') + ', [Og]8s².')
d.basic('Update: NCERT Problem 3.3 says Z = 117 is "not yet discovered". Status?', 'Discovered in ' + N('2010') + ', named ' + T('Tennessine (Ts)') + ' in 2016; Z = 120 is still undiscovered')

d.sec('3.6.5-metals-nonmetals-metalloids')
d.basic('What fraction of elements are metals?', 'More than ' + N('78%'))
d.basic('Metals with very low melting points?', X('Mercury') + ' (liquid); ' + E('gallium') + ' (303 K) and ' + E('caesium') + ' (302 K)')
d.basic('Non-metals with high melting points (exceptions)?', X('Boron and carbon'))
d.basic('Name the metalloids given in NCERT.', E('Si, Ge, As, Sb, Te'))
d.basic('Trend in metallic character?', 'Increases ' + T('down a group') + '; decreases ' + T('left to right'))
d.basic('Increasing metallic character: Si, Be, Mg, Na, P? (Problem 3.4)', T('P < Si < Be < Mg < Na'))
d.basic('Group with a metal, a non-metal, a liquid and a gas at room T? (Ex 3.27)', T('Group 17') + ' (At metallic, I solid non-metal, Br liquid, F/Cl gases)')

# ---------------------------------------------------------------- 3.7 Trends
d.sec('3.7.1-atomic-and-ionic-radius')
d.basic('Why can’t atomic size be measured precisely?', 'Atoms are tiny (~1.2 Å) and the electron cloud has ' + X('no sharp boundary'))
d.basic('Covalent radius, e.g. chlorine?', 'Half the single-bond distance: Cl₂ 198 pm → ' + N('99 pm'))
d.basic('Metallic radius, e.g. copper?', 'Half the distance between metal cores: 256 pm → ' + N('128 pm'))
d.basic('Why is atomic radius of noble gases not compared with others?', 'They are monatomic: their (van der Waals) radii are ' + T('much larger') + ' than covalent radii')
d.basic('Atomic radii of period 2 (pm)?', 'Li 152, Be 111, B 88, C 77, N 74, O 66, F 64', **fig('tab_3_6a_radii_period'))
d.basic('Atomic radius across a period and why?', T('Decreases') + ': same shell, ' + T('Zeff increases'), **fig('fig_3_4a_radius_period'))
d.basic('Atomic radius down a group and why?', T('Increases') + ': n increases and inner shells shield', **fig('fig_3_4b_radius_group'))
d.basic('Atomic radii down group 1 and group 17 (pm)?', 'Li 152, Na 186, K 231, Rb 244, Cs 262; F 64, Cl 99, Br 114, I 133, At 140', **fig('tab_3_6b_radii_group'))
d.basic('Why is a cation smaller than its atom?', 'Fewer electrons, ' + T('same nuclear charge') + ' (Na 186 → Na⁺ 95 pm)')
d.basic('Why is an anion larger than its atom?', 'Extra electron → more ' + T('repulsion') + ', lower Zeff (F 64 → F⁻ 136 pm)')
d.basic('What are isoelectronic species?', 'Atoms/ions with the ' + T('same number of electrons') + ', e.g. O²⁻, F⁻, Na⁺, Mg²⁺ (10 e⁻)')
d.basic('Radius trend among isoelectronic ions?', 'Greater positive charge → ' + T('smaller') + '; greater negative charge → ' + T('larger'))
d.basic('Increasing ionic radius: N³⁻, O²⁻, F⁻, Na⁺, Mg²⁺, Al³⁺? (Ex 3.12)', T('Al³⁺ < Mg²⁺ < Na⁺ < F⁻ < O²⁻ < N³⁻'))
d.basic('Largest and smallest: Mg, Mg²⁺, Al, Al³⁺? (Problem 3.5)', 'Largest ' + T('Mg') + '; smallest ' + T('Al³⁺'))
d.basic('Isoelectronic partners of F⁻, Ar, Mg²⁺, Rb⁺? (Ex 3.11)', 'F⁻: Na⁺/Ne. Ar: Cl⁻/K⁺. Mg²⁺: Na⁺/Ne. Rb⁺: Br⁻/Kr.')

d.sec('3.7.1-ionization-enthalpy')
d.basic('Define first ionization enthalpy.', 'Energy to remove an electron from an ' + T('isolated gaseous atom') + ' in its ground state: X(g) → X⁺(g) + e⁻')
d.basic('Why "isolated gaseous atom in ground state" in the definition? (Ex 3.14)', 'So values are ' + T('comparable') + ': no neighbour interactions, same starting state')
d.basic('Why is ΔᵢH₂ > ΔᵢH₁?', 'Harder to remove an electron from a ' + T('positive ion') + ' than from a neutral atom')
d.basic('Is ionization enthalpy ever negative?', X('No') + ': energy is always required')
d.basic('Where are maxima and minima in the ΔᵢH vs Z plot?', 'Maxima at ' + T('noble gases') + '; minima at ' + T('alkali metals'), **fig('fig_3_5_ie_vs_z'))
d.basic('ΔᵢH trend across a period and down a group?', T('Increases') + ' across; ' + T('decreases') + ' down', **fig('fig_3_6_ie_period_group'))
d.basic('Why does ΔᵢH increase across a period?', 'Nuclear charge rises but ' + T('shielding barely increases') + ' (same shell)')
d.basic('Why does ΔᵢH decrease down a group?', 'Electron farther away; ' + T('increased shielding') + ' outweighs rising nuclear charge')
d.basic('Why is ΔᵢH of B < Be?', 'B loses a ' + T('2p') + ' electron, more shielded and less penetrating than Be’s ' + T('2s'))
d.basic('Why is ΔᵢH of O < N?', 'O has a ' + T('paired 2p') + ' electron (extra repulsion); N’s 2p³ is half-filled')
d.basic('Actual order of ΔᵢH in period 2?', T('Li < B < Be < C < O < N < F < Ne'))
d.basic('Al ΔᵢH closer to 575 or 760 kJ/mol? (Problem 3.6: Na 496, Mg 737, Si 786)', N('575') + ': Al’s 3p electron is shielded by 3s')
d.basic('Na has lower ΔᵢH₁ than Mg but higher ΔᵢH₂. Why? (Ex 3.17)', 'Na⁺ has a ' + T('noble gas core') + ' (2p⁶); Mg⁺ still has a 3s electron')
d.basic('Ionization enthalpy of H in J/mol from E₁ = −2.18 × 10⁻¹⁸ J? (Ex 3.15)', '2.18 × 10⁻¹⁸ × 6.022 × 10²³ = ' + N('1.31 × 10⁶ J mol⁻¹'))
d.basic('Do two isotopes have the same ΔᵢH? (Ex 3.25)', T('Yes') + ': same electronic configuration and nuclear charge')
d.basic('Why does Ga have higher ΔᵢH than Al? (group 13 anomaly)', 'Poor shielding by ' + T('3d electrons') + ' in Ga raises Zeff')

d.sec('3.7.1-electron-gain-enthalpy')
d.basic('Define electron gain enthalpy.', 'Enthalpy change when a neutral ' + T('gaseous atom') + ' gains an electron: X(g) + e⁻ → X⁻(g)')
d.basic('Why do halogens have very negative ΔegH?', 'Gaining one electron gives a ' + T('noble gas configuration'))
d.basic('Why do noble gases have positive ΔegH?', 'The electron must enter the ' + X('next higher shell'))
d.basic('ΔegH trend across a period and down a group?', 'More negative ' + T('across') + '; less negative ' + T('down'))
d.basic('Why is ΔegH of F less negative than Cl (and O than S)?', 'Added electron enters the ' + T('small n = 2 shell') + ': strong repulsion')
d.basic('Most negative ΔegH of all elements?', T('Chlorine') + ' (−349 kJ/mol)', **fig('tab_3_7_electron_gain'))
d.basic('Most and least negative ΔegH: P, S, Cl, F? (Problem 3.7)', 'Most: ' + T('Cl') + '; least: ' + T('P'))
d.basic('Is the second electron gain enthalpy of O positive? (Ex 3.21)', T('Positive') + ': adding e⁻ to O⁻ faces strong repulsion')
d.basic('Electron affinity vs electron gain enthalpy (footnote)?', 'Aₑ = ' + T('−ΔegH') + ' (sign reversed); strictly defined at 0 K: ΔegH = −Aₑ − 5/2 RT')

d.sec('3.7.1-electronegativity')
d.basic('Define electronegativity.', 'Ability of an atom ' + T('in a compound') + ' to attract ' + T('shared electrons') + '; not measurable')
d.basic('Electron gain enthalpy vs electronegativity? (Ex 3.22)', 'ΔegH: ' + T('isolated atom') + ', measurable. EN: ' + T('bonded atom') + ', relative, not measurable.')
d.basic('Three electronegativity scales?', T('Pauling') + ' (most used), Mulliken-Jaffe, Allred-Rochow')
d.basic('Pauling’s reference value?', 'Fluorine = ' + N('4.0') + ' (assigned in 1922)')
d.basic('Pauling EN of period 2 and period 3?', 'Li 1.0, Be 1.5, B 2.0, C 2.5, N 3.0, O 3.5, F 4.0; Na 0.9 … Cl 3.0', **fig('tab_3_8a_en_period'))
d.basic('Is the EN of N always 3.0? (Ex 3.23)', X('No') + ': EN varies with the atom it is bonded to (and hybridisation)', **fig('tab_3_8b_en_group'))
d.basic('Link between EN and metallic character?', 'EN is directly related to ' + T('non-metallic') + ' and inversely to metallic character')
d.occlusion('Figure 3.7 · Periodic trends (name each arrow)', M + 'fig_3_7_trends.webp', TR, [
    ('Electron gain enthalpy', [340, 38, 305, 48], True), ('Ionization enthalpy', [372, 112, 240, 48], True),
    ('Atomic radius', [405, 586, 190, 46], True), ('Electronegativity', [405, 666, 210, 46], True),
    ('Electronegativity', [20, 160, 42, 282], True), ('Atomic radius', [84, 175, 44, 232], True),
    ('Ionization enthalpy', [860, 258, 42, 250], True), ('Electron gain enthalpy', [940, 240, 44, 285], True)])
d.basic('Mnemonic for trends? (intuition)', '"' + T('Size goes down-left, everything else goes up-right') + '": IE, EN, |ΔegH| rise towards F; radius rises towards Cs')

d.sec('3.7.2-chemical-properties')
d.basic('Valence of representative elements?', 'Number of valence electrons, or ' + T('8 − valence electrons'), **fig('tab_valence_groups'))
d.basic('Oxidation state of O in OF₂ and Na₂O?', N('+2') + ' in OF₂ (F more EN); ' + N('−2') + ' in Na₂O')
d.basic('Define oxidation state (NCERT).', 'Charge acquired by an atom on the basis of ' + T('electronegativity') + ' of other atoms in the molecule')
d.basic('Formulas from Si + Br and Al + S? (Problem 3.8)', T('SiBr₄') + ' and ' + T('Al₂S₃'))
d.basic('Hydride and oxide formulas across groups (Table 3.9)?', 'e.g. LiH, CaH₂, B₂H₆, CH₄, NH₃, H₂O, HF; Li₂O, MgO, B₂O₃, CO₂, N₂O₃, SO₃, Cl₂O₇', **fig('tab_3_9_hydrides_oxides'))
d.basic('Oxidation state vs covalency of Al in [AlCl(H₂O)₅]²⁺? (Problem 3.9)', 'Oxidation state ' + N('+3') + '; covalency ' + N('6'))
d.basic('What is the diagonal relationship?', 'Similarity of Li with ' + T('Mg') + ' and Be with ' + T('Al'), **fig('tab_anomalous_li_be'))
d.cloze('Second-period elements behave anomalously due to {{c1::small size}}, large {{c2::charge/radius ratio}}, high {{c3::electronegativity}} and only {{c4::four}} valence orbitals (2s, 2p).')
d.basic('Maximum covalency of B vs Al?', 'B: ' + N('4') + ' ([BF₄]⁻). Al: ' + N('6') + ' ([AlF₆]³⁻), using d orbitals.')
d.basic('What bonding is special to second-period p-block elements?', T('pπ–pπ multiple bonds') + ' (C=C, C≡C, N≡N, C=O, C≡N)')

d.sec('3.7.3-chemical-reactivity')
d.basic('Where in a period is reactivity highest and lowest?', 'Highest at the ' + T('two extremes') + ' (alkali metals, halogens); lowest in the ' + T('centre'))
d.basic('Oxide nature across a period?', T('Basic') + ' (left, e.g. Na₂O) → ' + T('amphoteric/neutral') + ' (centre) → ' + T('acidic') + ' (right, e.g. Cl₂O₇)')
d.basic('Examples of amphoteric and neutral oxides?', 'Amphoteric: ' + E('Al₂O₃, As₂O₃') + '. Neutral: ' + E('CO, NO, N₂O') + '.')
d.basic('Show Na₂O is basic and Cl₂O₇ acidic. (Problem 3.10)', 'Na₂O + H₂O → ' + T('2NaOH') + '; Cl₂O₇ + H₂O → ' + T('2HClO₄'))
d.basic('Reactivity order in group 1 vs group 17? (Ex 3.28)', 'Group 1: ' + T('Li < Na < K < Rb < Cs') + ' (easier e⁻ loss). Group 17: ' + T('F > Cl > Br > I') + ' (easier e⁻ gain).')
d.basic('Change in atomic radius across 3d and 4f series?', T('Much smaller') + ' than for representative elements; smallest for 4f')
d.basic('Trend in transition metals down a group?', 'Reverse of main groups: metallic character ' + X('does not rise') + ' (explained by size and IE)')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Summary', 'Across a period (→) / down a group (↓)?', [
    ('Atomic radius', '→ decreases; ↓ increases', False), ('Ionization enthalpy', '→ increases; ↓ decreases', False),
    ('Electron gain enthalpy', '→ more negative; ↓ less negative', False), ('Electronegativity', '→ increases; ↓ decreases', False),
    ('Metallic character', '→ decreases; ↓ increases', True)], term='Periodic trends summary')
table_card(d, 'Summary', 'Proposed by?', [
    ('Triads (1829)', 'Dobereiner', False), ('Cylindrical table (1862)', 'de Chancourtois', False),
    ('Octaves (1865)', 'Newlands', False), ('Periodic law by atomic weight (1869)', 'Mendeleev (and Lothar Meyer)', False),
    ('Atomic number as basis (1913)', 'Moseley', False)], term='History of periodic classification')

n = d.write(os.path.join(OUT, 'deck.json'))
print(n, 'cards')
