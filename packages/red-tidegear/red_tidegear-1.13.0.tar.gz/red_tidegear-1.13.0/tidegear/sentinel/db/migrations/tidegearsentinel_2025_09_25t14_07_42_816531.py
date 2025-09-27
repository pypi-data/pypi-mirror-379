# SPDX-FileCopyrightText: NONE
# SPDX-License-Identifier: CC0-1.0

from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import ForeignKey, Serial
from piccolo.columns.indexes import IndexMethod
from piccolo.table import Table


class Moderation(Table, tablename="moderation", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


ID = "2025-09-25T14:07:42:816531"
VERSION = "1.28.0"
DESCRIPTION = "temporary"


async def forwards():
    manager = MigrationManager(migration_id=ID, app_name="TidegearSentinel", description=DESCRIPTION)

    manager.alter_column(
        table_class_name="Change",
        tablename="change",
        column_name="moderation_id",
        db_column_name="moderation_id",
        params={"references": Moderation},
        old_params={"references": Moderation},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
        schema=None,
    )

    return manager
