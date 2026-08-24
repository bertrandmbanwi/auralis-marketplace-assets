# Syntalume 0.10.0 media provenance

Cutover set prepared 2026-08-24. This record distinguishes genuine application
captures from permitted mechanical processing.

## VS Code set

- Source: the reviewed real-VS-Code Syntalume capture set committed to
  `bertrandmbanwi/auralis-site` PR 3 at
  `27158533e97c73e7de7a812d2979d198bb3cac8d`.
- Processing: WebP-to-PNG conversion, metadata removal, and color-profile
  normalization only. No UI, text, product state, or branding was generated or
  reconstructed.
- `marketplace-hero.png` comes from `platform-vscode-1280.webp`.
- Theme, language, and icon filenames come from the same-named 1280-wide site
  capture where available. `hero-botanica.png` comes from
  `variant-botanica-1280.webp`.
- The two compatibility-named GIFs are four-second sequences made only from
  those real VS Code frames. They are visual theme tours, not feature-webview
  demonstrations.
- The legacy `feature-*.png` paths remain to avoid breaking older Marketplace
  revisions. They now contain neutral real editor captures and are not used as
  proof of a particular feature UI.

## JetBrains set

- Source: the real PyCharm 2025.3 Syntalume 0.10.0 captures previously
  committed on this branch.
- Processing: each source was cropped to remove the operator's local workspace
  path and trial-status chrome, then metadata was removed. The 1280x800
  Marketplace files are resized from those crops. No application UI was added
  or reconstructed.

## Release checks

- Every PNG has the documented output dimensions.
- Both GIFs are 960x540 and four seconds per loop.
- OCR review found no `Auralis` branding, local `.codex`/ChatGPT path, trial
  marker, email address, token, or secret in the shipping set.
- `media/SHA256SUMS` pins the exact release bytes.

