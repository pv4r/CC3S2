# WEEK-1

## Scripts

| Script | Descripcion |
|---|---|
| `spa_router.py` | Simulador de enrutamiento SPA con rutas estaticas y dinamicas |
| `bank_loyalty.py` | Determina el cliente mas fiel por socio segun transacciones |

## Requisitos

- Python 3.10+
- Opcionalmente, [uv](https://docs.astral.sh/uv/) para gestionar la version de Python

## Ejecucion

Cada script lee su entrada desde stdin. Se incluyen archivos de prueba:
`input_1.txt` para `spa_router.py` e `input_2.txt` para `bank_loyalty.py`.

### Linux / WSL

```bash
python3 spa_router.py < input_1.txt
python3 bank_loyalty.py < input_2.txt
```

### Windows (PowerShell)

PowerShell no soporta `<` para redirigir stdin, se usa `Get-Content` con pipe:

```powershell
Get-Content input_1.txt | python spa_router.py
Get-Content input_2.txt | python bank_loyalty.py
```

### Con uv (cualquier plataforma)

Si no tienes Python instalado globalmente, `uv run` descarga y usa la version
especificada en `.python-version` automaticamente:

```bash
# Linux / WSL / Git Bash
uv run spa_router.py < input_1.txt
uv run bank_loyalty.py < input_2.txt
```

```powershell
# PowerShell
Get-Content input_1.txt | uv run spa_router.py
Get-Content input_2.txt | uv run bank_loyalty.py
```

## Salida esperada

`spa_router.py` con `input_1.txt`:

```
HomePage
AboutPage
UserPage 42
404 Not Found
```

`bank_loyalty.py` con `input_2.txt`:

```
1 1501
2 1501
3 1502
4 -1
```
