from pydzn.base_component import BaseComponent
from pydzn.variants import VariantSupport
from pydzn.htmx import HtmxSupport
from pydzn.dzn import register_dzn_classes


class Iframe(BaseComponent, HtmxSupport, VariantSupport):
    """
    Renders an Iframe element.
    Expects `template.html`
    """

    def __init__(self, children: str | None = None, src: str = "", dzn: str | None = None, **attrs):
        

        extra_dzn = dzn or attrs.pop("dzn", None)

        # Track base vs runtime classes (like NavItem)
        self._base_dzn = ""
        self._runtime_dzn: list[str] = []

        # Pre-register CSS classes for emission
        if self._base_dzn:
            register_dzn_classes(self._base_dzn)

        super().__init__(children=children, dzn=self._base_dzn, **attrs)

        self.src = src

    def w(self, v: int | str):
        self._add_runtime(f"w-[{v if isinstance(v, str) else str(v)+'px'}]")
        return self

    def h(self, v: int | str):
        self._add_runtime(f"h-[{v if isinstance(v, str) else str(v)+'px'}]")
        return self

    def size(self, wv: int | str, hv: int | str):
        return self.w(wv).h(hv)

    # ---------- internals ----------
    def _merge_all(self) -> str:
        return " ".join([self._base_dzn] + self._runtime_dzn).strip()

    def _add_runtime(self, *classes: str) -> None:
        cls_str = " ".join(c for c in classes if c)
        if not cls_str:
            return
        register_dzn_classes(cls_str)
        self._runtime_dzn.extend(c for c in cls_str.split() if c)
        merged = self._merge_all()
        # BaseComponent should have html_attrs and class merge like NavItem uses
        self.html_attrs["class"] = self._merge_classes(self.html_attrs.get("class", ""), merged)

    def context(self) -> dict:
        return {
            "src": self.src
        }
