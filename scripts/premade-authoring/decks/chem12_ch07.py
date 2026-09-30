import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch07-alcohols-phenols-and-ethers')
d = Deck('Chapter 7: Alcohols, Phenols and Ethers', 'Class 12', ['class-12', 'chemistry', 'ch-7'])
d.description = 'Classification, naming, preparation, acidity, esterification, dehydration, oxidation, phenol ring reactions, Kolbe, Reimer–Tiemann, Williamson, ether cleavage'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- intro
d.sec('7.0-introduction')
d.basic('Alcohol vs phenol vs ether?', T('Alcohol') + ': –OH on an aliphatic carbon (CH₃OH)<br>' + T('Phenol') + ': –OH on an aromatic carbon (C₆H₅OH)<br>' + T('Ether') + ': R–O–R / Ar–O–R (CH₃OCH₃)')
d.basic('Everyday uses (chapter opener)?', 'Alcohols → detergents, phenols → ' + T('antiseptics') + ', ethers → ' + T('fragrances') + '; ethanol in wood-polishing spirit; sugar, cotton, paper contain –OH')

# ---------------------------------------------------------------- 7.1 Classification
d.sec('7.1-classification')
d.basic('Mono-, di-, trihydric alcohols?', 'One, two, three –OH groups: ' + E('C₂H₅OH, ethylene glycol, glycerol'), **fig('fig_mono_di_trihydric'))
d.basic('Mono-, di-, trihydric phenols?', 'One, two, three –OH on the ring (phenol, cresol; catechol; pyrogallol-type)', **fig('fig_phenols_hydric'))
d.basic('1°, 2°, 3° alcohols?', '–OH on a carbon attached to ' + N('1, 2, 3') + ' other carbons', **fig('fig_alcohol_1_2_3'))
d.basic('Allylic alcohols?', '–OH on an ' + T('sp³ carbon next to C=C') + '; can be 1°, 2° or 3°', **fig('fig_allylic_alcohols'))
d.basic('Benzylic alcohols?', '–OH on an ' + T('sp³ carbon next to an aromatic ring') + '; 1°, 2° or 3°', **fig('fig_benzylic_alcohols'))
d.basic('Vinylic alcohols?', '–OH on an ' + T('sp² carbon of C=C') + ' (or aryl carbon): CH₂=CH–OH')
d.basic('Simple vs mixed ethers?', T('Simple (symmetrical)') + ': both groups same (C₂H₅OC₂H₅). ' + T('Mixed (unsymmetrical)') + ': different (C₂H₅OCH₃, C₂H₅OC₆H₅).')
d.basic('Classify (Intext 7.1): (CH₃)₃CCH₂OH, CH₂=CHCH₂OH, C₆H₅CH(OH)CH₃, C₆H₅CH=CHC(OH)(CH₃)₂?', '1°, 1° (allylic), 2° (benzylic), 3° (allylic)')

# ---------------------------------------------------------------- 7.2 Nomenclature
d.sec('7.2-nomenclature')
d.basic('IUPAC naming of alcohols?', 'Replace "e" of the alkane with "' + T('ol') + '"; number from the end nearest –OH. Polyols keep the "e": ' + E('ethane-1,2-diol'))
d.cloze('IUPAC names: isopropyl alcohol = {{c1::propan-2-ol}}; isobutyl alcohol = {{c2::2-methylpropan-1-ol}}; tert-butyl alcohol = {{c3::2-methylpropan-2-ol}}; glycerol = {{c4::propane-1,2,3-triol}}.')
d.basic('Table 7.1: common and IUPAC names of alcohols', 'Table 7.1', **fig('tab_7_1_alcohol_names'))
d.basic('How are cyclic alcohols named?', 'Prefix ' + T('cyclo') + ', –OH at C-1: cyclohexanol, 2-methylcyclopentanol', **fig('fig_cyclic_alcohols'))
d.basic('IUPAC names of cresols?', 'o-, m-, p-cresol = ' + T('2-, 3-, 4-methylphenol'), **fig('fig_cresols'))
d.cloze('Benzenediols: catechol = {{c1::benzene-1,2-diol}}; resorcinol = {{c2::benzene-1,3-diol}}; hydroquinone (quinol) = {{c3::benzene-1,4-diol}}.')
d.basic('Identify the three benzenediols.', 'Catechol (1,2), resorcinol (1,3), hydroquinone (1,4)', **img('fig_benzenediols'))
d.basic('IUPAC naming of ethers?', 'Hydrocarbon with an ' + T('–OR / –OAr') + ' substituent; the ' + T('larger') + ' group is the parent (alkoxyalkane)')
d.cloze('Ether names: CH₃OCH₃ = {{c1::methoxymethane}}; C₂H₅OC₂H₅ = {{c2::ethoxyethane}}; anisole = {{c3::methoxybenzene}}; phenetole = {{c4::ethoxybenzene}}.')
d.basic('Table 7.2: common and IUPAC names of ethers', 'Table 7.2', **fig('tab_7_2_ether_names'))
d.basic('IUPAC names (Example 7.1): CH₃CH(Cl)CH(CH₃)CH(CH₃)CH₂OH and CH₃CH(CH₃)OCH₂CH₃?', T('4-Chloro-2,3-dimethylpentan-1-ol') + '; ' + T('2-ethoxypropane'))

