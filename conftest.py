#!/usr/bin/env python
# encoding: utf-8
# @author   : changhsing
# @time     : 2020/7/17 13:24
# @site     : 
# @file     : conftest.py
# @software : PyCharm
import pytest
import allure
import sys

sys.path.append('.\interfacetestcase')
from interfacetestcase.tool import *


@allure.step('清空用户表：users')
@pytest.fixture()
def truncate_table_users():
    Mysql().truncate_table('users')
