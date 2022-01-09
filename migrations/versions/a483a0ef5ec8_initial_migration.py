"""Initial migration.

Revision ID: a483a0ef5ec8
Revises: 
Create Date: 2022-01-09 21:39:01.601610

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a483a0ef5ec8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('SmartContract',
    sa.Column('smartContractAddress', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('assetName', sa.VARCHAR(length=255), nullable=True),
    sa.Column('assetDescription', sa.TEXT(), nullable=True),
    sa.Column('numberOfItems', sa.INTEGER(), nullable=True),
    sa.Column('website', sa.VARCHAR(length=255), nullable=True),
    sa.Column('discord', sa.VARCHAR(length=255), nullable=True),
    sa.Column('mediumUsername', sa.VARCHAR(length=255), nullable=True),
    sa.Column('telegramUrl', sa.VARCHAR(length=255), nullable=True),
    sa.Column('twitterUsername', sa.VARCHAR(length=255), nullable=True),
    sa.Column('instagramUsername', sa.VARCHAR(length=255), nullable=True),
    sa.Column('safeListRequestStatus', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('smartContractAddress')
    )
    op.create_table('Asset',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('smartContractAddress', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('token_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('onSale', sa.Boolean(), nullable=True),
    sa.Column('rarityScore', sa.Integer(), nullable=True),
    sa.Column('metaData', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['smartContractAddress'], ['SmartContract.smartContractAddress'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('TradingHistory',
    sa.Column('smartContractAddress', sa.String(length=255), nullable=False),
    sa.Column('token_id', sa.Integer(), nullable=False),
    sa.Column('timeStamp', sa.DateTime(timezone=6), nullable=False),
    sa.Column('eventType', sa.String(length=255), nullable=False),
    sa.Column('salePrice', sa.Float(), nullable=True),
    sa.Column('saleCurrency', sa.String(length=255), nullable=True),
    sa.Column('usdSalePrice', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['smartContractAddress'], ['SmartContract.smartContractAddress'], ),
    sa.PrimaryKeyConstraint('smartContractAddress', 'token_id', 'timeStamp', 'eventType')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('TradingHistory')
    op.drop_table('Asset')
    op.drop_table('SmartContract')
    # ### end Alembic commands ###