# ---------------------------------------------------------------- 7.3 Structures
d.sec('7.3-structures')
d.basic('C–O–H angle in methanol and why?', N('108.9°') + ', slightly less than tetrahedral: ' + T('lone pair–lone pair repulsion') + ' on O', **fig('fig_7_1_structures'))
d.basic('Why is C–O in phenol (136 pm) shorter than in methanol (142 pm)?', '(i) ' + T('Partial double bond') + ' from lone pair conjugation with the ring; (ii) ' + T('sp²') + ' carbon')
d.basic('C–O–C angle in methoxymethane and why?', N('111.7°') + ', slightly more than tetrahedral: repulsion between the ' + T('bulky R groups') + '; C–O = 141 pm')

# ---------------------------------------------------------------- 7.4.1 Preparation of alcohols
d.sec('7.4.1-preparation-of-alcohols')
d.basic('Acid-catalysed hydration of alkenes: rule followed?', T('Markovnikov') + ': propene + H₂O/H⁺ → propan-2-ol', **fig('fig_hydration'))
d.basic('Mechanism of acid-catalysed hydration (3 steps)?', '1. ' + T('Protonation') + ' of alkene by H₃O⁺ → carbocation. 2. ' + T('Nucleophilic attack') + ' of water. 3. ' + T('Deprotonation') + '.', **fig('fig_hydration_mechanism'))
d.basic('Hydroboration–oxidation: reagents and outcome?', '(BH₃)₂, then ' + T('H₂O₂ / OH⁻') + ': propene → ' + T('propan-1-ol') + ' (looks anti-Markovnikov), excellent yield', **fig('fig_hydroboration'))
d.basic('Why is hydroboration "anti-Markovnikov"?', 'Boron attaches to the sp² carbon with ' + T('more H atoms') + '; OH later replaces B there')
d.basic('Who discovered hydroboration?', T('H.C. Brown') + ' (1959); Nobel 1979 shared with G. Wittig')
d.basic('Reducing aldehydes and ketones to alcohols?', 'H₂/Pt, Pd or Ni, or ' + T('NaBH₄ / LiAlH₄') + '. Aldehyde → ' + T('1°') + '; ketone → ' + T('2°') + '.', **fig('fig_carbonyl_reduction'))
d.basic('Reducing carboxylic acids to alcohols?', T('LiAlH₄') + ' → 1° alcohol (excellent yield)', **fig('fig_acid_lialh4'))
d.basic('Commercial route from acids to alcohols, and why?', 'LiAlH₄ is ' + X('expensive') + ': convert acid to ' + T('ester') + ', then catalytic hydrogenation', **fig('fig_ester_hydrogenation'))
d.basic('Grignard + carbonyl: mechanism?', 'Nucleophilic addition of R–MgX to C=O → ' + T('adduct') + '; hydrolysis → alcohol + Mg(OH)X', **fig('fig_grignard_mechanism'))
d.basic('Grignard product with HCHO, other aldehydes, ketones?', T('1°') + ', ' + T('2°') + ', ' + T('3°') + ' alcohol respectively', **fig('fig_grignard_overall'))
d.basic('Mnemonic: Grignard + carbonyl → which alcohol?', 'Count the R groups the carbonyl carbon ends with:<br>HCHO has 0 → R adds 1 → 1°<br>RCHO has 1 → 2°<br>R₂CO has 2 → 3°')
d.basic('Products (Example 7.2): catalytic reduction of butanal; propene + dil. H₂SO₄; propanone + CH₃MgBr then H₂O?', T('Butan-1-ol') + '; ' + T('propan-2-ol') + '; ' + T('2-methylpropan-2-ol'))
d.basic('Primary alcohols from HCHO + Grignard (Intext 7.4): (CH₃)₂CHCH₂OH and cyclohexylmethanol?', T('(CH₃)₂CHMgBr') + ' + HCHO; ' + T('cyclohexylmagnesium bromide') + ' + HCHO')

