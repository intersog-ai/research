from app.service import export_orders_csv
def test_csv():
    lines = export_orders_csv().strip().splitlines()
    assert lines[0].replace(" ", "") == "id,customer,total"
    assert len(lines) == 4
