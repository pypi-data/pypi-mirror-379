import io
import os
import sys
import types
from pathlib import Path
from unittest.mock import patch, MagicMock, call

import pytest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django

django.setup()

from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site

from pages.models import Application, Module
from nodes.models import Node, NodeRole

from core.models import RFID
from ocpp.rfid.reader import read_rfid, enable_deep_read
from ocpp.rfid.detect import detect_scanner, main as detect_main
from ocpp.rfid import background_reader
from ocpp.rfid.constants import (
    DEFAULT_IRQ_PIN,
    DEFAULT_RST_PIN,
    GPIO_PIN_MODE_BCM,
    MODULE_WIRING,
    SPI_BUS,
    SPI_DEVICE,
)


pytestmark = [pytest.mark.feature("rfid-scanner")]


class BackgroundReaderConfigurationTests(SimpleTestCase):
    def setUp(self):
        background_reader._auto_detect_logged = False

    def tearDown(self):
        background_reader._auto_detect_logged = False

    def test_is_configured_auto_detects_without_lock(self):
        fake_lock = Path("/tmp/rfid-auto-detect.lock")
        with (
            patch("ocpp.rfid.background_reader._lock_path", return_value=fake_lock),
            patch("ocpp.rfid.background_reader._has_spi_device", return_value=True),
            patch(
                "ocpp.rfid.background_reader._dependencies_available",
                return_value=True,
            ),
        ):
            self.assertTrue(background_reader.is_configured())

    def test_is_configured_requires_dependencies(self):
        fake_lock = Path("/tmp/rfid-auto-detect.lock")
        with (
            patch("ocpp.rfid.background_reader._lock_path", return_value=fake_lock),
            patch("ocpp.rfid.background_reader._has_spi_device", return_value=True),
            patch(
                "ocpp.rfid.background_reader._dependencies_available",
                return_value=False,
            ),
        ):
            self.assertFalse(background_reader.is_configured())