# ---------------------------------------------------------------- 7.4.2 Preparation of phenols
d.sec('7.4.2-preparation-of-phenols')
d.basic('Another name for phenol, and first source?', T('Carbolic acid') + '; first isolated from ' + T('coal tar') + ' (19th century)')
d.basic('Phenol from chlorobenzene?', 'Fuse with NaOH at ' + N('623 K, 320 atm') + ' → sodium phenoxide; acidify', **fig('fig_phenol_from_haloarene'))
d.basic('Trap: NCERT gives 300 atm in Ch 6 but 320 atm in Ch 7 for this. Which to write?', 'Either is accepted; remember ' + T('623 K and ~300 atm') + ' (high T and P because aryl C–Cl is unreactive)')
d.basic('Phenol from benzenesulphonic acid?', 'Benzene + ' + T('oleum') + ' → C₆H₅SO₃H; fuse with ' + T('molten NaOH') + ' → phenoxide; acidify', **fig('fig_phenol_from_sulphonic'))
d.basic('Phenol from aniline?', 'Aniline + NaNO₂ + HCl (273–278 K) → ' + T('benzenediazonium chloride') + '; warm with water → phenol + N₂', **fig('fig_phenol_from_diazonium'))
d.basic('Cumene process?', 'Cumene (isopropylbenzene) + ' + T('O₂ (air)') + ' → cumene hydroperoxide; ' + T('dil. acid') + ' → ' + T('phenol + acetone'), **fig('fig_cumene_process'))
d.basic('Why is the cumene process important?', 'Most of the world’s phenol is made this way; ' + T('acetone') + ' is a valuable by-product')

# ---------------------------------------------------------------- 7.4.3 Physical properties
d.sec('7.4.3-physical-properties')
d.basic('Effect of chain length and branching on b.p. of alcohols?', 'More C: ' + T('higher') + ' (van der Waals). More branching: ' + X('lower') + ' (less surface area).')
d.basic('Why do alcohols and phenols boil higher than ethers, hydrocarbons, haloalkanes of similar mass?', T('Intermolecular hydrogen bonding'), **fig('fig_hbond_alcohol_phenol'))
d.basic('Boiling points of ethanol, methoxymethane, propane?', N('351 K') + ' > ' + N('248 K') + ' > ' + N('231 K') + ' (similar masses 46, 46, 44)', **fig('fig_bp_comparison'))
d.basic('Why are lower alcohols miscible with water? Trend?', 'They ' + T('H-bond with water') + '; solubility falls as the hydrophobic alkyl/aryl part grows')
d.basic('Increasing b.p. (Example 7.3): pentan-1-ol, butan-1-ol, butan-2-ol, ethanol, propan-1-ol, methanol?', 'Methanol < ethanol < propan-1-ol < butan-2-ol < butan-1-ol < pentan-1-ol')
d.basic('Increasing b.p.: pentan-1-ol, n-butane, pentanal, ethoxyethane?', 'n-Butane < ethoxyethane < pentanal < pentan-1-ol')

# ---------------------------------------------------------------- 7.4.4 Reactions: O-H cleavage
d.sec('7.4.4-reactions-overview')
d.basic('How can alcohols act as nucleophiles and as electrophiles?', 'Nucleophile: O attacks, ' + T('O–H bond breaks') + '. Electrophile: protonated alcohol, ' + T('C–O bond breaks') + '.', **fig('fig_nucleophile_electrophile'))

