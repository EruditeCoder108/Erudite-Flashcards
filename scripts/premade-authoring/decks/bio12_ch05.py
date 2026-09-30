import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch05-molecular-basis-of-inheritance')
d = Deck('Chapter 5: Molecular Basis of Inheritance', 'Class 12', ['class-12', 'biology', 'ch-5'])
d.description = 'DNA structure and packaging, search for genetic material, replication, transcription, genetic code, translation, lac operon, HGP and DNA fingerprinting'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}
NU, TU, LAC = (1001, 992), (1001, 303), (1000, 726)

# ---------------------------------------------------------------- intro
d.sec('5.0-intro')
d.basic('Two types of nucleic acids?', T('DNA') + ' (deoxyribonucleic acid) and ' + T('RNA') + ' (ribonucleic acid)')
d.basic('Functions of RNA besides genetic material in some viruses?', T('Messenger') + ', ' + T('adapter') + ', ' + T('structural') + ' and sometimes ' + T('catalytic') + ' molecule')

# ---------------------------------------------------------------- 5.1 DNA
d.sec('5.1-the-dna')
d.basic('How is the length of DNA usually defined?', 'As the number of ' + T('nucleotides') + ' (or base pairs); characteristic of an organism')
table_card(d, 'DNA length', 'Size?', [
    ('Bacteriophage φ×174', '5386 nucleotides', False), ('Bacteriophage lambda', '48502 bp', False),
    ('E. coli', '4.6 × 10⁶ bp', False), ('Human (haploid)', '3.3 × 10⁹ bp', False)], term='Genome sizes')
d.sec('5.1.1-polynucleotide-chain')
d.basic('Three components of a nucleotide?', 'A ' + T('nitrogenous base') + ', a ' + T('pentose sugar') + ' (ribose/deoxyribose), a ' + T('phosphate group'))
d.cloze('Purines: {{c1::adenine and guanine}}. Pyrimidines: {{c2::cytosine, uracil and thymine}}.')
d.basic('Which base is only in DNA, and which only in RNA?', T('Thymine') + ' in DNA; ' + T('uracil') + ' in RNA (cytosine in both)')
d.basic('Mnemonic for purines?', '"' + T('Pure As Gold') + '": purines are Adenine, Guanine (two rings)')
d.basic('Nucleoside vs nucleotide?', T('Nucleoside') + ' = base + sugar (N-glycosidic bond)<br>' + T('Nucleotide') + ' = nucleoside + phosphate (phosphoester bond at 5′-OH)')
d.basic('Bond linking base to sugar?', T('N-glycosidic linkage') + ' to the OH of 1′ C of pentose')
d.basic('Bond joining two nucleotides?', T('3′–5′ phosphodiester linkage'))
d.basic('Group nucleosides and bases: adenine, cytidine, thymine, guanosine, uracil, cytosine (Exercise 1).', T('Bases') + ': adenine, thymine, uracil, cytosine. ' + T('Nucleosides') + ': cytidine, guanosine.')
d.basic('5′-end vs 3′-end of a polynucleotide?', T('5′-end') + ': free phosphate on 5′ C of sugar. ' + T('3′-end') + ': free OH on 3′ C of sugar.', **fig('fig_5_1_polynucleotide'))
d.basic('What forms the backbone of a polynucleotide?', T('Sugar and phosphate') + '; bases project from it')
d.basic('Two chemical differences of RNA from DNA?', 'Extra ' + T('2′-OH') + ' on ribose; ' + T('uracil') + ' instead of thymine (thymine = 5-methyl uracil)')
d.basic('Who first identified DNA, when, and what name?', T('Friedrich Miescher') + ', ' + N('1869') + ', named it "' + T('Nuclein') + '"')
d.basic('Correction: NCERT spells the discoverer "Meischer". Correct spelling?', T('Miescher') + ' (Johann Friedrich Miescher)')
d.basic('Who proposed the double helix and on what data?', T('Watson and Crick') + ' (' + N('1953') + '), using X-ray diffraction data of ' + T('Maurice Wilkins and Rosalind Franklin'))
d.basic('Chargaff’s rule?', 'In double-stranded DNA, ' + T('A/T = G/C = 1') + ' (A = T, G = C)')
d.basic('What does complementarity allow?', 'Knowing one strand predicts the other; each strand can template an identical daughter DNA')
d.basic('Backbone and bases in the double helix?', 'Sugar-phosphate backbone ' + T('outside') + '; bases project ' + T('inside'), **fig('fig_5_2_double_strand'))
d.basic('What does antiparallel polarity mean?', 'If one chain is ' + T('5′→3′') + ', the other is ' + T('3′→5′'))
d.cloze('A pairs with T by {{c1::two}} H-bonds; G pairs with C by {{c2::three}} H-bonds.')
d.basic('Why is the distance between the two strands constant?', 'A ' + T('purine') + ' always pairs with a ' + T('pyrimidine') + ' (2 rings + 1 ring)')
d.cloze('DNA helix is {{c1::right}}-handed; pitch {{c2::3.4 nm}}; about {{c3::10}} bp per turn; distance between bp {{c4::0.34 nm}}.')
d.basic('What stabilises the helix besides H-bonds?', T('Stacking') + ' of base-pair planes over one another', **fig('fig_5_3_double_helix'))
d.basic('Why is GC-rich DNA harder to melt? (intuition)', 'Each G≡C pair has ' + T('three') + ' H-bonds vs two for A=T, so more energy is needed to separate strands')
steps_card(d, 'Exercise 2', 'DNA has 20% cytosine. % adenine?', 'Use Chargaff: C = G, A = T, total 100%.',
           ['C = 20% so G = 20%', 'A + T = 100 − 40 = 60%', 'A = T, so A = <b>30%</b>'], 2, 'Chargaff calculation: 20% C → A?', 'A = 30%')
