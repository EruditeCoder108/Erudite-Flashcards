import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Chemistry', 'class11-chemistry-ch07-redox-reactions')
d = Deck('Chapter 7: Redox Reactions', 'Class 11', ['class-11', 'chemistry', 'ch-7'])
d.description = 'Classical and electronic redox, oxidation number rules, types of redox reactions, balancing by two methods, redox titrations and electrode potentials'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
DC = (1001, 817)

# ---------------------------------------------------------------- intro
d.sec('7.0-intro')
d.basic('Everyday processes that are redox?', 'Burning fuels, extraction of reactive metals, making caustic soda, batteries, ' + T('corrosion'))
d.basic('Environmental issues linked to redox (NCERT)?', T('Hydrogen economy') + ' (liquid H₂ as fuel) and the ' + T('ozone hole'))

# ---------------------------------------------------------------- 7.1 Classical
d.sec('7.1-classical-idea')
d.basic('Original meaning of oxidation?', 'Addition of ' + T('oxygen') + ': 2Mg + O₂ → 2MgO; S + O₂ → SO₂')
d.cloze('Classical oxidation: addition of {{c1::oxygen/electronegative element}} or removal of {{c2::hydrogen/electropositive element}}.')
d.cloze('Classical reduction: removal of {{c1::oxygen/electronegative element}} or addition of {{c2::hydrogen/electropositive element}}.')
d.basic('Why is 2H₂S + O₂ → 2S + 2H₂O an oxidation of H₂S?', T('Removal of hydrogen') + ' from H₂S')
d.basic('Why is K₄[Fe(CN)₆] → K₃[Fe(CN)₆] (with H₂O₂) an oxidation?', 'Removal of the electropositive element ' + T('potassium'))
d.basic('Classify: 2HgO → 2Hg + O₂; 2FeCl₃ + H₂ → 2FeCl₂ + 2HCl; C₂H₄ + H₂ → C₂H₆.', 'All ' + T('reductions') + ': removal of O; removal of Cl; addition of H')
d.basic('2HgCl₂ + SnCl₂ → Hg₂Cl₂ + SnCl₄: what is oxidised and reduced?', 'HgCl₂ ' + T('reduced') + ' (Hg added); SnCl₂ ' + T('oxidised') + ' (Cl added)')
d.basic('Why the word "redox"?', 'Oxidation and reduction ' + T('always occur together'))
d.basic('Problem 7.1: oxidised/reduced in H₂S + Cl₂ → 2HCl + S; 3Fe₃O₄ + 8Al → 9Fe + 4Al₂O₃; 2Na + H₂ → 2NaH?', '(i) H₂S oxidised, Cl₂ reduced. (ii) Al oxidised, Fe₃O₄ reduced. (iii) Na oxidised, H₂ reduced.')

# ---------------------------------------------------------------- 7.2 Electron transfer
d.sec('7.2-electron-transfer')
d.cloze('Oxidation = {{c1::loss}} of electrons; reduction = {{c2::gain}} of electrons; oxidising agent = electron {{c3::acceptor}}; reducing agent = electron {{c4::donor}}.')
d.basic('Mnemonic for electron transfer? (intuition)', '"' + T('OIL RIG') + '": Oxidation Is Loss, Reduction Is Gain')
d.basic('What is a half reaction?', 'One step showing only ' + T('loss or gain of electrons') + ', e.g. 2Na → 2Na⁺ + 2e⁻')
d.basic('In 2Na + Cl₂ → 2NaCl, which is the reducing agent?', T('Na') + ' (it donates electrons and is itself oxidised)')
d.basic('Why is 2Na + H₂ → 2NaH redox? (Problem 7.2)', 'NaH is Na⁺H⁻: Na → Na⁺ + e⁻ (oxidised); H₂ + 2e⁻ → 2H⁻ (reduced)')
d.basic('Zn strip in Cu(NO₃)₂ solution: observations?', 'Reddish copper coats the zinc; ' + T('blue colour disappears'), **fig('fig_7_1_zn_in_cu_nitrate'))
d.basic('Test for Zn²⁺ formed in that reaction?', 'Pass ' + T('H₂S') + ' in ammoniacal solution: white ' + T('ZnS'))
d.basic('Cu strip in ZnSO₄: what happens?', X('No reaction') + ': not even CuS (a very sensitive test) forms; equilibrium greatly favours Zn²⁺ + Cu')
d.basic('Cu in AgNO₃ solution?', 'Solution turns ' + T('blue') + ' (Cu²⁺); silver deposits: Cu + 2Ag⁺ → Cu²⁺ + 2Ag', **fig('fig_7_2_cu_in_silver_nitrate'))
d.basic('Co in NiSO₄: which side is favoured?', X('Neither') + ': both Ni²⁺ and Co²⁺ present at moderate concentrations')
d.basic('Electron-releasing order of Zn, Cu, Ag?', T('Zn > Cu > Ag'))
d.basic('What does electron competition lead to?', 'The ' + T('activity (electrochemical) series') + ' and galvanic cells')

