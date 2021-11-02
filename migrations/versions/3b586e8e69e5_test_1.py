"""test 1

Revision ID: 3b586e8e69e5
Revises: 
Create Date: 2021-10-29 23:00:28.276350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b586e8e69e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('SmartContract',
    sa.Column('smartContractAddress', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('numberOfItems', sa.INTEGER(), nullable=True),
    sa.Column('website', sa.TEXT(), nullable=True),
    sa.Column('discord', sa.TEXT(), nullable=True),
    sa.Column('mediumUsername', sa.TEXT(), nullable=True),
    sa.Column('telegramUrl', sa.TEXT(), nullable=True),
    sa.Column('twitterUsername', sa.TEXT(), nullable=True),
    sa.Column('instagramUsername', sa.TEXT(), nullable=True),
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
