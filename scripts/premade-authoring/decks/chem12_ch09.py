import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch09-amines')
d = Deck('Chapter 9: Amines', 'Class 12', ['class-12', 'chemistry', 'ch-9'])
d.description = 'Structure, naming, preparation, basicity, carbylamine and Hinsberg tests, aniline substitution, diazonium salts and coupling'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- intro
d.sec('9.0-introduction')
d.basic('What are amines?', 'Derivatives of ' + T('ammonia') + ' in which one, two or three H are replaced by alkyl/aryl groups', **fig('fig_amine_examples'))
d.cloze('Amines in use: {{c1::adrenaline and ephedrine}} (2° amino) raise blood pressure; {{c2::novocain}} is a dental anaesthetic; {{c3::benadryl}} (3° amino) is an antihistamine; quaternary ammonium salts are {{c4::surfactants}}.')

# ---------------------------------------------------------------- 9.1 Structure
d.sec('9.1-structure')
d.basic('Hybridisation and shape of amines?', 'N is ' + T('sp³') + '; shape ' + T('pyramidal') + ', one orbital holds the lone pair')
d.basic('C–N–C angle in trimethylamine and why?', N('108°') + ' (< 109.5°): ' + T('lone pair') + ' repulsion', **fig('fig_9_1_trimethylamine'))

# ---------------------------------------------------------------- 9.2-9.3
d.sec('9.2-classification')
d.basic('1°, 2°, 3° amines?', 'One, two, three H of NH₃ replaced: RNH₂, R₂NH, R₃N', **fig('fig_1_2_3_amines'))
d.basic('Simple vs mixed amines?', T('Simple') + ': all groups the same. ' + T('Mixed') + ': different groups.')
d.basic('Trap: is (CH₃)₃C–NH₂ a tertiary amine?', X('No') + ': it is a ' + T('primary') + ' amine (one C on N); amine class counts groups on N, not the carbon type')
d.sec('9.3-nomenclature')
d.basic('IUPAC naming of amines?', 'Primary: ' + T('alkanamine') + ' (replace "e" by "amine": methanamine). 2°/3°: prefix ' + T('N-') + ' for groups on N.')
d.cloze('IUPAC names: CH₃NHCH₂CH₃ = {{c1::N-methylethanamine}}; (C₂H₅)₃N = {{c2::N,N-diethylethanamine}}; H₂N–CH₂CH₂–NH₂ = {{c3::ethane-1,2-diamine}}; allylamine = {{c4::prop-2-en-1-amine}}.')
d.cloze('Arylamines: C₆H₅NH₂ = {{c1::aniline / benzenamine}}; o-toluidine = {{c2::2-methylaniline}}; hexamethylenediamine = {{c3::hexane-1,6-diamine}}.')
d.basic('Table 9.1: names', 'Table 9.1', **fig('tab_9_1_names'))
d.basic('Isomers of C₄H₁₁N (Intext 9.2)?', N('8') + ': butan-1-amine, butan-2-amine, 2-methylpropan-1-amine, 2-methylpropan-2-amine (1°); N-methylpropan-1-amine, N-methylpropan-2-amine, N-ethylethanamine (2°); N,N-dimethylethanamine (3°)')
d.basic('Isomerism shown among C₄H₁₁N amines?', 'Chain, position and ' + T('metamerism') + ' (and functional between classes)')

