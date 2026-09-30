import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Chemistry', 'class12-chemistry-ch08-aldehydes-ketones-and-carboxylic-acids')
d = Deck('Chapter 8: Aldehydes, Ketones and Carboxylic Acids', 'Class 12', ['class-12', 'chemistry', 'ch-8'])
d.description = 'Naming, carbonyl structure, preparation, nucleophilic addition, Tollens and Fehling, haloform, aldol, Cannizzaro, acidity, HVZ and uses'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- intro
d.sec('8.0-introduction')
d.basic('Aldehyde vs ketone vs carboxylic acid?', 'C=O bonded to C and ' + T('H') + ' (aldehyde); to ' + T('two C') + ' (ketone); to C/H and ' + T('–OH') + ' (acid). With –NH₂: amide; with halogen: acyl halide.', **fig('fig_general_formulas'))
d.basic('Which are derivatives of carboxylic acids?', T('Esters') + ' and ' + T('anhydrides') + ' (also amides, acyl halides)', **fig('fig_ester_anhydride'))
d.basic('Natural fragrant aldehydes and their sources?', E('Vanillin') + ' (vanilla beans), ' + E('salicylaldehyde') + ' (meadow sweet), ' + E('cinnamaldehyde') + ' (cinnamon)', **fig('fig_fragrant_aldehydes'))

# ---------------------------------------------------------------- 8.1 Nomenclature
d.sec('8.1.1-nomenclature')
d.basic('How are common names of aldehydes formed?', 'From the common acid name, ' + T('–ic acid → aldehyde') + '<br>Substituent positions by Greek letters α, β, γ (α = carbon next to CHO)', **fig('fig_common_aldehydes'))
d.basic('Common names of ketones?', 'Name the two groups + ketone; ' + T('acetone') + ' for dimethyl ketone; alkyl phenyl ketones as acyl + "phenone" (acetophenone, benzophenone)', **fig('fig_common_ketones'))
d.basic('IUPAC suffixes for aldehydes and ketones?', 'Replace –e with ' + T('–al') + ' / ' + T('–one') + '; aldehyde carbon is C-1; ketone numbered from the end nearer C=O')
d.basic('Naming an aldehyde on a ring?', 'Suffix ' + T('carbaldehyde') + ' after the cycloalkane (ring C bearing CHO = C-1)<br>benzenecarbaldehyde = ' + T('benzaldehyde') + ' (accepted)')
d.basic('IUPAC name examples?', 'Ethanal<br>4-Bromo-3-methylheptanal<br>3-Methylcyclopentanone<br>Cyclohexanecarbaldehyde<br>Pent-2-enal<br>1-Phenylpropan-1-one', **fig('fig_iupac_examples'))
d.basic('More IUPAC examples?', '3-Oxopentanal, 2,4-dimethylpentan-3-one, 4-nitrobenzaldehyde, propane-1,2,3-tricarbaldehyde', **fig('fig_iupac_examples2'))
d.cloze('Names: acrolein = {{c1::prop-2-enal}}; mesityl oxide = {{c2::4-methylpent-3-en-2-one}}; diisopropyl ketone = {{c3::2,4-dimethylpentan-3-one}}; phthaldehyde = {{c4::benzene-1,2-dicarbaldehyde}}.')
d.basic('Table 8.1 names', 'Table 8.1', **fig('tab_8_1_names'))

d.sec('8.1.2-structure-of-carbonyl')
d.basic('Hybridisation and geometry of carbonyl carbon?', T('sp²') + ', trigonal planar, bond angles ~' + N('120°') + '; π bond from p–p overlap with O', **fig('fig_8_1_carbonyl_orbitals'))
d.basic('Why is the carbonyl group polar?', 'O is more electronegative: resonance between neutral (A) and dipolar (B) C⁺–O⁻', **fig('fig_carbonyl_resonance'))
d.basic('Carbonyl carbon and oxygen as acid/base centres?', 'Carbon: ' + T('electrophilic (Lewis acid)') + '. Oxygen: ' + T('nucleophilic (Lewis base)') + '.')
d.basic('Carbonyl compounds vs ethers: polarity?', 'Carbonyl compounds have larger dipole moments: ' + T('more polar') + ' than ethers')

