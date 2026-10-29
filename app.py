import os
import platform
import shutil
from http.server import BaseHTTPRequestHandler, HTTPServer
from html import escape

def check():
    return {
        "Architecture": platform.machine(),
        "Operating system": platform.platform(),
        "Python": platform.python_version(),
        "QEMU executable": shutil.which("qemu-system-x86_64") or "Not found",
        "Docker executable": shutil.which("docker") or "Not found",
        "/dev/kvm": "Available" if os.path.exists("/dev/kvm") else "Not available",
        "User ID": str(os.getuid()) if hasattr(os, "getuid") else "Unknown",
    }

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = check()
        rows = "".join(
            f"<tr><th>{escape(k)}</th><td>{escape(v)}</td></tr>"
            for k, v in data.items()
        )
        html = f"""<!doctype html>
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Motu Patlu Cloud Phone Test</title>
<style>
body{{font-family:system-ui;background:#111827;color:#f9fafb;margin:0;padding:22px}}
.card{{max-width:720px;margin:auto;background:#1f2937;border-radius:16px;padding:22px}}
h1{{font-size:25px}} .tag{{color:#67e8f9}} table{{width:100%;border-collapse:collapse}}
th,td{{text-align:left;padding:12px;border-bottom:1px solid #374151;overflow-wrap:anywhere}}
th{{width:42%;color:#cbd5e1}} .note{{background:#312e81;padding:14px;border-radius:10px;line-height:1.5}}
</style></head><body><div class="card">
<h1>☁️ MOTU PATLU <span class="tag">Cloud Phone Test</span></h1>
<p>This is a diagnostics page only — it is not an Android phone.</p>
<h2>Container checks</h2><table>{rows}</table>
<div class="note"><b>What this means:</b><br>
A full Android emulator commonly needs QEMU and, for good performance, KVM access.
If /dev/kvm is unavailable in this Pterodactyl container, this test cannot create a usable full Android phone.
Ask the hosting administrator to provide a supported Android runtime or a separate VM with virtualization enabled.
</div>
<p>To refresh checks, reload this page.</p></div></body></html>"""
        body = html.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *_):
        pass

port = int(os.environ.get("SERVER_PORT", os.environ.get("PORT", "8080")))
print(f"Cloud Phone diagnostics test listening on 0.0.0.0:{port}", flush=True)
HTTPServer(("0.0.0.0", port), Handler).serve_forever()
