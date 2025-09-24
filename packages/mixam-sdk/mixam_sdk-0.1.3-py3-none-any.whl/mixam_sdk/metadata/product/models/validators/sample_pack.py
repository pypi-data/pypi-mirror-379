from __future__ import annotations

from mixam_sdk.item_specification.models.component_support import ComponentSupport
from mixam_sdk.metadata.product.models.product_metadata import ProductMetadata
from mixam_sdk.metadata.product.services.validation_result import ValidationResult
from .base import DefaultComponentValidator


class SamplePackComponentValidator(DefaultComponentValidator):
    def validate(self, product: ProductMetadata, spec: "ItemSpecification", component: ComponentSupport, result: ValidationResult, base_path: str) -> None:
        # Sample Pack specific rules are not modeled; apply only base validations
        super().validate(product, spec, component, result, base_path)


__all__ = ["SamplePackComponentValidator"]
