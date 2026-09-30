import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch12-ecosystem')
d = Deck('Chapter 12: Ecosystem', 'Class 12', ['class-12', 'biology', 'ch-12'])
d.description = 'Ecosystem structure, pond ecosystem, productivity, decomposition, energy flow, food chains, trophic levels and ecological pyramids'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- intro
d.sec('12.0-intro')
d.basic('Define ecosystem.', 'A ' + T('functional unit of nature') + ' where organisms interact among themselves and with the physical environment')
d.basic('What is the global ecosystem?', 'The ' + T('biosphere') + ': composite of all local ecosystems')
d.basic('Two basic categories of ecosystems with examples?', T('Terrestrial') + ': forest, grassland, desert. ' + T('Aquatic') + ': pond, lake, wetland, river, estuary.')
d.basic('Examples of man-made ecosystems?', E('Crop fields, aquarium'))

# ---------------------------------------------------------------- 12.1 Structure
d.sec('12.1-structure-and-function')
d.basic('What is species composition?', 'Identification and enumeration of plant and animal species of an ecosystem')
d.basic('What is stratification?', T('Vertical distribution') + ' of species at different levels')
d.basic('Stratification in a forest?', 'Trees: top layer; shrubs: second; herbs and grasses: bottom')
d.cloze('Four functional aspects of an ecosystem: {{c1::productivity}}, {{c2::decomposition}}, {{c3::energy flow}}, {{c4::nutrient cycling}}.')
d.basic('Why is a pond a good model ecosystem?', 'Fairly ' + T('self-sustainable') + ', simple, and shows all four functional aspects')
table_card(d, 'Pond ecosystem', 'What is it?', [
    ('Abiotic', 'Water with dissolved substances, bottom soil; sun, temperature, day-length', False),
    ('Autotrophs', 'Phytoplankton, algae, floating/submerged/marginal plants', False),
    ('Consumers', 'Zooplankton, free-swimming and bottom-dwelling forms', False),
    ('Decomposers', 'Fungi, bacteria, flagellates (at the bottom)', False)], term='Components of a pond ecosystem')
d.basic('Direction of energy flow in an ecosystem?', T('Unidirectional') + ' towards higher trophic levels, with loss as heat')
d.basic('Components of an ecosystem (Exercise 7)?', T('Abiotic') + ' (air, water, soil, climate) and ' + T('biotic') + ' (producers, consumers, decomposers)')

# ---------------------------------------------------------------- 12.2 Productivity
d.sec('12.2-productivity')
d.basic('Basic requirement for an ecosystem to function?', 'Constant input of ' + T('solar energy'))
d.basic('Define primary production.', 'Amount of ' + T('biomass/organic matter') + ' produced per unit area over time by plants during photosynthesis')
d.basic('Units of primary production vs productivity?', T('Production') + ': g m⁻² or kcal m⁻². ' + T('Productivity (rate)') + ': g m⁻² yr⁻¹ or kcal m⁻² yr⁻¹.')
d.basic('What is GPP?', T('Gross primary productivity') + ': rate of production of organic matter during photosynthesis')
d.basic('What is NPP?', T('Net primary productivity') + ' = GPP − respiration losses (R)')
d.basic('NPP equation?', '\\( NPP = GPP - R \\)')
d.basic('Significance of NPP?', 'Biomass available to ' + T('heterotrophs') + ' (herbivores and decomposers)')
d.basic('What is secondary productivity?', 'Rate of formation of new organic matter by ' + T('consumers'))
d.basic('Primary vs secondary productivity (Exercise 6f)?', T('Primary') + ': by producers (photosynthesis). ' + T('Secondary') + ': by consumers.')
d.basic('Factors affecting primary productivity (Exercise 9)?', 'Plant ' + T('species') + ', environmental factors, ' + T('nutrient availability') + ', photosynthetic capacity')
d.basic('Annual NPP of the biosphere?', 'About ' + N('170 billion tons') + ' (dry weight)')
d.basic('NPP of oceans?', 'Only ' + N('55 billion tons') + ' despite covering ~' + N('70%') + ' of the surface')
d.basic('Why is ocean productivity low? (think)', T('Light') + ' does not penetrate deep and ' + T('nutrients') + ' (N, P) are limiting in open ocean')
d.basic('Limiting factor for aquatic productivity (Exercise 1c)?', T('Light') + ' (also nutrients)')
d.basic('Mnemonic: GPP vs NPP?', '"' + T('Gross = Gross salary, Net = take-home') + '": respiration is the tax the plant pays itself')

