import sys
sys.path.insert(0, '/app')
import bootstrap

app = bootstrap.create_app()

with app.app_context():
  bootstrap.db.create_all()