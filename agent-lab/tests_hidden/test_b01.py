from app.service import parse_duration
def test_iso():
    assert parse_duration("PT1H30M") == 5400
    assert parse_duration("PT45S") == 45
    assert parse_duration("1h30m") == 5400
