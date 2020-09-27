import pytest
from utilities.common_utils import get_config


@pytest.mark.parametrize("keys",
                         [
                             "API_KEY",
                             "API_SECRET_KEY",
                             "ACCESS_TOKEN",
                             "ACCESS_TOKEN_SECRET"
                         ])
def test_secret_key_accessible(keys):
    assert (get_config(keys) != '')


def test_environment_variable_not_set_exception():
    key = 'API_KEY_N'
    with pytest.raises(OSError) as env_error:
        get_config(key)
    assert (str(env_error.value) == f"Environment variable '{key}' is not set")



