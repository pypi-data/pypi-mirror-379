#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Конвертер между Python файлами с ячейками и Jupyter ноутбуками

Логика конвертации:
- py -> ipynb: многострочные комментарии \"\"\" становятся markdown ячейками,
  функции и классы - отдельными code ячейками, остальной код группируется
- ipynb -> py: аналогично в обратном направлении, outputs игнорируются
"""

import ast
import glob
import json
import re
import sys
import warnings
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional

# Подавляем предупреждения об устаревших функциях AST для совместимости
warnings.filterwarnings("ignore", category=DeprecationWarning, message=".*ast.Str.*")
warnings.filterwarnings("ignore", category=DeprecationWarning, message=".*Attribute s.*")


# Экспортируем функцию main для использования в __main__.py
def expand_glob_patterns(patterns: List[str]) -> List[str]:
    """Расширяет glob-шаблоны в список файлов, сортирует по имени"""
    expanded_files = []
    for pattern in patterns:
        # Используем glob для расширения шаблона
        matches = glob.glob(pattern)
        if matches:
            # Сортируем найденные файлы по имени
            matches.sort()
            expanded_files.extend(matches)
        else:
            # Если шаблон не нашел файлов, добавляем как есть (для обратной совместимости)
            expanded_files.append(pattern)
    return expanded_files


def show_help():
    """Показывает справку по использованию инструмента"""
    print("🔄 py2jupyter - Конвертер Python ↔ Jupyter Notebook")
    print("=" * 50)
    print()
    print("📖 ОПИСАНИЕ:")
    print("  Двунаправленный конвертер между Python файлами и Jupyter ноутбуками")
    print("  с поддержкой markdown комментариев и умным структурированием кода.")
    print()
    print("🚀 ИСПОЛЬЗОВАНИЕ:")
    print("  Базовая конвертация:")
    print("    py2jupyter input.py                    # → input.ipynb")
    print("    py2jupyter input.ipynb                 # → input.py")
    print("    py2jupyter input.py output.ipynb       # указанное имя")
    print("    py2jupyter input.py output             # → output.ipynb")
    print()
    print("  Многофайловое слияние:")
    print("    py2jupyter file1.py file2.py merged.ipynb")
    print("    py2jupyter nb1.ipynb nb2.ipynb merged.py")
    print("    py2jupyter script*.py                    # → script.ipynb (автоматически)")
    print("    py2jupyter test_*.py output.ipynb       # с указанием выходного файла")
    print()
    print("📝 ФОРМАТЫ КОММЕНТАРИЕВ:")
    print("  Python → Jupyter:")
    print('    """ # Заголовок # """           → markdown заголовок')
    print('    """ Описание текста """         → markdown блок')
    print('    r""" LaTeX: $\\int x dx$ """    → markdown с r-префиксом')
    print("    def func(): \"\"\"docstring\"\"\"  → остается в коде")
    print("    # обычный комментарий          → остается комментарием")
    print()
    print("  Jupyter → Python:")
    print("    # Заголовок #                  → \"\"\" # Заголовок # \"\"\"")
    print("    Markdown с \\ символами        → r\"\"\"...\"\"\"")
    print("    Обычный markdown               → \"\"\"...\"\"\"")
    print()
    print("⚙️  ОСОБЕННОСТИ:")
    print("  ✓ Функции и классы в отдельных ячейках")
    print("  ✓ Умное определение r-префикса по наличию \\ символов")
    print("  ✓ Автоматическое определение расширений файлов")
    print("  ✓ Многофайловое слияние")
    print("  ✓ Поддержка glob-шаблонов (*, ?)")
    print("  ✓ Взаимообратимая конвертация")
    print()
    print("📚 ПРИМЕРЫ:")
    print("  py2jupyter script.py")
    print("  py2jupyter notebook.ipynb")
    print("  py2jupyter --help")
    print()


