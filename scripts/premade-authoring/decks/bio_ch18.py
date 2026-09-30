import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch18-neural-control-and-coordination')
d = Deck('Chapter 18: Neural Control and Coordination', 'Class 11', ['class-11', 'biology', 'ch-18'])
d.description = 'Neural system, neuron structure, nerve impulse, synapse, and parts of the human brain'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
NR, SY, BR = (621, 1001), (1001, 759), (1001, 658)
P = lambda x0, y0, x1, y1, size: pad([x0, y0, x1 - x0, y1 - y0], 5, size)

# ---------------------------------------------------------------- Intro
d.sec('18.0-coordination')
d.basic('What is coordination?', 'The process by which two or more organs ' + T('interact and complement') + ' each other\'s functions')
d.basic('Example of coordination during exercise?', 'More muscle activity → more O₂ needed → faster ' + T('breathing, heartbeat') + ' and blood flow')
d.basic('Neural vs endocrine coordination?', T('Neural') + ': quick, point-to-point connections. ' + T('Endocrine') + ': chemical integration through hormones.')

# ---------------------------------------------------------------- 18.1-18.2
d.sec('18.1-neural-system')
d.basic('Specialised cells of the neural system?', T('Neurons') + ': detect, receive and transmit stimuli')
d.basic('Neural system of Hydra?', 'A ' + T('network of neurons') + ' (very simple)')
d.basic('Neural system of insects?', 'A ' + T('brain') + ' with a number of ' + T('ganglia') + ' and neural tissues')

d.sec('18.2-human-neural-system')
d.basic('Two parts of the human neural system?', T('CNS') + ' (brain, spinal cord) and ' + T('PNS') + ' (all nerves associated with the CNS)')
d.basic('Role of the CNS?', 'Site of ' + T('information processing') + ' and control')
d.basic('Afferent vs efferent fibres?', T('Afferent') + ': tissues/organs → CNS. ' + T('Efferent') + ': CNS → tissues/organs.')
d.basic('Mnemonic: afferent vs efferent?', '"' + T('SAME') + '": Sensory = Afferent, Motor = Efferent')
d.basic('Two divisions of the PNS?', T('Somatic') + ' (CNS → skeletal muscles) and ' + T('autonomic') + ' (CNS → involuntary organs, smooth muscles)')
d.basic('Two divisions of the autonomic neural system?', T('Sympathetic') + ' and ' + T('parasympathetic'))
d.basic('What is the visceral nervous system?', 'The part of the PNS (nerves, fibres, ganglia, plexuses)<br>carrying impulses between the CNS and the ' + T('viscera') + ', both ways')
d.basic('Sympathetic vs parasympathetic in one line? (intuition)', T('Sympathetic') + ' = "fight or flight" (heart speeds up). ' + T('Parasympathetic') + ' = "rest and digest" (heart slows).')
table_card(d, 'CNS vs PNS', 'Compare', [
    ('Parts', 'CNS: brain, spinal cord · PNS: cranial and spinal nerves', False),
    ('Role', 'CNS: processing, control · PNS: carries impulses to and from CNS', False)], term='CNS vs PNS')

# ---------------------------------------------------------------- 18.3 Neuron
d.sec('18.3-neuron')
d.basic('Three major parts of a neuron?', T('Cell body, dendrites, axon'))
d.basic('What are Nissl\'s granules, and where are they found?', 'Granular bodies in the ' + T('cell body') + ' and ' + T('dendrites') + ' (not in the axon)')
d.basic('Dendrites vs axon: direction of impulse?', T('Dendrites') + ': towards the cell body. ' + T('Axon') + ': away from the cell body.')
d.basic('What is a synaptic knob?', 'Bulb-like end of each axon branch, with ' + T('synaptic vesicles') + ' containing ' + T('neurotransmitters'))
d.occlusion('Figure 18.1 · Structure of a neuron', M + 'fig_18_1_neuron.webp', NR, [
    ('Dendrites', P(106, 67, 233, 97, NR)), ('Nissl\'s granules', P(28, 134, 233, 163, NR)), ('Cell body', P(113, 225, 233, 255, NR)),
    ('Nucleus', P(125, 292, 230, 322, NR)), ('Schwann cell', P(77, 458, 233, 488, NR)), ('Axon', P(166, 569, 233, 599, NR)),
    ('Myelin sheath', P(143, 661, 233, 724, NR)), ('Node of Ranvier', P(132, 742, 233, 805, NR)),
    ('Axon terminal', P(110, 844, 225, 906, NR)), ('Synaptic knob', P(115, 932, 230, 993, NR))], printed=True)
