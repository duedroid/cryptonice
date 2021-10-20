"""init

Revision ID: f4c4f9ad6dba
Revises: 
Create Date: 2021-10-20 06:18:02.079483

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f4c4f9ad6dba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('bridge', sa.String(), nullable=True),
    sa.Column('api_key', sa.String(), nullable=True),
    sa.Column('api_secret', sa.String(), nullable=True),
    sa.Column('max_open_trades', sa.Integer(), nullable=True),
    sa.Column('current_open_trades', sa.Integer(), nullable=True),
    sa.Column('is_bot_active', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.String(), nullable=True),
    sa.Column('pair', sa.String(), nullable=False),
    sa.Column('side', sa.String(), nullable=False),
    sa.Column('price', sa.DECIMAL(), nullable=False),
    sa.Column('amount', sa.DECIMAL(), nullable=False),
    sa.Column('amount_bridge', sa.DECIMAL(), nullable=False),
    sa.Column('profit', sa.DECIMAL(), nullable=True),
    sa.Column('profit_bridge', sa.DECIMAL(), nullable=True),
    sa.Column('order_data', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('is_force_sell', sa.Boolean(), nullable=True),
    sa.Column('is_buy_order_sell', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_id'), 'order', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_order_id'), table_name='order')
    op.drop_table('order')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