# ---------------------------------------------------------------- 8.2 Preparation
d.sec('8.2.1-preparation-of-aldehydes-and-ketones')
d.basic('Aldehydes and ketones from alcohols?', 'Oxidation of ' + T('1° → aldehyde, 2° → ketone') + '; or dehydrogenation over ' + T('Ag / Cu') + ' (volatile alcohols, industrial)')
d.basic('From alkenes?', T('Ozonolysis') + ' then Zn dust + H₂O → aldehydes/ketones by substitution pattern')
d.basic('Hydration of alkynes (H₂SO₄ + HgSO₄)?', 'Ethyne → ' + T('acetaldehyde') + '; all other alkynes → ' + T('ketones'))

d.sec('8.2.2-preparation-of-aldehydes')
d.basic('Rosenmund reduction?', 'Acyl chloride + H₂ over ' + T('Pd–BaSO₄') + ' → aldehyde (benzoyl chloride → benzaldehyde)', **fig('fig_rosenmund'))
d.basic('Why is Pd poisoned with BaSO₄ in Rosenmund? (insight)', 'To stop reduction at the ' + T('aldehyde') + ' (unpoisoned Pd would go on to the alcohol)')
d.basic('Stephen reaction?', 'Nitrile + ' + T('SnCl₂ + HCl') + ' → imine (RCH=NH); hydrolysis → aldehyde', **fig('fig_stephen'))
d.basic('DIBAL-H on nitriles?', 'Selective reduction to imine, then H₂O → aldehyde; C=C untouched', **fig('fig_dibal_nitrile'))
d.basic('DIBAL-H on esters?', T('Esters → aldehydes'), **fig('fig_dibal_ester'))
d.basic('Etard reaction?', 'Toluene + ' + T('CrO₂Cl₂ (chromyl chloride)') + ' in CS₂ → chromium complex; H₃O⁺ → benzaldehyde', **fig('fig_etard'))
d.basic('Toluene + CrO₃ in acetic anhydride?', '→ ' + T('benzylidene diacetate') + '; aqueous acid → benzaldehyde', **fig('fig_cro3_acetic_anhydride'))
d.basic('Why do these reagents stop at the aldehyde?', 'They convert CH₃ into an intermediate (complex / diacetate) that is ' + T('hard to oxidise further'))
d.basic('Commercial benzaldehyde from toluene?', 'Side-chain chlorination (Cl₂/hν) → ' + T('benzal chloride') + '; hydrolysis at 373 K', **fig('fig_side_chain_chlorination'))
d.basic('Gattermann–Koch reaction?', 'Benzene + ' + T('CO + HCl') + ' with anhyd. AlCl₃ / CuCl → benzaldehyde', **fig('fig_gattermann_koch'))

d.sec('8.2.3-preparation-of-ketones')
d.basic('Ketones from acyl chlorides?', 'With ' + T('dialkylcadmium R₂Cd') + ' (from Grignard + CdCl₂)', **fig('fig_dialkylcadmium'))
d.basic('Ketones from nitriles?', T('Grignard reagent') + ' then hydrolysis: CH₃CH₂CN + C₆H₅MgBr → propiophenone', **fig('fig_nitrile_grignard'))
d.basic('Friedel–Crafts acylation?', 'Benzene + RCOCl / ArCOCl with ' + T('anhyd. AlCl₃') + ' → aryl ketone', **fig('fig_friedel_crafts_acylation'))
d.cloze('Reagents (Example 8.1): hexan-1-ol → hexanal = {{c1::PCC}}; p-fluorotoluene → p-fluorobenzaldehyde = {{c2::CrO₃ in acetic anhydride (or CrO₂Cl₂)}}; ethanenitrile → ethanal = {{c3::DIBAL-H}}; but-2-ene → ethanal = {{c4::O₃ / H₂O–Zn}}.')
table_card(d, 'Name reactions', 'Reagent?', [
    ('Rosenmund', 'H₂ / Pd–BaSO₄ on RCOCl', False), ('Stephen', 'SnCl₂ + HCl on RCN, then H₃O⁺', False), ('Etard', 'CrO₂Cl₂ on toluene', False),
    ('Gattermann–Koch', 'CO + HCl, AlCl₃/CuCl on benzene', False), ('Friedel–Crafts acylation', 'RCOCl + anhyd. AlCl₃', False)], term='Aldehyde and ketone name reactions: reagents')