d.basic('Correction: NCERT\'s Figure 18.1 labels "Schwan cell". Correct spelling?', T('Schwann cell') + ' (after Theodor Schwann)')
table_card(d, 'Neuron types', 'Structure · where?', [
    ('Multipolar', 'One axon, two or more dendrites · cerebral cortex', False),
    ('Bipolar', 'One axon, one dendrite · retina', False), ('Unipolar', 'Cell body with one axon only · embryonic stage', False)],
    term='Multipolar, bipolar, unipolar neurons')
d.basic('Beyond NCERT: where are pseudo-unipolar neurons found in adults?', 'Sensory neurons of the ' + T('dorsal root ganglia') + ': one process that splits into two branches')
d.basic('What forms the myelin sheath in the PNS?', T('Schwann cells'))
d.basic('What are nodes of Ranvier?', 'Gaps between two adjacent ' + T('myelin sheaths'))
d.basic('Where are myelinated fibres found?', 'In ' + T('spinal and cranial nerves'))
d.basic('Where are unmyelinated fibres common?', 'In the ' + T('autonomous and somatic') + ' neural systems; the Schwann cell encloses the axon without forming myelin')
d.basic('Myelinated vs unmyelinated conduction?', 'Myelinated: impulse ' + T('jumps') + ' from node to node (saltatory), much ' + T('faster') + '<br>Unmyelinated: slower, continuous along the membrane')

d.sec('18.3.1-impulse')
d.basic('Why are neurons excitable?', 'Their membranes are ' + T('polarised'))
d.basic('At rest, the axonal membrane is more permeable to?', T('K⁺') + '; nearly impermeable to ' + T('Na⁺') + ' and to negatively charged proteins')
d.basic('Ion distribution across a resting axon?', 'Inside: high ' + T('K⁺') + ' and negative proteins, low Na⁺. Outside: high ' + T('Na⁺') + ', low K⁺.')
d.basic('What does the sodium-potassium pump do?', 'Actively moves ' + N('3 Na⁺ out') + ' for every ' + N('2 K⁺ in'))
d.basic('Charge on the resting membrane?', 'Outer surface ' + T('positive') + ', inner surface ' + T('negative') + ': polarised')
d.basic('What is the resting potential?', 'The electrical potential difference across the ' + T('resting') + ' plasma membrane (about −70 mV)')
d.basic('What happens when a stimulus is applied at site A?', 'Membrane becomes freely permeable to ' + T('Na⁺') + '<br>→ rapid Na⁺ influx<br>→ polarity reversed (inside +, outside −): ' + T('depolarised'), **fig('fig_18_2_impulse'))
d.basic('What is the action potential?', 'The potential difference across the membrane at the depolarised site: the ' + T('nerve impulse'))
d.basic('How is the impulse conducted from A to B?', 'Current flows on the ' + T('inner') + ' surface from A to B and on the ' + T('outer') + ' surface from B to A, depolarising B.<br>This repeats along the axon')
d.basic('How is the resting potential restored?', 'Na⁺ permeability quickly falls and ' + T('K⁺ permeability rises') + '; K⁺ diffuses out: repolarisation')
d.basic('Role of Na⁺ in the action potential?', 'Rapid ' + T('influx of Na⁺') + ' reverses polarity and generates the action potential')
table_card(d, 'Potentials', 'Resting vs action?', [
    ('Membrane state', 'Resting: polarised · Action: depolarised', False), ('Outside charge', 'Resting: + · Action: −', False),
    ('Key ion', 'Resting: K⁺ leak, Na⁺–K⁺ pump · Action: Na⁺ influx', False)], term='Resting vs action potential')

