# Add src to path for local development without pip install
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
