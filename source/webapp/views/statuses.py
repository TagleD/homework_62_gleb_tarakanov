from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import StatusForm
from webapp.models import Status


class StatusAddView(UserPassesTestMixin, CreateView):
    template_name = 'status/status_create.html'
    model = Status
    form_class = StatusForm
    permission_denied_message = 'У вас нет прав доступа'

    def test_func(self):
        return self.request.user.has_perm('webapp.change_status')

    def get_success_url(self):
        return reverse('index')