d.basic('Complement of 5′-ATGCATGC-3′, written 5′→3′ (Exercise 3)?', '5′-' + T('GCATGCAT') + '-3′ (reverse complement)')
d.basic('What is the central dogma?', 'Proposed by ' + T('Crick') + ': information flows ' + T('DNA → RNA → Protein'), **fig('fig_5_x_central_dogma'))
d.basic('Reverse flow RNA → DNA in some viruses is called?', T('Reverse transcription') + ' (e.g. retroviruses like HIV)')

d.sec('5.1.2-packaging')
d.basic('Length of DNA in a typical mammalian cell?', '\\( 6.6 \\times 10^{9} \\) bp × \\( 0.34 \\times 10^{-9} \\) m ≈ ' + N('2.2 m') + ', vs nucleus ~\\( 10^{-6} \\) m')
steps_card(d, 'Try it', 'E. coli DNA is 1.36 mm long. How many bp?', 'Length ÷ distance per bp.',
           ['1.36 mm = 1.36 × 10⁻³ m', 'bp = 1.36 × 10⁻³ / 0.34 × 10⁻⁹', '= <b>4 × 10⁶ bp</b>'], 2, 'E. coli bp from length', '4 × 10⁶ bp')
d.basic('How is DNA held in prokaryotes?', 'Negatively charged DNA held by positive proteins in the ' + T('nucleoid') + ', organised in large loops')
d.basic('What are histones?', 'Positively charged, ' + T('basic proteins') + ' rich in ' + T('lysine and arginine'))
d.basic('What is a histone octamer?', 'A unit of ' + N('eight') + ' histone molecules')
d.basic('What is a nucleosome?', 'Negatively charged DNA wrapped around a positively charged ' + T('histone octamer') + '; contains ~' + N('200 bp'))
d.occlusion('Figure 5.4a · Nucleosome', M + 'fig_5_4a_nucleosome.webp', NU, [
    ('DNA', wbox(72, 258, 182, 296, NU), True), ('H1 histone', wbox(492, 240, 752, 280, NU), True),
    ('Histone octamer', wbox(788, 534, 974, 618, NU), True), ('Core of histone molecules', wbox(50, 892, 656, 936, NU), True)])
d.basic('How does chromatin look under EM?', '"' + T('Beads-on-string') + '" (nucleosomes = beads)', **fig('fig_5_4b_beads_on_string'))
d.basic('How many nucleosomes in a mammalian cell? (think)', '\\( 6.6 \\times 10^{9} \\) bp ÷ 200 bp ≈ ' + N('3.3 × 10⁷') + ' nucleosomes')
d.basic('Packaging hierarchy?', 'DNA → nucleosome → beads-on-string → ' + T('chromatin fibres') + ' → condensed ' + T('chromosomes') + ' at metaphase')
d.basic('Proteins for higher-level packaging?', T('Non-histone chromosomal (NHC) proteins'))
d.basic('Euchromatin vs heterochromatin?', T('Euchromatin') + ': loosely packed, stains light, transcriptionally ' + T('active') + '<br>' + T('Heterochromatin') + ': dense, stains dark, ' + X('inactive'))

# ---------------------------------------------------------------- 5.2 Search for genetic material
d.sec('5.2-search-for-genetic-material')
d.basic('By 1926, the search for genetic material was narrowed to?', 'The ' + T('chromosomes') + ' in the nucleus')
d.basic('Griffith’s experiment: organism and year?', EI('Streptococcus pneumoniae') + ', ' + N('1928'))
d.basic('S strain vs R strain?', T('S') + ': smooth shiny colonies, polysaccharide coat, ' + X('virulent') + '. ' + T('R') + ': rough, no coat, non-virulent.')
table_card(d, 'Griffith 1928', 'Mice?', [
    ('Live S strain', 'Die', True), ('Live R strain', 'Live', False), ('Heat-killed S', 'Live', False),
    ('Heat-killed S + live R', 'Die (live S recovered)', True)], term='Griffith’s transformation experiment')
