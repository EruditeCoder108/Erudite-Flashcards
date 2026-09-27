import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch11-organisms-and-populations')
d = Deck('Chapter 11: Organisms and Populations', 'Class 12', ['class-12', 'biology', 'ch-11'])
d.description = 'Population attributes, density, growth models, life history, and interactions: predation, competition, parasitism, commensalism, mutualism'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
PD = (1001, 606)

# ---------------------------------------------------------------- intro
d.sec('11.0-intro')
d.basic('Who is the Father of Ecology in India?', T('Ramdeo Misra') + ' (BHU, Varanasi)')
d.basic('"How" vs "why" questions in biology?', T('How') + ': mechanism of a process. ' + T('Why') + ': significance of the process.')
d.basic('Example: bulbul singing: how and why?', T('How') + ': voice box and vibrating bone. ' + T('Why') + ': to communicate with its mate in the breeding season.')
d.basic('Define ecology.', 'Study of interactions among organisms and between organisms and their ' + T('physical (abiotic) environment'))
d.basic('Four levels of organisation in ecology?', T('Organisms, populations, communities, biomes'))

# ---------------------------------------------------------------- 11.1 Populations
d.sec('11.1.1-population-attributes')
d.basic('Define population.', 'Individuals of a species in a well-defined area sharing/competing for resources and potentially ' + T('interbreeding'))
d.basic('Are asexually produced groups populations?', T('Yes') + ', for ecological studies')
d.basic('Examples of populations (NCERT)?', 'Cormorants in a wetland, rats in a dwelling, teakwood trees in a forest, bacteria on a plate, lotus plants in a pond')
d.basic('Why is population ecology important?', 'Natural selection operates at the ' + T('population level') + '; links ecology to population genetics and evolution')
d.basic('Attributes of a population but not an individual (Exercise 1)?', T('Birth rate, death rate, sex ratio, age distribution') + ', population density')
steps_card(d, 'Birth rate', '20 lotus plants; 8 new plants added in a year. Birth rate?', 'Per capita rate = new ÷ initial.',
           ['Births = 8', 'Initial population = 20', 'Birth rate = 8/20 = <b>0.4</b> offspring per lotus per year'], 2, 'Birth rate calculation (lotus)', '0.4 per lotus per year')
steps_card(d, 'Death rate', '4 of 40 fruitflies die in a week. Death rate?', 'Per capita rate = deaths ÷ population.',
           ['Deaths = 4', 'Population = 40', 'Death rate = 4/40 = <b>0.1</b> per fruitfly per week'], 2, 'Death rate calculation (fruitflies)', '0.1 per fruitfly per week')
d.basic('What is an age pyramid?', 'Plot of age distribution (per cent individuals of each age group), for males and females')
d.basic('Three shapes of age pyramids?', T('Expanding') + ' (broad base, growing), ' + T('stable') + ', ' + T('declining') + ' (narrow base)', **fig('fig_11_1_age_pyramids'))
d.basic('Three age groups in a pyramid?', 'Pre-reproductive, reproductive, post-reproductive')
d.basic('What does a broad pre-reproductive base indicate? (intuition)', 'Many young individuals about to reproduce → ' + T('growing') + ' population')
d.basic('Examples of small and huge population sizes?', '< 10 ' + T('Siberian cranes') + ' at Bharatpur; millions of ' + EI('Chlamydomonas') + ' in a pond')
d.basic('Technical name for population size?', T('Population density (N)'))
d.basic('When is number not a good measure of density?', 'E.g. one huge banyan vs 200 ' + EI('Parthenium') + ' plants: use ' + T('per cent cover or biomass'))
d.basic('Best measure of density for dense bacterial culture?', T('Biomass') + '/turbidity rather than counting')
d.basic('Example of relative density?', 'Number of ' + T('fish caught per trap'))
d.basic('How is tiger census done?', 'Indirectly using ' + T('pug marks and fecal pellets'))

