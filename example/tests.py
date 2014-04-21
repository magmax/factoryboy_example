from django.test import TestCase

from factory import Factory

import models


class ExampleFactory(Factory):
    FACTORY_FOR = models.Example
    name = "This is an example"


class ExampleTest(TestCase):
    def test_example_build(self):
        ExampleFactory.build()

        self.assertEquals(0, len(models.Example.objects.all()))

    def test_example_create(self):
        ExampleFactory.create()

        self.assertEquals(1, len(models.Example.objects.all()))
