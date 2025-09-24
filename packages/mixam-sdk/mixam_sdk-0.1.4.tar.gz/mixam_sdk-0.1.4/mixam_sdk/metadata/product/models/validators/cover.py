from __future__ import annotations

from mixam_sdk.item_specification.models.component_support import ComponentSupport
from mixam_sdk.metadata.product.models.product_metadata import ProductMetadata
from mixam_sdk.metadata.product.services.validation_result import ValidationResult
from .base import DefaultComponentValidator


class CoverComponentValidator(DefaultComponentValidator):
    def validate(self, product: ProductMetadata, spec: "ItemSpecification", component: ComponentSupport, result: ValidationResult, base_path: str) -> None:
        # Run generic rules first
        super().validate(product, spec, component, result, base_path)
        # Substrate combination validation against cover_substrate_types
        try:
            st = next((t for t in product.cover_substrate_types if t.id == component.substrate.type_id), None)
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
                        f"Invalid substrate combination for cover. Type ID: {component.substrate.type_id}, "
                        f"Colour ID: {component.substrate.colour_id}, Weight ID: {component.substrate.weight_id}"
                    ),
                    code="substrate.combo.invalid.cover",
                )
        except Exception:
            pass
        # Lamination rules using cover substrates
        try:
            from mixam_sdk.item_specification.interfaces.component_protocol import LaminatedComponent as ILaminatedComponent
            from mixam_sdk.item_specification.enums.lamination import Lamination
            if isinstance(component, ILaminatedComponent) and component.lamination != Lamination.NONE:
                st = next((t for t in product.cover_substrate_types if t.id == component.substrate.type_id), None)
                if st is None or not st.allow_lamination:
                    result.add_error(
                        path=f"{base_path}.lamination",
                        message="Unsupported lamination for cover. Specified substrate type does not support lamination.",
                        code="lamination.substrate_type_unsupported.cover",
                    )
                else:
                    try:
                        sc = next((c for c in st.substrate_colours if c.id == component.substrate.colour_id), None)
                        sw = next((w for w in sc.weights if w.id == component.substrate.weight_id), None) if sc else None
                        if sw is not None and not sw.supports_lamination:
                            result.add_error(
                                path=f"{base_path}.lamination",
                                message="Lamination is not supported for this cover substrate weight.",
                                code="lamination.substrate_weight_unsupported.cover",
                            )
                    except Exception:
                        pass
        except Exception:
            pass
        # Cover colours validation based on selected BindingTypeOption
        try:
            from mixam_sdk.item_specification.models.cover_component import CoverComponent
            from mixam_sdk.metadata.product.models.validators.utils import select_binding_type_option_for_item_specification
            from typing import cast

            cover = cast(CoverComponent, component)
            match = select_binding_type_option_for_item_specification(spec, product.cover_substrate_types, product.bound_metadata)
            bto = match.binding_type_option
            if bto is not None:
                # Outer colours
                outer_options = bto.separate_cover_outer_colours_options
                allowed_outer = {o.colours.name for o in outer_options}
                if allowed_outer and cover.colours.name not in allowed_outer:
                    result.add_error(
                        path=f"{base_path}.colours",
                        message="Unsupported colour (outer).",
                        code="cover.outer_colours.unavailable",
                        allowed=sorted(list(allowed_outer)),
                    )
                # Inner colours with SAME_AS_FRONT handling
                inner_options = bto.separate_cover_inner_colours_options
                same_as_front = any(o.same_as_front for o in inner_options)
                if same_as_front:
                    if cover.back_colours.name not in {cover.colours.name, "NONE"}:
                        result.add_error(
                            path=f"{base_path}.backColours",
                            message="Unsupported back colour (inner). Must match front or be NONE",
                            code="cover.inner_colours.same_as_front_required",
                        )
                else:
                    allowed_inner = {o.colours.name for o in inner_options}
                    if allowed_inner and cover.back_colours.name not in allowed_inner:
                        result.add_error(
                            path=f"{base_path}.backColours",
                            message="Unsupported back colour (inner).",
                            code="cover.inner_colours.unavailable",
                            allowed=sorted(list(allowed_inner)),
                        )
        except Exception:
            # Defensive: never crash due to metadata shape or missing bound metadata
            pass


__all__ = ["CoverComponentValidator"]