d.sec('7.4.4a-acidity')
d.basic('Reaction of alcohols and phenols with Na, K, Al?', 'Give ' + T('alkoxides / phenoxides + H₂'), **fig('fig_reaction_with_metals'))
d.basic('Which reacts with aqueous NaOH: alcohol or phenol?', 'Only ' + T('phenol') + ' (→ sodium phenoxide + H₂O)', **fig('fig_phenol_naoh'))
d.basic('Alcohols and phenols as Brönsted acids?', 'They donate a proton to a stronger base, forming alkoxide / phenoxide (conjugate bases)', **fig('fig_bronsted_acid'))
d.basic('Acid strength order of alcohols, and reason?', T('1° > 2° > 3°') + ': alkyl groups (+I) push electron density onto O, reducing O–H polarity', **fig('fig_alcohol_acidity_order'))
d.basic('Alcohols vs water as acids?', 'Alcohols are ' + X('weaker') + ' acids than water; so alkoxides are ' + T('stronger bases') + ' than OH⁻ (NaOEt > NaOH)', **fig('fig_water_alkoxide'))
d.basic('Why can alcohols also act as Brönsted bases?', 'Lone pairs on O accept protons')
d.basic('Why is the O of phenol’s –OH slightly positive?', 'Resonance puts the O lone pair into the ring', **fig('fig_phenol_resonance'))
d.basic('Why is phenol more acidic than alcohols? (2 reasons)', '(i) ' + T('sp² carbon') + ' is more electronegative, polarising O–H. (ii) ' + T('Phenoxide is resonance-stabilised') + ' (charge delocalised); alkoxide charge is localised.', **fig('fig_ionisation'))
d.basic('Resonance structures of phenoxide ion?', 'Negative charge delocalised onto ' + T('o- and p-carbons'), **fig('fig_phenoxide_resonance'))
d.basic('Why is phenoxide more stable than phenol itself?', 'Phenol’s resonance structures involve ' + X('charge separation') + '; phenoxide’s do not')
d.basic('pKa of phenol vs ethanol, and meaning?', N('10.0') + ' vs ' + N('15.9') + ': phenol is about a ' + T('million times') + ' more acidic (higher pKa = weaker acid)', **fig('tab_7_3_pka'))
d.basic('Effect of –NO₂ and –CH₃ on phenol acidity?', '–NO₂ (EWG) ' + T('increases') + ' acidity, most at ' + T('o/p') + '; –CH₃ (EDG) ' + X('decreases') + ' it (cresols weaker than phenol)')
d.cloze('pKa values: o-nitrophenol {{c1::7.2}}; m-nitrophenol {{c2::8.3}}; p-nitrophenol {{c3::7.1}}; phenol {{c4::10.0}}; ethanol {{c5::15.9}}.')
d.basic('Increasing acid strength (Example 7.4): propan-1-ol, 2,4,6-trinitrophenol, 3-nitrophenol, 3,5-dinitrophenol, phenol, 4-methylphenol?', 'Propan-1-ol < 4-methylphenol < phenol < 3-nitrophenol < 3,5-dinitrophenol < 2,4,6-trinitrophenol')
d.basic('Why is picric acid a strong acid?', 'Three ' + T('–NO₂') + ' groups pull electrons and stabilise the phenoxide')
d.basic('Intuition: why do EWGs at o/p help more than at m?', 'Phenoxide’s negative charge sits on o/p carbons.<br>An NO₂ there can ' + T('soak up') + ' that charge by resonance; at meta only inductively')

d.sec('7.4.4b-esterification')
d.basic('Esterification of alcohols and phenols?', 'With RCOOH or (RCO)₂O (conc. H₂SO₄ catalyst) or RCOCl (' + T('pyridine') + ') → esters', **fig('fig_esterification'))
d.basic('Why remove water in acid esterification?', 'The reaction is ' + T('reversible') + '; removing water pushes it forward')
d.basic('Role of pyridine with acid chlorides?', 'Base that ' + T('neutralises HCl') + ', shifting equilibrium right')
d.basic('What is acetylation? Example?', 'Introducing CH₃CO–: salicylic acid + acetic anhydride → ' + T('aspirin') + ' (acetylsalicylic acid)', **fig('fig_aspirin'))
d.basic('Properties of aspirin?', T('Analgesic, anti-inflammatory, antipyretic'))

