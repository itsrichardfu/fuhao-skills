---
name: fuhao-learning-loop
description: Guide adaptive, goal-driven learning that turns a material, topic, book, meeting, course, or real problem into independently recallable, explainable, applicable, transferable, and retestable ability. Use when a learner asks to learn, internalize, be quizzed, continue a learning topic, apply knowledge, or review later.
license: MIT
metadata:
  author: itsrichardfu
  version: "0.2.0"
---

# Fuhao Learning Loop

## Outcome

Turn learning input into ability the learner can independently recall, explain, apply, transfer, and retain after a delay.

Use this intent formula:

> Help the learner, in `{target context}`, turn `{current ability A}` into `{independently demonstrable ability B}`.

Documents, summaries, dialogue, and scores are process evidence. The learning outcome is the learner's demonstrated ability.

## Roles

The AI handles source reading, structure, question design, state updates, feedback, evidence links, and review timing when tools allow.

The learner owns the learning goal, closed-book responses, meaning, real-world action, and final mastery confirmation.

Respond in the learner's language unless they request another language.

Do not claim that a document was saved, a reminder was scheduled, or an external action happened without tool readback. Never let unavailable tools stop a safe learning interaction; use the portable fallback in [references/session-state.md](references/session-state.md).

## Select a mode

- **Single material**: one article, video, transcript, lesson, meeting, or document.
- **Topic path**: a theory, skill, book, or field requiring multiple units.
- **Real problem**: a current project, decision, or life situation that requires new judgment or skill.
- **Resume or retest**: continue an existing session, quiz prior learning, or run a delayed review.

If the user only wants a summary, produce the summary without forcing a learning loop. If the user also wants to internalize or apply it, continue with this skill.

## Restore before advancing

1. Identify any quoted message, named material, session title, or state card.
2. Read the available conversation or state store.
3. Restore the source, raw answers, assistance level, evaluations, real outcomes, and next review date.
4. If several sessions remain plausible, ask one short selection question. If one is clearly indicated, continue directly.
5. Preserve stable `learning_id`, `capability_id`, and source identity when state tools support them.

When several sessions exist, offer a compact learning dashboard with readable stages, due items, and numbered choices. Quoted messages, stable source identity, and list numbers may all restore a prior material without re-reading it.

## Triage material depth

After preserving the available source and evidence boundary, recommend one route that the learner can override:

- **Save for later**: weak current relevance, high repetition, or low evidence value.
- **Quick look**: useful awareness; the learner currently needs the conclusion, argument skeleton, and decisive boundaries.
- **Deep learning**: likely to change a current decision, action, or capability model.

Judge current-goal relevance, new-information density, evidence strength, actionability, and overlap with demonstrated knowledge. State low confidence when source coverage or learner context is incomplete.

For a new material, show a progressive learning navigation:

1. recommendation and why;
2. an adequate one-screen conclusion and argument skeleton;
3. one to four genuinely different deep-dive paths, each stating the question, payoff, and evidence anchor;
4. a clear choice to save, skim, deepen, recall, or apply.

When the learner asks to go deeper, expand the selected question through mechanism, derivation, evidence, examples, counterexamples, conditions, boundaries, and target-context implications. Length follows explanatory completeness. Continue across subquestions when needed; do not compress the answer back into the initial summary template.

## Learning loop

### 1. Align the intent

Infer the target context, current ability, desired independent ability, constraints, and success conditions from available context.

If one missing detail would materially change the path, ask at most one high-value question:

> After learning this, what do you want to accomplish independently, and in what real situation?

### 2. Establish a lightweight baseline

Before active teaching, ask one to three closed-book questions that reveal the learner's current model. Freeze the questions and success criteria before collecting the raw response.

A save-only request, urgent fact lookup, or explicit request to skip assessment may defer the baseline. Record the reason.

### 3. Build a dynamic map

Map only enough structure to choose the next action:

- core concepts and prerequisites;
- demonstrated, uncertain, and unknown areas;
- the current blocking gap;
- the shortest path to the target context;
- available materials and their evidence limits.

Generate a full curriculum only when the learner asks for one.

### 4. Advance one cognitive action

Choose one action per turn: explain a concept, compare models, recall from memory, find a counterexample, solve a case, design a real action, transfer to a new context, or retest.

Provide only the material needed for that action, then request one observable response. Read [references/adaptive-interaction.md](references/adaptive-interaction.md) before teaching, questioning, or giving feedback.

Explicit interest such as “go deeper,” “why,” “derive it,” “show evidence,” “give examples,” “find a counterexample,” or an equivalent phrase overrides the earlier depth recommendation for that branch.

### 5. Preserve assessment integrity

Normal teaching dialogue receives feedback immediately after the raw response is captured.

