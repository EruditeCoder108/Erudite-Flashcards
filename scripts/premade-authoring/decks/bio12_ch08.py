import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch08-microbes-in-human-welfare')
d = Deck('Chapter 8: Microbes in Human Welfare', 'Class 12', ['class-12', 'biology', 'ch-8'])
d.description = 'Microbes in household foods, industrial products, antibiotics, sewage treatment, biogas, biocontrol and biofertilisers'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
BG = (1001, 880)

# ---------------------------------------------------------------- intro
d.sec('8.0-intro')
d.basic('Where are microbes found?', 'Everywhere: soil, water, air, inside bodies; even in ' + T('thermal vents (~100 °C)') + ', deep soil, under snow, highly acidic places')
d.basic('Types of microbes?', 'Protozoa, bacteria, fungi, microscopic plant and animal viruses, ' + T('viroids') + ' and ' + T('prions'))
d.basic('What are prions?', T('Proteinaceous infectious agents'))
d.basic('Identify the bacterial shapes in Figure 8.1.', '(a) Rod-shaped, (b) spherical (both ×1500), (c) rod-shaped with ' + T('flagella') + ' (×50,000)', **img('fig_8_1_bacteria'))
d.basic('Identify the viruses in Figure 8.2.', '(a) ' + T('Bacteriophage') + ', (b) ' + T('Adenovirus') + ' (respiratory infections), (c) rod-shaped ' + T('TMV'), **img('fig_8_2_viruses'))
d.basic('How can bacteria and fungi be seen with the naked eye?', 'Grown on nutritive media as ' + T('colonies'), **fig('fig_8_3_colonies'))
d.basic('Correction: NCERT prints the vent temperature as "1000C". Correct?', N('100 °C') + ' (degree sign lost in printing)')

# ---------------------------------------------------------------- 8.1 Household
d.sec('8.1-household-products')
d.basic('Microbes that convert milk to curd?', EI('Lactobacillus') + ' and others: ' + T('lactic acid bacteria (LAB)'))
d.basic('How does LAB make curd?', 'Produces ' + T('acids') + ' that coagulate and partially digest milk proteins')
d.basic('What is the "starter" in curd making?', 'A small amount of curd containing millions of LAB, used as ' + T('inoculum'))
d.basic('Nutritional benefit of curd over milk?', 'Increased ' + T('vitamin B₁₂'))
d.basic('Role of LAB in our stomach?', 'Checks ' + T('disease-causing microbes'))
d.basic('Why does idli/dosa dough puff up?', 'Bacterial fermentation produces ' + T('CO₂'))
d.basic('Microbe for bread dough?', T('Baker’s yeast') + ', ' + EI('Saccharomyces cerevisiae'))
d.basic('What is toddy?', 'Traditional drink of southern India made by fermenting ' + T('palm sap'))
d.basic('Foods made by microbial fermentation (besides curd, bread)?', 'Fermented ' + E('fish, soyabean, bamboo-shoots') + '; cheese')
d.basic('What makes the large holes in Swiss cheese?', 'CO₂ from the bacterium ' + EI('Propionibacterium sharmanii'))
d.basic('How is Roquefort cheese ripened?', 'By growing a specific ' + T('fungus') + ' on it for flavour')
d.basic('Traditional Indian foods from microbes (Exercise 4)?', 'Wheat: ' + E('bread, bhatura') + '. Rice: ' + E('idli, dosa') + '. Bengal gram: ' + E('dhokla, khaman') + '.')
d.basic('Sample to show microbes under a microscope (Exercise 1)?', T('Curd') + ': full of LAB, easy to carry and observe')

