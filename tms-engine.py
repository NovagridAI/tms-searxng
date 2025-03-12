# -*- coding: utf-8 -*-
"""
Tencent Cloud TMS Search Engine for SearxNG
"""

import base64
import hashlib
import hmac
import json
import time
from urllib.parse import urlencode
import traceback

# Engine metadata
name = 'Tencent TMS'
description = 'Search using Tencent Cloud TMS API'
default_params = {
    'method': 'GET',
    'timeout': 10,
    'headers': {'User-Agent': 'SearxNG'},
}
paging = False
supports_categories = ['general']

# Tencent Cloud configuration (load from environment or config in production)
SECRET_ID = ""  # Replace with your Secret ID
SECRET_KEY = ""  # Replace with your Secret Key
ENDPOINT = "tms.tencentcloudapi.com"


def get_string_to_sign(method, endpoint, params):
    """Generate the string to sign for Tencent Cloud API authentication."""
    query_str = "&".join(f"{k}={params[k]}" for k in sorted(params))
    return f"{method}{endpoint}/?{query_str}"


def sign_str(key, s, method):
    """Generate HMAC signature using the provided key and string."""
    hmac_str = hmac.new(key.encode("utf8"), s.encode("utf8"), method).digest()
    return base64.b64encode(hmac_str).decode("utf8")


def request(query, params):
    """Construct the API request for Tencent TMS."""
    api_params = {
        'Action': 'SearchPro',
        'Query': query,
        'Nonce': 0,
        'Mode': 2,
        'Region': 'ap-guangzhou',
        'SecretId': SECRET_ID,
        'Timestamp': int(time.time()),
        'Version': '2020-12-29'
    }

    # Generate signature
    sign_string = get_string_to_sign("GET", ENDPOINT, api_params)
    api_params["Signature"] = sign_str(SECRET_KEY, sign_string, hashlib.sha1)

    # Set the full URL in params
    params['url'] = f"https://{ENDPOINT}/?{urlencode(api_params)}"
    return params


def response(resp):
    """Parse the API response and format results for SearxNG."""
    results = []

    try:
        data = resp.json()
        pages = data.get("Response", {}).get("Pages", [])

        for page in pages:
            page = json.loads(page)
            title = page.get('title', 'Important Result JSON')
            url = page.get('url', 'http://www.baidu.com') # just fill result
            content = page.get('passage', json.dumps(page, ensure_ascii=False))

            results.append({
                'title': title,
                'url': url,
                'content': content,
            })
        print(results)
    except Exception:
        print(traceback.format_exc())

    return results


def _init():
    """Validate engine configuration during initialization."""
    if not SECRET_ID or not SECRET_KEY:
        raise ValueError("Tencent TMS engine requires SECRET_ID and SECRET_KEY")


if __name__ == "__main__":
    # Example usage (for testing purposes)
    test_params = {}
    query = "test query"
    updated_params = request(query, test_params)
    print(updated_params)
