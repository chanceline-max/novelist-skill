# 小说家 · Novel Writing Coach ✍️

> 把一个灵感，慢慢写成一个人物会呼吸、剧情会推进、伏笔能回收的故事。

[![Release](https://img.shields.io/github/v/release/chanceline-max/novelist-skill?style=flat-square)](https://github.com/chanceline-max/novelist-skill/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-22c55e?style=flat-square)](LICENSE)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-7c3aed?style=flat-square)](https://developers.openai.com/codex/)

**小说家**是一个面向 Codex 的中文原创小说创作 Skill。它不只负责“写几段好看的文字”，还会帮你管理大纲、人物、世界观、伏笔、时间线和章节连续性，让长篇故事不容易写着写着就散架。

适合写玄幻、都市、言情、悬疑、现实、无限流，以及更多需要持续推进和长期记忆的故事。

## 它能做什么？🚀

- 从一个模糊灵感出发，找到真正能展开的故事核心
- 设计主角欲望、主要阻力、人物弧光和关系变化
- 搭建卷纲、章纲，让情节由选择和代价推动
- 直接写章节、续写正文、扩写场景或重写问题段落
- 检查角色突然降智、设定打架、节奏拖沓和情绪跳跃
- 维护人物、世界观、伏笔、时间线、章节索引和章节总结
- 针对不同题材切换创作策略，同时保持故事逻辑
- 对正文执行反模板化检查，减少机械感、套路腔和空洞抒情

## 30 秒安装 ⚡

### 方法一：直接让 Codex 安装

在 Codex 中调用 `$skill-installer`，并告诉它：

```text
请从 https://github.com/chanceline-max/novelist-skill 安装这个 skill。
```

### 方法二：手动安装

macOS / Linux：

```bash
git clone https://github.com/chanceline-max/novelist-skill.git \
  ~/.agents/skills/novel-writing-coach
```

Windows PowerShell：

```powershell
git clone https://github.com/chanceline-max/novelist-skill.git `
  "$HOME\.agents\skills\novel-writing-coach"
```

Codex 通常会自动发现新安装的 Skill。如果暂时没有出现，重启一次 Codex 即可。

## 怎么用？🎬

在提示词里点名 `$novel-writing-coach`，然后直接说你想做什么。

### 从零策划

```text
$novel-writing-coach

我想写一个都市悬疑故事：一个替人整理遗物的女孩，
发现每位客户都在隐瞒同一个人的存在。
帮我找到核心卖点，并设计主角、主要矛盾和第一卷大纲。
```

### 写第一章

```text
$novel-writing-coach

根据当前大纲写第一章，约 2500 字。
开场要尽快出现异常，但不要急着解释真相。
```

### 长篇续写

```text
$novel-writing-coach

读取当前小说项目，先检查人物状态、未回收伏笔和时间线，
然后续写下一章。不要让角色知道他们尚未获得的信息。
```

### 改稿救场

```text
$novel-writing-coach

这章读起来很平，帮我诊断问题。
保留关键事件，但加强目标、阻力、选择和代价，不要只做句子润色。
```

## 它和普通“帮我写小说”有什么不同？🧠

普通提示词常常只关注这一段写得顺不顺。**小说家**更关心故事能不能继续活下去：

1. 人物为什么做这个选择？
2. 这个选择造成了什么新问题？
3. 本章结束后，关系、信息、资源或局势改变了吗？
4. 前文留下的设定、伏笔和时间线还对得上吗？
5. 文字是在推进故事，还是只是在制造“很像小说”的感觉？

它会把这些问题变成一套持续工作的创作流程。

## 内置长篇记忆系统 🗂️

仓库附带一个可直接复制使用的小说项目模板：

```text
assets/novel-project/
├── 大纲.md
├── 人物.md
├── 世界观.md
├── 伏笔.md
├── 时间线.md
├── 章节索引.md
├── 章节总结/
├── 素材库.md
└── 反馈与改稿.md
```

这些文件不是为了增加仪式感，而是为了让几十章之后的故事依然记得：

- 谁知道什么，谁还不知道
- 哪段关系已经改变
- 哪个道具被谁拿走
- 哪条伏笔应该回收
- 事件究竟发生在哪一天

## 仓库结构

```text
.
├── SKILL.md                 # 核心工作流与写作规则
├── agents/openai.yaml       # Skill 展示信息
├── references/              # 大纲、人物、伏笔、连续性等方法模块
├── assets/novel-project/    # 可复用的长篇小说项目模板
└── scripts/search_corpus.py # 项目材料检索工具
```

## 小提醒 🌱

- 它是创作教练和编辑，不是“一键爆款保证器”。
- 好故事仍然需要你的判断、生活经验和真实表达。
- 生成内容应保持原创；可以学习方法，不要模仿具体作者的独特表达。
- 长篇创作时，建议把大纲和连续性文件与正文一起维护。

## 一起把它变得更好

如果它帮你解决了卡文、人物失控或长篇失忆，欢迎：

- 点一个 ⭐ Star，让更多写作者遇见它
- 提交 Issue，分享你遇到的创作问题
- 提交 PR，增加新的题材适配器或工作流
- 分享你的使用案例——成功案例和翻车现场都很有价值

## English

**Novel Writing Coach** is a Codex Skill for planning, drafting, continuing, and revising original fiction. It treats a novel as a living story system—not just a stream of polished paragraphs.

It helps you:

- turn a rough idea into characters, conflict, and a workable outline;
- draft and revise chapters with clear goals, obstacles, choices, and costs;
- track character knowledge, relationships, world rules, foreshadowing, and timelines;
- keep long-form stories consistent across many chapters;
- reduce generic, mechanical, and overly templated prose.

Install the repository into `~/.agents/skills/novel-writing-coach`, then invoke it in Codex:

```text
$novel-writing-coach

Help me plan a mystery novel about an archivist who discovers
that every missing-person file was edited by someone who does not exist.
```

The instructions are primarily optimized for Chinese-language fiction, but the story-planning and continuity workflows can be adapted to other languages.

---

如果你也相信“人物的选择，比漂亮句子更能推动故事”，欢迎 Star 这个项目。✨

