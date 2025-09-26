import TextField from "@mui/material/TextField"
import {render_description} from "./description"

export function render({model, el}) {
  const [autogrow] = model.useState("auto_grow")
  const [color] = model.useState("color")
  const [disabled] = model.useState("disabled")
  const [error_state] = model.useState("error_state")
  const [max_length] = model.useState("max_length")
  const [max_rows] = model.useState("max_rows")
  const [label] = model.useState("label")
  const [placeholder] = model.useState("placeholder")
  const [resizable] = model.useState("resizable")
  const [rows] = model.useState("rows")
  const [value_input, setValueInput] = model.useState("value_input")
  const [_, setValue] = model.useState("value")
  const [variant] = model.useState("variant")
  const [sx] = model.useState("sx")

  el.style.display = "flex"

  let props = {}
  if (autogrow) {
    props = {minRows: rows}
  } else if (rows) {
    props = {rows}
  }

  const resizeMode =
    !resizable ? "none"
      : resizable === "height" ? "vertical"
        : resizable === "width" ? "horizontal"
          : resizable

  const effectiveResize = autogrow ? "none" : resizeMode
  return (
    <TextField
      color={color}
      disabled={disabled}
      error={error_state}
      fullWidth
      inputProps={{maxLength: max_length}}
      label={model.description ? <>{label}{render_description({model, el})}</> : label}
      multiline
      maxRows={max_rows}
      onKeyDown={(e) => {
        if (e.key === "Enter" && e.shiftKey) {
          e.preventDefault()
          setValue(value_input)
        }
      }}
      onBlur={() => setValue(value_input)}
      onChange={(event) => setValueInput(event.target.value)}
      placeholder={placeholder}
      sx={{
        ...sx,
        ...{
          flexGrow: 1,
          "& .MuiInputBase-root": {
            flexGrow: 1,
            alignItems: "stretch",
          },
          "& .MuiInputBase-inputMultiline": {
            resize: effectiveResize,
            height: (resizeMode === "vertical" || resizeMode === "both") ? "unset" : "100% !important",
            overflow: "auto"
          }
        }
      }}
      value={value_input}
      variant={variant}
      {...props}
    />
  )
}
