"""
Problema 2: Cliente más fiel por socio — Banco de la Nación.

Cada socio tiene terminales POS; cada transacción registra cliente y terminal.
Se determina, por socio, el cliente con más compras. Empate: menor ID gana.
Sin transacciones: -1.

Entrada (stdin):
    N M S -> socios, terminales, transacciones
    p t -> M líneas: socio_id terminal_id
    c t -> S líneas: cliente_id terminal_id

Salida (stdout):
    socio_id cliente_mas_fiel (o -1 si no hubo transacciones)
"""

import sys
from collections import defaultdict


def build_terminal_to_partner_map(
    terminal_lines: list[str],
) -> dict[int, int]:
    """Mapea cada terminal_id a su partner_id.

    Args:
        terminal_lines: Líneas con formato "partner_id terminal_id".

    Returns:
        Diccionario {terminal_id: partner_id}.
    """
    terminal_to_partner = {}
    for line in terminal_lines:
        partner_id, terminal_id = map(int, line.split())
        terminal_to_partner[terminal_id] = partner_id
    return terminal_to_partner


def count_purchases_per_partner(
    transaction_lines: list[str],
    terminal_to_partner: dict[int, int],
    num_partners: int,
) -> dict[int, dict[int, int]]:
    """Cuenta compras de cada cliente agrupadas por socio.

    Args:
        transaction_lines: Líneas con formato "client_id terminal_id".
        terminal_to_partner: Mapeo {terminal_id: partner_id}.
        num_partners: Cantidad total de socios.

    Returns:
        Diccionario {partner_id: {client_id: cantidad_de_compras}}.
    """
    partner_client_counts = {
        p: defaultdict(int) for p in range(1, num_partners + 1)
    }

    for line in transaction_lines:
        client_id, terminal_id = map(int, line.split())
        if terminal_id in terminal_to_partner:
            partner_id = terminal_to_partner[terminal_id]
            partner_client_counts[partner_id][client_id] += 1

    return partner_client_counts


def find_most_loyal_client(client_counts: dict[int, int]) -> int:
    """Retorna el cliente con más compras, o -1 si no hay transacciones.

    Args:
        client_counts: Diccionario {client_id: num_compras}.

    Returns:
        client_id más fiel, o -1.
    """
    if not client_counts:
        return -1

    # Mayor compras, menor ID en empate
    best_client = min(client_counts.keys(), key=lambda c: (-client_counts[c], c))
    return best_client


def main() -> None:
    """Lee entrada de stdin y muestra el cliente más fiel por socio."""
    input_data = sys.stdin.read().split("\n")
    idx = 0

    first_line = input_data[idx].split()
    num_partners = int(first_line[0])
    num_terminals = int(first_line[1])
    num_transactions = int(first_line[2])
    idx += 1

    terminal_lines = []
    for _ in range(num_terminals):
        terminal_lines.append(input_data[idx].strip())
        idx += 1

    terminal_to_partner = build_terminal_to_partner_map(terminal_lines)

    transaction_lines = []
    for _ in range(num_transactions):
        transaction_lines.append(input_data[idx].strip())
        idx += 1

    partner_client_counts = count_purchases_per_partner(
        transaction_lines, terminal_to_partner, num_partners
    )

    for partner_id in range(1, num_partners + 1):
        most_loyal = find_most_loyal_client(partner_client_counts[partner_id])
        print(f"{partner_id} {most_loyal}")


if __name__ == "__main__":
    main()