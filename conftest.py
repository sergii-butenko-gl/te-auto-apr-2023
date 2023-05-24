import pytest
from src.user import User
from src.applications.api.github_api_client import GitHubAPIClient
from src.config.config import Config
from selenium import webdriver


@pytest.fixture(scope='session')  # session|package|module|class|function
def user_fixture():
    # create a user -> precondition
    user_name = User.username
    user = dict(name=user_name) 
    print(f"User '{user_name}' created")

    # execute test -> test step
    yield user

    # remove a user -> postconditions
    user = None  # user.remove()
    print(f"User '{user_name}' removed")


def pytest_html_report_title(report):
    report.title = "TE Apr 2023!"


@pytest.fixture(scope='module')
def fixture_git_hub_api_client():
    api = GitHubAPIClient()
    api.login(Config.get_property("USERNAME"), Config.get_property("PASSWORD"))

    yield api

    api.logout()


@pytest.fixture(scope='module')
def fixture_git_hub_api_client_search_repo():
    api = GitHubAPIClient()
    api.login(Config.get_property("USERNAME"), Config.get_property("PASSWORD"))

    yield api.search_repo

    api.logout()



@pytest.fixture
def wed_driver():
    # created a driver
    driver = webdriver.Chrome()

    yield driver

    driver.quit()


@pytest.fixture
def github_ui():
    browser_name = 'chrome'
    github_app = GithubApp()
    github_app.launch_browser(browser_name)

    yield github_app

    github_app.close_browser()