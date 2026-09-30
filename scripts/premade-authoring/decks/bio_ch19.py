import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch19-chemical-coordination-and-integration')
d = Deck('Chapter 19: Chemical Coordination and Integration', 'Class 11', ['class-11', 'biology', 'ch-19'])
d.description = 'Endocrine glands and their hormones, disorders, hormones of heart, kidney and gut, and mechanism of hormone action'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
EG, PT, AD = (787, 1001), (883, 1001), (1000, 618)

# ---------------------------------------------------------------- 19.1
d.sec('19.1-hormones')
d.basic('Neural vs hormonal coordination?', 'Neural: ' + T('fast but short-lived') + ', point-to-point. Hormonal: slower, ' + T('longer lasting') + ', reaches cells nerves do not innervate.')
d.basic('Why are endocrine glands called ductless?', 'They ' + X('lack ducts') + '; secretions go into the blood')
d.basic('Exocrine vs endocrine gland?', T('Exocrine') + ': secretes through ducts (e.g. salivary). ' + T('Endocrine') + ': ductless, secretes hormones into blood.')
d.basic('Current definition of a hormone?', T('Non-nutrient chemicals') + ' that act as ' + T('intercellular messengers') + ' and are produced in ' + T('trace amounts'))
d.basic('Why was the hormone definition broadened?', 'To include many new molecules made outside the organised endocrine glands (e.g. by the gut, heart, kidney)')

# ---------------------------------------------------------------- 19.2 System
d.sec('19.2-endocrine-system')
d.basic('Organised endocrine glands of the human body?', 'Pituitary, pineal, thyroid, adrenal, pancreas, parathyroid, thymus, gonads (testis, ovary)')
d.basic('Other organs that also produce hormones?', T('Gastrointestinal tract, liver, kidney, heart'))
d.occlusion('Figure 19.1 · Location of endocrine glands', M + 'fig_19_1_endocrine_glands.webp', EG, [
    ('Hypothalamus', wbox(10, 104, 203, 131, EG), True), ('Pituitary', wbox(69, 165, 183, 192, EG), True),
    ('Pineal', wbox(508, 110, 588, 137, EG), True), ('Thyroid and parathyroid', wbox(546, 245, 702, 302, EG), True),
    ('Thymus', wbox(609, 382, 716, 409, EG), True), ('Pancreas', wbox(639, 529, 759, 556, EG), True),
    ('Adrenal', wbox(648, 581, 751, 608, EG), True), ('Ovary (in female)', wbox(50, 780, 186, 838, EG), True),
    ('Testis (in male)', wbox(615, 796, 728, 854, EG), True)])

d.sec('19.2.1-hypothalamus')
d.basic('Location of the hypothalamus?', 'Basal part of the ' + T('diencephalon') + ' (forebrain)')
d.basic('What are hypothalamic nuclei?', 'Groups of ' + T('neurosecretory cells') + ' that produce hormones')
d.basic('Two types of hypothalamic hormones?', T('Releasing') + ' (stimulate pituitary secretion) and ' + T('inhibiting') + ' (inhibit it)')
d.basic('Example of a releasing hormone?', T('GnRH') + ': stimulates pituitary release of gonadotrophins')
d.basic('Example of an inhibiting hormone?', T('Somatostatin') + ': inhibits release of growth hormone')
d.basic('How do hypothalamic hormones reach the anterior pituitary?', 'Through a ' + T('portal circulatory system'))
d.basic('How does the hypothalamus control the posterior pituitary?', 'By ' + T('direct neural regulation'))
d.occlusion('Figure 19.2 · Pituitary and hypothalamus', M + 'fig_19_2_pituitary.webp', PT, [
    ('Hypothalamus', wbox(366, 26, 616, 61, PT), True), ('Hypothalamic neurons', wbox(611, 92, 848, 169, PT), True),
    ('Portal circulation', wbox(471, 588, 766, 623, PT), True), ('Posterior pituitary', wbox(534, 742, 686, 818, PT), True),
    ('Anterior pituitary', wbox(143, 909, 290, 985, PT), True)])

