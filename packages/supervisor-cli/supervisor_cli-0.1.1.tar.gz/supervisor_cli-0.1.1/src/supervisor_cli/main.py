#!/usr/bin/env python3
import subprocess
import sys
from typing import List, Tuple
import argparse


def run_cmd(cmd: List[str]) -> str:
    """Run a shell command and return its output as string."""
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()


def get_services() -> List[Tuple[str, str]]:
    """Fetch all supervisor services with their status."""
    output = run_cmd(["sudo", "supervisorctl", "status"])
    services = []
    for line in output.splitlines():
        parts = line.split()
        if len(parts) >= 2:
            services.append((parts[0], parts[1]))
    return services


def show_services(services: List[Tuple[str, str]]):
    """Display services with indices."""
    print("\nSupervisor Services")
    print("=" * 40)
    for i, (name, status) in enumerate(services, start=1):
        print(f"{i}) {name:<20} {status}")
    print("0) Exit")


def manage_service(service: str):
    """Show actions for a service and execute chosen one."""
    while True:
        print(f"\nActions for {service}:")
        print("1) Start")
        print("2) Stop")
        print("3) Restart")
        print("4) Tail logs")
        print("0) Back")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            print(run_cmd(["sudo", "supervisorctl", "start", service]))
        elif choice == "2":
            print(run_cmd(["sudo", "supervisorctl", "stop", service]))
        elif choice == "3":
            print(run_cmd(["sudo", "supervisorctl", "restart", service]))
        elif choice == "4":
            print("Press CTRL+C to exit logs.")
            try:
                subprocess.run(["sudo", "supervisorctl", "tail", "-f", service])
            except KeyboardInterrupt:
                print("\nReturning...")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def interactive_mode():
    """Run the interactive service manager."""
    while True:
        services = get_services()
        show_services(services)

        choice = input("Select a service (by number): ").strip()
        if choice == "0":
            print("Goodbye 👋")
            sys.exit(0)

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(services):
                manage_service(services[idx][0])
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a valid number.")


def cli():
    """CLI entrypoint with argparse."""
    parser = argparse.ArgumentParser(
        description="Interactive CLI tool to manage Supervisor services"
    )
    parser.add_argument("--list", action="store_true", help="List all services")
    parser.add_argument("--start", metavar="SERVICE", help="Start a service")
    parser.add_argument("--stop", metavar="SERVICE", help="Stop a service")
    parser.add_argument("--restart", metavar="SERVICE", help="Restart a service")
    parser.add_argument("--logs", metavar="SERVICE", help="Tail logs for a service")

    args = parser.parse_args()

    if args.list:
        services = get_services()
        show_services(services)
    elif args.start:
        print(run_cmd(["sudo", "supervisorctl", "start", args.start]))
    elif args.stop:
        print(run_cmd(["sudo", "supervisorctl", "stop", args.stop]))
    elif args.restart:
        print(run_cmd(["sudo", "supervisorctl", "restart", args.restart]))
    elif args.logs:
        try:
            subprocess.run(["sudo", "supervisorctl", "tail", "-f", args.logs])
        except KeyboardInterrupt:
            print("\nReturning...")
    else:
        interactive_mode()


def main():
    cli()
