from __future__ import annotations

from mixam_sdk.item_specification.models.component_support import ComponentSupport
from mixam_sdk.metadata.product.models.product_metadata import ProductMetadata
from mixam_sdk.metadata.product.services.validation_result import ValidationResult
from .base import DefaultComponentValidator


class EnvelopeComponentValidator(DefaultComponentValidator):
    def validate(self, product: ProductMetadata, spec: "ItemSpecification", component: ComponentSupport, result: ValidationResult, base_path: str) -> None:
        super().validate(product, spec, component, result, base_path)
        # Envelope components use envelope_substrate_types for substrate validation
        try:
            st = next((t for t in product.envelope_substrate_types if t.id == component.substrate.type_id), None)
            valid_combo = False
            if st is not None:
                sc = next((c for c in st.substrate_colours if c.id == component.substrate.colour_id), None)
                if sc is not None:
                    sw = next((w for w in sc.weights if w.id == component.substrate.weight_id), None)
                    valid_combo = sw is not None
            if not valid_combo:
                result.add_error(
                    path=f"{base_path}.substrate",
                    message=(
                        f"Invalid substrate combination for envelope. Type ID: {component.substrate.type_id}, "
                        f"Colour ID: {component.substrate.colour_id}, Weight ID: {component.substrate.weight_id}"
                    ),
                    code="substrate.combo.invalid.envelope",
                )
        except Exception:
            pass
        # Lamination rules using envelope substrates
        try:
            from mixam_sdk.item_specification.interfaces.component_protocol import LaminatedComponent as ILaminatedComponent
            from mixam_sdk.item_specification.enums.lamination import Lamination
            if isinstance(component, ILaminatedComponent) and component.lamination != Lamination.NONE:
                st = next((t for t in product.envelope_substrate_types if t.id == component.substrate.type_id), None)
                if st is None or not st.allow_lamination:
                    result.add_error(
                        path=f"{base_path}.lamination",
                        message="Unsupported lamination for envelope. Specified substrate type does not support lamination.",
                        code="lamination.substrate_type_unsupported.envelope",
                    )
                else:
                    try:
                        sc = next((c for c in st.substrate_colours if c.id == component.substrate.colour_id), None)
                        sw = next((w for w in sc.weights if w.id == component.substrate.weight_id), None) if sc else None
                        if sw is not None and not sw.supports_lamination:
                            result.add_error(
                                path=f"{base_path}.lamination",
                                message="Lamination is not supported for this envelope substrate weight.",
                                code="lamination.substrate_weight_unsupported.envelope",
                            )
                    except Exception:
                        pass
        except Exception:
            pass


__all__ = ["EnvelopeComponentValidator"]
