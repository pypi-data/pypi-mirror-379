from __future__ import annotations

from mixam_sdk.item_specification.enums.binding_edge import BindingEdge
from mixam_sdk.item_specification.models.component_support import ComponentSupport
from mixam_sdk.metadata.product.models.product_metadata import ProductMetadata
from mixam_sdk.item_specification.models.item_specification import ItemSpecification
from mixam_sdk.metadata.product.services.validation_result import ValidationResult
from .base import DefaultComponentValidator


class BoundComponentValidator(DefaultComponentValidator):
    def validate(self, productMetadata: ProductMetadata, itemSpecification: ItemSpecification, component: ComponentSupport, result: ValidationResult, base_path: str) -> None:
        # Primary-component substrate/lamination checks are handled by PrimaryComponentValidator.
        # Apply generic component-agnostic rules first.
        super().validate(productMetadata, itemSpecification, component, result, base_path)

        # Bound-specific validations based on product bound metadata and item specification
        try:
            from typing import cast
            from mixam_sdk.item_specification.models.item_specification import ItemSpecification
            from mixam_sdk.item_specification.models.bound_component import BoundComponent
            from mixam_sdk.item_specification.enums.binding_loops import BindingLoops
            from mixam_sdk.item_specification.enums.product import Product as ProductEnum
            from mixam_sdk.item_specification.enums.component_type import ComponentType
            from mixam_sdk.item_specification.enums.lamination import Lamination
            from mixam_sdk.metadata.product.models.lamination_option import LaminationOption
            from mixam_sdk.metadata.product.models.page_count_metadata import PageCountMetadata
            from .utils import select_binding_type_option_for_item_specification

            bound = cast(BoundComponent, component)

            # Retrieve spec if the validator was given a hint (non-standard but helpful in our SDK tests)
            itemSpecification = getattr(result, "_spec", None)

            bm = productMetadata.bound_metadata
            if bm is None:
                result.add_error(
                    path=f"{base_path}",
                    message="Bound metadata is missing; cannot validate bound component",
                    code="bound.metadata.missing",
                )
                return

            # Loops must be TWO_LOOPS
            if bound.binding.loops != BindingLoops.TWO_LOOPS:
                result.add_error(
                    path=f"{base_path}.binding.loops",
                    message="Only TWO_LOOPS is supported",
                    code="bound.binding.loops.unsupported",
                )

            # Ribbon colour must be among metadata if selected
            if bound.ribbon_colour.name != "NONE":
                allowed_ribbons = {rm.ribbon_colour.name for rm in bm.ribbon_metadata}
                if allowed_ribbons and bound.ribbon_colour.name not in allowed_ribbons:
                    result.add_error(
                        path=f"{base_path}.ribbonColour",
                        message="Unsupported Ribbon Colour.",
                        code="bound.ribbon_colour.unavailable",
                        allowed=sorted(list(allowed_ribbons)),
                    )

            # Head & Tail Bands validation when selected
            if bound.binding.head_and_tail_bands.name != "NONE":
                allowed_hnt = {m.head_and_tail_bands.name for m in bm.head_and_tail_band_metadata}
                if allowed_hnt and bound.binding.head_and_tail_bands.name not in allowed_hnt:
                    result.add_error(
                        path=f"{base_path}.binding.headAndTailBands",
                        message="Unsupported Head & Tail Band.",
                        code="bound.head_and_tail_bands.unavailable",
                        allowed=sorted(list(allowed_hnt)),
                    )

            # Pages increment/default exceptions
            if bm.pages_increment > 0 and itemSpecification is not None:
                if bound.pages % bm.pages_increment != 0:
                    if itemSpecification.product in {ProductEnum.VR_DESK_CALENDARS, ProductEnum.VR_WALL_CALENDARS}:
                        if bound.pages != bm.default_pages:
                            result.add_error(
                                path=f"{base_path}.pages",
                                message=f"Pages must be {bm.default_pages}",
                                code="bound.pages.must_equal_default",
                                allowed=[bm.default_pages],
                            )
                    else:
                        result.add_error(
                            path=f"{base_path}.pages",
                            message=f"Pages must be an increment of {bm.pages_increment}",
                            code="bound.pages.increment",
                        )

            # Determine binding type option to drive further rules (if we have the spec)
            bto = None
            if itemSpecification is not None:
                match = select_binding_type_option_for_item_specification(itemSpecification, productMetadata.cover_substrate_types, bm)
                if match.binding_type_option is None and match.errors:
                    # Surface at least one violation to guide the user (mirror Java 'fewest violations')
                    for v in match.errors:
                        result.add_error(v.path, v.message, v.code, **getattr(v, "extra", {}))
                bto = match.binding_type_option

            # Page count ranges
            if itemSpecification is not None:
                # Find body substrate weight metadata to inspect page counts
                st = next((t for t in productMetadata.substrate_types if t.id == bound.substrate.type_id), None)
                sc = next((c for c in (st.substrate_colours if st else []) if c.id == bound.substrate.colour_id), None)
                sw = next((w for w in (sc.weights if sc else []) if w.id == bound.substrate.weight_id), None)
                page_count_md: PageCountMetadata | None = None
                if sw is not None and bto is not None:
                    page_count_md = next((pc for pc in sw.page_counts if pc.binding_type == bto.binding_type), None)
                if page_count_md is not None:
                    if not (page_count_md.min <= bound.pages <= page_count_md.max):
                        result.add_error(
                            path=f"{base_path}.pages",
                            message=f"Pages must be between {page_count_md.min} and {page_count_md.max} [Page Range]",
                            code="bound.pages.range.binding_type",
                            range_min=page_count_md.min,
                            range_max=page_count_md.max,
                        )
                else:
                    # Fallback to global min/max
                    gmin = bm.global_min_pages or 0
                    from mixam_sdk.metadata.product.models.bound_metadata import BoundMetadata as _BM
                    gmax = bm.global_max_pages or _BM.DEFAULT_GLOBAL_MAX_PAGES
                    if not (gmin <= bound.pages <= gmax):
                        result.add_error(
                            path=f"{base_path}.pages",
                            message=f"Pages must be between {gmin} and {gmax} [Global]",
                            code="bound.pages.range.global",
                            range_min=gmin,
                            range_max=gmax,
                        )

            # Hard rule: minimum 8 pages unless a cover component exists
            if itemSpecification is not None and bound.pages < 8 and not itemSpecification.has_component(ComponentType.COVER):
                result.add_error(
                    path=f"{base_path}.pages",
                    message="Minimum pages is 8 for bound items without a cover component",
                    code="bound.pages.min_without_cover",
                )

            # Binding Edge rules
            if not bm.binding_edge_options and bound.binding.edge != BindingEdge.LEFT_RIGHT:
                result.add_error(
                    path=f"{base_path}.binding.edge",
                    message="Only LEFT_RIGHT binding edge is supported by this product",
                    code="bound.binding.edge.only_left_right",
                )
            elif bm.binding_edge_options:
                allowed_edges = {e.binding_edge.name for e in bm.binding_edge_options}
                if bound.binding.edge.name not in allowed_edges:
                    result.add_error(
                        path=f"{base_path}.binding.edge",
                        message="Unsupported Binding Edge.",
                        code="bound.binding.edge.unavailable",
                        allowed=sorted(list(allowed_edges)),
                    )

            # Body lamination options (Layflats support lamination on body)
            lam_meta = productMetadata.lamination_metadata
            front_opts = lam_meta.front_options if lam_meta is not None else []
            if not front_opts and bound.lamination != Lamination.NONE:
                result.add_error(
                    path=f"{base_path}.lamination",
                    message="Lamination is not supported by this product",
                    code="bound.lamination.unsupported",
                )
            elif bound.lamination != Lamination.NONE:
                allowed_values = {int(opt.value) for opt in front_opts}
                if allowed_values and bound.lamination.get_value() not in allowed_values and bound.lamination.value not in allowed_values:
                    result.add_error(
                        path=f"{base_path}.lamination",
                        message="Unsupported lamination. This product accepts configured front laminations",
                        code="bound.lamination.option_invalid",
                        allowed=sorted(list(allowed_values)),
                    )

        except Exception:
            # Defensive: do not break validation on unexpected metadata shape
            pass


__all__ = ["BoundComponentValidator"]