def main():
    """Главный интерфейс конвертера"""
    # Проверяем флаг справки
    if len(sys.argv) == 2 and sys.argv[1] in ['--help', '-h', 'help']:
        show_help()
        sys.exit(0)
    
    if len(sys.argv) < 2:
        print("🔄 py2jupyter - Конвертер Python ↔ Jupyter Notebook")
        print()
        print("Использование:")
        print("  python py2jupyter.py input.py [output.ipynb]    # py → ipynb")
        print("  python py2jupyter.py input.ipynb [output.py]    # ipynb → py")
        print("  python py2jupyter.py input1.py input2.py output.ipynb  # многофайловое слияние")
        print("  python py2jupyter.py script*.py                 # glob-шаблоны")
        print("  python py2jupyter.py --help                     # подробная справка")
        print()
        print("Если выходной файл не указан, он генерируется автоматически")
        sys.exit(1)

    # Разделяем аргументы на входные файлы и выходной файл
    original_input_pattern = None  # Для генерации имени из glob-шаблона
    if len(sys.argv) == 2:
        # Один входной файл, выходной генерируется автоматически
        original_input_pattern = sys.argv[1]
        input_files = [sys.argv[1]]
        output_file = None
    elif len(sys.argv) == 3:
        # Может быть один входной файл с выходным, или два входных файла (результат glob-расширения)
        first_path = Path(sys.argv[1])
        second_path = Path(sys.argv[2])

        # Проверяем, есть ли у второго файла расширение .py/.ipynb - если да, то это несколько входных файлов
        if second_path.suffix in ['.py', '.ipynb'] and first_path.suffix == second_path.suffix:
            # Это может быть результат glob-расширения - обрабатываем как несколько входных файлов
            input_files = [sys.argv[1], sys.argv[2]]
            output_file = None
        else:
            # Это один входной файл с выходным файлом
            input_files = [sys.argv[1]]
            output_file = sys.argv[2]
    else:
        # Проверяем, все ли аргументы - существующие файлы с одинаковым расширением
        all_args = sys.argv[1:]
        all_paths_exist = all(Path(arg).exists() for arg in all_args)
        if all_paths_exist:
            # Все аргументы - существующие файлы
            all_suffixes = set(Path(arg).suffix for arg in all_args)
            if len(all_suffixes) == 1 and all_suffixes.pop() in ['.py', '.ipynb']:
                # Все файлы имеют одинаковое расширение .py или .ipynb - считаем их входными
                input_files = all_args
                output_file = None
            else:
                # Разные расширения или неподдерживаемые - последний выходной
                input_files = all_args[:-1]
                output_file = all_args[-1]
        else:
            # Некоторые аргументы не существуют - последний выходной
            input_files = all_args[:-1]
            output_file = all_args[-1]

    # Расширяем glob-шаблоны в списке входных файлов
    input_files = expand_glob_patterns(input_files)

    # Проверяем существование всех входных файлов
    input_paths = []
    for input_file in input_files:
        input_path = Path(input_file)
        if not input_path.exists():
            print(f"Файл {input_file} не найден")
            sys.exit(1)
        input_paths.append(input_path)

    # Проверяем, что все входные файлы имеют одинаковое расширение
    if len(input_paths) > 1:
        first_suffix = input_paths[0].suffix
        if not all(p.suffix == first_suffix for p in input_paths):
            print("Ошибка: Все входные файлы должны иметь одинаковое расширение (.py или .ipynb)")
            sys.exit(1)

    # Определяем выходной файл, если не указан
    if output_file is None:
        if len(input_paths) > 1:
            # Для нескольких файлов пытаемся определить общий префикс
            # (что указывает на использование glob-шаблона)
            file_names = [p.stem for p in input_paths]  # имена без расширений

            # Находим общий префикс
            if file_names:
                common_prefix = file_names[0]
                for name in file_names[1:]:
                    # Находим общую часть до первого отличия
                    for i, (a, b) in enumerate(zip(common_prefix, name)):
                        if a != b:
                            common_prefix = common_prefix[:i]
                            break
                    else:
                        # Если одно имя короче другого
                        common_prefix = common_prefix[:min(len(common_prefix), len(name))]

                # Убираем trailing символы, которые могут быть частью шаблона
                common_prefix = common_prefix.rstrip('_-0123456789')

                if common_prefix and len(common_prefix) > 1:  # Минимум 2 символа для осмысленного имени
                    base_name = common_prefix
                else:
                    # Если общего префикса нет, используем просто первый файл без номера
                    base_name = file_names[0].rstrip('_-0123456789')

                # Используем директорию первого файла как базовую для выходного файла
                output_dir = input_paths[0].parent
                if input_paths[0].suffix == '.py':
                    output_file = str(output_dir / (base_name + '.ipynb'))
                elif input_paths[0].suffix == '.ipynb':
                    output_file = str(output_dir / (base_name + '.py'))
                else:
                    print(f"Неподдерживаемый формат файла: {input_paths[0].suffix}")
                    print("Поддерживаются только .py и .ipynb файлы")
                    sys.exit(1)
            else:
                print("Ошибка: Для многофайлового слияния необходимо указать выходной файл")
                sys.exit(1)
        else:
            # Автоматическая генерация выходного файла для одного входного
            input_path = input_paths[0]
            if input_path.suffix == '.py':
                output_file = str(input_path.with_suffix('.ipynb'))
            elif input_path.suffix == '.ipynb':
                output_file = str(input_path.with_suffix('.py'))
            else:
                print(f"Неподдерживаемый формат файла: {input_path.suffix}")
                print("Поддерживаются только .py и .ipynb файлы")
                sys.exit(1)

    output_path = Path(output_file)
    
    # Автоматическое определение расширения если оно не указано
    if not output_path.suffix:
        # Определяем нужное расширение по типу входных файлов
        if input_paths[0].suffix == '.py':
            # Python -> Jupyter
            output_path = output_path.with_suffix('.ipynb')
        elif input_paths[0].suffix == '.ipynb':
            # Jupyter -> Python  
            output_path = output_path.with_suffix('.py')
        else:
            print(f"Неподдерживаемый формат входного файла: {input_paths[0].suffix}")
            sys.exit(1)

    try:
        if input_paths[0].suffix == '.py':
            # Конвертация Python -> Jupyter (одиночная или множественная)
            converter = PythonToIPythonConverter()
            total_cells = 0

            if len(input_paths) == 1:
                # Для одиночной конвертации используем основной конвертер
                cells = converter.parse_python_file(str(input_path))
                total_cells = len(cells)
            else:
                # Для слияния создаем временный конвертер для каждого файла
                for input_path in input_paths:
                    temp_converter = PythonToIPythonConverter()
                    cells = temp_converter.parse_python_file(str(input_path))
                    total_cells += len(cells)
                    # Добавляем ячейки из этого файла к общему списку
                    converter.cells.extend(cells)

            converter.generate_ipynb(str(output_path))
            if len(input_paths) == 1:
                print(f"Конвертировано {total_cells} ячеек: {input_paths[0].name} → {output_path.name}")
            else:
                file_names = [p.name for p in input_paths]
                print(f"Объединено {len(input_paths)} файлов ({', '.join(file_names)}) → {output_path}")
                print(f"Всего ячеек: {total_cells}")

        elif input_paths[0].suffix == '.ipynb':
            # Конвертация Jupyter -> Python (одиночная или множественная)  
            converter = IPythonToPythonConverter()
            combined_code = []
            
            for i, input_path in enumerate(input_paths):
                file_converter = IPythonToPythonConverter()  # Создаем новый для каждого файла
                python_code = file_converter.parse_ipynb_file(str(input_path))
                if python_code.strip():
                    if i > 0:  # Добавляем разделитель между файлами
                        combined_code.append('\n' + '# ' + '='*60)
                        combined_code.append(f'# Файл: {input_path.name}')
                        combined_code.append('# ' + '='*60 + '\n')
                    combined_code.append(python_code)
            
            final_code = '\n'.join(combined_code)
            converter.save_python_file(final_code, str(output_path))
            
            if len(input_paths) == 1:
                print(f"Конвертировано: {input_paths[0].name} → {output_path.name}")
            else:
                file_names = [p.name for p in input_paths]
                print(f"Объединено {len(input_paths)} файлов ({', '.join(file_names)}) → {output_path}")

        else:
            print("Неподдерживаемый формат файла")
            sys.exit(1)

    except Exception as e:
        print(f"Ошибка при конвертации: {e}")
        sys.exit(1)


