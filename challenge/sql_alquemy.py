from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import inspect
from sqlalchemy import ForeignKey

Base = declarative_base()

class Client(Base):
  __tablename__ = 'client'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  cpf = Column(String(10))
  address = Column(String(10))
  account = relationship(
    "Account", back_populates="clients", cascade="all, delete-orphan" 
  )
  def __repr__(self):
    return  f"Client(id={self.id}, name={self.name}, cpf={self.cpf}, address={self.address} )"

class Account(Base):
  __tablename__ = 'account'
  id = Column(Integer, primary_key=True)
  type = Column(String)
  bank_agency = Column(String)
  num = Column(Integer)
  id_client = Column(Integer,  ForeignKey("client.id"), nullable=False )
  balance = Column(DECIMAL)
  clients = relationship("Client", back_populates="account")
  def __repr__(self):
    return  f"Client(id={self.id}, type={self.type}, bank_agency={self.bank_agency}, num={self.num}, id_client={self.id_client}, balance={self.balance} )"

engine = create_engine("sqlite://")
Base.metadata.create_all(engine)

inspector_engine = inspect(engine)
"""
table analysis
"""
print("Table name\n")

print(inspector_engine.get_table_names())
"""
table name
"""
print("Database\n")
print(inspector_engine.default_schema_name)
"""
database name
"""

with Session(engine) as session:
  spongebob = Client(
  name = "spongebob",
  cpf= "333333333",
  address="Pineapple",
  account = [
    Account(type="krusty krab",bank_agency="003", num="01", balance=400)
  ]
  )

  sandy = Client(
  name = "sandy",
  address = "Texas",
  cpf= "444444444",
  account = [
    Account(type="krusty krab", bank_agency="004", num="02", balance=800),
    Account(type="krusty krab", bank_agency="004", num="04", balance=100),
    Account(type="krusty krab", bank_agency="004", num="05", balance=50),
    Account(type="krusty krab", bank_agency="004", num="06", balance=250)
  ]
  )
  patrick = Client(
    name="patrick",
    cpf= "777777777",
    address ="Rock",
    account = [
      Account(type="Krusty Krab", bank_agency="004",  num="03", balance=0)
    ]
    )

  session.add_all([spongebob, sandy, patrick])
  session.commit()

session = Session(engine)
stmt = select(Client).where(Client.name.in_(["spongebob", "sandy", "patrick"]))
"""
list of registered customers
"""
for user in session.scalars(stmt):
  print(user)

print("\n")

stmt_account = select(Account).where(Account.id.in_([2]))
"""
list of accounts for each client
"""
for account in session.scalars(stmt_account):
  print(account)
  print("\n")