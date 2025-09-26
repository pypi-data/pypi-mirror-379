import InputLabel from "@mui/material/InputLabel"
import FormControl from "@mui/material/FormControl"
import Select from "@mui/material/Select"
import OutlinedInput from "@mui/material/OutlinedInput"
import FilledInput from "@mui/material/FilledInput"
import Input from "@mui/material/Input"
import {render_description} from "./description"

export function render({model, view, el}) {
  const [color] = model.useState("color")
  const [disabled] = model.useState("disabled")
  const [label] = model.useState("label")
  const [max_items] = model.useState("max_items")
  const [options] = model.useState("options")
  const [value, setValue] = model.useState("value")
  const [variant] = model.useState("variant")
  const [sx] = model.useState("sx")

  const handleChange = (event) => {
    const {options} = event.target
    const newSelections = []
    for (let i = 0, l = options.length; i < l; i += 1) {
      if (options[i].selected) {
        newSelections.push(options[i].value)
      }
    }
    if (!max_items) {
      setValue(newSelections)
      return
    }

    const added = newSelections.find(item => !value.includes(item));
    if (added) {
      const newValue = [...value, added];
      if (max_items && newValue.length > max_items) {
        newValue.shift();
      }
      setValue(newValue);
    } else {
      setValue(newSelections);
    }
  }

  const spacer = model.description ? "\u00A0" : ""
  const label_spacer = label ? label+spacer : null

  const inputId = `select-multiple-native-${model.id}`
  return (
    <FormControl disabled={disabled} fullWidth variant={variant}>
      {label &&
        <InputLabel id={`select-multiple-label-${model.id}`} shrink htmlFor={inputId}>
          {label}
          {model.description ? render_description({model, el, view}) : null}
        </InputLabel>
      }
      <Select
        color={color}
        input={variant === "outlined" ?
          <OutlinedInput id={inputId} label={label_spacer}/> :
          variant === "filled" ?
            <FilledInput id={inputId} label={label_spacer}/> :
            <Input id={inputId} label={label_spacer}/>
        }
        labelId={`select-multiple-label-${model.id}`}
        multiple
        native
        onChange={handleChange}
        sx={sx}
        value={value}
      >
        {options.map((name) => (
          <option
            key={name}
            value={name}
          >
            {name}
          </option>
        ))}
      </Select>
    </FormControl>
  );
}