d.sec('11.1.2-population-growth')
d.cloze('Density increases by {{c1::natality}} and {{c2::immigration}}; decreases by {{c3::mortality}} and {{c4::emigration}}.')
d.basic('Define natality and mortality.', T('Natality') + ': number of births in a period. ' + T('Mortality') + ': number of deaths in a period.')
d.basic('Define immigration and emigration.', T('Immigration') + ': individuals of the same species ' + T('coming in') + '. ' + T('Emigration') + ': individuals ' + T('leaving') + '.')
d.basic('Equation for population density at t + 1?', '\\( N_{t+1} = N_t + [(B + I) - (D + E)] \\)')
d.occlusion('Figure 11.2 · Factors changing population density', M + 'fig_11_2_population_density.webp', PD, [
    ('Immigration (I)', wbox(420, 45, 575, 105, PD), True), ('Natality (B)', wbox(80, 255, 175, 320, PD), True),
    ('Mortality (D)', wbox(805, 255, 930, 322, PD), True), ('Emigration (E)', wbox(428, 495, 565, 560, PD), True),
    ('Population density (N)', wbox(420, 270, 572, 376, PD), True)])
d.basic('Most important factors under normal conditions?', T('Births and deaths'))
d.basic('When is immigration more important than births?', 'When a ' + T('new habitat') + ' is just being colonised')

d.basic('When does exponential growth occur?', 'When resources (food, space) are ' + T('unlimited'))
d.basic('Exponential growth equation?', '\\( \\frac{dN}{dt} = rN \\), where \\( r = b - d \\)')
d.basic('What is r?', T('Intrinsic rate of natural increase') + ': per capita births minus deaths')
table_card(d, 'r values', 'r?', [
    ('Norway rat', '0.015', False), ('Flour beetle', '0.12', False), ('Human population, India (1981)', '0.0205', False)], term='Intrinsic rates of increase')
d.basic('Shape of exponential growth curve?', T('J-shaped'), **fig('fig_11_3_growth_curves'))
d.basic('Integral form of exponential growth?', '\\( N_t = N_0 e^{rt} \\)')
d.basic('Chess-board anecdote teaches?', 'Doubling each square (1, 2, 4, 8…) quickly exceeds a kingdom’s wheat: ' + T('exponential growth') + ' explodes')
steps_card(d, 'Exercise 2', 'Population doubles in 3 years. Find r.', 'Use \\( N_t = N_0 e^{rt} \\).',
           ['2N₀ = N₀ e^{3r}', 'ln 2 = 3r', 'r = 0.693 / 3 = <b>0.231 per year</b>'], 2, 'Exercise 2: r from doubling time', 'r ≈ 0.231 per year')
d.basic('What is carrying capacity (K)?', 'Maximum number a habitat’s resources can support')
d.basic('Phases of logistic growth?', T('Lag') + ' → acceleration → deceleration → ' + T('asymptote') + ' at K')
d.basic('Name and shape of logistic growth?', T('Verhulst–Pearl logistic growth') + '; ' + T('sigmoid (S-shaped)') + ' curve')
d.basic('Logistic growth equation?', '\\( \\frac{dN}{dt} = rN \\left( \\frac{K - N}{K} \\right) \\)')
d.basic('What does (K − N)/K do in the logistic equation? (intuition)', 'It is the ' + T('fraction of space left') + ': near zero when N ≈ K, so growth slows to zero')
d.basic('Which growth model is more realistic, and why?', T('Logistic') + ': resources are finite and become limiting')
d.basic('Read Figure 11.3: curve a vs b?', '(a) ' + T('Exponential') + ' (J), responses not limiting. (b) ' + T('Logistic') + ' (S), responses limiting; flattens at K.', **img('fig_11_3_growth_curves'))

d.sec('11.1.3-life-history')
d.basic('What do populations evolve to maximise?', T('Reproductive (Darwinian) fitness') + ' (high r)')
d.basic('Organisms that breed only once?', E('Pacific salmon fish, bamboo'))
d.basic('Organisms breeding many times?', E('Most birds and mammals'))
d.basic('Many small offspring vs few large offspring?', T('Many small') + ': ' + E('oysters, pelagic fishes') + '. ' + T('Few large') + ': ' + E('birds, mammals') + '.')
d.basic('What shapes life-history traits?', 'Constraints of the ' + T('abiotic and biotic') + ' components of the habitat')

# ---------------------------------------------------------------- 11.1.4 Interactions
d.sec('11.1.4-population-interactions')
d.basic('Can a habitat have just one species?', X('No') + '; even a plant needs soil microbes and pollinators')
d.basic('What are interspecific interactions?', 'Interactions between populations of ' + T('two different species'))
table_card(d, 'Table 11.1', 'Name of interaction?', [
    ('+ / +', 'Mutualism', False), ('− / −', 'Competition', True), ('+ / − (eats)', 'Predation', False),
    ('+ / − (lives on/in)', 'Parasitism', False), ('+ / 0', 'Commensalism', False), ('− / 0', 'Amensalism', True)],
    term='Population interactions (Table 11.1)')
