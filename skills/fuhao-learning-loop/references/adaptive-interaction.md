# Adaptive learning interaction

Each turn handles the most important current capability gap. Long reading and real actions may enter the loop when needed.

## Depth and cognitive load are separate

“Deep learning” means that the explanation preserves the mechanism, evidence, examples, and boundaries. It does not automatically make the learner answer more variables at once.

Use four cognitive levels in order:

1. **Identify** one claim, distinction, or step already shown;
2. **Reconstruct** one mechanism and one key condition in the learner's own words;
3. **Examine** one premise, counterexample, or piece of evidence that could change the judgment;
4. **Apply** one judgment in one concrete target-context situation with one observable signal.

Move one level at a time. Keep one main question per turn, with at most two short answer slots. If a task needs a current judgment, missing information, a comparison, an observation, and a revision condition, serialize it as `judgment → one key variable → one comparison → one observation signal → revision condition`.

Raise a level or add a variable only after two consecutive low-assistance turns are stable and the learner reproduces the capability in a new question. A long or fluent answer alone does not authorize a jump.

When the learner says `too hard`, `I don't understand`, `I don't know how to answer`, `step by step`, `give me an example`, or an equivalent phrase, immediately lower one level. Restate the purpose in plain language, offer one concrete example or a binary choice, ask only one question answerable in one or two sentences, and pause the remaining fields. Keep the overload signal in session state. An explicit `Challenge me`, `a little harder`, or `add a counterexample` request can restore the challenge after the same stability gate.

## One interaction turn

1. Restore the learning target, stage, and previous raw result.
2. Select one observable learning objective and mark the cognitive level and current load mode.
3. Provide the minimum material, example, or question needed.
4. Ask for one closed-book recall, explanation, judgment, case response, or real action. Keep one main question and at most two short answer slots.
5. Capture the raw response before choosing the applicable feedback timing.
6. Update demonstrated ability, current gap, assistance level, and next action.

Wait for the learner after one turn unless they explicitly request continuous reading.

## Micro-lessons and optional deepening

- When teaching new content, explain one mechanism at a time. A useful starting size is 300 to 500 Chinese characters, 180 to 300 English words, or 3 to 7 minutes of reading.
- Extend the material when a causal chain, evidence boundary, or necessary case cannot fit without losing meaning.
- Offer optional deepening after a micro-lesson: `mechanism / evidence / example / counterexample / comparison experiment / supporting sources / target-context implication`.
- Deepening stays in the current unit by default. Update the path only when it reveals a new decisive gap.
- Skip the deepening menu when the turn contains only a question, feedback, or real action.

Treat the size above as a starting point. Once the learner expresses deep interest, explanation length follows the selected question. Preserve the full causal chain, decisive evidence, at least one useful example, a boundary or counterexample, and the connection to the learner's target. Split a genuinely long explanation into named subquestions and continue one at a time.

## Progressive material navigation

For a newly supplied material, the first useful response should help the learner choose attention depth:

1. route recommendation: save for later, quick look, or deep learning;
2. why: current relevance, novelty, evidence strength, actionability, and overlap;
3. one-screen understanding: adequate conclusion, argument skeleton, and decisive boundary;
4. one to four deep-dive paths, each with a question, payoff, and evidence anchor;
5. learner choices: save, skim, deepen, recall, or apply.

Order deep-dive paths by expected value for the learner's current goal. Recommend the first path in plain language, explain the payoff, and let a generic `Deep learning`, `Go deeper`, or equivalent request select it automatically. Natural interest statements select their topic; `Try another direction` advances to another distinct path. Numbers are optional shortcuts for precise selection.

Avoid two common failures:

- showing the entire analysis schema as a large first response;
- reducing a material to a thin summary that hides the ideas most likely to create curiosity.

The full analysis may remain in a document or state store. The dialogue presents a useful navigation layer and expands according to learner interest.

## Adapt to observable signals

Keep difficulty close to the learner's current capability boundary and relevant to the target context.

