"""Test the exam_env module.

all import and structural testing is done in this module.
"""

from datacenter.model.foo_bar import FooBar
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


def test_01_foobar(capsys):
    """Test FooBar."""
    session = create_test_session()
    foo_bar = datacenter.model.FooBar()
    foo_bar.value = "FooBar"
    session.add(foo_bar)
    session.commit()

    assert repr(foo_bar) == "FooBar:FooBar"

    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
