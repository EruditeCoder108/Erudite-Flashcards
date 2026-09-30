import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from deckkit import *
import showcase_phy as sp

OUT = os.path.join(ROOT, 'premade-cards', '12th', 'Physics', 'class12-physics-ch14-semiconductor-electronics-materials-devices-and-simple-circuits')
d = Deck('Chapter 14: Semiconductor Electronics: Materials, Devices and Simple Circuits', 'Class 12', ['class-12', 'physics', 'ch-14'])
d.description = 'Energy bands, intrinsic and extrinsic semiconductors, p-n junction, diode, rectifiers, plus Zener, LED, transistor and logic gates'
M = 'media/'
fig = lambda name: {'definitionImage': M + name + '.webp'}
img = lambda name: {'termImage': M + name + '.webp'}

# ---------------------------------------------------------------- 14.1 Introduction
d.sec('14.1-introduction')
d.basic('Before transistors (1948), which devices controlled electron flow?', T('Vacuum tubes (valves)') + ': diode (2 electrodes), triode (cathode, plate, grid), tetrode, pentode')
d.basic('Why were vacuum tubes replaced by semiconductor devices?', 'Tubes are bulky, power-hungry, need high voltages (~100 V), need a heated cathode, and have a short life. Semiconductor devices are ' + T('small, low-power, low-voltage, long-lived, reliable'))
d.basic('In which direction do electrons flow in a vacuum diode? Why “valve”?', 'Only from ' + T('cathode to anode') + ', so the device acts like a one-way valve')
d.basic('Where do the mobile charges in a semiconductor device come from?', 'From the ' + T('solid itself') + ' (controlled by light, heat or a small voltage); no external heating or vacuum needed')
d.basic('Early semiconductor detector of radio waves?', 'A crystal of ' + T('galena (PbS)') + ' with a metal point contact')

# ---------------------------------------------------------------- 14.2 Classification
d.sec('14.2-classification-of-metals-conductors-and-semiconductors')
d.basic('Classify solids by resistivity ρ and conductivity σ.', T('Metals') + ': ρ ~ 10⁻²–10⁻⁸ Ω m (σ ~ 10²–10⁸ S/m). ' + T('Semiconductors') + ': ρ ~ 10⁻⁵–10⁶ Ω m. ' + T('Insulators') + ': ρ ~ 10¹¹–10¹⁹ Ω m')
d.basic('Types of semiconductors (with examples)?', T('Elemental') + ': Si, Ge<br>' + T('Compound inorganic') + ': GaAs, CdS, CdSe, InP<br>' + T('Organic') + ': anthracene, doped phthalocyanines<br>Polymers: polypyrrole, polyaniline')
d.basic('Which semiconductors does the chapter study?', 'Inorganic ' + T('Si and Ge') + ' (most devices are made of them)')
d.basic('Valence band and conduction band?', T('Valence band') + ': the energy band containing the valence electrons’ levels<br>' + T('Conduction band') + ': the band above it; electrons here are free to move')
d.basic('Why do energy bands form in a solid?', 'Outer orbits of neighbouring atoms ' + T('overlap') + ', so each electron sees a unique surrounding and gets a slightly different energy.<br>Closely spaced levels form bands')
d.basic('Band structure of Si and Ge at 0 K?', 'The 8N states split into two bands with a gap E_g.<br>Lower ' + T('valence band') + ' (4N states): completely full with the 4N valence electrons<br>Upper ' + T('conduction band') + ' (4N states): empty', **fig('fig_14_1_bands_0K'))
d.basic('Correction: NCERT writes the outer electrons of Si/Ge as “2s and 2p”. What is right?', X('Slip') + ': Si has ' + T('3s² 3p²') + ' and Ge ' + T('4s² 4p²') + ' (outermost orbit n = 3 and n = 4, as the same paragraph says)')
d.basic('Energy band diagram of a metal?', 'Conduction and valence bands ' + T('overlap') + ' (E_g ≈ 0), or the band is partially filled.<br>Many free electrons, so high conductivity', **fig('fig_14_2a_metal'))
d.basic('Energy band diagram of an insulator?', 'Large gap ' + T('E_g > 3 eV') + ': no electrons in the conduction band; thermal energy cannot bridge the gap', **fig('fig_14_2b_insulator'))
d.basic('Energy band diagram of a semiconductor?', 'Small gap ' + T('E_g < 3 eV') + ' (0.2–3 eV): at room temperature a few electrons cross into the conduction band', **fig('fig_14_2c_semiconductor'))
d.basic('Band gaps of C (diamond), Si, Ge and Sn?', N('5.4 eV') + ', ' + N('1.1 eV') + ', ' + N('0.7 eV') + ' (Ge 0.72), ' + N('0 eV') + ' (tin, a metal)')
d.basic('Example 14.1: why is carbon an insulator while Si and Ge are semiconductors, with the same lattice?', 'Bonding electrons lie in shells n = 2, 3, 4: ionisation energy (E_g) is least for Ge, then Si, largest for C.<br>So conduction electrons are ' + T('significant for Ge, Si and negligible for C'))
d.basic('Teacher addition: how does resistance vary with temperature for a metal and a semiconductor?', 'Metal: R ' + T('increases') + ' with T (more collisions). Semiconductor: R ' + T('decreases') + ' with T (more electron–hole pairs); temperature coefficient of resistance is negative')
d.basic('Teacher addition: is an insulator with a small E_g at high temperature a conductor?', 'Its conductivity rises with T; the classification depends on E_g relative to kT (≈ 0.026 eV at 300 K)')