# ---------------------------------------------------------------- 8.3 Physical properties
d.sec('8.3-physical-properties')
d.basic('Physical state of methanal and ethanal?', 'Methanal: ' + T('gas') + '. Ethanal: volatile liquid. Others: liquid or solid.')
d.basic('Why do aldehydes/ketones boil higher than hydrocarbons and ethers but lower than alcohols?', T('Dipole–dipole') + ' association; but ' + X('no intermolecular H-bonding'))
d.basic('b.p. order (mass ~58–60)?', 'n-butane 273 < methoxyethane 281 < propanal 322 < acetone 329 < propan-1-ol 370 K', **fig('fig_bp_table'))
d.basic('Why are lower aldehydes/ketones miscible with water?', 'Carbonyl O ' + T('accepts H-bonds') + ' from water; solubility falls with chain length', **fig('fig_carbonyl_water_hbond'))
d.basic('Odour trend?', 'Lower aldehydes: ' + T('sharp, pungent') + '; larger ones more ' + T('fragrant') + ' (perfumes, flavours)')
d.basic('Increasing b.p. (Example 8.2): butanal, butan-1-ol, ethoxyethane, n-pentane?', 'n-Pentane < ethoxyethane < butanal < butan-1-ol')
d.basic('Increasing b.p. (Intext 8.3): CH₃CHO, CH₃CH₂OH, CH₃OCH₃, CH₃CH₂CH₃?', 'CH₃CH₂CH₃ < CH₃OCH₃ < CH₃CHO < CH₃CH₂OH')

# ---------------------------------------------------------------- 8.4 Reactions
d.sec('8.4.1-nucleophilic-addition')
d.basic('Alkenes vs carbonyls: type of addition?', 'Alkenes: ' + T('electrophilic') + ' addition. Carbonyls: ' + T('nucleophilic') + ' addition.')
d.basic('Mechanism of nucleophilic addition?', 'Nu attacks C ~' + T('perpendicular') + ' to the sp² plane → ' + T('tetrahedral alkoxide') + ' (sp² → sp³); it takes up H⁺', **fig('fig_8_2_nucleophilic_addition'))
d.basic('Why are aldehydes more reactive than ketones? (2 reasons)', T('Steric') + ': one bulky group vs two. ' + T('Electronic') + ': two alkyl groups (+I) reduce electrophilicity more.')
d.basic('Is benzaldehyde more or less reactive than propanal? (Example 8.3)', X('Less') + ': resonance with the ring reduces the polarity of C=O', **fig('fig_benzaldehyde_resonance'))
d.basic('Increasing reactivity (Intext 8.4): ethanal, propanal, propanone, butanone?', 'Butanone < propanone < propanal < ethanal')
d.basic('Increasing reactivity: benzaldehyde, p-tolualdehyde, p-nitrobenzaldehyde, acetophenone?', 'Acetophenone < p-tolualdehyde < benzaldehyde < p-nitrobenzaldehyde')
d.basic('HCN addition: why base-catalysed? Product?', 'Pure HCN is slow; base makes ' + T('CN⁻') + ', a stronger nucleophile → ' + T('cyanohydrin') + ' (useful synthetic intermediate)', **fig('fig_hcn_addition'))
d.basic('NaHSO₃ addition: product and use?', 'Crystalline ' + T('bisulphite addition compound') + ', water-soluble.<br>Regenerated by dilute acid/alkali.<br>Used to ' + T('separate and purify aldehydes'), **fig('fig_bisulphite'))
d.basic('Why does the bisulphite equilibrium favour aldehydes, not ketones?', T('Steric') + ' reasons: lies right for most aldehydes, left for most ketones')
d.basic('Aldehyde + alcohol (dry HCl)?', '1 ROH → ' + T('hemiacetal') + '; 2nd ROH → ' + T('acetal') + ' (gem-dialkoxy)', **fig('fig_acetal'))
d.basic('Ketone + ethylene glycol (dry HCl)?', 'Cyclic ' + T('ethylene glycol ketal') + '; acetals/ketals hydrolyse back with aqueous acid', **fig('fig_ketal'))
d.basic('Role of dry HCl in acetal formation?', 'Protonates carbonyl O, making C ' + T('more electrophilic'))
d.basic('Carbonyl + H₂N–Z: product and why it forms?', T('>C=N–Z') + ' via a carbinolamine; acid-catalysed; rapid ' + T('dehydration') + ' drives it', **fig('fig_ammonia_derivatives'))
d.cloze('Derivatives: NH₂OH → {{c1::oxime}}; NH₂NH₂ → {{c2::hydrazone}}; C₆H₅NHNH₂ → {{c3::phenylhydrazone}}; NH₂NHCONH₂ → {{c4::semicarbazone}}; RNH₂ → {{c5::Schiff’s base (substituted imine)}}.')
d.basic('Table 8.2: N-derivatives', 'Table 8.2', **fig('tab_8_2_derivatives'))
d.basic('Use of 2,4-DNP derivatives?', 'Yellow, orange or red solids for ' + T('characterising') + ' aldehydes and ketones')

