#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from research_eda_osm_rj.skeleton import fib

__author__ = "jgmos"
__copyright__ = "jgmos"
__license__ = "none"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