d.basic('Mnemonic for "+/0" vs "−/0"?', 'Co' + T('M') + 'mensalism = one gets a "Meal/benefit" (+/0). ' + T('A') + 'mensalism = one gets "Ache" (−/0).')
d.basic('Which interactions involve species living closely together?', T('Predation, parasitism, commensalism'))
d.basic('Correct statement for parasitism (Exercise 9)?', '(d) ' + T('One benefits, the other is affected (harmed)'))

d.sec('predation')
d.basic('Predation as an energy process?', 'Nature’s way of transferring energy fixed by plants to ' + T('higher trophic levels'))
d.basic('Is a sparrow eating seeds a predator?', T('Yes') + '; herbivores are broadly predators too')
d.basic('Roles of predators?', 'Energy conduits; keep ' + T('prey populations under control') + '; maintain ' + T('species diversity') + ' by reducing competition among prey')
d.basic('Why do exotic species become invasive?', 'The invaded land ' + X('lacks their natural predators'))
d.basic('Prickly pear cactus in Australia?', 'Introduced in 1920s, spread over millions of hectares; controlled by a ' + T('cactus-feeding moth') + ' from its native habitat')
d.basic('Principle behind biological pest control (Exercise 5)?', 'Ability of the ' + T('predator to regulate prey') + ' population')
d.basic('Pisaster experiment?', 'Removing the starfish ' + EI('Pisaster') + ' from intertidal areas made ' + N('10+') + ' invertebrate species extinct within a year due to competition')
d.basic('Why are predators "prudent"?', 'Over-exploiting prey would make the prey and then the predator ' + X('extinct'))
d.basic('Prey defences against predation?', T('Camouflage') + ' (cryptic colouring in insects, frogs), being ' + T('poisonous'))
d.basic('Why is the Monarch butterfly distasteful to birds?', 'A special chemical acquired by its caterpillar from feeding on a ' + T('poisonous weed'))
d.basic('What fraction of insects are phytophagous?', 'Nearly ' + N('25%'))
d.basic('Why is herbivory severe for plants?', 'Plants ' + X('cannot run away'))
d.basic('Plant defences against herbivores (Exercise 3)?', T('Thorns') + ' (Acacia, cactus); ' + T('chemicals') + ' that sicken, deter, disrupt reproduction or kill')
d.basic('Why don’t cattle browse Calotropis?', 'It produces highly poisonous ' + T('cardiac glycosides'))
d.basic('Commercial plant chemicals that are actually defences?', E('Nicotine, caffeine, quinine, strychnine, opium'))
d.basic('What is camouflage? Example (Exercise 7c)?', 'Cryptic colouring to avoid detection; e.g. ' + E('insects and frogs') + ' blending with background')

d.sec('competition')
d.basic('Does competition occur only among related species?', X('No') + '; e.g. ' + E('flamingoes and fishes') + ' compete for zooplankton in South American lakes')
d.basic('Does competition need limiting resources?', X('Not always') + '; ' + T('interference competition') + ' reduces feeding efficiency even when resources are abundant')
d.basic('Best definition of competition?', 'Fitness (' + T('r') + ') of one species is significantly lower in the presence of another')
d.basic('Evidence: Abingdon tortoise?', 'Became extinct within a decade after ' + T('goats') + ' were introduced on Galapagos (better browsing efficiency)')
d.basic('What is competitive release?', 'A species restricted by a superior competitor ' + T('expands its range') + ' when the competitor is removed')
d.basic('Connell’s barnacle experiment?', 'On Scottish rocky coasts, larger ' + EI('Balanus') + ' excludes smaller ' + EI('Chthamalus') + ' from the intertidal zone')
d.basic('Correction: NCERT spells the barnacle "Chathamalus". Correct?', EI('Chthamalus'))
d.basic('Who are more affected by competition?', T('Herbivores and plants') + ' more than carnivores')
d.basic('State Gause’s competitive exclusion principle.', 'Two closely related species competing for the same resources ' + X('cannot co-exist') + ' indefinitely; the inferior one is eliminated')
d.basic('What is resource partitioning?', 'Competing species avoid competition by different feeding ' + T('times') + ' or ' + T('foraging patterns'))
d.basic('MacArthur’s warblers?', N('Five') + ' closely related warbler species on the same tree co-existed through ' + T('behavioural differences') + ' in foraging')
d.basic('Interspecific competition example (Exercise 7e)?', E('Flamingoes and resident fishes') + ' competing for zooplankton')