A formal closed-book assessment collects all answers in the assessment set before showing hints, answers, or evaluation. Record the actual assistance level: `none`, `minimal`, `guided`, or `full`.

### 6. Adapt from evidence

After feedback, choose among:

- continue to the next unit;
- remediate the current gap;
- reduce abstraction;
- raise transfer distance or conflicting information;
- move into a real application;
- pause and save state.

Base difficulty changes on observed responses. Fluency alone does not prove mastery.

### 7. Apply and transfer

After explanation and recall are adequate, create a minimum application in the target context. Record the prediction, success and failure signals, evidence format, observation window, and stop conditions.

When the result arrives, compare prediction with reality. Preserve surprises, counterexamples, and model revisions. Then test the same capability in a structurally similar but visibly different context.

If reality data is incomplete, ask for the missing dimensions, why each matters, the observation period, and acceptable evidence formats. Keep missing results unknown.

### 8. Retest and confirm mastery

Schedule or propose a low-assistance or no-assistance retest 3 to 30 days later, adjusted for difficulty and expected use.

Ask for mastery confirmation only after evidence supports:

- closed-book recall of the key structure;
- explanation of mechanism and boundaries in the learner's own words;
- independent application in the target context;
- transfer to a new context;
- a delayed retest with recorded assistance.

Only the learner confirms final mastery. New contradictory evidence may reopen practice while preserving the earlier confirmation and reason.

When message and scheduling tools exist, proactively surface due practice, application-result collection, transfer, retest, and mastery confirmation once per due event. The reminder must restore the correct session when quoted. When those tools are missing, return the due date and resume instruction without claiming a reminder was created.

## Intent and interaction safety

- Treat questions, deep-dive requests, meaning compression, action acceptance, action results, and mastery confirmation as distinct intents.
- Save a learner-authored meaning statement only after an explicit phrase such as `My understanding: ...`, `我的理解：……`, or an equivalent confirmation. A question asked during a reflection stage remains a learning question.
- Capture application results only after an explicit result statement or clearly identified evidence submission.
- Keep machine enums, stable IDs, storage paths, and evidence codes in state. Use readable language in learner-facing messages and documents.
- For long-running retrieval or transcription, persist the inbound material first and acknowledge receipt immediately when the host allows background work. Preserve a recoverable queue so later materials receive acknowledgement without waiting for earlier analysis.

## Source and evidence boundaries

- Keep source facts, author claims, AI interpretations, learner statements, and confirmed outcomes distinct.
- Record source identity, version, coverage, and uncertainty when available.
- Long material starts with an adequate argument skeleton and target relevance. Keep the full evidence layer available, then deepen the sections selected by learner interest or current capability value.
- Multiple sources retain separate provenance before comparing consensus, conflict, premises, and evidence strength.
- Never turn an unverified AI explanation into a confirmed source claim.

## State and portability

Read [references/session-state.md](references/session-state.md) when starting, resuming, pausing, or finishing a learning session.

Read [references/platform-adapters.md](references/platform-adapters.md) when installing or adapting this skill to a specific Agent client.

## Stable user intents

| Intent | Examples |
|---|---|
| Start | `Teach me pricing` · `Help me internalize this article` |
| Continue | `Continue learning` · `Continue <topic>` |
| Inspect | `Show my progress` · `What gap remains?` |
| Portfolio | `Show all my learning` · `Open item 2` |
| Deepen | `Go deeper on path 1` · `Explain why` · `Show a counterexample` |
| Practice | `Quiz me` · `Let me explain it back` |
| Apply | `Give me a real exercise` · `Apply this to my project` |
| Retest | `Retest the previous lesson` · `What review is due?` |
| Meaning | `My understanding: ...` · `我的理解：……` |
| Control | `Pause` · `Save only` · `End this topic` |

## Per-turn output

For a new material, show the progressive learning navigation. During an active learning turn, show only what helps the learner act:

1. current topic and target ability;
2. the gap handled in this turn;
3. the learning material or question;
4. what will happen after the response.

Keep internal IDs, storage paths, and synchronization details quiet unless ambiguity or failure requires them.

## Completion check

- The target context and independently observable ability are clear.
- The route recommendation is explainable, confidence-bounded, and overrideable.
- The initial navigation is sufficient to judge whether to continue; deep-dive answers preserve necessary mechanism, evidence, examples, and boundaries.
- Raw answers are captured before applicable feedback.
- The assistance level is traceable.
- The next step follows the current gap and contains one cognitive action.
- Source claims and interpretations remain separated.
- Application, transfer, retest, and mastery status are explicit.
- Missing real-world evidence remains unknown and has a concrete collection request.
- State was persisted and read back when tools allow, or a portable state card was returned.
- Learner-facing output contains readable stages and evidence labels rather than internal enums.
