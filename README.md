# 富豪技能 · Fuhao Skills

一组面向 AI Agent 的可复用 Skills。仓库采用多 Skill 结构，每个技能都可以独立安装、升级和使用。

所有技能优先遵循 [Agent Skills 开放规范](https://agentskills.io/specification)：以 `SKILL.md` 为入口，按需携带 `references/`、`scripts/`、`assets/` 或模板。

## Skills

| Skill | 用途 | 状态 |
|---|---|---|
| [`fuhao-learning-loop`](skills/fuhao-learning-loop/) | 把材料、主题或现实问题推进为能够独立回忆、解释、应用、迁移并复测的能力 | v0.1.0 |

## 安装

先克隆仓库：

```bash
git clone https://github.com/itsrichardfu/fuhao-skills.git
```

### Agent Skills 兼容客户端

将目标技能目录复制或链接到客户端扫描的 Skills 目录。例如，项目级通用目录通常是：

```text
<project>/.agents/skills/fuhao-learning-loop/
```

### WorkBuddy / CodeBuddy

将技能放入项目的 `.codebuddy/skills/`，或者通过 WorkBuddy 的 Skill 管理界面导入：

```text
<project>/.codebuddy/skills/fuhao-learning-loop/
```

参考：[WorkBuddy Skills 文档](https://www.workbuddy.ai/docs/zh/ide/Features/Skills)。

### 豆包工作

豆包工作支持自定义和团队共享 Skill。不同客户端版本的导入入口可能变化：

1. 优先尝试在“技能”或“自定义技能”界面导入 `skills/fuhao-learning-loop/`；
2. 若当前版本无法导入目录，使用 [`templates/prompt-only.md`](skills/fuhao-learning-loop/templates/prompt-only.md) 创建单文件技能；
3. 看到技能名称成功加载，并完成一次测试对话后，再视为安装成功。

参考：[豆包工作团队版](https://www.doubao.com/work/group)。

### 只有对话框的 Agent

把 [`templates/prompt-only.md`](skills/fuhao-learning-loop/templates/prompt-only.md) 作为系统提示词或首条提示词。没有持久化工具时，Agent 会在暂停或结束时输出便携学习状态卡。

## 仓库约定

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