d.sec('parasitism')
d.basic('Why has parasitism evolved so widely?', 'It ensures ' + T('free lodging and meals'))
d.basic('What is host–parasite co-evolution?', 'Host evolves resistance, parasite evolves counter-mechanisms (host-specific parasites)')
d.basic('Adaptations of parasites?', 'Loss of unnecessary ' + T('sense organs') + ', adhesive organs/' + T('suckers') + ', loss of ' + T('digestive system') + ', ' + T('high reproductive capacity'))
d.basic('Hosts of the human liver fluke?', 'Two intermediate hosts: a ' + T('snail') + ' and a ' + T('fish'))
d.basic('Effects of parasites on hosts?', 'Reduce survival, growth, reproduction, population density; make hosts vulnerable to predation')
d.basic('Why no totally harmless parasites? (think)', 'Parasites maximise their own reproduction; using host resources inevitably causes some ' + T('harm'))
d.basic('Ectoparasites: examples?', E('Lice on humans, ticks on dogs') + ', copepods on marine fish, ' + EI('Cuscuta') + ' on hedge plants')
d.basic('Adaptations of Cuscuta?', 'Lost ' + X('chlorophyll and leaves') + '; takes nutrition from host plant')
d.basic('Why is the female mosquito not a parasite?', 'It only takes a blood meal briefly for reproduction; does ' + X('not live') + ' on the host')
d.basic('What are endoparasites?', 'Live inside the host (liver, kidney, lungs, RBCs); complex life cycles, simplified bodies, high reproductive potential')
d.basic('What is brood parasitism? Example?', 'Parasitic bird lays eggs in the host’s nest for incubation; ' + E('cuckoo (koel) in crow’s nest'))
d.basic('Adaptation in brood parasites?', 'Eggs ' + T('resemble') + ' host eggs in size and colour')

d.sec('commensalism')
d.basic('Examples of commensalism?', 'Orchid epiphyte on mango; barnacles on whale; ' + T('cattle egret and cattle') + '; clown fish and sea anemone')
d.basic('Orchid on mango branch: interaction? (Exercise 4)', T('Commensalism') + ': orchid benefits, mango unaffected')
d.basic('Why does the egret follow cattle?', 'Moving cattle ' + T('flush out insects') + ' for the egret')
d.basic('Clown fish and sea anemone?', 'Fish gets ' + T('protection') + ' among stinging tentacles; anemone gains nothing apparent')

d.sec('mutualism')
d.basic('Examples of mutualism?', T('Lichens') + ' (fungus + alga/cyanobacteria), ' + T('mycorrhizae') + ' (fungus + roots), plant–pollinator relations')
d.basic('Benefits in mycorrhizae?', 'Fungi help ' + T('nutrient absorption') + '; plant gives ' + T('carbohydrates'))
d.basic('Rewards plants give animals?', T('Pollen and nectar') + ' for pollinators; juicy fruits for seed dispersers')
d.basic('Why do plant–animal interactions involve co-evolution?', 'To safeguard against ' + X('cheaters') + ' (nectar thieves); flower and pollinator evolution are tightly linked')
d.basic('Fig–wasp mutualism?', 'One-to-one: each fig species pollinated only by its partner wasp; wasp lays eggs in fruit and larvae eat some developing seeds', **fig('fig_11_4_fig_wasp'))
d.basic('Ophrys orchid strategy?', T('Sexual deceit') + ': a petal resembles the female bee; the male "pseudocopulates" and transfers pollen', **fig('fig_11_5_orchid_bee'))
d.basic('Why must Ophrys co-evolve with the bee?', 'If the female bee’s pattern changes, pollination success drops unless the petal keeps resembling her')

# ---------------------------------------------------------------- summary
d.sec('summary')
d.basic('Define population vs community (Exercise 6).', T('Population') + ': individuals of one species in an area. ' + T('Community') + ': populations of different species interacting in an area.')
table_card(d, 'Interaction examples', 'Type?', [
    ('Fig and wasp', 'Mutualism', False), ('Cuckoo and crow', 'Brood parasitism', False),
    ('Balanus and Chthamalus', 'Competition', False), ('Cattle egret and cattle', 'Commensalism', False),
    ('Prickly pear and moth', 'Predation (biocontrol)', False), ('Cuscuta and hedge plant', 'Parasitism', False)], term='Classify the interaction')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
