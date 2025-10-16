# credit_check/utils.py
def luhn_checksum_is_valid(number: str) -> bool:
    """
    Retourne True si number (str) est valide selon Luhn.
    number doit contenir uniquement des chiffres.
    """
    if not number.isdigit():
        return False

    total = 0
    reversed_digits = number[::-1]
    for i, d in enumerate(reversed_digits):
        n = int(d)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0


def card_type(number: str) -> str:
    """
    Retourne 'AMEX', 'MASTERCARD', 'VISA' ou 'INVALID' selon les règles (longueur + préfixe).
    (Ne vérifie pas Luhn — faire luhn_checksum_is_valid séparément.)
    """
    if not number.isdigit():
        return "INVALID"

    length = len(number)
    first_two = int(number[:2]) if length >= 2 else None
    first_one = number[0] if length >= 1 else ''

    if length == 15 and first_two in (34, 37):
        return "AMEX"
    if length == 16 and 51 <= (first_two or 0) <= 55:
        return "MASTERCARD"
    if length in (13, 16) and first_one == '4':
        return "VISA"
    return "INVALID"
