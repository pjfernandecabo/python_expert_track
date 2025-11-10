import os

def read_lines(filepath):
    """Generador que lee líneas de un archivo grande."""
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def filter_lines(lines, keyword):
    """Filtra líneas que contienen cierta palabra clave."""
    for line in lines:
        if keyword.lower() in line.lower():
            yield line


def line_stats(lines):
    """Calcula estadísticas sobre líneas procesadas."""
    total = 0
    total_chars = 0
    for line in lines:
        total += 1
        total_chars += len(line)
        yield {"line": line, "length": len(line), "avg_length": total_chars / total}


def analyze_file(filepath, keyword):
    """Orquesta el flujo completo de lectura, filtrado y análisis."""
    lines = read_lines(filepath)
    filtered = filter_lines(lines, keyword)
    stats = line_stats(filtered)
    return stats


if __name__ == "__main__":
    path = os.path.join(os.path.dirname(__file__), "test_files", "sample.txt")

    for info in analyze_file(path, "es"):
        print(f"{info['line']} ({info['length']} chars, avg={info['avg_length']:.2f})")
