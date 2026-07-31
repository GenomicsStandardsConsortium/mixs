"""Authentication for the GitHub API calls the release comparison makes.

The comparison fetches tags and trees from the GitHub API. Unauthenticated, that
is 60 requests per hour shared across GitHub's runner IP addresses, which is not
enough to finish, so a release that falls back to it fails on a rate limit.

That is not hypothetical. The v7.0.1 release run failed this way on 2026-07-31
because the token check demanded ``ghs_`` followed by exactly 36 characters and
the token GitHub Actions issues no longer matches, so a valid token was discarded
and the fallback was silent. The v7.0.0 run had the same fallback and survived
only because the shared budget was not yet used up.

These tests exist so that cannot regress unnoticed.
"""
import importlib.util
import logging
import os
import unittest
from unittest.mock import patch

ROOT = os.path.join(os.path.dirname(__file__), '..')
SCRIPT = os.path.join(ROOT, "src", "scripts", "diff_two_linkml_mixs_releases.py")


def load_module():
    """A fresh copy, so the once-per-run message flag starts unset."""
    spec = importlib.util.spec_from_file_location("diff_releases_auth", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # The module falls back to reading local/.env, which would make these tests
    # depend on whether the person running them happens to have a token there.
    module.load_dotenv = lambda *args, **kwargs: None
    return module


class TestTokenIsNotFormatChecked(unittest.TestCase):
    """A token is opaque. Only obviously unusable values are rejected."""

    def setUp(self):
        self.module = load_module()

    def test_tokens_github_issues_are_accepted(self):
        for token, description in [
            ("ghs_" + "a" * 36, "the Actions token as it used to be"),
            ("ghs_" + "a" * 40, "a longer Actions token, which the old check rejected"),
            ("ghp_" + "b" * 36, "a classic personal access token"),
            ("github_pat_" + "c" * 60, "a fine-grained personal access token"),
            ("some_future_prefix_" + "d" * 20, "a format GitHub has not invented yet"),
        ]:
            with self.subTest(description):
                self.assertTrue(
                    self.module.validate_github_token(token),
                    f"{description} must be accepted. Rejecting a usable token sends "
                    f"the comparison to the unauthenticated API, where it fails on a "
                    f"rate limit.",
                )

    def test_obviously_unusable_values_are_rejected(self):
        for token, description in [
            ("", "empty"),
            ("   ", "whitespace only"),
            ("ghs_abc def", "containing a space"),
            ("ghs_abc\ndef", "containing a newline"),
        ]:
            with self.subTest(description):
                self.assertFalse(self.module.validate_github_token(token), description)


class TestOneMessagePerRun(unittest.TestCase):
    """get_github_headers is called from several places; it must not repeat itself."""

    def collect(self, env):
        """Return (headers, log lines) after calling get_github_headers four times."""
        module = load_module()
        records = []

        class Capture(logging.Handler):
            def emit(self, record):
                records.append((record.levelname, record.getMessage()))

        module.logger.handlers = [Capture()]
        module.logger.setLevel(logging.DEBUG)
        module.logger.propagate = False

        with patch.dict(os.environ, env, clear=True):
            for _ in range(4):
                headers = module.get_github_headers()
        return headers, records

    def test_authenticated(self):
        headers, records = self.collect({"GITHUB_TOKEN": "ghs_" + "a" * 40})
        self.assertIn("Authorization", headers, "a usable token must be sent")
        self.assertEqual(len(records), 1, f"expected one message, got {records}")
        self.assertEqual(records[0][0], "INFO")

    def test_unauthenticated_in_github_actions_is_an_error(self):
        headers, records = self.collect({"GITHUB_ACTIONS": "true"})
        self.assertEqual(headers, {})
        self.assertEqual(len(records), 1, f"expected one message, got {records}")
        self.assertEqual(
            records[0][0],
            "ERROR",
            "In Actions an unauthenticated run is not degraded, it fails as soon as "
            "the shared rate limit is used up, so it must not be reported as a warning.",
        )

    def test_unauthenticated_locally_is_a_warning(self):
        headers, records = self.collect({})
        self.assertEqual(headers, {})
        self.assertEqual(len(records), 1, f"expected one message, got {records}")
        self.assertEqual(records[0][0], "WARNING")


if __name__ == "__main__":
    unittest.main()
