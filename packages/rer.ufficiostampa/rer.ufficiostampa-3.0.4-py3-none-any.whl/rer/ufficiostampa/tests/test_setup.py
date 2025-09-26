"""Setup tests for this package."""

from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from rer.ufficiostampa.testing import (  # noqa: E501
    RER_UFFICIOSTAMPA_INTEGRATION_TESTING,
)

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that rer.ufficiostampa is properly installed."""

    layer = RER_UFFICIOSTAMPA_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if rer.ufficiostampa is installed."""
        if hasattr(self.installer, "is_product_installed"):
            self.assertTrue(self.installer.is_product_installed("rer.ufficiostampa"))
        else:
            self.assertTrue(self.installer.isProductInstalled("rer.ufficiostampa"))

    def test_browserlayer(self):
        """Test that IRerUfficiostampaLayer is registered."""
        from plone.browserlayer import utils
        from rer.ufficiostampa.interfaces import IRerUfficiostampaLayer

        self.assertIn(IRerUfficiostampaLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):
    layer = RER_UFFICIOSTAMPA_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        if hasattr(self.installer, "uninstall_product"):
            self.installer.uninstall_product("rer.ufficiostampa")
        else:
            self.installer.uninstallProducts(["rer.ufficiostampa"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if rer.ufficiostampa is cleanly uninstalled."""
        if hasattr(self.installer, "is_product_installed"):
            self.assertFalse(self.installer.is_product_installed("rer.ufficiostampa"))
        else:
            self.assertFalse(self.installer.isProductInstalled("rer.ufficiostampa"))

    def test_browserlayer_removed(self):
        """Test that IRerUfficiostampaLayer is removed."""
        from plone.browserlayer import utils
        from rer.ufficiostampa.interfaces import IRerUfficiostampaLayer

        self.assertNotIn(IRerUfficiostampaLayer, utils.registered_layers())
