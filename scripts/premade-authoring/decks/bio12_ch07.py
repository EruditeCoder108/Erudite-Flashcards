import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch07-human-health-and-disease')
d = Deck('Chapter 7: Human Health and Disease', 'Class 12', ['class-12', 'biology', 'ch-7'])
d.description = 'Common diseases and pathogens, malaria life cycle, immunity, vaccines, allergy, lymphoid organs, AIDS, cancer and drug abuse'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
PL, AB = (897, 1001), (1001, 770)

# ---------------------------------------------------------------- intro
d.sec('7.0-health')
d.basic('Old "humors" idea of health?', 'Health = balance of certain ' + T('humors') + ' (Hippocrates, Ayurveda); "blackbile" persons were hot and had fevers')
d.basic('What disproved the "good humor" hypothesis?', T('William Harvey') + '’s discovery of blood circulation and normal temperature in "blackbile" persons (thermometer)')
d.basic('How does the mind affect health?', 'Through the ' + T('neural and endocrine systems') + ' acting on the immune system')
d.basic('Three factors affecting health?', T('Genetic disorders') + ', ' + T('infections') + ', ' + T('life style') + ' (food, water, rest, exercise, habits)')
d.basic('Define health.', 'A state of complete ' + T('physical, mental and social well-being') + ' (not just absence of disease)')
d.basic('Benefits of good health?', 'More efficiency and productivity, economic prosperity, longevity, lower infant and maternal mortality')
d.basic('Infectious vs non-infectious diseases?', T('Infectious') + ': easily transmitted (e.g. AIDS, fatal). ' + T('Non-infectious') + ': not transmitted; ' + T('cancer') + ' is the major killer.')

# ---------------------------------------------------------------- 7.1 Diseases
d.sec('7.1-common-diseases')
d.basic('What are pathogens?', 'Disease-causing organisms: bacteria, viruses, fungi, protozoans, helminths')
d.basic('Example of pathogen adaptation to the host?', 'Gut pathogens survive stomach’s ' + T('low pH') + ' and resist digestive enzymes')
table_card(d, 'Pathogens', 'Disease?', [
    ('Salmonella typhi', 'Typhoid', False), ('Streptococcus pneumoniae, Haemophilus influenzae', 'Pneumonia', False),
    ('Rhino viruses', 'Common cold', False), ('Plasmodium', 'Malaria', False),
    ('Entamoeba histolytica', 'Amoebiasis', False), ('Ascaris', 'Ascariasis', False),
    ('Wuchereria', 'Filariasis (elephantiasis)', False)], term='Pathogens and their diseases')