d.basic('Griffith’s conclusion?', 'R strain was ' + T('transformed') + ' by a "' + T('transforming principle') + '" from heat-killed S; its chemical nature ' + X('not defined'))
d.basic('Who identified the transforming principle and when?', T('Avery, MacLeod and McCarty') + ' (' + N('1933–44') + ')')
d.basic('What was the genetic material thought to be before Avery?', 'A ' + T('protein'))
d.basic('Enzyme evidence of Avery et al.?', 'Proteases and RNases ' + X('did not') + ' stop transformation; ' + T('DNase') + ' did → DNA is the transforming principle')
d.basic('DNAs vs DNase?', T('DNAs') + ' = plural of DNA (molecules). ' + T('DNase') + ' = enzyme that digests DNA.')
d.sec('5.2.1-hershey-chase')
d.basic('Who gave unequivocal proof that DNA is genetic material, and when?', T('Alfred Hershey and Martha Chase') + ' (' + N('1952') + '), using bacteriophages')
d.basic('How did Hershey and Chase label DNA vs protein? (Exercise 7)', 'DNA with radioactive ' + T('phosphorus (³²P)') + ' (DNA has P, protein doesn’t); protein with radioactive ' + T('sulfur (³⁵S)'))
d.cloze('Hershey–Chase steps: {{c1::infection}} → {{c2::blending}} (removes viral coats) → {{c3::centrifugation}} (separates bacteria from virus).')
d.basic('Hershey–Chase results?', 'Bacteria with ' + T('³²P') + ' were radioactive; ³⁵S stayed in the ' + T('supernatant') + ' → DNA enters bacteria', **fig('fig_5_5_hershey_chase'))
d.basic('Mnemonic: which isotope went where?', '"' + T('P goes in, S stays out') + '": ³²P (DNA) inside bacteria; ³⁵S (protein coat) in supernatant')

d.sec('5.2.2-dna-vs-rna')
d.basic('Examples of RNA as genetic material?', E('Tobacco Mosaic Virus') + ', ' + E('Qβ bacteriophage'))
d.cloze('Criteria for genetic material: {{c1::replication}}, {{c2::chemical and structural stability}}, scope for slow changes ({{c3::mutation}}), and {{c4::expression as Mendelian characters}}.')
d.basic('Why can’t proteins be genetic material?', 'They fail the first criterion: they cannot ' + X('replicate') + ' themselves')
d.basic('Evidence of DNA stability in Griffith’s experiment?', 'Heat killed bacteria but did not destroy the genetic material: separated DNA strands re-anneal')
d.basic('Why is RNA less stable than DNA?', T('2′-OH') + ' is reactive, making RNA labile; RNA is also ' + T('catalytic') + ' (reactive)')
d.basic('What extra stability does thymine give DNA?', 'Thymine in place of uracil confers additional stability (linked to ' + T('DNA repair') + ')')
d.basic('Why do RNA viruses evolve faster?', 'RNA is unstable and ' + T('mutates faster') + '; short life span')
d.basic('Why is RNA better at expression?', 'RNA can ' + T('directly code') + ' for proteins; DNA depends on RNA')
d.basic('DNA vs RNA for storage vs transmission?', T('DNA') + ': storage (stable). ' + T('RNA') + ': transmission of information.')

# ---------------------------------------------------------------- 5.3 RNA world
d.sec('5.3-rna-world')
d.basic('Which was the first genetic material?', T('RNA'))
d.basic('Evidence for an RNA world?', 'Essential processes (metabolism, translation, splicing) evolved around RNA; RNA acts as ' + T('catalyst') + ' (ribozymes)')
d.basic('Why did DNA evolve from RNA?', 'RNA was reactive and unstable; DNA has chemical modifications for ' + T('stability') + ', a complementary strand and ' + T('repair'))

