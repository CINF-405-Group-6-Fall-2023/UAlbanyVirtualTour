#!/usr/bin/env python
"""Django's command-line utility for administrative tasks and setup."""

import os
import sys
from shutil import which
from functools import cache

# Install colorama and Django
os.system("pip install colorama django")

# Import colorama and initialize it for colored output on Windows
from colorama import init

init()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campusmap.settings')

# ANSI escape codes for text formatting
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"

def print_colored(message, color=RESET, style=""):
    """Print a colored message."""
    print(f"{style}{color}{message}{RESET}")

def print_checklist(step, status):
    """Print a checklist item with status."""
    checkbox = f"{BOLD}{GREEN}✓{RESET}" if status else f"{BOLD}{RED}✗{RESET}"
    print(f"    {checkbox} {step}")

def check_dependency(command, package_name):
    """Check if a system command is available."""
    return which(command) is not None

@cache
def is_running_in_virtualenv():
    """Check if the script is running inside a virtual environment."""
    return hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)

def run_server_locally():
    """Run the Django server locally."""
    os.system("python manage.py runserver")

def activate_virtualenv():
    """Activate the virtual environment."""
    if sys.platform == "win32":
        os.system(".\\campusmap\\Scripts\\activate")
    else:
        os.system("source campusmap/bin/activate")

def create_and_activate_virtualenv():
    """Create and activate the virtual environment."""
    try:
        os.system("python -m venv campusmap")
        print_checklist("1. Create and activate the virtual environment:", True)
    except Exception as e:
        print_checklist("1. Create and activate the virtual environment:", False)
        print_colored(f"Error: {e}\nPlease check if you have the necessary permissions to create a virtual environment.", RED)
        sys.exit(1)

    if sys.platform == "win32":
        try:
            activate_virtualenv()  # Activate the virtual environment
            print_checklist("1. Create and activate the virtual environment:", True)
        except Exception as e:
            print_checklist("1. Create and activate the virtual environment:", False)
            print_colored(f"Error: {e}\nPlease check if you have the necessary permissions to activate the virtual environment.", RED)
            sys.exit(1)

def install_django():
    """Install Django."""
    try:
        os.system("pip install -r requirements.txt")
        print_checklist("2. Install Django:", True)
    except Exception as e:
        print_checklist("2. Install Django:", False)
        print_colored(f"Error: {e}\nPlease check if you have the necessary permissions to install Django.", RED)
        sys.exit(1)

def install_dependencies():
    """Install missing dependencies."""
    print_colored("\nInstalling missing dependencies...", BLUE)
    dependencies = [
        ("python3", "Python"),
        ("pip", "Pip"),
        ("git", "Git"),
        ("django-admin", "Django"),
    ]

    for command, package_name in dependencies:
        status = check_dependency(command, package_name)
        if not status:
            print_colored(f"Installing {package_name}...", BLUE)
            os.system(f"python -m pip install {package_name}")

    print_colored("\nAll missing dependencies installed!", GREEN)

def setup():
    """Run setup tasks."""
    print_colored(f"{'='*40}\n{'Django Project Setup':^40}\n{'='*40}\n", BLUE, BOLD)

    # Dependency checklist
    dependencies = [
        ("python", "Python"),
        ("pip", "Pip"),
        ("git", "Git"),
        ("django-admin", "Django"),
    ]

    print_colored("Dependency Checklist:", BLUE, BOLD)
    for command, package_name in dependencies:
        status = check_dependency(command, package_name)
        print_checklist(f"{package_name} installed", status)

    if not all(dependencies):
        install_dependencies()

    print_colored("\nAll dependencies are installed!", GREEN)

    # Check if running in a virtual environment
    print_colored("\nVirtual Environment Check:", BLUE, BOLD)
    status = is_running_in_virtualenv()
    print_checklist("Script running in a virtual environment", status)

    if not status:
        # Virtual environment setup
        print_colored("\nVirtual Environment Setup:", BLUE, BOLD)
        create_and_activate_virtualenv()

        # Install Django
        install_django()

    # Running the server inside the virtual environment
    print_colored("\nRunning the server inside the virtual environment...", BLUE)
    run_server_locally()

    print_colored("\nSetup complete! You can now run your Django server inside the virtual environment.", GREEN, BOLD)
    print_colored("="*40, BLUE, BOLD)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'setup':
        setup()
    else:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)