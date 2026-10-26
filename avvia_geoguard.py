from pathlib import Path
import socket
import subprocess
import sys
import time
import webbrowser

ROOT = Path(__file__).resolve().parent
URL = "http://127.0.0.1:8765"


def main():
    with socket.socket() as sock:
        running = sock.connect_ex(("127.0.0.1", 8765)) == 0
    if not running:
        from dotenv import load_dotenv
        load_dotenv(ROOT / ".env", override=False)
        log = open(ROOT / "geoguard-local.log", "a", encoding="utf-8")
        process = subprocess.Popen(
            [sys.executable, "-m", "marimo", "run",
             str(ROOT / "notebooks" / "geoguard-e2e.py"),
             "--host", "127.0.0.1", "--port", "8765", "--headless"],
            cwd=ROOT, stdout=log, stderr=log,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        (ROOT / "geoguard-local.pid").write_text(str(process.pid))
        for _ in range(120):
            if process.poll() is not None:
                raise RuntimeError("Avvio fallito. Consulta geoguard-local.log nella cartella GeoGuard.")
            with socket.socket() as sock:
                if sock.connect_ex(("127.0.0.1", 8765)) == 0:
                    break
            time.sleep(0.5)
        else:
            raise RuntimeError("Avvio troppo lento. Consulta geoguard-local.log.")
    webbrowser.open(URL)


if __name__ == "__main__":
    main()
