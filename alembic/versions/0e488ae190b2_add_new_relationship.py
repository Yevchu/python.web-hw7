"""add new relationship

Revision ID: 0e488ae190b2
Revises: 7e173421f401
Create Date: 2023-08-13 17:15:45.532595

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e488ae190b2'
down_revision: Union[str, None] = '7e173421f401'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subjects', sa.Column('grade_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'subjects', 'grades', ['grade_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subjects', type_='foreignkey')
    op.drop_column('subjects', 'grade_id')
    # ### end Alembic commands ###
