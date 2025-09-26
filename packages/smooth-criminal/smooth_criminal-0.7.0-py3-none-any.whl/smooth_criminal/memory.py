"""Módulo de persistencia configurable para Smooth Criminal.

Este archivo define una interfaz ``StorageBackend`` con tres
implementaciones disponibles: ``JsonBackend``, ``SQLiteBackend`` y
``TinyDBBackend``.  El backend se selecciona mediante la variable de
entorno ``SMOOTH_CRIMINAL_STORAGE`` que puede tomar los valores
``json`` (por defecto), ``sqlite`` o ``tinydb``.

Las funciones públicas del módulo delegan su comportamiento en el
backend elegido manteniendo la API original para el resto del
proyecto.
"""

from __future__ import annotations

import csv
import json
import os
import statistics
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set


def calcular_score(durations: List[float], decorators: Set[str]) -> int:
    """Calcula una puntuación de optimización basada en duración y decoradores."""
    if not durations:
        return 0

    avg = statistics.mean(durations)
    stddev = statistics.stdev(durations) if len(durations) > 1 else 0.0

    score = 100
    if "@smooth" not in decorators and "@jam" not in decorators:
        score -= 20
    if avg > 0.01:
        score -= min((avg * 1000), 20)
    if stddev > 0.005:
        score -= 10

    return max(0, round(score))


class StorageBackend(ABC):
    """Interfaz base para los distintos métodos de almacenamiento."""

    #: ruta por defecto utilizada por el backend
    path: Path

    @abstractmethod
    def log_execution_stats(
        self, func_name: str, input_type, decorator_used: str, duration: float
    ) -> None:
        """Guarda un registro de ejecución."""

    @abstractmethod
    def get_execution_history(self, func_name: Optional[str] = None) -> List[Dict]:
        """Obtiene el historial de ejecuciones."""

    def clear_execution_history(self) -> bool:
        """Limpia por completo el historial basado en :attr:`self.path`."""
        if self.path.exists():
            self.path.unlink()
            return True
        return False

    def export_execution_history(self, filepath, format: str = "csv") -> bool:
        """Exporta el historial a CSV, JSON, XLSX o Markdown."""
        data = self.get_execution_history()
        if not data:
            return False

        try:
            data.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
        except Exception:
            pass

        format = format.lower()
        keys = ["function", "input_type", "decorator", "duration", "timestamp"]
        if format == "json":
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        elif format == "csv":
            with open(filepath, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)
        elif format == "xlsx":
            try:
                from openpyxl import Workbook
            except Exception as exc:  # pragma: no cover - se captura en pruebas
                raise RuntimeError(
                    "openpyxl es requerido para exportar a XLSX"
                ) from exc

            wb = Workbook()
            ws = wb.active
            ws.append(keys)
            for row in data:
                ws.append([row.get(k, "") for k in keys])
            wb.save(filepath)
        elif format == "md":
            with open(filepath, "w", encoding="utf-8") as f:
                header = "| " + " | ".join(keys) + " |\n"
                separator = "|" + " --- |" * len(keys) + "\n"
                f.write(header)
                f.write(separator)
                for row in data:
                    line = "| " + " | ".join(str(row.get(k, "")) for k in keys) + " |\n"
                    f.write(line)
        else:
            raise ValueError("Formato no soportado: usa 'csv', 'json', 'xlsx' o 'md'.")

        return True

    def score_function(self, func_name: str) -> Tuple[Optional[int], str]:
        """Calcula la puntuación de optimización para una función."""
        logs = self.get_execution_history(func_name)
        if not logs:
            return None, "No hay registros para esta función."

        times = [entry["duration"] for entry in logs]
        decorators = {entry["decorator"] for entry in logs}
        count = len(times)
        avg = statistics.mean(times)
        stddev = statistics.stdev(times) if count > 1 else 0.0

        score = calcular_score(times, decorators)

        summary = (
            f"🧠 Function: {func_name}\n"
            f"- Executions: {count}\n"
            f"- Avg time: {avg:.6f}s\n"
            f"- Std dev: {stddev:.6f}s\n"
            f"- Decorators: {', '.join(sorted(decorators))}\n"
        )

        return score, summary


# ---------------------------------------------------------------------------
# Implementaciones concretas


class JsonBackend(StorageBackend):
    """Persistencia basada en un archivo JSON."""

    path = Path.home() / ".smooth_criminal_log.json"

    def log_execution_stats(self, func_name, input_type, decorator_used, duration):
        log_entry = {
            "function": func_name,
            "input_type": str(input_type),
            "decorator": decorator_used,
            "duration": duration,
            "timestamp": datetime.utcnow().isoformat(),
        }

        logs: List[Dict] = []
        if self.path.exists():
            with open(self.path, "r", encoding="utf-8") as f:
                try:
                    logs = json.load(f)
                except json.JSONDecodeError:
                    logs = []

        logs.append(log_entry)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2)

    def get_execution_history(self, func_name: Optional[str] = None) -> List[Dict]:
        if not self.path.exists():
            return []

        with open(self.path, "r", encoding="utf-8") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                return []

        if func_name:
            logs = [entry for entry in logs if entry["function"] == func_name]
        return logs


