import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch13-biodiversity-and-conservation')
d = Deck('Chapter 13: Biodiversity and Conservation', 'Class 12', ['class-12', 'biology', 'ch-13'])
d.description = 'Levels and numbers of biodiversity, latitudinal and species-area patterns, rivet popper, loss and evil quartet, in situ and ex situ conservation'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
GB = (1001, 956)

# ---------------------------------------------------------------- intro
d.sec('13.0-intro')
table_card(d, 'Species counts', 'How many species?', [
    ('Ants', '> 20,000', False), ('Beetles', '3,00,000', False), ('Fishes', '28,000', False), ('Orchids', 'nearly 20,000', False)],
    term='Astonishing species numbers')

# ---------------------------------------------------------------- 13.1 Biodiversity
d.sec('13.1-biodiversity')
d.basic('Who popularised the term biodiversity?', 'Sociobiologist ' + T('Edward Wilson'))
d.basic('Define biodiversity.', 'Combined diversity at ' + T('all levels of biological organisation') + ', macromolecules to biomes')
d.cloze('Three important levels of biodiversity: {{c1::genetic}}, {{c2::species}} and {{c3::ecological}} diversity.')
d.basic('Example of genetic diversity in a medicinal plant?', EI('Rauwolfia vomitoria') + ' in different Himalayan ranges varies in potency and concentration of ' + T('reserpine'))
d.basic('Genetic diversity in Indian rice and mango?', 'More than ' + N('50,000') + ' rice strains and ' + N('1,000') + ' mango varieties')
d.basic('Example of species diversity?', T('Western Ghats') + ' have greater amphibian diversity than the Eastern Ghats')
d.basic('Example of ecological diversity?', 'India (deserts, rain forests, mangroves, coral reefs, wetlands, estuaries, alpine meadows) > ' + T('Norway'))
d.basic('How fast could we lose biodiversity?', 'In less than ' + N('two centuries') + ' at present rates (it took millions of years to build)')

d.sec('13.1.1-how-many-species')
d.basic('Species described so far (IUCN 2004)?', 'Slightly more than ' + N('1.5 million'))
d.basic('How do ecologists estimate total species? (Exercise 2)', 'Compare ' + T('temperate–tropical species richness') + ' of a well-studied insect group,<br>and extrapolate the ratio to other groups')
d.basic('Robert May’s estimate of global species?', 'About ' + N('7 million') + ' (extreme estimates: 20–50 million)')
d.basic('Share of animals and plants among recorded species?', T('Animals') + ' > ' + N('70%') + '; ' + T('plants') + ' (incl. algae, fungi, bryophytes, gymnosperms, angiosperms) ≤ ' + N('22%'))
d.basic('Most species-rich animal group?', T('Insects') + ': > 70% of animals (7 of every 10 animals)')
d.basic('Fungi vs vertebrates in species number?', 'Fungi species exceed the ' + T('combined total') + ' of fishes, amphibians, reptiles and mammals')
d.basic('Why are prokaryotes not counted?', 'Conventional taxonomy unsuitable; many are ' + X('not culturable') + '; by molecular criteria they may run into millions')
d.occlusion('Figure 13.1 · Global biodiversity by taxa', M + 'fig_13_1_global_biodiversity.webp', GB, [
    ('Other animal groups', wbox(70, 120, 344, 150, GB), True), ('Crustaceans', wbox(40, 168, 208, 196, GB), True),
    ('Molluscs', wbox(48, 226, 166, 256, GB), True), ('Insects', wbox(52, 334, 146, 364, GB), True),
    ('Fishes', wbox(558, 172, 644, 202, GB), True), ('Mammals', wbox(788, 144, 918, 174, GB), True),
    ('Birds', wbox(890, 224, 962, 254, GB), True), ('Reptiles', wbox(870, 388, 976, 418, GB), True),
    ('Amphibians', wbox(772, 456, 932, 486, GB), True), ('Mosses', wbox(408, 566, 504, 596, GB), True),
    ('Ferns and allies', wbox(522, 544, 658, 604, GB), True), ('Fungi', wbox(254, 730, 334, 762, GB), True),
    ('Angiosperms', wbox(648, 730, 820, 762, GB), True), ('Algae', wbox(398, 894, 472, 926, GB), True),
    ('Lichens', wbox(508, 894, 612, 926, GB), True)], guess='hide-one')
