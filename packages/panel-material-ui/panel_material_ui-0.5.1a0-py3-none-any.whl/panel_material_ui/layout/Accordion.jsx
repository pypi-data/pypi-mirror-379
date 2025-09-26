import Accordion from "@mui/material/Accordion"
import AccordionSummary from "@mui/material/AccordionSummary"
import AccordionDetails from "@mui/material/AccordionDetails"
import ExpandMoreIcon from "@mui/icons-material/ExpandMore"
import Typography from "@mui/material/Typography"

export function render({model}) {
  const [active, setActive] = model.useState("active")
  const [active_header_background] = model.useState("active_header_background")
  const [active_header_color] = model.useState("active_header_color")
  const [disabled] = model.useState("disabled")
  const [disable_gutters] = model.useState("disable_gutters")
  const [elevation] = model.useState("elevation")
  const [header_background] = model.useState("header_background")
  const [header_color] = model.useState("header_color")
  const [names] = model.useState("_names")
  const [toggle] = model.useState("toggle")
  const [sx] = model.useState("sx")
  const [square] = model.useState("square")
  const [title_variant] = model.useState("title_variant")
  const [variant] = model.useState("variant")
  const headers = model.get_child("_headers")
  const objects = model.get_child("objects")

  const handle_expand = (index) => () => {
    let newActive
    if (active.includes(index)) {
      newActive = active.filter((v) => v != index)
    } else if (toggle) {
      newActive = [index]
    } else {
      newActive = [...active]
      newActive.push(index)
    }
    setActive(newActive)
  }

  return (
    <>
      { objects.map((obj, index) => {
        return (
          <Accordion
            defaultExpanded={active.includes(index)}
            disabled={disabled.includes(index)}
            disableGutters={disable_gutters}
            elevation={elevation}
            expanded={active.includes(index)}
            key={`accordion-${index}`}
            square={square}
            sx={sx}
            variant={variant}
          >
            <AccordionSummary
              expandIcon={<ExpandMoreIcon />}
              onClick={handle_expand(index)}
              sx={{
                backgroundColor: active.includes(index) ? active_header_background || header_background : header_background,
                color: active.includes(index) ? active_header_color || header_color : header_color,
                "& .MuiAccordionSummary-content.Mui-expanded": {margin: "12px 0"}
              }}
            >
              {names[index] ? (
                <Typography className="title" variant={title_variant} sx={{display: "inline-flex", alignItems: "center", gap: "0.25em"}} dangerouslySetInnerHTML={{__html: names[index]}} />
              ) : headers[index]}
            </AccordionSummary>
            <AccordionDetails sx={{p: "0 12px", "&.MuiAccordionDetails-root": {p: "0 calc(2 * var(--mui-spacing))"}}}>{obj}</AccordionDetails>
          </Accordion>
        )
      }) }
    </>
  );
}
