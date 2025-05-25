#!/usr/bin/env python3

# Script goes here!
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db',echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create some devs and companies
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
company1 = Company(name="TechCorp", founding_year=2001)
company2 = Company(name="CodeWorks", founding_year=1999)

session.add_all([dev1, dev2, company1, company2])
session.commit()

# Create freebies via company method

freebie1 = company1.give_freebie(dev1, "Sticker", 5, session)
freebie2 = company1.give_freebie(dev2, "T-shirt", 20, session)
freebie3 = company2.give_freebie(dev1, "Mug", 15, session)


session.commit()

print(" Database seeded successfully!")
