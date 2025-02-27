from model.entity import *

class UnitUserConnector(Base):
    __tablename__ = 'unit_user_connector'
    id = Column(Integer, primary_key=True, autoincrement=True)
    unit_id = Column(Integer, ForeignKey('units.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    unit = relationship("Units")
    user = relationship("Users")

    def __init__(self, unit, user):
        self.id = None
        self.unit_id = unit.id
        self.user_id = user.id
