import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Biology', 'class12-biology-ch03-reproductive-health')
d = Deck('Chapter 3: Reproductive Health', 'Class 12', ['class-12', 'biology', 'ch-3'])
d.description = 'Reproductive health programmes, population and contraception, MTP, sexually transmitted infections, infertility and ART'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- intro
d.sec('3.0-intro')
d.basic('Reproductive health according to WHO?', 'Total well-being in all aspects of reproduction: ' + T('physical, emotional, behavioural and social'))
d.basic('When is a society called reproductively healthy?', 'People have physically and functionally normal reproductive organs and normal emotional and behavioural interactions in all sex-related aspects')

# ---------------------------------------------------------------- 3.1
d.sec('3.1-problems-and-strategies')
d.basic('India’s distinction in reproductive health programmes?', 'Among the ' + T('first countries') + ' to start national action plans for total reproductive health as a social goal')
d.basic('Name and year of India’s first programme?', T('Family planning') + ', started in ' + N('1951'))
d.basic('Current name of the improved programmes?', T('Reproductive and Child Health Care (RCH)') + ' programmes')
d.basic('Major tasks under RCH programmes?', 'Creating ' + T('awareness') + ' about reproduction-related aspects<br>Providing ' + T('facilities and support') + ' for a reproductively healthy society')
d.basic('Who spreads reproductive health awareness?', 'Government and non-government agencies (audio-visual and print media)<br>Parents, relatives, ' + T('teachers') + ' and friends')
d.basic('Why is sex education in schools encouraged? (Exercise 3)', 'Gives the young ' + T('right information') + ', discourages belief in myths and misconceptions about sex')
d.basic('Topics that help adolescents lead a reproductively healthy life?', 'Reproductive organs, adolescence and its changes, safe hygienic sexual practices, ' + T('STDs, AIDS'))
d.basic('What should fertile couples be educated about?', 'Birth control options<br>Care of pregnant mothers<br>Post-natal care<br>Breast feeding<br>' + T('Equal opportunities for male and female child'))
d.basic('What do reproductive health action plans need to succeed?', 'Strong ' + T('infrastructure') + ', professional expertise and material support')
d.basic('Reproduction-related problems needing medical care?', 'Pregnancy, delivery, STDs, abortions, contraception, menstrual problems, infertility')
d.basic('Two programmes that merit mention (NCERT)?', T('Statutory ban on amniocentesis for sex determination') + ' and ' + T('massive child immunisation'))
d.basic('What is amniocentesis?', 'Some ' + T('amniotic fluid') + ' of the developing foetus is taken to analyse fetal cells and dissolved substances')
d.basic('Legitimate uses of amniocentesis?', 'Test for genetic disorders: ' + E('Down syndrome, haemophilia, sickle-cell anaemia') + '<br>Determine survivability of the foetus')
d.basic('Why is amniocentesis for sex determination banned? (Exercise 8)', 'To check the menace of ' + X('female foeticide') + ' and a falling sex ratio')
d.basic('What is Saheli, and who developed it?', 'Oral contraceptive for females, developed at ' + T('CDRI, Lucknow'))
d.basic('Indicators of improved reproductive health in society? (Exercise 4)', 'Better awareness, more medically assisted deliveries, better post-natal care → lower ' + T('MMR and IMR') + '; small families; better STD detection and cure')
d.basic('Correction: NCERT prints "aminocentesis" and "haemoplilia" on p. 42. Correct spellings?', T('Amniocentesis') + ' and ' + T('haemophilia'))

