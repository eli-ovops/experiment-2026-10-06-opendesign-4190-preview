from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse,unquote
ROOT=Path("/Users/USER/Library/Application Support/Open Design/namespaces/release-stable/data/projects/9d715456-79e6-4e46-a052-ea34ff4c950d")
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*a,**k): super().__init__(*a,directory=str(ROOT),**k)
 def list_directory(self,p): self.send_error(404); return None
 def allowed(self):
  p=unquote(urlparse(self.path).path).lstrip('/') or 'index.html'
  parts=Path(p).parts
  return not any(x.startswith('.') or x=='..' for x in parts) and (p in ['index.html','app.js','projects.js','styles.css'] or p.startswith('assets/') or (len(parts)==1 and Path(p).suffix.lower() in ['.png','.jpg','.webp']))
 def do_GET(self):
  if not self.allowed(): self.send_error(404); return
  super().do_GET()
 def do_HEAD(self):
  if not self.allowed(): self.send_error(404); return
  super().do_HEAD()
 def end_headers(self):
  self.send_header('Cache-Control','no-store'); super().end_headers()
ThreadingHTTPServer(('127.0.0.1',4190),Handler).serve_forever()
