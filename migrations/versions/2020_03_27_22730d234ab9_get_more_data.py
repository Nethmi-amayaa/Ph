"""Get more data

Revision ID: 22730d234ab9
Revises: 20df3809e96b
Create Date: 2020-03-27 12:22:49.989569

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "22730d234ab9"
down_revision = "20df3809e96b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "movie",
        sa.Column("categories", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    )
    op.add_column(
        "movie",
        sa.Column("tags", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("movie", "tags")
    op.drop_column("movie", "categories")
    # ### end Alembic commands ###
