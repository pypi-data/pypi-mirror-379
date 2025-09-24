from __future__ import annotations

from typing import cast

from mixam_sdk.item_specification.enums.orientation import Orientation
from mixam_sdk.item_specification.models.component_support import ComponentSupport
from mixam_sdk.item_specification.models.folded_component import FoldedComponent
from mixam_sdk.metadata.product.models.product_metadata import ProductMetadata
from mixam_sdk.metadata.product.services.validation_result import ValidationResult
from .base import DefaultComponentValidator


class FoldedComponentValidator(DefaultComponentValidator):
    def validate(self, product: ProductMetadata, spec: "ItemSpecification", component: ComponentSupport, result: ValidationResult, base_path: str) -> None:
        # Generic checks first
        super().validate(product, spec, component, result, base_path)

        try:
            folded = cast(FoldedComponent, component)  # safe: dispatched for ComponentType.FOLDED

            # Find matching StandardSize metadata by format and standard size
            ss = next(
                (
                    s for s in product.standard_sizes
                    if s.format == folded.format and s.standard_size == folded.standard_size
                ),
                None,
            )
            if ss is None or ss.folding_options is None:
                result.add_error(
                    path=f"{base_path}.standardSize",
                    message="Unsupported format & standard size combination for folding",
                    code="folded.standard_size.combo.invalid",
                )
                return

            folding_options = ss.folding_options

            # Select options based on orientation
            if folded.orientation == Orientation.PORTRAIT:
                options = folding_options.portrait_options
                orient_key = "portrait"
            else:
                options = folding_options.landscape_options
                orient_key = "landscape"

            # Validate simple fold is allowed in this orientation
            allowed_folds = {opt.simple_fold.name for opt in options}
            if allowed_folds and folded.simple_fold.name not in allowed_folds:
                result.add_error(
                    path=f"{base_path}.simpleFold",
                    message="Unsupported simple fold for this size & orientation",
                    code="folded.simple_fold.unavailable",
                    allowed=sorted(list(allowed_folds)),
                    orientation=orient_key,
                )
                return

            # Validate sides allowed for the selected simple fold
            selected = next((opt for opt in options if opt.simple_fold == folded.simple_fold), None)
            if selected is None:
                # Defensive: if not found due to data mismatch, already handled above
                return
            if selected.available_sides and folded.sides not in selected.available_sides:
                result.add_error(
                    path=f"{base_path}.sides",
                    message="Unsupported number of sides for this size & orientation",
                    code="folded.sides.unavailable",
                    allowed=sorted(list(selected.available_sides)),
                    orientation=orient_key,
                )
        except Exception:
            # Be defensive: never crash validator due to unexpected metadata shape
            pass


__all__ = ["FoldedComponentValidator"]
