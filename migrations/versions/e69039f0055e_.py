"""empty message

Revision ID: e69039f0055e
Revises: 
Create Date: 2022-02-19 10:43:26.516470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e69039f0055e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('last_name', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('phone', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=250), nullable=False),
    sa.Column('password_hash', sa.String(length=250), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('role', sa.String(length=3), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('NIF', sa.String(length=15), nullable=False),
    sa.Column('address', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roll',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('API_key',
    sa.Column('key', sa.String(length=262), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('installed', sa.String(length=5), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('key')
    )
    op.create_table('account_company_relationship',
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('account_id', 'company_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account_company_relationship')
    op.drop_table('API_key')
    op.drop_table('roll')
    op.drop_table('company')
    op.drop_table('account')
    # ### end Alembic commands ###
