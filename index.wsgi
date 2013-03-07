import sae
from myapp import app , db
db.create_all()
application = sae.create_wsgi_app(app)
