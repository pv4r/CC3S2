"""
Problema 1: Simulador de enrutamiento SPA.

Dado un conjunto de rutas (estáticas o con parámetros dinámicos ':param'),
resuelve cada URL visitada e imprime su contenido o "404 Not Found".

Entrada (stdin):
    N -> cantidad de rutas
    /path contenido -> N líneas
    M -> cantidad de transiciones
    /path/visitado -> M líneas

Salida (stdout):
    Contenido de la ruta que coincide, o "404 Not Found".
"""

import sys


def parse_routes(raw_routes: list[str]) -> list[tuple[list[str], str]]:
    """Convierte rutas crudas en segmentos con su contenido.

    Args:
        raw_routes: Líneas con formato "/path contenido".

    Returns:
        Lista de tuplas (segmentos, contenido).
    """
    routes = []
    for line in raw_routes:
        parts = line.split()
        path = parts[0]
        content = parts[1]
        segments = [s for s in path.split("/") if s]
        routes.append((segments, content))
    return routes


def match_route(
    routes: list[tuple[list[str], str]], transition: str
) -> str:
    """Resuelve una transición contra las rutas registradas.

    Args:
        routes: Rutas parseadas (segmentos, contenido).
        transition: URL visitada, e.g. "/user/42".

    Returns:
        Contenido con parámetros, o "404 Not Found".
    """
    transition_segments = [s for s in transition.split("/") if s]

    for route_segments, content in routes:
        if len(route_segments) != len(transition_segments):
            continue

        params: list[str] = []
        is_match = True

        for route_seg, trans_seg in zip(route_segments, transition_segments):
            if route_seg.startswith(":"):
                params.append(trans_seg)
            elif route_seg != trans_seg:
                is_match = False
                break

        if is_match:
            result_parts = [content] + params
            return " ".join(result_parts)

    return "404 Not Found"


def main() -> None:
    """Lee rutas y transiciones de stdin e imprime el resultado de cada una."""
    input_data = sys.stdin.read().split("\n")
    idx = 0

    # Lectura de rutas
    num_routes = int(input_data[idx].strip())
    idx += 1

    raw_routes = []
    for _ in range(num_routes):
        raw_routes.append(input_data[idx].strip())
        idx += 1

    routes = parse_routes(raw_routes)

    # Lectura de transiciones
    num_transitions = int(input_data[idx].strip())
    idx += 1

    for _ in range(num_transitions):
        transition = input_data[idx].strip()
        idx += 1
        print(match_route(routes, transition))


if __name__ == "__main__":
    main()