from .reader import *
from .collector import *

__all__: list[str]

def parse_mcap(py_array: np.ndarray, mcap_path: str, topic: str, start_time_ns: int = 0, quiet: bool = True) -> str:
    """
    Parse an MCAP file into a numpy structured array
    """

def find_mcap_schema(mcap_path: str, topic: str, quiet: bool = True) -> str:
    """
    Find the schema of an MCAP file by walking through the messages
    """
