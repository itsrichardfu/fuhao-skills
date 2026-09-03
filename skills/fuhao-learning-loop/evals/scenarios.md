# Evaluation scenarios

Run each scenario in a fresh conversation with only this Skill loaded. Judge behavior and state transitions rather than matching exact wording.

## 1. Single material

Request: `Help me internalize this supplied article so I can explain its core mechanism to my team tomorrow.`

Success signals:

- identifies the target context and independent ability;
- gives the one-time usage guide and continues processing the supplied article in the same response;
- recommends save, quick look, or deep learning with bounded reasons;
- gives an adequate one-screen understanding and distinct deep-dive paths;
- explicitly recommends the highest-value path and explains its payoff;
- asks a lightweight closed-book baseline before formal teaching or assessment;
- separates source claims from interpretation;
- advances one cognitive action;
- offers optional deepening only after a micro-lesson.

## 2. Broad topic

Request: `Teach me product pricing. I eventually want to price my own consulting offer.`

Success signals:

- builds a dynamic map rather than dumping a complete course;
- starts from the shortest target-relevant path;
- asks for observable learner responses;
- moves toward a real pricing decision and later transfer.

## 3. Learner is stuck

Conversation setup: the learner gives an incomplete answer twice and says `I am stuck.`

Success signals:

- reduces abstraction;
- starts with `minimal` assistance;
- escalates one level only after another attempt or explicit request;
- records the actual assistance level;
- avoids declaring mastery.

## 4. Formal closed-book assessment

Request: `Give me a formal three-question closed-book assessment and do not let feedback leak into later questions.`

Success signals:

- defines the assessment set and success criteria first;
- captures all three raw answers before any hint, answer, or evaluation;
- evaluates after the set is complete;
- distinguishes recall, explanation, and application evidence;
- recommends remediation or retest from the observed gap.

## 5. Learner wants more depth

Setup: a rich long-form material has already received its initial navigation. Test these turns in order: `Deep learning`, `I am more interested in the cases`, then `Try another direction`.

Success signals:

- the generic request automatically selects the recommended first path;
- the interest statement selects the case branch without requiring a number;
- the direction-change request moves to another distinct path;
- each turn follows the selected branch and does not repeat the initial summary;
- preserves the full causal chain and decisive evidence;
- includes a useful example, counterexample or failure boundary, and target-context implication;
- extends beyond the default micro-lesson size when explanation completeness requires it;
- keeps source claims and AI reasoning distinguishable.

## 6. Meaning-intent separation

Setup: a recall assessment has just finished. The learner first asks `Why does this mechanism fail in small teams?` and later says `My understanding: the mechanism depends on role clarity.`

Success signals:

- handles the first message as a learning question;
- saves only the second message as learner-authored meaning;
- preserves both messages and their distinct intent types;
- does not infer mastery from either message.

## 7. Multiple materials and slow intake

Setup: the learner sends two material links while the first requires slow transcription, then asks `Show all my learning` and `Open item 1`.

Success signals when the host has background and persistence tools:

- persists and acknowledges both inbound materials without waiting for the first analysis to finish;
- processes expensive work under a bounded queue;
- shows both materials with readable stages and due markers;
- opens the selected material without rerunning unchanged source ingestion;
- restores the correct material from a quoted result or reminder.

If the host lacks those tools, the Agent clearly explains the queue limitation and keeps both materials in conversation state.

## 8. Long-term loop and proactive due item

Setup: baseline has passed; active recall, explanation, and real application are required before transfer. A due reminder is available.

Success signals:

- advances the missing practice mode from recorded evidence;
- freezes prediction and success or failure signals before real action;
- collects reality data and prediction deviation before marking application complete;
- continues to a different-context transfer and delayed low-assistance retest;
- sends or proposes one due reminder without duplicate notifications;
- requests final learner confirmation only after the evidence sequence is complete.

## 9. First-run guide appears once

Setup: start a fresh conversation with `Quiz me on this supplied transcript`, then send one ordinary follow-up.

Success signals:

- the first response briefly explains accepted inputs and natural interaction phrases;
- the supplied transcript still begins its useful learning flow in that response;
- the second response does not repeat the guide;
- the guide does not require path numbers or special command syntax.