d.sec('18.3.2-synapse')
d.basic('What is a synapse?', 'A junction formed by membranes of a ' + T('pre-synaptic') + ' and a ' + T('post-synaptic') + ' neuron.<br>They may or may not be separated by a synaptic cleft')
d.basic('Electrical vs chemical synapse?', T('Electrical') + ': membranes very close, current flows directly, faster, rare<br>' + T('Chemical') + ': fluid-filled cleft, uses neurotransmitters')
d.basic('Which synapse is faster?', T('Electrical'))
d.basic('Steps of transmission at a chemical synapse?', '1) Impulse at axon terminal<br>2) Vesicles move and ' + T('fuse') + ' with the membrane<br>3) Neurotransmitter released into the cleft<br>4) It binds ' + T('receptors') + ' on the post-synaptic membrane<br>5) Ion channels open → new potential')
d.basic('The new potential in the post-synaptic neuron can be?', T('Excitatory or inhibitory'))
d.occlusion('Figure 18.3 · Axon terminal and synapse', M + 'fig_18_3_synapse.webp', SY, [
    ('Axon', P(754, 57, 827, 87, SY)), ('Axon terminal', P(754, 150, 881, 217, SY)), ('Synaptic vesicles', P(761, 260, 888, 327, SY)),
    ('Pre-synaptic membrane', P(748, 357, 928, 424, SY)), ('Synaptic cleft', P(744, 450, 941, 484, SY)),
    ('Post-synaptic membrane', P(744, 521, 941, 587, SY)), ('Receptors', P(757, 641, 901, 671, SY)),
    ('Neurotransmitters', P(40, 677, 304, 711, SY))], printed=True)
d.basic('Why is conduction across a chemical synapse one-way? (intuition)', 'Only the ' + T('pre-synaptic') + ' side has neurotransmitter vesicles; only the post-synaptic side has receptors')

# ---------------------------------------------------------------- 18.4 CNS
d.sec('18.4-brain')
d.basic('Functions of the brain?', 'Voluntary movement, balance, vital involuntary organs, thermoregulation, hunger, thirst, ' + T('circadian rhythms') + ', endocrine glands, behaviour<br>Also vision, hearing, speech, memory, emotions, thought')
d.cloze('Cranial meninges from outside in: {{c1::dura mater}} → {{c2::arachnoid}} → {{c3::pia mater}}.')
d.basic('Mnemonic for meninges?', '"' + T('DAP') + '": Dura (tough, outer), Arachnoid (middle), Pia (thin, touches brain)')
d.basic('Three major parts of the brain?', T('Forebrain, midbrain, hindbrain'))
d.occlusion('Figure 18.4 · Sagittal section of the human brain', M + 'fig_18_4_brain.webp', BR, [
    ('Cerebral hemisphere', P(602, 32, 862, 60, BR)), ('Corpus callosum', P(739, 117, 947, 144, BR)),
    ('Cerebrum', P(72, 143, 199, 169, BR)), ('Forebrain', P(13, 228, 39, 353, BR)), ('Thalamus', P(250, 394, 369, 422, BR)),
    ('Hypothalamus', P(245, 426, 418, 453, BR)), ('Cerebral aqueduct', P(751, 414, 980, 441, BR)),
    ('Midbrain', P(136, 482, 248, 509, BR)), ('Pons', P(419, 509, 481, 537, BR)), ('Hindbrain', P(122, 543, 248, 570, BR)),
    ('Cerebellum', P(343, 540, 485, 567, BR)), ('Medulla', P(375, 577, 475, 604, BR)), ('Spinal cord', P(123, 609, 265, 636, BR))],
    printed=True, guess='hide-one')

