from pydzn.base_component import BaseComponent
from pydzn.htmx import HtmxSupport
from pydzn.dzn import register_dzn_classes

class LabeledTextarea(BaseComponent, HtmxSupport):
    """
    <label> + <textarea> with dzn-aware classes.
    Supports optional label and label-as-placeholder behavior.
    """

    template_name = "template.html"

    def __init__(
        self,
        *,
        label: str,
        name: str,
        value: str = "",
        placeholder: str = "",
        autocomplete: str = "",
        required: bool = True,
        disabled: bool = False,
        readonly: bool = False,

        # label options
        show_label: bool = True,
        label_as_placeholder: bool = False,

        # dzn classes
        dzn: str = "",
        dzn_label: str = "block mb-2",
        dzn_input: str = "block w-full px-4 py-2 rounded-md border border-subtle",
        dzn_hint: str = "text-muted mt-1",
        dzn_error: str = "text-[red] mt-1",

        # helper/error text
        hint: str = "",
        error: str = "",

        # extra textarea attrs (e.g., {"rows": "6"})
        textarea_attrs: dict | None = None,

        # explicit id for textarea (else auto-generated)
        input_id: str | None = None,

        **wrapper_attrs,  # passes to outer <div>
    ):
        super().__init__(children="", tag="div", dzn=dzn, **wrapper_attrs)

        # Store props
        self.label = label
        self.name = name
        self.value = value
        self.placeholder = placeholder
        self.autocomplete = autocomplete
        self.required = bool(required)
        self.disabled = bool(disabled)
        self.readonly = bool(readonly)

        self.show_label = bool(show_label)
        self.label_as_placeholder = bool(label_as_placeholder)

        # If no visible label and no explicit placeholder, use label as placeholder
        if not self.show_label and (self.label_as_placeholder or not self.placeholder):
            self.placeholder = self.placeholder or self.label

        self.dzn_label = dzn_label or ""
        self.dzn_input = dzn_input or ""
        self.dzn_hint  = dzn_hint or ""
        self.dzn_error = dzn_error or ""

        self.hint  = hint or ""
        self.error = error or ""

        self.textarea_attrs = dict(textarea_attrs or {})
        self.input_id = input_id or (self.id + "-textarea")

        register_dzn_classes(" ".join(
            c for c in [self.dzn_label, self.dzn_input, self.dzn_hint, self.dzn_error] if c
        ))

    def context(self) -> dict:
        return {
            "input_id": self.input_id,
            "label": self.label,
            "name": self.name,
            "value": self.value,
            "placeholder": self.placeholder,
            "autocomplete": self.autocomplete,
            "required": self.required,
            "disabled": self.disabled,
            "readonly": self.readonly,
            "show_label": self.show_label,
            "dzn_label": self.dzn_label,
            "dzn_input": self.dzn_input,
            "dzn_hint": self.dzn_hint,
            "dzn_error": self.dzn_error,
            "hint": self.hint,
            "error": self.error,
            "textarea_attrs": self.textarea_attrs,
        }


class GenericLabeledTextarea(BaseComponent, HtmxSupport):
    """
    <label> + <textarea> with dzn-aware classes.
    Supports optional label and label-as-placeholder behavior.
    """

    template_name = "template.html"

    def __init__(
        self,
        *,
        label: str,
        name: str,
        value: str = "",
        placeholder: str = "",
        autocomplete: str = "",
        required: bool = True,
        disabled: bool = False,
        readonly: bool = False,

        # label options
        show_label: bool = True,
        label_as_placeholder: bool = False,

        # helper/error text
        hint: str = "",
        error: str = "",

        # extra textarea attrs (e.g., {"rows": "6"})
        textarea_attrs: dict | None = None,

        # explicit id for textarea (else auto-generated)
        input_id: str | None = None,

        **wrapper_attrs,  # passes to outer <div>
    ):
        super().__init__(children="", tag="div", **wrapper_attrs)

        # Store props
        self.label = label
        self.name = name
        self.value = value
        self.placeholder = placeholder
        self.autocomplete = autocomplete
        self.required = bool(required)
        self.disabled = bool(disabled)
        self.readonly = bool(readonly)

        self.show_label = bool(show_label)
        self.label_as_placeholder = bool(label_as_placeholder)

        # If no visible label and no explicit placeholder, use label as placeholder
        if not self.show_label and (self.label_as_placeholder or not self.placeholder):
            self.placeholder = self.placeholder or self.label
        
        self.hint  = hint or ""
        self.error = error or ""

        self.textarea_attrs = dict(textarea_attrs or {})
        self.input_id = input_id or (self.id + "-textarea")

    def context(self) -> dict:
        return {
            "input_id": self.input_id,
            "label": self.label,
            "name": self.name,
            "value": self.value,
            "placeholder": self.placeholder,
            "autocomplete": self.autocomplete,
            "required": self.required,
            "disabled": self.disabled,
            "readonly": self.readonly,
            "show_label": self.show_label,
            "hint": self.hint,
            "error": self.error,
            "textarea_attrs": self.textarea_attrs,
        }
