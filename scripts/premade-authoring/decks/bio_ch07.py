import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch07-structural-organisation-in-animals')
d = Deck('Chapter 7: Structural Organisation in Animals', 'Class 11', ['class-11', 'biology', 'ch-7'])
d.description = 'Tissues, organs and organ systems, and the morphology and anatomy of the frog'
M = 'media/'
P = lambda b: pad(b, 6)

# ---------------------------------------------------------------- 7.1
d.sec('7.1-organ-systems')
d.basic('What is a tissue?', 'A group of ' + T('similar cells') + ' with intercellular substances performing a specific function')
d.basic('How many basic tissue types make up all complex animals? Name them.', N('Four') + ': epithelial, connective, muscular, neural')
d.basic('What is an organ system?', 'Two or more ' + T('organs') + ' performing a common function by physical and/or chemical interaction, e.g. digestive system')
d.basic('Which organ does NCERT give as containing all four tissue types?', 'The ' + T('heart'))
d.basic('Morphology vs anatomy, in animals?', T('Morphology') + ': external appearance of organs and body parts. ' + T('Anatomy') + ': morphology of ' + T('internal') + ' organs.')
d.basic('What are epithelia?', 'Sheet-like tissues lining body surfaces, cavities, ducts and tubes, with one ' + T('free surface'))

# ---------------------------------------------------------------- 7.2 Frog
d.sec('7.2-frog')
d.basic('To which class and phylum do frogs belong?', 'Class ' + T('Amphibia') + ', phylum ' + T('Chordata'))
d.basic('Most common Indian frog (NCERT)?', EI('Rana tigrina') + ', the Indian bullfrog')
d.basic('What is the current scientific name of the Indian bullfrog? (beyond NCERT)', EI('Hoplobatrachus tigerinus') + ': NCERT still uses the older name ' + I('Rana tigrina') + '; write NCERT\'s name in board exams')
d.basic('Why are frogs called poikilotherms (cold-blooded)?', 'Their body temperature ' + T('varies') + ' with the environment')
d.basic('What are aestivation and hibernation in frogs?', T('Aestivation') + ': summer sleep. ' + T('Hibernation') + ': winter sleep. Both in deep burrows.')
d.basic('What does NCERT call the frog\'s protective colour change?', T('Mimicry') + ' (NCERT\'s term; the colour change is to hide from enemies, camouflage)')
d.basic('Is the frog\'s colour change really mimicry? (correction)', X('Strictly, no') + '. Blending with the background is ' + T('camouflage') + ' (cryptic colouration). Mimicry means resembling ' + T('another species') + '. For NCERT-based MCQs, NCERT\'s word is "mimicry".')

d.sec('7.2.1-morphology')
d.basic('Why is frog skin smooth and slippery?', 'Presence of ' + T('mucus'))
d.basic('Dorsal and ventral colour of a frog?', 'Dorsal: ' + T('olive green') + ' with dark irregular spots. Ventral: uniformly ' + T('pale yellow') + '.')
d.basic('How does a frog take in water?', 'It ' + X('never drinks') + '; it ' + T('absorbs water through the skin'))
d.basic('Into what is a frog\'s body divided? What is absent?', T('Head') + ' and ' + T('trunk') + '; ' + X('neck and tail absent'))
d.basic('What protects the frog\'s eyes in water?', 'A ' + T('nictitating membrane'))
d.basic('What receives sound in a frog?', 'A membranous ' + T('tympanum') + ' on either side of the eyes')
d.basic('Digits on fore and hind limbs?', 'Fore limb: ' + N('four') + '. Hind limb: ' + N('five') + ' (larger, muscular, webbed for swimming).')
d.basic('How can a male frog be told from a female?', 'Males have ' + T('vocal sacs') + ' and a ' + T('copulatory pad') + ' on the first digit of the fore limb')
d.occlusion('Figure 7.1 · External features of frog', M + 'fig_7_1_frog_external.webp', (1001, 657), [
    ('Head', P((770, 83, 112, 43))), ('Trunk', P((200, 108, 136, 43))), ('Eye', P((774, 183, 78, 43))),
    ('Fore limb', P((737, 463, 204, 43))), ('Hind limb', P((647, 586, 214, 43)))], printed=True)

