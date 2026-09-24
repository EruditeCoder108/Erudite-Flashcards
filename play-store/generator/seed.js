/*
 * Mock study library for Play Store screenshots. Runs inside the app page.
 * Review history is produced by the real FSRS scheduler with a faked clock, so
 * streaks, heatmaps, retention, and forecasts are the app's own numbers.
 */
(function () {
  'use strict';

  const DAY = 24 * 60 * 60 * 1000;
  const HISTORY_DAYS = 62;

  const CLASSES = [
    { id: 'neet-bio', name: 'NEET Biology', color: '#4FD69C', icon: 'fa-dna' },
    { id: 'jee-chem', name: 'JEE Chemistry', color: '#F2B544', icon: 'fa-flask' },
    { id: 'physics', name: 'Physics', color: '#8EA4FF', icon: 'fa-atom' },
    { id: 'languages', name: 'Languages', color: '#FF8A7A', icon: 'fa-language' }
  ];

  const CELL = [
    ['Which organelle is called the “suicide bag” of the cell?', '<b>Lysosome</b>. Its hydrolytic enzymes digest worn-out organelles and foreign material.'],
    ['Site of aerobic respiration in a eukaryotic cell?', '<b>Mitochondria</b>, the inner membrane folds into cristae.'],
    ['Sedimentation coefficient of prokaryotic ribosomes?', '<b>70S</b>, made of 50S and 30S subunits.'],
    ['Who proposed that all cells arise from pre-existing cells?', '<b>Rudolf Virchow</b> (1855): <i>omnis cellula-e cellula</i>.'],
    ['Model that describes the structure of the plasma membrane?', '<b>Fluid mosaic model</b>, Singer and Nicolson (1972).'],
    ['Which organelle packages and modifies proteins for secretion?', '<b>Golgi apparatus</b>, working from its cis to trans face.'],
    ['Function of the nucleolus?', 'Site of <b>rRNA synthesis</b> and ribosome subunit assembly.'],
    ['What do centrioles form in animal cells?', 'The <b>spindle apparatus</b> and the basal bodies of cilia and flagella.'],
    ['Which ER lacks ribosomes and makes lipids?', '<b>Smooth ER</b> (SER), also the site of steroid hormone synthesis.'],
    ['Name the pigment-containing plastids.', '<b>Chromoplasts</b>, with carotenoids such as carotene and xanthophyll.']
  ];
  const NEURAL = [
    ['Resting membrane potential of a neuron?', 'About <b>-70 mV</b>, inside negative.'],
    ['Which ion rushes in during depolarisation?', '<b>Na⁺</b>, through voltage-gated sodium channels.'],
    ['Part of the brain that controls balance and posture?', '<b>Cerebellum</b>.'],
    ['Neurotransmitter at the neuromuscular junction?', '<b>Acetylcholine</b>.']
  ];
  const BONDING = [
    ['Shape of SF₄ according to VSEPR theory?', '<b>See-saw</b> (4 bond pairs, 1 lone pair).'],
    ['Bond order of O₂ from molecular orbital theory?', '<b>2</b>, and O₂ is paramagnetic.'],
    ['Hybridisation of carbon in ethyne?', '<b>sp</b>, linear, 180°.'],
    ['Which has the higher dipole moment: NH₃ or NF₃?', '<b>NH₃</b>. In NF₃ the lone-pair moment opposes the bond moments.']
  ];
  const MOTION = [
    ['State Newton’s second law of motion.', 'Net force equals rate of change of momentum: <b>F = dp/dt</b>.'],
    ['Why does a gun recoil when fired?', '<b>Conservation of momentum</b>: bullet and gun get equal and opposite momentum.'],
    ['Coefficient of friction on the angle of repose θ?', '<b>μ = tan θ</b>.']
  ];
  const REACTIONS = [
    ['Aldehyde to alcohol and acid with conc. NaOH (no α-H)?', '<b>Cannizzaro reaction</b>.'],
    ['Reagent in the Clemmensen reduction?', '<b>Zn–Hg / conc. HCl</b>; reduces C=O to CH₂.'],
    ['Name the reaction: benzene + CH₃Cl with anhydrous AlCl₃.', '<b>Friedel–Crafts alkylation</b>.']
  ];
  const PLANTS = [
    ['Dominant phase in the bryophyte life cycle?', 'The <b>gametophyte</b>.'],
    ['Which algae store food as floridean starch?', '<b>Red algae</b> (Rhodophyceae).']
  ];
  const POLITY = [
    ['Which article abolishes untouchability?', '<b>Article 17</b>.'],
    ['Right to constitutional remedies is in which article?', '<b>Article 32</b>, called the heart and soul of the Constitution by Dr. Ambedkar.']
  ];
  const WORDS = [
    ['Ephemeral', 'Lasting a very short time.'],
    ['Laconic', 'Using very few words.'],
    ['Obdurate', 'Stubbornly refusing to change one’s opinion.'],
    ['Pellucid', 'Translucently clear; easy to understand.'],
    ['Sagacious', 'Having keen judgement.']
  ];

  const DECKS = [
    { id: 'cell', name: 'Cell: The Unit of Life', classId: 'neet-bio', size: 64, pool: CELL, pinned: true },
    { id: 'neural', name: 'Neural Control and Coordination', classId: 'neet-bio', size: 48, pool: NEURAL },
    { id: 'bonding', name: 'Chemical Bonding and Molecular Structure', classId: 'jee-chem', size: 52, pool: BONDING },
    { id: 'reactions', name: 'Organic Named Reactions', classId: 'jee-chem', size: 36, pool: REACTIONS },
    { id: 'motion', name: 'Laws of Motion', classId: 'physics', size: 40, pool: MOTION },
    { id: 'plants', name: 'Plant Kingdom', classId: 'neet-bio', size: 30, pool: PLANTS },
    { id: 'polity', name: 'Indian Polity: Fundamental Rights', classId: null, size: 28, pool: POLITY },
    { id: 'words', name: 'Vocabulary: High-Frequency Words', classId: 'languages', size: 80, pool: WORDS }
  ];

  // Deterministic randomness so every run produces the same screenshots.
  let seed = 20260924;
  function random() {
    seed = (seed * 1664525 + 1013904223) % 4294967296;
    return seed / 4294967296;
  }

  function withClock(time, work) {
    const RealDate = window.Date;
    class FakeDate extends RealDate {
      constructor(...args) {
        if (args.length) super(...args);
        else super(time);
      }
      static now() {
        return time;
      }
    }
    window.Date = FakeDate;
    try {
      return work();
    } finally {
      window.Date = RealDate;
    }
  }

  function pickRating(lapses) {
    const roll = random();
    if (roll < 0.07 + lapses * 0.02) return 'Again';
    if (roll < 0.15) return 'Hard';
    if (roll < 0.93) return 'Good';
    return 'Easy';
  }

  function buildCards(deck) {
    return Array.from({ length: deck.size }, (_, index) => {
      const [term, definition] = deck.pool[index % deck.pool.length];
      return { id: `${deck.id}-${index}`, term, definition };
    });
  }

  function simulate(deck, cards, todayStart, options) {
    const settings = {};
    // Introduce about 85% of the deck over the history; the rest stay new.
    const perDayNew = (deck.size * 0.85) / HISTORY_DAYS;
    let newBudget = 0;
    let introduced = 0;
    for (let day = HISTORY_DAYS; day >= 0; day -= 1) {
      const dayStart = todayStart - day * DAY;
      let minute = 18 * 60 + Math.floor(random() * 150);
      const due = cards.filter(card => card.srs && new Date(card.srs.due).getTime() <= dayStart + 22 * 60 * 60 * 1000);
      newBudget += perDayNew;
      const freshCount = day === 0 ? 0 : Math.floor(newBudget);
      newBudget -= freshCount;
      const fresh = cards.filter(card => !card.srs).slice(0, freshCount);
      introduced += fresh.length;
      let queue = [...due, ...fresh];
      if (day === 0) queue = queue.slice(0, Math.ceil(queue.length * options.todayShare));
      queue.forEach(card => {
        minute += 1 + Math.floor(random() * 2);
        const time = dayStart + minute * 60 * 1000;
        const previous = card.srs;
        const rating = pickRating(Number(previous?.lapses || 0));
        const reviewed = withClock(time, () => window.srsManager.reviewCard({ ...card }, rating, settings));
        const index = cards.indexOf(card);
        cards[index] = {
          ...reviewed,
          reviewHistory: [
            ...(card.reviewHistory || []),
            {
              reviewedAt: new Date(time).toISOString(),
              rating,
              previousState: previous?.state || 'New',
              nextState: reviewed.srs?.state || null,
              previousDue: previous?.due || null,
              nextDue: reviewed.srs?.due || null,
              durationMs: 3500 + Math.round(random() * 9000)
            }
          ]
        };
      });
    }
    return introduced;
  }

  function drawCellDiagram() {
    const width = 1200;
    const height = 900;
    const canvas = document.createElement('canvas');
    canvas.width = width;
    canvas.height = height;
    const g = canvas.getContext('2d');
    g.fillStyle = '#fbf8f2';
    g.fillRect(0, 0, width, height);

    // Cell body
    g.save();
    g.beginPath();
    g.ellipse(560, 470, 380, 300, -0.08, 0, Math.PI * 2);
    g.fillStyle = '#eaf3ea';
    g.fill();
    g.lineWidth = 10;
    g.strokeStyle = '#7fae86';
    g.stroke();
    g.restore();

    // Rough ER
    g.strokeStyle = '#c98fb0';
    g.lineWidth = 9;
    for (let row = 0; row < 4; row += 1) {
      g.beginPath();
      for (let x = 0; x <= 170; x += 5) {
        const y = 300 + row * 22 + Math.sin(x / 14) * 7;
        if (x === 0) g.moveTo(640 + x, y); else g.lineTo(640 + x, y);
      }
      g.stroke();
      g.fillStyle = '#7d4d6a';
      for (let x = 8; x <= 170; x += 22) {
        g.beginPath();
        g.arc(640 + x, 300 + row * 22 + Math.sin(x / 14) * 7 - 7, 3.2, 0, Math.PI * 2);
        g.fill();
      }
    }

    // Nucleus
    g.beginPath();
    g.arc(520, 450, 120, 0, Math.PI * 2);
    g.fillStyle = '#d9e2f7';
    g.fill();
    g.lineWidth = 8;
    g.strokeStyle = '#6f86c9';
    g.stroke();
    g.beginPath();
    g.arc(545, 430, 38, 0, Math.PI * 2);
    g.fillStyle = '#6f86c9';
    g.fill();

    // Mitochondria
    [[340, 640, 0.5], [760, 610, -0.3]].forEach(([x, y, angle]) => {
      g.save();
      g.translate(x, y);
      g.rotate(angle);
      g.beginPath();
      g.ellipse(0, 0, 70, 34, 0, 0, Math.PI * 2);
      g.fillStyle = '#f6d7b8';
      g.fill();
      g.lineWidth = 6;
      g.strokeStyle = '#d08a4c';
      g.stroke();
      g.beginPath();
      for (let x = -52; x <= 52; x += 4) g.lineTo(x, Math.sin(x / 6) * 16);
      g.lineWidth = 4;
      g.stroke();
      g.restore();
    });

    // Golgi
    g.strokeStyle = '#d6a531';
    g.lineCap = 'round';
    for (let arc = 0; arc < 4; arc += 1) {
      g.beginPath();
      g.arc(760, 460, 60 + arc * 13, Math.PI * 0.85, Math.PI * 1.35);
      g.lineWidth = 9;
      g.stroke();
    }

    // Lysosome
    g.beginPath();
    g.arc(420, 280, 28, 0, Math.PI * 2);
    g.fillStyle = '#e9b4b4';
    g.fill();
    g.lineWidth = 5;
    g.strokeStyle = '#b86363';
    g.stroke();

    // Labels and leader lines
    const labels = [
      ['Nucleus', 60, 470, 400, 450],
      ['Lysosome', 60, 250, 392, 280],
      ['Mitochondrion', 60, 790, 300, 660],
      ['Cell membrane', 60, 140, 330, 210],
      ['Rough ER', 960, 250, 810, 320],
      ['Golgi apparatus', 960, 470, 800, 460],
      ['Cytoplasm', 960, 720, 700, 690]
    ];
    const boxes = [];
    g.font = '600 34px Geist, Arial, sans-serif';
    g.textBaseline = 'middle';
    labels.forEach(([text, x, y, tx, ty]) => {
      const textWidth = g.measureText(text).width;
      const right = x > 600;
      const lineStart = right ? x - 14 : x + textWidth + 14;
      g.strokeStyle = '#8b8374';
      g.lineWidth = 2.5;
      g.beginPath();
      g.moveTo(lineStart, y);
      g.lineTo(tx, ty);
      g.stroke();
      g.fillStyle = '#26231e';
      g.fillText(text, x, y);
      boxes.push({ text, x: x - 8, y: y - 26, w: textWidth + 16, h: 52 });
    });
    return { dataUrl: canvas.toDataURL('image/webp', 0.9), width, height, boxes };
  }

  function occlusionDeck(diagram) {
    const masks = diagram.boxes.map((box, index) => ({
      id: `m${index}`,
      shape: 'rect',
      x: box.x / diagram.width,
      y: box.y / diagram.height,
      w: box.w / diagram.width,
      h: box.h / diagram.height,
      answer: box.text,
      hint: ''
    }));
    const target = masks.findIndex(mask => mask.answer === 'Golgi apparatus');
    const ordered = [masks[target], ...masks.filter((_, index) => index !== target)];
    return {
      id: 'cell-diagram',
      name: 'Animal Cell: Label the Diagram',
      classId: 'neet-bio',
      cards: ordered.map(mask => ({
        id: `cell-diagram-${mask.id}`,
        noteId: 'cell-diagram-note',
        noteType: 'image-occlusion',
        cardTemplate: 'image-occlusion-mask',
        term: '<strong>Name the hidden structure.</strong>',
        definition: mask.answer,
        termImage: diagram.dataUrl,
        definitionImage: diagram.dataUrl,
        noteFields: { answer: mask.answer, hint: '', maskId: mask.id },
        imageOcclusion: {
          version: 1,
          image: diagram.dataUrl,
          guessMode: 'hide-all',
          imageWidth: diagram.width,
          imageHeight: diagram.height,
          masks,
          targetMaskId: mask.id,
          targetMaskIndex: masks.indexOf(mask)
        }
      }))
    };
  }

  async function seedStoreData() {
    const store = window.flashcardStore;
    const now = Date.now();
    const today = new Date(now - 4 * 60 * 60 * 1000);
    today.setHours(4, 0, 0, 0);
    const todayStart = today.getTime();

    for (const classData of CLASSES) await store.saveClass(classData);
    let order = 0;
    for (const deck of DECKS) {
      const cards = buildCards(deck);
      simulate(deck, cards, todayStart, { todayShare: 0.55 });
      order += 1;
      await store.saveSet({
        id: deck.id,
        name: deck.name,
        classId: deck.classId,
        pinned: Boolean(deck.pinned),
        cards,
        created: todayStart - (HISTORY_DAYS + order) * DAY,
        lastOpened: now - order * 3600 * 1000
      });
    }

    for (let day = HISTORY_DAYS; day >= 0; day -= 1) {
      const start = todayStart - day * DAY + 18 * 3600 * 1000;
      await store.saveStudySession({
        id: `mock-session-${day}`,
        setId: DECKS[day % DECKS.length].id,
        startedAt: start,
        durationMs: (14 + Math.round(random() * 30)) * 60 * 1000,
        cardsViewed: 40 + Math.round(random() * 60),
        mode: 'srs'
      });
    }
    const settings = await store.getSettings();
    // Two new cards per deck keeps today's queue realistic.
    await store.saveSettings({ ...settings, srsDefaults: { newCardsPerDay: 2 }, reminder: { enabled: true, hour: 19, minute: 0 } });
    await store.flush?.();
  }

  async function seedOcclusion() {
    const diagram = drawCellDiagram();
    await window.flashcardStore.saveSet(occlusionDeck(diagram));
    await window.flashcardStore.flush?.();
  }

  // A small deck whose first card is the one shown in the study screenshots.
  async function seedShowcaseStudy() {
    const cards = CELL.slice(0, 6).map(([term, definition], index) => ({ id: `show-${index}`, term, definition }));
    await window.flashcardStore.saveSet({ id: 'showcase', name: 'Cell: The Unit of Life', classId: 'neet-bio', srsSettings: { newCardsPerDay: 20 }, cards });
    await window.flashcardStore.flush?.();
  }

  window.EruditeStoreSeed = { seedStoreData, seedOcclusion, seedShowcaseStudy };
}());
