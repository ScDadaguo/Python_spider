#!C:\Users\a\PycharmProjects\python_spider\venv2\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'qqbot==2.3.10','console_scripts','qq'
__requires__ = 'qqbot==2.3.10'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('qqbot==2.3.10', 'console_scripts', 'qq')()
    )