d.sec('8.4.2-reduction')
d.basic('Reduction to alcohols?', 'NaBH₄ / LiAlH₄ / H₂-catalyst: aldehyde → ' + T('1°') + ', ketone → ' + T('2°') + ' alcohol')
d.basic('Clemmensen reduction?', '>C=O → >CH₂ with ' + T('Zn–Hg + conc. HCl'), **fig('fig_clemmensen'))
d.basic('Wolff–Kishner reduction?', '>C=O + NH₂NH₂ → hydrazone; ' + T('KOH / ethylene glycol, heat') + ' → >CH₂ + N₂', **fig('fig_wolff_kishner'))
d.basic('Clemmensen vs Wolff–Kishner: when to choose which? (insight)', 'Clemmensen is ' + T('acidic') + ' (avoid for acid-sensitive groups)<br>Wolff–Kishner is ' + T('basic') + ' (avoid for base-sensitive groups)')

d.sec('8.4.3-oxidation')
d.basic('Oxidation of aldehydes vs ketones?', 'Aldehydes: ' + T('easily') + ' → acids (even mild agents). Ketones: only ' + T('vigorous') + ' conditions, with C–C cleavage → mixture of smaller acids.', **fig('fig_ketone_oxidation'))
d.basic('Tollens’ test?', 'Warm aldehyde + ' + T('ammoniacal AgNO₃') + ' → ' + T('silver mirror') + '; aldehyde → carboxylate (alkaline)', **fig('fig_tollens'))
d.basic('Fehling’s test?', 'Fehling A (' + T('CuSO₄') + ') + B (alkaline ' + T('Rochelle salt') + '); aldehyde → ' + T('red-brown Cu₂O') + ' ppt', **fig('fig_fehling'))
d.basic('Which aldehydes fail Fehling’s test?', X('Aromatic') + ' aldehydes (e.g. benzaldehyde); they still give Tollens’')
d.basic('Haloform reaction?', 'Methyl ketones (CH₃CO–) + NaOX → sodium salt of acid with ' + T('one C fewer') + ' + CHX₃; C=C not affected', **fig('fig_haloform'))
d.basic('What does the iodoform test detect?', T('CH₃CO–') + ' or ' + T('CH₃CH(OH)–') + ' groups (yellow CHI₃)')
d.basic('Which alcohol and aldehyde give a positive iodoform test? (insight)', T('Ethanol') + ' and ' + T('ethanal') + ' (the only aldehyde); methanol does not')
d.basic('Example 8.4: C₈H₈O, 2,4-DNP +, iodoform +, Tollens −, gives C₇H₆O₂ on oxidation. A and B?', 'A = ' + T('acetophenone') + '; B = ' + T('benzoic acid'), **fig('fig_ex84_dnp'))
d.basic('Example 8.4 reactions: A with chromic acid and with NaOI?', 'Benzoic acid; sodium benzoate + CHI₃', **fig('fig_ex84_iodoform'))

