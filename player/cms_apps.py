from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

@apphook_pool.register  # register the application
class PlayerApphook(CMSApp):
    app_name = "players"
    name = "Players"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["longturn.player.urls"]
