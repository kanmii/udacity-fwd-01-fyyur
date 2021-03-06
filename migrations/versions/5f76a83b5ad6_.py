"""empty message

Revision ID: 5f76a83b5ad6
Revises: ed12c59ab0d1
Create Date: 2020-05-17 11:04:34.259093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5f76a83b5ad6"
down_revision = "ed12c59ab0d1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("artist", sa.Column("seeking_description", sa.Text(), nullable=True))
    op.add_column("artist", sa.Column("seeking_venue", sa.Boolean(), nullable=False))
    op.add_column("artist", sa.Column("website", sa.String(length=120), nullable=True))
    op.alter_column("artist", "name", existing_type=sa.VARCHAR(), nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("artist", "name", existing_type=sa.VARCHAR(), nullable=True)
    op.drop_column("artist", "website")
    op.drop_column("artist", "seeking_venue")
    op.drop_column("artist", "seeking_description")
    # ### end Alembic commands ###