d.sec('8.4.4-alpha-hydrogen-reactions')
d.basic('Why are α-hydrogens acidic?', 'Strong –I of C=O and ' + T('resonance-stabilised enolate') + ' conjugate base', **fig('fig_alpha_h_acidity'))
d.basic('Aldol reaction?', 'Aldehydes/ketones with ≥1 α-H + ' + T('dilute alkali') + ' → β-hydroxy aldehyde (' + T('aldol') + ') or ketone (' + T('ketol') + ')')
d.basic('Aldol condensation of ethanal?', '2CH₃CHO → 3-hydroxybutanal (aldol) → −H₂O → ' + T('but-2-enal'), **fig('fig_aldol_ethanal'))
d.basic('Aldol condensation of propanone?', 'Ba(OH)₂: → 4-hydroxy-4-methylpentan-2-one (ketol) → ' + T('4-methylpent-3-en-2-one'), **fig('fig_aldol_propanone'))
d.basic('Origin of the name "aldol"?', T('Ald') + 'ehyde + alcoh' + T('ol'))
d.basic('Cross aldol between ethanal and propanal?', 'Both have α-H → ' + T('four products') + ': but-2-enal, 2-methylpent-2-enal (self); 2-methylbut-2-enal, pent-2-enal (cross)', **fig('fig_cross_aldol'))
d.basic('Cross aldol with a ketone (Claisen–Schmidt type)?', 'Benzaldehyde + acetophenone, OH⁻ 293 K → ' + T('benzalacetophenone (1,3-diphenylprop-2-en-1-one)') + ' major', **fig('fig_claisen_schmidt'))
d.basic('Intuition: why does aldol need an α-H?', 'Base must pull off an α-H to make the ' + T('enolate') + ' nucleophile, which then attacks another carbonyl')

d.sec('8.4.5-other-reactions')
d.basic('Cannizzaro reaction?', 'Aldehydes with ' + X('no α-H') + ' + ' + T('conc. alkali') + ', heat: one molecule → alcohol, one → carboxylate (disproportionation)')
d.basic('Cannizzaro of HCHO?', '2HCHO + conc. KOH → ' + T('CH₃OH + HCOOK'), **fig('fig_cannizzaro_hcho'))
d.basic('Cannizzaro of benzaldehyde?', '2C₆H₅CHO + conc. NaOH → ' + T('benzyl alcohol + sodium benzoate'), **fig('fig_cannizzaro_benzaldehyde'))
d.basic('Aldol or Cannizzaro? The quick test.', 'Has α-H + ' + T('dilute') + ' alkali → aldol. No α-H + ' + T('concentrated') + ' alkali → Cannizzaro.')
d.basic('Nitration of benzaldehyde?', 'HNO₃/H₂SO₄ at 273–283 K → ' + T('m-nitrobenzaldehyde') + ' (C=O deactivating, meta-directing)', **fig('fig_benzaldehyde_nitration'))

d.sec('8.5-uses')
d.basic('Formalin: what and uses?', T('40% HCHO') + ': preserves biological specimens; bakelite, urea–formaldehyde glues')
d.basic('Uses of acetaldehyde, benzaldehyde, acetone?', 'Acetaldehyde: acetic acid, ethyl acetate, vinyl acetate, polymers, drugs. Benzaldehyde: perfumery, dyes. Acetone, ethyl methyl ketone: ' + T('solvents') + '.')