# ---------------------------------------------------------------- 14.3 Intrinsic semiconductors
d.sec('14.3-intrinsic-semiconductor')
d.basic('Crystal structure of Si and Ge?', T('Diamond-like') + ' cubic structure: each atom has four nearest neighbours.<br>Lattice spacing: C 3.56 Å, Si 5.43 Å, Ge 5.66 Å', **fig('fig_14_3_diamond'))
d.basic('What is a covalent (valence) bond in Si?', 'Two atoms ' + T('share electron pairs') + '.<br>Each atom shares one of its four valence electrons with each of four neighbours', **fig('fig_14_4_bonds'))
d.basic('Intrinsic semiconductor: definition?', 'A ' + T('pure') + ' semiconductor whose carriers come only from thermal breaking of bonds; n_e = n_h = n_i')
d.basic('What is a hole?', 'A ' + T('vacancy in a covalent bond') + ' left when an electron breaks free.<br>It behaves like a free particle with effective positive charge +q', **fig('fig_14_5a_hole'))
d.basic('How does a hole “move”?', 'A neighbouring bound electron jumps into the vacancy, leaving a hole at its own site.<br>The hole appears to move in the ' + T('opposite direction to the electron'), **fig('fig_14_5b_hole_motion'))
d.basic('Total current in an intrinsic semiconductor?', r'\( I = I_e + I_h \)' + '; holes move towards the negative potential (hole current in the direction of the field)')
d.basic('Generation and recombination?', 'Thermal generation of electron–hole pairs is balanced at equilibrium by ' + T('recombination') + ' (an electron falling into a hole)')
d.basic('Intrinsic semiconductor at T = 0 K and at T > 0 K?', '0 K: behaves as an ' + T('insulator') + ' (valence band full, conduction band empty). T > 0: thermally excited electrons partly occupy the conduction band, leaving equal holes', **fig('fig_14_6a_intrinsic_0K'))
d.basic('Energy-band picture of an intrinsic semiconductor at T > 0 K?', 'Some electrons in the conduction band and an equal number of holes in the valence band', **fig('fig_14_6b_intrinsic_T'))
d.basic('Teacher addition: how does intrinsic carrier concentration n_i vary with temperature and gap?', T('n_i ∝ T^{3/2} e^{−E_g/2kT}') + '<br>Rises rapidly with temperature and falls for a larger gap<br>(Si at 300 K: ~1.5 × 10¹⁶ m⁻³)')
d.basic('Teacher addition: mobility of electrons vs holes?', T('μ_e > μ_h') + ' (electrons move more freely than holes): σ = e(nₑμₑ + nₕμₕ)')