# ---------------------------------------------------------------- 9.4 Preparation
d.sec('9.4-preparation')
d.basic('Reduction of nitro compounds?', 'H₂ with Ni/Pd/Pt, or metal + acid (' + T('Sn/HCl, Fe/HCl') + ')', **fig('fig_nitro_reduction'))
d.basic('Why is Fe + HCl preferred?', 'FeCl₂ formed ' + T('hydrolyses to release HCl') + ', so only a little acid is needed to start')
d.basic('Ammonolysis of alkyl halides?', 'R–X + ethanolic NH₃ in sealed tube at ' + N('373 K') + ': SN, C–X cleaved by NH₃', **fig('fig_ammonolysis_step'))
d.basic('Drawback of ammonolysis and fix?', 'Gives a ' + X('mixture') + ' of 1°, 2°, 3° amines and quaternary salt; use ' + T('large excess NH₃') + ' for 1°', **fig('fig_ammonolysis_series'))
d.basic('Getting the free amine from its salt?', 'Treat with strong base (NaOH)', **fig('fig_free_amine'))
d.basic('Reactivity of halides in ammonolysis?', T('RI > RBr > RCl'))
d.basic('Example 9.1: C₂H₅Cl + NH₃; benzyl chloride + NH₃ then 2 CH₃Cl?', 'Ethanamine → N-ethyl... → quaternary salt; benzylamine → N,N-dimethylphenylmethanamine', **fig('fig_ex91_solution'))
d.basic('Reduction of nitriles?', 'LiAlH₄ or H₂/Ni → 1° amine R–CH₂NH₂: ' + T('ascends') + ' the series by one C', **fig('fig_nitrile_reduction'))
d.basic('Reduction of amides?', T('LiAlH₄') + ' then H₂O → R–CH₂–NH₂ (same C count)', **fig('fig_amide_reduction'))
d.basic('Gabriel phthalimide synthesis?', 'Phthalimide + ' + T('ethanolic KOH') + ' → K-phthalimide; + R–X → N-alkylphthalimide; alkaline hydrolysis → ' + T('pure 1° amine'), **fig('fig_gabriel_1'))
d.basic('Gabriel: final hydrolysis step?', 'NaOH(aq) → sodium phthalate + R–NH₂', **fig('fig_gabriel_2'))
d.basic('Why can’t Gabriel make aniline?', 'Aryl halides ' + X('don’t undergo SN') + ' with phthalimide anion')
d.basic('Hoffmann bromamide degradation?', 'RCONH₂ + ' + T('Br₂ + 4NaOH') + ' → R–NH₂ + Na₂CO₃ + 2NaBr + 2H₂O: amine has ' + X('one C fewer'), **fig('fig_hoffmann'))
d.basic('What migrates in Hoffmann degradation?', 'The alkyl/aryl group moves from carbonyl C to ' + T('N'))
d.basic('Example 9.3: amide giving propanamine; amine from benzamide?', T('Butanamide') + '; ' + T('aniline'))
d.basic('Example 9.2: CH₃CH₂Cl → CH₃CH₂CH₂NH₂; C₆H₅CH₂Cl → C₆H₅CH₂CH₂NH₂?', 'Ethanolic NaCN (→ nitrile), then reduction', **fig('fig_ex92_solution'))
d.basic('Benzene → aniline; benzene → N,N-dimethylaniline (Intext 9.3)?', 'Nitration then Sn/HCl; then aniline + 2CH₃Cl')
d.basic('Cl–(CH₂)₄–Cl → hexane-1,6-diamine?', 'KCN (→ NC(CH₂)₄CN), then ' + T('LiAlH₄ / H₂-Ni'))
table_card(d, 'Carbon count', 'Change in carbons?', [
    ('Nitrile reduction (R–X → RCN → RCH₂NH₂)', '+1 C', False), ('Hoffmann bromamide', '−1 C', False),
    ('Amide reduction (LiAlH₄)', 'Same', False), ('Gabriel synthesis', 'Same (1° only)', False)], term='How amine preparations change the carbon count')

# ---------------------------------------------------------------- 9.5 Physical
d.sec('9.5-physical-properties')
d.basic('Physical state and smell of amines?', 'Lower aliphatic: ' + T('gases, fishy odour') + '; ≥3 C (1°): liquids; higher: solids')
d.basic('Why does aniline darken on storage?', T('Atmospheric oxidation'))
d.basic('Why are lower amines water-soluble?', 'H-bonding with water; falls as the hydrophobic alkyl part grows')
d.basic('More soluble in water: butan-1-ol or butan-1-amine?', T('Butan-1-ol') + ': O (3.5) more electronegative than N (3.0), stronger H-bonds')
d.basic('b.p. order of isomeric amines and why?', T('1° > 2° > 3°') + ': 1° has two N–H for H-bonding; 3° has none', **fig('fig_9_2_hbond'))
d.basic('b.p. of butan-1-amine vs butan-1-ol vs alkane?', 'n-C₄H₉NH₂ 350.8 K; (C₂H₅)₂NH 329.3; C₂H₅N(CH₃)₂ 310.5; alkane 300.8; ' + T('n-C₄H₉OH 390.3 K'), **fig('tab_9_2_bp'))