class ScanNextViewTests(TestCase):
    @patch("config.middleware.Node.get_local", return_value=None)
    @patch("config.middleware.get_site")
    @patch(
        "ocpp.rfid.views.scan_sources",
        return_value={
            "rfid": "ABCD1234",
            "label_id": 1,
            "created": False,
            "kind": RFID.CLASSIC,
        },
    )
    def test_scan_next_success(self, mock_scan, mock_site, mock_node):
        resp = self.client.get(reverse("rfid-scan-next"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.json(),
            {
                "rfid": "ABCD1234",
                "label_id": 1,
                "created": False,
                "kind": RFID.CLASSIC,
            },
        )

    @patch("config.middleware.Node.get_local", return_value=None)
    @patch("config.middleware.get_site")
    @patch("ocpp.rfid.views.scan_sources", return_value={"error": "boom"})
    def test_scan_next_error(self, mock_scan, mock_site, mock_node):
        resp = self.client.get(reverse("rfid-scan-next"))
        self.assertEqual(resp.status_code, 500)
        self.assertEqual(resp.json(), {"error": "boom"})


class ReaderNotificationTests(TestCase):
    def _mock_reader(self):
        class MockReader:
            MI_OK = 1
            PICC_REQIDL = 0

            def MFRC522_Request(self, _):
                return (self.MI_OK, None)

            def MFRC522_Anticoll(self):
                return (self.MI_OK, [0xAB, 0xCD, 0x12, 0x34, 0x56])

            def MFRC522_SelectTag(self, _uid):
                self.select_called = True
                return self.MI_OK

            def MFRC522_StopCrypto1(self):
                self.stop_called = True

        return MockReader()

    @patch("ocpp.rfid.reader.notify_async")
    @patch("core.models.RFID.objects.get_or_create")
    def test_notify_on_allowed_tag(self, mock_get, mock_notify):
        reference = MagicMock(value="https://example.com")
        tag = MagicMock(
            label_id=1,
            pk=1,
            allowed=True,
            color="B",
            released=False,
            reference=reference,
        )
        mock_get.return_value = (tag, False)

        reader = self._mock_reader()
        result = read_rfid(mfrc=reader, cleanup=False)
        self.assertEqual(result["label_id"], 1)
        self.assertEqual(result["kind"], RFID.CLASSIC)
        self.assertEqual(result["reference"], "https://example.com")
        self.assertEqual(mock_notify.call_count, 1)
        mock_notify.assert_has_calls([call("RFID 1 OK", f"{result['rfid']} B")])
        self.assertTrue(getattr(reader, "select_called", False))
        self.assertTrue(getattr(reader, "stop_called", False))

    @patch("ocpp.rfid.reader.notify_async")
    @patch("core.models.RFID.objects.get_or_create")
    def test_notify_on_disallowed_tag(self, mock_get, mock_notify):
        tag = MagicMock(
            label_id=2,
            pk=2,
            allowed=False,
            color="B",
            released=False,
            reference=None,
        )
        mock_get.return_value = (tag, False)

        reader = self._mock_reader()
        result = read_rfid(mfrc=reader, cleanup=False)
        self.assertEqual(result["kind"], RFID.CLASSIC)
        self.assertEqual(mock_notify.call_count, 1)
        mock_notify.assert_has_calls([call("RFID 2 BAD", f"{result['rfid']} B")])
        self.assertTrue(getattr(reader, "select_called", False))
        self.assertTrue(getattr(reader, "stop_called", False))


class CardTypeDetectionTests(TestCase):
    def _mock_ntag_reader(self):
        class MockReader:
            MI_OK = 1
            PICC_REQIDL = 0

            def MFRC522_Request(self, _):
                return (self.MI_OK, None)

            def MFRC522_Anticoll(self):
                return (
                    self.MI_OK,
                    [0x04, 0xD3, 0x2A, 0x1B, 0x5F, 0x23, 0x19],
                )

            def MFRC522_SelectTag(self, _uid):
                self.select_called = True
                return self.MI_OK

            def MFRC522_StopCrypto1(self):
                self.stop_called = True

        return MockReader()

    @patch("ocpp.rfid.reader.notify_async")
    @patch("core.models.RFID.objects.get_or_create")
    def test_detects_ntag215(self, mock_get, _mock_notify):
        tag = MagicMock(
            pk=1,
            label_id=1,
            allowed=True,
            color="B",
            released=False,
            reference=None,
            kind=RFID.NTAG215,
        )
        mock_get.return_value = (tag, True)
        reader = self._mock_ntag_reader()
        result = read_rfid(mfrc=reader, cleanup=False)
        self.assertEqual(result["kind"], RFID.NTAG215)
        self.assertTrue(getattr(reader, "select_called", False))
        self.assertTrue(getattr(reader, "stop_called", False))


class RFIDLastSeenTests(TestCase):
    def _mock_reader(self):
        class MockReader:
            MI_OK = 1
            PICC_REQIDL = 0

            def MFRC522_Request(self, _):
                return (self.MI_OK, None)

            def MFRC522_Anticoll(self):
                return (self.MI_OK, [0xAB, 0xCD, 0x12, 0x34])

            def MFRC522_SelectTag(self, _uid):
                self.select_called = True
                return self.MI_OK

            def MFRC522_StopCrypto1(self):
                self.stop_called = True

        return MockReader()

    @patch("ocpp.rfid.reader.notify_async")
    def test_last_seen_updated_on_read(self, _mock_notify):
        tag = RFID.objects.create(rfid="ABCD1234")
        reader = self._mock_reader()
        result = read_rfid(mfrc=reader, cleanup=False)
        tag.refresh_from_db()
        self.assertIsNotNone(tag.last_seen_on)
        self.assertEqual(result["kind"], RFID.CLASSIC)
        self.assertTrue(getattr(reader, "select_called", False))
        self.assertTrue(getattr(reader, "stop_called", False))


class RFIDDetectionScriptTests(SimpleTestCase):
    @patch("ocpp.rfid.detect._ensure_django")
    @patch(
        "ocpp.rfid.irq_wiring_check.check_irq_pin",
        return_value={"irq_pin": DEFAULT_IRQ_PIN},
    )
    def test_detect_scanner_success(self, mock_check, _mock_setup):
        result = detect_scanner()
        self.assertEqual(
            result,
            {
                "detected": True,
                "irq_pin": DEFAULT_IRQ_PIN,
            },
        )
        mock_check.assert_called_once()

    @patch("ocpp.rfid.detect._ensure_django")
    @patch(
        "ocpp.rfid.irq_wiring_check.check_irq_pin",
        return_value={"error": "no scanner detected"},
    )
    def test_detect_scanner_failure(self, mock_check, _mock_setup):
        result = detect_scanner()
        self.assertFalse(result["detected"])
        self.assertEqual(result["reason"], "no scanner detected")
        mock_check.assert_called_once()

    @patch(
        "ocpp.rfid.detect.detect_scanner",
        return_value={"detected": True, "irq_pin": DEFAULT_IRQ_PIN},
    )
    def test_detect_main_success_output(self, mock_detect):
        buffer = io.StringIO()
        with patch("sys.stdout", new=buffer):
            exit_code = detect_main([])
        self.assertEqual(exit_code, 0)
        self.assertIn("IRQ pin", buffer.getvalue())
        mock_detect.assert_called_once()

    @patch(
        "ocpp.rfid.detect.detect_scanner",
        return_value={"detected": False, "reason": "missing hardware"},
    )
    def test_detect_main_failure_output(self, mock_detect):
        buffer = io.StringIO()
        with patch("sys.stdout", new=buffer):
            exit_code = detect_main([])
        self.assertEqual(exit_code, 1)
        self.assertIn("missing hardware", buffer.getvalue())
        mock_detect.assert_called_once()


class RestartViewTests(SimpleTestCase):
    @patch("config.middleware.Node.get_local", return_value=None)
    @patch("config.middleware.get_site")
    @patch("ocpp.rfid.views.restart_sources", return_value={"status": "restarted"})
    def test_restart_endpoint(self, mock_restart, mock_site, mock_node):
        resp = self.client.post(reverse("rfid-scan-restart"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {"status": "restarted"})
        mock_restart.assert_called_once()


class ScanTestViewTests(SimpleTestCase):
    @patch("config.middleware.Node.get_local", return_value=None)
    @patch("config.middleware.get_site")
    @patch("ocpp.rfid.views.test_sources", return_value={"irq_pin": 7})
    def test_scan_test_success(self, mock_test, mock_site, mock_node):
        resp = self.client.get(reverse("rfid-scan-test"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {"irq_pin": 7})

    @patch("config.middleware.Node.get_local", return_value=None)
    @patch("config.middleware.get_site")
    @patch(
        "ocpp.rfid.views.test_sources",
        return_value={"error": "no scanner detected"},
    )
    def test_scan_test_error(self, mock_test, mock_site, mock_node):
        resp = self.client.get(reverse("rfid-scan-test"))
        self.assertEqual(resp.status_code, 500)
        self.assertEqual(resp.json(), {"error": "no scanner detected"})


class RFIDLandingTests(TestCase):
    def test_scanner_view_registered_as_landing(self):
        role, _ = NodeRole.objects.get_or_create(name="Terminal")
        Node.objects.update_or_create(
            mac_address=Node.get_current_mac(),
            defaults={"hostname": "localhost", "address": "127.0.0.1", "role": role},
        )
        Site.objects.update_or_create(
            id=1, defaults={"domain": "testserver", "name": ""}
        )
        app = Application.objects.create(name="Ocpp")
        module = Module.objects.create(node_role=role, application=app, path="/ocpp/")
        module.create_landings()
        self.assertTrue(module.landings.filter(path="/ocpp/rfid/").exists())


class ScannerTemplateTests(TestCase):
    def setUp(self):
        self.url = reverse("rfid-reader")

    def test_configure_link_for_staff(self):
        User = get_user_model()
        staff = User.objects.create_user("staff", password="pwd", is_staff=True)
        self.client.force_login(staff)
        resp = self.client.get(self.url)
        self.assertContains(resp, 'id="rfid-configure"')

    def test_no_link_for_anonymous(self):
        resp = self.client.get(self.url)
        self.assertNotContains(resp, 'id="rfid-configure"')

    def test_advanced_fields_for_staff(self):
        User = get_user_model()
        staff = User.objects.create_user("staff2", password="pwd", is_staff=True)
        self.client.force_login(staff)
        resp = self.client.get(self.url)
        self.assertContains(resp, 'id="rfid-kind"')
        self.assertContains(resp, 'id="rfid-rfid"')
        self.assertContains(resp, 'id="rfid-released"')
        self.assertContains(resp, 'id="rfid-reference"')

    def test_basic_fields_for_public(self):
        resp = self.client.get(self.url)
        self.assertContains(resp, 'id="rfid-kind"')
        self.assertNotContains(resp, 'id="rfid-rfid"')
        self.assertNotContains(resp, 'id="rfid-released"')
        self.assertNotContains(resp, 'id="rfid-reference"')

    def test_deep_read_button_for_staff(self):
        User = get_user_model()
        staff = User.objects.create_user("staff3", password="pwd", is_staff=True)
        self.client.force_login(staff)
        resp = self.client.get(self.url)
        self.assertContains(resp, 'id="rfid-deep-read"')

    def test_no_deep_read_button_for_public(self):
        resp = self.client.get(self.url)
        self.assertNotContains(resp, 'id="rfid-deep-read"')


class ReaderPollingTests(SimpleTestCase):
    def _mock_reader_no_tag(self):
        class MockReader:
            MI_OK = 1
            PICC_REQIDL = 0

            def MFRC522_Request(self, _):
                return (0, None)

        return MockReader()

    @patch("ocpp.rfid.reader.time.sleep")
    def test_poll_interval_used(self, mock_sleep):
        read_rfid(
            mfrc=self._mock_reader_no_tag(),
            cleanup=False,
            timeout=0.002,
            poll_interval=0.001,
        )
        mock_sleep.assert_called_with(0.001)

    @patch("ocpp.rfid.reader.time.sleep")
    def test_use_irq_skips_sleep(self, mock_sleep):
        read_rfid(
            mfrc=self._mock_reader_no_tag(),
            cleanup=False,
            timeout=0.002,
            use_irq=True,
        )
        mock_sleep.assert_not_called()


class DeepReadViewTests(TestCase):
    @patch("config.middleware.Node.get_local", return_value=None)
    @patch("config.middleware.get_site")
    @patch(
        "ocpp.rfid.views.enable_deep_read_mode",
        return_value={"status": "deep", "timeout": 60},
    )
    def test_enable_deep_read(self, mock_enable, mock_site, mock_node):
        User = get_user_model()
        staff = User.objects.create_user("staff4", password="pwd", is_staff=True)
        self.client.force_login(staff)
        resp = self.client.post(reverse("rfid-scan-deep"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {"status": "deep", "timeout": 60})
        mock_enable.assert_called_once()

    def test_forbidden_for_anonymous(self):
        resp = self.client.post(reverse("rfid-scan-deep"))
        self.assertNotEqual(resp.status_code, 200)


class DeepReadAuthTests(TestCase):
    class MockReader:
        MI_OK = 1
        MI_ERR = 2
        PICC_REQIDL = 0
        PICC_AUTHENT1A = 0x60
        PICC_AUTHENT1B = 0x61

        def __init__(self):
            self.auth_calls = []

        def MFRC522_Request(self, _):
            return (self.MI_OK, None)

        def MFRC522_Anticoll(self):
            return (self.MI_OK, [0xAA, 0xBB, 0xCC, 0xDD, 0xEE])

        def MFRC522_Auth(self, mode, block, key, uid):
            self.auth_calls.append(mode)
            return self.MI_ERR if mode == self.PICC_AUTHENT1A else self.MI_OK

        def MFRC522_Read(self, block):
            return (self.MI_OK, [0] * 16)

    @patch("core.notifications.notify_async")
    @patch("core.models.RFID.objects.get_or_create")
    def test_auth_tries_key_a_then_b(self, mock_get, mock_notify):
        tag = MagicMock(
            label_id=1,
            pk=1,
            allowed=True,
            color="B",
            released=False,
            reference=None,
        )
        mock_get.return_value = (tag, False)
        reader = self.MockReader()
        enable_deep_read(60)
        read_rfid(mfrc=reader, cleanup=False)
        self.assertGreaterEqual(len(reader.auth_calls), 2)
        self.assertEqual(reader.auth_calls[0], reader.PICC_AUTHENT1A)
        self.assertEqual(reader.auth_calls[1], reader.PICC_AUTHENT1B)


class RFIDWiringConfigTests(SimpleTestCase):
    def test_module_wiring_map(self):
        expected = [
            ("SDA", "CE0"),
            ("SCK", "SCLK"),
            ("MOSI", "MOSI"),
            ("MISO", "MISO"),
            ("IRQ", "IO4"),
            ("GND", "GND"),
            ("RST", "IO25"),
            ("3v3", "3v3"),
        ]
        self.assertEqual(list(MODULE_WIRING.items()), expected)
        self.assertEqual(DEFAULT_IRQ_PIN, 4)
        self.assertEqual(DEFAULT_RST_PIN, 25)

    def test_background_reader_uses_default_irq_pin(self):
        self.assertEqual(background_reader.IRQ_PIN, DEFAULT_IRQ_PIN)

    def test_reader_instantiation_uses_configured_pins(self):
        class DummyReader:
            init_args = None
            init_kwargs = None

            def __init__(self, *args, **kwargs):
                DummyReader.init_args = args
                DummyReader.init_kwargs = kwargs
                self.MI_OK = 1
                self.PICC_REQIDL = 0

        fake_mfrc = types.ModuleType("mfrc522")
        fake_mfrc.MFRC522 = DummyReader
        fake_gpio = types.ModuleType("RPi.GPIO")
        fake_rpi = types.ModuleType("RPi")
        fake_rpi.GPIO = fake_gpio

        with patch.dict(
            "sys.modules",
            {"mfrc522": fake_mfrc, "RPi": fake_rpi, "RPi.GPIO": fake_gpio},
        ):
            result = read_rfid(timeout=0, cleanup=False)

        self.assertEqual(result, {"rfid": None, "label_id": None})
        self.assertIsNotNone(DummyReader.init_kwargs)
        self.assertEqual(DummyReader.init_kwargs["bus"], SPI_BUS)
        self.assertEqual(DummyReader.init_kwargs["device"], SPI_DEVICE)
        self.assertEqual(DummyReader.init_kwargs["pin_mode"], GPIO_PIN_MODE_BCM)
        self.assertEqual(DummyReader.init_kwargs["pin_rst"], DEFAULT_RST_PIN)
