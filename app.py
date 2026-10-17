import json
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>KALVI - Ungal AI Thozhan</title>
<meta charset="UTF-8">
<style>
body { font-family: sans-serif; background: #0f172a; color: white; margin:0; display:flex; flex-direction:column; height:100vh; }
.header { background: #1e293b; padding: 15px; text-align:center; font-size:22px; font-weight:bold; color: #38bdf8; }
.chat { flex:1; overflow-y:auto; padding:20px; }
.msg { margin:10px 0; padding:12px 15px; border-radius:15px; max-width:80%; }
.user { background: #0284c7; align-self:flex-end; margin-left:auto; }
.bot { background: #1e293b; border:1px solid #334155; }
.input-area { display:flex; padding:15px; background:#1e293b; }
input { flex:1; padding:12px; border-radius:20px; border:none; outline:none; }
button { margin-left:10px; padding:12px 20px; border-radius:20px; border:none; background:#38bdf8; font-weight:bold; cursor:pointer; }
</style>
</head>
<body>
<div class="header">KALVI - Ungal AI Thozhan 🎓</div>
<div class="chat" id="chat">
<div class="msg bot">Vanakkam Atchaya! Naan KALVI! Enkitta ethavathu kelunga! 😊</div>
</div>
<div class="input-area">
<input id="q" placeholder="Ungal kelvi..." onkeypress="if(event.key=='Enter')send()">
<button onclick="send()">Send</button>
</div>
<script>
async function send(){
 let q=document.getElementById('q').value;
 if(!q) return;
 let chat=document.getElementById('chat');
 chat.innerHTML+=`<div class='msg user'>${q}</div>`;
 document.getElementById('q').value='';
 chat.scrollTop=chat.scrollHeight;
 let res=await fetch('/chat',{method:'POST',body:q});
 let ans=await res.text();
 chat.innerHTML+=`<div class='msg bot'>${ans}</div>`;
 chat.scrollTop=chat.scrollHeight;
}
</script>
</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode())

    def do_POST(self):
        length = int(self.headers.get('content-length',0))
        question = self.rfile.read(length).decode()
        
        data = {
            "model": "llama3.2:1b",
            "prompt": f"You are KALVI, a friendly AI assistant created by Atchaya. Answer helpfully. User: {question}",
            "stream": False
        }
        req = urllib.request.Request(
            "http://localhost:11434/api/generate",
            data=json.dumps(data).encode(),
            headers={'Content-Type':'application/json'}
        )
        try:
            with urllib.request.urlopen(req) as resp:
                result = json.loads(resp.read().decode())
                answer = result.get('response','Error')
        except Exception as e:
            answer = f"Error: {e} - Ollama running ah nu paarunga"
        
        self.send_response(200)
        self.send_header('Content-type','text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(answer.encode())

print("KALVI running at http://localhost:8000")
HTTPServer(('localhost',8000), Handler).serve_forever()