# ---------------------------------------------------------------- 8.6 Carboxylic acids
d.sec('8.6.1-carboxylic-acid-nomenclature')
d.basic('What are fatty acids?', 'Aliphatic acids ' + N('C₁₂–C₁₈') + ', occurring as glycerol esters in fats')
d.cloze('Origins: formic acid from {{c1::red ants (formica)}}; acetic acid from {{c2::vinegar (acetum)}}; butyric acid from {{c3::rancid butter (butyrum)}}.')
d.basic('IUPAC naming of carboxylic acids?', 'Replace –e with ' + T('–oic acid') + '; COOH carbon is C-1; multiple COOH: dicarboxylic/tricarboxylic acid')
d.cloze('Common → IUPAC: oxalic = {{c1::ethanedioic}}; malonic = {{c2::propanedioic}}; succinic = {{c3::butanedioic}}; glutaric = {{c4::pentanedioic}}; adipic = {{c5::hexanedioic}}.')
d.basic('Table 8.3: acid names', 'Table 8.3', **fig('tab_8_3_acid_names'))
d.basic('Aromatic acids: IUPAC names?', 'Benzoic = benzenecarboxylic acid; phenylacetic = 2-phenylethanoic acid; phthalic = benzene-1,2-dicarboxylic acid', **fig('tab_8_3_aromatic_acids'))

d.sec('8.6.2-structure-of-carboxyl')
d.basic('Why is the carboxyl carbon less electrophilic than a carbonyl carbon?', 'Resonance with the –OH lone pair', **fig('fig_carboxyl_resonance'))
d.basic('Consequence: do acids give typical carbonyl reactions (e.g. with NH₂OH)? (insight)', X('No') + ': the resonance-reduced C=O doesn’t give aldehyde/ketone addition reactions')

# ---------------------------------------------------------------- 8.7 Preparation of acids
d.sec('8.7-preparation-of-carboxylic-acids')
d.basic('Acids from 1° alcohols?', T('KMnO₄') + ' (neutral/acid/alkaline), K₂Cr₂O₇, or ' + T('CrO₃–H₂SO₄ (Jones reagent)'), **fig('fig_jones'))
d.basic('Acids from alkylbenzenes?', 'Vigorous oxidation (chromic acid / KMnO₄): ' + T('entire side chain → –COOH') + ' whatever its length', **fig('fig_alkylbenzene_oxidation'))
d.basic('Which alkyl side chain is not oxidised?', X('Tertiary') + ' (no benzylic H)')
d.basic('Acids from nitriles and amides?', 'Hydrolysis (H⁺ or OH⁻): RCN → amide → RCOOH; mild conditions stop at the amide', **fig('fig_nitrile_amide_hydrolysis'))
d.basic('Acids from Grignard reagents?', 'RMgX + ' + T('CO₂ (dry ice)') + ' → salt; H₃O⁺ → RCOOH', **fig('fig_grignard_co2'))
d.basic('Which methods ascend the series (one C more than R–X)?', T('Nitrile hydrolysis') + ' and ' + T('Grignard + CO₂'))
d.basic('Acids from acyl halides and anhydrides?', T('Hydrolysis') + ' (water; faster with base then acid)', **fig('fig_acyl_halide_anhydride_hydrolysis'))
d.basic('Acids from esters?', 'Acid hydrolysis gives acid directly; basic hydrolysis gives carboxylate, then acidify', **fig('fig_ester_hydrolysis'))
d.basic('Example 8.5 transformations (six)', 'Jones; HBr/KCN/H₃O⁺; Mg/CO₂; KMnO₄–KOH; KMnO₄–H₂SO₄; Tollens', **fig('fig_ex85_solution'))
d.basic('Convert to benzoic acid (Intext 8.7): ethylbenzene, acetophenone, bromobenzene, styrene?', 'KMnO₄–KOH then H₃O⁺; KMnO₄ (or NaOI); Mg/ether then CO₂, H₃O⁺; KMnO₄ then H₃O⁺')