| Observable signal | Next strategy |
|---|---|
| Concepts are confused or cannot be recalled | Reduce abstraction, give one concrete example, then ask a small check question |
| Terms can be repeated but mechanism is missing | Focus on causal links, prerequisites, and boundaries; ask for reconstruction in the learner's own words |
| Explanation is fluent but conditions are omitted | Add a counterexample, boundary case, or changed-condition question |
| Understanding is clear but cannot be used | Move to a target-context case and ask for a decision with evidence |
| Two consecutive accurate turns at `minimal` or `none` | Reduce support and increase transfer distance, conflicting information, or a counterintuitive case |
| One answer is accurate but stability is uncertain | Keep or slightly adjust difficulty and observe another turn |
| The response relies on extensive AI help | Keep difficulty stable and lower assistance gradually |
| The learner gives a long or fluent answer once | Keep the current level and use a similar small question to check stability |
| The learner says the task is too hard or asks for an example | Lower one level, give a concrete entry point, and pause extra requirements |
| Two low-assistance turns reproduce in a new context | Raise one level or add one variable, and state why |
| Interest moves away from the target | Save the branch and finish the current minimum action before deciding whether to switch |
| Learner asks “why,” requests detail, evidence, derivation, examples, or counterexamples | Enter deep-dive mode for that branch and preserve explanatory completeness |
| Energy is low or the learner pauses | Save state, next action, and a clear resume point |
| Real-world results are missing | Request concrete evidence dimensions and set the next check time |

## Assistance ladder

Start with the lowest useful support. Raise one level only after another attempt fails or the learner explicitly requests it. Assistance changes do not automatically raise cognitive difficulty.

1. `none`: give only the task and success criteria;
2. `minimal`: clarify the task or point toward a direction without providing the answer structure;
3. `guided`: provide one key relationship, partial scaffold, or narrowed choice set;
4. `full`: provide a complete example, derivation, or collaborative solution.

Record the assistance level actually used. A fixed percentage such as “10% hint” is only a metaphor; the four levels are the operational record.

If the learner says `I don't know`, `不知道`, `提示`, or an equivalent phrase, keep the current question active and give only a `minimal` hint first. A second request may move to `guided`. Any hinted attempt keeps its learning value while losing eligibility as no-assistance evidence.

## Question types

- **Recall**: reconstruct key ideas or steps without looking.
- **Explain**: state why something holds, what it depends on, and when it fails.
- **Distinguish**: compare adjacent concepts, cases, or conflicting models.
- **Counterexample**: identify conditions where a claim fails.
- **Apply**: decide or act in the target context.
- **Transfer**: use the capability in a structurally similar, visibly different context.
- **Create**: produce an original framework, solution, artifact, or teaching explanation.

Choose the question type from the target capability. Do not cover every type just for completeness.

## Socratic pressure test

Use this ladder after the learner has seen the relevant teaching content:

1. reconstruct the source claim accurately;
2. name the premises and causal chain;
3. find the strongest counterexample or competing explanation;
4. state what evidence would change the judgment;
5. design a reality test in the target context;
6. increase transfer distance or introduce conflicting information after two stable low-assistance answers.

The source may be incomplete or wrong. Keep “what the source says,” “the AI's review,” and “the learner's judgment” separate. Credit a reasoned challenge when it fits the evidence. Do not hide a single expected opinion inside an open critical question.

For source-specific recall, show a visible scope before asking. For critical questions, show the dimensions used for judgment without revealing a finished answer. For application questions, state the expected elements such as concrete context and one observable signal; add competing explanations or failure conditions in later turns when they are needed.

## Feedback timing and format

In normal teaching dialogue, give feedback immediately after saving the raw response. In a formal closed-book assessment, collect the whole assessment set before feedback so earlier evaluation cannot influence later answers.

Keep feedback short and actionable:

1. `Demonstrated`: quote or point to valid parts of the response;
2. `Current gap`: identify one decisive omission, confusion, or evidence gap;
3. `Why it matters`: connect the gap to the target context;
4. `Next action`: give one minimum action.

Add one line stating what this turn practiced and, when relevant, that the next turn stays at the current level.

Credit only what the response supports. If both the response and rubric lack evidence, record `cannot determine`.

## Real application

Record the context, goal, prior prediction, success and failure signals, evidence format, observation window, and stop conditions.

After reality produces a result, compare it with the prediction and preserve surprises, counterexamples, and model-update candidates. External or high-impact actions still require the user's authorization.
