from flask import Flask, jsonify
import psutil
import time
start_time = time.time()

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "running", "service": "devops-api"})

@app.route('/health')
def health():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    uptime = int(time.time() - start_time)
    return jsonify({
        "cpu_percent": cpu,
        "memory_percent": mem,
        "uptime_seconds": uptime,
        "status": "healthy" if cpu < 80 and mem < 80 else "unhealthy"
    })

@app.route('/metrics')
def metric():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    content = f"""# HELP app_cpu_percent CPU usage percentage
# TYPE app_cpu_percent gauge
app_cpu_percent {cpu}
# HELP app_memory_percent Memory usage percentage
# TYPE app_memory_percent gauge
app_memory_percent {mem}
"""
    return content, 200, {'Content-Type': 'text/plain; version=0.0.4'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