# ---------------------------------------------------------------- 7.3 Oxidation number
d.sec('7.3-oxidation-number')
d.basic('Why is H₂ + ½O₂ → H₂O called redox though no ions form?', 'Electrons ' + T('shift') + ' partially from H to O; oxidation number treats it as complete transfer (book-keeping)')
d.basic('Define oxidation number.', 'Charge an atom would have if every bonding pair belonged entirely to the ' + T('more electronegative') + ' atom')
d.cloze('Rules: free elements have O.N. {{c1::0}}; a monatomic ion has O.N. = its {{c2::charge}}; alkali metals {{c3::+1}}, alkaline earths {{c4::+2}}, Al {{c5::+3}} in compounds.')
d.basic('Oxidation number of oxygen: usual and exceptions?', 'Usually ' + N('−2') + '; peroxides ' + X('−1') + '; superoxides ' + X('−½') + '; OF₂ ' + X('+2') + '; O₂F₂ ' + X('+1'))
d.basic('Oxidation number of hydrogen: usual and exception?', N('+1') + '; ' + X('−1') + ' in binary metal hydrides (LiH, NaH, CaH₂)')
d.basic('Oxidation number of halogens?', 'F always ' + N('−1') + '; Cl, Br, I are −1 as halides but ' + T('positive') + ' with oxygen (oxoacids)')
d.basic('Sum of oxidation numbers in a neutral compound and an ion?', 'Zero in a compound; equal to the ' + T('ion charge') + ' in a polyatomic ion')
d.basic('Highest oxidation number of a representative element?', 'Group number (groups 1, 2); ' + T('group number − 10') + ' for groups 13–17', **fig('tab_highest_oxidation_numbers'))
d.basic('O.N. of Mn in K₂MnO₄ and of B in NaBH₄?', 'Mn ' + N('+6') + '; B ' + N('+3') + ' (H is −1)')
d.basic('O.N. of O in CaO₂ and of S in H₂S₂O₇?', 'O ' + N('−1') + ' (peroxide); S ' + N('+6'))
d.basic('What is Stock notation?', 'Roman numeral for the metal’s O.N. in brackets: Au(I)Cl, Au(III)Cl₃, Sn(II)Cl₂, Sn(IV)Cl₄ (Alfred Stock)')
d.basic('Stock notation for HAuCl₄, Tl₂O, Fe₂O₃, CuI, MnO₂? (Problem 7.3)', 'HAu(III)Cl₄, Tl₂(I)O, Fe₂(III)O₃, Cu(I)I, Mn(IV)O₂')
d.cloze('In terms of O.N.: oxidation = {{c1::increase}} in O.N.; reduction = {{c2::decrease}} in O.N.; an oxidant {{c3::increases}} another element’s O.N.')
d.basic('2Cu₂O + Cu₂S → 6Cu + SO₂: oxidant and reductant? (Problem 7.4)', 'Cu(+1) → 0 reduced; S(−2) → +4 oxidised. ' + T('Cu(I)') + ' is the oxidant; ' + T('S of Cu₂S') + ' is the reductant.')
d.basic('Fractional oxidation numbers: examples?', 'C₃O₂: ' + N('4/3') + '; Br₃O₈: ' + N('16/3') + '; S₄O₆²⁻: ' + N('2.5'))
d.basic('What does a fractional O.N. really mean?', 'An ' + T('average') + ': atoms are in different whole-number states (e.g. S₄O₆²⁻ has S at +5, 0, 0, +5)')
d.basic('Real oxidation states in C₃O₂ and Br₃O₈?', 'C₃O₂: +2, 0, +2. Br₃O₈: +6, +4, +6.')
d.basic('Mixed oxides with fractional average O.N.?', E('Fe₃O₄, Mn₃O₄, Pb₃O₄'))
d.basic('O.N. of I in KI₃ and of Fe in Fe₃O₄? (Ex 7.2)', 'I: ' + N('−1/3') + ' (really I⁻·I₂). Fe: ' + N('+8/3') + ' (Fe²⁺ + 2Fe³⁺).')
d.basic('O.N. of S in H₂SO₅ by formula vs by structure? (Ex 7.5)', 'Formula gives ' + X('+8') + ' (impossible); structure has a peroxide O–O, so S is ' + T('+6'))

