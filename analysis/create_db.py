import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Numeric, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Argument(Base):
    __tablename__ = 'argument'
    # Here we define columns for the table argument.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    tw_type = Column(String(10))
    argument_type = Column(String(10))
    #argument_block = Column(String(1), nullable=False)
    #conclusion = Column(String(250), nullable=False)
    #argument_time = Column(Numeric(precision = 5), nullable=False)
    response_to_question = Column(Boolean)
    response_time = Column(Numeric(precision = 5), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///arguments.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