# ---------------------------------------------------------------- 14.4 Extrinsic semiconductors
d.sec('14.4-extrinsic-semiconductor')
d.basic('What is doping? What are extrinsic semiconductors?', 'Deliberate addition of a small amount (parts per million) of a suitable impurity (' + T('dopant') + ') to a pure semiconductor to raise its conductivity manifold.<br>The result: ' + T('extrinsic (impurity) semiconductors'))
d.basic('Condition on the size of the dopant atom?', 'Its size must be ' + T('nearly the same') + ' as that of Si/Ge so that it does not distort the lattice')
d.basic('Dopants for Si and Ge?', T('Pentavalent') + ' (As, Sb, P): n-type. ' + T('Trivalent') + ' (B, Al, In, Ga): p-type')
d.basic('How does a pentavalent dopant make an n-type semiconductor?', 'Four of its five valence electrons form bonds; the ' + T('fifth is very loosely bound') + ' (ionisation energy ~ 0.01 eV for Ge, 0.05 eV for Si) and is free at room temperature. The dopant is a ' + T('donor'), **fig('fig_14_7a_donor'))
d.basic('Majority and minority carriers in n-type material?', 'Electrons are ' + T('majority') + ', holes ' + T('minority') + ' (n_e ≫ n_h). The crystal stays ' + T('electrically neutral'), **fig('fig_14_7b_n_type'))
d.basic('How does a trivalent dopant make a p-type semiconductor?', 'It has one electron too few, leaving a vacancy (' + T('hole') + ') in the fourth bond; a neighbour’s electron fills it and the hole moves on. The dopant is an ' + T('acceptor') + ' (becomes a fixed negative ion)', **fig('fig_14_8a_acceptor'))
d.basic('Majority and minority carriers in p-type material?', 'Holes are ' + T('majority') + ', electrons ' + T('minority') + ' (n_h ≫ n_e); one acceptor gives one hole', **fig('fig_14_8b_p_type'))
d.basic('Mass-action law for doped semiconductors?', r'\( n_en_h = n_i^2 \)' + ' (in thermal equilibrium, in every case); doping raises one carrier type and ' + T('reduces the other') + ' via recombination')
d.basic('Why do the minority carriers decrease with doping?', 'The abundant majority carriers give the thermally generated minority carriers many more chances to ' + T('recombine'))
d.basic('Energy-band picture of an n-type semiconductor?', 'A donor level E_D lies ' + T('just below E_C') + ' (~ 0.01–0.05 eV).<br>Nearly all donors are ionised at room temperature, so most conduction electrons come from the dopant', **fig('fig_14_9a_n_bands'))
d.basic('Energy-band picture of a p-type semiconductor?', 'An acceptor level E_A lies ' + T('just above E_V') + ' (~ 0.01–0.05 eV).<br>Electrons jump up into it, leaving holes in the valence band', **fig('fig_14_9b_p_bands'))
d.basic('Mnemonic: donor vs acceptor?', T('Donor → n-type') + ' (Negative carriers, pentavalent, 5 electrons: “Donate a Negative”)<br>' + T('Acceptor → p-type') + ' (Positive holes, trivalent, ' + T('3') + ' electrons: “Accepts electrons”)')
d.basic('Do the number of donor electrons depend on temperature?', 'Weakly: donor electrons depend on ' + T('doping level') + ', not temperature, while the intrinsic pairs rise weakly with temperature')
steps_card(d, 'Example 14.2 · doped silicon', 'Find the missing step.', 'Si crystal with 5 × 10²⁸ atoms/m³ is doped with 1 ppm arsenic. Find n_e and n_h (n_i = 1.5 × 10¹⁶ m⁻³).',
           ['N_D = 10⁻⁶ × 5 × 10²⁸ = 5 × 10²² m⁻³', 'n_i ≪ N_D, so n_e ≈ N_D = <b>5 × 10²² m⁻³</b>', 'n_h = n_i²/n_e = (2.25 × 10³²)/(5 × 10²²)', '<b>n_h ≈ 4.5 × 10⁹ m⁻³</b> (a factor 10¹³ smaller)'], 2,
           'Carrier densities in doped Si (Example 14.2)', 'n_e ≈ 5 × 10²² m⁻³; n_h ≈ 4.5 × 10⁹ m⁻³')
