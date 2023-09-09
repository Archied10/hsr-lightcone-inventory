from django.test import TestCase, Client

# Create your tests here.
class mainTest(TestCase):
    def test_html_is_equal(self):
        self.assertHTMLEqual(
            '<td style="word-wrap:break-all; max-width:100px;">{{ name }}</td>',
            """<td style = "word-wrap:break-all; max-width:100px;">
            {{ name }}
            </td>"""
        )

    def test_main_contains_name(self):
        response = Client().get('/')
        self.assertContains(response, "Nama : Mika Ahmad Al Husseini")