d.basic('How does typhoid spread and where does it start?', 'Contaminated ' + T('food and water') + '; enters the ' + T('small intestine') + ', spreads through blood')
d.basic('Symptoms of typhoid?', 'Sustained high fever (' + N('39–40 °C') + '), weakness, stomach pain, constipation, headache, loss of appetite; severe: intestinal perforation')
d.basic('Test to confirm typhoid?', T('Widal test'))
d.basic('Who was "Typhoid Mary"?', T('Mary Mallon') + ', a cook and typhoid ' + T('carrier') + ' who spread it for years through food')
d.basic('What does pneumonia infect, and effect?', 'The ' + T('alveoli') + ' of lungs, which fill with fluid → severe breathing problems')
d.basic('Symptoms of pneumonia?', 'Fever, chills, cough, headache; severe: lips and nails ' + T('grey to bluish'))
d.basic('How is pneumonia acquired?', 'Inhaling ' + T('droplets/aerosols') + ' from an infected person, or sharing glasses and utensils')
d.basic('Other bacterial diseases?', E('Dysentery, plague, diphtheria'))
d.basic('What does the common cold infect?', 'Nose and respiratory passage, ' + X('not the lungs'))
d.basic('Symptoms and duration of common cold?', 'Nasal congestion and discharge, sore throat, hoarseness, cough, headache, tiredness; ' + N('3–7 days'))
d.basic('How does the common cold spread?', 'Droplets inhaled directly or via contaminated objects (pens, books, cups, doorknobs, keyboards)')
d.basic('Species causing malaria?', EI('P. vivax, P. malariae') + ' and ' + EI('P. falciparum'))
d.basic('Correction: NCERT prints "P. malaria". Correct name?', EI('Plasmodium malariae'))
d.basic('Most serious malaria?', T('Malignant malaria') + ' by ' + EI('P. falciparum') + '; can be fatal')
d.basic('Infectious form of Plasmodium entering humans?', T('Sporozoites') + ', via bite of infected ' + T('female Anopheles'))
d.basic('Sequence of Plasmodium in humans?', 'Multiplies in ' + T('liver cells') + ' → attacks ' + T('RBCs') + ' and ruptures them')
d.basic('What causes the chill and fever in malaria?', 'Release of toxic ' + T('haemozoin') + ' when RBCs rupture; recurs every ' + N('3–4 days'))
d.basic('Where do sporozoites form and get stored in the mosquito?', 'Formed after fertilisation in the mosquito’s ' + T('gut') + '; stored in the ' + T('salivary glands'))
d.basic('Where does sexual reproduction of Plasmodium happen?', 'Gametocytes form in human ' + T('RBCs') + '; fertilisation occurs in the ' + T('mosquito gut'))
d.basic('Hosts of Plasmodium?', 'Two: ' + T('human') + ' and ' + T('mosquito') + '; female Anopheles is also the ' + T('vector'))
d.occlusion('Figure 7.1 · Life cycle of Plasmodium', M + 'fig_7_1_plasmodium.webp', PL, [
    ('Sporozoites', wbox(232, 318, 334, 340, PL), True), ('Salivary glands', wbox(196, 374, 332, 396, PL), True),
    ('Mosquito host', wbox(300, 456, 388, 498, PL), True), ('Human host', wbox(504, 652, 574, 692, PL), True),
    ('Gametocytes', wbox(218, 764, 332, 786, PL), True), ('Female gametocyte', wbox(326, 792, 392, 814, PL)),
    ('Male gametocyte', wbox(322, 866, 370, 888, PL))])
d.basic('Mnemonic: Plasmodium stage entering each host?', '"' + T('S into Human, G into Mosquito') + '": Sporozoites enter humans; Gametocytes enter mosquitoes')
d.basic('Where does Entamoeba histolytica live, and disease?', T('Large intestine') + '; amoebiasis (' + T('amoebic dysentery') + ')')
d.basic('Symptoms of amoebiasis?', 'Constipation, abdominal pain and cramps, stools with excess ' + T('mucus and blood clots'))
d.basic('Role of houseflies in amoebiasis?', T('Mechanical carriers') + ': transfer the parasite from faeces to food')
d.basic('Symptoms of ascariasis?', 'Internal bleeding, muscular pain, fever, anaemia, ' + T('blockage of the intestine'))
d.basic('How is ascariasis acquired?', 'Eggs in faeces contaminate soil, water, plants; infection through contaminated ' + T('water, vegetables, fruits'))
d.basic('Species of filarial worms?', EI('Wuchereria bancrofti') + ' and ' + EI('W. malayi'))
d.basic('Effect of filarial worms?', 'Slow chronic inflammation of ' + T('lymphatic vessels of lower limbs') + ' (elephantiasis); genital organs also deformed', **fig('fig_7_2_elephantiasis'))
d.basic('How is filariasis transmitted?', 'Bite of ' + T('female mosquito') + ' vectors')
d.basic('Fungi causing ringworm?', EI('Microsporum, Trichophyton, Epidermophyton'))
d.basic('Symptoms of ringworm?', 'Dry, ' + T('scaly lesions') + ' on skin, nails, scalp, with intense itching', **fig('fig_7_3_ringworm'))
d.basic('Why does ringworm thrive in skin folds?', T('Heat and moisture') + ' (groin, between toes)')
d.basic('How is ringworm acquired?', 'From soil, or using towels, clothes, comb of infected persons')
table_card(d, 'Exercise 3', 'Transmission?', [
    ('Amoebiasis', 'Food/water contaminated with faeces (houseflies)', False), ('Malaria', 'Bite of female Anopheles', False),
    ('Ascariasis', 'Water, vegetables, fruits with eggs', False), ('Pneumonia', 'Droplets, sharing utensils', False)],
    term='Transmission of diseases (Exercise 3)')