d.basic('Exercise 14.1: in n-type silicon which statement is true?', T('(c)') + ': holes are minority carriers and pentavalent atoms are the dopants')
d.basic('Exercise 14.2: the true statement for p-type semiconductors?', T('(d)') + ': holes are the majority carriers and trivalent atoms are the dopants')
d.basic('Exercise 14.3: carbon, silicon, germanium band gaps?', T('(c)') + ' (E_g)_C > (E_g)_Si > (E_g)_Ge')
d.basic('Teacher addition: a Ge crystal doped with In, or Si with P. n-type or p-type?', 'In (Group III): ' + T('p-type') + '. P (Group V): ' + T('n-type'))
d.basic('Teacher addition: n-type and p-type materials are separately electrically neutral. Why?', 'The extra carriers (electrons or holes) are balanced by the equal and opposite charge of the ' + T('ionised dopant cores') + ' fixed in the lattice')
d.basic('Teacher addition: conductivity of an extrinsic semiconductor?', r'\( \sigma = e(n_e\mu_e + n_h\mu_h) \approx e\,n_e\mu_e \)' + ' (n-type) or ' + r'\( e\,n_h\mu_h \)' + ' (p-type)')

# ---------------------------------------------------------------- 14.5 p-n junction
d.sec('14.5-p-n-junction')
d.basic('Why is the p-n junction important?', 'It is the basic building block of ' + T('diodes, transistors') + ' and many other devices')
d.basic('Diffusion at a p-n junction?', 'Due to the concentration gradient, holes diffuse ' + T('p → n') + ' and electrons ' + T('n → p') + ': the diffusion current')
d.basic('How is the depletion region formed?', 'Electrons leaving n leave immobile ' + T('positive donor ions') + '.<br>Holes leaving p leave immobile ' + T('negative acceptor ions') + '.<br>This space-charge layer, free of mobile carriers, is the depletion region (~ 0.1 µm thick)', **fig('fig_14_10_formation'))
d.occlusion('Figure 14.10 · Formation of the p-n junction', M + 'fig_14_10_formation.webp', (1001, 535), [
    ('Electron diffusion', [455, 0, 425, 45], True), ('Electron drift', [10, 48, 315, 48], True), ('Hole diffusion', [0, 450, 330, 50], True),
    ('Hole drift', [462, 495, 225, 42], True), ('Depletion region', [618, 405, 383, 50], True)], guess='hide-all')
d.basic('Drift current at a p-n junction?', 'The junction field (from the positive n-side space charge to the negative p-side charge) sweeps electrons p → n and holes n → p.<br>This is the ' + T('drift current, opposite to diffusion'))
d.basic('Equilibrium in a p-n junction?', 'Diffusion current = drift current: ' + T('no net current') + ', constant barrier potential V₀', **fig('fig_14_11a_equilibrium'))
d.basic('Barrier potential (built-in potential V₀)?', 'The potential difference across the junction that opposes further diffusion: n side ' + T('positive') + ' relative to p. About ' + N('0.7 V for Si') + ' and 0.3 V for Ge', **fig('fig_14_11b_barrier'))
d.basic('Direction of the electric field in the depletion region?', 'From the positive ions on the n-side towards the negative ions on the p-side, i.e. ' + T('n → p'))
d.basic('Example 14.3: can two slabs of p- and n-type semiconductors simply be pressed together?', X('No') + ': surface roughness ≫ atomic spacing (2–3 Å), so there is no atomic-level contact: the junction acts as a discontinuity. The junction must be grown in a single crystal')
d.basic('Teacher addition: as the depletion layer grows, why does diffusion stop?', 'The growing field raises the drift current until it equals the diffusion current.<br>The barrier V₀ is set by the doping levels and temperature')

