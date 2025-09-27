#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
import datetime

import pytest
from owlmixin.util import load_yaml

from jumeaux.addons.did_challenge.tag import Executor
from jumeaux.models import (
    DidChallengeAddOnPayload,
    DidChallengeAddOnReference,
    Response,
    CaseInsensitiveDict,
    HttpMethod,
)

RES_ONE = Response.from_dict(
    {
        "body": b"a",
        "type": "unknown",
        "headers": CaseInsensitiveDict({}),
        "url": "url",
        "status_code": 200,
        "elapsed": datetime.timedelta(seconds=1),
        "elapsed_sec": 1.0,
    }
)


RES_OTHER = Response.from_dict(
    {
        "body": b"b",
        "type": "unknown",
        "headers": CaseInsensitiveDict({}),
        "url": "url",
        "status_code": 200,
        "elapsed": datetime.timedelta(seconds=2),
        "elapsed_sec": 2.0,
    }
)


RES_ONE_PROPS = {"id": 1, "name": "ichiro", "age": 32}


RES_OTHER_PROPS = {"id": 2, "name": "jiro", "age": 28}


def create_trial_dict(seq: int, name: str, tags: List[str], status: str) -> dict:
    return {
        "seq": seq,
        "name": name,
        "tags": tags,
        "headers": {},
        "queries": {},
        "one": {"url": "http://one", "type": "json", "response_sec": 1.2},
        "other": {"url": "http://other", "type": "json"},
        "method": "GET",
        "path": "/path",
        "request_time": "2018-11-28T01:29:29.481790+09:00",
        "status": status,
    }


ADD_TAG_IF_CONDITION_IS_FULFILLED = (
    "Add a tag if a condition is fulfilled",
    """
                                     conditions:
                                       - tag: tagged
                                         when: "trial.name == 'hoge'"
                                     """,
    create_trial_dict(1, "hoge", [], "same"),
    create_trial_dict(1, "hoge", ["tagged"], "same"),
)

ADD_TAGS_IF_CONDITIONS_ARE_FULFILLED = (
    "Add tags if conditions are fulfilled",
    """
                                        conditions:
                                          - tag: tagged1
                                            when: "trial.name == 'hoge'"
                                          - tag: tagged2
                                            when: "trial.name == 'hoge'"
                                        """,
    create_trial_dict(1, "hoge", [], "same"),
    create_trial_dict(1, "hoge", ["tagged1", "tagged2"], "same"),
)

DO_NOT_ADD_TAG_IF_CONDITION_IS_NOT_FULFILLED = (
    "Don't Add a tag if a condition is not fulfilled",
    """
                                                conditions:
                                                  - tag: tagged
                                                    when: "trial.name == 'hogehoge'"
                                                """,
    create_trial_dict(1, "hoge", [], "same"),
    create_trial_dict(1, "hoge", [], "same"),
)

ADD_TAG_IF_CONDITION_IS_EMPTY = (
    "Add a tag if condition is empty",
    """
                                 conditions:
                                   - tag: tagged
                                 """,
    create_trial_dict(1, "hoge", ["initial"], "same"),
    create_trial_dict(1, "hoge", ["initial", "tagged"], "same"),
)

ADD_TAG_FORMATTED = (
    "Add a tag formatted",
    """
                     conditions:
                       - tag: "{{ trial.name }}: {{ res_one.elapsed_sec }}"
                     """,
    create_trial_dict(1, "hoge", [], "same"),
    create_trial_dict(1, "hoge", ["hoge: 1.0"], "same"),
)


ADD_TAG_IF_PROPS_CONDITION_IS_FULFILLED = (
    "Add tag if props condition is fulfilled",
    """
                     conditions:
                       - tag: "{{ res_one_props.id }}: {{ res_one_props.name }} is U30"
                         when: "res_one_props.age < 30"
                       - tag: "{{ res_other_props.id }}: {{ res_other_props.name }} is U30"
                         when: "res_other_props.age < 30"
                     """,
    create_trial_dict(1, "hoge", [], "same"),
    create_trial_dict(1, "hoge", ["2: jiro is U30"], "same"),
)


ADD_TAG_IF_CONDITION_HAS_OPTIONAL_PARAMETER = (
    "Add a tag if condition has a optional parameter",
    """
                                               conditions:
                                                 - tag: "other slow"
                                                   when: 'trial.other.response_sec|default(0.0) > 1.0'
                                                 - tag: "one slow"
                                                   when: 'trial.one.response_sec|default(0.0) > 1.0'
                                               """,
    create_trial_dict(1, "hoge", [], "same"),
    create_trial_dict(1, "hoge", ["one slow"], "same"),
)


class TestExec:
    @pytest.mark.parametrize(
        "title, config_yml, trial, expected_result",
        [
            ADD_TAG_IF_CONDITION_IS_FULFILLED,
            ADD_TAGS_IF_CONDITIONS_ARE_FULFILLED,
            DO_NOT_ADD_TAG_IF_CONDITION_IS_NOT_FULFILLED,
            ADD_TAG_IF_CONDITION_IS_EMPTY,
            ADD_TAG_IF_PROPS_CONDITION_IS_FULFILLED,
            ADD_TAG_FORMATTED,
            ADD_TAG_IF_CONDITION_HAS_OPTIONAL_PARAMETER,
        ],
    )
    def test(self, title, config_yml, trial, expected_result):
        payload: DidChallengeAddOnPayload = DidChallengeAddOnPayload.from_dict({"trial": trial})
        reference: DidChallengeAddOnReference = DidChallengeAddOnReference.from_dict(
            {
                "res_one": RES_ONE,
                "res_other": RES_OTHER,
                "res_one_props": RES_ONE_PROPS,
                "res_other_props": RES_OTHER_PROPS,
            }
        )

        actual: DidChallengeAddOnPayload = Executor(load_yaml(config_yml)).exec(payload, reference)

        assert expected_result == actual.trial.to_dict()