d.sec('19.2.2-pituitary')
d.basic('Where is the pituitary located?', 'In a bony cavity, the ' + T('sella turcica') + ', attached to the hypothalamus by a stalk')
d.basic('Correction: NCERT prints "sella tursica". Correct spelling?', T('Sella turcica') + ' ("Turkish saddle")')
d.basic('Two anatomical parts of the pituitary?', T('Adenohypophysis') + ' (pars distalis + pars intermedia) and ' + T('neurohypophysis') + ' (pars nervosa)')
d.basic('Six hormones of the pars distalis (anterior pituitary)?', T('GH, PRL, TSH, ACTH, LH, FSH'))
d.basic('Mnemonic for anterior pituitary hormones?', '"' + T('FLAT PiG') + '": FSH, LH, ACTH, TSH, Prolactin, GH')
d.basic('Hormone of the pars intermedia?', T('MSH') + ' (melanocyte stimulating hormone); in humans the pars intermedia is almost merged with the pars distalis')
d.basic('Hormones released by the posterior pituitary?', T('Oxytocin') + ' and ' + T('vasopressin') + '<br>They are made in the ' + T('hypothalamus') + ' and transported axonally.<br>The neurohypophysis only stores and releases them')
table_card(d, 'Growth hormone', 'Disorder?', [
    ('Excess GH in childhood', 'Gigantism', False), ('Low GH in childhood', 'Pituitary dwarfism', False),
    ('Excess GH in adults (middle age)', 'Acromegaly (face disfigured)', False)], term='Growth hormone disorders')
d.basic('Why is acromegaly dangerous?', 'Hard to diagnose early; goes undetected for years; can cause serious complications and ' + T('premature death'))
d.basic('Function of prolactin?', 'Growth of ' + T('mammary glands') + ' and milk formation')
d.basic('Function of TSH?', 'Stimulates synthesis and secretion of ' + T('thyroid hormones'))
d.basic('Function of ACTH?', 'Stimulates ' + T('glucocorticoid') + ' secretion from the adrenal cortex')
d.basic('Why are LH and FSH called gonadotrophins?', 'They stimulate ' + T('gonadal') + ' activity')
d.basic('LH and FSH in males?', T('LH') + ': androgen secretion from testis. ' + T('FSH') + ' + androgens: regulate spermatogenesis.')
d.basic('LH and FSH in females?', T('LH') + ': induces ovulation of the Graafian follicle and maintains the corpus luteum<br>' + T('FSH') + ': growth of ovarian follicles')
d.basic('Function of MSH?', 'Acts on ' + T('melanocytes') + ': regulates skin pigmentation')
d.basic('Functions of oxytocin?', 'Contraction of smooth muscle: vigorous ' + T('uterine contraction') + ' at childbirth and ' + T('milk ejection'))
d.basic('Function of vasopressin, and its other name?', 'Water and electrolyte reabsorption by the distal tubules, reducing water loss; ' + T('ADH (antidiuretic hormone)'))
d.basic('What is diabetes insipidus?', 'Impaired synthesis or release of ' + T('ADH') + ' → kidneys cannot conserve water → water loss, dehydration')
d.basic('Diabetes insipidus vs diabetes mellitus?', 'Insipidus: ' + T('ADH') + ' problem, dilute urine, no sugar. Mellitus: ' + T('insulin') + ' problem, glucose in urine.')
table_card(d, 'Exercise 4', 'Target gland?', [
    ('Hypothalamic hormones', 'Pituitary', False), ('TSH (thyrotrophin)', 'Thyroid', False), ('ACTH (corticotrophin)', 'Adrenal cortex', False),
    ('LH, FSH (gonadotrophins)', 'Gonads', False), ('MSH (melanotrophin)', 'Melanocytes (skin)', False)], term='Pituitary hormones and targets')

d.sec('19.2.3-pineal')
d.basic('Location of the pineal gland?', 'Dorsal side of the ' + T('forebrain'))
d.basic('Hormone of the pineal gland?', T('Melatonin'))
d.basic('Functions of melatonin?', 'Regulates ' + T('24-hour (diurnal) rhythms') + ': sleep-wake cycle, body temperature<br>Also metabolism, pigmentation, menstrual cycle, defence')
d.basic('Why is melatonin secreted mainly at night? (intuition)', 'Light inhibits it; darkness raises it, signalling the body that it is ' + T('night') + '.<br>(That is why screens late at night disturb sleep)')

