import pytest

@pytest.fixture
def api_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def sample_post():
    return {
        "title": "QA Test",
        "body": "My first post",
        "userId": 1
    }

import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):
    yield
    if request.node.rep_call.failed:
        page.screenshot(
            path=f"screenshots/{request.node.name}.png"
        )