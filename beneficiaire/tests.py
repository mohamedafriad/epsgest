from django.test import TestCase

class HomePageTest(TestCase):
	def test_uses_home_template(self):
        	response=self.client.get("/beneficiaire/")
        	self.assertTemplateUsed(response, "list_benef.html")

class DetailBeneficiaireTest(TestCase):
	def test_uses_detail_template(self):
		response=self.client.get("/beneficiaire/1/")
		self.assertTemplateUsed(response, "detail_benef.html")
