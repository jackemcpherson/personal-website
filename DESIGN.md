# DESIGN.md

## Purpose
Establish a minimalist, corporate-modern design system inspired by 1960s IBM and Penguin Classics. Prioritize clarity, order, and restraint.

## Design Principles
- Grid-first. Type-led. Color as structure, not decoration.
- Fewer elements. Strong hierarchy. No visual noise.
- Consistency over novelty. Predictable patterns.

## Layout & Grid
- Baseline grid: 8px units (all spacing and sizing align to multiples).
- Container widths: narrow reading column with generous margins.
- Columns: 12-col desktop, 8-col tablet, 4-col mobile.
- Section rhythm: vertical spacing = 6–10 baseline units between major sections.
- Hairline rules only. No ornamental dividers.

## Responsive Breakpoints
- Mobile: ≤480px  
- Tablet: 481–960px  
- Desktop: 961–1440px  
- Wide: >1440px  
Rules scale type, spacing, and columns. Content never exceeds comfortable line length.

## Typography
- **Primary type:** corporate grotesk (Helvetica/IBM Plex Sans/Univers).
- **Secondary type:** readable book serif (Georgia/Tiempos Text/IBM Plex Serif).
- Headings: tight tracking, strong weight contrast. No italics.
- Body: normal tracking, 140–160% line-height.
- Max line length: 60–75 characters.
- Hierarchy: H1 → H6 with fixed ratio steps.

## Color System

### Overall Structure
- **Base:** near-monochrome neutrals (white → charcoal) for most UI.
- **Accent:** single corporate blue as the only vivid hue.
- **Purpose:** neutrals carry design; blue signals interaction and brand.

### Neutral Scale (Light Mode)
- Background light: `#FFFFFF` or `#F8F8F8`
- Background dark: `#F1F1F1` and `#E0E0E0`
- Text primary: `#111111`
- Text secondary: `#555555`
- Borders/hairlines: `#D0D0D0`

### Neutral Scale (Dark Mode)
- Background light: `#181A1B`
- Background dark: `#121314` and `#0C0D0D`
- Text primary: `#FFFFFF`
- Text secondary: `#B0B0B0`
- Borders/hairlines: `#2E2F30`

### Accent Blue
- **IBM Heritage Blue** – `#006699` (base tone)
- Lighter for hover/focus: `#1985B5`
- Darker for active: `#004D73`
- Accessible on both light and dark backgrounds.

### Usage Rules
- Accent for links, hover states, primary buttons, active UI, key brand marks.
- Avoid accent in large backgrounds except hero/banner blocks.
- No other vivid colors; keep others neutral.

### Accessibility
- Blue on white must meet AA contrast for text (≥4.5:1).
- Blue on dark neutrals must meet AA for large and small text.
- Test both normal and hover/focus states.

## Spacing Scale
- Base: 8px. Steps: 4px micro, then 8, 12, 16, 24, 32, 48, 64, 96.
- Vertical rhythm is king; align to baseline multiples.

## Iconography & Graphics

### Style
- **Form:** Flat, monoline, geometric. No skeuomorphism, gradients, or drop shadows.
- **Line weight:** Consistent across all icons (recommended: 1.5–2px at 24px base size).
- **Corners:** Rounded to match type and border radius system.
- **Proportions:** All icons should align to a common pixel grid and visual balance.

### Color & Contrast
- **Light mode:** Icons use near-black (`#111111`) or secondary text grey (`#555555`). Accent blue (`#006699`) only for interactive icons (hover, active, selected).
- **Dark mode:** Icons use white (`#FFFFFF`) or light grey (`#B0B0B0`). Accent blue remains unchanged for interactive states.
- **Contrast:** Icons must meet WCAG AA when used as the sole indicator.

### Usage Rules
- Icons support text, never replace it entirely for core navigation.
- Interactive icons must have visible hover, focus, and active states.
- Avoid decorative-only icons. Every icon must serve a functional purpose.

### Consistency with Theme
- Design vocabulary should match the 1960s modernist corporate aesthetic:
  - Simplified shapes (no unnecessary detail).
  - Clear, rational geometry (IBM design system influence).
  - Even negative space within and around shapes.
- Penguin Classics influence: icons should have clarity and proportion akin to typographic symbols in print, avoiding over-complex or playful forms.

