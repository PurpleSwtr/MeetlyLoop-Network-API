# python commit.py ""

import sys
import os
import subprocess

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def run_command(command, working_dir):
    """Выполняет команду в указанной рабочей директории и выводит результат."""
    print(f"{Colors.OKCYAN}▶️  Выполняю: {' '.join(command)}{Colors.ENDC}")
    try:
        # subprocess.run - это современный и безопасный способ запускать команды
        result = subprocess.run(
            command,
            cwd=working_dir,    # Указываем, где выполнить команду
            check=True,         # Выбросить исключение, если команда завершилась с ошибкой
            capture_output=True,# Захватить stdout и stderr
            text=True           # Декодировать вывод в текст
        )
        # Если есть вывод, печатаем его зеленым
        if result.stdout:
            print(f"{Colors.OKGREEN}{result.stdout.strip()}{Colors.ENDC}")
        # Если есть ошибки (например, предупреждения от git), печатаем их желтым
        if result.stderr:
            print(f"{Colors.WARNING}{result.stderr.strip()}{Colors.ENDC}")
        return True
    except FileNotFoundError:
        print(f"{Colors.FAIL}❌ Ошибка: Команда '{command[0]}' не найдена. Убедитесь, что Git установлен и доступен в PATH.{Colors.ENDC}")
        return False
    except subprocess.CalledProcessError as e:
        # Если команда вернула код ошибки, печатаем ее красным
        print(f"{Colors.FAIL}❌ Команда завершилась с ошибкой (код {e.returncode}):{Colors.ENDC}")
        print(f"{Colors.FAIL}{e.stderr.strip()}{Colors.ENDC}")
        return False

def main():
    # 1. Определяем директорию, в которой находится сам скрипт
    # Это ключевой момент, чтобы команды выполнялись в правильном месте
    repo_path = os.path.dirname(os.path.abspath(__file__))
    print(f"{Colors.HEADER}--- Запуск Git-автоматизации в директории: {repo_path} ---\n{Colors.ENDC}")

    # 2. Получаем сообщение для коммита из аргументов командной строки
    if len(sys.argv) < 2:
        print(f"{Colors.FAIL}❌ Ошибка: Пожалуйста, укажите сообщение для коммита.{Colors.ENDC}")
        print(f"{Colors.BOLD}Пример использования: python {os.path.basename(__file__)} \"Исправлен баг в авторизации\"{Colors.ENDC}")
        sys.exit(1) # Выходим с кодом ошибки

    commit_message = sys.argv[1]

    # 3. Список команд для выполнения
    commands = [
        ["git", "status"],
        ["git", "add", "."],
        ["git", "commit", "-m", commit_message],
        ["git", "push"]
    ]

    # 4. Выполняем каждую команду по очереди
    for cmd in commands:
        if not run_command(cmd, repo_path):
            print(f"\n{Colors.FAIL}--- 🛑 Процесс остановлен из-за ошибки. ---\n{Colors.ENDC}")
            sys.exit(1)

    print(f"\n{Colors.OKGREEN}--- ✨ Все команды успешно выполнены! ---\n{Colors.ENDC}")

if __name__ == "__main__":
    main()