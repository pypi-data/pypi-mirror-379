import CircularProgress from "@mui/material/CircularProgress";
import Box from "@mui/material/Box";
import InputAdornment from "@mui/material/InputAdornment"
import IconButton from "@mui/material/IconButton"
import Icon from "@mui/material/Icon"
import SpeedDial from "@mui/material/SpeedDial"
import SpeedDialAction from "@mui/material/SpeedDialAction"
import SendIcon from "@mui/icons-material/Send"
import StopIcon from "@mui/icons-material/Stop"
import SpeedDialIcon from "@mui/material/SpeedDialIcon"
import OutlinedInput from "@mui/material/OutlinedInput"
import {styled} from "@mui/material/styles"
import Chip from "@mui/material/Chip"
import Typography from "@mui/material/Typography"
import CloseIcon from "@mui/icons-material/Close"
import AttachFileIcon from "@mui/icons-material/AttachFile"
import TextareaAutosize from "@mui/material/TextareaAutosize"
import {isFileAccepted, processFilesChunked, apply_flex, waitForRef} from "./utils"

// Map MIME types to Material Icons
const mimeTypeIcons = {
  // Images
  "image/": "image",
  "image/jpeg": "image",
  "image/png": "image",
  "image/gif": "gif_box",
  "image/svg+xml": "image",
  "image/webp": "image",

  // Documents
  "application/pdf": "picture_as_pdf",
  "application/msword": "description",
  "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "description",
  "application/vnd.ms-excel": "table_chart",
  "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "table_chart",
  "application/vnd.ms-powerpoint": "slideshow",
  "application/vnd.openxmlformats-officedocument.presentationml.presentation": "slideshow",

  // Text
  "text/": "article",
  "text/plain": "article",
  "text/html": "html",
  "text/css": "css",
  "text/javascript": "javascript",
  "text/csv": "table_chart",
  "text/markdown": "article",

  // Audio
  "audio/": "audio_file",
  "audio/mpeg": "audio_file",
  "audio/wav": "audio_file",
  "audio/ogg": "audio_file",

  // Video
  "video/": "video_file",
  "video/mp4": "video_file",
  "video/webm": "video_file",
  "video/ogg": "video_file",

  // Archives
  "application/zip": "folder_zip",
  "application/x-rar-compressed": "folder_zip",
  "application/x-7z-compressed": "folder_zip",
  "application/x-tar": "folder_zip",
  "application/gzip": "folder_zip",

  // Code
  "application/json": "code",
  "application/xml": "code",
  "text/xml": "code",

  // Default
  default: "insert_drive_file"
};

const SpinningStopIcon = (props) => {
  return (
    <Box sx={{position: "relative", display: "inline-block", width: 40, height: 40}}>
      {/* Spinning Circular Arc */}
      <CircularProgress
        size={40}
        thickness={4}
        sx={{
          color: `${props.color}.main`,
          animationDuration: "1s",
          strokeLinecap: "round", // Makes the arc smoother
        }}
        value={props.progress}
        variant={props.progress == null ? "indeterminate" : "determinate"}
      />
      {/* Centered Stop Icon */}
      <Box
        sx={{
          position: "absolute",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          backgroundColor: "white",
          borderRadius: "50%",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          width: 25,
          height: 25,
        }}
      >
        <StopIcon color={props.color} sx={{fontSize: 24}} />
      </Box>
    </Box>
  );
};

const HiddenFileInput = styled("input")({
  clip: "rect(0 0 0 0)",
  clipPath: "inset(50%)",
  height: "100%",
  overflow: "hidden",
  position: "absolute",
  bottom: 0,
  left: 0,
  whiteSpace: "nowrap",
  width: "100%",
  opacity: 0,
  cursor: "pointer",
  zIndex: 1,
})

// Format bytes for display
function formatBytes(bytes) {
  if (bytes === 0) { return "0 B" }
  const k = 1024
  const sizes = ["B", "KB", "MB", "GB"]
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return `${parseFloat((bytes / k**i).toFixed(2))} ${sizes[i]}`
}

const CustomInput = React.forwardRef(({filePreview, footerObjects, ...props}, ref) => {
  const inputRef = React.useRef(null);
  React.useImperativeHandle(ref, () => ({
    focus: () => inputRef.current?.focus(),
    blur: () => inputRef.current?.blur(),
    value: inputRef.current?.value,
  }));

  return (
    <Box sx={{alignSelf: "center", width: "100%"}}>
      {filePreview}
      <TextareaAutosize
        ref={inputRef}
        {...props}
        style={{
          ...props.style,
          border: "none",
          outline: "none",
          resize: "none",
          background: "transparent",
          fontFamily: "inherit",
          fontSize: "inherit",
          lineHeight: "inherit",
          width: "100%",
          boxSizing: "border-box",
          paddingTop: "0.5rem",
          paddingBottom: "0.5rem",
        }}
      />
      {footerObjects && footerObjects.length > 0 && (
        <Box
          sx={{
            display: "flex",
            flexDirection: "row",
            flexWrap: "nowrap",
            gap: 1,
            pt: 0,
            pb: 0,
            mb: -1,
            alignItems: "center",
            width: "100%",
            maxWidth: "calc(100% - 16px)",
            overflowX: "auto",
            "&::-webkit-scrollbar": {
              height: "1px",
            },
            "&::-webkit-scrollbar-track": {
              backgroundColor: "transparent",
            },
            "&::-webkit-scrollbar-thumb": {
              backgroundColor: "rgba(0,0,0,0.2)",
              borderRadius: "1px",
            },
          }}
        >
          {footerObjects}
        </Box>
      )}
    </Box>
  );
});