# ---------------------------------------------------------------- 8.2 Industrial
d.sec('8.2-industrial-products')
d.basic('Vessels for industrial-scale microbe growth?', T('Fermentors'), **fig('fig_8_4_fermentors'))
d.sec('8.2.1-fermented-beverages')
d.basic('Yeast used for beverages?', EI('Saccharomyces cerevisiae') + ' (' + T('brewer’s yeast') + ')')
d.basic('What does brewer’s yeast ferment, and product?', 'Malted cereals and fruit juices → ' + T('ethanol'))
d.basic('Beverages made without vs with distillation?', T('Without') + ': wine, beer. ' + T('With') + ': whisky, brandy, rum.', **fig('fig_8_5_fermentation_plant'))
d.basic('Mnemonic for distilled drinks?', '"' + T('Wise Boys Run') + '" (Whisky, Brandy, Rum) to the still')
d.sec('8.2.2-antibiotics')
d.basic('Meaning of "antibiotic"?', '"Against life" (of pathogens); ' + T('pro-life') + ' for humans')
d.basic('Define antibiotics.', 'Chemicals produced by some microbes that ' + T('kill or retard') + ' growth of other (disease-causing) microbes')
d.basic('First antibiotic, and who discovered it?', T('Penicillin') + ', ' + T('Alexander Fleming') + ' (chance discovery)')
d.basic('How was penicillin discovered?', 'A mould in an unwashed ' + EI('Staphylococci') + ' plate prevented bacterial growth around it')
d.basic('Source of penicillin?', EI('Penicillium notatum'))
d.basic('Who established penicillin’s full potential?', T('Ernest Chain and Howard Florey'))
d.basic('Nobel Prize for penicillin?', N('1945') + ': Fleming, Chain and Florey; used to treat soldiers in World War II')
d.basic('Diseases controlled by antibiotics?', 'Plague, whooping cough (' + E('kali khansi') + '), diphtheria (' + E('gal ghotu') + '), leprosy (' + E('kusht rog') + ')')
d.basic('Two fungi producing antibiotics (Exercise 6)?', EI('Penicillium notatum') + ' (penicillin) and ' + EI('Cephalosporium') + ' (cephalosporin)')
d.basic('Why is overuse of antibiotics dangerous? (intuition)', 'It ' + T('selects resistant bacteria') + ' (evolution in action), making antibiotics useless')
d.sec('8.2.3-chemicals-enzymes')
table_card(d, 'Microbial acids', 'Producer?', [
    ('Citric acid', 'Aspergillus niger (fungus)', False), ('Acetic acid', 'Acetobacter aceti (bacterium)', False),
    ('Butyric acid', 'Clostridium butylicum (bacterium)', False), ('Lactic acid', 'Lactobacillus (bacterium)', False)],
    term='Microbes producing organic acids')
d.basic('Microbe for commercial ethanol?', EI('Saccharomyces cerevisiae'))
d.basic('Use of lipases?', 'In ' + T('detergents') + ': remove oily stains')
d.basic('Why are bottled juices clearer than homemade?', 'Clarified by ' + T('pectinases and proteases'))
d.basic('What is streptokinase and its use?', 'From ' + EI('Streptococcus') + ', modified by genetic engineering; ' + T('clot buster') + ' for myocardial infarction patients')
d.basic('Cyclosporin A: source and use?', 'Fungus ' + EI('Trichoderma polysporum') + '; ' + T('immunosuppressant') + ' in organ transplants')
d.basic('Statins: source and use?', 'Yeast ' + EI('Monascus purpureus') + '; lower ' + T('blood cholesterol') + ' by competitively inhibiting its synthesis enzyme')
table_card(d, 'Bioactive molecules', 'Source?', [
    ('Streptokinase', 'Streptococcus', False), ('Cyclosporin A', 'Trichoderma polysporum', False),
    ('Statins', 'Monascus purpureus', False), ('Penicillin', 'Penicillium notatum', False)], term='Microbial bioactive molecules')
d.basic('Mnemonic: cyclosporin vs statins source?', T('T') + 'ransplant drug from ' + T('T') + 'richoderma; cholesterol drug from ' + T('M') + 'onascus (' + T('M') + 'ind your heart)')

