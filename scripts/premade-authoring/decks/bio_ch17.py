import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch17-locomotion-and-movement')
d = Deck('Chapter 17: Locomotion and Movement', 'Class 11', ['class-11', 'biology', 'ch-17'])
d.description = 'Types of movement, muscles, sarcomere, sliding filament theory, human skeleton, joints and disorders'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
MC, AM, SK, VC = (1001, 608), (1001, 571), (1001, 704), (950, 1001)
PV, PC, RC = (872, 1001), (811, 1001), (1001, 891)

# ---------------------------------------------------------------- Intro, 17.1
d.sec('17.0-intro')
d.basic('Movement vs locomotion?', T('Locomotion') + ' = voluntary movement that changes ' + T('place') + '. All locomotions are movements, but ' + X('not all') + ' movements are locomotions.')
d.basic('Structure used for both feeding and locomotion in Paramoecium?', T('Cilia') + ' (move food through cytopharynx and help locomotion)')
d.basic('Structure used for both prey capture and locomotion in Hydra?', T('Tentacles'))
d.basic('Why do animals locomote?', 'Search of food, shelter, mate, breeding grounds, favourable climate, or to ' + T('escape predators'))

d.sec('17.1-types-of-movement')
d.basic('Three types of movement shown by human cells?', T('Amoeboid, ciliary, muscular'))
d.basic('Which human cells show amoeboid movement?', T('Macrophages') + ' and ' + T('leucocytes'))
d.basic('What causes amoeboid movement?', T('Pseudopodia') + ' formed by protoplasmic streaming; ' + T('microfilaments') + ' are involved')
d.basic('Two examples of ciliary movement in humans?', 'Cilia in the ' + T('trachea') + ' remove dust; cilia move ' + T('ova') + ' through the female reproductive tract')
d.basic('Examples of flagellar movement?', 'Swimming of ' + E('spermatozoa') + ', water current in ' + E('sponge') + ' canals, locomotion of ' + EI('Euglena'))
d.basic('Locomotion needs coordination of which systems?', T('Muscular, skeletal and neural'))

# ---------------------------------------------------------------- 17.2 Muscle
d.sec('17.2-muscle')
d.basic('Germ-layer origin of muscle?', T('Mesoderm'))
d.basic('What percentage of adult body weight is muscle?', N('40–50%'))
d.basic('Four properties of muscle?', T('Excitability, contractility, extensibility, elasticity'))
table_card(d, 'Muscle types', 'Striated? Voluntary? Where?', [
    ('Skeletal', 'Striated · voluntary · attached to bones', False), ('Visceral (smooth)', 'Non-striated · involuntary · walls of hollow organs', False),
    ('Cardiac', 'Striated · involuntary · heart (branched)', False)], term='Skeletal vs visceral vs cardiac muscle')
d.basic('Skeletal vs cardiac muscle?', 'Both ' + T('striated') + '. Skeletal: voluntary, unbranched. Cardiac: ' + T('involuntary') + ', ' + T('branched') + '.')
d.basic('Roles of visceral muscle?', 'Moving food through the ' + T('digestive tract') + ' and gametes through the ' + T('genital tract'))

d.sec('17.2-skeletal-muscle-structure')
d.basic('What holds muscle bundles (fascicles) together?', 'A collagenous connective tissue layer, the ' + T('fascia'))
d.basic('Plasma membrane and cytoplasm of a muscle fibre?', T('Sarcolemma') + ' and ' + T('sarcoplasm'))
d.basic('Why is a muscle fibre a syncytium?', 'Its sarcoplasm has ' + T('many nuclei'))
d.basic('Store house of calcium in a muscle fibre?', T('Sarcoplasmic reticulum'))
d.occlusion('Figure 17.1 · Cross section of a muscle', M + 'fig_17_1_muscle_cs.webp', MC, [
    ('Fascicle (muscle bundle)', wbox(710, 173, 870, 218, MC), True), ('Muscle fibre (muscle cell)', wbox(117, 309, 242, 354, MC), True),
    ('Sarcolemma', wbox(116, 382, 241, 403, MC), True), ('Blood capillary', wbox(94, 441, 244, 462, MC), True)])
