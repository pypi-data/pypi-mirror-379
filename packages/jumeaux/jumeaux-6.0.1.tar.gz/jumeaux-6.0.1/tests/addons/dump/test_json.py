#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import json
import pytest

from owlmixin.util import load_yaml

from jumeaux.addons.dump.json import Executor
from jumeaux.models import Response, DumpAddOnPayload

NORMAL_BODY = json.dumps({
    "total": 10,
    "items": [
        {"id": 1, "name": "Ichiro", "favorites": ["apple", "orange"]},
        {"id": 2, "name": "次郎"}
    ]
}, ensure_ascii=False)

CORRUPTION_BODY_BYTES: bytes = '{"normal": "次郎", '.encode('euc-jp') + '"corruption": "三郎"}'.encode('utf8')

NORMAL_CASE = ("Normal",
               """
               force: False 
               """,
               Response.from_dict({
                   "body": NORMAL_BODY.encode('euc-jp'),
                   "type": "json",
                   "encoding": 'euc-jp',
                   "headers": {
                       "content-type": "application/json; charset=euc-jp"
                   },
                   "url": "http://test",
                   "status_code": 200,
                   "elapsed": datetime.timedelta(seconds=1),
                   "elapsed_sec": 1.0,
               }),
               NORMAL_BODY.encode('euc-jp'),
               'euc-jp',
               """
{
    "items": [
        {
            "favorites": [
                "apple",
                "orange"
            ],
            "id": 1,
            "name": "Ichiro"
        },
        {
            "id": 2,
            "name": "次郎"
        }
    ],
    "total": 10
}
""".strip().encode('euc-jp'),
               'euc-jp'
               )


CORRUPTION_CASE = ("Corruption",
               """
               force: False 
               """,
               Response.from_dict({
                   "body": CORRUPTION_BODY_BYTES,
                   "type": "json",
                   "encoding": 'euc-jp',
                   "headers": {
                       "content-type": "application/json; charset=euc-jp"
                   },
                   "url": "http://test",
                   "status_code": 200,
                   "elapsed": datetime.timedelta(seconds=1),
                   "elapsed_sec": 1.0,
               }),
               CORRUPTION_BODY_BYTES,
               'euc-jp',
               """
{
    "corruption": "筝����",
    "normal": "次郎"
}
""".strip().encode('euc-jp', errors='replace'),
               'euc-jp'
               )


class TestExec:
    @pytest.mark.parametrize(
        'title, config_yml, response, body, encoding, expected_body, expected_encoding', [
            NORMAL_CASE,
            CORRUPTION_CASE,
        ]
    )
    def test(self, title, config_yml, response, body, encoding, expected_body, expected_encoding):
        payload: DumpAddOnPayload = DumpAddOnPayload.from_dict({
            'response': response,
            'body': body,
            'encoding': encoding,
        })

        actual: DumpAddOnPayload = Executor(load_yaml(config_yml)).exec(payload)

        assert actual.body == expected_body
        assert actual.encoding.get() == expected_encoding
