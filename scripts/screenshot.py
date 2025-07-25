import sys
import yaml
from pathlib import Path

def screenshot_site(handle):
    config_path = Path("sites") / f"{handle}.yml"
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    site = yaml.safe_load(config_path.read_text())
    print(f"Would capture screenshot for: {site['url']} (wait={site.get('wait', 0)}ms)")
    # Screenshot logic should be added here (e.g., with Playwright or Puppeteer)

if __name__ == "__main__":
    handle = sys.argv[1] if len(sys.argv) > 1 else "wsj"
    screenshot_site(handle)