# ---------------------------------------------------------------- C-O cleavage
d.sec('7.4.4c-c-o-cleavage-in-alcohols')
d.basic('Do phenols undergo C–O cleavage reactions?', X('Only with zinc') + '; the others are alcohols only')
d.basic('What is the Lucas test?', 'Alcohol + ' + T('conc. HCl + ZnCl₂') + ': 3° → turbidity ' + T('immediately') + '; 1° → ' + X('no turbidity') + ' at room temperature (2° in a few minutes)')
d.basic('Why does turbidity appear in the Lucas test?', 'Alcohols dissolve in the reagent; the alkyl halides formed are ' + T('immiscible'))
d.basic('Alcohol + PBr₃?', T('Alkyl bromide'))
d.basic('Dehydration of alcohols: reagents?', 'Conc. H₂SO₄ or H₃PO₄, anhyd. ZnCl₂ or alumina → alkene; ethanol with conc. H₂SO₄ at ' + N('443 K'), **fig('fig_ethanol_dehydration'))
d.basic('Dehydration conditions for 2° and 3° alcohols?', 'Milder: butan-2-ol with 85% H₃PO₄ at 440 K; 2-methylpropan-2-ol with 20% H₃PO₄ at 358 K', **fig('fig_dehydration_2_3'))
d.basic('Ease of dehydration?', T('3° > 2° > 1°') + ' (carbocation stability)')
d.basic('Mechanism of dehydration of ethanol (NCERT)?', '1. Protonation (ethyl oxonium ion). 2. Loss of water → carbocation (' + T('slow, rate-determining') + '). 3. Loss of H⁺ → ethene.', **fig('fig_dehydration_mechanism'))
d.basic('Insight: does ethanol really form a CH₃CH₂⁺ carbocation?', 'A 1° carbocation is very unstable; for 1° alcohols the steps effectively merge (' + T('E2-like') + '). Write NCERT’s 3 steps in exams; the carbocation route is real for ' + T('2° and 3°') + '.')
d.basic('How is dehydration equilibrium driven forward?', 'Remove ' + T('ethene') + ' as it forms; the acid of step 1 is regenerated in step 3')

d.sec('7.4.4d-oxidation')
d.basic('What happens in alcohol oxidation?', 'C=O forms with cleavage of O–H and C–H: a ' + T('dehydrogenation'), **fig('fig_oxidation_to_acid'))
d.basic('Oxidant for 1° alcohol → carboxylic acid?', T('Acidified KMnO₄') + ' (strong)')
d.basic('Oxidant to stop at the aldehyde?', T('CrO₃ in anhydrous medium'), **fig('fig_cro3_aldehyde'))
d.basic('Best reagent for 1° alcohol → aldehyde? What is it?', T('PCC') + ' (pyridinium chlorochromate: CrO₃ + pyridine + HCl); e.g. but-2-en-1-ol → but-2-enal', **fig('fig_pcc'))
d.basic('Oxidation of 2° alcohols?', '→ ' + T('ketones') + ' (CrO₃)', **fig('fig_sec_alcohol_ketone'))
d.basic('Oxidation of 3° alcohols?', X('Resist') + ' oxidation; with strong oxidants/heat, C–C cleaves → mixture of acids with fewer C')
d.basic('Heated Cu at 573 K on 1°, 2°, 3° alcohols?', '1° → ' + T('aldehyde') + '; 2° → ' + T('ketone') + '; 3° → ' + T('alkene') + ' (dehydration)', **fig('fig_cu_573k'))
d.basic('Mnemonic: Cu at 573 K?', '"1° and 2° lose H₂; 3° loses H₂O" (no H on the carbinol carbon to lose)')
d.basic('Why is methanol poisonous? Treatment?', 'Oxidised to ' + T('methanal → methanoic acid') + ' (blindness, death). Treat with IV ' + T('diluted ethanol') + ': it swamps the enzyme so kidneys excrete methanol.')

