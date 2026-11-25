"""Auditoría física de una línea base del repositorio de aseguramiento de 8=1.

Uso, desde la raíz de un clon nuevo del repositorio:

    python3 08_Configuracion/verificar_linea_base.py LB-SQAP-04

Comprueba cinco cosas en la etiqueta:
  1. Cada archivo del manifiesto existe y su SHA-256 coincide.
  2. El registro del estado y el manifiesto anotan los mismos archivos con la misma huella.
  3. Ningún archivo de la etiqueta queda sin registrar.
  4. Nadie escribió directo en main desde el commit e3ab430.
  5. No quedan marcadores de conflicto en los archivos Markdown.

Necesita Python 3 y openpyxl. No cambia nada del repositorio, salvo que deja la copia de trabajo en la etiqueta.
"""
import hashlib
import subprocess
import sys

from openpyxl import load_workbook

INICIO = 'e3ab430'


def git(*args):
    return subprocess.run(['git', *args], capture_output=True, text=True, check=True).stdout


def main(tag):
    git('checkout', '-q', tag)
    manifiesto = {}
    with open(f'08_Configuracion/{tag}.sha256', encoding='utf-8') as f:
        for ln in f:
            h, p = ln.rstrip('\n').split('  ', 1)
            manifiesto[p] = h
    disc = []
    for p, h in manifiesto.items():
        try:
            with open(p, 'rb') as f:
                if hashlib.sha256(f.read()).hexdigest() != h:
                    disc.append(f'Huella distinta: {p}')
        except FileNotFoundError:
            disc.append(f'Falta en la etiqueta: {p}')
    wb = load_workbook('08_Configuracion/Registro_del_estado_de_la_configuracion.xlsx', read_only=True)
    reg = {r[7]: r[8] for r in wb['Líneas base'].iter_rows(min_row=5, values_only=True) if r[0] == tag and r[7]}
    otros = {r[0] for r in wb['Otros archivos'].iter_rows(min_row=5, values_only=True) if r[0]}
    if reg != manifiesto:
        disc.append('El registro del estado y el manifiesto no anotan los mismos archivos o huellas.')
    archivos = [a for a in git('ls-tree', '-r', '--name-only', tag).split('\n') if a]
    for a in archivos:
        if a not in manifiesto and a not in otros and a != f'08_Configuracion/{tag}.sha256':
            disc.append(f'Archivo sin registrar: {a}')
    directos = [c for c in git('log', '--first-parent', '--no-merges', '--format=%h', f'{INICIO}..{tag}').split('\n') if c]
    if directos:
        disc.append(f'Commits directos en main: {", ".join(directos)}')
    marcas = git('grep', '-n', '-E', '^(<<<<<<<|=======|>>>>>>>)', tag, '--', '*.md') if subprocess.run(
        ['git', 'grep', '-q', '-E', '^(<<<<<<<|=======|>>>>>>>)', tag, '--', '*.md']).returncode == 0 else ''
    if marcas:
        disc.append('Quedan marcadores de conflicto en archivos Markdown.')
    print(f'Línea base {tag}: {len(manifiesto)} archivos de elementos y {len(archivos)} archivos en la etiqueta.')
    if disc:
        print('No conforme. Discrepancias:')
        for d in disc:
            print(' -', d)
        return 1
    print('Conforme. Todo coincide con el manifiesto y el registro, no hay commits directos en main y no quedan marcadores.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