class PythonToIPythonConverter:
    """Конвертер Python файлов в Jupyter ноутбуки"""

    def __init__(self):
        self.cells = []

    def parse_python_file(self, filepath: str) -> List[Dict[str, Any]]:
        """Парсит Python файл и выделяет блоки для конвертации в ячейки"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Используем AST для парсинга структур
        try:
            tree = ast.parse(content)
        except SyntaxError as e:
            print(f"Ошибка синтаксиса в файле {filepath}: {e}")
            return []

        self.cells = []
        self._extract_cells_from_ast(tree, content)

        return self.cells

    def _extract_cells_from_ast(self, tree: ast.AST, content: str):
        """Извлекает ячейки из AST дерева"""
        lines = content.split('\n')

        # Находим все функции, классы, многострочные строки и однострочные многострочные комментарии
        functions: List[Tuple[int, int, str]] = []
        classes: List[Tuple[int, int, str]] = []
        multiline_strings = []
        single_line_multistrings = []

        # Собираем все функции для определения вложенности
        all_functions: List[Tuple[int, int, str, Any]] = []
        all_classes: List[Tuple[int, int, str, Any]] = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Определяем реальное начало функции с учетом декораторов
                start_line = node.lineno
                if node.decorator_list:
                    # Находим минимальный lineno среди всех декораторов
                    decorator_start = min(decorator.lineno for decorator in node.decorator_list)
                    start_line = min(start_line, decorator_start)
                all_functions.append((start_line, node.end_lineno, node.name, node)) #type:ignore
            elif isinstance(node, ast.ClassDef):
                # Определяем реальное начало класса с учетом декораторов
                start_line = node.lineno
                if node.decorator_list:
                    # Находим минимальный lineno среди всех декораторов
                    decorator_start = min(decorator.lineno for decorator in node.decorator_list)
                    start_line = min(start_line, decorator_start)
                all_classes.append((start_line, node.end_lineno, node.name, node)) #type:ignore

        # Фильтруем только top-level функции (не вложенные)
        for func_start, func_end, func_name, func_node in all_functions:
            # Проверяем, является ли функция вложенной
            is_nested = False
            for parent_start, parent_end, _, _ in all_functions + all_classes:
                if parent_start < func_start < parent_end and (func_start, func_end, func_name, func_node) != (parent_start, parent_end, _, _):
                    is_nested = True
                    break
            if not is_nested:
                functions.append((func_start, func_end, func_name))

        # Фильтруем только top-level классы
        for class_start, class_end, class_name, class_node in all_classes:
            # Проверяем, является ли класс вложенным
            is_nested = False
            for parent_start, parent_end, _, _ in all_functions + all_classes:
                if parent_start < class_start < parent_end and (class_start, class_end, class_name, class_node) != (parent_start, parent_end, _, _):
                    is_nested = True
                    break
            if not is_nested:
                classes.append((class_start, class_end, class_name))

        # Находим многострочные строки (только top-level, не внутри функций/классов)
        for node in ast.walk(tree):
            # Проверяем является ли это строковой константой (совместимость с Python 3.8+)
            is_string_node = False
            if hasattr(ast, 'Constant') and isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
                # Python 3.8+: используем ast.Constant
                is_string_node = isinstance(node.value.value, str)
            elif hasattr(ast, 'Str') and isinstance(node, ast.Expr) and isinstance(node.value, ast.Str):
                # Python < 3.8: используем ast.Str
                is_string_node = True
                
            if is_string_node and hasattr(node, 'lineno') and hasattr(node, 'end_lineno') and node.end_lineno:
                if node.lineno != node.end_lineno:  # Многострочный
                    # Проверяем, является ли это docstring (находится внутри функции/класса)
                    is_docstring = False
                    parent = getattr(node, '_parent', None)
                    if parent and isinstance(parent, (ast.FunctionDef, ast.ClassDef)):
                        is_docstring = True

                    # Также проверяем по положению в коде
                    for func_start, func_end, _, _ in all_functions:
                        if func_start < node.lineno < func_end:
                            is_docstring = True
                            break
                    for class_start, class_end, _, _ in all_classes:
                        if class_start < node.lineno < class_end:
                            is_docstring = True
                            break

                    if not is_docstring:
                        multiline_strings.append((node.lineno, node.end_lineno))

        # Находим magic команды в формате #> %command
        magic_commands = []
        for i, line in enumerate(lines, 1):  # i - номер строки (1-based)
            stripped = line.strip()
            if stripped.startswith('#> %'):
                # Извлекаем magic команду (убираем #> )
                magic_content = stripped[3:].strip()  # убираем #> и пробелы

                # Проверяем, что это не внутри функции/класса
                is_inside_block = False
                for func_start, func_end, _, _ in all_functions:
                    if func_start < i < func_end:
                        is_inside_block = True
                        break
                for class_start, class_end, _, _ in all_classes:
                    if class_start < i < class_end:
                        is_inside_block = True
                        break

                if not is_inside_block:
                    magic_commands.append((i, i, magic_content))

        # Находим shell команды в формате #> !command
        shell_commands = []
        for i, line in enumerate(lines, 1):  # i - номер строки (1-based)
            stripped = line.strip()
            if stripped.startswith('#> !'):
                # Извлекаем shell команду (убираем #> )
                shell_content = stripped[3:].strip()  # убираем #> и пробелы

                # Проверяем, что это не внутри функции/класса
                is_inside_block = False
                for func_start, func_end, _, _ in all_functions:
                    if func_start < i < func_end:
                        is_inside_block = True
                        break
                for class_start, class_end, _, _ in all_classes:
                    if class_start < i < class_end:
                        is_inside_block = True
                        break

                if not is_inside_block:
                    shell_commands.append((i, i, shell_content))

        # Находим однострочные многострочные комментарии в формате """ текст """
        for i, line in enumerate(lines, 1):  # i - номер строки (1-based)
            stripped = line.strip()
            # Проверяем формат """ текст """ или r""" текст """ на одной строке
            # Включает как обычные комментарии, так и заголовочные """ # текст # """
            if ((stripped.startswith('"""') and stripped.endswith('"""') and len(stripped) > 6) or
                (stripped.startswith('r"""') and stripped.endswith('"""') and len(stripped) > 7)):

                # Извлекаем содержимое
                if stripped.startswith('r"""'):
                    inner_content = stripped[4:-3].strip()
                else:
                    inner_content = stripped[3:-3].strip()

                # Проверяем, что это не внутри функции/класса (не docstring)
                is_inside_block = False
                for func_start, func_end, _, _ in all_functions:
                    if func_start < i < func_end:
                        is_inside_block = True
                        break
                for class_start, class_end, _, _ in all_classes:
                    if class_start < i < class_end:
                        is_inside_block = True
                        break

                if not is_inside_block:
                    # Все однострочные многострочные комментарии обрабатываются одинаково
                    single_line_multistrings.append((i, i, inner_content))

        # Сортируем все блоки по начальной строке
        all_blocks = []
        for start, end, name in functions:
            all_blocks.append(('function', start, end, name))
        for start, end, name in classes:
            all_blocks.append(('class', start, end, name))
        for start, end in multiline_strings:
            all_blocks.append(('multiline_string', start, end, ''))
        for start, end, content in single_line_multistrings:
            all_blocks.append(('single_line_multistring', start, end, content))
        for start, end, content in magic_commands:
            all_blocks.append(('magic_command', start, end, content))
        for start, end, content in shell_commands:
            all_blocks.append(('shell_command', start, end, content))

        all_blocks.sort(key=lambda x: x[1])  # Сортировка по начальной строке

        # Создаем ячейки
        current_pos = 0
        for block_type, start, end, name in all_blocks:
            # Добавляем код перед блоком
            if start > current_pos + 1:
                code_lines = lines[current_pos:start-1]
                self._add_code_cell(code_lines)

            # Добавляем сам блок
            if block_type in ('function', 'class'):
                cell_lines = lines[start-1:end]
                self._add_code_cell_with_name(cell_lines, f"{block_type} {name}")
                current_pos = end  # Обновляем позицию сразу после добавления функции/класса
                continue  # Пропускаем обновление current_pos в конце цикла
            elif block_type == 'magic_command':
                # Magic команды становятся code ячейками
                self.cells.append({
                    'type': 'code',
                    'name': 'magic',
                    'content': name  # name содержит magic команду
                })
                current_pos = end  # Обновляем позицию после magic команды
                continue  # Пропускаем обновление current_pos в конце цикла
            elif block_type == 'shell_command':
                # Shell команды становятся code ячейками
                self.cells.append({
                    'type': 'code',
                    'name': 'shell',
                    'content': name  # name содержит shell команду
                })
                current_pos = end  # Обновляем позицию после shell команды
                continue  # Пропускаем обновление current_pos в конце цикла
            elif block_type == 'multiline_string':
                # Проверяем, является ли это markdown ячейкой (начинается с r""" или """)
                first_line = lines[start-1] if start-1 < len(lines) else ""
                stripped_first_line = first_line.strip()
                is_markdown_cell = (stripped_first_line.startswith('r\"\"\"') or 
                                  stripped_first_line.startswith('\"\"\"'))

                if is_markdown_cell:
                    # Это markdown ячейка - создаем отдельную ячейку
                    docstring_lines = lines[start-1:end]
                    # Убираем r""" или """
                    if docstring_lines and docstring_lines[0].strip().startswith('r\"\"\"'):
                        docstring_lines[0] = docstring_lines[0].replace('r\"\"\"', '', 1)
                    elif docstring_lines and docstring_lines[0].strip().startswith('\"\"\"'):
                        docstring_lines[0] = docstring_lines[0].replace('\"\"\"', '', 1)
                    if docstring_lines and docstring_lines[-1].strip().endswith('\"\"\"'):
                        docstring_lines[-1] = docstring_lines[-1].rsplit('\"\"\"', 1)[0]

                    # Очищаем пустые строки
                    while docstring_lines and not docstring_lines[0].strip():
                        docstring_lines.pop(0)
                    while docstring_lines and not docstring_lines[-1].strip():
                        docstring_lines.pop()

                    if docstring_lines:
                        content = '\n'.join(docstring_lines)
                        
                        # Проверяем, является ли это заголовком в формате # text #
                        content_stripped = content.strip()
                        self.cells.append({
                            'type': 'markdown',
                            'name': 'markdown',
                            'content': content
                        })
                    current_pos = end  # Обновляем позицию после markdown ячейки
                    continue  # Пропускаем обновление current_pos в конце цикла
                # Если это обычный """ или docstring, игнорируем его -
                # он будет включен в ячейку функции/класса или обычного кода

            elif block_type == 'single_line_multistring':
                # Это однострочный многострочный комментарий - создаем markdown ячейку
                if name:  # name содержит контент комментария
                    self.cells.append({
                        'type': 'markdown',
                        'name': 'markdown',
                        'content': name
                    })
                current_pos = end  # Обновляем позицию после markdown ячейки
                continue  # Пропускаем обновление current_pos в конце цикла

            current_pos = end

        # Добавляем оставшийся код
        if current_pos < len(lines):
            remaining_lines = lines[current_pos:]
            self._add_code_cell(remaining_lines)

        # Если ничего не найдено, добавляем весь файл как одну ячейку
        if not self.cells:
            content_lines = content.split('\n')
            self._add_code_cell_with_name(content_lines, 'main')

    def _find_block_end(self, lines: List[str], start_line_idx: int) -> int:
        """Находит конец блока (функции/класса) по отступам"""
        if start_line_idx >= len(lines):
            return len(lines)

        # Определяем базовый отступ блока
        base_indent = len(lines[start_line_idx]) - len(lines[start_line_idx].lstrip())

        # Ищем конец блока - строку с тем же или меньшим отступом
        for i in range(start_line_idx + 1, len(lines)):
            line = lines[i]
            if line.strip():  # Пропускаем пустые строки
                current_indent = len(line) - len(line.lstrip())
                # Если отступ меньше или равен базовому - это конец блока
                if current_indent <= base_indent:
                    return i

        return len(lines)  # Если не нашли конец, возвращаем конец файла

    def _add_code_cell(self, lines: List[str]):
        """Добавляет code ячейку из списка строк"""
        # Разбиваем на блоки по пустым строкам
        code_blocks = self._split_code_by_empty_lines(lines)

        for block in code_blocks:
            # Очищаем пустые строки в начале и конце каждого блока
            while block and not block[0].strip():
                block.pop(0)
            while block and not block[-1].strip():
                block.pop()

            if block:
                self.cells.append({
                    'type': 'code',
                    'name': 'code',
                    'content': '\n'.join(block)
                })

    def _split_code_by_empty_lines(self, lines: List[str]) -> List[List[str]]:
        """Разбивает код на блоки по двум пустым строкам (только на уровне нулевого отступа)"""
        if not lines:
            return []

        blocks = []
        current_block = []

        i = 0
        while i < len(lines):
            line = lines[i]
            current_block.append(line)

            # Проверяем, есть ли две пустые строки подряд на уровне нулевого отступа
            if (i + 2 < len(lines) and
                not line.strip() and  # текущая строка пустая
                not lines[i + 1].strip() and  # следующая строка пустая
                self._is_zero_indent_line(lines[i + 2])):  # следующая после пустых имеет нулевой отступ

                # Нашли разделитель - сохраняем текущий блок и начинаем новый
                if current_block:
                    blocks.append(current_block)
                current_block = []
                i += 1  # Пропускаем одну пустую строку из разделителя

            i += 1

        # Добавляем последний блок
        if current_block:
            blocks.append(current_block)

        return blocks

    def _is_zero_indent_line(self, line: str) -> bool:
        """Проверяет, имеет ли строка нулевой отступ (не пустая и начинается не с пробела)"""
        stripped = line.strip()
        return bool(stripped) and not line.startswith((' ', '\t'))

    def _add_code_cell_with_name(self, lines: List[str], name: str):
        """Добавляет code ячейку из списка строк с указанным именем"""
        # Разбиваем на блоки по пустым строкам
        code_blocks = self._split_code_by_empty_lines(lines)

        for block in code_blocks:
            # Очищаем пустые строки в начале и конце каждого блока
            while block and not block[0].strip():
                block.pop(0)
            while block and not block[-1].strip():
                block.pop()

            if block:
                self.cells.append({
                    'type': 'code',
                    'name': name,
                    'content': '\n'.join(block)
                })

    def generate_ipynb(self, output_path: str):
        """Генерирует .ipynb файл из ячеек"""

        cells: list = []

        notebook = {
            "cells": cells,
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3"
                },
                "language_info": {
                    "name": "python",
                    "version": "3.8.5"
                }
            },
            "nbformat": 4,
            "nbformat_minor": 2
        }

        for cell_data in self.cells:
            if cell_data['type'] == 'markdown':
                cell = {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": cell_data['content'].split('\n')
                }
            else:  # code
                cell = {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": cell_data['content'].split('\n')
                }
            cells.append(cell)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)


