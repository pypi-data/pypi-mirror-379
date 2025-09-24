#!/usr/bin/env python3

import asyncio

from mitmproxy import options
from mitmproxy.tools.web.master import WebMaster


async def start_gateway():
    opts = options.Options(
        mode=["reverse:https://api.anthropic.com"],
        listen_port=8080
    )
    master = WebMaster(opts)
    master.options.web_host = "127.0.0.1"
    master.options.web_port = 8081

    # import main_script
    # master.addons.add(main_script)
    # import annotate
    # master.addons.add(annotate)
    # import traffic_view
    # master.addons.add(traffic_view)
    from . import addon_list
    master.addons.add(addon_list)

    try:
        await master.run()
    except KeyboardInterrupt:
        print("\nShutting down gateway...")


def main():
    print("Starting MITM Gateway...")
    print("Web interface will be available at: http://127.0.0.1:8081")
    print("Proxy listening on: http://127.0.0.1:8080")
    print("Reverse proxy target: https://api.anthropic.com")
    print("Press Ctrl+C to stop")

    try:
        asyncio.run(start_gateway())
    except KeyboardInterrupt:
        print("\nShutting down gateway...")


if __name__ == "__main__":
    main()