d.sec('7.2.2-digestive')
d.basic('Why is the frog\'s alimentary canal short?', 'Frogs are ' + T('carnivores') + ', so the intestine is reduced')
d.cloze('Path of food: mouth → {{c1::buccal cavity}} → {{c2::pharynx}} → oesophagus → {{c3::stomach}} → intestine → rectum → {{c4::cloaca}}.')
d.basic('How does a frog capture food?', 'With its ' + T('bilobed tongue'))
d.basic('What is chyme?', 'Partially digested food passed from the stomach to the ' + T('duodenum'))
d.basic('What reaches the duodenum through the common bile duct?', T('Bile') + ' (from the gall bladder) and ' + T('pancreatic juice'))
d.basic('What do bile and pancreatic juice do?', 'Bile ' + T('emulsifies fat') + '; pancreatic juice digests ' + T('carbohydrates and proteins'))
d.basic('Where is digested food absorbed?', 'By ' + T('villi and microvilli') + ' on the inner wall of the intestine')
d.occlusion('Figure 7.2 · Internal organs of frog (digestive system)', M + 'fig_7_2_frog_internal.webp', (1001, 733), [
    ('Heart', P((168, 38, 59, 21))), ('Oesophagus', P((525, 57, 130, 21))), ('Liver', P((596, 136, 53, 21))),
    ('Gall bladder', P((11, 180, 81, 45))), ('Lung', P((32, 264, 54, 21))), ('Stomach', P((633, 304, 94, 21))),
    ('Fat bodies', P((75, 370, 109, 21))), ('Kidney', P((101, 420, 72, 21))), ('Ureter', P((154, 499, 68, 21))),
    ('Intestine', P((815, 501, 94, 21))), ('Urinary bladder', P((15, 564, 82, 46))), ('Rectum', P((800, 589, 81, 21))),
    ('Cloaca', P((44, 649, 72, 21))), ('Cloacal aperture', P((767, 690, 180, 21)))], printed=True)

d.sec('7.2.2-respiration')
d.basic('What is cutaneous respiration? When?', 'Gas exchange through the ' + T('skin') + ' by diffusion: in water, and during aestivation and hibernation')
d.basic('Which organs does a frog breathe with on land?', T('Buccal cavity, skin and lungs'))
d.basic('What is pulmonary respiration?', 'Respiration by the ' + T('lungs'))
d.basic('Describe frog lungs.', 'A pair of elongated, pink, sac-like structures in the upper trunk (thorax)')

d.sec('7.2.2-circulation')
d.basic('What type of vascular system does a frog have?', 'Well developed, ' + T('closed') + ', plus a lymphatic system')
d.basic('Chambers of the frog heart? What covers it?', N('Three') + ': two atria, one ventricle; covered by the ' + T('pericardium'))
d.basic('What is the sinus venosus?', 'A ' + T('triangular') + ' structure joining the ' + T('right atrium') + '; it receives blood through the vena cava')
d.basic('Into what does the frog ventricle open?', 'A sac-like ' + T('conus arteriosus') + ' on the ventral side')
d.basic('Hepatic portal vs renal portal system?', T('Hepatic portal') + ': between liver and intestine. ' + T('Renal portal') + ': between kidney and lower parts of the body.')
d.basic('Frog RBCs: nucleated or not?', T('Nucleated') + ', with haemoglobin')
d.basic('How does lymph differ from blood?', 'It lacks ' + X('RBCs') + ' and a few proteins')
d.basic('Single or double circulation in frog?', T('Single') + ' circulation (NCERT summary): the 3-chambered heart mixes some blood. Many texts call it "incomplete double" circulation.')

d.sec('7.2.2-excretion')
d.basic('Name the frog\'s excretory organs.', 'A pair of ' + T('kidneys') + ', ureters, cloaca, urinary bladder')
d.basic('Describe frog kidneys.', 'Compact, dark red, ' + T('bean-like') + ', on both sides of the vertebral column')
d.basic('What are the units of the frog kidney?', T('Uriniferous tubules') + ' (nephrons)')
d.basic('Ureters in male vs female frogs?', 'Male: ureters act as ' + T('urinogenital ducts') + ' into the cloaca. Female: ureters and oviducts open ' + T('separately') + '.')
d.basic('What nitrogenous waste does a frog excrete?', T('Urea') + ': it is ' + T('ureotelic'))

