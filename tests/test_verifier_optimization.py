"""Optimized Python must still reject changed archive evidence."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class OptimizedVerifierTests(unittest.TestCase):
    def test_changed_evidence_rejects_with_and_without_optimization(self):
        with tempfile.TemporaryDirectory() as directory:
            library = Path(directory) / 'library'
            shutil.copytree(ROOT, library, ignore=shutil.ignore_patterns('__pycache__', '.git'))
            path = next(library.glob('models/*/*/evidence.json'))
            evidence = json.loads(path.read_text())
            evidence['omex_sha256'] = '0' * 64
            path.write_text(json.dumps(evidence))
            for options in ([], ['-O']):
                result = subprocess.run([sys.executable, '-B', *options,
                                         str(library / 'scripts/verify_library.py')],
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
                self.assertIn('Library verification rejected:', result.stderr)


if __name__ == '__main__':
    unittest.main()
