from __future__ import annotations

from typing import cast

from mixam_sdk.item_specification.models.component_support import ComponentSupport
from mixam_sdk.metadata.product.models.product_metadata import ProductMetadata
from mixam_sdk.metadata.product.services.validation_result import ValidationResult
from .base import DefaultComponentValidator


class FlatComponentValidator(DefaultComponentValidator):
    def validate(self, product: ProductMetadata, spec: "ItemSpecification", component: ComponentSupport, result: ValidationResult, base_path: str) -> None:
        # Primary-component substrate/lamination checks are handled by PrimaryComponentValidator.
        # Apply only generic component-agnostic rules here.
        super().validate(product, spec, component, result, base_path)

        # Flat-specific: rounded corners rule based on product.rounded_corners (Trilean)
        try:
            from mixam_sdk.metadata.product.enums.trilean import Trilean
            from mixam_sdk.item_specification.models.flat_component import FlatComponent

            flat = cast(FlatComponent, component)  # safe: dispatched by ComponentType.FLAT
            setting = product.rounded_corners
            if setting == Trilean.REQUIRED:
                if not flat.round_corners:
                    result.add_error(
                        path=f"{base_path}.roundCorners",
                        message="This product requires rounded corners",
                        code="flat.rounded_corners.required",
                    )
            elif setting == Trilean.UNAVAILABLE:
                if flat.round_corners:
                    result.add_error(
                        path=f"{base_path}.roundCorners",
                        message="This product does not support rounded corners",
                        code="flat.rounded_corners.unavailable",
                    )
            # OPTIONAL/LBS_TEXT -> no additional validation
        except Exception:
            pass


__all__ = ["FlatComponentValidator"]
