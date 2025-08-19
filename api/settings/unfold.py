from os import environ
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

######################################################################
# Unfold
######################################################################
UNFOLD = {
    "SITE_HEADER": _("Turbo Admin"),
    "SITE_TITLE": _("Turbo Admin"),,
    "SITE_ICON": lambda request: static("logo.png"),
    "SHOW_HISTORY": False,
    "SHOW_VIEW_ON_SITE": False,
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": _("Navigation"),
                "separator": False,
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "person",
                        "link": reverse_lazy("admin:api_user_changelist"),
                    },
                ],
            },
        ],
    },
}
