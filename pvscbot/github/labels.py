# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import enum


@enum.unique
class Status(enum.Enum):
    classify = "classify"
    triage = "triage"
    needs_decision = "needs decision"
    needs_more_info = "info needed"
    needs_PR = "needs PR"
    needs_spec = "needs spec"
    needs_upstream_fix = "needs upstream fix"
    validate_fix = "validate fix"


@enum.unique
class Skip(enum.Enum):
    news = "skip news"
