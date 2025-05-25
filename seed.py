#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

# Set up the database
engine = create_engine('sqlite:///freebies.db', echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#  Clear existing data
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()
session.commit()

#  Seed fresh data
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
dev3 = Dev(name="Gloria")
dev4 = Dev(name="Gilbert")
dev5 = Dev(name="Chebson")

company1 = Company(name="TechCorp", founding_year=2001)
company2 = Company(name="CodeWorks", founding_year=1999)
company3 = Company(name="Kibabi", founding_year=2000)
company4 = Company(name="Zetech", founding_year=1990)
company5 = Company(name="Moringa", founding_year=2008)

session.add_all([dev1, dev2, dev3, dev4, dev5,
                 company1, company2, company3, company4, company5])
session.commit()


# Add more freebies
freebie4 = company3.give_freebie(dev3, "Water Bottle", 10, session)
freebie5 = company4.give_freebie(dev4, "Laptop Sticker", 7, session)
freebie6 = company5.give_freebie(dev5, "Notebook", 12, session)
freebie7 = company1.give_freebie(dev3, "USB Drive", 25, session)
freebie8 = company2.give_freebie(dev4, "Pen", 3, session)
freebie9 = company3.give_freebie(dev5, "Keychain", 6, session)
freebie10 = company5.give_freebie(dev1, "Tote Bag", 15, session)



session.commit()

print(" Database seeded successfully!")
