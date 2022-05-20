from django.contrib.auth.mixins import UserPassesTestMixin


class OwnerAccessMixin(UserPassesTestMixin):

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user