# Platform adapters

The core skill assumes no particular vendor, storage system, or tool name. Adapt installation and persistence to the host while preserving the learning semantics.

## Agent Skills-compatible clients

Install the complete `fuhao-learning-loop/` directory in a project-level or user-level Skills directory scanned by the client. Cross-client implementations commonly scan `.agents/skills/`; the Agent Skills specification defines the package contents and leaves installation paths to clients.

Verify installation by checking that the client discovers `fuhao-learning-loop` and loads its `SKILL.md` for a request such as “Help me internalize this article.”

References:

- [Agent Skills specification](https://agentskills.io/specification)
- [Adding Skills support to an Agent](https://agentskills.io/client-implementation/adding-skills-support)

## Codex

Use the project or user Skills mechanism available in the current Codex environment. Prefer the cross-client `.agents/skills/fuhao-learning-loop/` location when it is already scanned. Preserve the complete directory so relative references resolve.

Persistent learning state is optional. If a memory or task-state tool exists, map the fields from `session-state.md`; otherwise use the conversation-only state card. When the host supports scheduled tasks or thread wakeups, use them for due practice and retest while preserving one-notification-per-due-event behavior.

## WorkBuddy / CodeBuddy

Place the complete skill directory at:

```text
<project>/.codebuddy/skills/fuhao-learning-loop/
```

WorkBuddy also exposes a Skill management interface that can import Skills. Verify that the visible skill name and description match the frontmatter, then run one learning request.

Reference: [WorkBuddy Skills](https://www.workbuddy.ai/docs/zh/ide/Features/Skills).

## Doubao Work

Doubao Work supports custom and team-shared Skills. Public product pages do not currently document a stable GitHub repository import contract for the Agent Skills directory format.

Use this compatibility order:

1. Try the client's current Skill import interface with the complete directory.
2. If directory import is unavailable, create a custom Skill from `templates/prompt-only.md`.
3. Keep session state in the conversation or a host-provided document until a persistent state interface is confirmed.
4. Treat installation as verified only after the client displays the skill and follows both micro-lesson and assessment-integrity behavior in a test conversation.

Reference: [Doubao Work for teams](https://www.doubao.com/work/group).

## Generic chat or custom Agent

Use `templates/prompt-only.md` as a system prompt or initial instruction. If the Agent can read files, attach `references/session-state.md` as supporting context. If the Agent cannot schedule, return the recommended review date to the learner.

## Capability degradation

| Missing host capability | Safe fallback |
|---|---|
| File or database storage | Conversation state plus portable YAML state card |
| Scheduler or reminder | Return `retest_at` explicitly |
| Source retrieval | Ask the learner to provide the material or continue with clearly bounded information |
| Citation locator | Record source title, supplied link, and available section marker |
| Cross-conversation message lookup | Resume from the portable state card |
| Tool readback | Describe the intended write as pending and avoid claiming success |
| Background queue | Acknowledge after the source is safely held in the current conversation, then process sequentially and report that later materials may wait |
| Proactive messaging | Return a readable due date and exact resume phrase |

## Message-channel implementation

When adapting to Feishu, Slack, Discord, or another message channel:

1. persist message identity, source link, requested mode, and receipt time before starting slow retrieval;
2. acknowledge immediately after the persistence write succeeds;
3. process expensive retrieval or transcription under a bounded worker queue;
4. record outbound message identity so quoted replies restore the correct learning session;
5. send each due reminder once and preserve retry-safe idempotency;
6. accept time-range or recent-count batch requests when the state store can enumerate source sessions;
7. deduplicate before building a bounded evidence packet, then create a separate aggregate session while preserving every source session;
8. validate each cross-source agreement or conflict against verbatim excerpts from at least two distinct sources;
9. keep machine status codes in the state store and render human-readable stages in chat.
