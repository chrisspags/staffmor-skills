---
name: compare-screenshots
description: "Compare matched visual captures to an intended reference with local landmarks and honest evidence. Use it to locate and resolve a reported visual difference against an approved reference."
---

Expertise method only; preserve the original authorized scope, existing actor/task, actual tools and required checks. No accounts, credentials, grants, model workers or publication are authorized by these instructions.

# Compare visible results

Read the original visual requirement and Staffmor's existing App Designer guidance when doing product design. This procedure adds reference-comparison evidence; it does not duplicate App Designer, create a reviewer or authorize capture, dependency installs or publication. Use permitted existing tools and the landmark method (included below).

1. Identify the intended target. An owner-approved reference and corrections govern; a historical screenshot is an earlier attempt and may be wrong. If intent is materially ambiguous, present the pair and a concrete recommendation through the existing decision route.
2. Confirm comparable viewport, DPR, route, UI/data state, time, framing, fonts and assets. Record differences; fix capture setup or limit the claim to a comparable region. Keep original captures and clearly label crops or alignment images.
3. Before changing code, measure visible anchors in the target: glyphs, rule endpoints, icon edges, silhouette and local contrast. Record reference → candidate → delta → pass/fix/uncertain. Distinguish opaque/core edges from transition and faint fringe.
4. Inspect all four boundaries and every foreground feature crossed by a changed effect. Include the full fade and surrounding context. A crop at the component box or a global similarity score can hide clipping, dimmed text or spill.
5. Judge each material divergence against the intended result: missing content, framing, hierarchy, overlap, contrast, blur, spacing or style. Metrics locate differences; a lower distance cannot decide which image is correct. Use only metrics that answer the actual question and available tools that have been inspected.
6. Return one scoped verdict: candidate closer, baseline closer, both need correction, or unresolved. Retain local findings even when the whole image looks attractive. Recapture only the corrected boundary and affected neighbors; carry unaffected evidence.

Use the existing named independent reviewer when the current work requires one. Author inspection remains author inspection. Do not hide detail, crop away a defect or alter the application scale to improve a score. Captured fixtures, installed builds, browser viewport checks and physical-device/live acceptance establish different boundaries.

Derived from David Zhang's MIT-licensed `compare-screenshots`; see pinned provenance and adaptations (embedded provenance below). Its optional image scripts and dependencies are not imported.

# Local landmarks before global scores

Record capture identity and the intended target, then fill the reference column before tuning the candidate.

| Feature | Reference observation/range | Candidate | Delta | Verdict/evidence |
| --- | --- | --- | --- | --- |
| Rule endpoint | Position relative to last glyph | Measured position | Local distance | Pass, fix or uncertain; crop pointer |
| Soft boundary | Core, transition and outer fringe on each side | Same observations | Extent/contrast difference | Preserve surrounding context |

Inspect top, right, bottom and left independently. Check text, lines, icons and nearby panels for brightness, color, sharpness and continuity through an effect. Legibility alone does not prove the intended contrast survived.

Preserve native-scale originals. If raster dimensions differ, document the mapping; if unknown, compare ratios to a stable landmark and disclose the limitation. Derived crops supplement the full frames. Recheck bounds after geometry changes so a crop does not conceal a new tail or overflow.

When texture or lighting could masquerade as an effect, an authorized same-state effect-on/off pair can isolate it. Label that diagnostic; retain the normal image. If isolation is unavailable, report uncertainty rather than inventing an exact opacity.

Pixel difference, luminance, edge energy, masks or element dimensions may answer specific questions. Whole-frame averages are weak evidence for a local defect. An empty capture can have a misleading similarity score; inspect visible content first. No upstream metric script, image package or fixed numeric acceptance threshold is supplied by this skill.

A neutral reviewer gets the intended target, normal full frames and matched detail crops, without the author's favored answer or prior verdict. Independent agreement cannot cancel an unresolved local discrepancy. After a correction, revisit affected neighbors and the table before declaring that boundary finished.


Source and license
Adapted by GPT Skipper for bounded Staffmor work from David Zhang, dzhng/skills.
Exact source revision: d51322866ffa298838346960414d18a221b52588
Source: https://github.com/dzhng/skills/blob/d51322866ffa298838346960414d18a221b52588/skills/visual/compare-screenshots/SKILL.md
Original source SHA256: bf514a2ee89e7c2ded88e52d178333e5623d5c67ed3eafb1825c2e9458c7b305
Curated private source SHA256: d1275aad41375b42f90b97ad6a9cea2c1b280130b3912140a87b6154d56b3804
Original App Designer remains the required design source; this method adds no replacement.

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
