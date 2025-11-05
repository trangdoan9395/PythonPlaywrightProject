from turtle import pd
import pytest
from playwright.sync_api import sync_playwright
import pytest
import pandas as pd
import pyodbc as sql    

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)  # headless=False để thấy trình duyệt chạy
        context = browser.new_context(
        viewport={'width': 1920, 'height': 1080}  # kích thước full HD
)
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture(scope="session")
def db_connection():
    conn = sql.connect(
        server_hostname="adb-xxx.azuredatabricks.net",
        http_path="sql/protocolv1/o/123456789/1234-567890-abc123",
        access_token="YOUR_TOKEN"
    )
    yield conn
    conn.close()

def query_to_df(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    col_names = [desc[0] for desc in cursor.description]
    return pd.DataFrame(rows, columns=col_names)
