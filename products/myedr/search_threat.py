
from meshroom.decorators import setup_executor

from meshroom.model import Integration, Plug, Instance



@setup_executor("search_threat")

def setup_threat_search_api_via_myedr_plugin(integration: Integration, plug: Plug, instance: Instance):

    some_value = instance.settings.get("some_setting")

    some_secret = plug.get_secret("SOME_SECRET")

    api_key = instance.get_secret("API_KEY")

    raise NotImplementedError("Implement the setup mechanism here")

