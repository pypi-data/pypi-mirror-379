from __future__ import annotations

from mixam_sdk.item_specification.enums.component_type import ComponentType
from mixam_sdk.item_specification.models.component_support import ComponentSupport
from mixam_sdk.item_specification.models.item_specification import ItemSpecification
from mixam_sdk.metadata.product.models.product_metadata import ProductMetadata
from mixam_sdk.metadata.product.services.validation_result import ValidationResult
from .base import DefaultComponentValidator


class DustJacketComponentValidator(DefaultComponentValidator):
    def validate(self, productMetadata: ProductMetadata, itemSpecification: ItemSpecification, component: ComponentSupport, result: ValidationResult, base_path: str) -> None:

        super().validate(productMetadata, itemSpecification, component, result, base_path)

        try:
            from typing import cast
            from mixam_sdk.item_specification.models.dust_jacket_component import DustJacketComponent
            from mixam_sdk.item_specification.enums.flap_width import FlapWidth
            from mixam_sdk.item_specification.enums.lamination import Lamination
            from mixam_sdk.metadata.product.models.validators.utils import select_binding_type_option_for_item_specification

            dj = cast(DustJacketComponent, component)

            try:
                if itemSpecification.has_component(ComponentType.BOUND):
                    match = select_binding_type_option_for_item_specification(itemSpecification, productMetadata.cover_substrate_types, productMetadata.bound_metadata)
                    bto = match.binding_type_option
                    if bto is not None and not bto.supports_dust_jacket:
                        result.add_error(
                            path=f"{base_path}",
                            message="Dust Jackets are not supported by this binding type",
                            code="bound.dust_jacket.unsupported",
                        )
            except Exception:
                pass

            # Colours allowed for dust jacket
            try:
                allowed_dj_colours = {o.colours.name for o in productMetadata.colours_metadata.jacket_colours_options}
                if allowed_dj_colours and dj.colours.name not in allowed_dj_colours:
                    result.add_error(
                        path=f"{base_path}.colours",
                        message="Unsupported colour.",
                        code="dust_jacket.colours.unavailable",
                        allowed=sorted(list(allowed_dj_colours)),
                    )
            except Exception:
                pass

            # Lamination options for dust jacket
            try:
                lam_meta = productMetadata.lamination_metadata
                dj_opts = lam_meta.dust_jacket_options if lam_meta is not None else []
                if not dj_opts and dj.lamination != Lamination.NONE:
                    result.add_error(
                        path=f"{base_path}.lamination",
                        message="This product does not support lamination",
                        code="dust_jacket.lamination.unsupported",
                    )
                elif dj.lamination != Lamination.NONE:
                    allowed_vals = {int(opt.value) for opt in dj_opts}
                    if allowed_vals and dj.lamination.get_value() not in allowed_vals and dj.lamination.value not in allowed_vals:
                        result.add_error(
                            path=f"{base_path}.lamination",
                            message="Unsupported lamination. This product accepts configured dust jacket laminations",
                            code="dust_jacket.lamination.option_invalid",
                            allowed=sorted(list(allowed_vals)),
                        )
            except Exception:
                pass

            # Foiling support for dust jacket
            try:
                if dj.foiling.has_foiling() and not productMetadata.foiling_metadata.dust_jacket_foiling:
                    result.add_error(
                        path=f"{base_path}.foiling",
                        message="Foiling is not supported by this product",
                        code="dust_jacket.foiling.unsupported",
                    )
            except Exception:
                pass

            # If flapWidth is CUSTOM then customFlapWidth must be provided
            if dj.flap_width == FlapWidth.CUSTOM:
                if dj.custom_flap_width is None:
                    result.add_error(
                        path=f"{base_path}.customFlapWidth",
                        message="CustomFlapWidth must be set when FlapWidth is CUSTOM",
                        code="dust_jacket.custom_flap_width.required",
                    )
        except Exception:
            # Defensive: don't crash on metadata/model discrepancies
            pass


__all__ = ["DustJacketComponentValidator"]
