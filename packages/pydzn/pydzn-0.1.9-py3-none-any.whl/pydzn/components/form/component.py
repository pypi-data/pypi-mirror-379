# components/common/form/__init__.py
from pydzn.base_component import BaseComponent
from pydzn.htmx import HtmxSupport
from pydzn.dzn import register_dzn_classes


class Form(BaseComponent, HtmxSupport):
    """
    Minimal form that supports dzn classes, HTMX attrs, and a built-in feedback slot.
    """

    template_name = "template.html"

    def __init__(
        self,
        children: str = "",
        *,
        action: str = "",
        method: str = "post",
        feedback: str = "",                 # initial HTML (error/success) to render
        feedback_id: str | None = None,     # optional; defaults to "<form-id>-feedback"
        dzn_feedback: str = "p-4",          # classes for the feedback container
        feedback_pos: str = "after",        # "before" | "after" (relative to children)
        dzn: str = "",
        **attrs,
    ):
        attrs.setdefault("action", action)
        attrs.setdefault("method", method.lower())

        super().__init__(children=children, tag="form", dzn=dzn, **attrs)

        self._feedback         = feedback or ""
        self._feedback_id      = feedback_id or (self.id + "-feedback")
        self._dzn_feedback     = dzn_feedback or ""
        self._feedback_pos     = "before" if feedback_pos == "before" else "after"

        register_dzn_classes(self._dzn_feedback)

    # handy for hx-target in calling code
    @property
    def feedback_id(self) -> str:
        return self._feedback_id

    def context(self) -> dict:
        return {
            "feedback": self._feedback,
            "feedback_id": self._feedback_id,
            "dzn_feedback": self._dzn_feedback,
            "feedback_pos": self._feedback_pos,
        }



class GenericForm(BaseComponent, HtmxSupport):
    """
    Minimal form that supports HTMX attrs and a built-in feedback slot.
    """

    template_name = "template.html"

    def __init__(
        self,
        children: str = "",
        *,
        action: str = "",
        method: str = "post",
        feedback: str = "",                 # initial HTML (error/success) to render
        feedback_id: str | None = None,     # optional; defaults to "<form-id>-feedback"
        feedback_pos: str = "after",        # "before" | "after" (relative to children)
        **attrs,
    ):
        attrs.setdefault("action", action)
        attrs.setdefault("method", method.lower())

        super().__init__(children=children, tag="form", **attrs)

        self._feedback         = feedback or ""
        self._feedback_id      = feedback_id or (self.id + "-feedback")
        self._feedback_pos     = "before" if feedback_pos == "before" else "after"

    # handy for hx-target in calling code
    @property
    def feedback_id(self) -> str:
        return self._feedback_id

    def context(self) -> dict:
        return {
            "feedback": self._feedback,
            "feedback_id": self._feedback_id,
            "feedback_pos": self._feedback_pos,
        }