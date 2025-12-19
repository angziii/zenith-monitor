import subprocess
import threading
import time

class ScreenMonitor:
    def __init__(self):
        self.active_app = "Unknown"
        self.active_window_title = "Unknown"
        self.is_running = False
        self._thread = None
        self.slacking_apps = ["bilibili", "youtube", "steam", "discord", "netflix", "wechat"] # Examples

    def start(self):
        self.is_running = True
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self):
        self.is_running = False
        if self._thread:
            self._thread.join()

    def _get_active_window_macos(self):
        try:
            # AppleScript to get the name of the frontmost application
            script = 'tell application "System Events" to get name of first process whose frontmost is true'
            app_name = subprocess.check_output(['osascript', '-e', script], encoding='utf-8').strip()
            
            # AppleScript to get the window title (optional, sometimes fails if no windows)
            # script_title = 'tell application "System Events" to get name of first window of (first process whose frontmost is true)'
            # window_title = subprocess.check_output(['osascript', '-e', script_title], encoding='utf-8').strip()
            
            return app_name, ""
        except Exception:
            return "Unknown", ""

    def _run(self):
        while self.is_running:
            app, title = self._get_active_window_macos()
            self.active_app = app
            self.active_window_title = title
            time.sleep(2) # Polling interval

    def get_status(self):
        is_slacking = any(s in self.active_app.lower() for s in self.slacking_apps)
        return {
            "active_app": self.active_app,
            "is_slacking_app": is_slacking
        }

if __name__ == "__main__":
    monitor = ScreenMonitor()
    monitor.start()
    try:
        while True:
            print(monitor.get_status())
            time.sleep(2)
    except KeyboardInterrupt:
        monitor.stop()
