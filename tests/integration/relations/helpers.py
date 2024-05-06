#!/usr/bin/env python3
# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.
from typing import Optional

import yaml
from pytest_operator.plugin import OpsTest

from ..helpers import (
    METADATA,
    get_password,
    get_unit_address
)

from ..new_relations.test_new_relations import (
    get_application_relation_data,
    APPLICATION_APP_NAME,
)

APP_NAME = METADATA["name"]
DB_RELATION = "db"
DATABASE_RELATION = "database"
FIRST_DATABASE_RELATION = "first-database"
APP_NAMES = [APP_NAME, APPLICATION_APP_NAME]


async def get_database_connect_str(ops_test, application_name: str, relation_name: str) -> str:
    password = await get_password(ops_test)
    username = "operator"
    database = await get_application_relation_data(
        ops_test,
        application_name=application_name,
        relation_name=relation_name,
        key="database"
    )
    ip = await get_unit_address(ops_test, unit_name=f"{APP_NAME}/0")
    return f"dbname='{database}' user='{username}' host='{ip}' password='{password}' connect_timeout=10"
