import re

from django.core.exceptions import ValidationError



EMAIL_REGEX = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'


def word_validator(validate_form_field_func):
    def wrapper(self):
        field = validate_form_field_func(self)

        if not (field.isalpha() and field.istitle()):
            raise ValidationError('The word must consist only letters and start with a capital letter!')
        else:
            return field

    return wrapper

def email_validator(validate_form_field_func):
    def wrapper(self):
        field = validate_form_field_func(self)

        regex = re.compile(EMAIL_REGEX)
        if not re.fullmatch(regex, field):
            raise ValidationError('Wrong email!')
        else:
            return field

    return wrapper
