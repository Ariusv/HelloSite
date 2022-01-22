from main.models import Person


def get_person_fields(start_index=1, end_index=None):
    return Person._meta.fields[start_index:end_index]

def get_person_names_count(person):
    return Person.objects.filter(name=person.name).count()