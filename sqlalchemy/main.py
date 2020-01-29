from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db.s3db", echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    
    def __repr__(self):
        return f"<User(firstname='{self.firstname}', lastname='{self.lastname}')>"

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


if True:
    user1 = User(firstname='Ronny', lastname='Richardson')
    user2 = User(firstname='Tom', lastname='Taylor')
    session.add_all([user1, user2])
    session.commit()


for instance in session.query(User).order_by(User.id):
    print(f"{instance.id} {instance.firstname} {instance.lastname}")