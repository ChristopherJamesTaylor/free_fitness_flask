# -*- coding: utf-8 -*-
from sqlalchemy import Column, Date, Index, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Person(Base):
    __tablename__ = u'person'
    __table_args__ = (
        Index(u'username_2', u'username', u'realSite'),
    )

    personId = Column(Integer, primary_key=True)
    nt_domain = Column(String(55))
    nt_username = Column(String(55))
    bExcludeFromReports = Column(Integer)
    nickname = Column(String(255))
    firstname = Column(String(255), index=True)
    lastname = Column(String(255), index=True)
    middleName = Column(String(255))
    fullName = Column(String(255), index=True)
    company = Column(String(255))
    companyID = Column(Integer)
    division = Column(String(255))
    costCenter = Column(Integer)
    startDate = Column(Date)
    positionType = Column(String(100))
    employeeStatus = Column(String(100), index=True)
    email = Column(String(255))
    departmentID = Column(Integer)
    department = Column(String(255))
    title = Column(String(255))
    buildingID = Column(String(11))
    building = Column(String(100))
    room = Column(String(100))
    address1 = Column(String(100))
    address2 = Column(String(100))
    city = Column(String(100))
    state = Column(String(100))
    country = Column(String(100))
    postalCode = Column(String(20))
    terminationDate = Column(Date)
    siteCode = Column(Integer)
    site = Column(String(50))
    realSite = Column(String(50))
    phone = Column(String(100))
    shoretelPhone = Column(String(100))
    username = Column(String(100), index=True)
    prefix = Column(String(50))
    suffix = Column(String(50))
    altLastName = Column(String(100))
    supervisorPersonID = Column(Integer)
    supervisorFirstName = Column(String(255))
    supervisorLastName = Column(String(255))
    primaryLocation = Column(String(255))
    renewDate = Column(Date)
    hrorg = Column(String(100))
    location_type_id = Column(Integer)
    LOCATION_TYPE_DESC = Column(String(100))
    rs3 = Column(String(100))
