# Soft Slate Dark desktop UI test

Tested 24 November 2026 on Windows in Obsidian Desktop 1.15.1, the version declared as the minimum in the theme manifest. Obsidian loaded Soft Slate Dark 3.7.2 from an isolated sample vault. The vault contained five synthetic files. Community plugins and account actions were outside this run.

## Fix and retest

The enabled Editor settings switches in 3.7.1 used a white thumb against the light blue track. The contrast between the thumb and track was 1.57:1 in the running app. Version 3.7.2 uses the charcoal accent foreground for the enabled thumb, where the same switch measured 9.44:1. The disabled switch measured 4.69:1. Turning the switch off and on restored its state and appearance. The light-mode comparison confirmed that the enabled switch still uses the native styling in that mode.

| Switch state | Track | Thumb before | Thumb after | Contrast before | Contrast after |
| --- | --- | --- | --- | --- | --- |
| Enabled | `#abd2ff` | `#ffffff` | `#232831` | 1.57:1 | 9.44:1 |
| Disabled | `#66758a` | `#ffffff` | `#ffffff` | 4.69:1 | 4.69:1 |

Contrast was calculated from the rendered track and thumb colors in the live Settings window.

## Results

All 20 desktop UI checks and five source tests passed.

| Check | Verified behavior |
| --- | --- |
| Theme loading | The Desktop 1.15.1 title, loaded stylesheet version and charcoal background matched the selected theme in the sample vault. |
| Reading mode | Warm text, properties, headings, four callouts and a table rendered. |
| Reading content and disclosure | A callout expanded and collapsed. Syntax highlighting, marked text, math and internal and external links rendered. |
| Live Preview | The reading view control opened editing. Live Preview displayed an editable note, properties and rendered callouts. |
| Source Mode | The command palette switched editing modes. A typed change appeared in the note and keyboard undo removed it. |
| Tasks, bullets and headings | A reading-view checkbox saved and restored its state. Checked marks and list bullets used the theme colors. Six heading levels rendered. |
| Tabs, Files and linked notes | Multiple note tabs, the Files view and the ribbon border rendered. An internal note link opened its target. |
| Search | The query returned both matching samples and an unmatched query displayed the empty state. |
| Bases | The study table displayed three notes and their text and boolean fields. |
| Canvas | Three cards and two connections loaded. Zoom to fit displayed the board. |
| Note menu | Its border and commands rendered. Escape dismissed it. |
| Quick switcher | Typing filtered the choices and Enter opened the highlighted note. |
| Keyboard focus | The visible Search field showed a 2 px blue focus outline. |
| Sidebar | The left sidebar collapsed and expanded through its visible control. |
| Graph | The graph canvas and its controls loaded. |
| Appearance settings | The base color scheme and the installed Soft Slate Dark theme matched the selected state. |
| Editor settings switches | The enabled and disabled states met the measured contrasts above. Toggling restored both state and style. |
| Other settings pages | General, Interface, Files and links, Hotkeys, Core plugins, Community plugins, Backlinks, Canvas, Command palette, Page preview and Quick switcher displayed their controls with the dark palette. |
| Light fallback | The sampled palette and enabled switch matched Obsidian's default Light with Soft Slate Dark selected. |
| System mode | Adapt to system followed the host's light preference. Selecting Dark restored the theme palette. |

The scope was Windows desktop with the installed core app views and synthetic data. Mobile, other desktop platforms, the system-dark branch of automatic mode and third-party plugin views were outside the test. The five source tests were run with `python -B -m unittest discover -s tests`.

## Screenshots

These ten captures are from the running application with the updated theme. The workspace captures are 1024 × 800 and the Settings capture is 900 × 700.

1. [Reading view with properties and callouts](screens/01-reading-properties.png)
2. [Live Preview with editor focus](screens/02-live-preview.png)
3. [Source Mode with front matter and Markdown](screens/03-source-mode.png)
4. [Reading view with a nested checklist](screens/04-checklist.png)
5. [Vault search results](screens/05-search-results.png)
6. [Bases table](screens/06-bases-table.png)
7. [Canvas board](screens/07-canvas-board.png)
8. [Note options menu](screens/08-note-menu.png)
9. [Quick switcher with a filtered result](screens/09-quick-switcher.png)
10. [Editor settings with both switch states](screens/10-editor-settings.png)