d.basic('What gives skeletal muscle its striations?', 'Distribution of two proteins, ' + T('actin') + ' and ' + T('myosin') + ', in alternate bands on myofibrils')
d.cloze('Light band = {{c1::I band (isotropic)}}, contains {{c2::actin}}. Dark band = {{c3::A band (anisotropic)}}, contains {{c4::myosin}}.')
d.basic('Mnemonic for A and I bands?', 'd' + T('A') + 'rk = ' + T('A') + ' band; l' + T('I') + 'ght = ' + T('I') + ' band')
d.basic('Thin vs thick filaments?', T('Thin') + ' = actin. ' + T('Thick') + ' = myosin.')
d.basic('What is the Z line?', 'An elastic fibre bisecting each ' + T('I band') + '; thin filaments attach to it')
d.basic('What is the M line?', 'A thin fibrous membrane holding thick filaments together in the middle of the ' + T('A band'))
d.basic('What is a sarcomere?', 'Portion of a myofibril between two successive ' + T('Z lines') + ': the ' + T('functional unit') + ' of contraction', **fig('fig_17_2_sarcomere'))
d.basic('What is the H zone?', 'Central part of the thick filaments ' + X('not overlapped') + ' by thin filaments')
d.basic('True or false: the H zone has both thick and thin filaments.', X('False') + '. The H zone has only ' + T('thick') + ' filaments.')
d.basic('Anatomical vs functional unit of muscle?', 'Anatomical: ' + T('muscle fibre') + '. Functional: ' + T('sarcomere') + '.')

d.sec('17.2.1-contractile-proteins')
d.basic('Structure of an actin (thin) filament?', 'Two ' + T('F-actins') + ' helically wound; each F-actin is a polymer of ' + T('G-actin') + ' monomers')
d.basic('Two other proteins on the thin filament?', T('Tropomyosin') + ' (two filaments along F-actin) and ' + T('troponin') + ' (at regular intervals on tropomyosin)')
d.basic('What masks myosin-binding sites on actin at rest?', 'A subunit of ' + T('troponin'))
d.basic('Monomers of the myosin filament?', T('Meromyosins'))
d.basic('Heavy vs light meromyosin?', T('HMM') + ': globular head + short arm. ' + T('LMM') + ': tail.')
d.basic('What is the cross arm?', 'The HMM (head and short arm) projecting outward from the myosin filament at regular distance and angle')
d.basic('Enzyme activity of the myosin head?', 'It is an ' + T('ATPase') + ', with binding sites for ATP and active sites for actin')
d.occlusion('Figure 17.3 · Actin filament and myosin monomer', M + 'fig_17_3_actin_myosin.webp', AM, [
    ('Actin binding sites', wbox(354, 305, 553, 327, AM), True), ('ATP binding sites', wbox(370, 346, 556, 368, AM), True),
    ('Head', wbox(747, 320, 802, 342, AM), True), ('Cross arm', wbox(744, 418, 855, 440, AM), True)])
table_card(d, 'Actin vs myosin', 'Compare', [
    ('Filament', 'Actin: thin · Myosin: thick', False), ('Band', 'Actin: I band · Myosin: A band', False),
    ('Units', 'Actin: G-actin → F-actin · Myosin: meromyosin', False), ('Extra', 'Actin: troponin, tropomyosin · Myosin: ATPase head', False)],
    term='Actin vs myosin')

d.sec('17.2.2-contraction')
d.basic('State the sliding filament theory.', 'Contraction occurs by ' + T('sliding of thin filaments over thick filaments'))
d.basic('What is a motor unit?', 'A ' + T('motor neuron') + ' plus the muscle fibres connected to it')
d.basic('What is the neuromuscular junction?', 'Junction between a motor neuron and the sarcolemma: the ' + T('motor-end plate'))
d.basic('Neurotransmitter at the neuromuscular junction?', T('Acetylcholine'))
d.basic('Steps of muscle contraction?', 'Nerve signal → ' + T('ACh') + ' → action potential in sarcolemma → ' + T('Ca²⁺') + ' released → Ca²⁺ binds ' + T('troponin') + ' → actin sites unmasked → myosin head (ATP energy) binds → ' + T('cross bridge') + ' pulls actin to centre of A band → sarcomere shortens')
d.basic('During contraction, which bands shorten and which stay the same?', T('I band') + ' (and H zone) shorten; ' + T('A band') + ' keeps its length', **fig('fig_17_5_sliding_filament'))
d.basic('What breaks the cross bridge?', 'A new ' + T('ATP') + ' binds to the myosin head', **fig('fig_17_4_cross_bridge'))
d.basic('What causes relaxation?', 'Ca²⁺ pumped back to the ' + T('sarcoplasmic cisternae') + '; actin sites masked again; Z lines return')
d.basic('Why do dead bodies become stiff (rigor mortis)? (intuition)', 'With no ' + T('ATP') + ', myosin heads cannot detach from actin, so cross bridges stay locked')
d.basic('What causes muscle fatigue?', T('Lactic acid') + ' from anaerobic breakdown of glycogen after repeated activation')
d.basic('Oxygen-storing pigment of muscle?', T('Myoglobin') + ' (red)')
d.basic('Red vs white muscle fibres?', T('Red') + ': much myoglobin, many mitochondria, aerobic. ' + T('White') + ': little myoglobin, few mitochondria, much sarcoplasmic reticulum, anaerobic.')
d.basic('Example: which fibres dominate in a flying bird\'s breast vs a chicken\'s breast?', 'Long-flying birds: ' + T('red') + ' (endurance). Chicken breast: ' + T('white') + ' (short bursts).')
d.cloze('In a muscle fibre, Ca²⁺ is stored in the {{c1::sarcoplasmic reticulum}}; the thin filament has two F-actins plus {{c2::tropomyosin}} and {{c3::troponin}}.')

