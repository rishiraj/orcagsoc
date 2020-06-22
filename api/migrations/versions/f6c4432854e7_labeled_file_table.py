"""labeled_file table

Revision ID: f6c4432854e7
Revises: 
Create Date: 2020-06-18 13:56:03.934283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6c4432854e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('labeled_file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=50), nullable=True),
    sa.Column('orca', sa.Boolean(), nullable=True),
    sa.Column('extra_label', sa.String(length=10), nullable=True),
    sa.Column('expertise_level', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('labeled_file')
    # ### end Alembic commands ###
