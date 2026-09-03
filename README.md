# 富豪技能 · Fuhao Skills

一组面向 AI Agent 的可复用 Skills，帮助你把 AI 从聊天工具变成能够持续协作的能力系统。

## 目前有哪些 Skill

| Skill | 它能帮你完成什么 | 状态 |
|---|---|---|
| [`fuhao-learning-loop`](skills/fuhao-learning-loop/) | 把材料、主题或现实问题，推进为能够独立回忆、审辩、应用、迁移并复测的能力 | v0.6.0 |

### fuhao-learning-loop：把“看过”变成“真正会用”

你可以交给它一篇文章、一本书、一段视频逐字稿、一个课程、一场会议，或一个想要攻克的现实问题。它会围绕你的目标自动完成：

- 第一次使用先给一段简明说明；材料已经发来时会同时开始处理；
- 一次采集多份材料时，可以先低打扰保存，再按时间范围选择、去重和聚类；AI 会围绕目标标出共识、分歧、逐来源证据和下一步主线；
- 每次新会话首次运行时轻量检查 GitHub 版本；只有发现新版本才提醒，检查失败不会影响学习；
- 先判断你已经会什么、真正卡在哪里；
- 根据目标、信息增量和证据强度，建议“先留档、快速了解、深入学习”；
- 先给足够判断价值的一屏导航，再主动推荐当前最值得继续的一条路径并说明原因；
- 你只说“深度学习”，AI 就会自动进入推荐方向；“详细讲讲这个机制”“我对案例更感兴趣”“换一个方向”也能直接理解；
- 编号继续作为可选快捷方式，完整讲解会覆盖机制、证据、案例、反例和边界，不受固定短摘要限制；
- 用小段讲解、复述考察和苏格拉底追问推动理解；
- 先展示会考什么，再只考已经学过的内容，不会要求你回原文寻找未讲过的答案；
- 把材料当作可审查的观点，追问前提、反例、竞争解释和现实证据，有依据地反驳也能获得高评价；
- 卡住时先给很小的方向提示并留在原题，同时记录辅助程度；
- 根据你的真实回答，自动加深、补课或调整难度；
- 把知识放进现实任务，继续检验应用与迁移；
- 同时管理多份学习材料，并从编号列表或引用消息切回任意一份；
- 保留学习进度，并在几天后进行低辅助复测；宿主支持调度时可主动提醒到期项。

最终结果是：你能在没有答案提示的情况下，自己讲清楚、做出来、迁移到新场景，并在延迟复测中再次证明掌握。

AI 负责阅读、筛选、拆解、出题、反馈、调整路径、记录状态和调度到期项；你只需要给出学习目标与兴趣选择、独立作答、完成现实行动并确认最终掌握。

## 30 秒安装

你只需要做两步：复制与你使用的 Agent 对应的整段口令，发送并等待安装回执；随后发送第一条真实学习需求。

### Codex（推荐）

把下面整段复制给 Codex：

```text
请使用 $skill-installer 安装并验证这个 Skill：
https://github.com/itsrichardfu/fuhao-skills/tree/main/skills/fuhao-learning-loop

安装到当前用户的 Skills 目录，并保留 SKILL.md、references、scripts、templates 和 evals 的完整结构。如果同名 Skill 已存在：先读取本地与 GitHub 的版本；版本相同就停止，版本较旧则把旧目录备份到同级带时间戳的目录，再安装新版。安装或验证失败时恢复旧目录。最后检查 metadata.version、相对引用和脚本，并用“带我学习一个主题”验证触发。只回复安装路径、版本、验证结果、备份路径（首次安装写“无”）和是否需要重启 Codex。
```

安装成功后的下一条消息可以这样写：

```text
$fuhao-learning-loop 带我学习产品定价。我希望最后能独立给自己的产品定价。
```

也可以直接用自然语言：

```text
请使用 fuhao-learning-loop 帮我内化这篇材料：<材料链接>
```

