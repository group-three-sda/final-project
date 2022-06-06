from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class OwnerAccessMixin(UserPassesTestMixin):

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class UserConfirmMixin(UserPassesTestMixin):

    def test_func(self):
        obj = self.get_object()
        confirmed = obj.confirm
        if not confirmed:
            raise PermissionDenied
        else:
            return True
