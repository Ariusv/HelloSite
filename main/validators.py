from django.core.exceptions import ValidationError
import re


EMAIL_REGEX = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'


def word_validator(word):
    if not (word.isalpha() and word.istitle()):
        raise ValidationError('The word must consist only letters and start with a capital letter!')
    else:
        pass


def email_validator(email):
    regex = re.compile(EMAIL_REGEX)
    if not re.fullmatch(regex, email):
        raise ValidationError('Wrong email!')
    else:
        pass