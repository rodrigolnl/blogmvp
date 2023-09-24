import factory
from factory.django import DjangoModelFactory
from user_api.models import User, UserManager


class UserManagerFactory(DjangoModelFactory):

    class Meta:
        model = UserManager

    def create(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user


class UserFactory(DjangoModelFactory):
    email = factory.Faker("email")
    username = factory.Faker('first_name')
    is_active = True

    objects = UserManagerFactory()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    class Meta:
        model = User