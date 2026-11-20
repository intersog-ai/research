from app.service import list_orders
def test_min_total():
    assert [o["customer"] for o in list_orders(min_total=100)] == ["acme", "initech"]
    assert len(list_orders()) == 3