# ---------------------------------------------------------------- Reactions of phenols
d.sec('7.4.4e-phenol-ring-reactions')
d.basic('Effect of –OH on the benzene ring?', T('Activates') + ' the ring and directs to ' + T('o/p') + ' (resonance)')
d.basic('Phenol + dilute HNO₃ (298 K)?', 'Mixture of ' + T('o- and p-nitrophenol'), **fig('fig_phenol_nitration'))
d.basic('Why is o-nitrophenol steam volatile but p- is not?', 'o-: ' + T('intramolecular H-bond') + '. p-: ' + T('intermolecular H-bond') + ' (associated molecules). Separated by steam distillation.', **fig('fig_nitrophenol_hbond'))
d.basic('Phenol + conc. HNO₃?', T('2,4,6-Trinitrophenol (picric acid)') + ', poor yield', **fig('fig_picric_acid'))
d.basic('Modern preparation of picric acid?', 'Phenol + conc. H₂SO₄ → ' + T('phenol-2,4-disulphonic acid') + '; then conc. HNO₃')
d.basic('Phenol + Br₂ in CS₂/CHCl₃ at 273 K?', T('Monobromophenols') + ': p-bromophenol major, o- minor', **fig('fig_phenol_br2_cs2'))
d.basic('Why does phenol brominate without FeBr₃?', 'Strongly activating –OH ' + T('polarises Br₂') + ' itself')
d.basic('Phenol + bromine water?', T('2,4,6-Tribromophenol') + ': white precipitate', **fig('fig_tribromophenol'))
d.basic('Intuition: why solvent decides mono- vs tribromination?', 'Water ionises phenol to the super-activated ' + T('phenoxide') + ' and polarises Br₂ further, so all o/p sites react.<br>Non-polar CS₂ keeps it gentle')
d.basic('Kolbe’s reaction?', 'Phenol + NaOH → phenoxide; + ' + T('CO₂') + ' then H⁺ → ' + T('2-hydroxybenzoic acid (salicylic acid)'), **fig('fig_kolbe'))
d.basic('Why does Kolbe’s reaction use phenoxide, not phenol?', 'Phenoxide is ' + T('more reactive') + ', enough to attack the weak electrophile CO₂')
d.basic('Reimer–Tiemann reaction?', 'Phenol + ' + T('CHCl₃ + aq. NaOH') + ' → substituted benzal chloride intermediate → hydrolysis → ' + T('salicylaldehyde') + ' (–CHO at ortho)', **fig('fig_reimer_tiemann'))
d.basic('Mnemonic: Kolbe vs Reimer–Tiemann?', T('K') + 'olbe adds ' + T('C') + 'O₂ → –COOH. ' + T('R') + 'eimer–Tiemann uses ' + T('CHCl₃') + ' → –CHO. Both go ortho.')
d.basic('Phenol + zinc dust (heat)?', T('Benzene') + ' + ZnO', **fig('fig_phenol_zinc'))
d.basic('Oxidation of phenol with chromic acid? In air?', T('Benzoquinone') + ' (conjugated diketone). Air: slowly → dark quinone mixtures.', **fig('fig_benzoquinone'))
d.basic('Products with HCl–ZnCl₂, HBr, SOCl₂ (Intext 7.6): butan-1-ol; 2-methylbutan-2-ol?', 'Butan-1-ol: 1-chlorobutane, 1-bromobutane, 1-chlorobutane<br>2-Methylbutan-2-ol: 2-chloro-2-methylbutane, 2-bromo-2-methylbutane, 2-chloro-2-methylbutane')
d.basic('Acid-catalysed dehydration (Intext 7.7): 1-methylcyclohexanol; butan-1-ol?', T('1-Methylcyclohexene') + '; ' + T('but-2-ene') + ' (major, Saytzeff after rearrangement)')

