from datetime import datetime
import sqlalchemy 
from .base import Base

class NetworkUsage(Base):
    __tablename__ = 'network_usage'

    network_usage_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    timestamp = sqlalchemy.Column(DateTime, default=datetime.utcnow)
    traffic = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    performance = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    connection_id = Column(Integer, ForeignKey('connection.id'))

    def __repr__(self):
        """Generate nice representation!"""
        return "NetworkUsage: {}mb/s, {}, time:{}".f(self.traffic, self.performance, self.timestamp)
