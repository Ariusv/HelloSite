from django.core.exceptions import ValidationError


def word_validator(word):
    if not word.isalpha():
        raise ValidationError('the word should consist only letters')
    else:
        pass