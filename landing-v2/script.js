/* ==========================================================================
   Erudite Flashcards - Landing Page JavaScript (v2)
   10x Refined Study Interactions: Keyboard Shortcuts, Web Audio, Deck Filter & FAQ
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // --- 1. Web Audio Sound Engine ---
  let soundEnabled = true;
  const soundToggleBtn = document.getElementById('sound-toggle');
  
  const audioSounds = {
    flip: new Audio('assets/audio/flip-sound.mp3'),
    click: new Audio('assets/audio/click.mp3'),
    next: new Audio('assets/audio/Next-card.mp3')
  };

  Object.values(audioSounds).forEach(audio => {
    audio.volume = 0.4;
  });

  function playSound(soundKey) {
    if (!soundEnabled) return;
    const sound = audioSounds[soundKey];
    if (sound) {
      sound.currentTime = 0;
      sound.play().catch(err => {
        console.warn('Audio playback prevented:', err);
      });
    }
  }

  if (soundToggleBtn) {
    soundToggleBtn.addEventListener('click', () => {
      soundEnabled = !soundEnabled;
      soundToggleBtn.classList.toggle('active', soundEnabled);
      soundToggleBtn.setAttribute('aria-label', soundEnabled ? 'Mute audio' : 'Unmute audio');
      if (soundEnabled) playSound('click');
    });
  }

  // --- 2. Header Scroll Backdrop Blur ---
  const header = document.getElementById('main-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }, { passive: true });
  }

  // --- 3. Mobile Navigation Menu Toggle ---
  const mobileToggle = document.getElementById('mobile-toggle');
  const navLinks = document.getElementById('nav-links');
  if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', () => {
      const isOpen = navLinks.classList.toggle('open');
      mobileToggle.setAttribute('aria-expanded', isOpen);
      playSound('click');
    });
  }

  // --- 4. Interactive 3D Flashcard Deck Engine & Keyboard Shortcuts ---
  const sampleCards = [
    {
      deck: 'NCERT Class 12 Biology',
      question: 'What organelle produces ATP via oxidative phosphorylation during cellular respiration?',
      answer: 'Mitochondria (The powerhouse of the cell)',
      explanation: 'The inner mitochondrial membrane houses the Electron Transport Chain (ETC) and ATP Synthase complexes.'
    },
    {
      deck: 'Human Anatomy & Physiology',
      question: 'Which valve prevents backflow of blood from the left ventricle into the left atrium?',
      answer: 'Bicuspid (Mitral) Valve',
      explanation: 'It consists of two cusps and closes during ventricular systole to prevent regurgitation into the left atrium.'
    },
    {
      deck: 'FSRS Memory Science',
      question: 'What parameters does the FSRS algorithm compute to determine the next review date?',
      answer: 'Stability (S), Difficulty (D), and Retrievability (R)',
      explanation: 'FSRS calculates memory stability and retrievability based on your target retention probability (e.g. 90%).'
    },
    {
      deck: 'Biochemistry & Enzymes',
      question: 'What is the primary function of Ribulose-1,5-bisphosphate carboxylase-oxygenase (RuBisCO)?',
      answer: 'Carbon Fixation in the Calvin Cycle',
      explanation: 'RuBisCO catalyzes the first major step of carbon fixation, incorporating CO2 into ribulose 1,5-bisphosphate.'
    }
  ];

  let currentCardIndex = 0;
  const cardElement = document.getElementById('demo-card');
  const cardQuestionEl = document.getElementById('card-question');
  const cardAnswerEl = document.getElementById('card-answer');
  const cardExplanationEl = document.getElementById('card-explanation');
  const deckTagEl = document.getElementById('deck-tag');
  const cardCounterEl = document.getElementById('card-counter');
  const srsControlsEl = document.getElementById('srs-controls');

  function renderCurrentCard() {
    const cardData = sampleCards[currentCardIndex];
    if (!cardData) return;

    deckTagEl.textContent = cardData.deck;
    cardQuestionEl.textContent = cardData.question;
    cardAnswerEl.textContent = cardData.answer;
    cardExplanationEl.textContent = cardData.explanation;
    cardCounterEl.textContent = `Card ${currentCardIndex + 1} of ${sampleCards.length}`;

    cardElement.classList.remove('flipped');
    srsControlsEl.classList.remove('visible');
  }

  function advanceCard() {
    playSound('next');
    currentCardIndex = (currentCardIndex + 1) % sampleCards.length;
    
    cardElement.style.opacity = '0.5';
    cardElement.style.transform = 'scale(0.98)';
    
    setTimeout(() => {
      renderCurrentCard();
      cardElement.style.opacity = '1';
      cardElement.style.transform = 'none';
    }, 200);
  }

  function toggleFlip() {
    const isFlipped = cardElement.classList.toggle('flipped');
    playSound('flip');

    if (isFlipped) {
      srsControlsEl.classList.add('visible');
    } else {
      srsControlsEl.classList.remove('visible');
    }
  }

  if (cardElement) {
    cardElement.addEventListener('click', (e) => {
      if (e.target.closest('.srs-btn')) return;
      toggleFlip();
    });

    const srsButtons = document.querySelectorAll('.srs-btn');
    srsButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        advanceCard();
      });
    });

    renderCurrentCard();
  }

  // Keyboard Shortcuts Listener for Power Users
  document.addEventListener('keydown', (e) => {
    if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;

    if (e.code === 'Space') {
      e.preventDefault();
      toggleFlip();
    } else if (['Digit1', 'Digit2', 'Digit3', 'Digit4'].includes(e.code)) {
      e.preventDefault();
      advanceCard();
    } else if (e.code === 'KeyM') {
      if (soundToggleBtn) soundToggleBtn.click();
    }
  });

  // --- 5. Filterable NCERT Deck Browser ---
  const chapterData = [
    { title: 'Ch 1: The Living World', category: 'class11', cards: '240 Cards' },
    { title: 'Ch 2: Biological Classification', category: 'class11', cards: '315 Cards' },
    { title: 'Ch 3: Plant Kingdom', category: 'class11', cards: '410 Cards' },
    { title: 'Ch 4: Animal Kingdom', category: 'class11', cards: '490 Cards' },
    { title: 'Ch 8: Cell - Unit of Life', category: 'class11', cards: '520 Cards' },
    { title: 'Ch 10: Cell Cycle & Division', category: 'class11', cards: '380 Cards' },
    { title: 'Ch 1: Reproduction in Organisms', category: 'class12', cards: '180 Cards' },
    { title: 'Ch 2: Sexual Reproduction in Flowering Plants', category: 'class12', cards: '460 Cards' },
    { title: 'Ch 3: Human Reproduction', category: 'class12', cards: '510 Cards' },
    { title: 'Ch 5: Principles of Inheritance & Variation', category: 'class12', cards: '640 Cards' },
    { title: 'Ch 6: Molecular Basis of Inheritance', category: 'class12', cards: '720 Cards' },
    { title: 'Ch 8: Human Health & Disease', category: 'class12', cards: '580 Cards' }
  ];

  const chaptersContainer = document.getElementById('chapters-grid');
  const filterButtons = document.querySelectorAll('.filter-btn');

  function renderChapters(filterCategory = 'all') {
    if (!chaptersContainer) return;
    chaptersContainer.innerHTML = '';

    const filtered = chapterData.filter(ch => filterCategory === 'all' || ch.category === filterCategory);

    filtered.forEach(ch => {
      const card = document.createElement('div');
      card.className = 'chapter-item-card';
      card.innerHTML = `
        <span>${ch.title}</span>
        <span class="chapter-count">${ch.cards}</span>
      `;
      chaptersContainer.appendChild(card);
    });
  }

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      playSound('click');
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const cat = btn.getAttribute('data-filter') || 'all';
      renderChapters(cat);
    });
  });

  renderChapters('all');

  // --- 6. Interactive FAQ Accordion Handler ---
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const headerBtn = item.querySelector('.faq-header');
    if (headerBtn) {
      headerBtn.addEventListener('click', () => {
        playSound('click');
        const isOpen = item.classList.contains('open');

        faqItems.forEach(other => {
          if (other !== item) other.classList.remove('open');
        });

        item.classList.toggle('open', !isOpen);
      });
    }
  });
});