# ---------------------------------------------------------------- 9.6 Reactions
d.sec('9.6.1-basic-character')
d.basic('Amines + acids?', 'Form ' + T('ammonium salts') + ' (aniline + HCl → anilinium chloride); NaOH regenerates amine', **fig('fig_amine_salt'))
d.basic('Use of amine salts’ solubility?', 'Salts are water-soluble, ether-insoluble: ' + T('separate amines') + ' from non-basic compounds')
d.basic('Why are amines Lewis bases?', 'Lone pair on N')
d.basic('Kb and pKb of amines?', 'R–NH₂ + H₂O ⇌ R–NH₃⁺ + OH⁻; ' + T('larger Kb / smaller pKb = stronger base'), **fig('fig_kb_expression'))
d.basic('pKb of ammonia? Aliphatic amines? Aniline?', N('4.75') + '; ' + N('3–4.22') + ' (stronger); aniline ' + N('9.38') + ' (much weaker)', **fig('tab_9_3_pkb'))
d.basic('Why are alkylamines stronger bases than NH₃?', T('+I') + ' of alkyl pushes electron density to N and stabilises the cation', **fig('fig_protonation'))
d.basic('Basicity order in the gas phase?', T('3° > 2° > 1° > NH₃') + ' (inductive only)')
d.basic('Why is the aqueous order different?', 'Cation also stabilised by ' + T('H-bonding with water (solvation)') + ': 1° cation has most N–H (best solvated); plus ' + T('steric') + ' hindrance', **fig('fig_solvation_order'))
d.cloze('Aqueous basicity: methyl series {{c1::(CH₃)₂NH > CH₃NH₂ > (CH₃)₃N > NH₃}}; ethyl series {{c2::(C₂H₅)₂NH > (C₂H₅)₃N > C₂H₅NH₂ > NH₃}}.')
d.basic('Memory hook for the aqueous order?', 'Secondary always wins. Methyl: ' + T('2 > 1 > 3') + ' (small CH₃ lets water solvate 1° well, 3° worst). Ethyl: ' + T('2 > 3 > 1') + ' (bulky ethyls make +I matter more).')
d.basic('Why is aniline a weaker base than NH₃?', 'N lone pair is ' + T('delocalised into the ring') + ' (5 resonance structures); anilinium has only 2, so protonation loses stabilisation', **fig('fig_aniline_resonance'))
d.basic('Substituents on aniline and basicity?', 'EDG (–OCH₃, –CH₃) ' + T('increase') + '; EWG (–NO₂, –SO₃H, –COOH, –X) ' + X('decrease'))
d.basic('Decreasing basicity (Example 9.4): C₆H₅NH₂, C₂H₅NH₂, (C₂H₅)₂NH, NH₃?', '(C₂H₅)₂NH > C₂H₅NH₂ > NH₃ > C₆H₅NH₂')
d.basic('Increasing basicity (Intext 9.4 i): C₂H₅NH₂, C₆H₅NH₂, NH₃, C₆H₅CH₂NH₂, (C₂H₅)₂NH?', 'C₆H₅NH₂ < NH₃ < C₆H₅CH₂NH₂ < C₂H₅NH₂ < (C₂H₅)₂NH')
d.basic('Why is benzylamine (pKb 4.70) much stronger than aniline?', 'CH₂ separates N from the ring: ' + T('no resonance') + ' of the lone pair')

d.sec('9.6.2-alkylation-acylation')
d.basic('Alkylation of amines?', 'With R–X → higher amines and finally ' + T('quaternary ammonium salt'))
d.basic('Aniline + excess CH₃I (Na₂CO₃)? (Intext 9.6)', T('N,N,N-Trimethylanilinium iodide') + ' (quaternary)')
d.basic('Acylation of amines?', '1° and 2° amines + acid chloride/anhydride/ester → ' + T('amides') + '; base (pyridine) removes HCl', **fig('fig_acetylation'))
d.basic('Can 3° amines be acylated?', X('No') + ': no H on N')
d.basic('Benzoylation?', 'Amine + C₆H₅COCl: methanamine → ' + T('N-methylbenzamide') + '; aniline → benzanilide', **fig('fig_benzoylation'))
d.basic('Amines + carboxylic acids at room temperature?', 'Form ' + T('salts'))

