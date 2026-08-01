# Graph Report - .  (2026-07-29)

## Corpus Check
- Corpus is ~2,923 words - fits in a single context window. You may not need a graph.

## Summary
- 74 nodes · 51 edges · 30 communities (25 shown, 5 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.8)
- Token cost: 17,818 input · 629 output

## Community Hubs (Navigation)
- Safe Calculator & Error Handling (Day 7)
- Project Metadata & Authorship
- Student Grading (Day 9)
- Inheritance Practice (Day 9)
- Module Import Example (Day 8)
- Student Class (Day 9 File1)
- Day 8 Exercise
- Day 8 File3

## God Nodes (most connected - your core abstractions)
1. `Student` - 5 edges
2. `DivbyzeroError` - 3 edges
3. `name()` - 3 edges
4. `Student` - 3 edges
5. `Person` - 3 edges
6. `Student` - 3 edges
7. `Kavya Dahal` - 3 edges
8. `div()` - 2 edges
9. `main()` - 2 edges
10. `Bulletproof calculator (buffer / stretch) Type hints + a custom exception + try` - 1 edges

## Surprising Connections (you probably didn't know these)
- `main()` --calls--> `name()`  [EXTRACTED]
  Day08/module/dummpy.py → Day08/module/helper.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Kavya Dahal Identity** — kavya_dahal, mailmap, data_excersice, data_test_file [EXTRACTED 0.90]

## Communities (30 total, 5 thin omitted)

### Community 1 - "Safe Calculator & Error Handling (Day 7)"
Cohesion: 0.33
Nodes (4): div(), DivbyzeroError, Bulletproof calculator (buffer / stretch) Type hints + a custom exception + try, Exception

### Community 2 - "Project Metadata & Authorship"
Cohesion: 0.33
Nodes (3): ATLAS, Claude, Kavya Dahal

### Community 4 - "Inheritance Practice (Day 9)"
Cohesion: 0.40
Nodes (3): Person, class Person:     def __init__(self, name):         self.name = name      de, Student

## Knowledge Gaps
- **2 isolated node(s):** `Claude`, `ATLAS`
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `Claude`, `ATLAS` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._