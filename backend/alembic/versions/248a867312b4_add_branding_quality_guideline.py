"""Add branding quality guideline

Revision ID: 248a867312b4
Revises: e87774655843
Create Date: 2024-02-19 00:31:43.064367

"""

import datetime
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from app.models import Guideline, GuidelineCategory

# revision identifiers, used by Alembic.
revision = "248a867312b4"
down_revision = "e87774655843"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.bulk_insert(
        sa.table(
            "guideline_category",
            sa.Column("id", sa.String(), nullable=False),
            sa.Column("order", sa.Integer(), nullable=False),
        ),
        [
            {"id": "branding", "order": 2},
        ],
    )

    op.bulk_insert(
        sa.table(
            "guideline",
            sa.Column("id", sa.String(), nullable=False),
            sa.Column("url", sa.String(), nullable=False),
            sa.Column("needed_to_pass_since", sa.Date(), nullable=False),
            sa.Column("read_only", sa.Boolean(), nullable=False),
            sa.Column("guideline_category_id", sa.String(), nullable=False),
            sa.Column("show_on_fullscreen_app", sa.Boolean(), nullable=False),
            sa.Column("order", sa.Integer(), nullable=False),
        ),
        [
            {
                "id": "branding-has-primary-brand-colors",
                "url": "https://docs.flathub.org/docs/for-app-authors/metainfo-guidelines/quality-guidelines#has-primary-brand-colors",
                "needed_to_pass_since": datetime.datetime(2024, 3, 1),
                "read_only": True,
                "guideline_category_id": "branding",
                "show_on_fullscreen_app": True,
                "order": 1,
            },
            {
                "id": "branding-good-primary-brand-colors",
                "url": "https://docs.flathub.org/docs/for-app-authors/metainfo-guidelines/quality-guidelines#good-brand-colors",
                "needed_to_pass_since": datetime.datetime(2024, 3, 1),
                "read_only": False,
                "guideline_category_id": "branding",
                "show_on_fullscreen_app": True,
                "order": 2,
            },
        ],
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    sa.delete(Guideline).where(Guideline.id == "branding-has-primary-brand-colors")
    sa.delete(Guideline).where(Guideline.id == "branding-good-primary-brand-colors")

    sa.delete(GuidelineCategory).where(GuidelineCategory.id == "branding")
    # ### end Alembic commands ###