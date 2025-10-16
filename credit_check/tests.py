from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .utils import luhn_checksum_is_valid, card_type

class UtilsTest(TestCase):
    def test_luhn_valid(self):
        assert luhn_checksum_is_valid("4003600000000014")  # exemple VISA
        assert luhn_checksum_is_valid("378282246310005")   # AMEX

    def test_luhn_invalid(self):
        assert not luhn_checksum_is_valid("1234567890")

    def test_card_type(self):
        assert card_type("378282246310005") == "AMEX"
        assert card_type("5555555555554444") == "MASTERCARD"
        assert card_type("4111111111111111") == "VISA"
        assert card_type("1234567890") == "INVALID"
