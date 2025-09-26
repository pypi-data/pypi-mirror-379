from pathlib import Path
from trame_vuetify import __version__

serve_path = str(Path(__file__).with_name("vue3-lab-serve").resolve())
roboto_path = str(Path(__file__).with_name("roboto").resolve())

serve = {
    f"__trame_vuetify_lab_{__version__}": serve_path,
    f"__trame_roboto_{__version__}": roboto_path,
}

scripts = [f"__trame_vuetify_lab_{__version__}/trame-vuetify-lab.umd.js"]
styles = [
    f"__trame_vuetify_lab_{__version__}/style.css",
    f"__trame_vuetify_lab_{__version__}/css/mdi.css",
    f"__trame_roboto_{__version__}/roboto.css",
]
vue_use = ["vuetifylab.createVuetify(trame.state.get('trame__vuetify3_config')||{})"]


def setup(server, **kargs):
    client_type = "vue2"
    if hasattr(server, "client_type"):
        client_type = server.client_type

    if client_type != "vue3":
        raise TypeError(
            f"Server using client_type='{client_type}' while we expect 'vue3'"
        )