# ---------------------------------------------------------------- 7.5 Commercial alcohols
d.sec('7.5-commercial-alcohols')
d.basic('Methanol: old name, old and modern production?', T('Wood spirit') + ': destructive distillation of wood. Now: CO + 2H₂ over ' + T('ZnO–Cr₂O₃') + ', 200–300 atm, 573–673 K.', **fig('fig_methanol_synthesis'))
d.basic('Methanol: b.p., toxicity, uses?', N('337 K') + '; small amounts cause blindness, large amounts death; solvent for paints/varnishes, mainly to make ' + T('formaldehyde'))
d.basic('Fermentation: enzymes?', T('Invertase') + ': sucrose → glucose + fructose. ' + T('Zymase') + ' (yeast): glucose → ethanol + CO₂.', **fig('fig_fermentation'))
d.basic('Conditions and limit of fermentation?', T('Anaerobic') + '; zymase stops above ~' + N('14%') + ' alcohol; air oxidises ethanol to ethanoic acid (spoils taste)')
d.basic('Ethanol: b.p. and uses?', N('351 K') + '; solvent in paint industry, making carbon compounds; modern industrial route: hydration of ethene')
d.basic('What is denatured alcohol?', 'Commercial ethanol made undrinkable with ' + T('CuSO₄') + ' (colour) and ' + T('pyridine') + ' (foul smell)')
d.basic('Effects of drinking ethanol?', 'Acts on the CNS: impairs judgment, lowers inhibitions<br>High amounts cause nausea, unconsciousness, and can stop breathing')

# ---------------------------------------------------------------- 7.6 Ethers
d.sec('7.6.1-preparation-of-ethers')
d.basic('Ethanol + H₂SO₄ at 443 K vs 413 K?', '443 K: ' + T('ethene') + '. 413 K: ' + T('ethoxyethane') + '.', **fig('fig_ethanol_ether_alkene'))
d.basic('Mechanism of ether formation from alcohol?', T('SN2') + ': an alcohol molecule attacks a protonated alcohol, then loses H⁺', **fig('fig_ether_sn2_mechanism'))
d.basic('Limits of acid dehydration for ethers?', 'Only for ' + T('1°, unhindered') + ' alkyl groups at low T; 2° and 3° give ' + X('alkenes'))
d.basic('Why can’t bimolecular dehydration make ethyl methyl ether cleanly?', 'A mixture of ' + T('three ethers') + ' forms (dimethyl, diethyl, ethyl methyl)')
d.basic('Diethyl ether as an anaesthetic?', 'Widely used once; replaced due to ' + X('slow effect and unpleasant recovery'))
d.basic('Williamson synthesis?', 'R–X + R′–O⁻Na⁺ → R–O–R′ + NaX: ' + T('SN2 attack of alkoxide on a 1° alkyl halide'), **fig('fig_williamson_sn2'))
d.basic('Why must the alkyl halide be primary in Williamson?', 'Alkoxides are also ' + T('strong bases') + ': with 3° halides only ' + X('elimination') + ' occurs', **fig('fig_williamson_elimination'))
d.basic('CH₃ONa + (CH₃)₃CBr gives?', T('2-Methylpropene') + ' only, no ether')
d.basic('Right way to make t-butyl ethyl ether? (Example 7.6)', T('(CH₃)₃C–ONa + CH₃CH₂Cl') + ' (bulky part as alkoxide, 1° halide)')
d.basic('Williamson for phenyl ethers?', 'Use ' + T('phenoxide') + ' + alkyl halide', **fig('fig_williamson_phenoxide'))
d.basic('Correct reactants for 1-methoxy-4-nitrobenzene? (Intext 7.11)', T('Sodium 4-nitrophenoxide + CH₃Br') + '; 4-bromonitrobenzene + CH₃ONa fails (aryl halide won’t do SN2)')
d.basic('Williamson route to 2-ethoxy-3-methylpentane? (Intext 7.10)', 'Sodium salt of ' + T('3-methylpentan-2-ol') + ' + ' + T('ethyl bromide') + ' (1° halide)')
d.basic('Who was Williamson?', 'Alexander William Williamson (1824–1904), professor at University College, London (1849)')

d.sec('7.6.2-physical-properties-of-ethers')
d.basic('b.p. of n-pentane, ethoxyethane, butan-1-ol?', N('309.1 K') + ', ' + N('307.6 K') + ', ' + N('390 K') + ': ethers ≈ alkanes; alcohols much higher (H-bonding)')
d.basic('Why are ethers as water-soluble as alcohols of similar mass?', 'Ether O can ' + T('accept H-bonds') + ' from water (ethoxyethane 7.5 g, butan-1-ol 9 g per 100 mL; pentane immiscible)')

