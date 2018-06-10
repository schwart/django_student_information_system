from django.test import TestCase
from class_groups.models import (
    ClassGroup,
    School,
    Year
)
from class_groups.factories import (
    ClassGroupFactory,
    SchoolFactory,
    YearFactory
)

# Create your tests here.
class ClassTestCase(TestCase):
    def test_class_creation(self):
        class_group = ClassGroupFactory()
        class_group_db = ClassGroup.objects.get(
            pk=class_group.pk
        )

        self.assertEqual(class_group_db.year, class_group.year)
        self.assertEqual(class_group_db.band, class_group.band)
        self.assertEqual(class_group_db.set, class_group.set)

class SubjectTestCase(TestCase):
    def test_subject_creation(self):
        pass

class SchoolTestCase(TestCase):
    def setUp(self):
        self.school = SchoolFactory()
    def test_school_creation(self):
        school = School.objects.get(pk=self.school.pk)

        self.assertEqual(
            school.name,
            self.school.name
        )

class YearTestCase(TestCase):
    def setUp(self):
        self.year = YearFactory()

    def test_year_creation(self):
        year = Year.objects.get(pk=self.year.pk)

        self.assertEqual(
            year.value,
            self.year.value
        )

        self.assertEqual(
            year.school.name,
            self.year.school.name
        )