# ---------------------------------------------------------------- 8.3 Sewage
d.sec('8.3-sewage-treatment')
d.basic('What is sewage?', 'Municipal ' + T('waste water') + ', largely human excreta; rich in organic matter and microbes (many pathogenic)')
d.basic('Why can’t sewage go directly into rivers? (Exercise 7)', 'It is pathogenic and rich in organic matter: pollutes water, depletes O₂, spreads ' + X('water-borne diseases'))
d.basic('Who treats sewage in STPs?', T('Heterotrophic microbes') + ' naturally present in sewage')
d.basic('What is primary treatment?', T('Physical removal') + ' of particles by filtration and sedimentation')
d.basic('Steps of primary treatment?', 'Floating debris removed by sequential ' + T('filtration') + '; grit removed by ' + T('sedimentation') + ' → primary sludge + effluent')
d.basic('What is secondary (biological) treatment?', 'Primary effluent is agitated and aerated in ' + T('aeration tanks') + ', growing aerobic microbes into flocs', **fig('fig_8_6_secondary_treatment'))
d.basic('What are flocs?', 'Masses of ' + T('bacteria with fungal filaments') + ' forming mesh-like structures')
d.basic('Key difference: primary vs secondary treatment (Exercise 8)?', T('Primary') + ': physical. ' + T('Secondary') + ': biological (microbes consume organic matter).')
d.basic('Define BOD.', 'Amount of O₂ consumed if all organic matter in ' + N('one litre') + ' of water were oxidised by bacteria')
d.basic('What does BOD indicate?', 'Indirect measure of ' + T('organic matter') + '; higher BOD = more polluting potential')
d.basic('What is activated sludge?', 'Sediment of bacterial ' + T('flocs') + ' in the settling tank after BOD is reduced')
d.basic('Fate of activated sludge?', 'Small part → back to aeration tank as ' + T('inoculum') + '; major part → ' + T('anaerobic sludge digesters'))
d.basic('What happens in anaerobic sludge digesters?', 'Anaerobic bacteria digest bacteria and fungi, producing ' + T('biogas') + ' (methane, H₂S, CO₂)')
d.basic('Fate of secondary effluent?', 'Released into ' + T('rivers and streams'))
d.basic('Aerial view of an STP (Figure 8.7): circular tanks are?', 'Settling/aeration tanks of a sewage treatment plant', **img('fig_8_7_sewage_plant'))
d.cloze('Sewage treatment flow: {{c1::primary treatment (filtration, sedimentation)}} → {{c2::aeration tank (flocs)}} → {{c3::settling tank (activated sludge)}} → {{c4::anaerobic sludge digester (biogas)}}.')
steps_card(d, 'Exercise 11', 'BOD: A = 20, B = 8, C = 400 mg/L. Identify samples.', 'River water is relatively clean.',
           ['Highest BOD = most polluted', 'C (400) = untreated sewage', 'A (20) = secondary effluent', 'B (8) = <b>river water</b>'], 3, 'BOD identification (Exercise 11)', 'C sewage, A secondary effluent, B river water')
d.basic('Plans to save Indian rivers from sewage?', T('Ganga Action Plan') + ' and ' + T('Yamuna Action Plan') + ' (Ministry of Environment and Forests)')
d.basic('Why is untreated sewage still discharged?', 'Sewage production rose with urbanisation but ' + X('STPs did not increase') + ' enough')

# ---------------------------------------------------------------- 8.4 Biogas
d.sec('8.4-biogas')
d.basic('What is biogas?', 'Mixture of gases, predominantly ' + T('methane') + ', produced by microbes; used as fuel')
d.basic('What are methanogens? Example?', 'Anaerobic bacteria producing methane (with CO₂, H₂) from cellulosic material; ' + EI('Methanobacterium'))
d.basic('Where are methanogens found?', 'Anaerobic sludge of sewage and the ' + T('rumen') + ' of cattle')
d.basic('Role of methanogens in cattle?', 'Help break down ' + T('cellulose') + '; important for cattle nutrition')
d.basic('Why is gobar good for biogas?', 'Cattle dung is rich in ' + T('methanogens'))
d.basic('Structure of a biogas plant?', 'Concrete tank ' + N('10–15 ft') + ' deep with dung slurry; floating cover rises as gas forms; gas outlet pipe; spent slurry outlet (used as fertiliser)')
d.occlusion('Figure 8.8 · Biogas plant', M + 'fig_8_8_biogas_plant.webp', BG, [
    ('Gas', wbox(905, 40, 990, 72, BG), True), ('Gas-holder', wbox(640, 250, 814, 284, BG), True),
    ('Dung', wbox(60, 338, 150, 370, BG), True), ('Water', wbox(170, 338, 264, 370, BG), True),
    ('Sludge', wbox(740, 340, 846, 372, BG), True), ('Digester', wbox(650, 724, 782, 758, BG), True)])
d.basic('Why are biogas plants mostly rural?', 'Cattle dung is plentiful there')
d.basic('Uses of biogas?', T('Cooking and lighting'))
d.basic('Who developed biogas technology in India?', T('IARI') + ' and ' + T('KVIC') + ' (Khadi and Village Industries Commission)')
d.basic('Can microbes be a source of energy? (Exercise 9)', T('Yes') + ': methanogens produce biogas (methane) from dung and waste; yeast makes ethanol')
d.basic('Gases released by microbes (Exercise 2)?', 'CO₂ in dough, Swiss cheese; methane, CO₂, H₂S in biogas')

