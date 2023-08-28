import pytest
from faker import Faker

fake = Faker()
Faker.seed(1369)


@pytest.fixture(name="fake")
def fixture_fake():
    """Pass a seeded Faker instance as a fixture"""
    return fake
