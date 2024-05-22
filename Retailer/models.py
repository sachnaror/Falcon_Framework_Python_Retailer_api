from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Update the database URI for MySQL
DB_URI = 'mysql+pymysql://root@127.0.0.1/falcon_db'


class Retailer(Base):
    __tablename__ = 'retailer'
    id = Column(Integer, primary_key=True)
    GSTIN = Column(String(15))
    Business_name = Column(String(100))
    Contact_person = Column(String(50))
    Contact_number = Column(Integer)
    Contact_address = Column(String(100))
    Contact_emailId = Column(String(50))
    Status = Column(String(10))
    Outlet_limit = Column(Integer)


if __name__ == "__main__":
    from sqlalchemy import create_engine

    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
