# Soft Slate Dark

A medium charcoal Obsidian theme with warm text and clearly separated panels.

Historical design plan from 13 November 2026. See the [README](README.md) for the current theme and installation instructions.

At the time of planning, Soft Slate Dark was a working name that still needed a Community name check.

Search keywords: Obsidian theme, soft dark mode, charcoal, medium dark, warm text.

## Who this is for

People who find black themes too dark and bright light themes uncomfortable.

## User need and evidence

Users explicitly request a dark theme that is less dark, with good defaults and no hours spent adjusting CSS.

- [Direct request for a less-dark theme](https://www.reddit.com/r/ObsidianMD/comments/1xlissp/is_there_a_dark_theme_that_isnt_quite_so_dark/)

The Reddit links come from the preceding idea research and represent qualitative demand, not a market-size estimate or proof that existing themes do not solve the problem. For Pure OLED Rainbow, the additional requirement comes directly from the owner. Other themes and snippets may already address parts of these needs.

## Planned appearance and features

- Use medium charcoal and slate surfaces rather than pure black or very dark blue.
- Use warm off-white body text and restrained blue or amber accents.
- Separate editor, sidebars, menus and dialogs with visible borders and small tonal differences.
- Keep links, selections, search results, inactive tabs and muted text readable.
- Provide useful defaults without requiring a settings plugin; any later tuning should be optional.

## Mode scope

Dark mode is the primary scope. A matching light mode is optional future scope.

## Future implementation and release plan

1. Confirm the final palette and layout against the requirements above.
2. Build the theme only after Rahul authorises implementation. Prefer supported Obsidian CSS variables and keep source readable.
3. Test representative notes, navigation, tabs, properties, menus, settings, search, Canvas and Bases where applicable. Include focus, selection, hover and error states.
4. Run the theme-specific checks below and record the actual Obsidian versions, devices and modes tested.
5. Prepare the root manifest, stylesheet, licence and real screenshots. Decide the first release version and minimum app version from actual testing.
6. Follow the current Obsidian submission guidance when a release is separately authorised. Commit source and screenshots, tag the intended revision, attach matching release assets and verify the published listing.

Keep assets offline, respect font and third-party licences, and avoid required plugins for the core appearance. Do not configure GitHub Actions or automatic deployment.

Official references for later implementation:

- [Build a theme](https://docs.obsidian.md/Themes/App%20themes/Build%20a%20theme)
- [Submit a theme](https://docs.obsidian.md/Themes/App%20themes/Submit%20your%20theme)
- [Developer policies](https://docs.obsidian.md/community-directory/developer-policies)

These milestones were pending when the plan was written. The release and installation links are in the [README](README.md).

## Acceptance checklist for later implementation

- [ ] Compare the result with default dark mode using long notes and small sidebar text.
- [ ] Check text and controls against their actual backgrounds, including disabled, hover and focus states.
- [ ] Confirm the medium-dark background remains consistent in settings and pop-up menus.
- [ ] Confirm every claimed feature has been implemented and tested before replacing the planning-only status.
- [ ] Review screenshots for private information and verify all published documentation and asset paths.
- [ ] Verify the default branch, release revision and uploaded assets before calling any future release complete.

## Original scope

The initial task covered repository creation and this Markdown plan. Theme code, assets and publication were deferred until implementation.
