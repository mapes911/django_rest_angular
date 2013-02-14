import factory

from django.contrib.auth.models import User

from .models import Experience, Chapter


class UserFactory(factory.Factory):
    FACTORY_FOR = User
    username = factory.Sequence(lambda n: 'user{0}'.format(n))
    email = factory.Sequence(lambda n: 'person{0}@example.com'.format(n))


class ExperienceFactory(factory.Factory):
    FACTORY_FOR = Experience

    title = factory.Sequence(lambda n: 'Lorem Ipsum {0}'.format(n))
    moral = 'Lorem Ipsum'
    user = factory.SubFactory(UserFactory)


class ChapterFactory(factory.Factory):
    FACTORY_FOR = Chapter

    title = factory.Sequence(lambda n: 'Lorem Ipsum {0}'.format(n))
    body = factory.Sequence(lambda n: 'Lorem Body {0}'.format(n))
    experience = factory.SubFactory(ExperienceFactory)
