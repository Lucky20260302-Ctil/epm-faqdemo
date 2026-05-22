import { i18n } from "../../i18n"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "../types"

const NotFound: QuartzComponent = ({ cfg }: QuartzComponentProps) => {
  const url = new URL(`https://${cfg.baseUrl ?? "example.com"}`)
  const baseDir = url.pathname

  return (
    <article class="popover-hint">
      <h1>404</h1>
      <p>{i18n(cfg.locale).pages.error.notFound}</p>
      <p>頁面不存在，3 秒後自動返回首頁...</p>
      <a href={baseDir}>{i18n(cfg.locale).pages.error.home}</a>
      <script dangerouslySetInnerHTML={{ __html: `setTimeout(function(){window.location.href='${baseDir}';},3000);` }} />
    </article>
  )
}

export default (() => NotFound) satisfies QuartzComponentConstructor
