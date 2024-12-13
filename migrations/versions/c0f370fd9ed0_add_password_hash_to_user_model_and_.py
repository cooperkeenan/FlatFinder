"""Add password_hash to User model and integrate Flask-Bcrypt

Revision ID: c0f370fd9ed0
Revises: 
Create Date: 2024-12-13 02:08:14.824725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0f370fd9ed0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=128), nullable=False))
        batch_op.alter_column('first_name',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=150),
               nullable=False)
        batch_op.alter_column('last_name',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=150),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=150),
               nullable=False)
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=20),
               existing_nullable=True)
        batch_op.create_unique_constraint(None, ['email'])
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=100), nullable=True))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('phone',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
        batch_op.alter_column('email',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('last_name',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('first_name',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
