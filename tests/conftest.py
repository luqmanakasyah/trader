import sys
import os
# Add project root so 'packages' module can be found
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
