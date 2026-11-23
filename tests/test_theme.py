import json
from pathlib import Path
import unittest
from xml.etree import ElementTree

import cssselect2
import tinycss2


ROOT = Path(__file__).resolve().parents[1]
MARKUP = """
<body class="{classes}">
  <div class="workspace-split mod-horizontal">
    <div class="workspace-leaf" />
    <div id="leaf" class="workspace-leaf" />
  </div>
  <div id="ribbon" class="workspace-ribbon" />
  <div class="workspace-leaf-content">
    <button id="workspace-focus" data-focus-visible="" />
  </div>
  <div id="menu" class="menu">
    <button id="menu-focus" data-focus-visible="" />
  </div>
  <div id="modal" class="modal">
    <button id="modal-focus" data-focus-visible="" />
  </div>
  <div class="markdown-rendered"><span id="reading-bullet" class="list-bullet" /></div>
  <div class="markdown-source-view mod-cm6">
    <span id="editor-bullet" class="list-bullet" />
    <div class="cm-contentContainer"><div id="editor" class="cm-content" /></div>
  </div>
</body>
"""


class SoftSlateDarkTests(unittest.TestCase):
    def setUp(self):
        self.stylesheet = (ROOT / "theme.css").read_text(encoding="utf-8")
        self.matcher = cssselect2.Matcher()
        rules = tinycss2.parse_stylesheet(self.stylesheet, skip_comments=True, skip_whitespace=True)
        for rule in rules:
            self.assertEqual(rule.type, "qualified-rule")
            declarations = {}
            for declaration in tinycss2.parse_declaration_list(
                rule.content, skip_comments=True, skip_whitespace=True
            ):
                self.assertEqual(declaration.type, "declaration")
                declarations[declaration.name] = tinycss2.serialize(declaration.value).strip()
            # The selector engine has no keyboard state. Model that state in the fixture.
            selector = tinycss2.serialize(rule.prelude).replace(":focus-visible", "[data-focus-visible]")
            for compiled_selector in cssselect2.compile_selector_list(selector):
                self.matcher.add_selector(compiled_selector, declarations)

    def styles_for(self, classes):
        root = ElementTree.fromstring(MARKUP.format(classes=classes))
        elements = cssselect2.ElementWrapper.from_html_root(root)
        styles = {}
        for element in elements.iter_subtree():
            for _, _, pseudo_element, declarations in self.matcher.match(element):
                styles.setdefault((element.id, pseudo_element), {}).update(declarations)
        return styles

    def test_light_mode_uses_host_styles_on_desktop_and_mobile(self):
        for classes in ("theme-light", "theme-light is-mobile"):
            with self.subTest(classes=classes):
                self.assertEqual(self.styles_for(classes), {})

    def test_dark_mode_keeps_palette_borders_keyboard_focus_and_bullets(self):
        styles = self.styles_for("theme-dark")
        self.assertIn("--background-primary", styles[(None, None)])
        for element in ("leaf", "ribbon", "menu", "modal"):
            with self.subTest(element=element):
                self.assertTrue({"border", "border-color"} & styles[(element, None)].keys())
        for element in ("workspace-focus", "menu-focus", "modal-focus"):
            with self.subTest(element=element):
                self.assertEqual(styles[(element, None)]["outline"], "2px solid var(--text-accent)")
        for element in ("reading-bullet", "editor-bullet"):
            with self.subTest(element=element):
                self.assertEqual(styles[(element, "after")]["background-color"], "var(--text-muted)")

    def test_editor_padding_applies_on_mobile_only(self):
        self.assertNotIn("padding-inline", self.styles_for("theme-dark").get(("editor", None), {}))
        mobile_styles = self.styles_for("theme-dark is-mobile")
        self.assertEqual(mobile_styles[("editor", None)]["padding-inline"], "8px")

    def test_source_version_matches_manifest(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        version = manifest["version"]
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertIn(f"Soft Slate Dark {version}.", self.stylesheet)
        self.assertIn(f"Source version {version}.", (ROOT / "README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