# ---------------------------------------------------------------- 12.3 Decomposition
d.sec('12.3-decomposition')
d.basic('Why is the earthworm the "farmer’s friend"?', 'Breaks down complex organic matter and ' + T('loosens the soil'))
d.basic('Define decomposition.', 'Breakdown of complex organic matter into inorganic ' + T('CO₂, water and nutrients') + ' by decomposers')
d.basic('What is detritus?', 'Dead plant remains (leaves, bark, flowers) and dead animal remains incl. faecal matter.<br>Raw material for decomposition')
d.cloze('Steps of decomposition: {{c1::fragmentation}}, {{c2::leaching}}, {{c3::catabolism}}, {{c4::humification}}, {{c5::mineralisation}}.')
d.basic('Mnemonic for decomposition steps?', '"' + T('Farmers Love Cows, Hens, Mangoes') + '": Fragmentation, Leaching, Catabolism, Humification, Mineralisation')
d.basic('What is fragmentation?', T('Detritivores') + ' (e.g. earthworm) break detritus into smaller particles')
d.basic('What is leaching?', 'Water-soluble inorganic nutrients go down into the soil horizon and precipitate as ' + X('unavailable salts'))
d.basic('What is catabolism?', 'Bacterial and fungal ' + T('enzymes') + ' degrade detritus into simpler inorganic substances')
d.basic('Do decomposition steps happen in sequence?', X('No') + '; all operate ' + T('simultaneously') + ' on the detritus', **fig('fig_12_1_decomposition'))
d.basic('What is humification?', 'Accumulation of dark, amorphous ' + T('humus') + ', highly resistant to microbes, decomposed extremely slowly')
d.basic('Why is humus a nutrient reservoir?', 'It is ' + T('colloidal'))
d.basic('What is mineralisation?', 'Release of ' + T('inorganic nutrients') + ' by microbial degradation of humus')
d.basic('Is decomposition aerobic?', 'Largely ' + T('oxygen-requiring'))
d.basic('Detritus decomposing slowly vs quickly?', T('Slow') + ': rich in ' + X('lignin and chitin') + '. ' + T('Fast') + ': rich in nitrogen and water-soluble sugars.')
d.basic('Most important climatic factors for decomposition?', T('Temperature and soil moisture'))
d.basic('Conditions favouring vs inhibiting decomposition?', T('Warm and moist') + ' favour; ' + X('low temperature and anaerobiosis') + ' inhibit → organic matter builds up')
d.basic('Why do peat bogs and tundra accumulate organic matter? (intuition)', 'Cold and waterlogged (anaerobic): decomposers work very ' + X('slowly'))
d.basic('Common detritivore (Exercise 1d)?', T('Earthworm'))
d.basic('Production vs decomposition (Exercise 6b)?', T('Production') + ': inorganic → organic by producers. ' + T('Decomposition') + ': organic → inorganic by decomposers.')
d.basic('Litter vs detritus (Exercise 6e)?', T('Litter') + ': dead plant parts on the ground. ' + T('Detritus') + ': all dead plant and animal remains incl. faeces.')