d.basic('Personal hygiene measures?', 'Keeping body clean; clean drinking water, food, vegetables, fruits')
d.basic('Public hygiene measures?', 'Proper disposal of waste and excreta; cleaning and disinfecting water reservoirs, pools, tanks; hygiene in public catering')
d.basic('Controlling vector-borne diseases?', 'Avoid stagnant water, clean coolers, mosquito nets, ' + E('Gambusia') + ' fish in ponds, insecticides, wire mesh on doors/windows')
d.basic('Diseases spread by Aedes mosquitoes?', T('Dengue and chikungunya'))
d.basic('Disease eradicated by vaccination?', T('Smallpox') + ' (declared eradicated by WHO in 1980)')
d.basic('Diseases controlled largely by vaccines?', E('Polio, diphtheria, pneumonia, tetanus'))
d.basic('How has biology helped control infectious diseases? (Exercise 2)', T('Vaccines') + ', immunisation programmes, ' + T('antibiotics') + ' and drugs, vector control, understanding of pathogens')

# ---------------------------------------------------------------- 7.2 Immunity
d.sec('7.2-immunity')
d.basic('Define immunity.', 'Overall ability of the host to fight disease-causing organisms, conferred by the ' + T('immune system'))
d.sec('7.2.1-innate')
d.basic('What is innate immunity?', T('Non-specific') + ' defence present ' + T('at birth') + '; barriers to entry of foreign agents')
table_card(d, 'Innate immunity', 'Examples?', [
    ('Physical barriers', 'Skin; mucus of respiratory, GI, urogenital tracts', False),
    ('Physiological barriers', 'Stomach acid, saliva, tears', False),
    ('Cellular barriers', 'PMNL-neutrophils, monocytes, NK cells, macrophages', False),
    ('Cytokine barriers', 'Interferons from virus-infected cells', False)], term='Four barriers of innate immunity')
d.basic('Function of interferons?', 'Secreted by ' + T('virus-infected cells') + '; protect non-infected cells from further viral infection')
d.basic('Mnemonic for innate barriers?', '"' + T('Please Put Cats Carefully') + '": Physical, Physiological, Cellular, Cytokine')
d.sec('7.2.2-acquired')
d.basic('Two features of acquired immunity?', T('Pathogen-specific') + ' and has ' + T('memory'))
d.basic('Primary vs secondary response?', T('Primary') + ': first encounter, low intensity. ' + T('Secondary (anamnestic)') + ': later encounter, highly intensified.')
d.basic('Cells carrying out acquired immune responses?', T('B-lymphocytes') + ' and ' + T('T-lymphocytes'))
d.basic('Role of B cells vs T cells?', T('B cells') + ' produce antibodies. ' + T('T cells') + ' do ' + X('not') + ' secrete antibodies but help B cells, and mediate CMI.')
d.basic('Structure of an antibody?', N('Four') + ' peptide chains: two light, two heavy; ' + T('H₂L₂'))
d.occlusion('Figure 7.4 · Antibody molecule', M + 'fig_7_4_antibody.webp', AB, [
    ('Antigen binding site', wbox(54, 78, 356, 106, AB), True), ('Antigen binding site', wbox(618, 70, 918, 100, AB), True),
    ('Light chain', wbox(110, 368, 198, 434, AB), True), ('Heavy chain', wbox(150, 566, 340, 600, AB), True)])