# ---------------------------------------------------------------- 14.6 Diode
d.sec('14.6-semiconductor-diode')
d.basic('What is a semiconductor diode? Symbol?', 'A p-n junction with metallic contacts: a ' + T('two-terminal') + ' device. The arrow head (from p to n) shows the conventional current direction in ' + T('forward') + ' bias', **fig('fig_14_12a_diode'))
d.basic('Forward bias: connections and effect on the barrier?', T('p to +, n to −') + '. The applied field opposes V₀: the depletion layer ' + T('narrows') + ' and barrier falls to ' + r'\( V_0 - V \)', **fig('fig_14_13a_forward'))
d.basic('Effect of forward bias on carriers?', 'Barrier reduced, more carriers cross: ' + T('minority-carrier injection') + ' (electrons into p-side, holes into n-side).<br>Current is large (mA)', **fig('fig_14_14_injection'))
d.basic('Reverse bias: connections and effect on the barrier?', T('n to +, p to −') + '. The applied field adds to V₀: the depletion layer ' + T('widens') + ' and barrier rises to ' + r'\( V_0 + V \)', **fig('fig_14_15a_reverse'))
d.basic('Why is the reverse current tiny and nearly voltage-independent?', 'It is due to ' + T('minority carriers') + ' swept across (drift).<br>It is limited by their concentration, not by the applied voltage; of the order of µA')
sp.pn_junction_bias(d)
d.basic('Diode breakdown voltage?', 'At a critical reverse voltage V_br the reverse current increases ' + T('sharply') + '.<br>An ordinary diode is destroyed if the current is not limited by the circuit')
d.basic('Experimental set-up for diode characteristics?', 'Diode + potentiometer/rheostat + battery; a ' + T('milliammeter') + ' in forward bias and a ' + T('microammeter') + ' in reverse bias', **fig('fig_14_16a_forward_circuit'))
d.basic('Typical V–I characteristic of a Si diode?', 'Forward: almost no current till the ' + T('threshold (cut-in) voltage') + ' (~0.7 V Si, ~0.2 V Ge), then it rises exponentially. Reverse: tiny constant ' + T('reverse saturation current') + ' till breakdown', **fig('fig_14_16c_vi'))
d.basic('Threshold voltage of Si and Ge diodes?', T('~0.7 V (Si)') + ' and ' + T('~0.2 V (Ge)'))
d.basic('Dynamic resistance of a diode?', r'\( r_d = \dfrac{\Delta V}{\Delta I} \)' + ': the small-signal ratio; low in forward bias, very large in reverse bias')
steps_card(d, 'Example 14.4 · diode resistance', 'Find the missing step.', 'For a silicon diode: (a) resistance at I_D = 15 mA (b) resistance at V_D = −10 V (reverse current 1 µA). Read: 0.7 V at 10 mA, 0.8 V at 20 mA.',
           ['(a) Between 10 mA and 20 mA the curve is nearly a line: ΔV = 0.1 V, ΔI = 10 mA', 'r_fb = ΔV/ΔI = 0.1/(10 × 10⁻³) = <b>10 Ω</b>', '(b) At −10 V, I = −1 µA', 'r_rb = 10 V/1 µA = <b>1.0 × 10⁷ Ω</b>'], 1,
           'Forward and reverse resistance (Example 14.4)', 'r_fb = 10 Ω; r_rb = 1.0 × 10⁷ Ω')
d.basic('Exercise 14.4: in an unbiased p-n junction holes diffuse from p to n because…?', T('(c)') + ' hole concentration is greater in the p-region than in the n-region (concentration gradient)')
d.basic('Exercise 14.5: forward bias applied to a p-n junction…?', T('(c)') + ': lowers the potential barrier')
d.basic('Teacher addition: ideal diode?', 'Zero resistance in forward bias (short circuit)<br>Infinite resistance in reverse bias (open circuit)<br>A practical Si diode has a ' + T('0.7 V drop') + ' when conducting')
d.basic('Teacher addition: a diode in series with a resistor and a battery. Current?', 'If forward biased: I = (E − 0.7)/R for silicon (E − 0 for ideal); if reverse biased: ' + T('I ≈ 0') + ' (open circuit)')
d.basic('Teacher addition: diode forward current equation?', r'\( I = I_0\left(e^{eV/kT} - 1\right) \)' + ' (Shockley): exponential in forward bias, saturates at −I₀ in reverse bias')

