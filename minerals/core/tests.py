from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from minerals.core.models import Mineral


class MineralModelTests(TestCase):
    """Test for Mineral Model"""
    def test_mineral_creation(self):
        """Test to create 1 mineral"""
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
        self.assertLess(mineral.pub_date, now)


class MineralViewsTests(TestCase):
    """Testing Mineral View"""
    def setUp(self):
        """Creating 2 Minerals"""
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
        """Testing Mineral List View"""
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'index.html')

    def test_mineral_detail_view(self):
        """Testing Mineral Detail View"""
        resp = self.client.get(reverse('detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'detail.html')

    def test_search_q(self):
        """Testing Search View by Alphabet"""
        resp = self.client.get(reverse('search'), {'q': 'G'})
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'index.html')

    def test_search_q2(self):
        """Testing Search View by Alphabet 404"""
        resp = self.client.get(reverse('search'), {'q': 'X'})
        self.assertEqual(resp.status_code, 404)
        self.assertTemplateUsed(resp, '404.html')

    def test_search_group(self):
        """Testing Search View by Group"""
        resp = self.client.get(reverse('search'), {'group': 'Sulfides'})
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'index.html')

    def test_search_text(self):
        """Testing Search View by Full-Text Search"""
        resp = self.client.get(reverse('search'), {'text': 'Cubic'})
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'index.html')