# ---------------------------------------------------------------- 8.8 Physical properties
d.sec('8.8-physical-properties-of-acids')
d.basic('State and odour of aliphatic acids?', 'Up to C₉: colourless liquids, ' + T('unpleasant') + ' odour; higher: wax-like, odourless')
d.basic('Why do acids boil higher than alcohols of similar mass?', 'More extensive H-bonding; exist as ' + T('dimers') + ' even in vapour and aprotic solvents', **fig('fig_acid_dimer_hbond'))
d.basic('Solubility of acids in water?', 'Up to ' + N('4 C') + ' miscible; decreases with chain length; benzoic acid nearly insoluble in cold water')

# ---------------------------------------------------------------- 8.9 Reactions of acids
d.sec('8.9.1-acidity')
d.basic('Reactions of acids with metals and bases?', 'Na → salt + H₂; NaOH → salt; also ' + T('NaHCO₃ → CO₂ effervescence') + ' (test for –COOH; phenols don’t)', **fig('fig_acid_metals_bases'))
d.basic('Why are carboxylic acids acidic?', 'Ionise to ' + T('resonance-stabilised carboxylate') + ' + H₃O⁺', **fig('fig_carboxylate_resonance'))
d.basic('pKa of HCl, CF₃COOH, benzoic acid, acetic acid?', N('−7.0, 0.23, 4.19, 4.76') + '; smaller pKa = stronger acid')
d.cloze('pKa scale: strong acids {{c1::< 1}}; moderately strong {{c2::1–5}}; weak {{c3::5–15}}; extremely weak {{c4::> 15}}.')
d.basic('Why are carboxylic acids stronger than phenols?', 'Carboxylate: charge on ' + T('two equivalent O') + ' (equivalent resonance). Phenoxide: non-equivalent structures with charge on ' + X('less electronegative C') + '.')
d.basic('Effect of EWG and EDG on acidity?', T('EWG') + ' stabilises carboxylate, ' + T('increases') + ' acidity; ' + T('EDG') + ' destabilises, ' + X('decreases') + ' it', **fig('fig_ewg_edg'))
d.basic('Order of groups increasing acidity?', 'Ph < I < Br < Cl < F < CN < NO₂ < ' + T('CF₃'))
d.basic('Acidity order of halo and substituted acetic acids (NCERT)?', 'CF₃COOH > CCl₃COOH > CHCl₂COOH > NO₂CH₂COOH > NCCH₂COOH > FCH₂COOH > ClCH₂COOH > BrCH₂COOH > HCOOH > ClCH₂CH₂COOH > C₆H₅COOH > C₆H₅CH₂COOH > CH₃COOH > CH₃CH₂COOH')
d.basic('Why does phenyl or vinyl directly on COOH increase acidity?', 'The attached carbon is ' + T('sp²') + ' (more electronegative), outweighing the resonance donation', **fig('fig_vinyl_phenyl_acid'))
d.basic('pKa of 4-methoxy-, benzoic, 4-nitrobenzoic acid?', N('4.46, 4.19, 3.41'), **fig('fig_substituted_benzoic_pka'))
d.basic('Stronger acid (Intext 8.8): CH₃COOH or CH₂FCOOH; CH₂FCOOH or CH₂ClCOOH?', T('CH₂FCOOH') + '; ' + T('CH₂FCOOH') + ' (F more electronegative)')
d.basic('Stronger: CH₂FCH₂CH₂COOH or CH₃CHFCH₂COOH? F₃C–C₆H₄–COOH or CH₃–C₆H₄–COOH?', T('CH₃CHFCH₂COOH') + ' (F closer); ' + T('4-CF₃-benzoic acid'))
d.basic('Intuition: why does distance weaken the –I effect?', 'Inductive pull passes through σ bonds and ' + T('fades quickly') + ', roughly halving per bond')

