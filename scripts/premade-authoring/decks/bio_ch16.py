import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch16-excretory-products-and-their-elimination')
d = Deck('Chapter 16: Excretory Products and their Elimination', 'Class 11', ['class-11', 'biology', 'ch-16'])
d.description = 'Nitrogenous wastes, excretory organs, kidney and nephron, urine formation, counter current, regulation, micturition, disorders'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
US, KL, NP, MB = (1001, 980), (1001, 855), (1000, 737), (980, 1000)

# ---------------------------------------------------------------- Intro
d.sec('16.0-nitrogenous-wastes')
d.basic('Three major nitrogenous wastes?', T('Ammonia, urea, uric acid'))
d.basic('Most and least toxic nitrogenous waste?', 'Most toxic: ' + T('ammonia') + ' (needs lots of water). Least toxic: ' + T('uric acid') + ' (minimum water loss).')
table_card(d, 'Nitrogenous excretion', 'Which animals?', [
    ('Ammonotelic (ammonia)', 'Bony fishes, aquatic amphibians, aquatic insects', False),
    ('Ureotelic (urea)', 'Mammals, terrestrial amphibians, marine fishes', False),
    ('Uricotelic (uric acid)', 'Reptiles, birds, land snails, insects', False)], term='Ammonotelic, ureotelic, uricotelic animals')
d.basic('How is ammonia excreted?', 'By ' + T('diffusion') + ' across body surfaces or gills as ammonium ions; kidneys play ' + X('no significant role'))
d.basic('Why are terrestrial animals ureotelic or uricotelic, not ammonotelic?', 'To ' + T('conserve water') + ': urea and uric acid are less toxic and need less water to remove')
d.basic('Where is ammonia converted to urea?', 'In the ' + T('liver'))
d.basic('Why do some animals retain urea in the kidney matrix?', 'To maintain a desired ' + T('osmolarity'))
d.basic('In what form do uricotelic animals excrete uric acid?', 'As a ' + T('pellet or paste'))
d.basic('Mnemonic for uricotelic animals?', '"' + T('Birds and Reptiles Save Water') + '": birds, reptiles, land snails and insects excrete uric acid')

d.sec('16.0-excretory-structures')
table_card(d, 'Excretory structures', 'Found in?', [
    ('Protonephridia (flame cells)', 'Flatworms (Planaria), rotifers, some annelids, Amphioxus', False),
    ('Nephridia', 'Earthworm, other annelids', False), ('Malpighian tubules', 'Most insects (cockroach)', False),
    ('Antennal (green) glands', 'Crustaceans (prawn)', False), ('Kidneys', 'Vertebrates', False)], term='Excretory structures across animals')
d.basic('Main function of protonephridia?', T('Osmoregulation') + ' (ionic and fluid volume regulation)')
d.basic('A chordate with flame cells?', EI('Amphioxus') + ' (cephalochordate)')
d.basic('What is osmoregulation?', 'Regulation of ' + T('water and ionic balance') + ' of body fluids')

# ---------------------------------------------------------------- 16.1 Human excretory system
d.sec('16.1-human-system')
d.basic('Parts of the human excretory system?', 'A pair of ' + T('kidneys') + ', a pair of ' + T('ureters') + ', a ' + T('urinary bladder') + ' and a ' + T('urethra'))
d.occlusion('Figure 16.1 · Human urinary system', M + 'fig_16_1_urinary_system.webp', US, [
    ('Adrenal gland', [658, 10, 273, 43]), ('Inferior vena cava', [84, 91, 196, 74]), ('Renal artery', [717, 101, 235, 43]),
    ('Pelvis', [119, 213, 112, 43]), ('Renal vein', [780, 185, 207, 43]), ('Medulla', [14, 311, 157, 43]),
    ('Kidney', [735, 304, 136, 43]), ('Cortex', [140, 434, 130, 42]), ('Dorsal aorta', [703, 480, 242, 42]),
    ('Ureter', [721, 556, 126, 43]), ('Urinary bladder', [693, 749, 154, 84]), ('Urethra', [693, 868, 151, 42])], printed=True)