d.sec('19.2.4-thyroid')
d.basic('Structure of the thyroid gland?', 'Two lobes on either side of the ' + T('trachea') + ', joined by a thin flap, the ' + T('isthmus'), **fig('fig_19_3_thyroid'))
d.basic('What makes up the thyroid gland?', T('Follicles') + ' (follicular cells around a cavity) and stromal tissue')
d.basic('Two thyroid hormones from follicular cells?', T('Thyroxine (T₄)') + ' and ' + T('triiodothyronine (T₃)'))
d.basic('Which element is essential for thyroid hormones?', T('Iodine'))
d.basic('What does iodine deficiency cause?', T('Hypothyroidism') + ' and thyroid enlargement: ' + T('goitre'))
d.basic('What is cretinism?', 'Hypothyroidism ' + T('during pregnancy') + '.<br>The baby shows stunted growth, intellectual disability, low IQ, abnormal skin, deaf-mutism')
d.basic('Effect of hypothyroidism in adult women?', 'Irregular ' + T('menstrual cycle'))
d.basic('Causes of hyperthyroidism?', 'Thyroid ' + T('cancer') + ' or ' + T('nodules'))
d.basic('What is exophthalmic goitre (Graves\' disease)?', 'Hyperthyroidism with enlarged thyroid, ' + T('protruding eyeballs') + ', raised BMR, weight loss')
d.basic('Functions of thyroid hormones?', 'Regulate ' + T('basal metabolic rate') + '; support RBC formation; control carbohydrate, protein, fat metabolism; water and electrolyte balance')
d.basic('What is thyrocalcitonin (TCT)?', 'A protein hormone from the thyroid that ' + T('lowers') + ' blood calcium')
d.basic('Correction: NCERT spells it "Exopthalmic goitre". Correct?', T('Exophthalmic') + ' (Greek ' + I('ophthalmos') + ' = eye)')

d.sec('19.2.5-parathyroid')
d.basic('Number and location of parathyroid glands?', N('Four') + ', on the back side of the thyroid (one pair in each lobe)')
d.basic('Hormone of the parathyroid, and what regulates it?', T('Parathyroid hormone (PTH)') + ', a peptide; regulated by circulating ' + T('Ca²⁺') + ' levels')
d.basic('Three actions of PTH?', 'Stimulates ' + T('bone resorption') + ' (demineralisation); Ca²⁺ reabsorption by renal tubules; Ca²⁺ absorption from digested food')
d.basic('Why is PTH called hypercalcemic?', 'It ' + T('increases') + ' blood Ca²⁺')
d.basic('PTH vs TCT?', T('PTH') + ' raises blood Ca²⁺; ' + T('TCT') + ' lowers it: together they balance calcium')
d.basic('What happens if the parathyroids are removed? (link to Ch 17)', 'Blood Ca²⁺ falls → ' + T('tetany') + ' (muscle spasms)')

d.sec('19.2.6-thymus')
d.basic('Location of the thymus?', 'Between the lungs, behind the ' + T('sternum') + ', on the ventral side of the aorta')
d.basic('Hormones of the thymus?', T('Thymosins') + ' (peptides)')
d.basic('Functions of thymosins?', 'Differentiation of ' + T('T-lymphocytes') + ' (cell-mediated immunity); promote antibody production (humoral immunity)')
d.basic('Why are immune responses weaker in old people?', 'The thymus ' + T('degenerates') + ' with age, so thymosin production falls')

d.sec('19.2.7-adrenal')
d.basic('Location and parts of the adrenal gland?', 'One above each ' + T('kidney') + '; central ' + T('medulla') + ', outer ' + T('cortex'))
d.occlusion('Figure 19.4 · Adrenal gland', M + 'fig_19_4_adrenal.webp', AD, [
    ('Adrenal gland', wbox(151, 22, 303, 43, AD), True), ('Adrenal cortex', wbox(474, 9, 631, 30, AD), True),
    ('Kidney', wbox(241, 482, 314, 503, AD), True), ('Adrenal medulla', wbox(601, 452, 779, 473, AD), True)])