# ---------------------------------------------------------------- 14.7 Rectifier
d.sec('14.7-application-of-junction-diode-as-a-rectifier')
d.basic('What is rectification?', 'Converting ' + T('ac to a unidirectional (pulsating dc)') + ' voltage using the one-way conduction of a diode')
d.basic('Half-wave rectifier: circuit and action?', 'Transformer secondary → diode in series with R_L.<br>Output appears only in the ' + T('half-cycles when the diode is forward biased'), **fig('fig_14_18_half_wave'))
d.basic('Half-wave rectifier waveforms?', 'Output = positive half-cycles only; ' + T('output frequency = input frequency (50 Hz)'), **fig('fig_14_18b_half_waveforms'))
d.basic('Full-wave rectifier: circuit and operation?', 'Two diodes with a ' + T('centre-tap transformer') + '.<br>D₁ conducts in one half-cycle and D₂ in the other.<br>Both give current through R_L in the same direction (each diode rectifies half of the secondary voltage)', **fig('fig_14_19_full_wave'))
d.basic('Frequency of output of half-wave and full-wave rectifiers for 50 Hz input? (Exercise 14.6)', 'Half-wave: ' + N('50 Hz') + '. Full-wave: ' + N('100 Hz'))
d.basic('Another full-wave circuit?', 'The ' + T('bridge rectifier') + ' with four diodes needs no centre-tapped transformer')
d.basic('Why is a filter needed after a rectifier?', 'The rectified output is ' + T('pulsating') + ' (half sinusoids); a filter removes the ac ripple to give steady dc', **fig('fig_14_20a_filter'))
d.basic('How does a capacitor filter work?', 'The capacitor across R_L charges to the peak.<br>It then discharges slowly through R_L (time constant ' + T('R_LC') + ') while the input dips, and is recharged in the next pulse.<br>A large C gives a smoother output', **fig('fig_14_20b_filter_wave'))
sp.rectifier_waveforms(d)
d.basic('Alternative filter?', 'An ' + T('inductor in series') + ' with R_L (choke input filter)')
d.basic('Why must the diode’s reverse breakdown voltage exceed the peak ac secondary voltage?', 'Otherwise the diode breaks down in the non-conducting half-cycle and is damaged')
d.basic('Teacher addition: peak inverse voltage (PIV) for half-wave and centre-tap full-wave rectifiers?', 'Half-wave: PIV = V_m. Centre-tap full-wave: PIV = ' + T('2V_m') + ' (V_m = peak of half the secondary). Bridge: PIV = V_m')
d.basic('Teacher addition: average (dc) and rms values of the output of half-wave and full-wave rectifiers?', 'Half-wave: V_dc = V_m/π, V_rms = V_m/2. Full-wave: V_dc = ' + T('2V_m/π') + ', V_rms = V_m/√2')
d.basic('Teacher addition: ripple factor and efficiency?', 'Half-wave: efficiency 40.6%, ripple factor 1.21. Full-wave: efficiency ' + T('81.2%') + ', ripple factor 0.48')
d.basic('Teacher addition: why does the capacitor filter output approach V_peak?', 'With large R_LC the discharge is small between recharge pulses, so the output stays close to the ' + T('peak value') + ' of the rectified voltage')

