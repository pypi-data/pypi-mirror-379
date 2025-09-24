from __future__ import annotations

from typing import cast

from mixam_sdk.item_specification.models.component_support import ComponentSupport
from mixam_sdk.item_specification.models.framed_component import FramedComponent
from mixam_sdk.metadata.product.models.product_metadata import ProductMetadata
from mixam_sdk.metadata.product.services.validation_result import ValidationResult
from .base import DefaultComponentValidator


class FramedComponentValidator(DefaultComponentValidator):
    def validate(self, product: ProductMetadata, spec: "ItemSpecification", component: ComponentSupport, result: ValidationResult, base_path: str) -> None:
        # Run generic/base validations first
        super().validate(product, spec, component, result, base_path)

        # Component-specific: frame depth option must be supported by product.framed_metadata
        try:
            framed = cast(FramedComponent, component)  # safe: dispatched for ComponentType.FRAMED
            meta = product.framed_metadata
            if meta is None:
                # No framed metadata -> report as an error per requirement
                result.add_error(
                    path=f"{base_path}.frameDepth",
                    message="Framed metadata is missing; cannot validate frame depth for this product.",
                    code="framed.metadata.missing",
                )
                return
            options = meta.frame_depth_options or []
            allowed = {opt.frame_depth.name for opt in options}
            if allowed and framed.frame_depth.name not in allowed:
                result.add_error(
                    path=f"{base_path}.frameDepth",
                    message="Unsupported frame depth. This product accepts the configured frame depths",
                    code="framed.frame_depth.unavailable",
                    allowed=sorted(list(allowed)),
                )
        except Exception:
            # Be defensive: do not crash validator on metadata shape issues
            pass


__all__ = ["FramedComponentValidator"]
