import tempfile
import unittest
from pathlib import Path

from scripts.install import DESTINATIONS, SOURCE, install


class InstallTests(unittest.TestCase):
    def test_installs_all_tools_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            self.assertEqual(install(project, list(DESTINATIONS)), 0)
            for destination in DESTINATIONS.values():
                for skill in SOURCE.iterdir():
                    self.assertEqual(
                        (project / destination / skill.name / "SKILL.md").read_bytes(),
                        (skill / "SKILL.md").read_bytes(),
                    )
            self.assertEqual(install(project, list(DESTINATIONS)), 0)

    def test_conflict_stops_all_copies_without_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            conflict = project / DESTINATIONS["claude"] / "nuguard-aibom"
            conflict.mkdir(parents=True)
            (conflict / "SKILL.md").write_text("local changes", encoding="utf-8")
            self.assertEqual(install(project, list(DESTINATIONS)), 1)
            self.assertEqual((conflict / "SKILL.md").read_text(), "local changes")
            self.assertFalse((project / DESTINATIONS["codex"]).exists())


if __name__ == "__main__":
    unittest.main()