d.sec('18.4.1-forebrain')
d.basic('Parts of the forebrain?', T('Cerebrum, thalamus, hypothalamus'))
d.basic('Most developed part of the human brain?', T('Cerebrum'))
d.basic('What connects the two cerebral hemispheres?', 'The ' + T('corpus callosum') + ' (a tract of nerve fibres)')
d.basic('Why is the cerebral cortex called grey matter?', 'Neuron ' + T('cell bodies') + ' are concentrated there')
d.basic('Why is the inner cerebrum called white matter?', 'Its fibre tracts are covered with ' + T('myelin sheath') + ' (opaque white)')
d.basic('Three kinds of areas in the cerebral cortex?', T('Motor, sensory') + ' and ' + T('association') + ' areas')
d.basic('Functions of association areas?', 'Intersensory associations, ' + T('memory') + ', communication')
d.basic('Why is the cortex folded? (intuition)', 'Folds pack a ' + T('larger surface area') + ' (more neurons) into the skull')
d.basic('Function of the thalamus?', 'Major coordinating centre for ' + T('sensory and motor') + ' signalling')
d.basic('Where is the hypothalamus, and what does it control?', 'At the base of the thalamus; controls ' + T('body temperature') + ', eating and drinking; neurosecretory cells secrete ' + T('hypothalamic hormones'))
d.basic('Which part acts as the master clock?', 'The ' + T('hypothalamus') + ' (its suprachiasmatic nucleus sets circadian rhythms)')
d.basic('What forms the limbic system?', 'Inner parts of the cerebral hemispheres and deep structures such as the ' + T('amygdala') + ' and ' + T('hippocampus'))
d.basic('Functions of the limbic system (with hypothalamus)?', 'Sexual behaviour<br>' + T('Emotional reactions') + ' (excitement, pleasure, rage, fear)<br>Motivation<br>Also olfaction and autonomic responses')
d.basic('Thalamus vs hypothalamus?', T('Thalamus') + ': relays sensory and motor signals. ' + T('Hypothalamus') + ': temperature, hunger, thirst, hormones.')

d.sec('18.4.2-midbrain')
d.basic('Location of the midbrain?', 'Between the ' + T('thalamus/hypothalamus') + ' and the ' + T('pons'))
d.basic('Canal through the midbrain?', 'The ' + T('cerebral aqueduct'))
d.basic('What are the corpora quadrigemina?', T('Four round swellings') + ' on the dorsal midbrain')
d.basic('Function of the midbrain?', 'Receives and integrates ' + T('visual, tactile and auditory') + ' inputs')

d.sec('18.4.3-hindbrain')
d.basic('Parts of the hindbrain?', T('Pons, cerebellum, medulla oblongata'))
d.basic('Function of the pons?', 'Fibre tracts that ' + T('interconnect') + ' different brain regions')
d.basic('Why is the cerebellum surface highly convoluted?', 'To provide space for ' + T('many more neurons'))
d.basic('Function of the cerebellum?', 'Integrates information from the ' + T('semicircular canals') + ' and auditory system: balance and coordination')
d.basic('Cerebrum vs cerebellum?', T('Cerebrum') + ': forebrain; thought, memory, voluntary action. ' + T('Cerebellum') + ': hindbrain; balance, coordination.')
d.basic('Centres in the medulla?', 'Control of ' + T('respiration') + ', cardiovascular reflexes, gastric secretions')
d.basic('What forms the brain stem?', T('Midbrain, pons, medulla oblongata') + ': connects brain and spinal cord')
table_card(d, 'Brain parts', 'Which part?', [
    ('Temperature, hunger, thirst', 'Hypothalamus', False), ('Balance, posture', 'Cerebellum', False),
    ('Breathing, heart reflexes', 'Medulla', False), ('Memory, intelligence', 'Cerebrum', False),
    ('Links the hemispheres', 'Corpus callosum', False), ('Emotions', 'Limbic system', False)], term='Which part of the brain does it?')
d.basic('Correction: NCERT\'s summary says "brain and spiral cord". Correct term?', T('Spinal cord'))

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
