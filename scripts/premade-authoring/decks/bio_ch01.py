import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase as sc

OUT = os.path.join(ROOT, 'premade-cards', '11th', 'Biology', 'class11-biology-ch01-the-living-world')
d = Deck('Chapter 1: The Living World', 'Class 11', ['class-11', 'biology', 'ch-1'])
d.description = 'Diversity, nomenclature, binomial names, taxonomy and the taxonomic hierarchy'
M = 'media/'

# ---------------------------------------------------------------- Ernst Mayr
d.sec('ernst-mayr')
d.basic("Which biologist has been called 'the Darwin of the 20th century'?", T('Ernst Mayr') + ' (' + N('1904–2004') + ')')
d.basic('Which definition did Ernst Mayr pioneer?', 'The currently accepted definition of a ' + T('biological species'))
d.basic("Which central question of evolutionary biology did Mayr make it what it is today?", 'The ' + T('origin of species diversity'))

# ---------------------------------------------------------------- 1.1 Diversity
d.sec('1.1-diversity')
d.basic('How many species are known and described?', N('1.7–1.8 million'))
d.basic('What does each different kind of plant, animal or organism represent?', 'A ' + T('species'))
d.basic('What does biodiversity refer to?', 'The ' + T('number and types') + ' of organisms present on earth')
d.basic('Why do we need scientific names instead of local names?', 'Local names vary from place to place, even within a country; a ' + T('standard name') + ' is known all over the world')
d.basic('What is nomenclature?', 'Standardising the ' + T('naming') + ' of living organisms, so an organism has the same name all over the world')
d.basic('What is identification?', 'Describing the organism ' + T('correctly') + ', so we know to which organism a name is attached')
d.basic('Why must identification come before nomenclature?', 'A name can only be given once we know ' + T('which organism') + ' it is attached to')
d.cloze('Scientific names of plants follow the {{c1::International Code for Botanical Nomenclature (ICBN)}}; '
        'animals follow the {{c2::International Code of Zoological Nomenclature (ICZN)}}.')
d.basic('What three things do scientific names ensure?', '<ul><li>Each organism has ' + T('only one name') + '</li>'
        '<li>People anywhere can arrive at the ' + T('same name') + '</li><li>The name is ' + X('not used') + ' for any other known organism</li></ul>')

d.sec('1.1-binomial-nomenclature')
d.basic('What is binomial nomenclature?', 'Naming with ' + T('two components') + ': the ' + T('generic name') + ' and the ' + T('specific epithet'))
d.basic('Who gave the binomial system of nomenclature?', T('Carolus Linnaeus'))
d.basic('What is the scientific name of mango?', EI('Mangifera indica'))
d.cloze('In <i>Mangifera indica</i>, <i>Mangifera</i> is the {{c1::genus}} and <i>indica</i> is the {{c2::specific epithet}}.')
sc.binomial_anatomy(d)
d.basic('In what language are biological names written?', T('Latin') + ' (Latinised or derived from Latin, whatever their origin)')
d.basic('How is a biological name shown when printed, and when handwritten?', 'Printed in ' + T('italics') + '; handwritten, each word is ' + T('separately underlined'))
d.basic('Which word of a biological name starts with a capital letter?', 'The ' + T('genus') + '. The specific epithet starts with a ' + X('small') + ' letter.')
d.basic('Where is the author\'s name written in a biological name, and how?', 'After the specific epithet, at the ' + T('end') + ', in an ' + T('abbreviated') + ' form')
d.basic("What does 'Linn.' in <i>Mangifera indica</i> Linn. tell you?", 'The species was first described by ' + T('Linnaeus'))
d.basic('Which is written correctly: <i>Mangifera Indica</i> or <i>Mangifera indica</i>?', EI('Mangifera indica') + ': the specific epithet starts with a ' + X('small') + ' letter')

