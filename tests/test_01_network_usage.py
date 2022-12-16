"""Test the exam_env module.

all import and structural testing is done in this module.
"""
import datetime
from datacenter.model.network_usage import NetworkUsage
from utilities import create_test_session

try:
    import datacenter
except ImportError:
    pass

def test_00(capsys):
    """Test module import."""
    assert datacenter
    assert datacenter.model

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""


def test_02_network_usage(capsys):
    """Test Networkusage."""
    session = create_test_session()
    network_usage = datacenter.model.NetworkUsage()
    network_usage.traffic = 200
    network_usage.performance = 10
    network_usage.time = datetime.utcnow()
    session.commit()

    assert repr(network_usage) == "NetworkUsage: {}mb/s, {}, time:{}".f(network_usage.traffic, network_usage.performance, network_usage.timestamp)

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