export function render({model, view}) {
  const [accept] = model.useState("accept")
  const [actions] = model.useState("actions")
  const [autogrow] = model.useState("auto_grow")
  const [color] = model.useState("color")
  const [disabled] = model.useState("disabled")
  const [disabled_enter] = model.useState("disabled_enter")
  const [enable_upload] = model.useState("enable_upload")
  const [enter_sends] = model.useState("enter_sends")
  const [error_state] = model.useState("error_state")
  const [loading, setLoading] = model.useState("loading")
  const [max_rows] = model.useState("max_rows")
  const [label] = model.useState("label")
  const [placeholder] = model.useState("placeholder")
  const [rows] = model.useState("rows")
  const [sx] = model.useState("sx")
  const [value_input, setValueInput] = model.useState("value_input")
  const [variant] = model.useState("variant")
  const [isDragOver, setIsDragOver] = React.useState(false)
  const fileInputRef = React.useRef(null)
  const footer_objects = model.get_child("footer_objects")

  const [progress, setProgress] = React.useState(undefined)
  const [file_data, setFileData] = React.useState([])
  const upload_ref = React.useRef(null)

  React.useEffect(() => {
    model.on("msg:custom", (msg) => {
      if (msg.status === "finished") {
        upload_ref.current = msg
      }
    })

    model.on("lifecycle:update_layout", () => {
      footer_objects.map((object, index) => {
        apply_flex(view.get_child_view(model.footer_objects[index]), "row")
      })
    })
  }, [])

  const isSendEvent = (event) => {
    return (event.key === "Enter") && (
      (enter_sends && (!(event.ctrlKey || event.shiftKey))) ||
        (!enter_sends && (event.ctrlKey || event.shiftKey))
    )
  }

  let props = {sx: {width: "100%", height: "100%", ...sx}}
  if (autogrow) {
    props = {minRows: rows}
  } else {
    props = {rows}
  }

  const send = async () => {
    if (disabled) {
      return
    }
    if (file_data.length) {
      let validFiles = file_data
      if (accept) {
        validFiles = Array.from(file_data).filter(file => isFileAccepted(file, accept))
      }
      const count = await processFilesChunked(
        validFiles,
        model,
        model.max_file_size,
        model.max_total_file_size,
        model.chunk_size || 10 * 1024 * 1024,
        setProgress,
        upload_ref
      )
    }
    model.send_msg({type: "input", value: value_input})
    setFileData([])
    setValueInput("")
    await waitForRef(status_ref)
    setProgress(undefined)
  }

  const stop = () => {
    model.send_msg({type: "action", action: "stop"})
  }

  const handleDragEnter = (e) => {
    e.preventDefault()
    e.stopPropagation()
    if (e.dataTransfer.types && e.dataTransfer.types.includes("Files")) {
      setIsDragOver(true)
    }
  }

  const handleDragLeave = (e) => {
    e.preventDefault()
    e.stopPropagation()
    setIsDragOver(false)
  }

  const handleDragOver = (e) => {
    e.preventDefault()
    e.stopPropagation()
    if (e.dataTransfer.types && e.dataTransfer.types.includes("Files")) {
      e.dataTransfer.dropEffect = "copy"
    } else {
      e.dataTransfer.dropEffect = "none"
    }
  }

  const handleDrop = (e) => {
    e.preventDefault()
    e.stopPropagation()
    setIsDragOver(false)

    if (disabled) { return }

    const files = Array.from(e.dataTransfer.files)
    let validFiles = files
    if (accept) {
      validFiles = files.filter(file => isFileAccepted(file, accept))
    }
    setFileData([...file_data, ...validFiles])
  }

  const removeFile = (index) => {
    const newFiles = [...file_data]
    newFiles.splice(index, 1)
    setFileData(newFiles)
  }

  const FilePreview = () => (
    <Box
      sx={{
        display: "flex",
        flexWrap: "wrap",
        gap: 0.5,
        p: 1,
        pb: 0.5,
        width: "100%",
        minHeight: "32px",
        maxHeight: "60px",
        overflowY: "auto",
        alignItems: "center",
        borderBottom: 1,
        borderColor: "divider",
        backgroundColor: "background.paper",
      }}
    >
      {file_data.map((file, index) => (
        <Chip
          key={`${file.name}-${index}`}
          icon={
            <Icon>
              {Object.entries(mimeTypeIcons).find(([type, icon]) =>
                file.type.startsWith(type))?.[1] || mimeTypeIcons.default
              }
            </Icon>
          }
          label={
            <Typography variant="caption" noWrap sx={{maxWidth: "150px"}}>
              {file.name} ({formatBytes(file.size)})
            </Typography>
          }
          onDelete={() => removeFile(index)}
          deleteIcon={<CloseIcon />}
          size="small"
          color={color}
          variant="outlined"
          sx={{height: "24px", mb: "8px"}}
        />
      ))}
    </Box>
  )

  const inputRef = React.useRef(null);

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        width: "100%",
        height: "100%",
        gap: 1,
      }}
    >
      <Box
        sx={{
          position: "relative",
          width: "100%",
          height: "100%",
          ...(isDragOver && {
            "&::after": {
              content: '""',
              position: "absolute",
              top: 0,
              left: 0,
              right: 0,
              bottom: 0,
              backgroundColor: "rgba(0, 0, 0, 0.1)",
              border: "2px dashed",
              borderColor: `${color}.main`,
              borderRadius: 1,
              zIndex: 2,
            }
          })
        }}
        onDragEnter={handleDragEnter}
        onDragLeave={handleDragLeave}
        onDragOver={handleDragOver}
        onDrop={handleDrop}
      >
        {enable_upload && <HiddenFileInput
          ref={fileInputRef}
          type="file"
          multiple
          accept={accept}
          onChange={(event) => {
            if (event.target.files && event.target.files.length > 0) {
              const files = Array.from(event.target.files)
              let validFiles = files
              if (accept) {
                validFiles = files.filter(file => isFileAccepted(file, accept))
              }
              setFileData([...file_data, ...validFiles])
            }
          }}
        />
        }
        <OutlinedInput
          multiline
          color={color}
          disabled={disabled}
          inputComponent={CustomInput}
          inputProps={{
            ref: inputRef,
            filePreview: (enable_upload && file_data.length > 0) ? <FilePreview /> : null,
            footerObjects: footer_objects.map((object, index) => {
              apply_flex(view.get_child_view(model.footer_objects[index]), "row")
              return object
            }),
            value: value_input,
            onChange: (event) => setValueInput(event.target.value),
            onKeyDown: (event) => {
              if (isSendEvent(event)) {
                event.preventDefault()
                send()
              }
            },
            maxRows: max_rows,
            placeholder,
            ...props,
          }}
          placeholder={placeholder}
          startAdornment={
            Object.keys(actions).length > 0 ? (
              <InputAdornment position="start" sx={{alignItems: "end", maxHeight: "35px", mr: "4px", alignSelf: "center"}}>
                <SpeedDial
                  ariaLabel="Actions"
                  disabled={disabled}
                  size="small"
                  FabProps={{size: "small", sx: {width: "35px", height: "35px", minHeight: "35px"}}}
                  icon={<SpeedDialIcon color={color}/>}
                  sx={{zIndex: 1000, ml: "-4px"}}
                >
                  <SpeedDialAction
                    icon={<AttachFileIcon />}
                    tooltipTitle="Attach files"
                    slotProps={{popper: {container: view.container}}}
                    onClick={() => fileInputRef.current?.click()}
                  />
                  {Object.keys(actions).map((action) => (
                    <SpeedDialAction
                      key={action}
                      icon={<Icon>{actions[action].icon}</Icon>}
                      slotProps={{popper: {container: view.container}}}
                      tooltipTitle={actions[action].label || action}
                      onClick={() => model.send_msg({type: "action", action})}
                    />
                  ))}
                </SpeedDial>
              </InputAdornment>
            ) : (enable_upload ? <IconButton color="primary" disabled={disabled} onClick={() => fileInputRef.current?.click()}><AttachFileIcon /></IconButton> : null)
          }
          endAdornment={
            <InputAdornment onClick={() => (disabled_enter || loading) ? stop() : send()} position="end" sx={{mb: "2px", ml: "-4px", alignSelf: "center"}}>
              <IconButton color="primary" disabled={disabled}>
                {(disabled_enter || loading || progress !== undefined) ? <SpinningStopIcon color={color} progress={progress}/> : <SendIcon/>}
              </IconButton>
            </InputAdornment>
          }
          error={error_state}
          label={label}
          variant={variant}
          fullWidth
          sx={{
            ...props.sx,
            p: "8px",
            alignItems: "end",
            position: "relative",
            zIndex: 0,
            width: "100%",
            ".MuiInputBase-root": {
              alignItems: "flex-start",
              padding: (Object.keys(actions).length > 0 || enable_upload) ? "8px" : "8px 8px 8px 16px",
            },
          }}
        />
      </Box>
    </Box>
  )
}
