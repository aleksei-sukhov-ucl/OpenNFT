"""test 2

Revision ID: 4019005a5d4d
Revises: 4ef3534a8a37
Create Date: 2021-10-31 15:28:49.747460

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4019005a5d4d'
down_revision = '4ef3534a8a37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('SmartContract', 'website',
               existing_type=mysql.TEXT(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
    op.alter_column('SmartContract', 'discord',
               existing_type=mysql.TEXT(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
    op.alter_column('SmartContract', 'mediumUsername',
               existing_type=mysql.TEXT(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
    op.alter_column('SmartContract', 'telegramUrl',
               existing_type=mysql.TEXT(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
    op.alter_column('SmartContract', 'twitterUsername',
               existing_type=mysql.TEXT(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
    op.alter_column('SmartContract', 'instagramUsername',
               existing_type=mysql.TEXT(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('SmartContract', 'instagramUsername',
               existing_type=sa.VARCHAR(length=255),
               type_=mysql.TEXT(),
               existing_nullable=True)
    op.alter_column('SmartContract', 'twitterUsername',
               existing_type=sa.VARCHAR(length=255),
               type_=mysql.TEXT(),
               existing_nullable=True)
    op.alter_column('SmartContract', 'telegramUrl',
               existing_type=sa.VARCHAR(length=255),
               type_=mysql.TEXT(),
               existing_nullable=True)
    op.alter_column('SmartContract', 'mediumUsername',
               existing_type=sa.VARCHAR(length=255),
               type_=mysql.TEXT(),
               existing_nullable=True)
    op.alter_column('SmartContract', 'discord',
               existing_type=sa.VARCHAR(length=255),
               type_=mysql.TEXT(),
               existing_nullable=True)
    op.alter_column('SmartContract', 'website',
               existing_type=sa.VARCHAR(length=255),
               type_=mysql.TEXT(),
               existing_nullable=True)
    # ### end Alembic commands ###