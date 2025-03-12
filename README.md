# Tencent TMS Search Engine for SearXNG

This project provides a custom search engine integration for [SearxNG](https://github.com/searxng/searxng) using the Tencent Cloud TMS (Text Mining Service) API. It allows users to leverage Tencent's AI-enhanced search capabilities within the SearxNG framework.

## Features

- **Tencent Cloud TMS Integration**: Perform searches using the Tencent TMS API.
- **SearxNG Compatibility**: Formats results in the standard SearxNG structure (`title`, `url`, `content`).
- **Lightweight**: No paging support, optimized for simple, fast queries.
- **Error Handling**: Robust parsing with fallback values for missing data.

## Requirements

- Python 3.6+
- [SearxNG](https://github.com/searxng/searxng) installed and configured
- Tencent Cloud account with TMS API access
- `SECRET_ID` and `SECRET_KEY` from Tencent Cloud

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/tms-searxng-engine.git
   
2. Copy tms.py to the searx/engines/ directory of your SearxNG installation:
   
```bash
cp tms.py /path/to/searxng/searx/engines/
```

3. Configure your Tencent Cloud credentials:
Edit tms.py and replace `SECRET_ID` and `SECRET_KEY` with your Tencent Cloud credentials.

4. Restart your SearxNG instance to load the new engine.

### Usage
Add Tencent TMS to your enabled engines in the SearxNG configuration (settings.yml):
yaml
```
engines:
  - name: Tencent TMS
```
Perform a search via the SearxNG interface, and results from Tencent TMS will appear when the engine is selected.