# ---------------------------------------------------------------- 5.4 Replication
d.sec('5.4-replication')
d.basic('Famous Watson–Crick quote on replication?', '"It has not escaped our notice that the specific pairing… suggests a possible copying mechanism"')
d.basic('What is semiconservative replication?', 'Each daughter DNA has ' + T('one parental') + ' and ' + T('one new') + ' strand', **fig('fig_5_6_semiconservative'))
d.basic('Property of DNA that suggested semiconservative replication (Exercise 5)?', 'Complementary ' + T('base pairing') + ' of antiparallel strands: each strand can template the other')
d.sec('5.4.1-experimental-proof')
d.basic('Who proved semiconservative replication, when, in what?', T('Meselson and Stahl') + ', ' + N('1958') + ', ' + EI('E. coli'))
d.basic('Meselson–Stahl: heavy nitrogen source?', '\\( ^{15}NH_4Cl \\) as the only N source for many generations')
d.basic('How were heavy and light DNA separated?', 'Centrifugation in a ' + T('CsCl density gradient'), **fig('fig_5_7_meselson_stahl'))
d.basic('Is ¹⁵N radioactive?', X('No') + '; it is a heavy isotope, separated from ¹⁴N only by density')
d.cloze('After transfer to ¹⁴N: generation I (20 min) = all {{c1::hybrid}} DNA; generation II (40 min) = {{c2::equal hybrid and light}} DNA.')
d.basic('Meselson–Stahl: after 80 min (4 generations)?', N('1/8 hybrid') + ' : ' + N('7/8 light') + ' (2 hybrid out of 16 molecules)')
d.basic('Why did the first generation rule out conservative replication? (intuition)', 'Conservative would give one heavy + one light band.<br>A single ' + T('hybrid') + ' band means each molecule kept one old strand')
d.basic('Who showed semiconservative replication in chromosomes?', T('Taylor') + ' and colleagues (' + N('1958') + '), ' + EI('Vicia faba') + ', using radioactive thymidine')
d.sec('5.4.2-machinery')
d.basic('Main enzyme of replication?', T('DNA-dependent DNA polymerase'))
d.basic('Replication speed in E. coli?', N('4.6 × 10⁶') + ' bp in ' + N('18 min') + ': about ' + N('2000 bp/s'))
d.basic('Dual role of deoxyribonucleoside triphosphates?', T('Substrates') + ' and ' + T('energy source') + ' (two terminal high-energy phosphates)')
d.basic('What is a replication fork?', 'A small opening of the helix where replication occurs (strands can’t separate fully: too much energy)', **fig('fig_5_8_replication_fork'))
d.basic('Direction of DNA polymerase activity?', 'Only ' + T('5′ → 3′'))
d.basic('Leading vs lagging strand synthesis?', 'On template ' + T('3′→5′') + ': ' + T('continuous') + '. On template ' + T('5′→3′') + ': ' + T('discontinuous') + '.')
d.basic('Enzyme joining discontinuous fragments?', T('DNA ligase') + ' (fragments are Okazaki fragments)')
d.basic('Can DNA polymerase start replication on its own?', X('No') + '; it needs an ' + T('origin of replication') + ' (and a primer)')
d.basic('What is the origin of replication?', 'A definite region in DNA where replication ' + T('originates'))
d.basic('Why do cloned DNA pieces need a vector?', 'Vectors provide the ' + T('origin of replication'))
d.basic('When does eukaryotic DNA replicate?', 'In the ' + T('S-phase') + ' of the cell cycle')
d.basic('Result of DNA replication without cell division?', T('Polyploidy'))

# ---------------------------------------------------------------- 5.5 Transcription
d.sec('5.5-transcription')
d.basic('Define transcription.', 'Copying genetic information from ' + T('one strand of DNA into RNA'))
d.basic('Base-pairing difference in transcription?', 'Adenine pairs with ' + T('uracil') + ' instead of thymine')
d.basic('Replication vs transcription in extent?', 'Replication copies ' + T('whole DNA') + '; transcription copies ' + T('only a segment') + ' and only ' + T('one strand'))
d.basic('Why are both strands not transcribed? (two reasons)', '1) One segment would code ' + T('two different proteins') + '. 2) The two RNAs would pair into ' + X('dsRNA') + ' and not be translated.')
d.sec('5.5.1-transcription-unit')
d.cloze('A transcription unit has a {{c1::promoter}}, a {{c2::structural gene}} and a {{c3::terminator}}.')
d.basic('Template strand vs coding strand?', T('Template') + ': 3′→5′, read by RNA polymerase<br>' + T('Coding') + ': 5′→3′, same sequence as RNA (T for U), displaced; codes for nothing')
d.basic('Reference strand for defining a transcription unit?', 'The ' + T('coding strand'))
d.basic('Coding strand 5′-ATGCATGC-3′: mRNA? (Exercise 4)', '5′-' + T('AUGCAUGC') + '-3′ (same as coding strand, U for T)')
d.basic('Where is the promoter, and what does it do?', 'Towards the ' + T('5′-end (upstream)') + ' of the structural gene; binding site for ' + T('RNA polymerase') + '; defines template and coding strands')
d.basic('Where is the terminator?', 'Towards the ' + T('3′-end (downstream)') + ' of the coding strand; defines end of transcription')
d.basic('What happens if promoter and terminator swap positions?', 'The definition of ' + T('template and coding strands reverses'))
d.occlusion('Figure 5.9 · Transcription unit', M + 'fig_5_9_transcription_unit.webp', TU, [
    ('Transcription start site', wbox(262, 46, 504, 70, TU), True), ('Promoter', wbox(154, 104, 252, 126, TU), True),
    ('Structural gene', wbox(324, 120, 488, 142, TU), True), ('Template strand', wbox(534, 120, 706, 142, TU), True),
    ('Terminator', wbox(746, 104, 864, 126, TU), True), ('Coding strand', wbox(558, 212, 706, 236, TU), True)])
d.sec('5.5.2-transcription-unit-and-gene')
d.basic('Define a gene (NCERT).', 'The ' + T('functional unit of inheritance'))
d.basic('What is a cistron?', 'A segment of DNA coding for a ' + T('polypeptide'))
d.basic('Monocistronic vs polycistronic?', T('Monocistronic') + ': mostly eukaryotes. ' + T('Polycistronic') + ': mostly bacteria/prokaryotes.')
d.basic('Exons vs introns?', T('Exons') + ': coding/expressed, appear in mature RNA. ' + T('Introns') + ': intervening, ' + X('absent') + ' from mature RNA.')
d.basic('What is a split gene?', 'Eukaryotic gene with coding sequences (exons) ' + T('interrupted by introns'))
d.basic('What are "regulatory genes" loosely?', 'Promoter and regulatory sequences that affect inheritance though they ' + X('code for no RNA or protein'))
d.sec('5.5.3-types-of-rna')
table_card(d, 'Bacterial RNAs', 'Role in protein synthesis?', [
    ('mRNA', 'Provides the template', False), ('tRNA', 'Brings amino acids, reads the code', False),
    ('rRNA', 'Structural and catalytic role', False)], term='mRNA vs tRNA vs rRNA')
