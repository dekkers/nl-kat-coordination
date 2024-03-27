"""Remove redundant dispatches field

Revision ID: 0006
Revises: 0005
Create Date: 2022-03-25 14:28:34.584808

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "0006"
down_revision = "0005"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("boefje_meta", "dispatches")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "boefje_meta",
        sa.Column("dispatches", postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    )
    # ### end Alembic commands ###
