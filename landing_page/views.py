from django.views.generic import TemplateView
from django.conf import settings


class IndexView(TemplateView):
    template_name = "index.html"
    company_name = settings.COMPANY_NAME