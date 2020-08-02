from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

@apphook_pool.register  # register the application
class WarcalcApphook(CMSApp):
    app_name = "warcalc"
    name = "Warcalc"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["longturn.warcalc.urls"]