# ---------------------------------------------------------------- 3.2
d.sec('3.2-population-and-birth-control')
d.basic('Why did population explode in the last century?', 'Better health facilities and living conditions')
d.cloze('World population: about {{c1::2 billion}} in 1900, about {{c2::6 billion}} by 2000, {{c3::7.2 billion}} in 2011.')
d.cloze('India’s population: about {{c1::350 million}} at independence, close to {{c2::1 billion}} by 2000, crossed {{c3::1.2 billion}} in May 2011.')
d.basic('Update: India’s population today?', 'About ' + N('1.4 billion') + '; India became the ' + T('most populous') + ' country in 2023 (UN estimate)')
d.basic('Probable reasons for population explosion? (Exercise 5)', 'Rapid decline in ' + T('death rate, MMR, IMR') + ' and increase in people of reproducible age')
d.basic('What are MMR and IMR?', T('Maternal mortality rate') + ' and ' + T('infant mortality rate'))
d.basic('Population growth rate per 2011 census?', 'Less than ' + N('2%') + ', i.e. ' + N('20/1000/year'))
d.basic('Danger of this growth rate?', 'Absolute scarcity of basic needs: ' + T('food, shelter, clothing'))
d.basic('Most important step to check population growth?', 'Motivate ' + T('smaller families') + ' using contraceptive methods')
d.basic('Slogan promoting small families?', E('Hum Do Hamare Do') + ' (we two, our two); many young urban couples adopt a ' + T('one child norm'))
d.basic('Legal marriageable ages set to check population?', 'Females ' + N('18') + ' years, males ' + N('21') + ' years')
d.basic('Features of an ideal contraceptive?', T('User-friendly, easily available, effective, reversible') + '<br>No or least side effects<br>Not interfering with sexual drive or act')
d.basic('Categories of contraceptive methods?', 'Natural/traditional, barrier, IUDs, oral contraceptives, injectables, implants, surgical')

d.basic('Principle of natural methods?', 'Avoid chances of ' + T('ovum and sperm meeting'))
d.basic('What is periodic abstinence?', 'Avoiding coitus from ' + N('day 10 to 17') + ' of the cycle, when ovulation is expected')
d.basic('Why are days 10–17 called the fertile period?', 'Chances of fertilisation are very high because ' + T('ovulation') + ' is expected then')
d.basic('What is coitus interruptus?', 'Withdrawal: male withdraws the penis just ' + T('before ejaculation') + ' to avoid insemination')
d.basic('What is lactational amenorrhea?', 'Absence of menstruation during ' + T('intense lactation') + ' after parturition: ovulation does not occur')
d.basic('For how long is lactational amenorrhea effective?', 'Up to a maximum of ' + N('six months') + ' after parturition, only with full breast-feeding')
d.basic('Pros and cons of natural methods?', 'Side effects almost ' + T('nil') + ' (no medicines/devices), but chances of ' + X('failure are high'))

d.basic('Principle of barrier methods?', 'Physically prevent ' + T('ovum and sperm from meeting'))
d.basic('What are condoms made of, and how do they work?', 'Thin ' + T('rubber/latex sheath') + ' covering the penis (male) or vagina and cervix (female).<br>Semen does not enter the female tract', **fig('fig_3_1a_male_condom'))
d.basic('Popular brand of male condom?', E('Nirodh'))
d.basic('Why has condom use increased?', 'Additional benefit: protection from ' + T('STIs and AIDS'))
d.basic('Other advantages of condoms?', 'Disposable, can be self-inserted, give ' + T('privacy') + ' to the user')
d.basic('Identify this contraceptive.', T('Female condom') + ' (Figure 3.1b)', **img('fig_3_1b_female_condom'))
d.basic('Diaphragms, cervical caps and vaults: how do they work?', 'Rubber barriers covering the ' + T('cervix') + ' during coitus, blocking sperm entry; ' + T('reusable'))
d.basic('What is used with these barriers to increase efficiency?', T('Spermicidal') + ' creams, jellies and foams')

d.basic('Who inserts IUDs and where?', 'Doctors or expert nurses, in the ' + T('uterus') + ' through the vagina')
table_card(d, 'IUDs', 'Example?', [
    ('Non-medicated', 'Lippes loop', False), ('Copper-releasing', 'CuT, Cu7, Multiload 375', False),
    ('Hormone-releasing', 'Progestasert, LNG-20', False)], term='Types of IUDs')
