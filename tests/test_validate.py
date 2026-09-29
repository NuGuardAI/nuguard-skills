import re
import unittest
from pathlib import Path

from scripts.validate import ROOT, validate


class ValidateTests(unittest.TestCase):
    def test_package_is_valid(self):
        self.assertEqual(validate(), [])

    def test_stages_do_not_require_an_llm_key(self):
        for name in ("sbom", "analyze"):
            text = (ROOT / "commands" / f"nuguard-{name}.md").read_text(encoding="utf-8")
            self.assertIn("--no-llm", text, name)

    def test_referenced_commands_and_skills_exist(self):
        commands = {p.stem for p in (ROOT / "commands").glob("*.md")}
        skills = {p.name for p in (ROOT / "skills").iterdir()}
        for file in list((ROOT / "commands").glob("*.md")) + list((ROOT / "agents").glob("*.md")):
            text = file.read_text(encoding="utf-8")
            for ref in re.findall(r"`/(nuguard-[a-z]+)", text):
                self.assertIn(ref, commands, f"{file.name}: {ref}")
            for ref in re.findall(r"`(claude-code-llm|[a-z-]+-analysis|ai-security-review)` skill", text):
                self.assertIn(ref, skills, f"{file.name}: {ref}")


if __name__ == "__main__":
    unittest.main()