d.basic('How many RNA polymerases in bacteria?', 'A ' + T('single') + ' DNA-dependent RNA polymerase for all RNAs')
d.cloze('Transcription steps: {{c1::initiation}} → {{c2::elongation}} → {{c3::termination}}.')
d.basic('Which step can RNA polymerase catalyse alone?', 'Only ' + T('elongation'))
d.basic('Factors for initiation and termination in bacteria?', T('σ (sigma)') + ' initiation factor; ' + T('ρ (rho)') + ' termination factor', **fig('fig_5_10_transcription_bacteria'))
d.basic('Why are transcription and translation coupled in bacteria?', 'mRNA needs ' + X('no processing') + ' and there is no nucleus: both occur in the same compartment')
table_card(d, 'Eukaryotic RNA polymerases', 'Transcribes?', [
    ('RNA polymerase I', 'rRNAs (28S, 18S, 5.8S)', False), ('RNA polymerase II', 'hnRNA (precursor of mRNA)', False),
    ('RNA polymerase III', 'tRNA, 5S rRNA, snRNAs', False)], term='Eukaryotic RNA polymerases')
d.basic('Mnemonic for eukaryotic RNA polymerases?', '"' + T('R-M-T') + '" = I: rRNA, II: mRNA, III: tRNA (1-2-3 like "Ribosome Makes Tea")')
d.basic('What is splicing?', 'Removal of ' + T('introns') + ' and joining of ' + T('exons') + ' in a defined order', **fig('fig_5_11_transcription_eukaryotes'))
d.basic('What is capping?', 'Adding an unusual nucleotide, ' + T('methyl guanosine triphosphate') + ', to the ' + T('5′-end') + ' of hnRNA')
d.basic('What is tailing?', 'Adding ' + N('200–300') + ' adenylate residues at the ' + T('3′-end') + ', template-independently')
d.basic('What leaves the nucleus for translation?', 'Fully processed hnRNA = ' + T('mRNA'))
d.basic('Significance of split genes and splicing?', 'Introns are reminiscent of ' + T('antiquity') + '; splicing reflects dominance of the ' + T('RNA world'))

# ---------------------------------------------------------------- 5.6 Genetic code
d.sec('5.6-genetic-code')
d.basic('Why was a genetic code needed for translation?', 'No complementarity exists between ' + T('nucleotides and amino acids'))
d.basic('Who argued the code must be a triplet?', T('George Gamow') + ' (physicist): 4 bases for 20 amino acids → \\( 4^3 = 64 \\) codons')
d.basic('Contribution of Har Gobind Khorana?', 'Chemical method to synthesise RNA with defined base combinations (' + T('homopolymers, copolymers') + ')')
d.basic('Contribution of Marshall Nirenberg?', T('Cell-free system') + ' for protein synthesis that deciphered the code')
d.basic('Contribution of Severo Ochoa?', 'Enzyme ' + T('polynucleotide phosphorylase') + ': template-independent RNA synthesis')
d.basic('Read the checkerboard (Table 5.1).', 'Codons read first (left), second (top), third (right) position; e.g. UUU = Phe, AUG = Met', **img('table_5_1_codons'))
d.basic('How many codons code amino acids, and how many stop?', N('61') + ' code amino acids; ' + N('3') + ' are stop codons')
d.basic('Why is the code "degenerate"?', 'Some amino acids are coded by ' + T('more than one codon'))
d.basic('What does "no punctuation" mean?', 'Codons are read ' + T('contiguously') + ' in mRNA')
d.basic('Why is the code "nearly universal"?', 'UUU = Phe from bacteria to humans; ' + X('exceptions') + ' in mitochondria and some protozoans')
d.basic('Dual function of AUG?', 'Codes ' + T('methionine') + ' and acts as the ' + T('initiator codon'))
d.basic('Stop codons?', T('UAA, UAG, UGA'))
d.basic('Mnemonic for stop codons?', '"' + T('U Are Away, U Are Gone, U Go Away') + '": UAA, UAG, UGA')
d.basic('Translate: AUG UUU UUC UUC UUU UUU UUC', T('Met-Phe-Phe-Phe-Phe-Phe-Phe'))
d.basic('Why can’t you uniquely predict mRNA from Met-Phe-Phe…?', 'The code is ' + T('degenerate') + ' (Phe = UUU or UUC)')
d.sec('5.6.1-mutations-and-code')
d.basic('Point mutation in sickle-cell anaemia (Ch 5 view)?', 'Single bp change in β-globin gene: ' + T('glutamate → valine'))
d.basic('RAM HAS RED CAP: insert B → ?', 'RAM HAS ' + X('BRE DCA P') + ': reading frame shifts from the insertion point')
d.basic('Insert BIG into RAM HAS RED CAP → ?', 'RAM HAS BIG RED CAP: one extra codon, ' + T('frame unchanged'))
d.basic('What are frameshift mutations?', 'Insertion or deletion of ' + T('one or two') + ' bases, changing the reading frame downstream')
d.basic('Effect of inserting/deleting three bases?', 'Adds/removes ' + T('one codon (one amino acid)') + '; reading frame ' + T('unaltered'))
d.sec('5.6.2-trna')
d.basic('Who postulated an adapter molecule?', T('Francis Crick'))
d.basic('Earlier name of tRNA?', T('sRNA (soluble RNA)'))
d.basic('Two key parts of tRNA?', T('Anticodon loop') + ' (complementary to codon) and ' + T('amino acid acceptor end'), **fig('fig_5_12_trna'))
d.basic('Is there a tRNA for stop codons?', X('No'))
d.basic('Special tRNA for initiation?', T('Initiator tRNA'))
d.basic('Secondary vs actual 3D shape of tRNA?', 'Secondary: ' + T('clover-leaf') + '. 3D: compact ' + T('inverted L') + '.')
d.basic('Read Figure 5.12: anticodon UCA pairs with codon?', T('AGU') + ' (Ser)', **img('fig_5_12_trna'))