d.basic('Hormones of the adrenal medulla?', T('Adrenaline (epinephrine)') + ' and ' + T('noradrenaline (norepinephrine)') + ': catecholamines')
d.basic('Why are catecholamines called emergency (fight or flight) hormones?', 'They are secreted rapidly in ' + T('stress and emergencies'))
d.basic('Effects of adrenaline and noradrenaline?', 'Alertness, pupil dilation, ' + T('piloerection') + ', sweating; faster, stronger heartbeat; faster breathing; glycogen breakdown (↑ blood glucose); breakdown of lipids and proteins')
d.cloze('Adrenal cortex layers from inside out: {{c1::zona reticularis}} → {{c2::zona fasciculata}} → {{c3::zona glomerulosa}}.')
d.basic('Mnemonic for adrenal cortex layers (outside in) and products?', '"' + T('GFR') + '":<br>Glomerulosa (salt: aldosterone)<br>Fasciculata (sugar: cortisol)<br>Reticularis (sex: androgens)<br>"Salt, sugar, sex"')
d.basic('Glucocorticoids vs mineralocorticoids?', T('Glucocorticoids') + ' (main: cortisol): carbohydrate metabolism<br>' + T('Mineralocorticoids') + ' (main: aldosterone): water and electrolyte balance')
d.basic('Actions of glucocorticoids (cortisol)?', T('Gluconeogenesis') + ', lipolysis, proteolysis; inhibit amino acid uptake; maintain heart and kidney function; ' + T('anti-inflammatory') + ', suppress immunity; stimulate RBC production')
d.basic('Actions of aldosterone?', 'At renal tubules: reabsorbs ' + T('Na⁺ and water') + ', excretes K⁺ and phosphate<br>→ maintains electrolytes, fluid volume, osmotic pressure, BP')
d.basic('Role of adrenal androgens?', 'Growth of axial, pubic and facial hair at ' + T('puberty'))
d.basic('What is Addison\'s disease?', 'Underproduction of adrenal ' + T('cortex') + ' hormones → altered carbohydrate metabolism, acute weakness and fatigue')

d.sec('19.2.8-pancreas')
d.basic('Why is the pancreas a composite gland?', 'It is both ' + T('exocrine') + ' and ' + T('endocrine'))
d.basic('Endocrine part of the pancreas, with numbers?', T('Islets of Langerhans') + ': ' + N('1–2 million') + ', only ' + N('1–2%') + ' of pancreatic tissue')
d.cloze('α-cells secrete {{c1::glucagon}}; β-cells secrete {{c2::insulin}}.')
d.basic('Actions of glucagon?', 'On liver: ' + T('glycogenolysis') + ' and ' + T('gluconeogenesis') + '; reduces cellular glucose uptake → hyperglycemia')
d.basic('Actions of insulin?', 'On hepatocytes and adipocytes: ↑ glucose ' + T('uptake and use') + ', ' + T('glycogenesis') + ' → hypoglycemia')
d.basic('Hyperglycemic vs hypoglycemic hormone?', 'Hyperglycemic: ' + T('glucagon') + ' (also adrenaline, cortisol). Hypoglycemic: ' + T('insulin') + '.')
d.basic('What is diabetes mellitus?', 'Prolonged hyperglycemia from insulin deficiency and/or resistance:<br>glucose in urine, harmful ' + T('ketone bodies') + '<br>Treated with insulin therapy')
d.basic('Mnemonic: α vs β cells?', T('A') + 'lpha → glucagon ("' + T('A') + 'dds' + '" sugar to blood); ' + T('B') + 'eta → insulin ("' + T('B') + 'rings it down")')

