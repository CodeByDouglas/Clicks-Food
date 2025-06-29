import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import *

app = create_app()

with app.app_context():
    db.create_all()
    print('✅ Todas as tabelas foram criadas com sucesso!') 