# ---------------------------------------------------------------- 5.7 Translation
d.sec('5.7-translation')
d.basic('Define translation.', 'Polymerisation of ' + T('amino acids') + ' into a polypeptide, in the order set by mRNA bases', **fig('fig_5_13_translation'))
d.basic('What is charging (aminoacylation) of tRNA?', 'Amino acids are ' + T('activated with ATP') + ' and linked to their cognate tRNA')
d.basic('Why is charging needed?', 'Peptide bond formation needs ' + T('energy') + '; charged tRNAs close together favour it energetically')
d.basic('Composition of a ribosome?', 'Structural RNAs and about ' + N('80') + ' different proteins; two subunits (large and small)')
d.basic('When does translation begin?', 'When the ' + T('small subunit') + ' encounters an mRNA')
d.basic('Ribozyme in bacterial ribosome?', T('23S rRNA') + ': catalyses peptide bond formation')
d.basic('Two roles of ribosome in translation (Exercise 9)?', 'Provides ' + T('sites') + ' (in the large subunit) for tRNAs to bind; ' + T('catalyses') + ' peptide bond (23S rRNA)')
d.basic('What is a translational unit?', 'mRNA sequence flanked by the ' + T('start codon (AUG)') + ' and a ' + T('stop codon') + ', coding a polypeptide')
d.basic('What are UTRs?', T('Untranslated regions') + ' at the 5′-end (before start codon) and 3′-end (after stop codon).<br>They are needed for efficient translation')
d.basic('Steps of translation?', T('Initiation') + ': ribosome binds AUG with initiator tRNA<br>' + T('Elongation') + ': charged tRNAs pair by anticodon, amino acids added codon by codon<br>' + T('Termination') + ': release factor binds stop codon')
d.basic('Correction: NCERT says "5srRNA". Standard notation?', T('5S rRNA') + ' (S = Svedberg unit)')

# ---------------------------------------------------------------- 5.8 Regulation
d.sec('5.8-regulation')
d.cloze('Eukaryotic gene regulation levels: {{c1::transcriptional}}, {{c2::processing (splicing)}}, {{c3::mRNA transport}} from nucleus to cytoplasm, {{c4::translational}}.')
d.basic('What regulates gene expression, in simple terms?', 'Metabolic, physiological or environmental conditions')
d.basic('Predominant control point in prokaryotes?', 'Rate of ' + T('transcriptional initiation'))
d.basic('Activators vs repressors?', 'Regulatory proteins acting ' + T('positively') + ' (activators) or ' + T('negatively') + ' (repressors)')
d.basic('What is an operator?', 'Sequence adjacent to the promoter that binds a ' + T('repressor') + '; each operon has its specific operator and repressor')
d.sec('5.8.1-lac-operon')
d.basic('Who elucidated the lac operon?', T('François Jacob') + ' (geneticist) and ' + T('Jacques Monod') + ' (biochemist): first transcriptionally regulated system')
d.basic('What is an operon?', 'A ' + T('polycistronic structural gene') + ' regulated by a common promoter and regulatory genes')
d.basic('Examples of operons?', E('lac, trp, ara, his, val'))
d.basic('What does "i" in the i gene stand for?', T('Inhibitor') + ' (' + X('not') + ' inducer); codes for the ' + T('repressor'))
table_card(d, 'Lac operon', 'Codes for?', [
    ('i gene', 'Repressor', False), ('z gene', 'β-galactosidase (lactose → galactose + glucose)', False),
    ('y gene', 'Permease (entry of β-galactosides)', False), ('a gene', 'Transacetylase', False)], term='Genes of the lac operon')