d.sec('7.3.1-types-of-redox-reactions')
table_card(d, 'Types of redox reactions', 'Example?', [
    ('Combination', 'C + O₂ → CO₂; 3Mg + N₂ → Mg₃N₂', False), ('Decomposition', '2KClO₃ → 2KCl + 3O₂', False),
    ('Metal displacement', 'CuSO₄ + Zn → Cu + ZnSO₄', False), ('Non-metal displacement', '2Na + 2H₂O → 2NaOH + H₂', False),
    ('Disproportionation', '2H₂O₂ → 2H₂O + O₂', False)], term='Four types of redox reactions')
d.basic('When is a combination reaction redox?', 'When ' + T('A or B (or both) is an element'))
d.basic('Is every decomposition a redox reaction?', X('No') + ': CaCO₃ → CaO + CO₂ has no O.N. change')
d.basic('Metal displacement reactions in metallurgy?', 'V₂O₅ + 5Ca → 2V + 5CaO; TiCl₄ + 2Mg → Ti + 2MgCl₂; Cr₂O₃ + 2Al → Al₂O₃ + 2Cr')
d.basic('Which metals displace H₂ from cold water?', 'All ' + T('alkali metals') + ' and Ca, Sr, Ba')
d.basic('Which metals need steam to give H₂?', E('Mg and Fe'))
d.basic('Correction: NCERT writes 2Fe + 3H₂O → Fe₂O₃ + 3H₂. What does iron actually give with steam?', T('3Fe + 4H₂O → Fe₃O₄ + 4H₂') + ' (magnetic oxide)')
d.basic('Metals that don’t react with steam but displace H₂ from acids?', E('Cadmium and tin'))
d.basic('Rate of H₂ evolution with HCl: Mg, Zn, Fe?', T('Mg fastest') + ', Fe slowest')
d.basic('Metals that don’t react even with HCl?', X('Ag and Au') + ' (occur native)')
d.basic('Oxidising power order of halogens?', T('F₂ > Cl₂ > Br₂ > I₂'))
d.basic('What does F₂ do with water?', 'Displaces oxygen: 2H₂O + 2F₂ → ' + T('4HF + O₂'))
d.basic('Basis of the "layer test" for Br⁻ and I⁻?', 'Cl₂ displaces Br₂/I₂, which dissolve in ' + T('CCl₄') + ' with characteristic colour')
d.basic('Can Br₂ displace I⁻?', T('Yes') + ': Br₂ + 2I⁻ → 2Br⁻ + I₂')
d.basic('How is F₂ obtained from F⁻?', 'Only by ' + T('electrolysis') + ': no chemical oxidant is stronger than F₂')
d.basic('Define disproportionation.', 'An element in one oxidation state is ' + T('simultaneously oxidised and reduced'))
d.basic('Requirement for a species to disproportionate?', 'Element must have at least ' + T('three oxidation states') + ' and be in an ' + T('intermediate') + ' one')
d.basic('Disproportionation of P₄, S₈, Cl₂ in alkali?', 'P₄ → PH₃ (−3) + H₂PO₂⁻ (+1); S₈ → S²⁻ (−2) + S₂O₃²⁻ (+2); Cl₂ → Cl⁻ (−1) + ClO⁻ (+1)')
d.basic('Everyday use of Cl₂ + 2OH⁻ → ClO⁻ + Cl⁻ + H₂O?', 'Household ' + T('bleach') + ' (ClO⁻ oxidises coloured stains)')
d.basic('Why does fluorine not disproportionate?', 'Most electronegative: it ' + X('cannot show positive') + ' oxidation states (F₂ + OH⁻ gives F⁻ + OF₂)')
d.basic('Which of ClO⁻, ClO₂⁻, ClO₃⁻, ClO₄⁻ won’t disproportionate? (Problem 7.5)', T('ClO₄⁻') + ': Cl is already +7 (highest)')
d.basic('Classify N₂ + O₂ → 2NO; 2Pb(NO₃)₂ → 2PbO + 4NO₂ + O₂; NaH + H₂O → NaOH + H₂; 2NO₂ + 2OH⁻ → NO₂⁻ + NO₃⁻ + H₂O. (Problem 7.6)', 'Combination; decomposition; displacement; ' + T('disproportionation'))
d.basic('Why does Pb₃O₄ give Cl₂ with HCl but PbO₂ with HNO₃? (Problem 7.7)', 'Pb₃O₄ = 2PbO + PbO₂. PbO₂ (+4) ' + T('oxidises Cl⁻') + ' to Cl₂; HNO₃ is itself an oxidant, so PbO₂ stays unreacted.')

