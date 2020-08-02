from menus.base import Modifier
from menus.menu_pool import menu_pool

from cms.models import Page
from .models import CategoryExtension

class CategoryModifier(Modifier):
    """
    This modifier makes the category attribute of a page accessible for the menu
    system.
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        # only consider nodes that refer to cms pages
        # and put them in a dict for efficient access
        page_nodes = {n.id: n for n in nodes if n.attr["is_page"]}

        # retrieve the attributes of interest from the relevant pages
        pages = Page.objects.filter(id__in=page_nodes.keys())

        # loop over all relevant pages
        for page in pages:
            if hasattr(page, 'categoryextension'):
                page_nodes[page.id].attr['category'] = str(page.categoryextension)
            else:
                page_nodes[page.id].attr['category'] = ''

        return nodes

menu_pool.register_modifier(CategoryModifier)
