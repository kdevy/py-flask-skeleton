import sys
sys.path.insert(0, '/app')
import monitor

monitor.start(interval=1.0)

from bootstrap import create_app
application = create_app()