d.basic('Identify this device.', T('Copper T (CuT)') + ', a copper-releasing IUD', **img('fig_3_2_copper_t'))
d.basic('How do IUDs work?', 'Increase ' + T('phagocytosis of sperms') + ' in the uterus')
d.basic('How do copper ions in IUDs act?', 'Suppress ' + T('sperm motility') + ' and fertilising capacity')
d.basic('Extra action of hormone-releasing IUDs?', 'Make the uterus ' + T('unsuitable for implantation') + ' and the cervix ' + T('hostile to sperms'))
d.basic('For whom are IUDs ideal?', 'Females who want to ' + T('delay pregnancy and/or space children') + '; widely accepted in India')

d.basic('What are oral contraceptive pills made of?', 'Small doses of ' + T('progestogens') + ' or ' + T('progestogen–estrogen') + ' combinations')
d.basic('How are pills taken?', 'Daily for ' + N('21 days') + ', starting within the first ' + N('5 days') + ' of the cycle; gap of ' + N('7 days') + ' (menstruation), then repeat')
d.basic('How do pills prevent pregnancy?', 'Inhibit ' + T('ovulation') + ' and ' + T('implantation') + '; alter ' + T('cervical mucus') + ' to block sperm')
d.basic('Special features of Saheli?', T('Non-steroidal') + ', ' + T('once-a-week') + ' pill, very few side effects, high contraceptive value')
d.basic('Saheli’s active ingredient (beyond NCERT)?', T('Centchroman') + ' (ormeloxifene), a selective estrogen receptor modulator')
d.basic('Correct: "Oral pills are very popular among rural women." (Exercise 12c)', 'Pills are popular mainly among ' + T('urban') + ' women; awareness is low in rural areas')
d.basic('How are injectables and implants different from pills?', 'Same hormones and similar action, but ' + T('much longer effective periods'), **fig('fig_3_3_implants'))
d.basic('Where are implants placed?', T('Under the skin'))
d.basic('What are emergency contraceptives?', 'Progestogens, progestogen–estrogen combinations or IUDs used within ' + N('72 hours') + ' of coitus')
d.basic('When are emergency contraceptives used?', 'To avoid pregnancy after ' + T('rape') + ' or casual unprotected intercourse')

d.basic('What are surgical methods also called, and when advised?', T('Sterilisation') + '; a ' + T('terminal') + ' method to prevent any more pregnancies')
d.basic('How do surgical methods prevent conception?', 'Block ' + T('gamete transport'))
d.basic('What is vasectomy?', 'A small part of the ' + T('vas deferens') + ' is removed or tied through a small incision on the ' + T('scrotum'), **fig('fig_3_4_vasectomy_tubectomy'))
d.basic('What is tubectomy?', 'A small part of the ' + T('fallopian tube') + ' is removed or tied through a small incision in the abdomen or through the vagina')
d.basic('Identify both procedures (Figure 3.4).', 'Left: ' + T('vasectomy') + ' (vas deferens tied and cut). Right: ' + T('tubectomy') + ' (fallopian tubes tied and cut).', **img('fig_3_4_vasectomy_tubectomy'))
d.basic('Drawback of sterilisation?', 'Highly effective, but ' + X('reversibility is very poor'))
d.basic('Correct: "Surgical methods prevent gamete formation." (Exercise 12a)', 'They ' + X('do not') + ' stop gamete formation; they block ' + T('gamete transport'))
d.basic('Why is removal of gonads not a contraceptive option? (Exercise 7)', 'Gonads also make ' + T('hormones') + '; removing them disturbs secondary sexual characters and health, and is irreversible')
d.basic('Possible ill-effects of contraceptives?', 'Nausea, abdominal pain, breakthrough bleeding, irregular menstrual bleeding, even breast cancer')
d.basic('Are contraceptives regular requirements for reproductive health?', X('No') + '. They act against a natural event (conception); used to prevent, delay or space pregnancy')
d.basic('Mnemonic for how each contraceptive works?', T('Natural') + ' = avoid meeting in time; ' + T('Barrier') + ' = block physically; ' + T('IUD') + ' = kill/slow sperm; ' + T('Pill') + ' = stop ovulation; ' + T('Surgery') + ' = cut the road')

