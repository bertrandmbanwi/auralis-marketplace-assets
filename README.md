# Auralis Marketplace Assets

Public media used by the Auralis VS Code Marketplace listing and marketing site.

## Media standard

- VS Code product compositions are rendered deterministically at `1280x720`
  from the exact shipped theme JSON, file SVGs, and product-icon font.
- `auralis-feature-tour.gif` shows Tune 2, Icon Studio, terminal export, and
  Environment Guard in one short first-fold story.
- Feature stills cover Tune 2, Icon Studio, and Accessibility Lab.
- JetBrains upload images are rendered at the Marketplace-required `1280x800`
  and kept separately from VS Code imagery.
- Existing filenames stay stable because Marketplace and website copy use
  their raw GitHub URLs.

Generated compositions must use checked-in product assets and pass the source
repository's media build. Real clean-profile VS Code and JetBrains captures
remain the visual-regression evidence; do not label compositions as live UI
captures.
