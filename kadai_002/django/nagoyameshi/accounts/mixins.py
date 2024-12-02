from django.contrib.auth.mixins import UserPassesTestMixin


class OnlyManagementUserMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # user = self.request.user
        # return user.is_staff
        return True

