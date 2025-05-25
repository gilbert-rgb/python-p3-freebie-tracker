from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)

    freebies = relationship('Freebie', back_populates='company')
    devs = relationship('Dev', secondary='freebies', overlaps='freebies,companies')

    def give_freebie(self, dev, item_name, value, session):
        freebie = Freebie(dev=dev, company=self, item_name=item_name, value=value)
        session.add(freebie)
        return freebie

    def __repr__(self):
        return f"<Company id={self.id} name='{self.name}' founding_year={self.founding_year}>"

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    freebies = relationship('Freebie', back_populates='dev')
    companies = relationship('Company', secondary='freebies', overlaps='freebies,devs')

    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, dev, freebie):
        if freebie.dev == self:
            freebie.dev = dev

    def __repr__(self):
        return f"<Dev id={self.id} name='{self.name}'>"

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    value = Column(Integer)

    dev_id = Column(Integer, ForeignKey('devs.id'))
    dev = relationship('Dev', back_populates='freebies', overlaps='companies,devs')

    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship('Company', back_populates='freebies', overlaps='companies,devs')

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"

    def __repr__(self):
        return f"<Freebie id={self.id} item_name='{self.item_name}' value={self.value} dev_id={self.dev_id} company_id={self.company_id}>"