d.basic('Types of antibodies named in NCERT?', T('IgA, IgM, IgE, IgG'))
d.basic('Why is antibody response called humoral?', 'Antibodies are found in the ' + T('blood') + ' (body fluid)')
d.basic('Two types of acquired immune response?', T('Humoral') + ' (antibody-mediated, B cells) and ' + T('cell-mediated (CMI)') + ' (T cells)')
d.basic('What causes graft rejection?', T('Cell-mediated immune response') + ': body differentiates self from non-self')
d.basic('What is checked before a transplant, and after?', T('Tissue matching') + ' and ' + T('blood group matching') + '; patient takes ' + T('immunosuppressants') + ' lifelong')
d.sec('7.2.3-active-passive')
d.basic('What is active immunity?', 'Host produces its own antibodies on exposure to antigens; ' + T('slow') + ', takes time for full effect')
d.basic('Examples of active immunity?', T('Immunisation') + ' (vaccine) and ' + T('natural infection'))
d.basic('What is passive immunity?', T('Ready-made antibodies') + ' are given directly')
d.basic('Examples of passive immunity?', T('Colostrum') + ' (IgA), antibodies via ' + T('placenta') + ' to foetus, antitoxin, anti-venom')
d.basic('Why is colostrum essential for newborns?', 'Abundant ' + T('IgA') + ' antibodies protect the infant')
d.basic('Active vs passive (Exercise 8b)?', T('Active') + ': own antibodies, slow, long-lasting (vaccine). ' + T('Passive') + ': ready-made antibodies, fast, short-lived (colostrum, antivenom).')
d.basic('Innate vs acquired (Exercise 8a)?', T('Innate') + ': non-specific, from birth (skin, tears). ' + T('Acquired') + ': specific, with memory (antibodies, CMI).')
d.sec('7.2.4-vaccination')
d.basic('Principle of vaccination?', 'The ' + T('memory') + ' of the immune system')
d.basic('What does a vaccine contain?', 'Antigenic proteins of the pathogen or ' + T('inactivated/weakened') + ' pathogen')
d.basic('How does a vaccine protect?', 'Generates antibodies and ' + T('memory B and T cells') + ' that respond quickly and massively on later exposure')
d.basic('When is passive immunisation used? Examples?', 'When a quick response is needed: ' + T('tetanus') + ' antitoxin, ' + T('snakebite') + ' antivenom')
d.basic('What is an antitoxin?', 'A preparation containing ' + T('antibodies to the toxin'))
d.basic('Advantage of recombinant vaccines? Example?', 'Large-scale production, greater availability; e.g. ' + E('hepatitis B vaccine from yeast'))
d.basic('Why does a booster dose help? (intuition)', 'Each exposure re-trains memory cells, making the ' + T('secondary response') + ' stronger and longer-lasting')
d.sec('7.2.5-allergies')
d.basic('What is allergy?', 'Exaggerated immune response to certain environmental antigens (' + T('allergens') + ')')
d.basic('Antibody type in allergy?', T('IgE'))
d.basic('Common allergens?', 'Dust mites, pollen, animal dander')
d.basic('Symptoms of allergy?', 'Sneezing, watery eyes, running nose, difficulty in breathing')
d.basic('Chemicals released in allergy, and from which cells?', T('Histamine and serotonin') + ' from ' + T('mast cells'))
d.basic('How is the cause of allergy found?', 'Exposing/injecting very small doses of possible allergens and studying reactions')
d.basic('Drugs that reduce allergy symptoms?', T('Anti-histamine, adrenalin, steroids'))
d.basic('Why more allergies in metro children?', 'Protected environment early in life → lowered immunity and higher sensitivity')
d.sec('7.2.6-autoimmunity')
d.basic('What is autoimmune disease?', 'Body attacks ' + T('self-cells') + ' due to genetic and unknown reasons')
d.basic('Example of autoimmune disease?', T('Rheumatoid arthritis'))
d.sec('7.2.7-immune-system')
d.basic('Components of the immune system?', 'Lymphoid organs, tissues, cells and soluble molecules (antibodies)')
d.basic('Primary lymphoid organs?', T('Bone marrow and thymus') + ': immature lymphocytes become antigen-sensitive')
d.basic('Secondary lymphoid organs?', T('Spleen, lymph nodes, tonsils, Peyer’s patches, appendix') + ': lymphocytes meet antigens and become effector cells')
d.basic('Role of bone marrow?', 'Main lymphoid organ where ' + T('all blood cells') + ' including lymphocytes are produced')
d.basic('Location and change of the thymus?', 'Near the heart, beneath the breastbone; large at birth, ' + T('shrinks') + ' to very small by puberty', **fig('fig_7_5_lymph_nodes'))
d.basic('Where do T-lymphocytes develop and mature?', 'Bone marrow and ' + T('thymus'))
d.basic('Functions of the spleen?', 'Bean-shaped; lymphocytes and phagocytes; ' + T('filters blood') + ' trapping microbes; reservoir of ' + T('erythrocytes'))
d.basic('Function of lymph nodes?', T('Trap') + ' microbes/antigens in lymph and tissue fluid; activate lymphocytes')
d.basic('What is MALT?', T('Mucosa-associated lymphoid tissue') + ' in lining of respiratory, digestive, urogenital tracts; ~' + N('50%') + ' of lymphoid tissue')
table_card(d, 'Exercise 7', 'Full form?', [
    ('MALT', 'Mucosa-associated lymphoid tissue', False), ('CMI', 'Cell-mediated immunity', False),
    ('AIDS', 'Acquired Immuno Deficiency Syndrome', False), ('NACO', 'National AIDS Control Organisation', False),
    ('HIV', 'Human Immuno deficiency Virus', False)], term='Abbreviations (Exercise 7)')