d.sec('19.2.9-gonads')
d.basic('Where are the testes, and what are their two roles?', 'In the ' + T('scrotal sac') + ' outside the abdomen; primary sex organ and endocrine gland')
d.basic('Which cells of the testis make androgens?', T('Leydig (interstitial) cells') + ' in the intertubular spaces; mainly ' + T('testosterone'))
d.basic('Functions of androgens?', 'Development of male accessory organs; muscular growth, facial and axillary hair, low voice, aggressiveness; ' + T('spermatogenesis') + '; libido; anabolic effects')
d.basic('Two groups of ovarian hormones?', T('Estrogen') + ' and ' + T('progesterone') + ' (steroids)')
d.basic('Source of estrogen vs progesterone?', 'Estrogen: ' + T('growing ovarian follicles') + '. Progesterone: ' + T('corpus luteum') + ' (after ovulation).')
d.basic('Functions of estrogen?', 'Growth of female secondary sex organs<br>Follicle development<br>' + T('Female secondary sex characters') + ' (high-pitched voice)<br>Mammary development<br>Sexual behaviour')
d.basic('Functions of progesterone?', T('Supports pregnancy') + '; forms mammary alveoli and milk secretion')
d.basic('Progestational hormone?', T('Progesterone'))

# ---------------------------------------------------------------- 19.3
d.sec('19.3-other-hormones')
d.basic('What is ANF, and what does it do?', T('Atrial natriuretic factor') + ' from the atrial wall; ' + T('dilates') + ' vessels to lower blood pressure')
d.basic('Blood-pressure-lowering hormone?', T('ANF'))
d.basic('Hormone of the kidney, and its role?', T('Erythropoietin') + ' (from JG cells): stimulates ' + T('RBC formation'))
table_card(d, 'GI hormones', 'What does it do?', [
    ('Gastrin', 'Gastric glands: HCl and pepsinogen', False), ('Secretin', 'Exocrine pancreas: water and HCO₃⁻', False),
    ('Cholecystokinin (CCK)', 'Pancreatic enzymes and bile', False), ('GIP', 'Inhibits gastric secretion and motility', True)],
    term='Gastrointestinal hormones')
d.basic('What are growth factors?', 'Hormones from non-endocrine tissues, essential for normal ' + T('growth, repair and regeneration'))

# ---------------------------------------------------------------- 19.4 Mechanism
d.sec('19.4-mechanism')
d.basic('How do hormones act on target tissues?', 'By binding to specific ' + T('hormone receptors') + ' present only in target tissues')
d.basic('Membrane-bound vs intracellular receptors?', T('Membrane-bound') + ': on the cell membrane. ' + T('Intracellular') + ': inside the cell, mostly nuclear.')
d.basic('Why are hormone receptors specific?', 'Each receptor binds ' + T('one hormone only'))
table_card(d, 'Hormone chemistry', 'Examples?', [
    ('Peptide/protein', 'Insulin, glucagon, pituitary and hypothalamic hormones', False), ('Steroids', 'Cortisol, testosterone, estradiol, progesterone', False),
    ('Iodothyronines', 'Thyroid hormones', False), ('Amino-acid derivatives', 'Epinephrine', False)], term='Chemical nature of hormones')
d.basic('How do hormones with membrane receptors act?', 'They do ' + X('not enter') + ' the cell; they generate ' + T('second messengers') + ' (cAMP, IP₃, Ca²⁺) that regulate metabolism', **fig('fig_19_5a_protein_hormone'))
d.basic('Mechanism of action of FSH?', 'FSH binds a ' + T('membrane receptor') + ' on ovarian cells<br>→ second messenger (cAMP)<br>→ biochemical responses<br>→ ovarian growth')
d.basic('How do steroid and thyroid hormones act?', 'Enter the cell, bind ' + T('intracellular receptors') + '; the complex acts on the genome to regulate ' + T('gene expression'), **fig('fig_19_5b_steroid_hormone'))
d.basic('Why can steroid hormones enter cells? (intuition)', 'They are ' + T('lipid-soluble') + ' and pass through the lipid membrane; peptides are water-soluble and cannot')
table_card(d, 'Exercise 9', 'Match', [
    ('T₄', 'Thyroid', False), ('PTH', 'Parathyroid', False), ('GnRH', 'Hypothalamus', False), ('LH', 'Pituitary', False)],
    term='Match the column (Exercise 9)')
table_card(d, 'Exercise 7', 'Which deficiency?', [
    ('Diabetes mellitus', 'Insulin', False), ('Goitre', 'Thyroid hormone (iodine deficiency)', False),
    ('Cretinism', 'Thyroid hormone (in pregnancy/infancy)', False)], term='Hormone deficiency disorders')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
