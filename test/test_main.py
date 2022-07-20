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
    main.main(Github_token, 'xingzhuimeteorite/recordlife')


def test_login():
    """
    Test login function.
    """
    user = main.login(token)
    name = user.get_user().login
    repo = user.get_repo('xingzhuimeteorite/gitblog')
    # assert repo == 'gitblog'
    assert name == 'xingzhuimeteorite' 

def test_add_goldword():
    user = main.login(token)
    repo = user.get_repo('xingzhuimeteorite/gitblog')
    issese = repo.get_issues()
    