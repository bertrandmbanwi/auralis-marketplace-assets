# Syntalume Marketplace Assets

Public media used by the Syntalume (formerly Auralis) VS Code Marketplace
listing and marketing site.

> **Candidate status:** the 31 PNGs match the privacy-clean capture inventory
> used by the source candidate. Existing records describe real VS Code and
> PyCharm captures; no replacement editor interfaces were generated.
> Final visual approval must cover the remediated package actually published.
> See [provenance and limitations](MEDIA-PROVENANCE.md).
>
> Both legacy GIF URLs remain only for historical link compatibility. They
> loop indefinitely and are retired from current README, website, onboarding,
> and Marketplace embeds. Use the static `variant-noir.png` preview instead.

## Live capture standard

- Every editor or plugin image must come from the installed package in the real
  VS Code or JetBrains application.
- VS Code PNGs use a consistent `1280x720` output. Shipping previews are
  static images. The archived GIFs run four seconds per cycle and repeat
  indefinitely; they are not current accessible presentation assets.
- The legacy `feature-*.png` paths remain available so old listing revisions
  do not break. They now contain neutral real Syntalume editor captures and
  are not presented as evidence of a specific feature webview.
- JetBrains source images are real PyCharm captures. They are cropped to omit
  the operator's local workspace path and trial-status chrome. Their
  `1280x800` Marketplace variants are resized from those crops without adding
  or reconstructing UI.
- Existing filenames stay stable because Marketplace and website copy use
  their raw GitHub URLs.
- Allowed processing is limited to cropping, resizing, color-profile
  normalization, and GIF sequencing or compression.

Do not replace product screenshots with AI-generated editor interfaces, HTML
reconstructions, or other mockups. Update the installed extension or plugin,
capture the real application, and visually verify every referenced filename
before publishing.

## Integrity gate

Run `node scripts/check-media.js`, `python3 scripts/test-decode-media.py`, and `python3 scripts/decode-media.py` before committing media. Install the pinned QA-only Pillow dependency from `requirements-qa.txt`. The decoding check reads every PNG and GIF frame and rejects corrupt content and known identifying metadata patterns; visible privacy still requires human review. Every PR must pass the Media integrity workflow; changing image bytes requires updating the checksum manifest and reviewing the actual image.