# ---------------------------------------------------------------- NEET / JEE extras
d.sec('neet-jee-additions')
d.basic('NEET/JEE addition: Zener diode?', 'A heavily doped p-n diode designed to operate in ' + T('reverse breakdown') + '; the voltage across it stays nearly constant (V_Z) over a wide current range. Used as a ' + T('voltage regulator'))
d.basic('NEET/JEE addition: how does a Zener regulator work?', 'Connect the Zener in reverse across the load with a series resistor R_s. If input voltage or load current changes, the extra current passes through the Zener while ' + T('V_out = V_Z') + ' stays fixed; the difference is dropped across R_s')
d.basic('NEET/JEE addition: two breakdown mechanisms?', T('Zener breakdown') + ': heavy doping, thin depletion layer, V_Z < 5 V; strong field pulls electrons from bonds<br>' + T('Avalanche breakdown') + ': lighter doping, V > 6 V; impact ionisation')
d.basic('NEET/JEE addition: light-emitting diode (LED)?', 'A forward-biased heavily doped p-n junction that emits light on ' + T('electron–hole recombination') + '; photon energy ≈ E_g. Made from GaAs, GaP, GaAsP; colour set by the gap (Si and Ge are useless as they are indirect)')
d.basic('NEET/JEE addition: photodiode?', 'A p-n junction operated in ' + T('reverse bias') + '.<br>Photons of energy hν ≥ E_g create electron–hole pairs, and the reverse current rises with light intensity (light detector)')
d.basic('NEET/JEE addition: solar cell?', 'A p-n junction (large area, no bias) that turns light into electricity by generating an emf across the junction; the I–V curve is in the fourth quadrant. Materials: Si, GaAs, CdTe')
d.basic('NEET/JEE addition: modes of the three optoelectronic junctions?', T('LED') + ': forward bias, emits light. ' + T('Photodiode') + ': reverse bias, detects light. ' + T('Solar cell') + ': no bias, generates power')
d.basic('NEET/JEE addition: the junction transistor?', 'A three-region device (n-p-n or p-n-p): ' + T('emitter') + ' (heavily doped), ' + T('base') + ' (thin, lightly doped), ' + T('collector') + ' (moderately doped, larger). Emitter–base forward biased, collector–base reverse biased')
d.basic('NEET/JEE addition: transistor current relations?', r'\( I_E = I_B + I_C \)' + '; ' + r'\( \alpha = \dfrac{I_C}{I_E} \)' + ' (< 1), ' + r'\( \beta = \dfrac{I_C}{I_B} \)' + ' (50–200), ' + r'\( \beta = \dfrac{\alpha}{1-\alpha} \)')
d.basic('NEET/JEE addition: a transistor as an amplifier (common emitter)?', 'A small change in base current gives a large change in collector current; ' + T('phase reversal of 180°') + ' between input and output; voltage gain A_v = β R_L/R_i')
d.basic('NEET/JEE addition: a transistor as a switch?', 'In ' + T('cut-off') + ' (base off) it is an open switch; in ' + T('saturation') + ' (large base current) a closed switch')
d.basic('NEET/JEE addition: logic gates (digital electronics)?', 'Circuits that follow Boolean logic: ' + T('OR, AND, NOT') + ' (basic) and ' + T('NAND, NOR') + ' (universal gates) plus XOR')
table_card(d, 'Logic gates', 'Boolean expression and output rule?', [
    ('OR', 'Y = A + B; output 1 if any input is 1', False), ('AND', 'Y = A · B; output 1 only if both inputs are 1', False),
    ('NOT', 'Y = NOT A; inverts the input', False), ('NAND', 'Y = NOT(A · B); AND followed by NOT (output 0 only if both inputs are 1)', False),
    ('NOR', 'Y = NOT(A + B); OR followed by NOT (output 1 only if both inputs are 0)', False), ('XOR', 'Y = A ⊕ B; output 1 if inputs differ', False)],
    term='Logic gates (NEET/JEE addition)')
d.basic('NEET/JEE addition: which gates are universal? Why?', T('NAND and NOR') + ': any Boolean function (AND, OR, NOT) can be built from either alone')
d.basic('NEET/JEE addition: truth table of NAND for inputs (A, B) = (0,0), (0,1), (1,0), (1,1)?', 'Outputs: ' + N('1, 1, 1, 0'))
d.basic('NEET/JEE addition: truth table of NOR for the same inputs?', 'Outputs: ' + N('1, 0, 0, 0'))
d.basic('NEET/JEE addition: NOT gate built from a NAND gate?', 'Join both inputs together: ' + T('Y = NOT(A · A) = NOT A'))
d.basic('NEET/JEE addition: symbols of gates?', 'AND: D-shaped; OR: curved-back shield; NOT: triangle with a ' + T('bubble') + '; NAND/NOR: AND/OR with a bubble at the output')

# ---------------------------------------------------------------- Points to ponder
d.sec('points-to-ponder')
d.basic('Are E_C and E_V localised in space?', X('No') + ': band energies are ' + T('delocalised') + ' averages; drawn as straight lines they mean the bottom of the conduction band and the top of the valence band')
d.basic('How can compound semiconductors become n- or p-type?', 'By changing the ' + T('stoichiometric ratio') + ' (e.g. Ga-rich or As-rich GaAs) as well as by doping.<br>Defects control semiconductor properties')

