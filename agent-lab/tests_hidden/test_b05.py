from app import service, db

def test_customer_orders():
    rows = db.get_customer_orders("acme")
    assert len(rows) == 1

def test_list_orders_unchanged():
    assert len(service.list_orders()) == 3

def test_no_sql_in_service():
    import inspect
    src = inspect.getsource(service).upper()
    assert "SELECT " not in src and "INSERT " not in src
