"""Setup tests for this package."""

from plone.api.portal import set_registry_record
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from rer.ufficiostampa.behaviors.legislature import defaultLegislature
from rer.ufficiostampa.interfaces import IRerUfficiostampaSettings
from rer.ufficiostampa.testing import RER_UFFICIOSTAMPA_INTEGRATION_TESTING
from transaction import commit

import json
import unittest


class TestUtils(unittest.TestCase):
    """"""

    layer = RER_UFFICIOSTAMPA_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

        legislatures = [
            {"legislature": "First", "arguments": ["foo", "bar"]},
            {"legislature": "Second", "arguments": ["foo2", "bar2"]},
        ]
        set_registry_record(
            "legislatures",
            json.dumps(legislatures),
            interface=IRerUfficiostampaSettings,
        )
        commit()

    def test_defaultLegislature_returns_last_one(self):
        self.assertEqual(defaultLegislature(), "Second")
