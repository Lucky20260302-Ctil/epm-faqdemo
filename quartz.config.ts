import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "EPM / FEPOS FAQ",
    pageTitleSuffix: " — 故障排除知識庫",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "zh-TW",
    baseUrl: "lucky20260302-ctil.github.io/epm-faqdemo",
    ignorePatterns: [
      "private",
      "templates",
      ".obsidian",
      ".claude",
      ".git",
      "node_modules",
      "quartz",
      "public",
      "CLAUDE.md",
      ".canvases",
      "SKILL.md",
    ],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Outfit",
        body: "Noto Sans TC",
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          light: "#faf8f3",
          lightgray: "#e8e4dc",
          gray: "#b8b0a4",
          darkgray: "#5c554a",
          dark: "#1e1b18",
          secondary: "#c7512e",
          tertiary: "#6b8a5a",
          highlight: "rgba(199, 81, 46, 0.08)",
          textHighlight: "#f0d86066",
        },
        darkMode: {
          light: "#181a20",
          lightgray: "#282c34",
          gray: "#5c6370",
          darkgray: "#c8ccd4",
          dark: "#e8ecf0",
          secondary: "#e0a050",
          tertiary: "#8ab870",
          highlight: "rgba(224, 160, 80, 0.12)",
          textHighlight: "#a0902066",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: false,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
