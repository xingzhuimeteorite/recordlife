import pytest 
import sys
sys.path.append('./')
import main
from configinfo import Github_token

token = Github_token

def test_main():
    """
    Test main function.
    """
    main.main(Github_token, 'xingzhuimeteorite/gitblog')


def test_login():
    """
    Test login function.
    """
    user = main.login(token)
    name = user.get_user().login
    repo = user.get_repo('xingzhuimeteorite/gitblog')
    # assert repo == 'gitblog'
    assert name == 'xingzhuimeteorite'