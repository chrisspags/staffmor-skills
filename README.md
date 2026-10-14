# Staffmor skills for Codex, ChatGPT and Claude Code

The 91 roles and methods [Staffmor](https://staffmor.com/) members select for their AI team, in one plugin. This repo is generated from Staffmor's skill catalog (version `1.0.4-dzhng-methods-source`), so it always carries the same skills, word for word. Held skills that are still in review are not included.

## Install

Codex:

```bash
codex plugin marketplace add chrisspags/staffmor-skills
codex plugin add staffmor@staffmor
```

Claude Code:

```
/plugin marketplace add chrisspags/staffmor-skills
/plugin install staffmor@staffmor
```

Then ask for a role by name, for example "act as my accountant" or "be my research and decision partner".

## What's inside

| Category | Skills |
| --- | --- |
| Build and protect | `ai-and-automation-engineer`, `database-administrator`, `legal-and-compliance-researcher`, `quality-and-accessibility-reviewer`, `security-and-privacy-specialist`, `software-engineer` |
| Business and growth | `accountant`, `business-bookkeeper`, `business-operations-partner`, `conversion-and-sales-specialist`, `customer-support-partner`, `data-and-spreadsheet-analyst`, `growth-analyst`, `marketing-and-seo-partner`, `product-and-project-partner`, `publishing-and-indexing-operations-specialist`, `sales-and-customer-growth-partner`, `social-content-producer`, `youtube-seo-specialist` |
| Create and play | `documents-and-presentations-specialist`, `fantasy-and-dfs-analyst`, `game-and-interactive-creator`, `game-reverse-engineering-and-recompilation`, `motion-and-video-creator`, `music-and-creative-hobby-coach`, `sports-betting-analyst`, `visual-designer`, `writer-and-editor` |
| Data and operations | `data-engineering-and-validation-specialist` |
| Design and creation | `channel-packaging-designer`, `data-visualization-designer`, `product-web-designer-and-builder` |
| Everyday life | `aging-parent-care-organizer`, `ai-companion`, `cooking-and-nutrition-partner`, `family-organizer`, `fitness-and-sports-coach`, `health-information-navigator`, `home-and-garden-partner`, `personal-assistant-and-planner`, `personal-finance`, `pet-care-organizer`, `shopping-and-deal-scout`, `travel-and-local-planner`, `wellbeing-and-habit-coach` |
| Learn and explore | `astrology-and-reflection-guide`, `career-coach`, `knowledge-organizer`, `mathematician`, `probability-expert`, `research-and-decision-partner`, `tutor-and-learning-coach` |
| Marketing | `email-sequences-and-lifecycle-email` |
| Other | `accessibility-auditor`, `anthropologist`, `api-tester`, `app-designer`, `backend-architect`, `codebase-onboarding-engineer`, `data-engineer`, `database-optimizer`, `database-reliability-engineer`, `document-generator`, `dr-vale-dfs-analyst`, `dr-vale-sports-betting-analyst`, `executive-summary-generator`, `geographer`, `historian`, `korean-business-navigator`, `mcp-builder`, `model-qa-specialist`, `motion-design-engineer`, `multi-agent-systems-architect`, `numbers-and-reporting`, `performance-benchmarker`, `pricing-analyst`, `research-synthesist`, `salesforce-architect`, `seo-specialist`, `statistician`, `supply-chain-strategist`, `technical-writer`, `ui-finish-gate-reviewer`, `web-designer`, `workflow-architect`, `zk-steward` |
| Project methods | `bounded-auto-research`, `compare-screenshots`, `explore-unknowns`, `write-spec` |
| Technology and quality | `qa-and-reliability-specialist` |

## Credit and licenses

- Staffmor first-party roles and methods: see [LICENSES/README.md](LICENSES/README.md).
- 27 roles adapt [agency-agents](https://github.com/msitarzewski/agency-agents) (MIT, Copyright (c) 2025 AgentLand Contributors): [LICENSES/agency-agents-MIT.md](LICENSES/agency-agents-MIT.md).
- Explore Unknowns, Write Spec, Bounded Auto Research and Compare Screenshots adapt David Zhang's [dzhng/skills](https://github.com/dzhng/skills) (MIT): [LICENSES/dzhng-skills-MIT.md](LICENSES/dzhng-skills-MIT.md).
- Email Sequences and Lifecycle Email adapts Corey Haines's [marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT): [LICENSES/coreyhaines-marketingskills-MIT.md](LICENSES/coreyhaines-marketingskills-MIT.md).

Each skill ends with its own provenance. Adaptations are not endorsed by the original authors. Staffmor is independent of OpenAI and Anthropic.

## For maintainers

`python3 scripts/sync_from_catalog.py` rebuilds the skills from the catalog; `--check` fails if this repo and the catalog differ. `python3 scripts/check_plugin.py` checks OpenAI's published plugin rules.