# ---------------------------------------------------------------- 7.3 AIDS
d.sec('7.3-aids')
d.basic('Meaning of "acquired" and "syndrome" in AIDS?', T('Acquired') + ': during lifetime, not congenital. ' + T('Syndrome') + ': a group of symptoms.')
d.basic('When was AIDS first reported?', N('1981'))
d.basic('Update: NCERT says AIDS killed "more than 25 million". Current figure?', 'About ' + N('42 million') + ' deaths worldwide since the epidemic began (UNAIDS)')
d.basic('What type of virus is HIV?', 'A ' + T('retrovirus') + ': envelope enclosing an ' + T('RNA genome'), **fig('fig_7_6_retrovirus'))
d.basic('Routes of HIV transmission (Exercise 10)?', 'Sexual contact; transfusion of contaminated blood; ' + T('sharing needles') + '; infected mother to child through placenta')
d.basic('High-risk groups for HIV?', 'Multiple sexual partners, IV drug users, those needing repeated transfusions, children of infected mothers')
d.basic('Does HIV spread by touch?', X('No') + '; only through ' + T('body fluids') + '; infected persons should not be isolated')
d.basic('Time lag from HIV infection to AIDS?', 'Few months to many years, usually ' + N('5–10 years'))
d.basic('First cell HIV enters, and what happens?', T('Macrophages') + ': RNA → viral DNA by ' + T('reverse transcriptase') + ', integrates into host DNA; macrophage becomes an ' + T('HIV factory'))
d.basic('How does HIV cause immune deficiency? (Exercise 11)', 'It infects and destroys ' + T('helper T-lymphocytes (T_H)') + ' progressively; their number falls')
d.basic('Symptoms as T_H cells decline?', 'Bouts of fever, diarrhoea, weight loss; ' + T('opportunistic infections') + ' (Mycobacterium, viruses, fungi, Toxoplasma)')
d.basic('Diagnostic test for AIDS?', T('ELISA') + ' (enzyme linked immuno-sorbent assay)')
d.basic('Treatment of AIDS (NCERT)?', T('Anti-retroviral drugs') + ': only partially effective; prolong life')
d.basic('Update: NCERT says death is inevitable with AIDS. Today?', 'With early, lifelong ' + T('antiretroviral therapy') + ', people with HIV can reach near-normal life expectancy; undetectable viral load means no sexual transmission')
d.basic('Indian body educating about AIDS?', T('NACO') + ' (National AIDS Control Organisation) and NGOs')
d.basic('Steps to prevent spread of HIV?', 'Safe blood from banks, ' + T('disposable needles') + ', free condoms, controlling drug abuse, safe sex, regular check-ups')
d.basic('Slogan about AIDS awareness?', '"' + T('Don’t die of ignorance') + '"')

# ---------------------------------------------------------------- 7.4 Cancer
d.sec('7.4-cancer')
d.basic('What is contact inhibition?', 'Contact with other cells ' + T('inhibits uncontrolled growth') + '; cancer cells have lost it')
d.basic('How is a cancer cell different from a normal cell? (Exercise 12)', 'Lost ' + T('contact inhibition') + ' and growth regulation; divides uncontrollably forming tumours; may invade and metastasise')
d.basic('Benign vs malignant tumours?', T('Benign') + ': confined, little damage. ' + T('Malignant') + ': neoplastic cells grow rapidly, invade tissues, starve normal cells, metastasise.')
d.basic('What is metastasis? (Exercise 13)', 'Cells sloughed from a malignant tumour reach ' + T('distant sites via blood') + ' and start new tumours; most feared property')
d.basic('What are carcinogens?', 'Physical, chemical or biological agents that cause ' + T('neoplastic transformation'))
d.basic('Radiation carcinogens?', 'Ionising: ' + T('X-rays, gamma rays') + '. Non-ionising: ' + T('UV') + '. Both damage DNA.')
d.basic('Major cause of lung cancer?', 'Chemical carcinogens in ' + T('tobacco smoke'))
d.basic('Viral oncogenes vs proto-oncogenes?', T('Viral oncogenes') + ': genes of oncogenic viruses. ' + T('Cellular oncogenes (c-onc)/proto-oncogenes') + ': normal cell genes that cause cancer when activated.')
d.basic('Basis of cancer detection?', T('Biopsy') + ' and histopathology; blood and bone marrow tests for leukaemias')
d.basic('What is a biopsy?', 'Suspected tissue cut into thin sections, stained and examined under a microscope by a pathologist')
table_card(d, 'Cancer imaging', 'Uses?', [
    ('Radiography', 'X-rays', False), ('CT', 'X-rays to build a 3D image', False),
    ('MRI', 'Strong magnetic fields and non-ionising radiation', False)], term='Imaging techniques for cancer')
