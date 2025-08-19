from allauth.account.adapter import DefaultAccountAdapter
from django.http import JsonResponse


class AccountAdapter(DefaultAccountAdapter):
    """
    Adapter for the user management.
    """
    def respond_user_inactive(self, request, user):
        """
        Responds to an inactive user's access request.

        :param request: The HTTP request
        :param user: The user who made the request
        :return: A JSON response with an error message
        """
        return JsonResponse({'detail': 'User account is inactive.'}, status=400)
