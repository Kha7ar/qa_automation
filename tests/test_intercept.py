from playwright.sync_api import Page, expect
import json

def test_intercept(page: Page):
    # Перехватываем запрос и возвращаем свои данные
    def mock_response(route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps({
                "data": {
                    "id": 999,
                    "email": "khazar@qa.com",
                    "first_name": "Khazar",
                    "last_name": "QA"
                }
            })
        )
    
    # Перехватываем все запросы к /api/users/2
    page.route("**/api/users/2", mock_response)
    
    # Открываем страницу — запрос будет перехвачен
    page.goto("https://reqres.in/api/users/2")
    
    # Проверяем что видим наши данные
    expect(page.get_by_text("khazar@qa.com")).to_be_visible()