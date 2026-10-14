---
name: write-spec
description: Turn a large feature into small, verifiable units with explicit seams, preserved behavior and a current handoff. Use before building anything that needs more than one finished unit, or when a unit has grown too big to review.
---

Method only: it adds no tools, accounts or permissions. Follow the user's request, the project's own rules and the tools actually available.

# Write a finite spec

Recover the existing goal, scope decisions, project conventions and accepted evidence before drafting. Reuse the current spec or task packet. Read the contract checklist (included below) for a multi-unit feature. No agent fan-out, permission change or release follows from writing a plan.

1. Define the user outcome, exclusions, constraints and first useful observable result. Inspect code before asking source-answerable questions. Record compatibility, migration, privacy and recovery requirements from actual consumers; never assume a hard cutover is safe.
2. Research only the unfamiliar dependency that affects the next decision. Use primary sources and exact revisions. If porting a proven experiment, read and freeze its code, inputs, configuration and evidence before redesigning it.
3. Divide work at a meaningful API or behavior seam. Each unit has one question, one writer, pinned inputs, explicit outputs, acceptance evidence, allowed edits and a stop boundary. Name dependencies; do not require parallel agents merely because work can be divided.
4. For visual work, retain the approved direction and existing design process. Provide a runnable surface or captured example suited to the question. Isolate one material visual variable when useful; fixtures, rendered behavior and actual device acceptance remain distinct.
5. Map preserved behavior to its owning unit and parity check. Name deliberately delegated implementation choices. A material unassigned choice is a gap to resolve, not a silent new requirement.
6. Read the plan for duplicated ownership, missing consumers and forgotten owner corrections. When an implementation reveals extra scope, reslice that affected unit instead of broadening its patch.

Keep a short current handoff: completed result, next finite unit, exact blockers, remaining checklist and source/evidence pointers. The coordinator verifies a finished unit and authorizes the next through the existing process. A plan is ready when another worker can execute the next unit without reverse-engineering the chat. A plan marked complete is not a shipped feature; reconcile all promised decisions and actual delivery evidence before that claim.

Derived from David Zhang's MIT-licensed `write-spec`; see pinned provenance and adaptations (embedded provenance below).

# Contract and preservation checks

For each unit record:

- Original goal/task and accountable writer; exact allowed files and relevant consumers.
- Pinned source/data/runtime, input/output contract and dependency on prior accepted work.
- The smallest artifact someone can run, inspect or reproduce.
- Observable acceptance, meaningful failure control where needed, and unchanged behavior that must remain true.
- Deliberately delegated choices, known limitations, completion boundary and owned next action.

For an accepted experiment, make a compact **behavior → evidence → unit → parity check** table. Preserve the actual winner, including behavior whose contribution is unknown. Separate required differences from experiments. Check matched requests, decisions, complete outputs and relevant recovery through the production entry point before costly confirmation; a template resemblance is not parity.

For UI or imagery, name the intended target and comparable capture state. The existing design owner keeps exploration and taste. Comparison evidence may use Compare Screenshots; do not declare a fixture to be an installed or live result. Reuse unaffected accepted evidence.

Material missing credentials or dependencies stay explicit. A labelled placeholder can advance independent work, but cannot close an actual integration requirement. Required owner decisions remain pending; a reversible implementation choice already within scope does not need another approval.

Before closeout, reconcile every promised decision against the final artifact, including decisions that never became their own unit. Record implemented, no change required, deferred by owner, or unresolved. Keep the current handoff concise and retire superseded instructions with a pointer.


Source and license
Curated for Staffmor (staffmor.com) by GPT Skipper from David Zhang, dzhng/skills.
Exact source revision: d51322866ffa298838346960414d18a221b52588
Source: https://github.com/dzhng/skills/blob/d51322866ffa298838346960414d18a221b52588/skills/engineering/write-spec/SKILL.md
Original source SHA256: d85197bd76497e0b200f0722955fde6c8d6d2196ff8db3638042c51e2fb1269d
Curated private source SHA256: c555c18f5561e4dec3fa95b60bb445ad184d75d194bf9b030936e6a86f2c5b0d
The project's own design source stays authoritative; this method adds no replacement.

MIT License

Copyright (c) 2026 David Zhang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
