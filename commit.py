import os
import subprocess
import sys

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt

console = Console()

# --- ВСПОМОГАТЕЛЬНЫЕ GIT-ФУНКЦИИ ---

def get_current_branch(working_dir):
    """Определяет текущую активную ветку Git."""
    try:
        result = subprocess.run(["git", "branch", "--show-current"], cwd=working_dir, check=True, capture_output=True, text=True, encoding='utf-8')
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

def branch_exists_locally(branch_name, working_dir):
    """Проверяет, существует ли ветка в локальном репозитории."""
    try:
        result = subprocess.run(["git", "branch", "--list", branch_name], cwd=working_dir, capture_output=True, text=True, check=True, encoding='utf-8')
        return bool(result.stdout.strip())
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def remote_branch_exists(branch_name, remote_name, working_dir):
    """Проверяет, существует ли ветка на удаленном сервере."""
    try:
        result = subprocess.run(["git", "ls-remote", "--heads", remote_name, branch_name], cwd=working_dir, capture_output=True, text=True, check=True, encoding='utf-8')
        return bool(result.stdout.strip())
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def get_upstream_branch(branch_name, working_dir):
    """Проверяет, есть ли у локальной ветки 'upstream' (связь с удаленной)."""
    try:
        # Эта команда упадет с ошибкой, если upstream не настроен
        result = subprocess.run(["git", "rev-parse", "--abbrev-ref", f"{branch_name}@{{u}}"], cwd=working_dir, check=True, capture_output=True, text=True, encoding='utf-8')
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
        
def run_command(command, working_dir):
    """Выполняет команду и красиво выводит результат."""
    console.print(f"▶️  Выполняю: [bold cyan]{' '.join(command)}[/bold cyan]")
    try:
        result = subprocess.run(command, cwd=working_dir, check=True, capture_output=True, text=True, encoding='utf-8')
        if result.stdout:
            console.print(Panel(result.stdout.strip(), title="[green]Вывод[/green]", title_align="left", border_style="green"))
        if result.stderr:
            console.print(Panel(result.stderr.strip(), title="[yellow]Предупреждения[/yellow]", title_align="left", border_style="yellow"))
        return True
    except FileNotFoundError:
        console.print(f"[bold red]❌ Ошибка: Команда '{command[0]}' не найдена.[/bold red]")
        return False
    except subprocess.CalledProcessError as e:
        error_message = e.stderr.strip() if e.stderr else e.stdout.strip()
        console.print(Panel(f"[bold]Команда завершилась с ошибкой (код {e.returncode}):[/bold]\n\n{error_message}", title="[bold red]Ошибка выполнения[/bold red]", title_align="left", border_style="red"))
        return False

# --- "МОЗГ" СКРИПТА ---

def check_and_switch_branch(branch_name, working_dir):
    """Проверяет наличие ветки и предлагает создать/переключиться на нее."""
    if branch_exists_locally(branch_name, working_dir):
        # Ветка уже есть локально, просто переключаемся
        return run_command(["git", "checkout", branch_name], working_dir)

    console.print(f"[yellow]Локальная ветка '[bold]{branch_name}[/bold]' не найдена.[/yellow]")
    console.print("🔄 Обновляю информацию с удаленного сервера (`git fetch`)...")
    if not run_command(["git", "fetch", "origin"], working_dir):
        return False

    if remote_branch_exists(branch_name, "origin", working_dir):
        # Сценарий: Ветка есть на сервере, но не локально
        console.print(f"✅ Найдена удаленная ветка 'origin/{branch_name}'.")
        if Confirm.ask(f"Создать локальную ветку '[bold]{branch_name}[/bold]' и переключиться на неё?"):
            return run_command(["git", "checkout", branch_name], working_dir)
        else:
            console.print("[red]Операция отменена.[/red]")
            return False
    else:
        # Сценарий: Ветки нет нигде
        console.print(f"❌ Удаленная ветка '[bold]{branch_name}[/bold]' также не найдена.")
        if Confirm.ask(f"Создать совершенно новую локальную ветку '[bold]{branch_name}[/bold]'?"):
            return run_command(["git", "checkout", "-b", branch_name], working_dir)
        else:
            console.print("[red]Операция отменена.[/red]")
            return False

# --- ОСНОВНАЯ ЛОГИКА ---

def main():
    repo_path = os.path.dirname(os.path.abspath(__file__))
    
    current_branch = get_current_branch(repo_path)
    header_text = f"Запуск Git-автоматизации в директории:\n[cyan]{repo_path}[/cyan]\n"
    if current_branch:
        header_text += f"Текущая ветка: [bold yellow]{current_branch}[/bold yellow]"
    
    console.print(Panel(header_text, title="[bold magenta]🚀 Git-Автоматор[/bold magenta]", expand=False, border_style="magenta"))
    
    if not current_branch:
        console.print("[bold red]Не удалось определить текущую ветку. Убедитесь, что это Git-репозиторий.[/bold red]"); sys.exit(1)

    commit_message = Prompt.ask("[bold yellow]📝 Введите сообщение для коммита[/bold yellow]")
    target_branch = Prompt.ask("[bold yellow]🎯 В какую ветку отправить изменения?[/bold yellow]", default="dev")
    console.print(f"Выбрана ветка для пуша: [bold green]{target_branch}[/bold green]"); console.print("-" * 30)

    if current_branch != target_branch:
        if not check_and_switch_branch(target_branch, repo_path):
            console.print("\n[bold red]--- 🛑 Процесс остановлен, так как не удалось перейти на целевую ветку. ---[/bold red]\n"); sys.exit(1)

    # Определяем, нужно ли делать --set-upstream для первого пуша
    is_new_branch = not get_upstream_branch(target_branch, repo_path)
    push_command = ["git", "push"]
    if is_new_branch:
        push_command.extend(["--set-upstream", "origin", target_branch])
        console.print(f"[bold yellow]Внимание:[/bold yellow] Ветка '[bold]{target_branch}[/bold]' новая. Первый пуш будет с флагом `--set-upstream`.")

    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", commit_message],
        push_command
    ]

    for cmd in commands:
        if not run_command(cmd, repo_path):
            console.print(f"\n[bold red]--- 🛑 Процесс остановлен из-за ошибки. ---[/bold red]\n"); sys.exit(1)
        console.print()

    console.print("\n[bold green]--- ✨ Все команды успешно выполнены! ---[/bold green]\n")

if __name__ == "__main__":
    main()