# ---------------------------------------------------------------- 17.3 Skeletal system
d.sec('17.3-skeleton')
d.basic('Bone vs cartilage matrix?', 'Bone: very hard (' + T('calcium salts') + '). Cartilage: slightly pliable (' + T('chondroitin salts') + ').')
d.basic('Number of bones in the human skeleton?', N('206') + ' (plus a few cartilages)')
d.basic('Number of bones in the axial skeleton?', N('80'))
d.basic('Parts of the axial skeleton?', T('Skull, vertebral column, sternum, ribs'))
d.basic('Number of bones in the skull?', N('22') + ': ' + N('8') + ' cranial + ' + N('14') + ' facial')
d.cloze('The human cranium is made of {{c1::8}} bones; the face has {{c2::14}}.')
d.basic('Where is the hyoid bone, and its shape?', 'A single ' + T('U-shaped') + ' bone at the base of the buccal cavity')
d.basic('Three ear ossicles?', T('Malleus, incus, stapes') + ' (in each middle ear)')
d.basic('Why is the human skull called dicondylic?', 'It articulates with the vertebral column by ' + N('two') + ' occipital condyles')
d.occlusion('Figure 17.6 · Human skull', M + 'fig_17_6_skull.webp', SK, [
    ('Parietal bone', wbox(57, 112, 148, 166, SK), True), ('Frontal bone', wbox(477, 7, 631, 32, SK), True),
    ('Temporal bone', wbox(41, 313, 154, 367, SK), True), ('Occipital bone', wbox(40, 432, 146, 486, SK), True),
    ('Occipital condyle', wbox(26, 527, 132, 581, SK), True), ('Sphenoid bone', wbox(712, 146, 891, 171, SK), True),
    ('Ethmoid bone', wbox(710, 203, 878, 228, SK), True), ('Lacrimal bone', wbox(747, 247, 917, 272, SK), True),
    ('Nasal bone', wbox(775, 293, 907, 318, SK), True), ('Zygomatic bone', wbox(809, 380, 997, 405, SK), True),
    ('Maxilla', wbox(798, 454, 885, 479, SK), True), ('Mandible', wbox(807, 576, 918, 601, SK), True),
    ('Hyoid bone', wbox(710, 656, 845, 681, SK), True)], guess='hide-one')

d.sec('17.3-vertebral-column')
d.basic('Number of vertebrae in an adult?', N('26'))
d.basic('What passes through the neural canal?', 'The ' + T('spinal cord'))
d.basic('First vertebra, and what does it articulate with?', T('Atlas') + '; with the occipital condyles')
d.cloze('Vertebral column: cervical {{c1::7}}, thoracic {{c2::12}}, lumbar {{c3::5}}, sacral {{c4::1 (fused)}}, coccygeal {{c5::1 (fused)}}.')
d.basic('Mnemonic for vertebral counts?', '"Breakfast at ' + N('7') + ', lunch at ' + N('12') + ', dinner at ' + N('5') + '": cervical 7, thoracic 12, lumbar 5')
d.basic('Number of cervical vertebrae in almost all mammals?', N('Seven') + ', even in the giraffe and the whale')
d.basic('Functions of the vertebral column?', 'Protects the ' + T('spinal cord') + ', supports the head, gives attachment to ribs and back muscles')
d.occlusion('Figure 17.7 · Vertebral column (right lateral view)', M + 'fig_17_7_vertebral_column.webp', VC, [
    ('Cervical vertebra', wbox(619, 14, 921, 51, VC), True), ('Thoracic vertebra', wbox(664, 323, 817, 403, VC), True),
    ('Lumbar vertebra', wbox(663, 617, 810, 697, VC), True), ('Intervertebral disc', wbox(46, 620, 290, 700, VC), True),
    ('Sacrum', wbox(115, 779, 255, 816, VC), True), ('Coccyx', wbox(161, 901, 287, 938, VC), True)])

