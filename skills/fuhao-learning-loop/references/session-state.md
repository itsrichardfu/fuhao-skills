# Portable learning session state

The interaction protocol works with a database, files, memory tools, or conversation-only state. Use the strongest available persistence mechanism while keeping the same semantics.

## Minimum state

```yaml
schema: fuhao-learning-loop/v2
onboarding_version: 0
learning_id: ""
capability_id: ""
title: ""
mode: material | topic | real_problem
depth_route:
  recommendation: save_for_later | quick_look | deep_learning
  confidence: high | medium | low
  why: ""
deep_dive_paths: []
selected_deep_dive:
  path_index: null
  topic: ""
visible_assessment:
  version: ""
  shown_at: ""
  lesson_kind: navigation | deep_dive | remediation
  questions: []
  scoring_points: []
intent:
  current_ability: ""
  target_ability: ""
  target_context: ""
  success_signals: []
stage: intent | baseline | learning | recall | application | transfer | retest | awaiting_confirmation | mastered | paused | retired
current_gap: ""
next_action:
  type: ""
  request_to_learner: ""
  due_at: null
assistance_level: none | minimal | guided | full
source_refs: []
evidence: []
learner_meaning: []
inbound_status: received | queued | processing | ready | failed
retest_at: null
updated_at: ""
```

Generate stable IDs only when the host can preserve them. A readable title plus source identity is enough for a conversation-only session.

## Evidence entries

Each meaningful result may record:

```yaml
- kind: raw_answer | evaluation | application | transfer | retest | mastery_confirmation
  observed_at: ""
  assistance_level: none | minimal | guided | full
  summary: ""
  locator: ""
  source: "learner | ai | external"
  independence: independent | shared_origin | unverified
```

Preserve the learner's raw answer separately from AI feedback. Mark inferred or incomplete evidence.

## Persistence rules

- Read before writing when a state store is available.
- Use an idempotency key when the host supports one.
- Confirm a write through tool readback before claiming it succeeded.
- Keep one current minimum next action while retaining prior evidence.
- Preserve state history when mastery is reopened by contradictory evidence.
- Do not require the learner to manually move state between systems when the host offers connectors or file tools.
- Store questions and ordinary dialogue separately from explicitly confirmed learner meaning.
- When background work is available, persist inbound identity before acknowledgement and keep a recoverable queue status.
- Keep the initial depth recommendation and later learner-selected branches so resume does not collapse back to a generic summary.
- Freeze source-specific questions with the visible assessment scope that preceded them. Ordinary dialogue never replaces that scope silently.
- Preserve AI teaching and deep-dive turns separately from the canonical source analysis so later questions and explanations remain recoverable.
- Record hint requests and the resulting assistance level on the exact assessment attempt.

## Conversation-only fallback

When the host has no persistent store:

1. Keep the active state in the current conversation.
2. At pause, end, or context-limit risk, output the state as a fenced YAML block titled `FUHAO LEARNING STATE`.
3. Tell the learner to provide that block when resuming in a new conversation.
4. Do not claim a reminder was scheduled. Return the recommended `retest_at` explicitly.

## Resume resolution

Prefer identifiers in this order:

1. quoted or linked prior message;
2. `learning_id`;
3. exact source identity;
4. exact title;
5. most recent unique active session.

If multiple sessions remain plausible, show a short candidate list and ask one selection question.

## Multi-session dashboard

When the host can enumerate sessions, show a compact numbered view with readable stages:

- saved for later;
- ready to explore;
- active recall or explanation;
- waiting for a real-world result;
- transfer or retest due;
- awaiting learner mastery confirmation;
- mastered or paused.

Highlight due items and let the learner open a numbered session. Restore its source, selected depth branch, raw evidence, assistance level, and next action without rerunning source ingestion unless the source changed.