# ---------------------------------------------------------------- Exam patterns
d.sec('exam-patterns')
d.basic('NEET pattern: in a p-n junction diode, holes diffuse from p to n because…?', 'Of the ' + T('concentration gradient') + ' (not because of an applied field)')
d.basic('NEET pattern: the depletion layer in a p-n junction consists of…?', 'Immobile ' + T('ionised donors and acceptors') + ' (no mobile carriers)')
d.basic('NEET pattern: in forward bias the width of the depletion region and the barrier height?', 'Both ' + T('decrease'))
d.basic('NEET pattern: electron–hole pairs in a pure Si crystal at T > 0 K: n_e vs n_h?', 'n_e = n_h = n_i; after n-type doping, n_e ≫ n_h but n_e n_h = n_i² still')
d.basic('NEET pattern: Si doped with B. Nature and majority carriers?', T('p-type') + ', holes')
d.basic('NEET pattern: with a half-wave rectifier of 50 Hz input, ripple frequency?', T('50 Hz') + ' (full-wave gives 100 Hz)')
d.basic('JEE pattern: given the ratio n_e/n_h in a semiconductor, find the type and n_i.', 'n_e n_h = n_i²: e.g. n_e = 10²² and n_h = 10¹⁰ gives n_i = √(10³²) = ' + N('10¹⁶ m⁻³') + ' and it is n-type')
d.basic('JEE pattern: a diode with 0.7 V drop in series with 100 Ω across a 5.7 V battery, forward biased. Current?', 'I = (5.7 − 0.7)/100 = ' + N('50 mA'))
d.basic('JEE pattern: an ideal diode circuit: two diodes in parallel branches with different resistors, which conducts?', 'The diode whose ' + T('anode is at the higher potential') + ' (forward biased) conducts; the other is reverse biased and acts as an open circuit')
d.basic('Board pattern: differentiate between intrinsic and extrinsic semiconductors.', 'Intrinsic: pure, n_e = n_h, conductivity small and strongly temperature-dependent<br>Extrinsic: doped, n_e ≠ n_h, much higher conductivity from majority carriers')
d.basic('Board pattern: differentiate n-type and p-type.', 'n-type: pentavalent donor, electrons majority, donor level just below E_C<br>p-type: trivalent acceptor, holes majority, acceptor level just above E_V')

# ---------------------------------------------------------------- Summary
d.sec('summary')
table_card(d, 'Summary', 'Fact?', [
    ('Insulator band gap', 'E_g > 3 eV', False), ('Semiconductor band gap', 'E_g between 0.2 and 3 eV (Si 1.1, Ge 0.7)', False), ('Metal', 'E_g ≈ 0 (bands overlap)', False),
    ('Intrinsic', 'n_e = n_h = n_i', False), ('Mass action', 'n_e n_h = n_i²', False), ('n-type / p-type dopants', 'Pentavalent (donor) / trivalent (acceptor)', False),
    ('Forward bias', 'p to +; barrier V₀ − V; mA current', False), ('Reverse bias', 'p to −; barrier V₀ + V; µA current', False),
    ('Cut-in voltage', '0.7 V (Si), 0.2 V (Ge)', False), ('Rectifier output frequency', 'Half-wave f; full-wave 2f', False)],
    term='Chapter 14 summary')
table_card(d, 'Concept checks', 'True or false?', [
    ('A pure semiconductor at 0 K behaves as an insulator', 'True', False), ('Adding pentavalent impurity makes a p-type semiconductor', 'False (n-type)', True),
    ('Depletion region has many mobile charges', 'False (immobile ions only)', True), ('Forward bias narrows the depletion layer', 'True', False),
    ('Reverse saturation current strongly depends on the applied voltage', 'False (nearly constant)', True), ('Full-wave rectifier output has twice the input frequency', 'True', False)],
    term='Chapter 14 concept checks')

print(d.write(os.path.join(OUT, 'deck.json')), 'cards')