d.sec('9.6.3-carbylamine-and-nitrous-acid')
d.basic('Carbylamine (isocyanide) test?', '1° amine + ' + T('CHCl₃ + ethanolic KOH') + ', heat → ' + T('foul-smelling isocyanide') + '; 2° and 3° don’t react', **fig('fig_carbylamine'))
d.basic('1° aliphatic amine + HNO₂?', 'Unstable diazonium salt → ' + T('N₂ (quantitative) + alcohol') + '; used to estimate amino acids and proteins', **fig('fig_nitrous_primary'))
d.basic('Aniline + HNO₂ at 273–278 K?', T('Benzenediazonium chloride') + ' (diazotisation)', **fig('fig_diazotisation_aniline'))
d.basic('Isomers of C₃H₉N giving N₂ with HNO₂ (Intext 9.8)?', 'Only the 1° amines: ' + T('propan-1-amine, propan-2-amine'))

d.sec('9.6.4-hinsberg')
d.basic('What is Hinsberg’s reagent?', T('Benzenesulphonyl chloride C₆H₅SO₂Cl') + ' (now often p-toluenesulphonyl chloride)')
d.basic('Hinsberg with 1° amine?', 'N-Ethylbenzenesulphonamide: N–H is ' + T('acidic') + ' (strong EWG SO₂) → ' + T('soluble in alkali'), **fig('fig_hinsberg_primary'))
d.basic('Hinsberg with 2° amine?', 'N,N-Diethylbenzenesulphonamide: no N–H → ' + X('insoluble in alkali'), **fig('fig_hinsberg_secondary'))
d.basic('Hinsberg with 3° amine?', X('No reaction'))
table_card(d, 'Tests', 'Result for 1° · 2° · 3°?', [
    ('Carbylamine (CHCl₃/KOH)', 'Foul smell · none · none', False), ('Hinsberg product in alkali', 'Soluble · insoluble · no reaction', False),
    ('HNO₂ (aliphatic)', 'N₂ + alcohol · different · different', False)], term='Distinguishing 1°, 2° and 3° amines')

d.sec('9.6.5-electrophilic-substitution')
d.basic('Effect of –NH₂ on the ring?', T('Powerful activating, o/p-directing'))
d.basic('Aniline + bromine water?', 'White ppt of ' + T('2,4,6-tribromoaniline') + ' (at room temperature)', **fig('fig_tribromoaniline'))
d.basic('How to get monobromoaniline?', T('Protect –NH₂ by acetylation') + ' (acetanilide), brominate (Br₂/CH₃COOH → p-bromo major), hydrolyse', **fig('fig_protection_bromination'))
d.basic('Why is –NHCOCH₃ less activating than –NH₂?', 'N lone pair is also ' + T('delocalised onto the C=O oxygen'), **fig('fig_acetanilide_resonance'))
d.basic('Direct nitration of aniline: products?', 'Tarry oxidation products + p (51%), ' + T('m (47%)') + ', o (2%)', **fig('fig_aniline_nitration'))
d.basic('Why so much meta-nitroaniline?', 'In strong acid aniline becomes ' + T('anilinium ion') + ', which is ' + T('meta-directing'))
d.basic('How to get p-nitroaniline cleanly?', 'Acetylate → nitrate (p-nitroacetanilide) → hydrolyse', **fig('fig_protected_nitration'))
d.basic('Sulphonation of aniline?', 'Conc. H₂SO₄ → anilinium hydrogensulphate; 453–473 K → ' + T('sulphanilic acid') + ' (exists as zwitter ion)', **fig('fig_sulphanilic'))
d.basic('Why no Friedel–Crafts on aniline?', 'Aniline ' + X('forms a salt with AlCl₃') + '; N⁺ strongly deactivates the ring')