d.basic('Location of the kidneys?', 'Between the ' + T('last thoracic and third lumbar') + ' vertebrae, close to the dorsal inner wall of the abdominal cavity')
d.basic('Size and weight of an adult kidney?', N('10–12 cm') + ' long, ' + N('5–7 cm') + ' wide, ' + N('2–3 cm') + ' thick; ' + N('120–170 g'))
d.basic('What is the hilum?', 'A notch on the inner ' + T('concave') + ' surface through which ureter, blood vessels and nerves enter')
d.basic('What is the renal pelvis?', 'A broad ' + T('funnel-shaped') + ' space inner to the hilum, with projections called ' + T('calyces'))
d.basic('Two zones inside the kidney?', 'Outer ' + T('cortex') + ' and inner ' + T('medulla'))
d.basic('What are medullary pyramids?', 'Conical masses of the medulla projecting into the ' + T('calyces'))
d.basic('What are the columns of Bertini?', 'Extensions of the ' + T('cortex') + ' between medullary pyramids (renal columns)')
d.occlusion('Figure 16.2 · L.S. of kidney', M + 'fig_16_2_kidney_ls.webp', KL, [
    ('Medullary pyramid', [557, 13, 190, 84]), ('Renal column', [104, 125, 145, 87]), ('Calyx', [747, 294, 111, 40]),
    ('Renal artery', [754, 404, 234, 40]), ('Cortex', [23, 494, 127, 40]), ('Renal vein', [754, 484, 200, 40]),
    ('Renal pelvis', [754, 554, 227, 40]), ('Renal capsule', [10, 564, 147, 77]), ('Ureter', [794, 604, 124, 40])], printed=True)

d.sec('16.1-nephron')
d.basic('Functional unit of the kidney, and how many per kidney?', T('Nephron') + '; nearly ' + N('one million'))
d.basic('Two parts of a nephron?', T('Glomerulus') + ' and ' + T('renal tubule'))
d.basic('What is the glomerulus?', 'A tuft of ' + T('capillaries') + ' formed by the afferent arteriole')
d.basic('Afferent vs efferent arteriole?', T('Afferent') + ' (from renal artery) brings blood to the glomerulus; ' + T('efferent') + ' carries it away')
d.basic('Mnemonic: afferent vs efferent?', T('A') + 'fferent = ' + T('A') + 'rrives; ' + T('E') + 'fferent = ' + T('E') + 'xits')
d.basic('What is Bowman\'s capsule?', 'A ' + T('double-walled cup') + ' at the start of the renal tubule, enclosing the glomerulus')
d.basic('What is the Malpighian body (renal corpuscle)?', T('Glomerulus + Bowman\'s capsule'))
d.occlusion('Figure 16.4 · Malpighian body', M + 'fig_16_4_malpighian_body.webp', MB, [
    ('Afferent arteriole', wbox(218, 29, 544, 69, MB), True), ('Efferent arteriole', wbox(747, 160, 907, 247, MB), True),
    ('Bowman\'s capsule', wbox(750, 325, 948, 409, MB), True), ('Proximal convoluted tubule', wbox(555, 851, 905, 936, MB), True)])
