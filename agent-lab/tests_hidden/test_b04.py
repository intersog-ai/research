from app.service import list_orders
def test_pages():
    assert len(list_orders(page=1, page_size=2)) == 2
    assert len(list_orders(page=2, page_size=2)) == 1