d.sec('7.2.2-control')
d.basic('Name the endocrine glands of the frog.', 'Pituitary, thyroid, parathyroid, thymus, pineal body, pancreatic islets, adrenals, gonads')
d.basic('Three divisions of the frog nervous system?', T('Central') + ' (brain, spinal cord), ' + T('peripheral') + ' (cranial, spinal nerves), ' + T('autonomic') + ' (sympathetic, parasympathetic)')
d.basic('How many pairs of cranial nerves in a frog?', N('Ten'))
d.basic('What encloses the frog brain?', 'A bony brain box, the ' + T('cranium'))
d.cloze('Frog brain: forebrain has {{c1::olfactory lobes}}, paired {{c2::cerebral hemispheres}} and unpaired {{c3::diencephalon}}; midbrain has a pair of {{c4::optic lobes}}; hindbrain has {{c5::cerebellum}} and {{c6::medulla oblongata}}.')
d.basic('Through what does the medulla oblongata pass out?', 'The ' + T('foramen magnum') + ', continuing into the spinal cord')
table_card(d, 'Frog · sense organs', 'Which structure for each sense?', [
    ('Touch', 'Sensory papillae', False), ('Taste', 'Taste buds', False), ('Smell', 'Nasal epithelium', False),
    ('Vision', 'Eyes', False), ('Hearing', 'Tympanum with internal ears', False)], term='Frog sense organs')
d.basic('Which frog sense organs are well organised structures?', T('Eyes') + ' and ' + T('internal ears') + '; the rest are cell clusters around nerve endings')
d.basic('What kind of eyes does a frog have?', T('Simple') + ' eyes (one unit each), in the orbits')
d.basic('Besides hearing, what does the frog ear do?', T('Balancing') + ' (equilibrium)')

d.sec('7.2.2-reproduction')
d.basic('Describe frog testes and their attachment.', 'A pair of ' + T('yellowish ovoid') + ' testes attached to the kidneys by a double fold of peritoneum, the ' + T('mesorchium'))
d.basic('How many vasa efferentia arise from frog testes, and where do they go?', N('10–12') + '; they enter the kidneys and open into ' + T("Bidder's canal"))
d.basic('What passes out through the cloaca?', 'Faecal matter, urine, and sperms')
d.occlusion('Figure 7.3 · Male reproductive system of frog', M + 'fig_7_3_male_reproductive.webp', (1001, 891), [
    ('Vasa efferentia', [300, 0, 240, 104]), ('Fat bodies', P((710, 181, 125, 85))), ('Testis', P((53, 309, 117, 39))),
    ('Kidney', P((702, 337, 134, 39))), ('Adrenal gland', P((12, 450, 156, 85))), ('Urinogenital duct', P((702, 523, 236, 86))),
    ('Rectum', P((61, 656, 150, 39))), ('Cloaca', P((706, 713, 134, 39))), ('Cloacal aperture', P((702, 768, 171, 85))),
    ('Urinary bladder', P((57, 768, 153, 85)))], printed=True)
d.basic('Is there a functional connection between frog ovaries and kidneys?', X('No'))
d.basic('How many ova can a mature female frog lay at a time?', N('2500–3000'))
d.basic('Fertilisation and development in frogs?', 'Fertilisation ' + T('external') + ', in water; a larval ' + T('tadpole') + ' undergoes ' + T('metamorphosis'))
d.occlusion('Figure 7.4 · Female reproductive system of frog', M + 'fig_7_4_female_reproductive.webp', (994, 1001), [
    ('Oviduct', P((765, 82, 149, 38))), ('Ovary', P((765, 268, 113, 38))), ('Ova', P((772, 325, 74, 38))), ('Ureter', P((765, 491, 122, 38))),
    ('Cloaca', P((606, 753, 130, 38))), ('Cloacal aperture', P((606, 836, 320, 38))), ('Urinary bladder', P((606, 906, 149, 83)))], printed=True)
d.basic('How are frogs useful to us?', 'They eat insects and protect crops; they are a link in food chains and webs')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