d.sec('7.3.2-balancing-redox')
d.cloze('Oxidation number method: assign O.N.s → equalise {{c1::increase and decrease}} → balance charge with {{c2::H⁺ (acid) or OH⁻ (base)}} → balance H with {{c3::H₂O}} → check O.')
d.basic('Balanced: Cr₂O₇²⁻ + SO₃²⁻ in acid → Cr³⁺ + SO₄²⁻. (Problem 7.8)', 'Cr₂O₇²⁻ + 3SO₃²⁻ + 8H⁺ → 2Cr³⁺ + 3SO₄²⁻ + 4H₂O')
d.basic('Balanced: MnO₄⁻ + Br⁻ in base → MnO₂ + BrO₃⁻. (Problem 7.9)', '2MnO₄⁻ + Br⁻ + H₂O → 2MnO₂ + BrO₃⁻ + 2OH⁻')
steps_card(d, 'Half-reaction method', 'Balance Fe²⁺ + Cr₂O₇²⁻ → Fe³⁺ + Cr³⁺ (acid).', 'Balance each half, then equalise electrons.',
           ['Cr₂O₇²⁻ + 14H⁺ + 6e⁻ → 2Cr³⁺ + 7H₂O', 'Fe²⁺ → Fe³⁺ + e⁻ (× 6)', 'Add: <b>6Fe²⁺ + Cr₂O₇²⁻ + 14H⁺ → 6Fe³⁺ + 2Cr³⁺ + 7H₂O</b>'], 0, 'Dichromate–ferrous balancing', '6Fe²⁺ + Cr₂O₇²⁻ + 14H⁺ → 6Fe³⁺ + 2Cr³⁺ + 7H₂O')
d.basic('Half-reaction method: how to handle basic medium?', 'Balance as in acid, then add ' + T('OH⁻ equal to H⁺') + ' on both sides and combine into H₂O')
d.basic('Balanced: MnO₄⁻ + I⁻ in base → MnO₂ + I₂. (Problem 7.10)', '2MnO₄⁻ + 6I⁻ + 4H₂O → 2MnO₂ + 3I₂ + 8OH⁻')
d.basic('Electrons gained by MnO₄⁻ in acid, neutral/weakly basic, strongly basic? (JEE)', 'Acid → Mn²⁺: ' + N('5') + '; neutral → MnO₂: ' + N('3') + '; strong base → MnO₄²⁻: ' + N('1'))
d.basic('Trap: sanity check while balancing by O.N.?', 'If two things are reduced and nothing oxidised, a ' + X('formula or O.N. is wrong'))

