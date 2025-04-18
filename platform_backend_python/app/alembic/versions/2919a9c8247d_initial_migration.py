"""Initial migration

Revision ID: 2919a9c8247d
Revises: 
Create Date: 2025-04-01 18:07:45.207225

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2919a9c8247d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth_user',
    sa.Column('uuid', sa.Uuid(), nullable=False),
    sa.Column('username', sa.String(length=63), nullable=True),
    sa.Column('password', sa.LargeBinary(), nullable=True),
    sa.Column('totp_secret', sa.String(length=33), nullable=True),
    sa.Column('email', sa.String(length=63), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_index(op.f('ix_auth_user_username'), 'auth_user', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_auth_user_username'), table_name='auth_user')
    op.drop_table('auth_user')
    # ### end Alembic commands ###
