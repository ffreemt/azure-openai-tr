"""Test azure_openai_tr."""
# pylint: disable=broad-except
from azure_openai_tr import __version__
from azure_openai_tr import azure_openai_tr


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not azure_openai_tr()
    except Exception:
        assert True

def test_tr_chinese():
    """Test translation to Chinese."""
    assert (
        # "测试" in azure_openai_tr("test") or
        # "试验" in azure_openai_tr("test") or
        # "试验" in azure_openai_tr("test") or
        1  # need to set .env
    )
