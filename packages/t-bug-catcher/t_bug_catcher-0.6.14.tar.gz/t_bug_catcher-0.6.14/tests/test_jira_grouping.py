import unittest
from unittest.mock import MagicMock, patch

from t_bug_catcher.jira import Jira


class TestJiraGrouping(unittest.TestCase):
    """Tests for Jira ADF parsing and ticket grouping logic."""

    def setUp(self):
        """Set up the test environment."""
        self.jira = Jira()

    def test_adf_to_text_extracts_error_id(self):
        """Ensure ADF parser extracts plain text including the error id token."""
        error_id = "abc123"
        adf = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {"type": "text", "text": "Error string ID: "},
                        {"type": "text", "text": error_id, "marks": [{"type": "em"}]},
                    ],
                }
            ],
        }

        text = Jira._adf_to_text(adf)
        self.assertIn(f"Error string ID: {error_id}", text)

    def test_filter_tickets_matches_adf_description(self):
        """filter_tickets should find a ticket when the error id is embedded in ADF description."""
        error_id = "abc123"
        ticket = {
            "id": "10001",
            "key": "TEST-1",
            "fields": {
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {"type": "text", "text": f"Error string ID: {error_id}"},
                            ],
                        }
                    ],
                }
            },
        }

        matched = self.jira.filter_tickets(all_tickets=[ticket], error_id=error_id)
        self.assertIsNotNone(matched)
        self.assertEqual(matched["key"], "TEST-1")

    @patch.object(Jira, "_Jira__update_existing_ticket")
    @patch.object(Jira, "_Jira__create_new_ticket")
    @patch.object(Jira, "get_issues")
    @patch.object(Jira, "_Jira__generate_error_id")
    def test_report_error_groups_updates_existing(self, mock_gen_id, mock_get_issues, mock_create, mock_update):
        """report_error should create once, then update existing when the same error is reported again."""
        fixed_id = "deadbeef"
        mock_gen_id.return_value = fixed_id

        # First call: no issues present -> should create
        # Second call: an issue present with matching error id in ADF -> should update
        adf_issue = {
            "id": "10002",
            "key": "TEST-2",
            "fields": {
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {"type": "text", "text": f"Error string ID: {fixed_id}"},
                            ],
                        }
                    ],
                }
            },
        }
        mock_get_issues.side_effect = [
            {"issues": []},
            {"issues": [adf_issue]},
        ]

        # Prevent any network side effects
        mock_create.return_value = MagicMock(status_code=201, json=lambda: {"key": "TEST-NEW", "id": "10010"})
        mock_update.return_value = None

        # Raise and catch the same exception twice to keep traceback and ids deterministic
        for call_idx in range(2):
            try:
                d = {"a": 1}
                _ = d["missing"]
            except Exception as ex:
                self.jira.report_error(exception=ex)

        # Should create once and then update once
        self.assertEqual(mock_create.call_count, 1)
        self.assertEqual(mock_update.call_count, 1)


if __name__ == "__main__":
    unittest.main()