d.cloze('Renal tubule: Bowman\'s capsule → {{c1::PCT}} → {{c2::Henle\'s loop}} (descending, ascending limbs) → {{c3::DCT}} → {{c4::collecting duct}} → renal pelvis.')
d.basic('Which parts of the nephron lie in the cortex, and which dip into the medulla?', 'Cortex: ' + T('Malpighian corpuscle, PCT, DCT') + '. Medulla: ' + T('loop of Henle') + '.')
d.basic('Cortical vs juxtamedullary nephrons?', T('Cortical') + ' (majority): short loop, barely enters medulla. ' + T('Juxtamedullary') + ': long loop, deep into medulla.')
d.basic('What are peritubular capillaries?', 'A fine capillary network formed by the ' + T('efferent arteriole') + ' around the renal tubule')
d.basic('What is the vasa recta?', 'A minute ' + T('U-shaped') + ' vessel of the peritubular network running parallel to Henle\'s loop')
d.basic('In which nephrons is the vasa recta absent or reduced?', T('Cortical') + ' nephrons')
d.occlusion('Figure 16.3 · Nephron with blood vessels', M + 'fig_16_3_nephron.webp', NP, [
    ('Afferent arteriole', pad([320, 10, 107, 53], 4, NP)), ('Efferent arteriole', pad([783, 8, 210, 32], 4, NP)),
    ('Glomerulus', pad([273, 90, 154, 30], 4, NP)), ('Bowman\'s capsule', pad([280, 140, 127, 60], 4, NP)),
    ('Proximal convoluted tubule', pad([793, 177, 140, 83], 4, NP)), ('Distal convoluted tubule', pad([767, 303, 150, 84], 4, NP)),
    ('Descending limb of loop of Henle', pad([200, 373, 207, 54], 4, NP)), ('Henle\'s loop', pad([0, 440, 163, 33], 4, NP)),
    ('Ascending limb of loop of Henle', pad([193, 500, 214, 53], 4, NP)), ('Vasa recta', pad([317, 620, 133, 30], 4, NP)),
    ('Collecting duct', pad([737, 610, 190, 27], 4, NP))], printed=True, guess='hide-one')

# ---------------------------------------------------------------- 16.2 Urine formation
d.sec('16.2-urine-formation')
d.cloze('Urine formation: {{c1::glomerular filtration}} → {{c2::reabsorption}} → {{c3::secretion}}.')
d.basic('How much blood do the kidneys filter per minute?', N('1100–1200 mL') + ': about ' + N('1/5') + ' of cardiac output')
d.basic('Three layers of the filtration membrane?', T('Endothelium') + ' of glomerular vessels, ' + T('epithelium') + ' of Bowman\'s capsule, and a ' + T('basement membrane') + ' between them')
d.basic('What are podocytes?', 'Epithelial cells of Bowman\'s capsule, arranged to leave ' + T('filtration slits (slit pores)'))
d.basic('Why is glomerular filtration called ultrafiltration?', 'Filtering is so fine that all plasma constituents ' + X('except proteins') + ' pass into Bowman\'s capsule')
d.basic('What drives glomerular filtration?', T('Glomerular capillary blood pressure'))
d.basic('Why is glomerular blood pressure high? (intuition)', 'The efferent arteriole is ' + T('narrower') + ' than the afferent, so blood backs up in the glomerulus like a nozzle')
d.basic('What is GFR?', 'Amount of filtrate formed by the kidneys per minute: about ' + N('125 mL/min') + ' = ' + N('180 L/day'))
d.basic('What is the JGA?', 'Juxtaglomerular apparatus:<br>a sensitive region formed by cellular modifications of the ' + T('DCT') + ' and ' + T('afferent arteriole') + ' where they touch')
d.basic('How does the JGA restore a falling GFR?', 'JG cells release ' + T('renin') + ', which raises glomerular blood flow and GFR')
d.basic('Filtrate per day vs urine per day?', N('180 L') + ' vs ' + N('1.5 L') + ': nearly ' + N('99%') + ' is reabsorbed')
d.basic('Which substances are reabsorbed actively vs passively?', 'Active: ' + T('glucose, amino acids, Na⁺') + '. Passive: ' + T('nitrogenous wastes') + ', water (in initial segments).')
d.basic('What is secreted by tubular cells?', T('H⁺, K⁺, ammonia'))
d.basic('Importance of tubular secretion?', 'Maintains ' + T('ionic and acid-base balance') + ' of body fluids')