d.sec('7.3.3-redox-titrations')
d.basic('Why is KMnO₄ a self-indicator?', 'Intensely purple: the first ' + T('lasting pink tinge') + ' marks the end point (at ~10⁻⁶ M MnO₄⁻)')
d.basic('Indicator for dichromate titrations?', T('Diphenylamine') + ': oxidised after the equivalence point to intense blue')
d.basic('What is the equivalence point?', 'Where oxidant and reductant are equal in ' + T('mole stoichiometry'))
d.basic('Iodometric reactions with Cu²⁺?', '2Cu²⁺ + 4I⁻ → Cu₂I₂ + I₂; then I₂ + 2S₂O₃²⁻ → 2I⁻ + ' + T('S₄O₆²⁻'))
d.basic('End point in iodometry?', 'Starch gives ' + T('intense blue') + ' with I₂; colour vanishes when thiosulphate consumes all I₂')
d.basic('How does iodine stay in solution though insoluble in water?', 'As ' + T('KI₃') + ' in KI solution')
d.basic('Modern view of oxidation and reduction (limitation of O.N.)?', 'Oxidation = ' + T('decrease in electron density') + '; reduction = increase')

# ---------------------------------------------------------------- 7.4 Electrode processes
d.sec('7.4-electrode-processes')
d.basic('Zn rod in CuSO₄: how is electron transfer made indirect?', 'Separate Zn|ZnSO₄ and Cu|CuSO₄ in two beakers, link by a wire and a ' + T('salt bridge'))
d.basic('Define a redox couple and its notation.', 'Oxidised and reduced forms of a species in a half reaction, written ' + T('oxidised/reduced') + ': Zn²⁺/Zn, Cu²⁺/Cu')
d.basic('What is a salt bridge made of, and its job?', 'U-tube of ' + T('KCl or NH₄NO₃') + ' set in agar-agar jelly; electrical contact without mixing')
d.occlusion('Figure 7.3 · Daniell cell', M + 'fig_7_3_daniell_cell.webp', DC, [
    ('Anode', [6, 136, 124, 54], True), ('Cathode', [842, 140, 158, 54], True), ('Salt bridge', [428, 376, 130, 98], True),
    ('Oxidation', [160, 704, 180, 56], True), ('Reduction', [626, 704, 192, 56], True)])
d.basic('Direction of electron flow vs current in a Daniell cell?', 'Electrons: ' + T('Zn → Cu') + ' through the wire; current flows the ' + T('opposite way'))
d.basic('Define standard electrode potential.', 'Electrode potential with all species at ' + T('unit concentration') + ' (gases 1 atm) and ' + N('298 K'))
d.basic('Reference electrode and its E°?', 'Standard ' + T('hydrogen electrode') + ': E° = ' + N('0.00 V'))
d.basic('Meaning of negative vs positive E°?', T('Negative') + ': stronger reducing agent than H⁺/H₂. ' + T('Positive') + ': weaker reducing agent (stronger oxidant).')
d.basic('Strongest oxidant and strongest reductant in Table 7.1?', 'Oxidant: ' + T('F₂') + ' (+2.87 V). Reductant: ' + T('Li') + ' (−3.05 V).', **fig('tab_7_1_electrode_potentials'))
d.basic('E° of Cu²⁺/Cu and Zn²⁺/Zn?', N('+0.34 V') + ' and ' + N('−0.76 V'))
d.basic('Why does Zn displace Cu²⁺ but not the reverse? (intuition)', 'Zn²⁺/Zn has a ' + T('more negative') + ' E°: zinc gives up electrons more readily, like water flowing downhill')
d.basic('Mnemonic for reading the E° table? (intuition)', '"' + T('Top-left grabs, bottom-right gives') + '"<br>High E° oxidised forms are strong oxidants<br>Low E° reduced forms are strong reductants')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Summary', 'Oxidation means?', [
    ('Classical', 'Add O / electronegative element; remove H / electropositive', False),
    ('Electronic', 'Loss of electrons', False), ('Oxidation number', 'Increase in O.N.', False),
    ('Modern', 'Decrease in electron density', False)], term='Evolving definitions of oxidation')
table_card(d, 'Summary', 'Oxidation number?', [
    ('O in H₂O₂', '−1', True), ('O in KO₂', '−½', True), ('O in OF₂', '+2', True),
    ('H in NaH', '−1', True), ('S in S₄O₆²⁻ (average)', '+2.5', False), ('Cr in Cr₂O₇²⁻', '+6', False)], term='Oxidation number exceptions')

n = d.write(os.path.join(OUT, 'deck.json'))
print(n, 'cards')