### Sizing
- Standard sizes: 16px, 20px, 24px, 32px.
- Maintain clear optical alignment with text and surrounding UI elements.
- Touch targets for mobile ≥ 40×40px regardless of icon size.

### Source & Format
- Preferred source: single, unified icon set or custom set to maintain stylistic unity.
- Format: SVG for scalability, with stroke/fill controlled via CSS variables.
- All icons should be optimized for minimal file size and crisp rendering on high-DPI screens.

### Motion
- If icons animate (e.g., loading indicators, toggles), motion must be:
  - Functional and minimal.
  - 120–200ms duration.
  - Consistent easing curves across UI.

## Motion
- Functional, subtle: fade, slide, scale.
- Duration: 120–200ms. Easing: standard in/out.
- Respect reduced motion preference.

## Navigation
- Single clear header bar. Left wordmark, right nav.
- Persistent across breakpoints.
- Hover: underline reveal. Active: solid underline + accent.
- No hamburger on desktop. Mobile: single icon + label.

## Links & Buttons
- Links: accent color, underline on hover/focus. Never remove underline in body.
- Primary button: filled accent. Secondary: hairline outline. Tertiary: text-only.
- States: default, hover, active, disabled, focus.
- Dark mode buttons adjust:
  - Primary: accent on dark background.
  - Secondary: light hairline border, lighter hover background.

## Cards & Sections
- Solid backgrounds, 1px hairline borders, 4–8px radius.
- Section headers may use accent or muted panel backgrounds.
- In dark mode: panels use lighter neutral from dark scale.

## Forms
- Inputs: 1px border, 4px radius, generous padding.
- Labels always visible. No placeholder-only labels.
- Error: border + helper text. No color-only indication.
- Focus ring: 2px high-contrast outline outside element.
- In dark mode: inputs use lighter neutral fills with white text.

## Tables
- Dense baseline alignment. Left-align text; right-align numbers.
- Header row: stronger weight or banded background.
- Row hover: subtle background change using light or dark neutral depending on theme.

## Content Rules
- Title case for nav/headings. Sentence case for body.
- Italics only for citations. Bold sparingly.
- No emoji, gradients, drop shadows, or decorative flourishes.

## Accessibility
- WCAG AA min contrast. AAA for body if possible.
- Logical focus order. Keyboard operable.
- Hit targets ≥40×40px.
- Alt text for all imagery.
- Dark mode colors tested for AA compliance.

## Layout Patterns
- Hero: text-first left column, optional image right. No carousels.
- Sections: consistent padding, clear headings, optional solid bands.
- Footer: multi-column list, small print on baseline.

## Elevation & Borders
- Space and alignment over heavy borders.
- Borders: 1px hairline. Shadows minimal and neutral.
- In dark mode: shadows softened or replaced with lighter outlines.

## State System
- Tokens for: interactive-hover, interactive-active, focus-ring, disabled-foreground, disabled-surface.
- Disabled: reduce contrast, remove shadows, not just opacity.

## Token Naming (CSS Variables)
- Color: `--color-bg`, `--color-text`, `--color-accent`, `--color-muted`, `--color-border`
- Type scale: `--font-size-xs` … `--font-size-xxl`; weights `--font-weight-regular|medium|bold`
- Space: `--space-1` … `--space-9`
- Radii: `--radius-0` to `--radius-2`
- Motion: `--motion-duration-fast|base`, `--motion-ease-standard`
- Z-layers: `--z-base`, `--z-sticky`, `--z-overlay`, `--z-modal`

## Theming
- **Light mode default**: as above.
- **Dark mode**:
  - Backgrounds shift to near-black/dark neutrals.
  - Text shifts to white/light neutrals.
  - Accent color remains consistent for brand recognition.
  - Hover states use light neutrals for contrast.
- Maintain contrast parity across modes.

## Content Imagery
- Documentary-style photos. B/W or duotone.
- Geometric crops. Align to grid.

## Error, Empty, Loading
- Error: concise message, guidance, retry link.
- Empty: single icon, short text, primary action.
- Loading: progress bar or spinner. Minimal illustration.

## Governance
- Changes via tokens first; then components.
- New colors or type sizes must meet principles and contrast.