# ---------------------------------------------------------------- 16.3 Tubules
d.sec('16.3-tubules')
d.basic('Lining of the PCT?', 'Simple cuboidal ' + T('brush border') + ' epithelium: more surface area for reabsorption')
d.basic('What is reabsorbed in the PCT?', 'Nearly all ' + T('essential nutrients') + ' and ' + N('70–80%') + ' of electrolytes and water')
d.basic('How does the PCT maintain pH?', 'Secretes ' + T('H⁺ and ammonia') + ' into the filtrate and absorbs ' + T('HCO₃⁻'))
d.basic('Descending limb of Henle\'s loop: permeability?', 'Permeable to ' + T('water') + ', almost impermeable to electrolytes → filtrate becomes ' + T('concentrated'))
d.basic('Ascending limb of Henle\'s loop: permeability?', X('Impermeable to water') + ', allows electrolyte transport → filtrate becomes ' + T('dilute'))
d.cloze('The ascending limb of Henle\'s loop is {{c1::impermeable}} to water, whereas the descending limb is {{c2::permeable}} to it.')
d.basic('Main role of Henle\'s loop?', 'Maintaining high ' + T('osmolarity') + ' of the medullary interstitial fluid (reabsorption is minimal in the ascending limb)')
d.basic('What happens in the DCT?', T('Conditional') + ' reabsorption of Na⁺ and water; reabsorbs HCO₃⁻; secretes H⁺, K⁺, NH₃ (pH and Na–K balance)')
d.basic('Role of the collecting duct?', 'Reabsorbs large amounts of ' + T('water') + ' (concentrated urine); passes some ' + T('urea') + ' to the medulla; secretes H⁺ and K⁺')
d.basic('Figure 16.5: where is glucose reabsorbed?', 'In the ' + T('PCT') + ' (actively)', **fig('fig_16_5_reabsorption'))

# ---------------------------------------------------------------- 16.4 Counter current
d.sec('16.4-counter-current')
d.basic('Which structures help concentrate urine?', T('Henle\'s loop') + ' and ' + T('vasa recta'))
d.basic('Why is it called counter current?', 'Filtrate in the two limbs of Henle\'s loop,<br>and blood in the two limbs of vasa recta,<br>flow in ' + T('opposite directions'))
d.basic('Osmolarity gradient of the medulla?', 'From ' + N('300 mOsmol/L') + ' in the cortex to about ' + N('1200 mOsmol/L') + ' in the inner medulla')
d.basic('Which two solutes cause the medullary gradient?', T('NaCl') + ' and ' + T('urea'))
d.basic('Path of NaCl in the counter current mechanism?', 'Ascending limb of Henle<br>→ exchanged with ' + T('descending vasa recta') + '<br>→ returned to interstitium by ' + T('ascending vasa recta'), **fig('fig_16_6_counter_current'))
d.basic('Path of urea in the counter current mechanism?', 'Small amounts enter the thin ascending limb of Henle\'s loop.<br>Returned to the interstitium by the ' + T('collecting tubule'))
d.basic('How does the medullary gradient concentrate urine?', 'Water leaves the ' + T('collecting duct') + ' easily into the hyperosmotic interstitium')
d.basic('How concentrated can human urine be?', 'Nearly ' + N('four times') + ' the initial filtrate (300 → 1200 mOsmol/L)')

# ---------------------------------------------------------------- 16.5 Regulation
d.sec('16.5-regulation')
d.basic('Kidney function is regulated by feedback involving?', 'The ' + T('hypothalamus') + ', ' + T('JGA') + ' and, to some extent, the ' + T('heart'))
d.basic('What activates osmoreceptors?', 'Changes in blood volume, body fluid volume and ionic concentration')
d.basic('What happens on excessive fluid loss?', 'Osmoreceptors → hypothalamus → ' + T('ADH (vasopressin)') + ' released from the ' + T('neurohypophysis'))
d.basic('What does ADH do?', 'Increases water reabsorption from latter parts of the tubule, ' + T('preventing diuresis') + '.<br>Also constricts vessels, raising BP and GFR')
d.basic('True or false: ADH helps in water elimination, making urine hypotonic.', X('False') + '. ADH conserves water and makes urine ' + T('concentrated (hypertonic)') + '.')
d.basic('Renin-angiotensin mechanism in steps?', 'Fall in GFR<br>→ JG cells release ' + T('renin') + '<br>→ angiotensinogen → angiotensin I → ' + T('angiotensin II') + '<br>→ vasoconstriction ↑ BP<br>Also ' + T('aldosterone') + ' from adrenal cortex')
d.basic('What does angiotensin II do?', 'Powerful ' + T('vasoconstrictor') + ' (↑ glomerular BP, GFR); stimulates ' + T('aldosterone') + ' release')
d.basic('What does aldosterone do?', 'Reabsorption of ' + T('Na⁺ and water') + ' from distal parts of the tubule → ↑ BP and GFR')
d.basic('What is ANF, and when is it released?', T('Atrial natriuretic factor') + ': released by the heart atria when blood flow to them increases')
d.basic('What does ANF do?', T('Vasodilation') + ' → lowers BP; acts as a ' + T('check') + ' on the renin-angiotensin mechanism')
table_card(d, 'Kidney regulation', 'Effect on blood pressure?', [
    ('ADH', 'Raises (water retained, vessels constricted)', False), ('Angiotensin II', 'Raises (vasoconstriction)', False),
    ('Aldosterone', 'Raises (Na⁺ and water retained)', False), ('ANF', 'Lowers (vasodilation)', True)], term='Hormones regulating kidney function')

