from time import sleep

import pytest

@pytest.fixture()
def on_start_10s_delay():
    sleep(10)
    

