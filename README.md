# Syntalume Marketplace Assets

Public media used by the Syntalume (formerly Auralis) VS Code Marketplace
listing and marketing site.

> **Rebrand status:** the media in this branch still shows the Auralis-era
> product. Every image is scheduled for recapture from the packaged Syntalume
> build in the real IDEs (see the source repo's
> `docs/rebrand/SCREENSHOT-MANIFEST.md`); filenames stay stable because the
> live listing hotlinks their raw URLs. Nothing here is ever mocked,
> composited, or AI-generated.

## Live capture standard

- Every editor or plugin image must come from the installed Syntalume package in
  the real VS Code or JetBrains application. The restored theme gallery was
  captured from Auralis `0.8.1` (pre-rename); the Tune, Icon Studio, Accessibility Lab, and
  feature-tour media was captured from the packaged Auralis `0.9.0` VSIX (pre-rename).
- VS Code PNGs use a consistent `1280x720` output. The feature-tour GIF is
  assembled only from real VS Code frames.
- JetBrains source images are real PyCharm captures. Their `1280x800`
  Marketplace variants may be cropped or resized from those captures without
  adding or reconstructing UI.
- Existing filenames stay stable because Marketplace and website copy use
  their raw GitHub URLs.
- Allowed processing is limited to cropping, resizing, color-profile
  normalization, and GIF sequencing or compression.

Do not replace product screenshots with AI-generated editor interfaces, HTML
reconstructions, or other mockups. Update the installed extension or plugin,
capture the real application, and visually verify every referenced filename
before publishing.