d.sec('7.6.3-reactions-of-ethers')
d.basic('Cleavage of dialkyl ethers?', 'Excess ' + T('HX') + ' under drastic conditions → two alkyl halides (via R–OH)', **fig('fig_ether_cleavage'))
d.basic('Reactivity of HX in ether cleavage?', T('HI > HBr > HCl') + ' (conc. HI or HBr at high T)')
d.basic('Anisole + HX gives?', T('Phenol + CH₃X') + ': alkyl–O bond breaks (aryl–O is stronger)', **fig('fig_anisole_hx'))
d.basic('Why doesn’t phenol go on to C₆H₅I?', 'sp² aryl carbon ' + X('cannot undergo nucleophilic substitution'))
d.basic('Mechanism of ether cleavage by HI (1°/2° groups)?', 'Protonation → oxonium ion; I⁻ attacks the ' + T('less substituted carbon') + ' (SN2): the ' + T('smaller') + ' alkyl becomes the iodide', **fig('fig_ether_hi_mechanism'))
d.basic('Ether with a tertiary group + HI?', 'The ' + T('tertiary') + ' group becomes the iodide (SN1, stable 3° carbocation): (CH₃)₃COCH₃ → CH₃OH + (CH₃)₃CI', **fig('fig_tert_ether_cleavage'))
d.basic('SN1 steps in cleavage of t-butyl methyl ether?', 'Slow: loss of CH₃OH → (CH₃)₃C⁺. Fast: I⁻ attacks.', **fig('fig_tert_sn1_steps'))
d.basic('Rule of thumb for ether + HI products?', '1°/2° groups: ' + T('smaller group → R–I') + ' (SN2). 3° group: ' + T('3° → R–I') + ' (SN1). Aryl: always gives ' + T('phenol') + '.')
d.basic('Products with HI (Example 7.7): benzyl phenyl ether?', T('Benzyl iodide + phenol'))
d.basic('Products (Intext 7.12): CH₃CH₂CH₂OCH₃ + HBr; C₆H₅OC₂H₅ + HBr; (CH₃)₃COC₂H₅ + HI?', 'CH₃CH₂CH₂OH + CH₃Br; phenol + C₂H₅Br; ' + T('(CH₃)₃CI + C₂H₅OH'))
d.basic('Effect of –OR on the benzene ring?', T('Activating, o/p-directing') + ' (like –OH)', **fig('fig_alkoxy_resonance'))
d.basic('Bromination of anisole?', 'Br₂ in ' + T('ethanoic acid') + ', no FeBr₃ needed: ' + T('p-bromoanisole (90%)') + ' major', **fig('fig_anisole_bromination'))
d.basic('Friedel–Crafts alkylation of anisole?', 'CH₃Cl / anhyd. AlCl₃ → 4-methoxytoluene (major) + 2-methoxytoluene', **fig('fig_anisole_fc_alkylation'))
d.basic('Friedel–Crafts acylation of anisole?', 'CH₃COCl / anhyd. AlCl₃ → ' + T('4-methoxyacetophenone') + ' (major) + 2- (minor)', **fig('fig_anisole_fc_acylation'))
d.basic('Nitration of anisole?', 'Conc. H₂SO₄ + HNO₃ → ' + T('2- and 4-nitroanisole') + ' (4- major)', **fig('fig_anisole_nitration'))

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Name reactions', 'What does it give?', [
    ('Kolbe (phenoxide + CO₂)', 'Salicylic acid', False), ('Reimer–Tiemann (phenol + CHCl₃/NaOH)', 'Salicylaldehyde', False),
    ('Williamson (RO⁻ + 1° R′X)', 'Ether R–O–R′', False), ('Cumene + O₂, then H⁺', 'Phenol + acetone', False),
    ('Hydroboration–oxidation', 'Anti-Markovnikov alcohol', False), ('Lucas test', '3° turbid at once; 1° none', False)], term='Name reactions and tests of Chapter 7')
table_card(d, 'Compare', 'Alcohol · phenol · ether?', [
    ('Reacts with Na', 'Yes · yes · no', False), ('Reacts with aq. NaOH', 'No · yes · no', False),
    ('Intermolecular H-bond', 'Yes · yes · no', False), ('C–O cleavage by HX', 'Yes · no · yes (drastic)', False)], term='Alcohols, phenols and ethers compared')

n = d.write(os.path.join(OUT, 'deck.json'))
print(n, 'cards')
