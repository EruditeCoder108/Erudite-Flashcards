(() => {
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];

  const header = $('[data-header]');
  const menuButton = $('[data-menu-button]');
  const mobileMenu = $('[data-mobile-menu]');
  const menuLabel = $('.sr-only', menuButton);
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Header & Mobile Nav Toggle
  const setMenu = (open) => {
    menuButton?.setAttribute('aria-expanded', String(open));
    mobileMenu?.classList.toggle('is-open', open);
    document.body.classList.toggle('menu-open', open);
    if (menuLabel) menuLabel.textContent = open ? 'Close navigation menu' : 'Open navigation menu';
  };

  menuButton?.addEventListener('click', () => {
    setMenu(menuButton.getAttribute('aria-expanded') !== 'true');
  });

  $$('#mobile-menu a').forEach((link) => link.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menuButton?.getAttribute('aria-expanded') === 'true') {
      setMenu(false);
      menuButton.focus();
    }
  });

  // Header Scroll State
  const onScroll = () => {
    header?.classList.toggle('is-scrolled', window.scrollY > 18);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Mobile Floating Quick-Dock (<620px screens)
  const quickDock = $('[data-quick-dock]');
  const onScrollDock = () => {
    if (quickDock) {
      quickDock.classList.toggle('is-visible', window.scrollY > 420);
    }
  };
  onScrollDock();
  window.addEventListener('scroll', onScrollDock, { passive: true });

  // Study Console Logic
  const consoleEl = $('[data-study-console]');
  const modeButtons = $$('[data-mode]', consoleEl);
  const normalControls = $('[data-normal-controls]', consoleEl);
  const ratingControls = $('[data-rating-controls]', consoleEl);
  const consoleCopy = $('[data-console-copy]', consoleEl);
  const consoleState = $('[data-console-state]', consoleEl);
  const flashcard = $('[data-flashcard]', consoleEl);
  const counterCurrent = $('[data-counter-current]', consoleEl);
  const progress = $('.progress-track span', consoleEl);
  let currentCard = 18;

  const setMode = (mode) => {
    modeButtons.forEach((button) => {
      const active = button.dataset.mode === mode;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-selected', String(active));
    });

    const smart = mode === 'smart';
    if (normalControls) normalControls.hidden = smart;
    if (ratingControls) ratingControls.hidden = !smart;
    if (consoleCopy) consoleCopy.textContent = smart ? 'Rate recall effort. Erudite schedules the next review.' : 'Flip. Recall. Continue.';
    if (consoleState) consoleState.textContent = smart ? 'LEARNING (FSRS)' : 'NORMAL MODE';
    consoleEl?.classList.toggle('is-smart', smart);
  };

  modeButtons.forEach((button) => button.addEventListener('click', () => setMode(button.dataset.mode)));
  flashcard?.addEventListener('click', () => flashcard.classList.toggle('is-flipped'));

  $('[data-next-card]')?.addEventListener('click', () => {
    currentCard = Math.min(367, currentCard + 1);
    if (counterCurrent) counterCurrent.textContent = currentCard;
    if (progress) progress.style.width = `${Math.max(4, (currentCard / 367) * 100)}%`;
    flashcard?.classList.remove('is-flipped');
  });

  $$('[data-rating]', consoleEl).forEach((button) => {
    button.addEventListener('click', () => {
      currentCard = Math.min(367, currentCard + 1);
      if (counterCurrent) counterCurrent.textContent = currentCard;
      if (consoleState) consoleState.textContent = button.dataset.rating === 'again' ? 'RELEARNING' : 'REVIEW';
      flashcard?.classList.remove('is-flipped');
      if (!prefersReducedMotion) {
        button.animate([
          { transform: 'scale(1)' },
          { transform: 'scale(.94)' },
          { transform: 'scale(1)' }
        ], { duration: 180 });
      }
    });
  });

  $('[data-scroll-smart]')?.addEventListener('click', () => {
    consoleEl?.scrollIntoView({ behavior: prefersReducedMotion ? 'auto' : 'smooth', block: 'center' });
    window.setTimeout(() => setMode('smart'), prefersReducedMotion ? 0 : 450);
  });

  // Android Screenshot Showcase Controller
  const showcaseTabs = $$('.showcase-tab');
  const showcaseShots = $$('.screen-shot');
  const showcaseGallery = $('[data-showcase-gallery]');
  const showcaseDots = $$('[data-showcase-dots] span');

  const activateShowcase = (index) => {
    showcaseTabs.forEach((tab, i) => {
      const active = i === index;
      tab.classList.toggle('is-active', active);
      tab.setAttribute('aria-selected', String(active));
    });

    showcaseShots.forEach((shot, i) => {
      shot.classList.toggle('is-active', i === index);
    });

    showcaseDots.forEach((dot, i) => {
      dot.classList.toggle('is-active', i === index);
    });

    if (window.innerWidth <= 620 && showcaseGallery && showcaseShots[index]) {
      const targetShot = showcaseShots[index];
      showcaseGallery.scrollTo({ left: targetShot.offsetLeft - 14, behavior: 'smooth' });
    }
  };

  showcaseTabs.forEach((tab) => {
    tab.addEventListener('click', () => {
      const idx = Number(tab.dataset.tab);
      activateShowcase(idx);
    });
  });

  if (showcaseGallery) {
    showcaseGallery.addEventListener('scroll', () => {
      if (window.innerWidth <= 620) {
        const scrollPos = showcaseGallery.scrollLeft;
        const width = showcaseGallery.offsetWidth;
        const newIndex = Math.round(scrollPos / (width * 0.75));
        if (newIndex >= 0 && newIndex < showcaseShots.length) {
          showcaseDots.forEach((dot, i) => dot.classList.toggle('is-active', i === newIndex));
          showcaseTabs.forEach((tab, i) => {
            tab.classList.toggle('is-active', i === newIndex);
            tab.setAttribute('aria-selected', String(i === newIndex));
          });
        }
      }
    }, { passive: true });
  }

  // FSRS Retention Instrument Slider
  const retentionInstrument = $('[data-retention-instrument]');
  const slider = $('[data-retention-slider]', retentionInstrument);
  const retentionValue = $('[data-retention-value]', retentionInstrument);
  const expectedInterval = $('[data-expected-interval]', retentionInstrument);
  const reviewInterval = $('[data-review-interval]', retentionInstrument);
  const dailyLoad = $('[data-daily-load]', retentionInstrument);

  const retentionMap = {
    80: [24, 21], 81: [23, 22], 82: [22, 23], 83: [21, 24],
    84: [20, 25], 85: [19, 27], 86: [18, 29], 87: [16, 31],
    88: [15, 33], 89: [13, 35], 90: [12, 38], 91: [10, 42],
    92: [9, 46], 93: [8, 51], 94: [7, 57], 95: [6, 64]
  };

  const updateRetention = () => {
    if (!slider) return;
    const value = Number(slider.value);
    const [days, load] = retentionMap[value] || [12, 38];
    if (retentionValue) retentionValue.textContent = value;
    if (expectedInterval) expectedInterval.textContent = `${days} ${days === 1 ? 'day' : 'days'}`;
    if (reviewInterval) reviewInterval.textContent = `${days}d`;
    if (dailyLoad) dailyLoad.textContent = `${load} cards`;
    slider.style.setProperty('--retention-progress', `${((value - 80) / 15) * 100}%`);
  };

  slider?.addEventListener('input', updateRetention);
  if (slider) updateRetention();

  // Image Occlusion Interactive Mask Reveal
  const maskAnswer = $('[data-mask-answer]');
  $$('[data-mask]').forEach((mask) => {
    mask.addEventListener('click', () => {
      $$('[data-mask]').forEach((item) => {
        item.classList.remove('is-revealed');
        item.textContent = item.dataset.original || item.textContent;
      });
      if (!mask.dataset.original) mask.dataset.original = mask.textContent;
      mask.classList.add('is-revealed');
      mask.textContent = mask.dataset.label;
      if (maskAnswer) maskAnswer.textContent = `Answer: ${mask.dataset.label}`;
    });
  });

  // AI Prompt Builder Preset Chips & Copy Button
  const promptPresets = {
    biology: `Generate a JSON flashcard deck for NEET Biology on "Cell Structure & Function" with 15 Cloze and Basic cards following the Erudite JSON schema: {"deckTitle":"Cell Structure", "cards":[{"type":"cloze","text":"The {{c1::mitochondrion}} produces ATP."}]}`,
    chemistry: `Generate a JSON flashcard deck for Chemistry on "Chemical Bonding & Molecular Structure" with 12 Cloze and Formula cards formatted for KaTeX equations in Erudite schema.`,
    language: `Generate a JSON flashcard deck for Spanish Vocabulary (Advanced B2) with 20 Basic+Reverse cards including audio pronunciation tags and context sentences.`
  };

  const promptChips = $$('[data-preset]');
  const promptOutput = $('[data-prompt-text]');
  const copyPromptBtn = $('[data-copy-prompt]');

  promptChips.forEach((chip) => {
    chip.addEventListener('click', () => {
      promptChips.forEach((c) => c.classList.remove('is-selected'));
      chip.classList.add('is-selected');
      const key = chip.dataset.preset;
      if (promptOutput && promptPresets[key]) {
        promptOutput.textContent = promptPresets[key];
      }
    });
  });

  copyPromptBtn?.addEventListener('click', () => {
    if (promptOutput) {
      navigator.clipboard.writeText(promptOutput.textContent.trim()).then(() => {
        const orig = copyPromptBtn.textContent;
        copyPromptBtn.textContent = '✓ Copied!';
        setTimeout(() => { copyPromptBtn.textContent = orig; }, 2000);
      }).catch(() => {
        alert('Prompt copied to clipboard!');
      });
    }
  });

  // FAQ Accordion Controller
  $$('.faq-item').forEach((item) => {
    const trigger = $('.faq-trigger', item);
    const panel = $('.faq-panel', item);

    trigger?.addEventListener('click', () => {
      const isOpen = item.classList.contains('is-open');
      $$('.faq-item').forEach((other) => {
        other.classList.remove('is-open');
        $('.faq-trigger', other)?.setAttribute('aria-expanded', 'false');
        $('.faq-panel', other)?.setAttribute('hidden', '');
      });

      if (!isOpen) {
        item.classList.add('is-open');
        trigger.setAttribute('aria-expanded', 'true');
        panel?.removeAttribute('hidden');
      }
    });
  });

  // NCERT Volume Drawers
  $$('[data-volume]').forEach((volume) => {
    const button = $('.volume-toggle', volume);
    const drawer = $('.chapter-drawer', volume);
    button?.addEventListener('click', () => {
      const open = !volume.classList.contains('is-open');
      volume.classList.toggle('is-open', open);
      button.setAttribute('aria-expanded', String(open));
      drawer?.setAttribute('aria-hidden', String(!open));
    });
  });

  // IntersectionObserver for Reveal Animations
  const revealItems = $$('[data-reveal]');
  if (prefersReducedMotion) {
    revealItems.forEach((item) => item.classList.add('is-visible'));
  } else if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px' });
    revealItems.forEach((item) => observer.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add('is-visible'));
  }
})();
