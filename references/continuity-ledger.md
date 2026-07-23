# 长篇连续性账本

连续写作、续写或大幅改稿时必须维护。没有账本时，先从已有文本提取；不确定项标记 `UNKNOWN`，不要擅自补成事实。

## 推荐结构

```yaml
work_state:
  current_chapter: 0
  current_time: ""
  current_location: ""
  pov: ""
facts:
  - id: F001
    statement: "可验证事实"
    source: "第几章/用户确认"
    certainty: canon|inference|unknown
characters:
  - name: ""
    goal_now: ""
    emotion: ""
    knowledge: []
    resources: []
    injuries_debts: []
    relationship_states: {}
timeline: []
world_rules: []
items_and_costs: []
foreshadowing:
  - id: P001
    plant: ""
    expected_payoff: ""
    status: planted|hinted|paid|invalidated
    deadline_or_window: ""
open_questions: []
chapter_log:
  - chapter: 0
    goal: ""
    change: ""
    new_facts: []
    ledger_updates: []
```

## 更新与冲突规则

每章结束更新：时间地点、在场人物、角色目标/情绪/资源、关系状态、新事实、伏笔状态、未决问题。若新想法与 `canon` 冲突，优先级为：用户明确要求 > 已发布文本 > 已确认大纲 > 推断 > 临时灵感；提出修复方案，不静默覆盖。

## 写前检查

检查人物是否知道该信息、资源是否已经获得、伤势/债务是否仍存在、规则是否被遵守、时间与移动是否可行、伏笔回收是否改变主线。发现冲突时先列冲突，不直接写正文。