# ---------------------------------------------------------------- Diazonium salts
d.sec('9.7-diazonium-salts')
d.basic('General formula and naming of diazonium salts?', r'\( ArN_2^+X^- \)' + '; e.g. ' + T('benzenediazonium chloride') + ', benzenediazonium hydrogensulphate')
d.basic('Why are arenediazonium salts more stable than alkyl ones?', 'Resonance with the ring', **fig('fig_diazonium_resonance'))
d.basic('Diazotisation: conditions?', 'Aniline + NaNO₂ + 2HCl at ' + N('273–278 K') + '; used immediately', **fig('fig_diazotisation'))
d.basic('Physical properties of benzenediazonium chloride?', 'Colourless crystalline, water-soluble, stable cold, reacts with warm water; decomposes dry. ' + T('Fluoroborate') + ' is insoluble and stable at room temperature.')

d.sec('9.9-reactions-of-diazonium-salts')
d.basic('Sandmeyer reaction?', 'ArN₂⁺ + ' + T('Cu₂Cl₂/HCl, Cu₂Br₂/HBr, CuCN/KCN') + ' → ArCl, ArBr, ArCN + N₂', **fig('fig_sandmeyer'))
d.basic('Gattermann reaction?', 'ArN₂⁺ + HX with ' + T('Cu powder') + ' → ArX; yield lower than Sandmeyer', **fig('fig_gattermann'))
d.basic('Diazonium → iodobenzene?', 'Just ' + T('KI'), **fig('fig_iodide'))
d.basic('Diazonium → fluorobenzene (Balz–Schiemann)?', T('HBF₄') + ' → ArN₂⁺BF₄⁻ ppt; heat → Ar–F', **fig('fig_fluoride'))
d.basic('Diazonium → benzene?', 'Mild reductants: ' + T('H₃PO₂') + ' or ' + T('ethanol') + ' (oxidised to H₃PO₃ / ethanal)', **fig('fig_replace_h'))
d.basic('Diazonium → phenol?', 'Let temperature rise to ' + N('283 K') + ' (warm with water)', **fig('fig_replace_oh'))
d.basic('Diazonium → nitrobenzene?', 'Fluoroborate + aq. ' + T('NaNO₂ / Cu') + ', heat', **fig('fig_replace_no2'))
d.basic('Coupling with phenol?', 'Para coupling (alkaline) → ' + T('p-hydroxyazobenzene (orange dye)'), **fig('fig_coupling_phenol'))
d.basic('Coupling with aniline?', '(acidic) → ' + T('p-aminoazobenzene (yellow dye)'), **fig('fig_coupling_aniline'))
d.basic('What type of reaction is coupling? Why coloured?', T('Electrophilic substitution') + '; extended conjugation through –N=N– (azo dyes)')
d.basic('Why are diazonium salts so useful in synthesis?', 'Introduce –F, –Cl, –Br, –I, –CN, –OH, –NO₂ where direct substitution fails (Ar–F, Ar–I, Ar–CN)')
d.basic('4-Nitrotoluene → 2-bromobenzoic acid (Example 9.5)?', 'Br₂/Fe → Sn/HCl → diazotise → H₃PO₂ (remove N) → KMnO₄', **fig('fig_ex95_solution'))
d.basic('Aniline → 1,3,5-tribromobenzene (Intext 9.9)?', 'Br₂/H₂O → 2,4,6-tribromoaniline; diazotise; ' + T('H₃PO₂') + ' removes the N group')
d.basic('3-Methylaniline → 3-nitrotoluene?', 'Diazotise, then ' + T('HBF₄, then NaNO₂/Cu') + ' (replace by NO₂)')
table_card(d, 'Diazonium', 'Reagent → product?', [
    ('CuCl/HCl', 'ArCl (Sandmeyer)', False), ('CuCN/KCN', 'ArCN', False), ('KI', 'ArI', False), ('HBF₄, heat', 'ArF', False),
    ('H₃PO₂ or C₂H₅OH', 'ArH', False), ('H₂O, 283 K', 'ArOH', False), ('Phenol (OH⁻)', 'p-Hydroxyazobenzene', False)], term='Reactions of benzenediazonium chloride')

n = d.write(os.path.join(OUT, 'deck.json'))
print(n, 'cards')