# ---------------------------------------------------------------- 12.4 Energy flow
d.sec('12.4-energy-flow')
d.basic('Only ecosystem not dependent on the sun?', 'Deep-sea ' + T('hydrothermal') + ' ecosystem')
d.basic('What fraction of incident solar radiation is PAR? (Exercise 5)', 'Less than ' + N('50%'))
d.basic('What fraction of PAR do plants capture?', 'Only ' + N('2–10%'))
d.basic('Energy flow and the first law of thermodynamics?', 'Energy is not created; it flows ' + T('unidirectionally') + ' from sun → producers → consumers')
d.basic('Why do ecosystems obey the second law?', 'They need a ' + T('constant energy supply') + ' to counter increasing disorder (entropy)')
d.basic('Major producers in terrestrial vs aquatic ecosystems?', T('Terrestrial') + ': herbaceous and woody plants. ' + T('Aquatic') + ': phytoplankton, algae, higher plants.')
d.basic('Why do food chains form?', T('Interdependency') + ': an animal feeds on a plant/animal and is food for another')
d.basic('Where does the detritus food chain begin?', 'With ' + T('death') + ' of an organism')
d.basic('Primary, secondary, tertiary consumers?', T('Primary') + ': eat producers (herbivores)<br>' + T('Secondary') + ': eat herbivores (primary carnivores)<br>' + T('Tertiary') + ': eat primary carnivores')
d.basic('Common herbivores?', 'Insects, birds, mammals (land); ' + T('molluscs') + ' (aquatic)')
d.basic('Example of grazing food chain?', 'Grass (producer) → goat (primary consumer) → man (secondary consumer)')
d.basic('What makes up the detritus food chain?', 'Decomposers (' + T('fungi and bacteria') + '): saprotrophs that secrete enzymes to digest dead matter and absorb products')
d.basic('Which chain dominates energy flow in water vs land?', T('Aquatic') + ': grazing food chain. ' + T('Terrestrial') + ': detritus food chain carries much more energy.')
d.basic('GFC vs DFC (Exercise 6a)?', T('GFC') + ': starts with producers, sun-dependent. ' + T('DFC') + ': starts with dead organic matter, decomposers.')
d.basic('What forms a food web?', 'Natural interconnection of food chains; DFC organisms eaten by GFC animals, omnivores (cockroaches, crows)')
d.basic('Food chain vs food web (Exercise 6d)?', T('Chain') + ': single linear path. ' + T('Web') + ': interconnected chains.')
d.basic('What is a trophic level?', 'An organism’s place in a food chain based on its ' + T('source of nutrition'), **fig('fig_12_2_trophic_levels'))
table_card(d, 'Figure 12.2', 'Examples?', [
    ('1st trophic level (producers)', 'Phytoplankton, grass, trees', False), ('2nd (herbivores)', 'Zooplankton, grasshopper, cow', False),
    ('3rd (carnivores)', 'Birds, fishes, wolf', False), ('4th (top carnivores)', 'Man, lion', False)], term='Trophic levels and examples')
d.basic('Second trophic level in a lake (Exercise 3)?', T('Zooplankton'))
d.basic('What happens to energy at successive trophic levels?', 'It ' + T('decreases') + '; lost as heat at each step', **fig('fig_12_3_energy_flow'))
d.basic('What is standing crop?', 'Mass of living material at a trophic level at a particular time (biomass or number per unit area)')
d.basic('Why is dry weight a better measure of biomass?', 'Water content varies and carries ' + X('no energy') + '; dry weight is accurate')
d.basic('What is the 10 per cent law?', 'Only ' + N('10%') + ' of energy is transferred to the next trophic level')
d.basic('Why are grazing food chains short? (intuition)', 'After 4–5 levels too little energy remains (10% × 10% × 10%…) to support another level')
d.basic('Is there a limit on the detritus food chain?', 'Not in the same way; decomposers work on dead matter from all levels')

