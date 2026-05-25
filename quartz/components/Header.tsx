import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"

const Header: QuartzComponent = ({ cfg, children }: QuartzComponentProps) => {
  const pageTitle = cfg?.pageTitle ?? "FAQ"

  return (
    <header class="site-header">
      <div class="header-inner">
        <a href="./" class="header-brand">
          <span class="header-logo">FAQ</span>
          <span class="header-title">{pageTitle}</span>
        </a>
        <nav class="header-nav desktop-only">
          <a href="./" class="header-nav-link">首頁</a>
          <a href="./FAQ_test/" class="header-nav-link">ERM FAQ</a>
          <a href="./ChainStoreplus/" class="header-nav-link">ChainStorePlus</a>
          <a href="./tags/" class="header-nav-link">標籤</a>
        </nav>
        {children}
      </div>
    </header>
  )
}

Header.css = `
.site-header {
  background: var(--light);
  border-bottom: 1px solid var(--lightgray);
}

.header-inner {
  max-width: calc(1200px + 300px);
  margin: 0 auto;
  display: flex;
  align-items: center;
  padding: 0.5rem 1.5rem;
  gap: 1.5rem;
}

.header-brand {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  text-decoration: none;
  font-family: var(--headerFont);
  flex-shrink: 0;
}

.header-logo {
  background: var(--secondary);
  color: #fff;
  font-size: 0.7rem;
  font-weight: 700;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
  letter-spacing: 0.05em;
  line-height: 1.4;
}

.header-title {
  font-size: 0.88rem;
  font-weight: 650;
  color: var(--dark);
  letter-spacing: -0.01em;
}

.header-nav {
  display: flex;
  gap: 0.15rem;
  flex: 1;
}

.header-nav-link {
  font-size: 0.78rem;
  color: var(--gray);
  text-decoration: none;
  padding: 0.25rem 0.55rem;
  border-radius: 5px;
  transition: color 0.15s ease, background 0.15s ease;
  font-weight: 500;
  white-space: nowrap;
}

.header-nav-link:hover {
  color: var(--secondary);
  background: var(--highlight);
}

@media all and (max-width: 800px) {
  .header-inner {
    padding: 0.4rem 0.8rem;
    gap: 0.5rem;
  }
  .header-title {
    font-size: 0.75rem;
  }
  .header-nav-link {
    font-size: 0.68rem;
    padding: 0.2rem 0.35rem;
  }
}
`

export default (() => Header) satisfies QuartzComponentConstructor