d.basic('Other detection methods?', T('Antibodies') + ' against cancer-specific antigens; molecular detection of genes for inherited susceptibility')
d.basic('Common cancer treatments?', T('Surgery, radiation therapy, chemotherapy') + ' and ' + T('immunotherapy'))
d.basic('Side effects of chemotherapy drugs?', T('Hair loss, anaemia'))
d.basic('What are biological response modifiers? Example?', 'Substances that activate the immune system against tumours; e.g. ' + T('α-interferon'))
d.basic('Why is immunotherapy needed? (intuition)', 'Tumour cells ' + T('evade') + ' immune detection; immunotherapy "wakes up" the immune system')

# ---------------------------------------------------------------- 7.5 Drugs
d.sec('7.5-drugs-and-alcohol')
d.basic('Commonly abused drug groups?', T('Opioids, cannabinoids, coca alkaloids') + ' (mostly from flowering plants, some from fungi)')
d.basic('Where do opioids act?', 'Bind to specific ' + T('opioid receptors') + ' in the ' + T('CNS and GI tract'))
d.basic('What is heroin chemically, and its common name?', T('Diacetylmorphine') + '; "smack": white, odourless, bitter crystals', **fig('fig_7_7_morphine'))
d.basic('How is heroin obtained?', 'By ' + T('acetylation of morphine') + ', from latex of poppy ' + EI('Papaver somniferum'), **fig('fig_7_8_opium_poppy'))
d.basic('How is heroin taken, and effect?', 'Snorting and injection; a ' + T('depressant') + ', slows body functions')
d.basic('Where do cannabinoids act?', T('Cannabinoid receptors') + ', mainly in the brain', **fig('fig_7_9_cannabinoid'))
d.basic('Source of natural cannabinoids and products?', 'Inflorescences of ' + EI('Cannabis sativa') + ' → marijuana, hashish, charas, ganja', **fig('fig_7_10_cannabis'))
d.basic('How are cannabinoids taken, and their effect?', 'Inhalation and oral ingestion; affect the ' + T('cardiovascular system'))
d.basic('Source of cocaine?', EI('Erythroxylum coca') + ', native to South America')
d.basic('How does cocaine act?', 'Interferes with transport of ' + T('dopamine') + '; potent CNS ' + T('stimulant') + ' (euphoria, energy); excess → hallucinations')
d.basic('Street names of cocaine?', T('Coke') + ' or ' + T('crack') + '; usually snorted')
d.basic('Other hallucinogenic plants?', EI('Atropa belladonna') + ' and ' + EI('Datura'), **fig('fig_7_11_datura'))
d.basic('Medicines often abused?', T('Barbiturates, amphetamines, benzodiazepines') + ' (used for depression, insomnia)')
d.basic('Legitimate use of morphine?', 'Very effective ' + T('sedative and painkiller') + ' after surgery')
d.basic('When does drug use become abuse?', 'Taken for non-medicinal purposes or in amounts/frequency that ' + T('impair') + ' physical, physiological or psychological functions')
table_card(d, 'Drugs', 'Source / action?', [
    ('Heroin (smack)', 'Papaver somniferum; depressant', False), ('Cannabinoids (charas, ganja)', 'Cannabis sativa; cardiovascular effects', False),
    ('Cocaine (coke, crack)', 'Erythroxylum coca; stimulant, blocks dopamine transport', False)], term='Commonly abused drugs')