d.basic('Inducer of the lac operon?', T('Lactose') + ' (or allolactose)')
d.basic('Lac operon without inducer?', 'Repressor (made constitutively) binds the ' + T('operator') + ' → RNA polymerase blocked → ' + X('no transcription'))
d.basic('Lac operon with inducer?', 'Inducer ' + T('inactivates the repressor') + ' → RNA polymerase transcribes z, y, a')
d.occlusion('Figure 5.14 · Lac operon', M + 'fig_5_14_lac_operon.webp', LAC, [
    ('i (regulator) gene', wbox(186, 48, 222, 80, LAC)), ('Operator (o)', wbox(330, 32, 364, 94, LAC)),
    ('Repressor', wbox(142, 288, 256, 314, LAC), True), ('lac mRNA', wbox(438, 454, 562, 478, LAC), True),
    ('β-galactosidase', wbox(340, 546, 512, 574, LAC), True), ('Permease', wbox(524, 544, 634, 572, LAC), True),
    ('Transacetylase', wbox(636, 544, 798, 572, LAC), True), ('Inducer', wbox(18, 598, 106, 624, LAC), True),
    ('Inactive repressor', wbox(98, 662, 312, 690, LAC), True)])
d.basic('Why must lac operon be expressed at a very low level always?', 'Otherwise ' + T('lactose cannot enter') + ' the cell (needs permease)')
d.basic('Can glucose or galactose induce the lac operon?', X('No'))
d.basic('Why does the lac operon shut down some time after lactose is added? (Exercise 10)', 'Lactose is ' + T('used up') + '; free repressor again binds the operator')
d.basic('Lac operon regulation by repressor is called?', T('Negative regulation') + ' (it also has positive regulation, beyond scope)')
d.basic('The lac operon as "regulation of enzyme synthesis by its substrate": intuition?', 'The food (lactose) switches on the tools to digest it; no food, no tools: a ' + T('demand-driven') + ' factory')

# ---------------------------------------------------------------- 5.9 HGP
d.sec('5.9-human-genome-project')
d.basic('When was the Human Genome Project launched and completed?', 'Launched ' + N('1990') + '; completed ' + N('2003') + ' (13-year project)')
d.basic('Why was HGP a mega project? (Exercise 12)', '~\\( 3 \\times 10^{9} \\) bp at US $3/bp ≈ ' + N('$9 billion') + '; data would fill ' + N('3300') + ' books of 1000 pages; needed high-speed computing')
d.basic('New field closely associated with HGP?', T('Bioinformatics'))
d.basic('Goals of HGP?', 'Identify all ~' + N('20,000–25,000') + ' genes; sequence ' + N('3 billion') + ' bp; store in databases; improve analysis tools; transfer technology; address ' + T('ELSI'))
d.basic('What is ELSI?', T('Ethical, legal and social issues') + ' arising from the project')
d.basic('Who coordinated HGP?', 'U.S. ' + T('Department of Energy') + ' and ' + T('National Institutes of Health') + '; ' + T('Wellcome Trust') + ' (UK) major partner')
d.basic('Non-human organisms also sequenced?', 'Bacteria, yeast, ' + EI('Caenorhabditis elegans') + ', ' + EI('Drosophila') + ', rice, ' + EI('Arabidopsis'))
d.basic('Two approaches of HGP?', T('Expressed Sequence Tags (ESTs)') + ': genes expressed as RNA<br>' + T('Sequence annotation') + ': sequence everything, assign functions later')
d.basic('Hosts and vectors used in HGP?', 'Hosts: bacteria and yeast. Vectors: ' + T('BAC') + ' and ' + T('YAC') + '.')
d.basic('Sequencing method used in HGP?', 'Automated sequencers based on ' + T('Frederick Sanger') + '’s method (Sanger also sequenced proteins)', **fig('fig_5_15_hgp'))
d.basic('How were fragment sequences assembled?', 'By ' + T('overlapping regions') + ', aligned with specialised computer programs')
d.basic('Last chromosome to be sequenced?', T('Chromosome 1') + ', in May ' + N('2006'))
d.basic('How were genetic and physical maps assigned?', 'Polymorphism of ' + T('restriction endonuclease sites') + ' and repetitive sequences (' + T('microsatellites') + ')')
d.sec('5.9.1-salient-features')
table_card(d, 'Human genome', 'Value?', [
    ('Total size', '3164.7 million bp', False), ('Average gene', '3000 bases', False),
    ('Largest gene', 'Dystrophin, 2.4 million bases', False), ('Estimated genes', '~30,000', False),
    ('Coding for proteins', 'Less than 2%', False), ('SNP sites', '~1.4 million', False)], term='Salient features of the human genome')
