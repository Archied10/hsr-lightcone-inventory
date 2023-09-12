from django.test import TestCase, Client
from django.template.loader import render_to_string

# Create your tests here.
class mainTest(TestCase):
    def test_html_is_equal(self):
        rendered = render_to_string('main.html')
        self.assertHTMLEqual(
            rendered,
            """<!DOCTYPE html>
                <html>
                <head>
                    <title>Light Cone Inventory</title>
                </head>
                <body>
                    <h1>Light Cone Inventory</h1>
                    <h2>Dibuat Oleh: </h2>
                    <h2>Nama : </h2>
                    <h2>NPM  : </h2>
                    <h2>Kelas: </h2>
                    <h3>Check out my <a href="lightcones/">Light Cones</a></h3>
                </body>
                </html>"""
        )

    def test_main_contains_name(self):
        response = Client().get('/')
        self.assertContains(response, "Mika Ahmad Al Husseini")