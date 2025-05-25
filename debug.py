# debug.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dev, Company, Freebie

import ipdb  

# Set up database and session
engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


print(" Companies:", session.query(Company).all())
print(" Devs:", session.query(Dev).all())
print("Freebies:", session.query(Freebie).all())

# Open IPython Debugger
ipdb.set_trace()
