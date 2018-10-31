from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Mineral

class MineralModelTests(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name="Greigite",
            image_filename="greigite.jpg",
            image_caption = "Greigite structure, SFe4 tetrahedra",
            category = "SulfideThiospinel groupSpinel structural group",
            formula = "Fe<sub>2</sub>+Fe<sub>3</sub>+<sub>2</sub>S<sub>4</sub>",
            strunz_classification = "02.DA.05",
            color = "Pale pink, tarnishes to metallic blue-black",
            crystal_system = "Cubic",
            unit_cell = "a = 9.876 Å; Z = 8",
            crystal_symmetry = "Isometric hexoctahedralH-M symbol: (4/m32/m)Space group: F d3m",
            cleavage = None,
            mohs_scale_hardness = "4 to 4.5",
            luster = "Metallic to earthy",
            streak = None,
            diaphaneity = "Opaque",
            optical_properties = None,
            refractive_index = None,
            crystal_habit = "Spheres of intergrown octahedra and as disseminated microscopic grains",
            specific_gravity = "4.049",
            group = "Sulfides",
        )
        now = timezone.now()
        self.assertLess(mineral.created_at, now)


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Greigite",
            image_filename="greigite.jpg",
            image_caption="Greigite structure, SFe4 tetrahedra",
            category="SulfideThiospinel groupSpinel structural group",
            formula="Fe<sub>2</sub>+Fe<sub>3</sub>+<sub>2</sub>S<sub>4</sub>",
            strunz_classification="02.DA.05",
            color="Pale pink, tarnishes to metallic blue-black",
            crystal_system="Cubic",
            unit_cell="a = 9.876 Å; Z = 8",
            crystal_symmetry="Isometric hexoctahedralH-M symbol: (4/m32/m)Space group: F d3m",
            cleavage=None,
            mohs_scale_hardness="4 to 4.5",
            luster="Metallic to earthy",
            streak=None,
            diaphaneity="Opaque",
            optical_properties=None,
            refractive_index=None,
            crystal_habit="Spheres of intergrown octahedra and as disseminated microscopic grains",
            specific_gravity="4.049",
            group="Sulfides",
        )
        self.mineral2 = Mineral.objects.create(
            name="Greigite-2nd-Category",
            image_filename="greigite.jpg",
            image_caption="Greigite structure, SFe4 tetrahedra",
            category="SulfideThiospinel groupSpinel structural group",
            formula="Fe<sub>2</sub>+Fe<sub>3</sub>+<sub>2</sub>S<sub>4</sub>",
            strunz_classification="02.DA.05",
            color="Pale pink, tarnishes to metallic blue-black",
            crystal_system="Cubic",
            unit_cell="a = 9.876 Å; Z = 8",
            crystal_symmetry="Isometric hexoctahedralH-M symbol: (4/m32/m)Space group: F d3m",
            cleavage=None,
            mohs_scale_hardness="4 to 4.5",
            luster="Metallic to earthy",
            streak=None,
            diaphaneity="Opaque",
            optical_properties=None,
            refractive_index=None,
            crystal_habit="Spheres of intergrown octahedra and as disseminated microscopic grains",
            specific_gravity="4.049",
            group="Sulfides",
        )

    def test_index(self):
        resp = self.client.get(reverse('courses:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])

    def test_course_detail_view(self):
        resp = self.client.get(reverse('courses:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])