d.basic('Largest slice in the vertebrate pie?', T('Fishes'))
d.basic('Largest slices in the plant pie?', T('Angiosperms') + ' and ' + T('fungi'))
d.basic('India’s share of land vs species?', N('2.4%') + ' of land area but ' + N('8.1%') + ' of global species diversity')
d.basic('India’s status in biodiversity?', 'One of the ' + N('12') + ' ' + T('mega diversity') + ' countries')
d.basic('Species recorded from India?', 'Nearly ' + N('45,000') + ' plants and ' + T('twice as many') + ' animals')
d.basic('Undiscovered species estimated in India?', 'More than ' + N('1,00,000') + ' plants and ' + N('3,00,000') + ' animals (only 22% recorded, by May’s estimate)')
d.basic('"Nature’s biological library is burning" means?', 'Species are going ' + X('extinct') + ' before we even discover and catalogue them')
d.basic('Why do animals outnumber plants in species? (Exercise 9)', 'Mobility, varied niches and body plans, rapid breeding and huge insect radiation (flight, small size, metamorphosis)')

d.sec('13.1.2-patterns')
d.basic('What is the latitudinal gradient?', 'Species diversity ' + T('decreases') + ' from the equator towards the poles')
d.basic('Latitudinal range of the tropics?', N('23.5° N to 23.5° S'))
table_card(d, 'Bird species', 'How many?', [
    ('Colombia (near equator)', 'nearly 1,400', False), ('New York (41° N)', '105', False),
    ('Greenland (71° N)', '56', False), ('India', 'more than 1,200', False)], term='Latitudinal gradient in birds')
d.basic('Tropical vs temperate forest plant diversity?', 'Ecuador forest has up to ' + N('10 times') + ' vascular plant species of a same-size Midwest USA forest')
d.basic('Place with the greatest biodiversity on earth?', 'The ' + T('Amazonian rain forest'))
table_card(d, 'Amazon', 'How many species?', [
    ('Plants', '> 40,000', False), ('Fishes', '3,000', False), ('Birds', '1,300', False), ('Mammals', '427', False),
    ('Amphibians', '427', False), ('Reptiles', '378', False), ('Invertebrates', '> 1,25,000', False)], term='Amazon rain forest diversity')
d.basic('Three hypotheses for tropical richness (Exercise 3)?', '(a) More ' + T('evolutionary time') + ' (no glaciations); (b) ' + T('less seasonal') + ', constant environment → niche specialisation; (c) more ' + T('solar energy') + ' → higher productivity')
d.basic('Mnemonic for tropical richness?', '"' + T('Time, Tranquillity, Tan') + '": more time, stable climate, more sunshine')
d.basic('Who observed the species–area relationship?', T('Alexander von Humboldt') + ' in South American jungles')
d.basic('Shape of species–area curve?', T('Rectangular hyperbola') + '; a straight line on a log–log scale', **fig('fig_13_2_species_area'))
d.basic('Species–area equation?', '\\( \\log S = \\log C + Z \\log A \\) (i.e. \\( S = CA^Z \\))')
table_card(d, 'Species–area', 'Meaning?', [
    ('S', 'Species richness', False), ('A', 'Area', False), ('Z', 'Slope (regression coefficient)', False), ('C', 'Y-intercept', False)],
    term='Terms of the species–area equation')
d.basic('Usual range of Z?', N('0.1 to 0.2') + ', regardless of taxon or region')
d.basic('Z for very large areas like continents?', 'Much steeper: ' + N('0.6 to 1.2') + '; frugivorous birds and mammals of tropical forests ' + N('1.15'))
d.basic('Significance of a steeper slope (Exercise 4)?', 'Species richness rises ' + T('faster with area') + '; losing area loses species much faster')

d.sec('13.1.3-importance-of-diversity')
d.basic('Features of a stable community?', 'Little year-to-year variation in productivity; ' + T('resistant or resilient') + ' to disturbance; resistant to ' + T('alien invasions'))
d.basic('Tilman’s findings?', 'Plots with more species had ' + T('less year-to-year biomass variation') + ' and ' + T('higher productivity'))
d.basic('Rivet popper hypothesis: who and analogy?', T('Paul Ehrlich') + ': airplane = ecosystem; rivets = species')
d.basic('Lessons of the rivet popper hypothesis?', 'Losing a few rivets may not matter at first, but losing many weakens the plane.<br>Losing ' + T('key rivets on wings') + ' (key species) is most dangerous')
d.basic('How is biodiversity important for ecosystems (Exercise 6)?', 'More species → stability, productivity, resistance to invasion and disturbance, ecosystem services')

