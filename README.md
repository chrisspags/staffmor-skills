# Staffmor skills for Codex, ChatGPT and Claude Code

Five working methods [Staffmor](https://staffmor.com/) gives its AI teams, packaged as one plugin:

| Skill | Use it to |
| --- | --- |
| `explore-unknowns` | Map what is known, unknown and undecided before a hard decision |
| `write-spec` | Turn a big feature into small units you can each verify |
| `auto-research` | Run a bounded experiment with a fixed baseline and measured results |
| `compare-screenshots` | Check a build against its visual reference with matched captures |
| `email-sequences` | Plan and write welcome, nurture, onboarding and win-back email that converts |

## Install

Codex:

```bash
codex plugin marketplace add staffmor/plugins
```

Then open the plugin directory in Codex and install **Staffmor**.

Claude Code:

```bash
/plugin marketplace add staffmor/plugins
/plugin install staffmor@staffmor
```

## Credit

Every skill keeps its original author's credit and license:

- `explore-unknowns`, `write-spec`, `auto-research` and `compare-screenshots` are adapted from David Zhang's [dzhng/skills](https://github.com/dzhng/skills) (MIT, see [LICENSES/dzhng-skills-MIT.md](LICENSES/dzhng-skills-MIT.md)).
- `email-sequences` is adapted from Corey Haines's [marketingskills](https://github.com/coreyhaines31/marketingskills) `emails` skill (MIT, see [LICENSES/coreyhaines-marketingskills-MIT.md](LICENSES/coreyhaines-marketingskills-MIT.md)).

Each skill file ends with its exact source revision and hashes. These adaptations are not endorsed by the original authors.

Staffmor is independent of OpenAI and Anthropic.
