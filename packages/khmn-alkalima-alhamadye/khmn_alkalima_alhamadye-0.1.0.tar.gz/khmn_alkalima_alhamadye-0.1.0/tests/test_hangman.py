from khmn_alkalima_alhamadye.cli import hangman, main

def test_imports():
    # basic import tests; no game run
    assert callable(hangman)
    assert callable(main)
