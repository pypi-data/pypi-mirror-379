import os
import sys
from asyncdjangoorm.main import main

proj = os.path.basename(os.path.abspath(os.path.dirname(__file__)))
os.environ.setdefault("ASYNCDJANGO_SETTINGS_MODULE", f"{proj}.settings")

if __name__ == "__main__":
    main()
