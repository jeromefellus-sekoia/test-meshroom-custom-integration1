from meshroom.decorators import setup_consumer, teardown_consumer, scaffold_executor
from meshroom.model import Integration, Plug, Instance
import requests


@setup_consumer("carots", order="first", mode="push")
def setup_carots_consumer(integration: Integration, plug: Plug, instance: Instance):
    print("I create the consumer myEDR-side for carots")
    print(instance.get_secret("API_KEY"))
    API_KEY = instance.get_secret("API_KEY")
    requests.post(
        "https://myedr.com/api/carots",
        json={},
        headers={
            "Authorization": f"Bearer {API_KEY}",
        },
    )


@teardown_consumer("carots", mode="push")
def teardown_carots_consumer(integration: Integration, plug: Plug, instance: Instance):
    print("I delete the consumer myEDR-side for carots")
    requests.delete("https://myedr.com/api/carots")


@scaffold_executor("playbook-action")
def generate_code_for_a_playbook_action(integration: Integration):
    print(integration.path)
    with open(integration.path.parent / "MANIFEST.md", "w") as f:
        f.write("THIS IS A SUPER MANIFEST FOR MY NEW PLAYBOOK ACTION FOR PRODUCT MYEDR")
