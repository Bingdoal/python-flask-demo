from alembic import op
import sqlalchemy as sa

revision = '0001_create_user_table'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('user',
                    sa.Column('id', sa.BIGINT(), primary_key=True),
                    sa.Column('name', sa.String(20), nullable=False),
                    sa.Column('email', sa.String(64), nullable=False),
                    sa.Column('password', sa.Text(), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table("user")