d.sec('1.1-classification-taxonomy')
d.basic('What is classification?', 'Grouping anything into ' + T('convenient categories') + ' based on some easily observable characters')
d.basic("What is the scientific term for categories such as 'plants', 'mammals', 'dogs' and 'wheat'?", T('Taxa') + ' (singular: taxon)')
d.basic("'Animals', 'mammals' and 'dogs' are all taxa. How do they differ?", 'They are taxa at ' + T('different levels') + ': a dog is a mammal, and mammals are animals')
d.basic('What is taxonomy?', 'The process of classifying all living organisms into taxa based on their ' + T('characteristics'))
d.basic('What forms the basis of modern taxonomic studies?', '<ul><li>External and internal structure</li><li>Structure of the cell</li><li>Development process</li><li>Ecological information</li></ul>')
d.cloze('The four processes basic to taxonomy are {{c1::characterisation}}, {{c2::identification}}, {{c3::classification}} and {{c4::nomenclature}}.')
d.basic('On what were the earliest classifications based?', 'The ' + T("'uses'") + ' of organisms, for food, clothing and shelter')
d.basic('What is systematics?', 'The study of the kinds and diversity of organisms and the ' + T('relationships') + ' among them')
d.basic("From which word is 'systematics' derived, and what does it mean?", 'Latin ' + T("'systema'") + ': systematic arrangement of organisms')
d.basic('What was the title of the publication of Linnaeus?', EI('Systema Naturae'))
d.basic('The scope of systematics was later enlarged to include what?', 'Identification, nomenclature and classification')
d.basic('What kind of relationships does systematics take into account?', T('Evolutionary') + ' relationships between organisms')
d.basic('Name four areas where taxonomic studies are useful.', 'Agriculture, forestry, industry, and knowing our ' + T('bio-resources') + ' and their diversity')

# ---------------------------------------------------------------- 1.2 Taxonomic categories
d.sec('1.2-taxonomic-categories')
d.basic('Is classification a single step?', X('No') + '. It is a ' + T('hierarchy of steps') + ', each step a rank or category')
d.cloze('Each step of classification is a {{c1::taxonomic category}}; all the categories together form the {{c2::taxonomic hierarchy}}.')
d.basic('What is a taxon?', 'A category or ' + T('rank') + ', used as a unit of classification')
d.basic('What common feature makes insects a recognisable group?', N('Three pairs') + ' of ' + T('jointed legs'))
d.basic('Are taxonomic categories merely morphological aggregates?', X('No') + '. They are distinct ' + T('biological entities'))
d.basic('What is the lowest taxonomic category of all organisms?', T('Species'))
d.basic('What is the basic requirement for placing an organism in the various categories?', 'Knowledge of its ' + T('characters'))
d.basic('In plants, which category takes the place of phylum?', T('Division'))
d.occlusion('Figure 1.1 · Taxonomic categories in ascending order', M + 'fig_1_1_hierarchy.webp', (530, 901), [
    ('Kingdom', [170, 12, 190, 52]), ('Phylum or Division', [70, 148, 390, 56]), ('Class', [202, 285, 126, 54]),
    ('Order', [198, 422, 136, 54]), ('Family', [190, 557, 152, 58]), ('Genus', [192, 694, 146, 58])], printed=True)
d.basic('Which sequence of categories is correct?<br>(a) Species, Order, Phylum, Kingdom<br>(b) Genus, Species, Order, Kingdom<br>(c) Species, Genus, Order, Phylum',
        T('(a) and (c)') + ' both run upwards correctly; ' + X('(b)') + ' is wrong: species comes below genus')

d.sec('1.2.1-species')
d.basic('What is a species, taxonomically?', 'A group of individual organisms with ' + T('fundamental similarities'))
d.basic('How is one species told apart from a closely related species?', 'By distinct ' + T('morphological differences'))
d.cloze('In <i>Mangifera indica</i>, <i>Solanum tuberosum</i> and <i>Panthera leo</i>, the specific epithets are {{c1::<i>indica</i>, <i>tuberosum</i> and <i>leo</i>}}.')
d.basic('What is <i>Solanum tuberosum</i>?', E('Potato'))
d.basic('Name another species of <i>Panthera</i> besides <i>leo</i>.', EI('tigris') + ' (tiger)')
d.basic('Name two other species of <i>Solanum</i> besides <i>tuberosum</i>.', EI('nigrum') + ' and ' + EI('melongena'))
d.basic('What is the scientific name of human beings?', EI('Homo sapiens') + ' (genus ' + I('Homo') + ', species ' + I('sapiens') + ')')

d.sec('1.2.2-genus')
d.basic('What is a genus?', 'A group of ' + T('related species') + ' with more characters in common than with species of other genera')
d.basic('Potato and brinjal belong to which genus?', EI('Solanum'))
d.cloze('Lion ({{c1::<i>Panthera leo</i>}}), leopard ({{c2::<i>P. pardus</i>}}) and tiger ({{c3::<i>P. tigris</i>}}) are species of the genus <i>Panthera</i>.')
d.basic('Which genus includes cats, and differs from <i>Panthera</i>?', EI('Felis'))

