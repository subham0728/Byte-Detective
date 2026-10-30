import unittest

import app


class GameLevelTests(unittest.TestCase):
    def test_has_more_than_three_cute_cases(self):
        self.assertGreater(len(app.CASES), 3)

    def test_case_progress_uses_full_case_count(self):
        self.assertGreaterEqual(len(app.CASES), 5)
        self.assertTrue(all(case["level"] in {"EASY", "MEDIUM", "CHALLENGE"} for case in app.CASES))


if __name__ == "__main__":
    unittest.main()
