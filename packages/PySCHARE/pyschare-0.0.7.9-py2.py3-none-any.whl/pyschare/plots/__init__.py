from .interactive_plots import _Visuals
from google.cloud import storage
storage_client = storage.Client()

def _init_plots():
    global plots
    plots = _Visuals()


_init_plots()


