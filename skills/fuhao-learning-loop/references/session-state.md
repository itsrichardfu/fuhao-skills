# Portable learning session state

The interaction protocol works with a database, files, memory tools, or conversation-only state. Use the strongest available persistence mechanism while keeping the same semantics.

## Minimum state

```yaml
schema: fuhao-learning-loop/v1
learning_id: ""
capability_id: ""
title: ""
mode: material | topic | real_problem
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
