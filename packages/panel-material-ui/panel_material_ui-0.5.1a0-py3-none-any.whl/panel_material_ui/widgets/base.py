from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

import param
from panel._param import Margin
from panel.widgets.base import WidgetBase

from ..base import ESMTransform, MaterialComponent

if TYPE_CHECKING:
    T = TypeVar('T')


class TooltipTransform(ESMTransform):
    """
    TooltipTransform wraps a Material UI widget with a tooltip that displays a description.

    This transform is used to provide additional context or help to users when they hover over a widget.
    """

    _transform = """\
import Icon from "@mui/material/Icon";
import Tooltip from "@mui/material/Tooltip";

{esm}

function {output}(props, ref) {{
  const [description] = props.model.useState("description")
  const [description_delay] = props.model.useState("description_delay")

  const Wrapped{input} = React.forwardRef({input})
  return (description ? (
    <Tooltip
      title={{description}}
      arrow
      enterDelay={{description_delay}}
      enterNextDelay={{description_delay}}
      placement="right"
      slotProps={{{{ popper: {{ container: props.el }} }}}}
    >
      <Wrapped{input} {{...props}}/>
    </Tooltip>) : <{input} {{...props}}/>
  )
}}
"""


class MaterialWidget(MaterialComponent, WidgetBase):
    """
    MaterialWidget is a base class for all Material UI widgets.

    Example
    -------
    >>> MaterialWidget(label='My Widget', description='Helpful info')
    """

    description = param.String(default="", doc="Tooltip text to display when hovering over the widget.")
    disabled = param.Boolean(default=False, doc="Whether the widget is disabled.")
    label = param.String(default="", doc="The label for the widget.")
    margin = Margin(default=10, doc="Margin around the widget.")
    width = param.Integer(default=300, bounds=(0, None), allow_None=True, doc="Width of the widget.")

    __abstract = True

    def __init__(self, **params):
        if 'label' not in params and 'name' in params:
            params['label'] = params['name']
        super().__init__(**params)

    def _process_param_change(self, params):
        description = params.pop("description", None)
        icon = params.pop("icon", None)
        label = params.pop("label", None)
        props = MaterialComponent._process_param_change(self, params)
        if icon:
            props["icon"] = icon
        if label:
            props["label"] = label
        if description:
            props["description"] = description
        return props

    @classmethod
    def from_param(cls: type[T], parameter: param.Parameter, **params) -> T:
        """
        Construct a widget from a Parameter and link the two
        bi-directionally.

        Parameters
        ----------
        parameter: param.Parameter
          A parameter to create the widget from.

        Returns
        -------
        Widget instance linked to the supplied parameter
        """
        widget = super().from_param(parameter, **params)
        if isinstance(parameter.owner, MaterialComponent) and isinstance(parameter.name, str):
            widget.jslink(parameter.owner, value=parameter.name)
        return widget
