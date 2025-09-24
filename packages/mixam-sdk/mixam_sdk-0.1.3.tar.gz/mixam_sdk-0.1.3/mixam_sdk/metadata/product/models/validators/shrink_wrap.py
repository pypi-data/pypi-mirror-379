from __future__ import annotations

from .base import DefaultComponentValidator


class ShrinkWrapComponentValidator(DefaultComponentValidator):
    def validate(self, product: ProductMetadata, spec: "ItemSpecification", component: ComponentSupport, result: ValidationResult, base_path: str) -> None:
        super().validate(product, spec, component, result, base_path)


__all__ = ["ShrinkWrapComponentValidator"]
