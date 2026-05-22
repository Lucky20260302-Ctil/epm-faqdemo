import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

const QUALITY_CONFIG = {
  complete: {
    label: "資訊完整",
    icon: "✓",
    color: "#2da44e",
    bg: "#dafbe1",
    darkBg: "#1a3a1f",
  },
  partial: {
    label: "部分資訊",
    icon: "!",
    color: "#bf8700",
    bg: "#fff8c5",
    darkBg: "#3a2e00",
  },
  stub: {
    label: "資訊不足",
    icon: "✗",
    color: "#cf222e",
    bg: "#ffebe9",
    darkBg: "#3d1518",
  },
}

const QualityBadge: QuartzComponent = ({ fileData, displayClass }: QuartzComponentProps) => {
  const quality = (fileData.frontmatter?.quality as string) || ""
  if (!quality || !QUALITY_CONFIG[quality as keyof typeof QUALITY_CONFIG]) {
    return null
  }

  const config = QUALITY_CONFIG[quality as keyof typeof QUALITY_CONFIG]

  return (
    <div class={classNames(displayClass, "quality-badge")} data-quality={quality}>
      <span class="quality-badge-icon">{config.icon}</span>
      <span class="quality-badge-label">{config.label}</span>
    </div>
  )
}

QualityBadge.css = `
.quality-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  font-size: 0.72rem;
  font-weight: 600;
  padding: 0.15rem 0.6rem;
  border-radius: 4px;
  margin: 0.3rem 0 0.6rem 0;
  letter-spacing: 0.03em;
  user-select: none;
}

.quality-badge[data-quality="complete"] {
  color: #2da44e;
  background: #dafbe1;
  border: 1px solid #b3e5c2;
}

.quality-badge[data-quality="partial"] {
  color: #9a6e00;
  background: #fff8c5;
  border: 1px solid #f0d84c;
}

.quality-badge[data-quality="stub"] {
  color: #cf222e;
  background: #ffebe9;
  border: 1px solid #f5c2c7;
}

:root[saved-theme="dark"] .quality-badge[data-quality="complete"] {
  color: #57d46e;
  background: rgba(45, 164, 78, 0.12);
  border-color: rgba(45, 164, 78, 0.3);
}

:root[saved-theme="dark"] .quality-badge[data-quality="partial"] {
  color: #e0b310;
  background: rgba(191, 135, 0, 0.12);
  border-color: rgba(191, 135, 0, 0.3);
}

:root[saved-theme="dark"] .quality-badge[data-quality="stub"] {
  color: #f76d76;
  background: rgba(207, 34, 46, 0.12);
  border-color: rgba(207, 34, 46, 0.3);
}

.quality-badge-icon {
  font-size: 0.85em;
  line-height: 1;
}

.quality-badge-label {
  line-height: 1;
}
`

export default (() => QualityBadge) satisfies QuartzComponentConstructor
