import {styled} from "@mui/material/styles"
import Card from "@mui/material/Card"
import CardContent from "@mui/material/CardContent"
import CardHeader from "@mui/material/CardHeader"
import Collapse from "@mui/material/Collapse"
import IconButton from "@mui/material/IconButton"
import ExpandMoreIcon from "@mui/icons-material/ExpandMore"
import Typography from "@mui/material/Typography"
import {apply_flex} from "./utils"

const ExpandMore = styled((props) => {
  const {expand, ...other} = props;
  return <IconButton {...other} />;
})(({theme}) => ({
  marginLeft: "auto",
  transition: theme.transitions.create("transform", {
    duration: theme.transitions.duration.shortest,
  }),
  variants: [
    {
      props: ({expand}) => !expand,
      style: {
        transform: "rotate(0deg)",
      },
    },
    {
      props: ({expand}) => !!expand,
      style: {
        transform: "rotate(180deg)",
      },
    },
  ],
}))

export function render({model, view}) {
  const [collapsible] = model.useState("collapsible")
  const [collapsed, setCollapsed] = model.useState("collapsed")
  const [elevation] = model.useState("elevation")
  const [header_color] = model.useState("header_color")
  const [header_css_classes] = model.useState("header_css_classes")
  const [header_background] = model.useState("header_background")
  const [hide_header] = model.useState("hide_header")
  const [raised] = model.useState("raised")
  const [square] = model.useState("square")
  const [sx] = model.useState("sx")
  const [title] = model.useState("title")
  const [title_css_classes] = model.useState("title_css_classes")
  const [title_variant] = model.useState("title_variant")
  const [variant] = model.useState("variant")
  const header = model.get_child("header")
  const objects = model.get_child("objects")

  const shouldHideHeader = hide_header || (!model.header && (!title || title.trim() === ""))
  const shouldHideContent = objects.length === 0

  React.useEffect(() => {
    model.on("lifecycle:update_layout", () => {
      objects.map((object, index) => {
        apply_flex(view.get_child_view(model.objects[index]), "column")
      })
    })
  }, [])

  if (model.header) {
    apply_flex(view.get_child_view(model.header), "row")
  }

  return (
    <Card
      elevation={elevation}
      square={square}
      raised={raised}
      variant={variant}
      sx={{display: "flex", flexDirection: "column", width: "100%", height: "100%", ...sx}}
    >
      {!shouldHideHeader && (
        <CardHeader
          action={
            collapsible &&
            <ExpandMore
              expand={!collapsed}
              onClick={() => setCollapsed(!collapsed)}
              aria-expanded={!collapsed}
              aria-label="show more"
            >
              <ExpandMoreIcon />
            </ExpandMore>
          }
          classes={header_css_classes}
          title={model.header ? header : (
            <Typography
              classes={title_css_classes}
              dangerouslySetInnerHTML={{__html: title}}
              sx={{display: "inline-flex", alignItems: "center", gap: "0.25em", fontSize: "1.15rem", fontWeight: 500}}
              variant={title_variant}
            />
          )}
          sx={{
            backgroundColor: header_background,
            color: header_color,
            display: "flex",
            minWidth: 0,
            p: "12px 16px",
            "& .MuiCardHeader-content": {minWidth: 0}
          }}
        />
      )}
      <Collapse
        in={!collapsed}
        timeout="auto"
        unmountOnExit
        sx={{
          flexGrow: 1,
          height: "100%",
          width: "100%",
          "& .MuiCollapse-wrapper": {
            height: "100% !important",
          },
        }}
      >
        {!shouldHideContent && (
          <CardContent
            sx={{
              height: "100%",
              width: "100%",
              display: "flex",
              flexDirection: "column",
              p: shouldHideHeader ? "16px 16px 12px 16px" : "0px 16px 12px 16px",
              "&:last-child": {
                pb: "12px",
              },
            }}
          >
            {objects.map((object, index) => {
              apply_flex(view.get_child_view(model.objects[index]), "column")
              return object
            })}
          </CardContent>
        )}
      </Collapse>
    </Card>
  );
}