class SQLiteBackend(StorageBackend):
    """Persistencia utilizando una base de datos SQLite."""

    path = Path.home() / ".smooth_criminal_log.sqlite"

    def _ensure_table(self, conn) -> None:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS logs (
                function TEXT,
                input_type TEXT,
                decorator TEXT,
                duration REAL,
                timestamp TEXT
            )
            """
        )
        conn.commit()

    def log_execution_stats(self, func_name, input_type, decorator_used, duration):
        import sqlite3

        with sqlite3.connect(self.path) as conn:
            self._ensure_table(conn)
            conn.execute(
                "INSERT INTO logs VALUES (?, ?, ?, ?, ?)",
                (
                    func_name,
                    str(input_type),
                    decorator_used,
                    float(duration),
                    datetime.utcnow().isoformat(),
                ),
            )
            conn.commit()

    def get_execution_history(self, func_name: Optional[str] = None) -> List[Dict]:
        import sqlite3

        if not self.path.exists():
            return []

        with sqlite3.connect(self.path) as conn:
            self._ensure_table(conn)
            cursor = conn.cursor()
            if func_name:
                cursor.execute(
                    "SELECT function,input_type,decorator,duration,timestamp FROM logs WHERE function=?",
                    (func_name,),
                )
            else:
                cursor.execute(
                    "SELECT function,input_type,decorator,duration,timestamp FROM logs"
                )
            rows = cursor.fetchall()

        return [
            {
                "function": r[0],
                "input_type": r[1],
                "decorator": r[2],
                "duration": r[3],
                "timestamp": r[4],
            }
            for r in rows
        ]


class TinyDBBackend(StorageBackend):
    """Persistencia mediante TinyDB."""

    path = Path.home() / ".smooth_criminal_log.tinydb"

    def __init__(self) -> None:
        try:
            from tinydb import Query, TinyDB
        except Exception as exc:  # pragma: no cover - la importación es dinámica
            raise RuntimeError(
                "TinyDB no está instalado. Instálalo con el extra 'tinydb'."
            ) from exc

        self.TinyDB = TinyDB
        self.Query = Query

    def _open(self):
        return self.TinyDB(self.path)

    def log_execution_stats(self, func_name, input_type, decorator_used, duration):
        with self._open() as db:
            db.insert(
                {
                    "function": func_name,
                    "input_type": str(input_type),
                    "decorator": decorator_used,
                    "duration": duration,
                    "timestamp": datetime.utcnow().isoformat(),
                }
            )

    def get_execution_history(self, func_name: Optional[str] = None) -> List[Dict]:
        if not self.path.exists():
            return []

        with self._open() as db:
            if func_name:
                results = db.search(self.Query().function == func_name)
            else:
                results = db.all()
        return list(results)


# ---------------------------------------------------------------------------
# Selección dinámica del backend


def _select_backend() -> StorageBackend:
    name = os.getenv("SMOOTH_CRIMINAL_STORAGE", "json").lower()
    if name == "sqlite":
        return SQLiteBackend()
    if name == "tinydb":
        return TinyDBBackend()
    return JsonBackend()


_BACKEND: StorageBackend = _select_backend()

# Exponer la ruta del backend seleccionado para mantener compatibilidad con
# el código existente y las pruebas.
LOG_PATH = _BACKEND.path


def log_execution_stats(func_name, input_type, decorator_used, duration):
    """Delegación pública al backend activo."""
    _BACKEND.log_execution_stats(func_name, input_type, decorator_used, duration)


_ORIGINAL_GET_HISTORY = None


def get_execution_history(func_name=None):
    """Obtiene el historial usando el backend activo.

    Mantiene compatibilidad con monkeypatch en tests que importaron una
    referencia previa de la función.
    """

    current = globals().get("get_execution_history", _ORIGINAL_GET_HISTORY)
    if _ORIGINAL_GET_HISTORY is not None and current is not _ORIGINAL_GET_HISTORY:
        try:
            return current(func_name)
        except TypeError:  # pragma: no cover - compatibilidad
            return current()

    return _BACKEND.get_execution_history(func_name)


_ORIGINAL_GET_HISTORY = get_execution_history


def clear_execution_history():
    """Limpia el historial usando el backend activo."""
    return _BACKEND.clear_execution_history()


def export_execution_history(filepath, format="csv"):
    """Exporta el historial usando el backend activo."""
    return _BACKEND.export_execution_history(filepath, format=format)


def build_summary(logs: List[Dict]) -> Dict[str, Dict[str, object]]:
    """Agrupa un listado de logs por función.

    Parameters
    ----------
    logs:
        Secuencia de registros devueltos por :func:`get_execution_history`.

    Returns
    -------
    dict
        Diccionario cuyas claves son los nombres de función y los valores
        contienen dos entradas:

        ``durations``
            Lista con las duraciones registradas.
        ``decorators``
            Conjunto con los decoradores utilizados.
    """

    summary: Dict[str, Dict[str, object]] = {}
    for entry in logs:
        fn = entry.get("function")
        if fn is None:
            continue
        data = summary.setdefault(fn, {"durations": [], "decorators": set()})
        if "duration" in entry:
            data["durations"].append(entry["duration"])
        if "decorator" in entry:
            data["decorators"].add(entry["decorator"])
    return summary


def score_function(func_name):
    """Calcula la puntuación delegando en el backend activo."""
    return _BACKEND.score_function(func_name)


def suggest_boost(func_name):
    """Función auxiliar original; se mantiene sin cambios."""
    logs = get_execution_history(func_name)
    if not logs:
        return f"No data found for function '{func_name}'."

    decor_stats = {}
    for entry in logs:
        decor_stats.setdefault(entry["decorator"], []).append(entry["duration"])

    avg_times = {decor: sum(times) / len(times) for decor, times in decor_stats.items()}
    best_decor = min(avg_times, key=avg_times.get)
    return (
        f"🧠 Suggestion for '{func_name}': use [bold green]{best_decor}[/bold green] "
        f"(avg {avg_times[best_decor]:.6f}s)"
    )


# Mantener compatibilidad con el sistema de parcheo utilizado por algunas
# pruebas; se almacena una referencia a la función original.
_ORIGINAL_GET_HISTORY = get_execution_history

