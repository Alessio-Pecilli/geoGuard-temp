from pathlib import Path

from dotenv import dotenv_values, set_key

ENV_PATH = Path(__file__).resolve().parent / ".env"


def read_gemini_key():
    return (dotenv_values(ENV_PATH).get("GOOGLE_API_KEY") or "").strip()


def save_gemini_key(value):
    key = value.strip()
    if not key:
        return "Inserisci prima la chiave nel campo sopra."
    if "\n" in key or "\r" in key:
        return "La chiave deve essere su una sola riga."
    set_key(str(ENV_PATH), "GOOGLE_API_KEY", key)
    return "Chiave salvata sul PC. Verra usata automaticamente anche ai prossimi avvii; puoi lasciare il campo vuoto."
