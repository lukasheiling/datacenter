"""utils for test sessions."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from datacenter.model import Base


def create_test_session():
    """Create in memory sqlite session for testing."""
    memory_engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(memory_engine)

    MemorySession = sessionmaker(bind=memory_engine)

    session = MemorySession()
    return session
