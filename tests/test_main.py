from particle_life_simulation.__main__ import main


def test_main_successful_exit():
    assert main() == 0