# ---------------------------------------------------------------- 3.3 MTP
d.sec('3.3-mtp')
d.basic('What is MTP?', 'Intentional or voluntary termination of pregnancy before full term; ' + T('induced abortion'))
d.basic('Number of MTPs worldwide per year?', N('45–50 million') + ': about ' + N('1/5th') + ' of all conceived pregnancies')
d.basic('When did India legalise MTP?', N('1971') + ', with strict conditions to prevent misuse')
d.basic('Why are restrictions on MTP important in India?', 'To check indiscriminate and illegal ' + X('female foeticide'))
d.basic('Why is MTP done?', 'Unwanted pregnancy (unprotected intercourse, contraceptive failure, rape)<br>Or when continuing is harmful or fatal to mother/foetus')
d.basic('When is MTP relatively safe?', 'During the ' + T('first trimester') + ' (up to ' + N('12 weeks') + '); second-trimester abortions are much riskier')
d.basic('Two disturbing trends with MTP?', 'Illegal MTPs by ' + X('unqualified quacks') + '; misuse of ' + X('amniocentesis') + ' for sex determination followed by MTP')
d.basic('How can these trends be reversed?', T('Counselling') + ' on avoiding unprotected coitus and risks of illegal abortion, plus more health care facilities')
d.basic('MTP (Amendment) Act as per NCERT: opinions needed?', 'Up to ' + N('12 weeks') + ': ' + N('one') + ' registered medical practitioner. ' + N('12–24 weeks') + ': ' + N('two') + ' practitioners.')
d.basic('Grounds for MTP under the Act?', 'Risk to the ' + T('life') + ' or grave physical/mental injury of the woman<br>Or substantial risk of the child being ' + T('seriously handicapped'))
d.basic('Update: NCERT calls it the MTP (Amendment) Act 2017. Current law?', 'The ' + T('MTP (Amendment) Act, 2021') + ':<br>One doctor up to ' + N('20 weeks') + '<br>Two doctors ' + N('20–24 weeks') + ' for special categories<br>No limit for substantial foetal abnormalities (medical board)')
d.basic('Can abortions happen spontaneously? (Exercise 11a)', T('True') + ': spontaneous abortion = miscarriage')

# ---------------------------------------------------------------- 3.4 STIs
d.sec('3.4-stis')
d.basic('Other names for sexually transmitted infections (STIs)?', T('Venereal diseases (VD)') + ' or ' + T('reproductive tract infections (RTI)'))
d.basic('Common STIs?', 'Gonorrhoea, syphilis, genital herpes, chlamydiasis, genital warts, trichomoniasis, hepatitis-B, HIV/AIDS')
d.basic('Most dangerous STI?', T('HIV') + ' infection (leading to AIDS)')
d.basic('STIs also transmitted by needles, blood and mother to foetus?', T('Hepatitis-B') + ' and ' + T('HIV'))
d.basic('Which STIs are not completely curable?', X('Hepatitis-B, genital herpes and HIV') + '; others are curable if detected early')
d.basic('Correct: "All STDs are completely curable." (Exercise 12b)', X('Not all') + '. Hepatitis-B, genital herpes and HIV are not completely curable.')
d.basic('Early symptoms of STIs?', 'Itching, fluid discharge, slight pain, swellings in the genital region')
d.basic('Why do STIs often go untreated?', 'Infected females may be ' + T('asymptomatic') + '; mild early symptoms; ' + T('social stigma'))
d.basic('Complications of untreated STIs?', T('PID') + ', abortions, still births, ' + T('ectopic pregnancy') + ', infertility, cancer of the reproductive tract')
d.basic('Age group with highest STI incidence?', N('15–24 years'))
d.basic('Three principles to prevent STIs? (Exercise 10)', 'Avoid sex with unknown/multiple partners; always use ' + T('condoms') + '; see a qualified doctor early if in doubt')
table_card(d, 'STI pathogens', 'Caused by? (beyond NCERT)', [
    ('Gonorrhoea', 'Neisseria gonorrhoeae (bacterium)', False), ('Syphilis', 'Treponema pallidum (bacterium)', False),
    ('Genital herpes', 'Herpes simplex virus', False), ('Genital warts', 'Human papilloma virus', False),
    ('Trichomoniasis', 'Trichomonas vaginalis (protozoan)', False), ('Chlamydiasis', 'Chlamydia trachomatis (bacterium)', False)],
    term='Causative agents of STIs')