d.sec('17.3-ribs')
d.basic('What is the sternum?', 'A ' + T('flat bone') + ' on the ventral midline of the thorax')
d.basic('How many pairs of ribs?', N('12'))
d.basic('Why are ribs called bicephalic?', 'Each has ' + N('two') + ' articulation surfaces on its dorsal end')
d.basic('What are true ribs?', 'First ' + N('7') + ' pairs: attached dorsally to thoracic vertebrae and ventrally to the sternum by ' + T('hyaline cartilage'))
d.basic('What are vertebrochondral (false) ribs?', N('8th, 9th, 10th') + ' pairs: join the ' + T('7th rib') + ' by hyaline cartilage, not the sternum directly')
d.basic('What are floating ribs?', N('11th and 12th') + ' pairs: ' + X('not connected ventrally'))
d.basic('What forms the rib cage?', T('Thoracic vertebrae, ribs, sternum'))
d.occlusion('Figure 17.8 · Ribs and rib cage', M + 'fig_17_8_rib_cage.webp', RC, [
    ('True ribs', [44, 260, 162, 35]), ('False ribs', [12, 605, 99, 79]), ('Floating ribs', [12, 819, 218, 36]),
    ('Sternum', [809, 282, 163, 35]), ('Ribs', [793, 450, 147, 36]), ('Vertebral column', [809, 559, 167, 80])], printed=True)

d.sec('17.3-appendicular')
d.basic('What forms the appendicular skeleton?', 'Bones of the ' + T('limbs') + ' and their ' + T('girdles'))
d.basic('Bones in each limb?', N('30'))
d.cloze('Fore limb: humerus, radius and ulna, carpals ({{c1::8}}), metacarpals ({{c2::5}}), phalanges ({{c3::14}}).')
d.cloze('Hind limb: femur, tibia and fibula, tarsals ({{c1::7}}), metatarsals ({{c2::5}}), phalanges ({{c3::14}}), and patella.')
d.basic('Longest bone in the body?', T('Femur') + ' (thigh bone)')
d.basic('What is the patella?', 'A cup-shaped bone covering the knee ventrally: the ' + T('knee cap'))
d.basic('Why 14 phalanges per hand?', 'Thumb has ' + N('2') + ', each of the other four fingers has ' + N('3') + ': 2 + 12')
d.basic('Function of girdles?', 'Articulate the limbs with the ' + T('axial skeleton'))
d.basic('Each half of the pectoral girdle consists of?', 'A ' + T('clavicle') + ' and a ' + T('scapula'))
d.basic('Position of the scapula?', 'A large triangular flat bone in the dorsal thorax between the ' + N('2nd and 7th') + ' ribs')
d.basic('What is the acromion?', 'The flat expanded process of the scapula\'s ' + T('spine') + '; the clavicle articulates with it')
d.basic('What is the glenoid cavity?', 'A depression below the acromion that articulates with the head of the ' + T('humerus') + ' (shoulder joint)')
d.basic('What is the collar bone?', 'The ' + T('clavicle') + ': a long slender bone with two curvatures')
d.occlusion('Figure 17.9 · Right pectoral girdle and upper arm', M + 'fig_17_9_pectoral_girdle.webp', PC, [
    ('Clavicle', [267, 9, 129, 36]), ('Scapula', [423, 352, 138, 36]), ('Humerus', [441, 434, 160, 36]),
    ('Radius', [423, 577, 123, 35]), ('Ulna', [430, 637, 82, 36]), ('Carpals', [405, 775, 129, 36]),
    ('Metacarpals', [410, 828, 202, 36]), ('Phalanges', [405, 911, 170, 35])], printed=True)
