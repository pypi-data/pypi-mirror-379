"""gbp-ps"""

import importlib.metadata

__version__ = importlib.metadata.version("gbp-ps")

# Plugin definition
plugin = {
    "name": "gbp-ps",
    "version": __version__,
    "description": "A plugin to display your Gentoo Build Publisher processes",
    "app": "gbp_ps.django.gbp_ps",
    "urls": "gbp_ps.django.gbp_ps.views",
    "graphql": "gbp_ps.graphql",
    "priority": -10,
}
