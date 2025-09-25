# SPDX-FileCopyrightText: 2023 Helge
# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT

from datetime import datetime, timedelta, timezone

from . import check_max_offset_now, get_gmt_now, parse_gmt


def test_get_gmt_now() -> None:
    date_string = get_gmt_now()

    assert "GMT" in date_string


def test_parse_gmt() -> None:
    date_string = get_gmt_now()

    parsed = parse_gmt(date_string)
    now = datetime.now(tz=timezone.utc)

    assert parsed <= now
    assert parsed >= now - timedelta(seconds=5)


def test_check_max_offset_now() -> None:
    now = datetime.now(tz=timezone.utc)

    assert check_max_offset_now(now - timedelta(minutes=4))
    assert check_max_offset_now(now + timedelta(minutes=4))
    assert not check_max_offset_now(now - timedelta(minutes=6))
    assert not check_max_offset_now(now + timedelta(minutes=6))