d.sec('1.2.3-family')
d.basic('What is a family?', 'A group of ' + T('related genera') + ', with still fewer similarities than genus and species')
d.basic('On what basis are plant families characterised?', 'Both ' + T('vegetative') + ' and ' + T('reproductive') + ' features')
d.basic('<i>Solanum</i>, <i>Petunia</i> and <i>Datura</i> belong to which family?', T('Solanaceae'))
d.basic('<i>Panthera</i> and <i>Felis</i> are put together in which family?', T('Felidae'))
d.basic('Cats and dogs are placed in which two families?', 'Cat: ' + T('Felidae') + '. Dog: ' + T('Canidae') + '.')

d.sec('1.2.4-order')
d.basic('What is an order?', 'An assemblage of ' + T('families') + ' that show a few similar characters')
d.basic('On what are order and higher categories identified?', T('Aggregates of characters'))
d.basic('Convolvulaceae and Solanaceae are placed in which order, and on what basis?', T('Polymoniales') + ', mainly on ' + T('floral characters'))
d.basic('Which animal order includes the families Felidae and Canidae?', T('Carnivora'))

d.sec('1.2.5-class')
d.basic('What does the category class include?', 'Related ' + T('orders'))
d.basic('Monkey, gorilla and gibbon belong to which order?', T('Primata'))
d.basic('Orders Primata and Carnivora are placed in which class?', T('Mammalia'))

d.sec('1.2.6-phylum')
d.basic('Fishes, amphibians, reptiles, birds and mammals form which phylum?', T('Chordata'))
d.basic('Which common features place animals in phylum Chordata?', 'A ' + T('notochord') + ' and a ' + T('dorsal hollow neural system'))
d.basic('In plants, what are classes with a few similar characters assigned to?', 'A ' + T('Division'))

d.sec('1.2.7-kingdom')
d.basic('To which kingdom are all animals of the various phyla assigned?', T('Animalia') + ', the highest category')
d.basic('What does Kingdom Plantae comprise?', 'All plants from the various ' + T('divisions'))
d.basic('Why have taxonomists developed sub-categories in the hierarchy?', 'For a more sound and scientific ' + T('placement') + ' of the various taxa')
d.cloze('Going up from species to kingdom, the number of common characteristics {{c1::decreases}}.')
d.basic('The lower the taxon, the ___ characteristics its members share.', T('More'))
d.basic('Why does classification get harder at higher categories?', 'It is more difficult to determine the ' + T('relationship') + ' to other taxa at the same level')

# ---------------------------------------------------------------- Table 1.1
d.sec('table-1.1')
sc.taxon_ladder(d, 'Man', ['Animalia', 'Chordata', 'Mammalia', 'Primata', 'Hominidae', 'Homo', 'Homo sapiens'], italic=(5, 6))
sc.taxon_ladder(d, 'Housefly', ['Animalia', 'Arthropoda', 'Insecta', 'Diptera', 'Muscidae', 'Musca', 'Musca domestica'], italic=(5, 6))
sc.taxon_ladder(d, 'Mango', ['Plantae', 'Angiospermae', 'Dicotyledonae', 'Sapindales', 'Anacardiaceae', 'Mangifera', 'Mangifera indica'], italic=(5, 6))
sc.taxon_ladder(d, 'Wheat', ['Plantae', 'Angiospermae', 'Monocotyledonae', 'Poales', 'Poaceae', 'Triticum', 'Triticum aestivum'], italic=(5, 6))
table_card(d, 'Table 1.1 · Family', 'Which family does each belong to?', [
    ('Man', 'Hominidae', False), ('Housefly', 'Muscidae', False), ('Mango', 'Anacardiaceae', False), ('Wheat', 'Poaceae', False)],
    term='Table 1.1: families')
table_card(d, 'Table 1.1 · Order', 'Which order does each belong to?', [
    ('Man', 'Primata', False), ('Housefly', 'Diptera', False), ('Mango', 'Sapindales', False), ('Wheat', 'Poales', False)],
    term='Table 1.1: orders')
table_card(d, 'Table 1.1 · Class', 'Which class does each belong to?', [
    ('Man', 'Mammalia', False), ('Housefly', 'Insecta', False), ('Mango', 'Dicotyledonae', False), ('Wheat', 'Monocotyledonae', False)],
    term='Table 1.1: classes')
d.basic('What is the biological name of the housefly?', EI('Musca domestica'))
d.basic('What is the biological name of wheat?', EI('Triticum aestivum'))
d.basic('Diptera is the order of which organism in Table 1.1?', E('Housefly'))
d.basic('Anacardiaceae is the family of which organism?', E('Mango'))
d.basic('Which two organisms of Table 1.1 share the division Angiospermae?', E('Mango') + ' and ' + E('wheat'))

os.makedirs(OUT, exist_ok=True)
n = d.write(os.path.join(OUT, 'deck.json'))
print('notes', n)
