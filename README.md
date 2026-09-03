# 富豪技能 · Fuhao Skills

一组面向 AI Agent 的可复用 Skills，帮助你把 AI 从聊天工具变成能够持续协作的能力系统。

## 目前有哪些 Skill

| Skill | 它能帮你完成什么 | 状态 |
|---|---|---|
| [`fuhao-learning-loop`](skills/fuhao-learning-loop/) | 把材料、主题或现实问题，推进为能够独立回忆、解释、应用、迁移并复测的能力 | v0.1.0 |

### fuhao-learning-loop：把“看过”变成“真正会用”

你可以交给它一篇文章、一本书、一段视频逐字稿、一个课程、一场会议，或一个想要攻克的现实问题。它会围绕你的目标自动完成：

- 先判断你已经会什么、真正卡在哪里；
- 从长材料中筛出当前最值得学习的部分；
- 用小段讲解、复述考察和苏格拉底追问推动理解；
- 根据你的真实回答，自动加深、补课或调整难度；
- 把知识放进现实任务，继续检验应用与迁移；
- 保留学习进度，并在几天后进行低辅助复测。

最终结果是：你能在没有答案提示的情况下，自己讲清楚、做出来、迁移到新场景，并在延迟复测中再次证明掌握。

AI 负责阅读、拆解、出题、反馈、调整路径和记录状态；你只需要给出学习目标、独立作答并完成现实行动。

## 一句话安装（推荐）

已经在使用 **Codex** 或 **Claude Code**？直接把下面整段发给它，剩下的交给 Agent：

```text
请帮我安装并验证这个 Agent Skill：
https://github.com/itsrichardfu/fuhao-skills/tree/main/skills/fuhao-learning-loop

请自动识别当前是 Codex 还是 Claude Code，并安装到当前用户的全局 Skills 目录，让所有项目都能使用。Codex 请优先使用内置 skill-installer；Claude Code 请遵循官方个人 Skills 目录规范。请保留 SKILL.md、references、templates 和 evals 的完整目录结构。

如果已经存在同名 Skill，请先备份旧版本，再更新；更新失败时自动恢复。安装后请检查目录完整性，读取 metadata.version，并用“带我学习一个主题”做一次触发测试。最后只告诉我：安装路径、版本、验证结果，以及是否需要开启新对话。
```

你只需要完成两步：

1. 复制上面的口令给 Agent；
2. 等它回复“安装成功”。

### Codex

安装完成后的下一条消息可以这样写：

```text
$fuhao-learning-loop 带我学习产品定价。我希望最后能独立给自己的产品定价。
```

也可以直接用自然语言：

```text
请使用 fuhao-learning-loop 帮我内化这篇材料：<材料链接>
```

如果 Skill 没有立刻出现，开启一个新对话后再试。

### Claude Code

Claude Code 的个人 Skill 会安装到：

```text
~/.claude/skills/fuhao-learning-loop/
```

安装后可以直接输入：

```text
/fuhao-learning-loop 带我学习产品定价。我希望最后能独立给自己的产品定价。
```

Claude Code 通常会自动发现新 Skill；首次创建个人 Skills 顶层目录时，重启一次 Claude Code 即可。

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