d.basic('Pelvic girdle consists of?', 'Two ' + T('coxal bones'))
d.basic('Each coxal bone is formed by fusion of?', T('Ilium, ischium, pubis'))
d.basic('What is the acetabulum?', 'The cavity at the fusion point of ilium, ischium and pubis, where the ' + T('femur') + ' articulates')
d.basic('What is the pubic symphysis?', 'Ventral meeting of the two halves of the pelvic girdle, containing ' + T('fibrous cartilage'))
d.occlusion('Figure 17.10 · Right pelvic girdle and lower limb', M + 'fig_17_10_pelvic_girdle.webp', PV, [
    ('Ilium', [122, 36, 96, 35]), ('Coxal bone', [572, 82, 196, 36]), ('Sacrum', [568, 154, 138, 35]),
    ('Pubis', [122, 154, 101, 35]), ('Ischium', [76, 203, 147, 33]), ('Femur', [568, 334, 116, 33]),
    ('Patella', [572, 501, 118, 36]), ('Tibia', [568, 639, 91, 34]), ('Fibula', [572, 706, 112, 33]),
    ('Tarsals', [474, 822, 132, 35]), ('Metatarsals', [479, 873, 205, 36]), ('Phalanges', [481, 924, 180, 36])], printed=True)
table_card(d, 'Girdles', 'Pectoral vs pelvic?', [
    ('Bones per half', 'Pectoral: clavicle + scapula · Pelvic: coxal (ilium, ischium, pubis)', False),
    ('Socket', 'Pectoral: glenoid cavity · Pelvic: acetabulum', False), ('Limb', 'Pectoral: fore limb · Pelvic: hind limb', False)],
    term='Pectoral vs pelvic girdle')

# ---------------------------------------------------------------- 17.4 Joints
d.sec('17.4-joints')
d.basic('What are joints?', 'Points of contact between bones, or between bones and cartilages; they act as a ' + T('fulcrum'))
d.basic('Three structural types of joints?', T('Fibrous, cartilaginous, synovial'))
d.basic('Fibrous joints: movement and example?', X('No movement') + '; ' + E('sutures') + ' between flat skull bones')
d.basic('Cartilaginous joints: movement and example?', T('Limited') + ' movement; between adjacent ' + E('vertebrae'))
d.basic('What characterises a synovial joint?', 'A fluid-filled ' + T('synovial cavity') + ' between the articulating surfaces; allows considerable movement')
table_card(d, 'Synovial joints', 'Example?', [
    ('Ball and socket', 'Humerus and pectoral girdle (shoulder); femur and acetabulum', False), ('Hinge', 'Knee (also between phalanges)', False),
    ('Pivot', 'Atlas and axis', False), ('Gliding', 'Between carpals', False), ('Saddle', 'Carpal and metacarpal of thumb', False)],
    term='Types of synovial joints')
table_card(d, 'Exercise 9', 'Type of joint?', [
    ('Atlas / axis', 'Pivot', False), ('Carpal / metacarpal of thumb', 'Saddle', False), ('Between phalanges', 'Hinge', False),
    ('Femur / acetabulum', 'Ball and socket', False), ('Between cranial bones', 'Fibrous (suture)', False),
    ('Between pubic bones', 'Cartilaginous', False)], term='Name the joint (Exercise 9)')

# ---------------------------------------------------------------- 17.5 Disorders
d.sec('17.5-disorders')
table_card(d, 'Disorders', 'What is it?', [
    ('Myasthenia gravis', 'Autoimmune; neuromuscular junction → fatigue, paralysis', False),
    ('Muscular dystrophy', 'Progressive muscle degeneration, mostly genetic', False),
    ('Tetany', 'Rapid muscle spasms from low Ca²⁺', False), ('Arthritis', 'Inflammation of joints', False),
    ('Osteoporosis', 'Less bone mass, more fractures; low estrogen', False), ('Gout', 'Joint inflammation from uric acid crystals', False)],
    term='Muscular and skeletal disorders')
d.basic('What is myasthenia gravis?', T('Autoimmune') + ' disorder of the ' + T('neuromuscular junction') + ': fatigue, weakening and paralysis of skeletal muscle')
d.basic('What causes tetany?', 'Low ' + T('Ca²⁺') + ' in body fluids → rapid spasms')
d.basic('Common cause of osteoporosis?', 'Decreased ' + T('estrogen') + ' levels (age-related)')
d.basic('What causes gout?', 'Accumulation of ' + T('uric acid crystals') + ' in joints')
table_card(d, 'Exercise 6', 'Match', [
    ('Smooth muscle', 'Involuntary', False), ('Tropomyosin', 'Thin filament', False), ('Red muscle', 'Myoglobin', False),
    ('Skull', 'Sutures', False)], term='Match the column (Exercise 6)')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
