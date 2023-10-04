"""deploy

Revision ID: 52bb24226b35
Revises: 
Create Date: 2023-10-04 02:52:41.380980

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '52bb24226b35'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('channel_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('member_count', sa.Integer(), nullable=True),
    sa.Column('link', sa.String(), nullable=True),
    sa.Column('messages', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_channel_info_id'), 'channel_info', ['id'], unique=False)
    op.create_index(op.f('ix_channel_info_username'), 'channel_info', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_channel_info_username'), table_name='channel_info')
    op.drop_index(op.f('ix_channel_info_id'), table_name='channel_info')
    op.drop_table('channel_info')
    # ### end Alembic commands ###
