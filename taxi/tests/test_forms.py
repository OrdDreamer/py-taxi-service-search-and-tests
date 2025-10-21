from django.test import TestCase

from taxi.forms import SearchForm


class FormTests(TestCase):
    def test_search(self):
        form_data = {
            "query": "Renault",
        }
        form = SearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