# ---------------------------------------------------------------- 8.5 Biocontrol
d.sec('8.5-biocontrol')
d.basic('Define biocontrol.', 'Use of ' + T('biological methods') + ' to control plant diseases and pests')
d.basic('Problems with chemical pesticides?', 'Toxic to humans and animals; pollute soil, groundwater, fruits, vegetables, crops')
d.basic('Organic farmer’s view on pests?', 'Keep pests at ' + T('manageable levels') + ', not eradicated; eradication is undesirable as predators depend on them')
d.basic('Key belief of organic farming?', T('Biodiversity furthers health'))
d.basic('Ladybird and dragonflies control?', 'Ladybird: ' + T('aphids') + '. Dragonflies: ' + T('mosquitoes') + '.')
d.basic('Microbial biocontrol of butterfly caterpillars?', EI('Bacillus thuringiensis') + ' (Bt)')
d.basic('How is Bt applied and how does it act?', 'Dried spores mixed with water, sprayed on plants; eaten by larvae; ' + T('toxin') + ' released in the gut kills them; other insects unharmed')
d.basic('Example of Bt toxin genes in crops?', T('Bt-cotton'))
d.basic('Fungal biocontrol agent of plant diseases?', EI('Trichoderma') + ': free-living in root ecosystems')
d.basic('What are baculoviruses?', 'Pathogens of insects and arthropods; used as biocontrol agents')
d.basic('Genus of most biocontrol baculoviruses?', EI('Nucleopolyhedrovirus'))
d.basic('Why are baculoviruses good biocontrol agents?', T('Species-specific, narrow spectrum') + '; no harm to plants, mammals, birds, fish or non-target insects')
d.basic('What is IPM?', T('Integrated pest management') + ': conserves beneficial insects; baculoviruses suit it')
d.basic('Mnemonic for microbial biocontrol agents?', '"' + T('Bt Treats Bugs') + '": Bacillus thuringiensis, Trichoderma, Baculovirus')

# ---------------------------------------------------------------- 8.6 Biofertilisers
d.sec('8.6-biofertilisers')
d.basic('What are biofertilisers?', 'Organisms that ' + T('enrich the nutrient quality') + ' of soil')
d.basic('Main sources of biofertilisers?', T('Bacteria, fungi, cyanobacteria'))
d.basic('Symbiotic N₂-fixer in legumes?', EI('Rhizobium') + ' in root nodules')
d.basic('Free-living N₂-fixing bacteria in soil?', EI('Azospirillum') + ' and ' + EI('Azotobacter'))
d.basic('Genus forming mycorrhiza?', EI('Glomus'))
d.basic('Benefit of mycorrhiza to plants?', 'Fungus absorbs ' + T('phosphorus') + ' for the plant; resistance to root pathogens; tolerance to salinity and drought; better growth')
d.basic('What does the fungus gain from mycorrhiza? (think)', T('Food (sugars)') + ' and shelter from the plant root')
d.basic('N₂-fixing cyanobacteria?', EI('Anabaena, Nostoc, Oscillatoria'))
d.basic('Where are cyanobacteria important biofertilisers?', T('Paddy fields'))
d.basic('Extra benefit of blue-green algae?', 'Add ' + T('organic matter') + ' to soil, increasing fertility')
d.basic('How do microbes reduce chemical fertilisers and pesticides? (Exercise 10)', T('Biofertilisers') + ' fix N and supply P; ' + T('biocontrol agents') + ' (Bt, Trichoderma, baculovirus) kill pests')
table_card(d, 'Biofertilisers', 'Type?', [
    ('Rhizobium', 'Symbiotic N₂-fixing bacterium', False), ('Azotobacter, Azospirillum', 'Free-living N₂-fixing bacteria', False),
    ('Glomus', 'Mycorrhizal fungus (P uptake)', False), ('Anabaena, Nostoc, Oscillatoria', 'N₂-fixing cyanobacteria', False)],
    term='Types of biofertilisers')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Microbes and products', 'Product?', [
    ('Lactobacillus', 'Curd, lactic acid', False), ('Saccharomyces cerevisiae', 'Bread, beverages, ethanol', False),
    ('Propionibacterium sharmanii', 'Swiss cheese', False), ('Aspergillus niger', 'Citric acid', False),
    ('Methanobacterium', 'Biogas', False), ('Bacillus thuringiensis', 'Bt toxin (biocontrol)', False)], term='Microbes in human welfare')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
