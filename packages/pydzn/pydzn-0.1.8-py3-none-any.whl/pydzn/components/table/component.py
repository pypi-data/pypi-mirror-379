from __future__ import annotations
from typing import List, Dict, Any, Optional, Iterable
from pydzn.base_component import BaseComponent
from pydzn.variants import VariantSupport
from pydzn.htmx import HtmxSupport
from pydzn.dzn import register_dzn_classes


class Table(VariantSupport, BaseComponent, HtmxSupport):
    """
    Server-rendered Table with:
      - arbitrary columns/rows
      - sortable headers (HTMX)
      - optional toolbar (Export / Add Column)
      - row striping
      - variants/sizes/tones

    Columns: list of dicts like:
      { "key": "id", "label": "ID", "sortable": True, "width": "80px", "align": "left", "dzn": "..." }

    Rows: list[dict], keys match column["key"]. Values can be strings (HTML allowed) or already-rendered HTML.

    Example - Row click - Drawer Open:
    row_click = {
        "url": "/admin/google-reviews/edit",         # endpoint that returns the edit form HTML
        "id_key": "id",                              # which key in each row dict holds the id
        "id_param": "id",                            # query param name to pass (e.g., ?id=123)
        "target": "#google-review-drawer-body",      # where to inject the returned HTML
        "swap": "innerHTML",                         # swap strategy
        "push_url": False,                           # usually false for drawers
        "open_drawer_id": "google-review-drawer",    # which drawer to unhide
    }
    
    """

    template_name = "template.html"

    VARIANTS = {
        "surface":  "flex flex-col gap-2 rounded-lg border border-subtle bg-[white] shadow-sm p-0",
        "minimal":  "flex flex-col gap-2 rounded-md border-0 bg-[transparent] shadow-none p-0",
        "soft":     "flex flex-col gap-2 rounded-lg border border-subtle bg-[rgba(15,23,42,.03)] shadow-sm p-0",
        "outlined": "flex flex-col gap-2 rounded-lg border-2 border-slate-300 bg-[transparent] shadow-none p-0",
        # NEW
        "square-admin": "flex flex-col gap-0 rounded-md border border-slate-300 bg-[white] shadow-none p-0",
    }

    # per-variant internal dzn for inner bits (thead/th/td/toolbar/etc.)
    STYLE_VARIANTS = {
        "square-admin": {
            "toolbar":      "flex items-center justify-between px-3 py-2 border-b border-subtle bg-[white]",
            "thead":        "sticky top-0 bg-[#f6f7f7] border-b border-subtle",
            "th":           "text-left text-[13px]",
            "td":           "text-[13px]",
            "tr":           "border-b border-subtle group",
            "tr_alt":       "bg-[rgba(15,23,42,.03)]",
            "primary":      "font-[600]",
            "row_actions":  "text-[12px] text-muted mt-1 opacity-0 group-hover:opacity-100 transition-[opacity]",
            "search_input": "px-3 py-2 rounded-sm border border-subtle text-[13px]",
            "btn":          "px-3 py-2 rounded-sm border bg-[white] hover:bg-[rgba(15,23,42,.04)] text-[13px]",
            "pager":        "px-3 py-1 rounded-sm border bg-[white] hover:bg-[rgba(15,23,42,.04)]",
            "footer":       "flex items-center justify-between px-3 py-2 border-t border-subtle bg-[white] text-[13px]",
        },
        # sensible defaults used by other variants:
        "_default": {
            "toolbar":"flex items-center justify-between px-3 py-2 border-b border-subtle bg-[white]",
            "thead":  "border-b border-subtle bg-[white]",
            "th":     "text-left",
            "td":     "",
            "tr":     "border-b border-subtle",
            "tr_alt": "bg-[rgba(15,23,42,.03)]",
            "primary":"font-[600]",
            "row_actions":"text-[12px] text-muted mt-1",
            "search_input":"px-3 py-2 rounded-sm border border-subtle",
            "btn":    "px-3 py-2 rounded-sm border bg-[white] hover:bg-[rgba(15,23,42,.04)]",
            "pager":  "px-3 py-1 rounded-sm border bg-[white] hover:bg-[rgba(15,23,42,.04)]",
            "footer": "flex items-center justify-between px-3 py-2 border-t border-subtle bg-[white] text-[13px]",
        }
    }


    # affects cell padding density (used in template via context)
    SIZES = {
        "sm": "px-3 py-2",
        "md": "px-4 py-3",
        "lg": "px-5 py-4",
    }

    # tones to tweak border/header emphasis
    TONES = {
        "neutral": "border-subtle",
        "primary": "border-blue-500",
        "danger":  "border-red-500",
        "success": "border-green-500",
    }

    DEFAULTS = {
        "variant": "surface",
        "size": "md",
        "tone": "neutral",
    }

    def __init__(
        self,
        *,
        columns: List[Dict[str, Any]],
        rows: List[Dict[str, Any]],
        # existing…
        sort_url: Optional[str] = None,
        sort_key: Optional[str] = None,
        sort_dir: str = "asc",
        export_url: Optional[str] = None,
        add_column_url: Optional[str] = None,
        show_toolbar: bool = False,
        striped: bool = False,
        row_click: dict | None = None, # row clickable functionality
        selectable: bool = False,                 # leading checkbox column
        bulk_actions: Optional[List[Dict[str,str]]] = None,  # [{label, value}]
        bulk_action_url: Optional[str] = None,    # POST target of bulk actions
        search_query: str = "",                   # shown in top-right search
        search_action: Optional[str] = None,      # GET/POST URL for search
        primary_key: Optional[str] = None,        # which column gets “title + actions”
        actions_key: str = "__actions_html",      # per-row tiny actions HTML
        sticky_header: bool = True,
        # pagination
        page: int = 1,
        per_page: int = 20,
        total: int = 0,
        # helps with search
        hx_target: Optional[str] = None,
        # variant system
        variant: Optional[str] = None,
        size: Optional[str] = None,
        tone: Optional[str] = None,
        dzn: Optional[str] = None,
        **attrs,
    ):
        self.columns = columns or []
        self.rows = rows or []
        self.sort_url = sort_url
        self.sort_key = sort_key
        self.sort_dir = "desc" if str(sort_dir).lower() == "desc" else "asc"
        self.export_url = export_url
        self.add_column_url = add_column_url
        self.show_toolbar = bool(show_toolbar or export_url or add_column_url)
        self.striped = bool(striped)
        self.hx_target = hx_target

        # Resolve variant/size/tone and capture size padding for cells
        size_key = size if size is not None else self.DEFAULTS.get("size", "md")
        # size dzn to apply on each <td>/<th>
        self._cell_pad_dzn = self.__class__._lookup_variant_piece("sizes", size_key) or "px-4 py-3"

        self.row_click = row_click or None
        self.selectable     = bool(selectable)
        self.bulk_actions   = bulk_actions or []
        self.bulk_action_url= bulk_action_url
        self.search_query   = search_query
        self.search_action  = search_action
        self.primary_key    = primary_key
        self.actions_key    = actions_key
        self.sticky_header  = bool(sticky_header)

        self.page           = max(1, int(page))
        self.per_page       = max(1, int(per_page))
        self.total          = max(0, int(total))

        var_key = (variant or self.DEFAULTS.get("variant") or "surface")
        effective_dzn = self._resolve_variant_dzn(
            variant=variant, size=size, tone=tone, extra_dzn=dzn or attrs.pop("dzn", None)
        )
        self._style = dict(self.STYLE_VARIANTS.get("_default", {}))
        self._style.update(self.STYLE_VARIANTS.get(var_key, {}))

        # use tighter padding for wp-admin feel
        size_key = size if size is not None else self.DEFAULTS.get("size", "md")
        self._cell_pad_dzn = {"sm":"px-3 py-2","md":"px-4 py-3","lg":"px-5 py-4"}.get(
            "sm" if var_key=="wp-admin" else size_key, "px-4 py-3"
        )

        register_dzn_classes(" ".join([
            effective_dzn,
            *self._style.values(),
            self._cell_pad_dzn,
            "w-[100%] sticky top-0 group text-[13px] text-[12px]",
        ]))

        super().__init__(children="", tag="div", dzn=effective_dzn, **attrs)


    def context(self) -> dict:
        ctx = {
            # existing…
            "cell_pad_dzn": self._cell_pad_dzn,
            # expose internal dzn to template
            "d_toolbar": self._style["toolbar"],
            "d_thead":   self._style["thead"],
            "d_th":      self._style["th"],
            "d_td":      self._style["td"],
            "d_tr":      self._style["tr"],
            "d_tr_alt":  self._style["tr_alt"],
            "d_primary": self._style["primary"],
            "d_row_actions": self._style["row_actions"],
            "d_search_input": self._style["search_input"],
            "d_btn":     self._style["btn"],
            "d_pager":   self._style["pager"],
            "d_footer":  self._style["footer"],
        }
        # plus your existing fields (columns, rows, sort, pagination…)
        return {**ctx, **{
            "id": self.id,
            "columns": self.columns,
            "rows": self.rows,
            "sort_url": self.sort_url,
            "sort_key": self.sort_key,
            "sort_dir": self.sort_dir,
            "toggle_dir": "desc" if self.sort_dir == "asc" else "asc",
            "show_toolbar": self.show_toolbar or bool(self.bulk_actions or self.search_action),
            "export_url": self.export_url,
            "add_column_url": self.add_column_url,
            "striped": self.striped,
            "selectable": self.selectable,
            "bulk_actions": self.bulk_actions,
            "bulk_action_url": self.bulk_action_url,
            "search_query": self.search_query,
            "search_action": self.search_action,
            "primary_key": self.primary_key,
            "actions_key": self.actions_key,
            "page": self.page, "per_page": self.per_page, "total": self.total,
            "pages": (self.total + self.per_page - 1)//self.per_page if self.total else 1,
            "hx_target": self.hx_target,
            "row_click": self.row_click,
        }}