d.sec('8.9.2-c-oh-cleavage')
d.basic('Anhydride formation?', 'Heat with ' + T('H₂SO₄ or P₂O₅') + ': 2CH₃COOH → ethanoic anhydride', **fig('fig_anhydride_formation'))
d.basic('Esterification: catalyst?', 'Alcohol/phenol + acid with ' + T('conc. H₂SO₄ or dry HCl'))
d.basic('Mechanism of esterification?', T('Nucleophilic acyl substitution') + ':<br>1) Protonation of C=O<br>2) Alcohol adds (tetrahedral intermediate)<br>3) Proton transfer makes –OH₂⁺<br>4) Water leaves<br>5) Loss of H⁺', **fig('fig_esterification_mechanism'))
d.basic('Acids + PCl₅, PCl₃, SOCl₂?', '→ ' + T('acyl chlorides') + '; SOCl₂ preferred (SO₂, HCl gases escape)', **fig('fig_pcl5_socl2'))
d.basic('Acids + NH₃?', 'Ammonium salt; strong heat → ' + T('amide') + ' (acetamide, benzamide)', **fig('fig_acid_ammonia'))
d.basic('Phthalic acid + NH₃ on strong heating?', 'Ammonium phthalate → phthalamide → ' + T('phthalimide'), **fig('fig_phthalimide'))

d.sec('8.9.3-cooh-group-reactions')
d.basic('Reduction of acids?', T('LiAlH₄') + ' or better ' + T('B₂H₆') + ' → 1° alcohol; ' + X('NaBH₄ does not') + ' reduce –COOH', **fig('fig_acid_reduction'))
d.basic('Why is diborane useful here?', 'It does ' + X('not easily reduce') + ' esters, nitro, halo groups: selective for –COOH')
d.basic('Decarboxylation?', 'Sodium salt + ' + T('soda lime (NaOH : CaO = 3 : 1)') + ', heat → RH + Na₂CO₃', **fig('fig_decarboxylation'))
d.basic('Kolbe electrolysis?', 'Electrolysis of aqueous alkali-metal carboxylates → hydrocarbon with ' + T('twice') + ' the alkyl carbons')

d.sec('8.9.4-hydrocarbon-part')
d.basic('Hell–Volhard–Zelinsky reaction?', 'Acid with α-H + ' + T('X₂ / red P') + ', then H₂O → ' + T('α-halocarboxylic acid'), **fig('fig_hvz'))
d.basic('Ring substitution of benzoic acid?', '–COOH is ' + T('deactivating, meta-directing') + ': m-nitro- and m-bromobenzoic acid', **fig('fig_ring_substitution_acid'))
d.basic('Why no Friedel–Crafts on benzoic acid?', 'Ring deactivated and ' + X('AlCl₃ binds') + ' to the carboxyl group')

d.sec('8.10-uses-of-acids')
d.cloze('Uses: methanoic acid in {{c1::rubber, textile, leather, electroplating}}; hexanedioic acid for {{c2::nylon-6,6}}; sodium benzoate as a {{c3::food preservative}}; higher fatty acids for {{c4::soaps and detergents}}.')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Tests', 'Aldehyde, ketone or both?', [
    ('Tollens’ silver mirror', 'Aldehydes (incl. aromatic)', False), ('Fehling’s red ppt', 'Aliphatic aldehydes only', False),
    ('2,4-DNP orange ppt', 'Both', False), ('Iodoform (yellow)', 'Methyl ketones, ethanal, ethanol', False), ('NaHCO₃ effervescence', 'Neither (acids)', True)],
    term='Distinguishing tests for carbonyl compounds')
table_card(d, 'Name reactions', 'What happens?', [
    ('Clemmensen / Wolff–Kishner', 'C=O → CH₂', False), ('Aldol', 'α-H carbonyl + dil. base → β-hydroxy carbonyl', False),
    ('Cannizzaro', 'No α-H + conc. base → alcohol + salt', False), ('HVZ', 'α-halogenation of acids', False), ('Haloform', 'CH₃CO– → CHX₃ + acid salt', False)],
    term='Reactions of carbonyls and acids')

n = d.write(os.path.join(OUT, 'deck.json'))
print(n, 'cards')
