from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from vision_engine import VisionEngine
from screen_monitor import ScreenMonitor
from contextlib import asynccontextmanager
import uvicorn
import asyncio
import time
import os
import signal

# Track last activity
last_activity_time = time.time()
TIMEOUT_SECONDS = 30  # Shut down if no request for 30 seconds

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    vision.start()
    monitor.start()
    
    # Background task to check timeout
    async def check_timeout():
        while True:
            await asyncio.sleep(5)
            if time.time() - last_activity_time > TIMEOUT_SECONDS:
                print(f"No activity for {TIMEOUT_SECONDS}s. Auto-shutting down...")
                os.kill(os.getpid(), signal.SIGINT)
                break
    
    asyncio.create_task(check_timeout())
    
    yield
    
    # Shutdown
    vision.stop()
    monitor.stop()

app = FastAPI(lifespan=lifespan)

# Enable CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

vision = VisionEngine()
monitor = ScreenMonitor()

@app.get("/status")
async def get_status():
    global last_activity_time
    last_activity_time = time.time() # Reset heartbeat
    
    v_status = vision.get_status()
    m_status = monitor.get_status()
    
    base_focus = v_status["focus_score"]
    if m_status["is_slacking_app"]:
        base_focus *= 0.5
        
    return {
        "focus_score": float(round(base_focus, 2)),
        "face_detected": bool(v_status["face_detected"]),
        "active_app": str(m_status["active_app"]),
        "is_slacking": bool(m_status["is_slacking_app"] or base_focus < 50)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
