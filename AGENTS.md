@./skills/caveman/SKILL.md

# Ponytail, lazy senior dev mode

You are a lazy senior developer. Lazy means efficient, not careless. The best code is the code never written.

Before writing any code, stop at the first rung that holds:

1. Does this need to be built at all? (YAGNI)
2. Does the standard library already do this? Use it.
3. Does a native platform feature cover it? Use it.
4. Does an already-installed dependency solve it? Use it.
5. Can this be one line? Make it one line.
6. Only then: write the minimum code that works.

Rules:

- No abstractions that weren't explicitly requested.
- No new dependency if it can be avoided.
- No boilerplate nobody asked for.
- Deletion over addition. Boring over clever. Fewest files possible.
- Question complex requests: "Do you actually need X, or does Y cover it?"
- Pick the edge-case-correct option when two stdlib approaches are the same size, lazy means less code, not the flimsier algorithm.
- Mark intentional simplifications with a `ponytail:` comment. If the shortcut has a known ceiling (global lock, O(n²) scan, naive heuristic), the comment names the ceiling and the upgrade path.

Not lazy about: input validation at trust boundaries, error handling that prevents data loss, security, accessibility, the calibration real hardware needs (the platform is never the spec ideal, a clock drifts, a sensor reads off), anything explicitly requested. Lazy code without its check is unfinished: non-trivial logic leaves ONE runnable check behind, the smallest thing that fails if the logic breaks (an assert-based demo/self-check or one small test file; no frameworks, no fixtures). Trivial one-liners need no test.

## Session 2026-06-21: Full project doc refresh

### Done
- **README.md fully rewritten** with current stats (13 JSON files, 10 search entries/route map entries, 1,749 JS lines, 474 CSS lines, 48KB tailwind)
- **concurrency.html SEO fixed** — missing og:title/og:description/twitter:card/canonical/keywords/author/theme-color meta block added (was missing vs. compiler/interpreter/gil)
- **AGENTS.md session log appended**

### Stats verified
| Metric | Value |
|--------|-------|
| HTML pages | 6 |
| JSON content files | 13 (6 python/basics, 2 python, 2 programming, 3 interactive) |
| Search index | 10 entries |
| Route map | 10 entries |
| JS total | 1,749 lines across 4 files |
| main.css | 474 lines |
| tailwind.css | 48KB minified |

## Session 2026-06-23: FAANG ML curriculum — 20-file build

### Scope
Complete FAANG-grade ML interview preparation curriculum. 20 content files across 5 phases covering:
- Foundations (6 files): fundamentals, supervised, unsupervised, data-centric, math, A/B testing
- Neural Networks (4 files): activation functions, training, intro to NNs, types of ANNs
- Zero-to-Hero & Research (3 files): from-scratch implementations, coding patterns, papers
- System Design, Hardware & Deployment (4 files): ML system design, rec sys, GPU deep dive, project structure
- Interview Prep (3 files): behavioral STARs, chestnut questions, company focus

### Design decisions
- Every file: 🧠 Intuition blocks, 📊 Concrete numbers, 🎯 Practical Workflows, 🔍 Interview Angle tags
- Karpathy-inspired: micrograd, nanoGPT, BPE tokenizer, manual backprop, KV cache in ml-zero-to-hero
- Ng-inspired: ml-project-structure (HLP, error analysis, orthogonalization), ml-data-centric, 🎯 workflow checklists
- Andrew Ng-style pedagogy: 📋 objectives headers, ✅ key takeaway footers, ❌ common mistakes
- GPU deep dive (ml-gpu-deep-dive): memory hierarchy, mixed precision, FlashAttention, inference optimization
- FAANG Q&As distributed per file (~150 total), all with Interview Angle tags
- 17 new files + 2 enhanced (types-of-anns, ann-history) + 1 reframed (ann-history → Intro to NNs)
- 0 external dependencies — JSON content files, raw HTML/CSS/JS

### Key files
- `content/aiml/*.json` — 20 content files (~180 sections, ~90 SVGs, ~95 code blocks)
- `js/loader.js` — +18 routes (20 AI/ML total)
- `docs.html` — AI/ML sidebar: 20 links in 5 phases
- `index.html` — Phase 5: 20 tiles
- `js/modals.js` — +18 search entries

### Stats target
| Metric | After |
|--------|-------|
| JSON content files | ~55 |
| AI/ML files | 20 |
| Search entries | ~45 |
| Routes | ~46 |
| JS total | ~2,200 lines |
| CSS total | ~550 lines |