d.sec('13.1.4-loss-of-biodiversity')
d.basic('Birds lost by human colonisation of Pacific islands?', 'More than ' + N('2,000') + ' native bird species')
d.basic('IUCN Red List 2004 extinctions in last 500 years?', N('784') + ' species: ' + N('338') + ' vertebrates, ' + N('359') + ' invertebrates, ' + N('87') + ' plants')
table_card(d, 'Recent extinctions', 'Where?', [
    ('Dodo', 'Mauritius', False), ('Quagga', 'Africa', False), ('Thylacine', 'Australia', False),
    ('Steller’s sea cow', 'Russia', False), ('Tiger subspecies (Bali, Javan, Caspian)', 'Asia', False)], term='Examples of recent extinctions')
d.basic('Extinctions in the last twenty years (NCERT)?', N('27') + ' species')
d.basic('Group most vulnerable to extinction?', T('Amphibians'))
d.basic('Species threatened worldwide (NCERT)?', 'More than ' + N('15,500'))
table_card(d, 'Threatened', '% facing extinction?', [
    ('Birds', '12%', False), ('Mammals', '23%', False), ('Amphibians', '32%', False), ('Gymnosperms', '31%', False)],
    term='Threatened fractions of groups')
d.basic('Update: how many species are threatened today?', 'IUCN Red List now lists over ' + N('44,000') + ' threatened species (2024); NCERT’s 15,500 is from 2004')
d.basic('How many mass extinctions in earth’s history?', N('Five') + ' (over > 3 billion years)')
d.basic('How is the "Sixth Extinction" different?', 'Rates are ' + N('100–1,000 times') + ' faster than pre-human times, due to ' + T('human activities'))
d.basic('Predicted loss if trends continue?', 'Nearly ' + T('half') + ' of all species within ' + N('100 years'))
d.basic('Effects of biodiversity loss in a region?', 'Decline in plant production; lower resistance to perturbations (drought); more variable productivity, water use, pest and disease cycles')
d.cloze('The "Evil Quartet" of biodiversity loss: {{c1::habitat loss and fragmentation}}, {{c2::over-exploitation}}, {{c3::alien species invasions}}, {{c4::co-extinctions}}.')
d.basic('Mnemonic for the Evil Quartet?', '"' + T('HOPE') + '" lost: Habitat loss, Over-exploitation, Pests/alien invaders, Extinction partners (co-extinction)')
d.basic('Most important cause of extinction?', T('Habitat loss and fragmentation'))
d.basic('Tropical rain forest cover then and now?', 'Once > ' + N('14%') + ' of land; now ≤ ' + N('6%'))
d.basic('Why is Amazon called the "lungs of the planet"?', 'Huge rain forest estimated to produce ' + N('20%') + ' of atmospheric oxygen')
d.basic('Why is the Amazon being cleared?', 'For ' + T('soya beans') + ' and grassland for ' + T('beef cattle'))
d.basic('Who suffers most from fragmentation?', 'Mammals and birds needing ' + T('large territories') + ', and migratory animals')
d.basic('Over-exploitation: examples?', T('Steller’s sea cow, passenger pigeon') + '; over-harvested marine fish')
d.basic('"Need turns to greed" refers to?', T('Over-exploitation'))
d.basic('Nile perch example?', 'Introduced into ' + T('Lake Victoria') + ' → extinction of > ' + N('200') + ' species of ' + T('cichlid fish'))
d.basic('Invasive weeds threatening Indian species?', E('Parthenium (carrot grass), Lantana, water hyacinth (Eichhornia)'))
d.basic('Correction: NCERT spells water hyacinth "Eicchornia". Correct?', EI('Eichhornia'))
d.basic('Alien fish threatening Indian catfishes?', 'African catfish ' + EI('Clarias gariepinus') + ' (illegal introduction for aquaculture)')
d.basic('What is co-extinction? Examples?', 'Obligately associated species die with the host: a fish’s unique ' + T('parasites') + '; a coevolved ' + T('plant–pollinator') + ' pair')
d.basic('Major causes of species loss in a region (Exercise 5)?', 'The Evil Quartet: habitat loss/fragmentation, over-exploitation, alien invasions, co-extinctions')

# ---------------------------------------------------------------- 13.2 Conservation
d.sec('13.2.1-why-conserve')
d.cloze('Reasons to conserve biodiversity: {{c1::narrowly utilitarian}}, {{c2::broadly utilitarian}}, and {{c3::ethical}}.')
d.basic('Narrowly utilitarian reasons?', 'Direct economic benefits:<br>food, firewood, fibre, construction<br>industrial products (tannins, lubricants, dyes, resins, perfumes)<br>medicines')
d.basic('Drugs derived from plants?', 'More than ' + N('25%') + ' of drugs sold worldwide; ' + N('25,000') + ' plant species in traditional medicine')
d.basic('What is bioprospecting?', 'Exploring molecular, genetic and species-level diversity for products of ' + T('economic importance'))
d.basic('Broadly utilitarian reasons?', 'Ecosystem services: ' + T('oxygen') + ' (Amazon ~20%), ' + T('pollination') + ', aesthetic pleasures')
d.basic('Ethical reason?', 'Every species has ' + T('intrinsic value') + '; moral duty to pass on our biological legacy')
d.basic('How do biotic components control floods and erosion? (Exercise 8)', 'Plant ' + T('roots bind soil') + ', vegetation and litter slow runoff and increase water infiltration')

