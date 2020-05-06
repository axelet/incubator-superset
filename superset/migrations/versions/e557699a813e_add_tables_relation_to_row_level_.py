# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""add_tables_relation_to_row_level_security

Revision ID: e557699a813e
Revises: 47a540c56d82
Create Date: 2020-04-24 10:46:24.119363

"""

# revision identifiers, used by Alembic.
revision = "e557699a813e"
down_revision = "f9a30386bd74"

import sqlalchemy as sa
from alembic import op


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "rls_filter_tables",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("table_id", sa.Integer(), nullable=True),
        sa.Column("rls_filter_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["rls_filter_id"], ["row_level_security_filters.id"]),
        sa.ForeignKeyConstraint(["table_id"], ["tables.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.drop_constraint(
        "row_level_security_filters_table_id_fkey",
        "row_level_security_filters",
        type_="foreignkey",
    )
    op.drop_column("row_level_security_filters", "table_id")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "row_level_security_filters",
        sa.Column("table_id", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.create_foreign_key(
        "row_level_security_filters_table_id_fkey",
        "row_level_security_filters",
        "tables",
        ["table_id"],
        ["id"],
    )
    op.drop_table("rls_filter_tables")
    # ### end Alembic commands ###