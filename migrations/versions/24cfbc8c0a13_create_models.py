"""create models

Revision ID: 24cfbc8c0a13
Revises: 
Create Date: 2023-05-18 15:45:27.149758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24cfbc8c0a13'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Descriptions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('love_description', sa.String(), nullable=True),
    sa.Column('work_description', sa.String(), nullable=True),
    sa.Column('issue_description', sa.String(), nullable=True),
    sa.Column('money_description', sa.String(), nullable=True),
    sa.Column('health_description', sa.String(), nullable=True),
    sa.Column('spirit_description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('images_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Users',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('chat_id', sa.BigInteger(), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('card_name', sa.String(), nullable=True),
    sa.Column('card_url', sa.String(), nullable=True),
    sa.Column('card_description', sa.String(), nullable=True),
    sa.Column('harness', sa.String(), nullable=True),
    sa.Column('descriptions_id', sa.BigInteger(), nullable=True),
    sa.Column('img_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['descriptions_id'], ['Descriptions.id'], ),
    sa.ForeignKeyConstraint(['img_id'], ['Images.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Cards')
    op.drop_table('Users')
    op.drop_table('Images')
    op.drop_table('Descriptions')
    # ### end Alembic commands ###