# ---------------------------------------------------------------- 12.5 Pyramids
d.sec('12.5-ecological-pyramids')
d.basic('Three types of ecological pyramids?', 'Pyramid of ' + T('number') + ', ' + T('biomass') + ', ' + T('energy'))
d.basic('What do base and apex represent?', 'Base: ' + T('producers') + '. Apex: ' + T('top consumers') + '.')
d.basic('Grassland pyramid of numbers: producers vs top carnivores?', 'About ' + N('5,842,000') + ' plants support only ' + N('3') + ' top carnivores', **fig('fig_12_4a_pyramid_numbers'))
d.basic('Pyramid of biomass values (Figure 12.4b)?', 'P ' + N('809') + ', PC ' + N('37') + ', SC ' + N('11') + ', TC ' + N('1.5') + ' kg m⁻²', **img('fig_12_4b_pyramid_biomass'))
d.basic('Inverted pyramid of biomass: where and why?', T('Sea') + ': small standing crop of phytoplankton (' + N('4') + ') supports larger zooplankton (' + N('21') + ')', **fig('fig_12_4c_inverted_biomass'))
d.basic('How can small phytoplankton biomass support larger consumers? (paradox)', 'Phytoplankton ' + T('reproduce very fast') + ' (high turnover), so productivity is high though standing crop is small')
d.basic('Pyramid of numbers for a single tree with insects and birds?', T('Inverted') + ' (one tree, many insects, fewer birds): spindle/inverted shape')
d.basic('Pyramid of numbers in a tree-dominated ecosystem (Exercise 1b)?', T('Inverted'))
d.basic('Why is the pyramid of energy always upright?', 'Energy is always ' + T('lost as heat') + ' at each transfer; it can never be inverted', **fig('fig_12_4d_pyramid_energy'))
d.basic('Ideal energy pyramid values (Figure 12.4d)?', '1,000,000 J sunlight → P ' + N('10,000 J') + ' → PC ' + N('1000 J') + ' → SC ' + N('100 J') + ' → TC ' + N('10 J'))
d.basic('What % of sunlight do producers convert into NPP (Figure 12.4d)?', 'Only ' + N('1%'))
d.basic('Why must pyramid calculations include all organisms at a level?', 'Generalisations from a few individuals would be ' + X('untrue'))
d.basic('Is a trophic level a species?', X('No') + '; it is a ' + T('functional level') + '; a species can occupy more than one')
d.basic('Example of a species at two trophic levels?', T('Sparrow') + ': primary consumer eating seeds/fruits, secondary consumer eating insects/worms')
d.basic('Upright vs inverted pyramid (Exercise 6c)?', T('Upright') + ': broad base (most ecosystems). ' + T('Inverted') + ': narrow base (tree–insect numbers, sea biomass).')
d.basic('Limitations of ecological pyramids?', 'Ignore a species at two or more levels; assume a simple chain, not a web; give ' + X('no place to saprophytes') + ' (decomposers)')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Pyramids', 'Shape?', [
    ('Numbers, grassland', 'Upright', False), ('Numbers, single tree', 'Inverted', True),
    ('Biomass, land', 'Upright', False), ('Biomass, sea', 'Inverted', True), ('Energy, any', 'Always upright', False)],
    term='Shapes of ecological pyramids')
table_card(d, 'Exercise 1', 'Fill the blank', [
    ('Plants fix CO₂ so they are', 'Producers (autotrophs)', False), ('Pyramid of numbers in a tree ecosystem', 'Inverted', False),
    ('Limiting factor in aquatic productivity', 'Light', False), ('Common detritivore', 'Earthworm', False),
    ('Major reservoir of carbon', 'Oceans', False)], term='Fill in the blanks (Exercise 1)')
d.basic('Nutrient cycle types (summary)?', T('Gaseous') + ': reservoir in atmosphere/hydrosphere (carbon). ' + T('Sedimentary') + ': reservoir in earth’s crust (phosphorus).')
d.basic('What are ecosystem services?', 'Products of ecosystem processes, e.g. ' + T('purification of air and water') + ' by forests')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
