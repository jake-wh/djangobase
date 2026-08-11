from pathlib import Path
import environ
# ----------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()

environ.Env.read_env(
    env_file=BASE_DIR / '.env/env_base'
)
