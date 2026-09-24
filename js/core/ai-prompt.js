(function (root, factory) {
  const api = factory();
  root.EruditeCore = root.EruditeCore || {};
  root.EruditeCore.aiPrompt = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof globalThis !== 'undefined' ? globalThis : window, function () {
  // Builds the instructions a learner pastes into ChatGPT, Claude, or Gemini
  // together with a chapter PDF. The AI returns a Smriti package that the app
  // imports. Every section here exists because a real import failed or a real
  // deck came back weak without it; keep additions just as specific.

  const PRESET_BRIEFS = {
    beginner: 'The learner has not mastered this chapter yet. Teach through the cards: simple wording, one memory point per card, and a short reason or example where it helps understanding.',
    revision: 'The learner has studied this chapter and wants efficient revision. Compress it into high-yield cards that are fast to review but still complete. Skip obvious basics unless they are examinable.',
    competitive: 'The learner is preparing for a competitive exam. Turn the chapter into dense, testable prompts: definitions, distinctions, exceptions, values, sequences, and trap points. Prefer precision over friendly explanation.',
    mastery: 'The learner wants durable, flexible understanding. Include core facts, the links between them, edge cases, and common misconceptions, not only isolated definitions.'
  };

  const EXAM_TARGETS = {
    school: 'Target: school exams. Weight definitions, core concepts, examples, comparisons, cause and effect, processes, labelled diagrams, tables, formulae, and units.',
    neet: 'Target: NEET. Preserve NCERT line-level facts: terminology, examples, exceptions, processes, labelled diagrams, table comparisons, values, classifications, and statement-based traps.',
    jee: 'Target: JEE. Focus on concepts, formula choice, variables, units, dimensions, assumptions, sign conventions, limiting cases, graphs, reactions, mechanisms, and standard results.',
    ssc: 'Target: SSC. Prioritise direct recall: definitions, classifications, lists, chronology, dates, and one-line distinctions. Keep answers extremely short.',
    upsc: 'Target: UPSC. Preserve dates, chronology, people, places, institutions, terminology, causes and consequences, and statement-based traps, with enough framing to support mains answers.'
  };

  const STUDIED_STATES = {
    yes: 'The learner has already studied this chapter: spend cards on high-yield recall, exceptions, and confusions, not on basics.',
    no: 'The learner has not studied this chapter yet: build a foundation first, while keeping every card atomic.',
    somewhat: 'The learner is partly familiar with the chapter: balance foundation cards with revision cards.'
  };

  const COVERAGE = {
    light: 'Coverage: essentials only, about 40 to 80 cards for a typical chapter. Include only frequently tested ideas.',
    standard: 'Coverage: balanced, about 80 to 160 cards for a typical chapter. Everything examinable, nothing padded.',
    detailed: 'Coverage: detailed, about 160 to 300 cards for a typical chapter. Add important examples, exceptions, comparisons, and diagram parts.',
    exhaustive: 'Coverage: exhaustive, about 300 to 600 cards for a typical chapter. Every supported testable detail, including captions, tables, boxes, and exercises. Exhaustive still means one fact per card and no repeats.'
  };

  const ANSWER_STYLES = {
    compact: 'Answers: compact. A word, a phrase, one sentence, or a tiny list.',
    keywords: 'Answers: keywords only. No explanatory sentences.',
    explained: 'Answers: the fact first, then at most one short sentence of reasoning when it aids understanding.',
    memory: 'Answers: the fact first, then a short memory hook or a "not to be confused with" cue when one genuinely helps.'
  };

  const CARD_MIXES = {
    simple: 'Card mix: mostly basic and cloze cards. Reverse only for true term and definition pairs. Advanced HTML only when a table is clearly better than text.',
    balanced: 'Card mix: basic and cloze cards for most facts, with reverse, image occlusion, and advanced HTML wherever each clearly serves recall.',
    visual: 'Card mix: image occlusion for every examinable labelled diagram or map, advanced HTML for comparison tables, timelines, and flowcharts; plain cards for everything else.',
    'exam-drill': 'Card mix: short direct questions, cloze for statement facts, reverse for definitions, and small comparison cards for confusable pairs. No decorative visuals.'
  };

  // Used when the output cannot carry image occlusion (text formats, Gemini, or media off).
  const CARD_MIXES_WITHOUT_OCCLUSION = {
    balanced: 'Card mix: basic and cloze cards for most facts, with reverse and advanced HTML wherever each clearly serves recall.',
    visual: 'Card mix: advanced HTML for comparison tables, timelines, and flowcharts; plain cards for everything else.'
  };

  const LANGUAGES = {
    english: 'Write every card in English, even if the source is in another language.',
    hindi: 'Write every card in Hindi.',
    hinglish: 'Write every card in Hinglish (Hindi in Latin script mixed with English), keeping technical terms accurate and in English.'
  };

  const SAFE_MEDIA_EXTENSIONS = '.webp, .png, .jpg, .jpeg, .gif, .mp3, .wav, .ogg, .mp4, or .webm';

  function clean(value) {
    return String(value || '').trim();
  }

  function learningBrief(options) {
    const parts = [
      'You are writing spaced-repetition flashcards for the Smriti flashcards app from the source material attached to this message.',
      PRESET_BRIEFS[options.preset] || PRESET_BRIEFS.revision,
      options.examTarget === 'custom'
        ? `Target: ${clean(options.customExamTarget) || 'the learner\'s own exam'}. Adjust emphasis and detail to match it.`
        : (EXAM_TARGETS[options.examTarget] || EXAM_TARGETS.school),
      STUDIED_STATES[options.studiedState] || '',
      COVERAGE[options.detailLevel] || COVERAGE.standard,
      options.language === 'custom'
        ? `Write every card in ${clean(options.customLanguage) || 'English'}.`
        : (LANGUAGES[options.language] || 'Write the cards in the same language as the source.'),
      ANSWER_STYLES[options.answerStyle] || ANSWER_STYLES.compact
    ];
    return parts.filter(Boolean).join('\n');
  }

  function sourceRules() {
    return `SOURCE RULES
- The attached source is the only factual authority. Do not add facts from memory, the web, or other editions unless the learner asks.
- Keep the source's terminology, spellings, names, dates, values, units, formulae, and diagram labels exactly.
- Read everything examinable: main text, definitions, examples, exceptions, tables, figures and captions, boxes, summaries, in-text questions, and exercises. Do not assume they repeat the main text.
- If something is unreadable or ambiguous, skip it. Never guess.
- No cards about chapter titles, learning objectives, or vague overviews.`;
  }

  function cardMix(options) {
    if (options.outputFormat === 'txt') {
      return 'Card mix: simple front and back cards only, because TXT import cannot carry cloze, reverse, media, or HTML.';
    }
    const key = CARD_MIXES[options.cardMix] ? options.cardMix : 'balanced';
    if (!occlusionAllowed(options) && CARD_MIXES_WITHOUT_OCCLUSION[key]) return CARD_MIXES_WITHOUT_OCCLUSION[key];
    return CARD_MIXES[key];
  }

  function cardWritingRules(options) {
    const textOnly = options.outputFormat === 'txt';
    const bold = text => (textOnly ? text : `<b>${text}</b>`);
    const rules = [
      'One fact per card. If an answer needs "and" to join two unrelated facts, make two cards.',
      'The prompt must have exactly one correct answer. Add a context cue in brackets when a question could be read two ways, e.g. "(Plant cell)".',
      'Ask about meaning, not wording: "why", "how", "what happens if", and "what distinguishes X from Y" beat "What is X?" for concepts. Plain recall is right for names, dates, values, and terms.',
      'No yes/no or true/false prompts; the learner can guess them.',
      textOnly
        ? 'Lists: do not ask "List the five X". Make one card per item, each with its own context. Lists of three or fewer may stay on one card.'
        : 'Lists: do not ask "List the five X". Write one cloze sentence with a separate deletion per item ({{c1::...}}, {{c2::...}}), or one card per item. Lists of three or fewer may stay on one card.',
      textOnly
        ? 'Keep answers short, most under 15 words.'
        : 'Keep answers short (most under 15 words) and put the key term in <b>bold</b>.',
      textOnly ? '' : 'Cloze deletions hide the key term or value, never filler words. Add a hint when the gap is ambiguous: {{c1::mitochondria::organelle}}.',
      textOnly ? '' : 'Reverse cards only for true term and definition pairs where recalling in both directions is useful.',
      'Never repeat a fact through reworded cards. Merge details that are always recalled together.',
      'Make the smallest deck that gives complete, reliable recall at the chosen coverage. Do not pad to reach a count.',
      options.avoidLazyCards ? 'Skip trivially obvious cards unless the fact is genuinely examinable.' : ''
    ].filter(Boolean);
    const examples = [
      '- Weak: "What is osmosis?" / "Osmosis is a process where water moves." (vague answer)',
      `  Strong: "Osmosis: water moves across a selectively permeable membrane toward which region?" / "Toward ${bold('lower water potential')} (higher solute concentration)."`,
      textOnly ? '' : '- Weak: "List the parts of a neuron." / "Dendrite, cell body, axon, nerve ending."',
      textOnly ? '' : '  Strong (cloze): "Impulse path in a neuron: {{c1::dendrite}} -> {{c2::cell body}} -> {{c3::axon}} -> {{c4::nerve ending}}."',
      '- Weak: "Is the Earth\'s core hot?" / "Yes."',
      `  Strong: "Approximate temperature at the centre of the Earth?" / "About ${bold('6000 °C')}."`
    ].filter(Boolean);
    return [
      'HOW TO WRITE EACH CARD',
      ...rules.map((rule, index) => `${index + 1}. ${rule}`),
      '',
      'Examples of fixing weak cards:',
      ...examples
    ].join('\n');
  }

  function formattingRules() {
    return `FORMATTING
- Card text may use this HTML only: b, strong, i, em, u, br, p, div, ul, ol, li, span, mark, code, pre, blockquote, hr.
- Maths: \\(...\\) inline and \\[...\\] for display, e.g. "\\(F = ma\\)". In JSON strings, escape the backslash: "\\\\(F = ma\\\\)".
- Never include app metadata: id, noteId, srs, reviewHistory, due, reps, lapses, created, lastModified.`;
  }

  function mediaAllowed(options) {
    return options.mediaMode !== 'none' && options.outputFormat !== 'txt' && options.outputFormat !== 'html';
  }

  // Gemini's chat UI cannot attach generated files, so it cannot hand back the
  // cropped images that occlusion needs.
  function occlusionAllowed(options) {
    return mediaAllowed(options) && options.aiProvider !== 'gemini';
  }

  function mediaRules(options) {
    if (!mediaAllowed(options)) {
      const htmlNote = options.outputFormat === 'txt' ? '' : ' Advanced HTML may still draw tables or flowcharts with HTML and CSS only.';
      return `MEDIA\n- Do not include images, audio, video, or image occlusion.${htmlNote}`;
    }
    if (!occlusionAllowed(options)) {
      return `MEDIA
- Prefer text, cloze, reverse, and advanced HTML cards. Draw tables, timelines, and flowcharts with HTML and CSS rather than images.
- Include an image only if you can supply its real file as Base64 in the media array. Do not create image occlusion cards.`;
    }
    const intensity = options.mediaMode === 'full'
      ? '- Use visuals actively: image occlusion for every examinable labelled diagram or map, and advanced HTML for tables, timelines, and flowcharts.'
      : '- Use images only when they improve recall: labelled diagrams, maps, apparatus, graphs, and tables. Skip decorative figures.';
    return `MEDIA
${intensity}
- Save each image as its own file in media/ with a safe lowercase name (letters, digits, "-", "_") ending in ${SAFE_MEDIA_EXTENSIONS}.
- Crop images tightly to the useful figure. Remove page numbers, running headers, and unrelated neighbouring text.`;
  }

  function occlusionProtocol(options) {
    if (!occlusionAllowed(options)) return '';
    return `IMAGE OCCLUSION (labelled diagrams)
Smriti turns every mask into its own study card, so one diagram with eight labels becomes eight cards. Mask coordinates must be measured, never estimated by eye; boxes that miss their label make the card useless.

Follow these steps with your code tool (for example Python with PyMuPDF, Pillow, and pytesseract or easyocr):
1. Pick diagrams whose labels are examinable. Skip decorative art and diagrams with fewer than two useful labels.
2. Render the PDF page at 200 DPI or more and crop tightly to the figure. Save the crop as the final media file. This saved file is the only coordinate space.
3. Find each label's exact box:
   - If the PDF has a text layer, take the label words' boxes from it (PyMuPDF: page.get_text("words")) and convert PDF points to crop pixels: pixel = (point - crop_origin_point) * DPI / 72.
   - Otherwise run OCR on the saved crop (pytesseract.image_to_data or easyocr) and use the returned word boxes.
   - Join the words of a multi-word label into one box.
4. Make one mask per label. Cover the whole label text plus about 4 px of padding on every side. Do not cover the drawing itself unless the drawn part is what is being asked.
5. Record occlusion.imageWidth and occlusion.imageHeight as the exact pixel size of the saved file, and each mask as bboxPx: [left, top, width, height] in that file's pixels.
6. Check your work: draw every box onto a copy of the crop, look at the copy, and fix any box that misses or clips its label. Do not include the check image in the package.
7. If you cannot run code in this conversation, do not create image occlusion cards. Guessed coordinates are worse than none.

Mask content:
- "answer" is the exact label text from the diagram. "hint" is optional and must not give the answer away.
- Use about 3 to 12 masks per image. Skip repeated labels, captions, figure numbers, and arrows without text.
- "guessMode": "hide-all" (default) covers every label and asks one; use "hide-one" when the other labels are needed as context to make the question fair, such as steps in a cycle.
- One image-occlusion card per diagram, with all of its masks in occlusion.masks. Never duplicate an image into one-mask cards.`;
  }

  function advancedHtmlRules(options) {
    if (options.outputFormat === 'txt') return '';
    return `ADVANCED HTML CARDS (tables, timelines, flowcharts)
- HTML and CSS only: no JavaScript, script tags, event attributes, iframes, forms, inputs, external URLs, @import, fixed or sticky positioning, or z-index tricks.
- Each side renders in a 340 px by 470 px canvas with 20 px corner radius. Wrap each side in one root such as <div class="card-design">, start the CSS with *{box-sizing:border-box}, and keep text readable at that size.
- Use them only when the layout itself aids recall; do not turn them into long notes pages.`;
  }

  function deckJsonExample(options) {
    const cards = [
      {
        type: 'basic',
        term: 'Osmosis: water moves across a selectively permeable membrane toward which region?',
        definition: 'Toward <b>lower water potential</b> (higher solute concentration).',
        tags: ['transport']
      },
      {
        type: 'basic',
        term: 'Mitochondria',
        definition: 'Site of <b>aerobic respiration</b> in the cell',
        reverse: true,
        tags: ['cell']
      },
      {
        type: 'cloze',
        text: 'The SI unit of force is the {{c1::newton}}, symbol {{c2::N::one letter}}.',
        definition: 'Optional extra note shown on the back.',
        tags: ['units']
      }
    ];
    if (occlusionAllowed(options)) {
      cards.push({
        type: 'image-occlusion',
        term: 'Human brain: label the parts',
        image: 'media/fig-6-3-human-brain.webp',
        occlusion: {
          guessMode: 'hide-all',
          units: 'px',
          imageWidth: 1180,
          imageHeight: 860,
          masks: [
            { shape: 'rect', bboxPx: [402, 96, 188, 44], answer: 'Cerebrum' },
            { shape: 'rect', bboxPx: [730, 612, 170, 44], answer: 'Cerebellum', hint: 'balance' }
          ]
        },
        tags: ['diagram']
      });
    }
    if (options.outputFormat !== 'txt') {
      cards.push({
        type: 'advanced-html',
        term: 'Hardy-Weinberg genotype frequencies',
        definition: 'p² AA, 2pq Aa, q² aa',
        advancedHtml: {
          frontHtml: '<div class="card-design"><h2>Hardy-Weinberg</h2><p>Genotype frequencies for alleles p and q?</p></div>',
          frontCss: '*{box-sizing:border-box}.card-design{width:340px;min-height:470px;padding:20px;border-radius:20px;background:#fff;color:#111;font-family:Arial,sans-serif}',
          backHtml: '<div class="card-design"><table><tr><td>AA</td><td>p²</td></tr><tr><td>Aa</td><td>2pq</td></tr><tr><td>aa</td><td>q²</td></tr></table></div>',
          backCss: '*{box-sizing:border-box}.card-design{width:340px;min-height:470px;padding:20px;border-radius:20px;background:#fff;color:#111;font-family:Arial,sans-serif}td{border:1px solid #ccc;padding:8px}'
        },
        tags: ['genetics']
      });
    }
    return {
      version: 1,
      name: clean(options.deckName) || 'Deck name',
      className: clean(options.className) || 'Optional existing class name',
      cards
    };
  }

  // One card per line keeps the example readable without pages of indentation.
  function formatDeckJson(deck) {
    const header = Object.entries(deck)
      .filter(([key]) => key !== 'cards')
      .map(([key, value]) => `  ${JSON.stringify(key)}: ${JSON.stringify(value)},`);
    const cards = deck.cards.map(card => `    ${JSON.stringify(card)}`).join(',\n');
    return `{\n${header.join('\n')}\n  "cards": [\n${cards}\n  ]\n}`;
  }

  function packageSourceSpec(options) {
    const deckName = JSON.stringify(clean(options.deckName) || 'Deck name');
    return `ERUDITE PACKAGE SOURCE (text alternative to a ZIP)
Start the reply with the line ERUDITE_PACKAGE_SOURCE_V1 and follow it with one JSON object and nothing else: no Markdown fences, comments, or trailing commas.
{
  "deck": { "version": 1, "name": ${deckName}, "cards": [ ...cards exactly as in deck.json... ] },
  "media": [
    { "path": "media/fig-6-3-human-brain.webp", "mime": "image/webp", "encoding": "base64", "data": "BASE64_DATA" }
  ]
}
- "deck" follows the deck.json schema above.
- Every media/... path used in the deck appears exactly once in "media", with Base64 file contents. Leave "media" empty when there are no files.`;
  }

  function outputSpec(options) {
    const format = options.outputFormat || 'zip';
    if (format === 'txt') {
      return `OUTPUT: plain text only, no Markdown, headings, or explanations.
Format: front;back@front;back@front;back
- A semicolon separates front and back; @ separates cards. Never use @ inside card text, and avoid semicolons in it.
- Simple front and back cards only: no cloze, media, tags, or HTML.
Example:
Photosynthesis;Process by which green plants make glucose from carbon dioxide and water using light@Site of aerobic respiration;Mitochondria`;
    }
    if (format === 'html') {
      return `OUTPUT: exactly four fenced code blocks labelled FRONT_HTML, FRONT_CSS, BACK_HTML, and BACK_CSS, for ONE custom card.
- Follow the advanced HTML rules above. No style attributes in the HTML; put all styling in the CSS blocks.
- Good uses: comparison table, timeline, flowchart, formula summary, small labelled schematic. Bad uses: posters, long notes, quizzes.`;
    }
    const json = formatDeckJson(deckJsonExample(options));
    if (format === 'json') {
      return `OUTPUT: one valid JSON object only. No Markdown fences, comments, or explanations.
${json}
- Embedded images must be data URLs ("data:image/webp;base64,..."), never external URLs.`;
    }
    return `OUTPUT: a Smriti package, a .zip file containing:
- deck.json at the root of the ZIP (not inside a folder), shaped like this:
${json}
- media/ holding every file that deck.json references by a media/... path, and nothing else.
- No Base64 inside deck.json and no external URLs.

${packageSourceSpec(options)}`;
  }

  function finalChecklist(options) {
    if (options.outputFormat === 'txt' || options.outputFormat === 'html') return '';
    const lines = [
      'BEFORE YOU ANSWER, CHECK',
      '- The JSON parses, and every referenced media/... file is included.',
      '- Every card tests one fact, and has a single unambiguous answer.',
      '- No duplicate facts, no vague prompts, no invented content.',
      '- The total number of study cards (each reverse direction, cloze deletion, and occlusion mask counts as one) is 999 or fewer.'
    ];
    if (occlusionAllowed(options)) {
      lines.push('- Every occlusion box was measured with code and checked on a drawn copy; imageWidth and imageHeight match the saved file.');
    }
    return lines.join('\n');
  }

  function providerInstruction(options) {
    if (options.outputFormat === 'txt' || options.outputFormat === 'html' || options.outputFormat === 'json') return '';
    if (options.aiProvider === 'gemini') {
      return 'FINAL ANSWER: reply with ERUDITE PACKAGE SOURCE text (not a ZIP). The Smriti app builds the ZIP from it.';
    }
    if (options.aiProvider === 'chatgpt' || options.aiProvider === 'claude') {
      return 'FINAL ANSWER: use your file tools to build the .zip and attach it as a downloadable file. Do not paste deck.json into the chat. If you cannot create files in this conversation, say so in one line and reply with ERUDITE PACKAGE SOURCE text instead.';
    }
    return 'FINAL ANSWER: attach the .zip as a downloadable file if you can create files; otherwise reply with ERUDITE PACKAGE SOURCE text.';
  }

  function buildDeckPrompt(options = {}) {
    const blocks = [
      learningBrief(options),
      sourceRules(),
      cardWritingRules(options),
      cardMix(options),
      options.outputFormat === 'txt' ? '' : formattingRules(),
      mediaRules(options),
      occlusionProtocol(options),
      advancedHtmlRules(options),
      outputSpec(options),
      finalChecklist(options),
      providerInstruction(options)
    ];
    return blocks.filter(Boolean).join('\n\n');
  }

  return {
    buildDeckPrompt,
    occlusionAllowed
  };
});
