"""Tests for app_reputation_probe. Fixtures synthetic — no network, no PII."""

from app_reputation_probe import flatten_permissions, play_record

APP = {
    "title": "Junk Cleaner Pro",
    "developer": "Acme Labs",
    "developerId": "Acme+Labs",
    "developerEmail": "acme@example.com",
    "developerWebsite": "https://example.com",
    "genre": "Tools",
    "installs": "1,000+",
    "minInstalls": 1000,
    "score": 4.1,
    "ratings": 37,
    "contentRating": "Everyone",
    "released": "Jan 2, 2026",
    "lastUpdatedOn": "Feb 9, 2026",
    "adSupported": True,
    "containsAds": True,
    "description": "ignored — not a selected field",
}

PERMS = {
    "Other": ["full network access", "view network connections"],
    "Phone": ["read phone status and identity"],
    "duplicate-group": ["full network access"],
}


class DescribeFlattenPermissions:
    def it_flattens_groups_to_a_sorted_unique_list(self):
        assert flatten_permissions(PERMS) == [
            "full network access",
            "read phone status and identity",
            "view network connections",
        ]

    def it_passes_none_through(self):
        assert flatten_permissions(None) is None


class DescribePlayRecord:
    def it_selects_identity_and_scope_fields_snake_cased(self):
        assert play_record("com.acme.clean", APP, PERMS) == {
            "package": "com.acme.clean",
            "found": True,
            "title": "Junk Cleaner Pro",
            "developer": "Acme Labs",
            "developer_id": "Acme+Labs",
            "developer_email": "acme@example.com",
            "developer_website": "https://example.com",
            "genre": "Tools",
            "installs": "1,000+",
            "min_installs": 1000,
            "score": 4.1,
            "ratings": 37,
            "content_rating": "Everyone",
            "released": "Jan 2, 2026",
            "last_updated_on": "Feb 9, 2026",
            "ad_supported": True,
            "contains_ads": True,
            "permissions": [
                "full network access",
                "read phone status and identity",
                "view network connections",
            ],
        }

    def it_drops_unselected_fields_like_description(self):
        assert "description" not in play_record("x", APP, PERMS)

    class WhenPlayHasNoListing:
        def it_marks_found_false_with_no_other_fields(self):
            assert play_record("com.gone.app", None, None) == {
                "package": "com.gone.app",
                "found": False,
            }