d.basic('Chromosome with most and fewest genes?', 'Most: ' + T('chromosome 1') + ' (' + N('2968') + '). Fewest: ' + T('Y') + ' (' + N('231') + ').')
d.basic('% bases identical in all humans?', N('99.9%'))
d.basic('Functions unknown for what % of genes?', 'Over ' + N('50%'))
d.basic('What are repetitive sequences?', 'Stretches repeated hundreds to thousands of times; ' + X('no direct coding') + ' function; shed light on chromosome structure and evolution')
d.basic('What are SNPs and their promise?', T('Single nucleotide polymorphisms') + ' ("snips"): single-base differences.<br>They help locate disease sequences and trace human history')
d.basic('Correction: NCERT gives ~30,000 genes but also 20,000–25,000 in the goals. Current estimate?', 'About ' + N('20,000') + ' protein-coding genes; the 30,000 figure was an early estimate')
d.basic('Update: was the 2003 genome truly complete?', 'No; ~8% gaps remained. The ' + T('T2T consortium') + ' published the first gap-free human genome in ' + N('2022') + '.')
d.basic('Impact of the human genome sequence on research?', 'Study ' + T('all genes at once') + ' (e.g. all transcripts in a tissue or tumour) instead of one gene at a time')

# ---------------------------------------------------------------- 5.10 DNA fingerprinting
d.sec('5.10-dna-fingerprinting')
d.basic('Humans share 99.9% bases. How many differ in 3 × 10⁹ bp?', '0.1% = ' + N('3 × 10⁶') + ' bases')
d.basic('Correction: NCERT says "compare two sets of 3 × 10⁶ base pairs". Should be?', N('3 × 10⁹') + ' bp (whole genome); 3 × 10⁶ is the number that differ')
d.basic('What is DNA fingerprinting?', 'A quick way to compare DNA of individuals by differences in ' + T('repetitive DNA') + ' regions')
d.basic('What is satellite DNA?', 'Repetitive DNA separating as ' + T('small peaks') + ' from bulk DNA in density gradient centrifugation')
d.basic('Basis of satellite DNA classification?', 'Base composition (A:T or G:C rich), segment length, number of repeats: ' + T('micro-satellites, mini-satellites'))
d.basic('Repetitive DNA vs satellite DNA (Exercise 8a)?', T('Repetitive DNA') + ': any sequence repeated many times<br>' + T('Satellite DNA') + ': repetitive DNA seen as separate peaks in centrifugation; highly polymorphic')
d.basic('Why is DNA fingerprinting useful in forensics?', 'DNA from ' + T('every tissue') + ' (blood, hair follicle, skin, bone, saliva, sperm) shows the same polymorphism')
d.basic('Why is it used in paternity testing?', 'Polymorphisms are ' + T('inherited') + ' from parents')
d.basic('What is DNA polymorphism?', 'More than one allele at a locus with frequency ' + T('> 0.01') + ' in a population.<br>An inheritable mutation at high frequency')
d.basic('Why are polymorphisms commoner in non-coding DNA?', 'Mutations there have ' + X('no immediate effect') + ' on reproduction, so they accumulate')
d.basic('Who developed DNA fingerprinting?', T('Alec Jeffreys'))
d.basic('Probe used by Jeffreys?', T('VNTR') + ' (Variable Number of Tandem Repeats), a ' + T('mini-satellite'))
d.cloze('DNA fingerprinting steps: {{c1::isolation of DNA}} → {{c2::digestion by restriction endonucleases}} → {{c3::electrophoresis}} → {{c4::blotting}} onto nitrocellulose/nylon → {{c5::hybridisation}} with labelled VNTR probe → {{c6::autoradiography}}.')
d.basic('Hybridisation technique used in DNA fingerprinting?', T('Southern blot') + ' hybridisation with radiolabelled VNTR')
d.basic('Size range of VNTRs?', N('0.1 to 20 kb'))
d.basic('Who share identical DNA fingerprints?', T('Monozygotic (identical) twins'))
d.basic('How was sensitivity increased?', T('PCR') + ': DNA from a single cell suffices')
d.basic('Read Figure 5.16: crime-scene DNA matches whom?', T('Individual B') + ', not A', **img('fig_5_16_dna_fingerprinting'))
d.basic('Other applications of DNA fingerprinting (Exercise 13)?', 'Forensics, paternity, ' + T('population and genetic diversity') + ' studies')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Exercise 6', 'Polymerase type', [
    ('DNA template → DNA', 'DNA-dependent DNA polymerase', False), ('DNA template → RNA', 'DNA-dependent RNA polymerase', False),
    ('RNA template → DNA', 'RNA-dependent DNA polymerase (reverse transcriptase)', False),
    ('RNA template → RNA', 'RNA-dependent RNA polymerase (replicase)', False)], term='Types of nucleic acid polymerases')
table_card(d, 'Who did what', 'Discovery?', [
    ('Griffith', 'Transforming principle (1928)', False), ('Avery, MacLeod, McCarty', 'Transforming principle is DNA', False),
    ('Hershey & Chase', 'DNA is genetic material (1952)', False), ('Meselson & Stahl', 'Semiconservative replication (1958)', False),
    ('Jacob & Monod', 'Lac operon', False), ('Alec Jeffreys', 'DNA fingerprinting', False)], term='Key experiments in molecular genetics')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