d.basic('How long has tobacco been used?', 'More than ' + N('400 years') + '; smoked, chewed or as snuff')
d.basic('Effect of nicotine?', 'Stimulates ' + T('adrenal gland') + ' to release adrenaline and noradrenaline → raises BP and heart rate')
d.basic('Diseases associated with smoking?', 'Cancers of lung, urinary bladder, throat; bronchitis, emphysema, coronary heart disease, gastric ulcer')
d.basic('Risk of tobacco chewing?', T('Oral cavity cancer'))
d.basic('Why does smoking cause oxygen deficiency?', 'Increases ' + T('CO') + ' in blood, reducing haem-bound oxygen')

d.sec('7.5.1-adolescence')
d.basic('Adolescence age range?', N('12–18 years') + ': both a period and a process; bridge between childhood and adulthood')
d.basic('Causes of drug/alcohol use in youth (Exercise 17)?', 'Curiosity, adventure, experimentation, escape from problems, ' + T('academic stress') + ', "cool" image (media), unstable families, ' + T('peer pressure'))
d.sec('7.5.2-addiction-dependence')
d.basic('What is addiction?', 'Psychological attachment to effects like ' + T('euphoria') + ' and temporary well-being')
d.basic('Why does addiction escalate? (Exercise 16)', 'Tolerance of ' + T('receptors') + ' increases, so they respond only to higher doses')
d.basic('Can a single use lead to addiction?', T('Yes') + '; even once can be a forerunner')
d.basic('What is dependence?', 'Body shows a ' + T('withdrawal syndrome') + ' (anxiety, shakiness, nausea, sweating) if regular dose stops abruptly')
d.sec('7.5.3-effects')
d.basic('Immediate effects of drug/alcohol abuse?', 'Reckless behaviour, vandalism, violence; overdose → coma, death from respiratory/heart failure, cerebral haemorrhage')
d.basic('Warning signs of drug abuse in youth?', 'Drop in academics, absence, poor hygiene, withdrawal, depression, aggression, changed sleep/eating, weight fluctuations')
d.basic('Infections risked by IV drug users?', T('AIDS and hepatitis B') + ' (sharing needles)')
d.basic('Long-term damage from alcohol?', 'Nervous system and ' + T('liver (cirrhosis)') + '; harms foetus in pregnancy')
d.basic('Drugs misused by sportspersons?', 'Narcotic analgesics, ' + T('anabolic steroids') + ', diuretics, certain hormones')
d.basic('Anabolic steroid effects in females?', T('Masculinisation') + ', aggressiveness, mood swings, abnormal cycles, facial hair, enlarged clitoris, deep voice')
d.basic('Anabolic steroid effects in males?', 'Acne, aggressiveness, ' + T('smaller testicles') + ', less sperm, kidney/liver dysfunction, breast enlargement, baldness, enlarged prostate')
d.basic('Steroid effect in adolescents?', 'Severe acne and ' + T('premature closure of growth centres') + ' of long bones → stunted growth')
d.sec('7.5.4-prevention')
d.cloze('Prevention of drug abuse: avoid undue {{c1::peer pressure}}; {{c2::education and counselling}}; seek help from {{c3::parents and peers}}; look for {{c4::danger signs}}; seek {{c5::professional and medical help}}.')
d.basic('Parenting linked to lower substance abuse?', 'High ' + T('nurturance') + ' with consistent ' + T('discipline'))
d.basic('Can friends influence drug use? Protection? (Exercise 15)', 'Yes, via peer pressure. Say no firmly, choose friends wisely, seek help from parents/teachers, channel energy into sports, music, yoga')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Disease groups', 'Pathogen type?', [
    ('Typhoid, pneumonia', 'Bacteria', False), ('Common cold', 'Virus', False), ('Malaria, amoebiasis', 'Protozoa', False),
    ('Ascariasis, filariasis', 'Helminths', False), ('Ringworm', 'Fungi', False)], term='Diseases by pathogen type')
table_card(d, 'Exercise 6', 'Primary or secondary?', [
    ('Bone marrow, thymus', 'Primary lymphoid organs', False),
    ('Spleen, lymph nodes, tonsils, Peyer’s patches, appendix', 'Secondary lymphoid organs', False)], term='Lymphoid organs (Exercise 6)')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