class IPythonToPythonConverter:
    """Конвертер Jupyter ноутбуков в Python файлы"""

    def __init__(self):
        self.python_code = []

    def parse_ipynb_file(self, filepath: str) -> str:
        """Парсит .ipynb файл и конвертирует в Python код"""
        with open(filepath, 'r', encoding='utf-8') as f:
            notebook = json.load(f)

        self.python_code = []
        first_code_cell_found = False

        for cell in notebook.get('cells', []):
            cell_type = cell.get('cell_type', 'code')
            source_lines = cell.get('source', [])

            # Преобразуем source из списка в строку
            if isinstance(source_lines, list):
                # Обрабатываем каждую строку, убирая лишние \n в конце
                processed_lines = []
                for line in source_lines:
                    # Убираем \n в конце каждой строки, если он есть
                    if line.endswith('\n'):
                        line = line[:-1]
                    processed_lines.append(line)

                # Убираем пустые строки в начале
                while processed_lines and not processed_lines[0].strip():
                    processed_lines.pop(0)

                # Убираем пустые строки в конце
                while processed_lines and not processed_lines[-1].strip():
                    processed_lines.pop()

                content = '\n'.join(processed_lines)
            else:
                content = source_lines

            # Проверяем, является ли это первой code ячейкой с shebang
            if cell_type == 'code' and not first_code_cell_found and content.strip().startswith('#!'):
                # Нашли shebang в первой code ячейке - добавляем его в начало
                shebang_lines = [line for line in content.split('\n') if line.strip().startswith('#!')]
                if shebang_lines:
                    self.python_code.append(shebang_lines[0])
                    self.python_code.append('')  # Добавляем пустую строку после shebang
                first_code_cell_found = True

            if cell_type == 'markdown':
                if content.strip():
                    # Определяем нужен ли префикс r на основе наличия символа \
                    needs_r_prefix = '\\' in content
                    prefix = 'r' if needs_r_prefix else ''

                    # Проверяем, является ли это однострочным контентом
                    lines_content = content.strip().split('\n')
                    is_single_line = len(lines_content) == 1

                    if (is_single_line and
                        content.strip().startswith('#') and content.strip().endswith('#')):
                        # Это заголовок - оборачиваем в """ # заголовок # """
                        self.python_code.append(f'{prefix}\"\"\" {content.strip()} \"\"\"')
                    elif is_single_line:
                        # Это однострочный markdown - используем однострочный формат
                        self.python_code.append(f'{prefix}\"\"\" {content.strip()} \"\"\"')
                    else:
                        # Многострочный markdown - используем многострочный формат
                        self.python_code.append(f'{prefix}\"\"\"\n{content}\n\"\"\"')

            elif cell_type == 'code':
                if content.strip():
                    # Проверяем, является ли это magic или shell командой
                    lines = content.strip().split('\n')
                    if len(lines) == 1:
                        single_line = lines[0].strip()
                        if single_line.startswith('%'):
                            # Это magic команда - конвертируем в комментарий
                            self.python_code.append(f'#> {single_line}')
                        elif single_line.startswith('!'):
                            # Проверяем, является ли это shebang
                            if single_line.startswith('!/usr/bin/env python') or single_line.startswith('!/usr/bin/python'):
                                # Это shebang - оставляем как есть
                                self.python_code.append(f'#{single_line}')
                            else:
                                # Это shell команда - конвертируем в комментарий
                                self.python_code.append(f'#> {single_line}')
                        else:
                            # Обычный код - добавляем как есть, но без shebang (уже обработан выше)
                            code_content = '\n'.join([line for line in content.split('\n') if not line.strip().startswith('#!')])
                            if code_content.strip():
                                self.python_code.append(code_content)
                    else:
                        # Многострочный код - добавляем как есть, но без shebang
                        code_content = '\n'.join([line for line in content.split('\n') if not line.strip().startswith('#!')])
                        if code_content.strip():
                            self.python_code.append(code_content)

                if cell_type == 'code':
                    first_code_cell_found = True

            # Добавляем пустую строку для разделения между ячейками (кроме последней)
            if cell != notebook.get('cells', [])[-1]:
                self.python_code.append('')

        return '\n'.join(self.python_code)

    def save_python_file(self, content: str, output_path: str):
        """Сохраняет Python код в файл"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)


if __name__ == "__main__":
    main()