# ---------------------------------------------------------------- 3.5 Infertility
d.sec('3.5-infertility')
d.basic('What is infertility?', 'Inability to produce children in spite of ' + T('unprotected sexual co-habitation') + ' (NCERT summary: after ' + N('2 years') + ')')
d.basic('Update: current clinical definition of infertility?', 'WHO: failure to conceive after ' + N('12 months') + ' of regular unprotected intercourse (exam answer per NCERT: 2 years)')
d.basic('Causes of infertility?', 'Physical, congenital, diseases, drugs, immunological or psychological')
d.basic('Is infertility always due to the female? (Exercise 11b)', X('False') + '. More often than not the problem lies in the ' + T('male') + ' partner.')
d.basic('What is ART?', T('Assisted reproductive technologies') + ': special techniques helping infertile couples have children')
d.basic('What is IVF–ET?', T('In vitro fertilisation') + ' (outside the body, in simulated conditions) followed by ' + T('embryo transfer') + '<br>The "test tube baby" programme')
d.basic('ZIFT: what is transferred and where?', T('Zygote or early embryo') + ' (up to ' + N('8 blastomeres') + ') into the ' + T('fallopian tube'))
d.basic('IUT: what is transferred and where?', 'Embryo with ' + T('more than 8 blastomeres') + ' into the ' + T('uterus'))
d.basic('Correct: "In ET, embryos are always transferred into the uterus." (Exercise 12d)', X('Not always') + '. Up to 8 blastomeres → fallopian tube (ZIFT); more → uterus (IUT).')
d.basic('Can embryos formed by in-vivo fertilisation be transferred?', T('Yes') + ', to assist females who cannot conceive')
d.basic('What is GIFT?', T('Gamete intra fallopian transfer') + ':<br>a donor ovum is transferred into the fallopian tube of a female who cannot produce one but can support fertilisation')
d.basic('What is ICSI?', T('Intra cytoplasmic sperm injection') + ': a sperm is directly injected into the ovum in the lab')
d.basic('When is artificial insemination (AI) used?', 'Male cannot inseminate, or ' + T('very low sperm count'))
d.basic('What is IUI?', T('Intra-uterine insemination') + ': semen from husband or donor introduced into the ' + T('uterus'))
d.basic('Mnemonic: what goes where in ART?', T('ZIFT') + ' = Zygote → tube. ' + T('GIFT') + ' = Gamete (ovum) → tube. ' + T('IUT') + ' = older embryo → uterus. ' + T('IUI') + ' = semen → uterus.')
d.basic('Why are ART facilities limited?', 'Need high precision, specialised professionals and expensive instruments<br>Also emotional, religious, social deterrents')
d.basic('Best alternative for couples seeking parenthood (NCERT)?', T('Legal adoption') + ' of orphaned and destitute children')

# ---------------------------------------------------------------- summary
d.sec('summary')
table_card(d, 'Contraceptives', 'Method type?', [
    ('Periodic abstinence', 'Natural', False), ('Diaphragm, cervical cap', 'Barrier (female)', False),
    ('Multiload 375', 'Copper IUD', False), ('LNG-20', 'Hormone IUD', False), ('Saheli', 'Oral pill (non-steroidal)', False),
    ('Vasectomy', 'Surgical (male)', False)], term='Classify the contraceptive')
table_card(d, 'Exercise 11', 'True or false?', [
    ('Abortions could happen spontaneously', 'True', False),
    ('Infertility is always due to the female', 'False', True),
    ('Complete lactation can act as natural contraception', 'True (up to 6 months)', False),
    ('Awareness improves reproductive health', 'True', False)], term='True/False (Exercise 11)')

os.makedirs(OUT, exist_ok=True)
print('notes', d.write(os.path.join(OUT, 'deck.json')))