d.sec('13.2.2-how-conserve')
d.basic('What is in situ conservation?', 'On-site: protecting the whole ecosystem; "save the entire forest to ' + T('save the tiger') + '"')
d.basic('What is ex situ conservation, and when used?', 'Off-site: threatened species taken out for special care; when species are ' + T('endangered') + ' and need urgent measures')
d.basic('What are biodiversity hotspots?', 'Regions with very high ' + T('species richness') + ' and high ' + T('endemism') + '; also regions of accelerated habitat loss')
d.basic('What is endemism?', 'Species ' + T('confined to a region') + ' and found nowhere else')
d.basic('Number of hotspots (NCERT)?', 'Initially ' + N('25') + ', then 9 added → ' + N('34'))
d.basic('Update: current number of hotspots?', N('36') + ' (two more added after NCERT’s count)')
d.basic('Three hotspots covering India?', T('Western Ghats and Sri Lanka, Indo-Burma, Himalaya'))
d.basic('Land area and impact of hotspots?', 'Less than ' + N('2%') + ' of land; strict protection could reduce mass extinctions by ~' + N('30%'))
d.basic('India’s protected areas (NCERT)?', N('14') + ' biosphere reserves, ' + N('90') + ' national parks, ' + N('448') + ' wildlife sanctuaries')
d.basic('Update: India’s protected areas now?', 'About ' + N('18') + ' biosphere reserves, ' + N('106') + ' national parks and over ' + N('570') + ' sanctuaries (numbers keep growing)')
d.basic('What are sacred groves? Role? (Exercise 7)', 'Forest tracts set aside by religious/cultural tradition where all trees and wildlife are ' + T('venerated and protected') + '.<br>They are refuges for rare species')
table_card(d, 'Sacred groves', 'Where?', [
    ('Meghalaya', 'Khasi and Jaintia Hills', False), ('Rajasthan', 'Aravalli Hills', False),
    ('Karnataka, Maharashtra', 'Western Ghats', False), ('Madhya Pradesh', 'Sarguja, Chanda, Bastar', False)], term='Sacred groves of India')
d.basic('Importance of Meghalaya’s sacred groves?', 'Last refuges for many ' + T('rare and threatened plants'))
d.basic('Ex situ conservation places?', T('Zoological parks, botanical gardens, wildlife safari parks'))
d.basic('Modern ex situ techniques?', T('Cryopreservation') + ' of gametes, in vitro fertilisation, ' + T('tissue culture') + ', ' + T('seed banks'))
d.basic('Mnemonic: in situ vs ex situ?', T('In situ') + ' = "in its site" (parks, reserves, sacred groves)<br>' + T('Ex situ') + ' = "exit the site" (zoos, gardens, seed banks)')
d.basic('Earth Summit: name, place, year?', T('Convention on Biological Diversity') + ', ' + T('Rio de Janeiro') + ', ' + N('1992'))
d.basic('World Summit on Sustainable Development?', N('2002') + ', Johannesburg: ' + N('190') + ' countries pledged significant reduction of biodiversity loss by ' + N('2010'))
d.basic('Update: were the 2010 targets met, and what now?', X('No') + '; the 2022 ' + T('Kunming–Montreal') + ' framework aims to protect ' + T('30% of land and sea by 2030') + ' ("30×30")')
d.basic('When might we want a species extinct? (Exercise 10)', 'Disease-causing organisms, e.g. the ' + T('smallpox virus') + ' or ' + T('polio virus') + ', to protect human health')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Conservation', 'In situ or ex situ?', [
    ('National park', 'In situ', False), ('Sacred grove', 'In situ', False), ('Biosphere reserve', 'In situ', False),
    ('Zoo', 'Ex situ', False), ('Seed bank', 'Ex situ', False), ('Cryopreserved gametes', 'Ex situ', False)], term='In situ vs ex situ examples')
d.basic('Earth’s age of life (summary)?', 'Life originated nearly ' + N('3.8 billion years') + ' ago')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
