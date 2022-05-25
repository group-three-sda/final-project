import factory
from faker import Faker
from django.contrib.auth import get_user_model
from snapvisite.models import Company, Category
profile = get_user_model()
fake = Faker()


"""User Factories"""


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = profile

    email = 'user@test.com'
    user_name = 'nickname'
    first_name = fake.first_name()
    last_name = fake.last_name()
    is_active = True
    is_staff = False
    is_superuser = False
    phone_number = '+48517856890'
    confirm = True
    print("user is created")


class SuperUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = profile

    email = 'superuser@test.com'
    user_name = 'supernickname'
    first_name = fake.first_name()
    last_name = fake.last_name()
    is_active = True
    is_staff = True
    is_superuser = True
    phone_number = '+48670765567'
    confirm = True
    print("Superuser is created")


"""END"""


"""Snapvisite Factories"""


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    category_name = 'category'


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    company_name = 'company'
    description = fake.text()
    owner = factory.SubFactory(UserFactory)

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for category in extracted:
                self.category.add(category)

    phone_number = "+48519874567"
    email = fake.ascii_company_email()