Codex 通常会自动发现新 Skill；没有出现时再重启 Codex。官方说明见 [Codex Skills](https://developers.openai.com/codex/skills)。

### Claude Code

把下面整段复制给 Claude Code：

```text
请从这个 GitHub 地址安装并验证 fuhao-learning-loop：
https://github.com/itsrichardfu/fuhao-skills/tree/main/skills/fuhao-learning-loop

安装到 ~/.claude/skills/fuhao-learning-loop/，保留 SKILL.md、references、scripts、templates 和 evals 的完整结构。如果同名目录已存在：先比较本地与 GitHub 版本；版本相同就停止，版本较旧则把旧目录备份到同级带时间戳的目录，再安装新版。安装或验证失败时恢复旧目录。最后检查 SKILL.md 和相对引用，再用“带我学习一个主题”验证自动触发。只回复安装路径、版本、验证结果、备份路径（首次安装写“无”）和是否需要重启 Claude Code。
```

安装后可以直接输入：

```text
/fuhao-learning-loop 带我学习产品定价。我希望最后能独立给自己的产品定价。
```

Claude Code 会监听已经存在的 Skills 目录；首次创建顶层目录时需要重启一次。官方说明见 [Claude Code Skills](https://code.claude.com/docs/en/skills)。

### 安装成功的判断

Agent 的回执需要同时包含：

- 安装路径与 `metadata.version`；
- `SKILL.md` 及四个配套目录完整；
- Skill 已被客户端发现；
- “带我学习一个主题”能够触发首次引导和学习目标对齐。

只复制了一个 `SKILL.md`、目录缺失或只能手动粘贴提示词，都不算完整安装。

### 安装后会获得什么

- Codex、Claude Code 等支持 Skills 的 Agent 会获得完整学习交互：目标对齐、材料深挖、多材料综合、苏格拉底考察、应用、迁移和复测协议；
- 飞书机器人、消息引用恢复、长期数据库、卡片和主动提醒需要宿主提供对应接口；缺少这些能力时，Skill 会使用便携状态卡继续工作；
- 安装 Skill 不会自动创建飞书机器人、读取个人知识库或取得额外权限。任何外部读取与写入仍由宿主权限和用户授权决定。

### 隐私与联网

仓库不包含账号凭据或学习记录。版本检查只读取 GitHub 上公开的 `SKILL.md` 版本号，并在本机缓存检查时间；不会上传学习材料。宿主无法运行脚本或无法联网时会静默跳过检查，不影响学习。

### 更新

Skill 每个新会话最多检查一次公开版本，24 小时内使用缓存。发现新版时只提醒，不会自行覆盖。看到提醒后，把上面的同一条安装口令再次发给 Agent，它会先备份旧版，再验证更新与回退路径。

## 其他安装方式

### 通用 Agent Skills 客户端

让 Agent 把完整的 `skills/fuhao-learning-loop/` 目录安装到客户端扫描的用户级或项目级 Skills 目录。例如：

```text
<project>/.agents/skills/fuhao-learning-loop/
```

### WorkBuddy / CodeBuddy

把完整技能目录放入项目的 `.codebuddy/skills/`，或通过 WorkBuddy 的 Skill 管理界面导入：

```text
<project>/.codebuddy/skills/fuhao-learning-loop/
```

参考：[WorkBuddy Skills 文档](https://www.workbuddy.ai/docs/zh/ide/Features/Skills)。

### 豆包工作

豆包工作支持自定义和团队共享 Skill。不同客户端版本的导入入口可能变化：

1. 优先尝试在“技能”或“自定义技能”界面导入 `skills/fuhao-learning-loop/`；
2. 当前版本无法导入目录时，使用 [`templates/prompt-only.md`](skills/fuhao-learning-loop/templates/prompt-only.md) 创建单文件技能；
3. 看到技能名称成功加载，并完成一次测试对话后，再视为安装成功。

参考：[豆包工作团队版](https://www.doubao.com/work/group)。

### 只有对话框的 Agent

把 [`templates/prompt-only.md`](skills/fuhao-learning-loop/templates/prompt-only.md) 作为系统提示词或首条提示词。没有持久化工具时，Agent 会在暂停或结束时输出便携学习状态卡。

## 仓库约定

- 所有技能优先遵循 [Agent Skills 开放规范](https://agentskills.io/specification)，以 `SKILL.md` 为入口，按需携带 `references/`、`scripts/`、`assets/` 或模板。
- 每个技能放在 `skills/<skill-name>/`，目录名与 `SKILL.md` 的 `name` 保持一致。
- 核心流程不依赖某个厂商、数据库或笔记软件。
- 平台专属路径、能力差异和降级方式写入技能自己的适配文档。
- 技能只有在真实场景测试后才提升版本号。
- 禁止提交凭据、个人绝对路径、私有消息、学习记录或第三方受限材料。

运行本地校验：

```bash
python3 scripts/validate_skills.py
```

## License

[MIT](LICENSE) © 2026 Richard Fu