# ---------------------------------------------------------------- 16.6 Micturition
d.sec('16.6-micturition')
d.basic('What is micturition?', 'The process of ' + T('release of urine'))
d.basic('Micturition reflex in steps?', '1) Bladder stretches<br>2) ' + T('Stretch receptors') + ' signal the CNS<br>3) CNS makes bladder smooth muscle ' + T('contract') + ' and urethral sphincter ' + T('relax'))
d.basic('Urine per day in an adult?', N('1–1.5 L'))
d.basic('Properties of normal urine?', 'Light yellow, watery, slightly ' + T('acidic (pH 6.0)') + ', characteristic odour')
d.basic('Urea excreted per day?', N('25–30 g'))
d.basic('What are glycosuria and ketonuria? What do they indicate?', 'Glucose and ketone bodies in urine; indicate ' + T('diabetes mellitus'))

# ---------------------------------------------------------------- 16.7 Other organs
d.sec('16.7-other-organs')
d.basic('Organs other than kidneys that help in excretion?', T('Lungs, liver, skin') + ' (and a little via saliva)')
d.basic('What do the lungs remove?', 'About ' + N('200 mL CO₂/min') + ' and significant water')
d.basic('What does the liver excrete through bile?', T('Bilirubin, biliverdin') + ', cholesterol, degraded steroid hormones, vitamins, drugs')
d.basic('What does sweat contain?', 'Water, ' + T('NaCl') + ', small amounts of urea, lactic acid')
d.basic('Primary function of sweat?', T('Cooling') + ' the body surface')
d.basic('What do sebaceous glands eliminate?', T('Sterols, hydrocarbons, waxes') + ' via sebum (protective oily covering)')

# ---------------------------------------------------------------- 16.8 Disorders
d.sec('16.8-disorders')
d.basic('What is uremia?', 'Accumulation of ' + T('urea in blood') + ' due to kidney malfunction')
d.basic('Haemodialysis in steps?', '1) Blood from an artery + ' + T('heparin') + '<br>2) Dialysing unit (coiled ' + T('cellophane') + ' tube in dialysing fluid)<br>3) Wastes diffuse out<br>4) ' + T('Anti-heparin') + ' added<br>5) Returned via a vein')
d.basic('Dialysing fluid contains everything in plasma except?', 'The ' + T('nitrogenous wastes'))
d.basic('Why is heparin added before dialysis and anti-heparin after?', 'Heparin stops ' + T('clotting') + ' in the machine; anti-heparin restores normal clotting before blood returns')
d.basic('Ultimate treatment for acute renal failure?', T('Kidney transplantation') + ', preferably from a close relative to minimise rejection')
d.basic('What are renal calculi?', T('Kidney stones') + ': insoluble crystallised salts (oxalates) formed in the kidney')
d.basic('What is glomerulonephritis?', 'Inflammation of the ' + T('glomeruli'))
table_card(d, 'Exercise 7', 'Match', [
    ('Ammonotelism', 'Bony fish', False), ('Bowman\'s capsule', 'Renal tubule', False), ('Micturition', 'Urinary bladder', False),
    ('Uricotelism', 'Birds', False), ('ADH', 'Water reabsorption', False)], term='Match the column (Exercise 7)')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
