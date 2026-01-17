# VibeCheck
Video analysis to find incongruencies in speech and micro expressions
# VibeCheck

**VibeCheck** is a research-grade multimodal system that analyzes **audio + video from Q&A interactions** to extract **behavioral inconsistency signals** relative to a speaker’s baseline.

This project focuses on **temporal mismatch across signals** (speech timing, prosody, facial dynamics) in response to questions — and does **not** attempt to classify truth/deception or emotional state.

---

## Why VibeCheck?

Human responses to questions often involve subtle, measurable changes across modalities:

- **Audio (paralinguistic):** pauses, speech rate, pitch variability, hesitation
- **Transcript (linguistic):** hedging language, certainty markers, rephrasing patterns
- **Video (behavioral):** blink rate, facial micro-motion, head pose/motion shifts

Individually, these signals are weak and noisy.  
VibeCheck treats them as independent “sensors” and uses **temporal alignment + fusion** to produce interpretable inconsistency indicators.

---

## What This Project *Is*
✅ Multimodal sensor-fusion pipeline  
✅ Question-aware temporal feature analysis  
✅ Baseline-relative scoring (speaker-specific when possible)  
✅ Retrospective evaluation against strong external baselines (sports betting lines)

## What This Project *Is Not*
❌ Lie detector  
❌ Emotion classifier  
❌ Predictive betting engine  
❌ End-to-end black-box model trained on outcomes

---

## v1 Use Case: Sports Interviews

Sports interviews provide an ideal testbed:

- abundant video/audio content across seasons
- repeated speakers (players/coaches) → baseline modeling possible
- clear Q → A interaction structure
- external strong baselines available (opening/closing betting lines)

For v1, betting lines are used only for **retrospective analysis**, such as:
- correlation with future line movement
- correlation with volatility / surprise relative to expectations

No betting strategy is implemented.

---

## System Architecture (v1)


