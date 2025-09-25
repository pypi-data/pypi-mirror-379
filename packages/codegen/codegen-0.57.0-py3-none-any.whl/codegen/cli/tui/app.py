"""Minimal TUI interface for Codegen CLI."""

import signal
import sys
import termios
import threading
import time
import tty
from datetime import datetime
from typing import Any

import requests
import typer

from codegen.cli.api.endpoints import API_ENDPOINT
from codegen.cli.auth.token_manager import get_current_org_name, get_current_token
from codegen.cli.commands.agent.main import pull
from codegen.cli.commands.claude.main import _run_claude_interactive
from codegen.cli.utils.org import resolve_org_id
from codegen.cli.utils.url import generate_webapp_url, get_domain
from codegen.shared.logging.get_logger import get_logger

# Initialize logger for TUI telemetry
logger = get_logger(__name__)


class MinimalTUI:
    """Minimal non-full-screen TUI for browsing agent runs."""

    def __init__(self):
        # Log TUI initialization
        logger.info("TUI session started", extra={"operation": "tui.init", "component": "minimal_tui"})

        self.token = get_current_token()
        self.is_authenticated = bool(self.token)
        if self.is_authenticated:
            self.org_id = resolve_org_id()
            logger.info("TUI authenticated successfully", extra={"operation": "tui.auth", "org_id": self.org_id, "authenticated": True})
        else:
            logger.warning("TUI started without authentication", extra={"operation": "tui.auth", "authenticated": False})

        self.agent_runs: list[dict[str, Any]] = []
        self.selected_index = 0
        self.running = True
        self.show_action_menu = False
        self.action_menu_selection = 0

        # Tab management
        self.tabs = ["recent", "claude", "new", "kanban"]
        self.current_tab = 0

        # Refresh state
        self.is_refreshing = False
        self.initial_loading = True  # Track if we're still doing the initial load
        self._auto_refresh_interval_seconds = 10
        self._refresh_lock = threading.Lock()

        # New tab state
        self.prompt_input = ""

        self.cursor_position = 0
        self.input_mode = False  # When true, we're typing in the input box

        # Set up signal handler for Ctrl+C
        signal.signal(signal.SIGINT, self._signal_handler)

        # Start background auto-refresh thread (daemon)
        self._auto_refresh_thread = threading.Thread(target=self._auto_refresh_loop, daemon=True)
        self._auto_refresh_thread.start()

        logger.debug("TUI initialization completed", extra={"operation": "tui.init", "tabs": self.tabs, "auto_refresh_interval": self._auto_refresh_interval_seconds})

    def _auto_refresh_loop(self):
        """Background loop to auto-refresh recent tab every interval."""
        while True:
            # Sleep first so we don't immediately spam a refresh on start
            time.sleep(self._auto_refresh_interval_seconds)

            if not self.running:
                break

            # Only refresh when on recent tab and not currently refreshing
            if self.current_tab == 0 and not self.is_refreshing:
                # Try background refresh; if lock is busy, skip this tick
                acquired = self._refresh_lock.acquire(blocking=False)
                if not acquired:
                    continue
                try:
                    # Double-check state after acquiring lock
                    if self.running and self.current_tab == 0 and not self.is_refreshing:
                        self._background_refresh()
                finally:
                    self._refresh_lock.release()

    def _background_refresh(self):
        """Refresh data without disrupting selection/menu state; redraw if still on recent."""
        self.is_refreshing = True
        # Do not redraw immediately to reduce flicker; header shows indicator on next paint

        previous_index = self.selected_index
        try:
            if self._load_agent_runs():
                # Preserve selection but clamp to new list bounds
                if self.agent_runs:
                    self.selected_index = max(0, min(previous_index, len(self.agent_runs) - 1))
                else:
                    self.selected_index = 0
        finally:
            self.is_refreshing = False

        # Redraw only if still on recent and app running
        if self.running and self.current_tab == 0:
            self._clear_and_redraw()

    def _get_webapp_domain(self) -> str:
        """Get the webapp domain based on environment."""
        return get_domain()

    def _generate_agent_url(self, agent_id: str) -> str:
        """Generate the complete agent URL."""
        return generate_webapp_url(f"x/{agent_id}")

    def _signal_handler(self, signum, frame):
        """Handle Ctrl+C gracefully without clearing screen."""
        self.running = False
        print("\n")  # Just add a newline and exit
        sys.exit(0)

    def _format_status_line(self, left_text: str) -> str:
        """Format status line with instructions and org info on a new line below."""
        # Get organization name
        org_name = get_current_org_name()
        if not org_name:
            org_name = f"Org {self.org_id}" if hasattr(self, "org_id") and self.org_id else "No Org"

        # Use the same purple color as the Codegen logo
        purple_color = "\033[38;2;82;19;217m"
        reset_color = "\033[0m"

        # Return instructions on first line, org on second line (bottom left)
        instructions_line = f"\033[90m{left_text}\033[0m"
        org_line = f"{purple_color}• {org_name}{reset_color}"

        # Append a subtle refresh indicator when a refresh is in progress
        if getattr(self, "is_refreshing", False):
            org_line += "  \033[90m■ Refreshing…\033[0m"

        return f"{instructions_line}\n{org_line}"

    def _load_agent_runs(self) -> bool:
        """Load the last 10 agent runs."""
        if not self.token or not self.org_id:
            logger.warning("Cannot load agent runs - missing auth", extra={"operation": "tui.load_agent_runs", "has_token": bool(self.token), "has_org_id": bool(getattr(self, "org_id", None))})
            return False

        start_time = time.time()

        # Only log debug info for initial load, not refreshes
        is_initial_load = not hasattr(self, "_has_loaded_before")
        if is_initial_load:
            logger.debug("Loading agent runs", extra={"operation": "tui.load_agent_runs", "org_id": self.org_id, "is_initial_load": True})

        try:
            import requests

            from codegen.cli.api.endpoints import API_ENDPOINT

            headers = {"Authorization": f"Bearer {self.token}"}

            # Get current user ID
            user_response = requests.get(f"{API_ENDPOINT.rstrip('/')}/v1/users/me", headers=headers)
            user_response.raise_for_status()
            user_data = user_response.json()
            user_id = user_data.get("id")

            # Fetch agent runs - limit to 10
            params = {
                "source_type": "API",
                "limit": 10,
            }

            if user_id:
                params["user_id"] = user_id

            url = f"{API_ENDPOINT.rstrip('/')}/v1/organizations/{self.org_id}/agent/runs"
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            response_data = response.json()

            self.agent_runs = response_data.get("items", [])
            self.initial_loading = False  # Mark initial loading as complete

            duration_ms = (time.time() - start_time) * 1000

            # Only log the initial load, not refreshes to avoid noise
            is_initial_load = not hasattr(self, "_has_loaded_before")
            if is_initial_load:
                logger.info(
                    "Agent runs loaded successfully",
                    extra={
                        "operation": "tui.load_agent_runs",
                        "org_id": self.org_id,
                        "user_id": user_id,
                        "agent_count": len(self.agent_runs),
                        "duration_ms": duration_ms,
                        "is_initial_load": True,
                    },
                )

            # Mark that we've loaded at least once
            self._has_loaded_before = True
            return True

        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            # Always log errors regardless of refresh vs initial load
            logger.error(
                "Failed to load agent runs",
                extra={"operation": "tui.load_agent_runs", "org_id": self.org_id, "error_type": type(e).__name__, "error_message": str(e), "duration_ms": duration_ms},
                exc_info=True,
            )
            print(f"Error loading agent runs: {e}")
            return False

    def _format_status(self, status: str, agent_run: dict | None = None) -> tuple[str, str]:
        """Format status with colored indicators matching kanban style."""
        # Check if this agent has a merged PR (done status)
        is_done = False
        if agent_run:
            github_prs = agent_run.get("github_pull_requests", [])
            for pr in github_prs:
                if pr.get("state") == "closed" and pr.get("merged", False):
                    is_done = True
                    break

        if is_done:
            return "\033[38;2;130;226;255m✓\033[0m", "done"  # aura blue #82e2ff checkmark for merged PR

        status_map = {
            "COMPLETE": "\033[38;2;66;196;153m○\033[0m",  # oklch(43.2% 0.095 166.913) ≈ rgb(66,196,153) hollow circle
            "ACTIVE": "\033[38;2;162;119;255m○\033[0m",  # aura purple #a277ff (hollow circle)
            "RUNNING": "\033[38;2;162;119;255m●\033[0m",  # aura purple #a277ff
            "ERROR": "\033[38;2;255;103;103m○\033[0m",  # aura red #ff6767 (empty circle)
            "FAILED": "\033[38;2;255;103;103m○\033[0m",  # aura red #ff6767 (empty circle)
            "CANCELLED": "\033[38;2;109;109;109m○\033[0m",  # aura gray #6d6d6d
            "STOPPED": "\033[38;2;109;109;109m○\033[0m",  # aura gray #6d6d6d
            "PENDING": "\033[38;2;109;109;109m○\033[0m",  # aura gray #6d6d6d
            "TIMEOUT": "\033[38;2;255;202;133m●\033[0m",  # aura orange #ffca85
            "MAX_ITERATIONS_REACHED": "\033[38;2;255;202;133m●\033[0m",  # aura orange #ffca85
            "OUT_OF_TOKENS": "\033[38;2;255;202;133m●\033[0m",  # aura orange #ffca85
            "EVALUATION": "\033[38;2;246;148;255m●\033[0m",  # aura pink #f694ff
        }

        status_text_map = {
            "COMPLETE": "complete",
            "ACTIVE": "active",
            "RUNNING": "running",
            "ERROR": "error",
            "FAILED": "failed",
            "CANCELLED": "cancelled",
            "STOPPED": "stopped",
            "PENDING": "pending",
            "TIMEOUT": "timeout",
            "MAX_ITERATIONS_REACHED": "max iterations",
            "OUT_OF_TOKENS": "out of tokens",
            "EVALUATION": "evaluation",
        }

        circle = status_map.get(status, "\033[37m○\033[0m")
        text = status_text_map.get(status, status.lower() if status else "unknown")
        return circle, text

    def _format_pr_info(self, agent_run: dict) -> str:
        """Format PR information as 'PR #123' or empty string."""
        github_prs = agent_run.get("github_pull_requests", [])
        if not github_prs:
            return ""

        pr = github_prs[0]  # Take the first PR
        pr_url = pr.get("url", "")
        if not pr_url:
            return ""

        # Extract PR number from URL like "https://github.com/org/repo/pull/123"
        try:
            pr_number = pr_url.split("/pull/")[-1].split("/")[0]
            return f"PR #{pr_number}"
        except (IndexError, AttributeError):
            return ""

    def _strip_ansi_codes(self, text: str) -> str:
        """Strip ANSI color codes from text."""
        import re

        ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
        return ansi_escape.sub("", text)

    def _format_date(self, created_at: str) -> str:
        """Format creation date."""
        if not created_at or created_at == "Unknown":
            return "Unknown"

        try:
            dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
            return dt.strftime("%m/%d %H:%M")
        except (ValueError, TypeError):
            return created_at[:16] if len(created_at) > 16 else created_at

    def _display_header(self):
        """Display the header with tabs."""
        # Simple header with indigo slashes and Codegen text
        print("\033[38;2;82;19;217m" + "/" * 20 + " Codegen\033[0m")
        print()  # Add blank line between header and tabs

        # Display tabs
        tab_line = ""
        for i, tab in enumerate(self.tabs):
            if i == self.current_tab:
                tab_line += f"\033[38;2;255;202;133m/{tab}\033[0m  "  # Orange for active tab with slash
            else:
                tab_line += f"\033[90m{tab}\033[0m  "  # Gray for inactive tabs

        print(tab_line)
        print()

    def _display_agent_list(self):
        """Display the list of agent runs, fixed to 10 lines of main content."""
        if not self.agent_runs:
            if self.initial_loading:
                print("Loading...")
            else:
                print("No agent runs found.")
            self._pad_to_lines(1)
            return

        # Determine how many extra lines the inline action menu will print (if open)
        menu_lines = 0
        if self.show_action_menu and 0 <= self.selected_index < len(self.agent_runs):
            selected_run = self.agent_runs[self.selected_index]
            github_prs = selected_run.get("github_pull_requests", [])
            options_count = 1  # "open in web"
            if github_prs:
                options_count += 1  # "pull locally"
            if github_prs and github_prs[0].get("url"):
                options_count += 1  # "open PR"
            menu_lines = options_count + 1  # +1 for the hint line

        # We want total printed lines (rows + menu) to be 10
        window_size = max(1, 10 - menu_lines)

        total = len(self.agent_runs)
        if total <= window_size:
            start = 0
            end = total
        else:
            start = max(0, min(self.selected_index - window_size // 2, total - window_size))
            end = start + window_size

        printed_rows = 0
        for i in range(start, end):
            agent_run = self.agent_runs[i]
            # Highlight selected item
            prefix = "→ " if i == self.selected_index and not self.show_action_menu else "  "

            status_circle, status_text = self._format_status(agent_run.get("status", "Unknown"), agent_run)
            created = self._format_date(agent_run.get("created_at", "Unknown"))
            summary = agent_run.get("summary", "No summary") or "No summary"

            # Append PR info to summary if available
            pr_info = self._format_pr_info(agent_run)
            if pr_info:
                summary = f"{summary} ({pr_info})"

            if len(summary) > 60:
                summary = summary[:57] + "..."

            # Calculate display width of status (without ANSI codes) for alignment
            status_display = f"{status_circle} {status_text}"
            status_display_width = len(self._strip_ansi_codes(status_display))
            status_padding = " " * max(0, 17 - status_display_width)

            if i == self.selected_index and not self.show_action_menu:
                line = f"\033[37m{prefix}{created:<10}\033[0m {status_circle} \033[37m{status_text}\033[0m{status_padding}\033[37m{summary}\033[0m"
            else:
                line = f"\033[90m{prefix}{created:<10}\033[0m {status_circle} \033[90m{status_text}\033[0m{status_padding}\033[90m{summary}\033[0m"

            print(line)
            printed_rows += 1

            # Show action menu right below the selected row if it's expanded
            if i == self.selected_index and self.show_action_menu:
                self._display_inline_action_menu(agent_run)

        # If fewer than needed to reach 10 lines, pad blank lines
        total_printed = printed_rows + menu_lines
        if total_printed < 10:
            self._pad_to_lines(total_printed)

    def _display_new_tab(self):
        """Display the new agent creation interface."""
        print("Create new background agent (Claude Code):")
        print()

        # Get terminal width, default to 80 if can't determine
        try:
            import os

            terminal_width = os.get_terminal_size().columns
        except (OSError, AttributeError):
            terminal_width = 80

        # Calculate input box width (leave some margin)
        box_width = max(60, terminal_width - 4)

        # Input box with cursor
        input_display = self.prompt_input
        if self.input_mode:
            # Add cursor indicator when in input mode
            if self.cursor_position <= len(input_display):
                input_display = input_display[: self.cursor_position] + "█" + input_display[self.cursor_position :]

        # Handle long input that exceeds box width
        if len(input_display) > box_width - 4:
            # Show portion around cursor
            start_pos = max(0, self.cursor_position - (box_width // 2))
            input_display = input_display[start_pos : start_pos + box_width - 4]

        # Display full-width input box with simple border like Claude Code
        border_style = "\033[37m" if self.input_mode else "\033[90m"  # White when active, gray when inactive
        reset = "\033[0m"

        print(border_style + "┌" + "─" * (box_width - 2) + "┐" + reset)
        padding = box_width - 4 - len(input_display.replace("█", ""))
        print(border_style + "│" + reset + f" {input_display}{' ' * max(0, padding)} " + border_style + "│" + reset)
        print(border_style + "└" + "─" * (box_width - 2) + "┘" + reset)
        print()

        # The new tab main content area should be a fixed 10 lines
        self._pad_to_lines(6)

    def _create_background_agent(self, prompt: str):
        """Create a background agent run."""
        logger.info("Creating background agent via TUI", extra={"operation": "tui.create_agent", "org_id": getattr(self, "org_id", None), "prompt_length": len(prompt), "client": "tui"})

        if not self.token or not self.org_id:
            logger.error("Cannot create agent - missing auth", extra={"operation": "tui.create_agent", "has_token": bool(self.token), "has_org_id": bool(getattr(self, "org_id", None))})
            print("\n❌ Not authenticated or no organization configured.")
            input("Press Enter to continue...")
            return

        if not prompt.strip():
            logger.warning("Agent creation cancelled - empty prompt", extra={"operation": "tui.create_agent", "org_id": self.org_id, "prompt_length": len(prompt)})
            print("\n❌ Please enter a prompt.")
            input("Press Enter to continue...")
            return

        print(f"\n\033[90mCreating agent run with prompt: '{prompt[:50]}{'...' if len(prompt) > 50 else ''}'\033[0m")

        start_time = time.time()
        try:
            payload = {"prompt": prompt.strip()}
            headers = {
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
                "x-codegen-client": "codegen__claude_code",
            }
            url = f"{API_ENDPOINT.rstrip('/')}/v1/organizations/{self.org_id}/agent/run"

            # API request details not needed in logs - focus on user actions and results

            response = requests.post(url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            agent_run_data = response.json()

            run_id = agent_run_data.get("id", "Unknown")
            status = agent_run_data.get("status", "Unknown")
            web_url = self._generate_agent_url(run_id)

            duration_ms = (time.time() - start_time) * 1000
            logger.info(
                "Background agent created successfully",
                extra={"operation": "tui.create_agent", "org_id": self.org_id, "agent_run_id": run_id, "status": status, "duration_ms": duration_ms, "prompt_length": len(prompt.strip())},
            )

            print("\n\033[90mAgent run created successfully!\033[0m")
            print(f"\033[90m   Run ID: {run_id}\033[0m")
            print(f"\033[90m   Status: {status}\033[0m")
            print(f"\033[90m   Web URL: \033[38;2;255;202;133m{web_url}\033[0m")

            # Clear the input
            self.prompt_input = ""
            self.cursor_position = 0
            self.input_mode = False

            # Show post-creation menu
            self._show_post_creation_menu(web_url)

        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(
                "Failed to create background agent",
                extra={"operation": "tui.create_agent", "org_id": self.org_id, "error_type": type(e).__name__, "error_message": str(e), "duration_ms": duration_ms, "prompt_length": len(prompt)},
                exc_info=True,
            )
            print(f"\n❌ Failed to create agent run: {e}")
            input("\nPress Enter to continue...")

    def _show_post_creation_menu(self, web_url: str):
        """Show menu after successful agent creation."""
        from codegen.cli.utils.inplace_print import inplace_print

        print("\n\033[90mWhat would you like to do next?\033[0m")
        options = ["Open Trace ↗", "Go to Recent"]
        selected = 0
        prev_lines = 0

        def build_lines():
            menu_lines = []
            # Options
            for i, option in enumerate(options):
                if i == selected:
                    menu_lines.append(f"    \033[37m→ {option}\033[0m")
                else:
                    menu_lines.append(f"    \033[90m  {option}\033[0m")
            # Hint line last
            menu_lines.append("\033[90m[Enter] select • [↑↓] navigate • [B] back to new tab\033[0m")
            return menu_lines

        # Initial render
        prev_lines = inplace_print(build_lines(), prev_lines)

        while True:
            key = self._get_char()
            if key == "\x1b[A" or key.lower() == "w":  # Up arrow or W
                selected = (selected - 1) % len(options)
                prev_lines = inplace_print(build_lines(), prev_lines)
            elif key == "\x1b[B" or key.lower() == "s":  # Down arrow or S
                selected = (selected + 1) % len(options)
                prev_lines = inplace_print(build_lines(), prev_lines)
            elif key == "\r" or key == "\n":  # Enter - select option
                if selected == 0:  # Open Trace
                    try:
                        import webbrowser

                        webbrowser.open(web_url)
                    except Exception as e:
                        print(f"\n❌ Failed to open browser: {e}")
                        input("Press Enter to continue...")
                elif selected == 1:  # Go to Recent
                    self.current_tab = 0  # Switch to recent tab
                    self.input_mode = False
                    self._load_agent_runs()  # Refresh the data
                break
            elif key == "B":  # Back to new tab
                self.current_tab = 2  # 'new' tab index
                self.input_mode = True
                break

    def _display_dashboard_tab(self):
        """Display the kanban interface access tab."""
        # Generate the proper domain-based URL for display
        me_url = generate_webapp_url("me")
        display_url = me_url.replace("https://", "").replace("http://", "")

        print(f"  \033[37m→ Open Kanban ({display_url})\033[0m")
        print()
        print("Press Enter to open web kanban.")
        # The kanban tab main content area should be a fixed 10 lines
        self._pad_to_lines(7)

    def _display_claude_tab(self):
        """Display the Claude Code interface tab."""
        # Check if Claude Code is installed
        from codegen.cli.commands.claude.utils import resolve_claude_path

        claude_path = resolve_claude_path()
        if not claude_path:
            # Display error message when Claude is not installed
            print("  \033[31m✗ Claude Code Not Installed\033[0m")
            print()
            print("\033[33m⚠ Claude Code CLI is not installed or cannot be found.\033[0m")
            print()
            print("To install Claude Code:")
            print("  • Install globally: \033[36mnpm install -g @anthropic-ai/claude-code\033[0m")
            print("  • Or run: \033[36mclaude /migrate-installer\033[0m for local installation")
            print()
            print("Once installed, restart this CLI to use Claude Code.")
        else:
            print("  \033[37m→ Run Claude Code\033[0m")
            print()
            print("Press Enter to launch Claude Code with session tracking.")

        # The claude tab main content area should be a fixed 10 lines
        self._pad_to_lines(7)

    def _pull_agent_branch(self, agent_id: str):
        """Pull the PR branch for an agent run locally."""
        logger.info("Starting local pull via TUI", extra={"operation": "tui.pull_branch", "agent_id": agent_id, "org_id": getattr(self, "org_id", None)})

        print(f"\n🔄 Pulling PR branch for agent {agent_id}...")
        print("─" * 50)

        start_time = time.time()
        try:
            # Call the existing pull command with the agent_id
            pull(agent_id=int(agent_id), org_id=self.org_id)

            duration_ms = (time.time() - start_time) * 1000
            logger.info("Local pull completed successfully", extra={"operation": "tui.pull_branch", "agent_id": agent_id, "org_id": self.org_id, "duration_ms": duration_ms, "success": True})

        except typer.Exit as e:
            duration_ms = (time.time() - start_time) * 1000
            # typer.Exit is expected for both success and failure cases
            if e.exit_code == 0:
                logger.info(
                    "Local pull completed via typer exit",
                    extra={"operation": "tui.pull_branch", "agent_id": agent_id, "org_id": self.org_id, "duration_ms": duration_ms, "exit_code": e.exit_code, "success": True},
                )
                print("\n✅ Pull completed successfully!")
            else:
                logger.error(
                    "Local pull failed via typer exit",
                    extra={"operation": "tui.pull_branch", "agent_id": agent_id, "org_id": self.org_id, "duration_ms": duration_ms, "exit_code": e.exit_code, "success": False},
                )
                print(f"\n❌ Pull failed (exit code: {e.exit_code})")
        except ValueError:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(
                "Invalid agent ID for pull",
                extra={"operation": "tui.pull_branch", "agent_id": agent_id, "org_id": getattr(self, "org_id", None), "duration_ms": duration_ms, "error_type": "invalid_agent_id"},
            )
            print(f"\n❌ Invalid agent ID: {agent_id}")
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(
                "Unexpected error during pull",
                extra={
                    "operation": "tui.pull_branch",
                    "agent_id": agent_id,
                    "org_id": getattr(self, "org_id", None),
                    "duration_ms": duration_ms,
                    "error_type": type(e).__name__,
                    "error_message": str(e),
                },
                exc_info=True,
            )
            print(f"\n❌ Unexpected error during pull: {e}")

        print("─" * 50)
        input("Press Enter to continue...")

    def _display_content(self):
        """Display content based on current tab."""
        if self.current_tab == 0:  # recent
            self._display_agent_list()
        elif self.current_tab == 1:  # claude
            self._display_claude_tab()
        elif self.current_tab == 2:  # new
            self._display_new_tab()
        elif self.current_tab == 3:  # kanban
            self._display_dashboard_tab()

    def _pad_to_lines(self, lines_printed: int, target: int = 10):
        """Pad the main content area with blank lines to reach a fixed height."""
        for _ in range(max(0, target - lines_printed)):
            print()

    def _display_inline_action_menu(self, agent_run: dict):
        """Display action menu inline below the selected row."""
        agent_id = agent_run.get("id", "unknown")
        web_url = self._generate_agent_url(agent_id)

        # Check if there are GitHub PRs associated with this agent run
        github_prs = agent_run.get("github_pull_requests", [])

        # Build options in the requested order
        options = []

        # 1. Open PR (if available)
        if github_prs:
            pr_url = github_prs[0].get("url", "")
            if pr_url:
                # Extract PR number for display
                try:
                    pr_number = pr_url.split("/pull/")[-1].split("/")[0]
                    options.append(f"Open PR #{pr_number} ↗")
                except (IndexError, AttributeError):
                    options.append("Open PR ↗")

        # 2. Pull locally (if PRs available)
        if github_prs:
            options.append("Pull locally")

        # 3. Open Trace (always available)
        options.append("Open Trace ↗")

        for i, option in enumerate(options):
            if i == self.action_menu_selection:
                # Highlight selected option in white
                print(f"    \033[37m→ {option}\033[0m")
            else:
                # All other options in gray
                print(f"    \033[90m  {option}\033[0m")

        print("\033[90m    [Enter] select • [↑↓] navigate • [C] close\033[0m")

    def _get_char(self):
        """Get a single character from stdin, handling arrow keys."""
        try:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setcbreak(fd)
                ch = sys.stdin.read(1)

                # Handle escape sequences (arrow keys)
                if ch == "\x1b":  # ESC
                    # Read the rest of the escape sequence synchronously
                    ch2 = sys.stdin.read(1)
                    if ch2 == "[":
                        ch3 = sys.stdin.read(1)
                        return f"\x1b[{ch3}"
                    else:
                        # Return combined sequence (e.g., Alt+<key>)
                        return ch + ch2
                return ch
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        except (ImportError, OSError, termios.error):
            # Fallback for systems where tty manipulation doesn't work
            print("\nUse: ↑(w)/↓(s) navigate, Enter details, R refresh, Q quit")
            try:
                return input("> ").strip()[:1].lower() or "\n"
            except KeyboardInterrupt:
                return "q"

    def _handle_keypress(self, key: str):
        """Handle key presses for navigation."""
        # Global quit (but not when typing in new tab)
        if key == "\x03":  # Ctrl+C
            logger.info(
                "TUI session ended by user",
                extra={
                    "operation": "tui.session_end",
                    "org_id": getattr(self, "org_id", None),
                    "reason": "ctrl_c",
                    "current_tab": self.tabs[self.current_tab] if self.current_tab < len(self.tabs) else "unknown",
                },
            )
            self.running = False
            return
        elif key.lower() == "q" and not (self.input_mode and self.current_tab == 2):  # q only if not typing in new tab
            logger.info(
                "TUI session ended by user",
                extra={
                    "operation": "tui.session_end",
                    "org_id": getattr(self, "org_id", None),
                    "reason": "quit_key",
                    "current_tab": self.tabs[self.current_tab] if self.current_tab < len(self.tabs) else "unknown",
                },
            )
            self.running = False
            return

        # Tab switching (works even in input mode)
        if key == "\t":  # Tab key
            old_tab = self.current_tab
            self.current_tab = (self.current_tab + 1) % len(self.tabs)

            # Log significant tab switches but at info level since it's user action
            logger.info(
                f"TUI tab switched to {self.tabs[self.current_tab]}",
                extra={
                    "operation": "tui.tab_switch",
                    "from_tab": self.tabs[old_tab] if old_tab < len(self.tabs) else "unknown",
                    "to_tab": self.tabs[self.current_tab] if self.current_tab < len(self.tabs) else "unknown",
                },
            )

            # Reset state when switching tabs
            self.show_action_menu = False
            self.action_menu_selection = 0
            self.selected_index = 0
            # Auto-focus prompt when switching to new tab
            if self.current_tab == 2:  # new tab
                self.input_mode = True
                self.cursor_position = len(self.prompt_input)
            else:
                self.input_mode = False
            return

        # Handle based on current context
        if self.input_mode:
            self._handle_input_mode_keypress(key)
        elif self.show_action_menu:
            self._handle_action_menu_keypress(key)
        elif self.current_tab == 0:  # recent tab
            self._handle_recent_keypress(key)
        elif self.current_tab == 1:  # claude tab
            self._handle_claude_tab_keypress(key)
        elif self.current_tab == 2:  # new tab
            self._handle_new_tab_keypress(key)
        elif self.current_tab == 3:  # kanban tab
            self._handle_dashboard_tab_keypress(key)

    def _handle_input_mode_keypress(self, key: str):
        """Handle keypresses when in text input mode."""
        if key == "B":  # Back action in new tab
            self.input_mode = False
        elif key == "\r" or key == "\n":  # Enter - create agent run
            if self.prompt_input.strip():  # Only create if there's actual content
                self._create_background_agent(self.prompt_input)
            else:
                self.input_mode = False  # Exit input mode if empty
        elif key == "\x7f" or key == "\b":  # Backspace
            if self.cursor_position > 0:
                self.prompt_input = self.prompt_input[: self.cursor_position - 1] + self.prompt_input[self.cursor_position :]
                self.cursor_position -= 1
        elif key == "\x1b[C":  # Right arrow
            self.cursor_position = min(len(self.prompt_input), self.cursor_position + 1)
        elif key == "\x1b[D":  # Left arrow
            self.cursor_position = max(0, self.cursor_position - 1)
        elif len(key) == 1 and key.isprintable():  # Regular character
            self.prompt_input = self.prompt_input[: self.cursor_position] + key + self.prompt_input[self.cursor_position :]
            self.cursor_position += 1

    def _handle_action_menu_keypress(self, key: str):
        """Handle action menu keypresses."""
        if key == "\r" or key == "\n":  # Enter
            self._execute_inline_action()
            self.show_action_menu = False  # Close menu after action
        elif key.lower() == "c" or key == "\x1b[D":  # 'C' key or Left arrow to close
            self.show_action_menu = False  # Close menu
            self.action_menu_selection = 0  # Reset selection
        elif key == "\x1b[A" or key.lower() == "w":  # Up arrow or W
            # Get available options count
            if 0 <= self.selected_index < len(self.agent_runs):
                agent_run = self.agent_runs[self.selected_index]
                github_prs = agent_run.get("github_pull_requests", [])
                options_count = 1  # Always have "Open Trace"
                if github_prs:
                    options_count += 1  # "Pull locally"
                if github_prs and github_prs[0].get("url"):
                    options_count += 1  # "Open PR"

                self.action_menu_selection = max(0, self.action_menu_selection - 1)
        elif key == "\x1b[B" or key.lower() == "s":  # Down arrow or S
            # Get available options count
            if 0 <= self.selected_index < len(self.agent_runs):
                agent_run = self.agent_runs[self.selected_index]
                github_prs = agent_run.get("github_pull_requests", [])
                options_count = 1  # Always have "Open Trace"
                if github_prs:
                    options_count += 1  # "Pull locally"
                if github_prs and github_prs[0].get("url"):
                    options_count += 1  # "Open PR"

                self.action_menu_selection = min(options_count - 1, self.action_menu_selection + 1)

    def _handle_recent_keypress(self, key: str):
        """Handle keypresses in the recent tab."""
        if key == "\x1b[A" or key.lower() == "w":  # Up arrow or W
            self.selected_index = max(0, self.selected_index - 1)
            self.show_action_menu = False  # Close any open menu
            self.action_menu_selection = 0
        elif key == "\x1b[B" or key.lower() == "s":  # Down arrow or S
            self.selected_index = min(len(self.agent_runs) - 1, self.selected_index + 1)
            self.show_action_menu = False  # Close any open menu
            self.action_menu_selection = 0
        elif key == "\x1b[C":  # Right arrow - open action menu
            self.show_action_menu = True  # Open action menu
            self.action_menu_selection = 0  # Reset to first option
        elif key == "\x1b[D":  # Left arrow - close action menu
            self.show_action_menu = False  # Close action menu
            self.action_menu_selection = 0
        elif key == "\r" or key == "\n" or key.lower() == "e":  # Enter or E
            self.show_action_menu = True  # Open action menu
            self.action_menu_selection = 0  # Reset to first option
        elif key.lower() == "r":
            self._refresh()
            self.show_action_menu = False  # Close menu on refresh
            self.action_menu_selection = 0

    def _handle_new_tab_keypress(self, key: str):
        """Handle keypresses in the new tab."""
        if key == "\r" or key == "\n":  # Enter - start input mode
            if not self.input_mode:
                self.input_mode = True
                self.cursor_position = len(self.prompt_input)
            else:
                # If already in input mode, Enter should create the agent
                self._create_background_agent(self.prompt_input)

    def _handle_dashboard_tab_keypress(self, key: str):
        """Handle keypresses in the kanban tab."""
        if key == "\r" or key == "\n":  # Enter - open web kanban
            logger.info("Opening web kanban from TUI", extra={"operation": "tui.open_kanban", "org_id": getattr(self, "org_id", None)})
            try:
                import webbrowser

                me_url = generate_webapp_url("me")
                webbrowser.open(me_url)
                # Debug details not needed for successful browser opens
            except Exception as e:
                logger.error("Failed to open kanban in browser", extra={"operation": "tui.open_kanban", "error": str(e)})
                print(f"\n❌ Failed to open browser: {e}")
                input("Press Enter to continue...")

    def _handle_claude_tab_keypress(self, key: str):
        """Handle keypresses in the claude tab."""
        if key == "\r" or key == "\n":  # Enter - run Claude Code
            # Check if Claude is installed before attempting to run
            from codegen.cli.commands.claude.utils import resolve_claude_path

            claude_path = resolve_claude_path()
            if not claude_path:
                # Claude is not installed, don't try to launch
                logger.warning("Attempted to launch Claude Code but it's not installed", extra={"operation": "tui.launch_claude", "error": "not_installed"})
                return

            self._run_claude_code()

    def _run_claude_code(self):
        """Launch Claude Code with session tracking."""
        logger.info("Launching Claude Code from TUI", extra={"operation": "tui.launch_claude", "org_id": getattr(self, "org_id", None), "source": "tui"})

        if not self.token or not self.org_id:
            logger.error("Cannot launch Claude - missing auth", extra={"operation": "tui.launch_claude", "has_token": bool(self.token), "has_org_id": bool(getattr(self, "org_id", None))})
            print("\n❌ Not authenticated or no organization configured.")
            input("Press Enter to continue...")
            return

        # Show immediate feedback in orange
        print("\n\033[38;2;255;202;133m> claude code mode\033[0m")

        # Stop the TUI and clear screen completely after brief moment
        self.running = False
        print("\033[2J\033[H", end="")  # Clear entire screen and move cursor to top

        start_time = time.time()
        try:
            # Transition details not needed - the launch and completion logs are sufficient

            # Call the interactive claude function with the current org_id
            # The function handles all the session tracking and launching
            _run_claude_interactive(self.org_id, no_mcp=False)

            duration_ms = (time.time() - start_time) * 1000
            logger.info("Claude Code session completed via TUI", extra={"operation": "tui.launch_claude", "org_id": self.org_id, "duration_ms": duration_ms, "exit_reason": "normal"})

        except typer.Exit:
            # Claude Code finished, just continue silently
            duration_ms = (time.time() - start_time) * 1000
            logger.info("Claude Code session exited via TUI", extra={"operation": "tui.launch_claude", "org_id": self.org_id, "duration_ms": duration_ms, "exit_reason": "typer_exit"})
            pass
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(
                "Error launching Claude Code from TUI",
                extra={"operation": "tui.launch_claude", "org_id": self.org_id, "error_type": type(e).__name__, "error_message": str(e), "duration_ms": duration_ms},
                exc_info=True,
            )
            print(f"\n❌ Unexpected error launching Claude Code: {e}")
            input("Press Enter to continue...")

        # Exit the TUI completely - don't return to it
        logger.info("TUI session ended - transitioning to Claude", extra={"operation": "tui.session_end", "org_id": getattr(self, "org_id", None), "reason": "claude_launch"})
        sys.exit(0)

    def _execute_inline_action(self):
        """Execute the selected action from the inline menu."""
        if not (0 <= self.selected_index < len(self.agent_runs)):
            return

        agent_run = self.agent_runs[self.selected_index]
        agent_id = agent_run.get("id", "unknown")
        web_url = self._generate_agent_url(agent_id)

        # Build options in the same order as display
        github_prs = agent_run.get("github_pull_requests", [])
        options = []

        # 1. Open PR (if available)
        if github_prs and github_prs[0].get("url"):
            options.append("open PR")

        # 2. Pull locally (if PRs available)
        if github_prs:
            options.append("pull locally")

        # 3. Open Trace (always available)
        options.append("open trace")

        # Execute the currently selected option
        if len(options) > self.action_menu_selection:
            selected_option = options[self.action_menu_selection]

            logger.info(
                "TUI action executed", extra={"operation": "tui.execute_action", "action": selected_option, "agent_id": agent_id, "org_id": getattr(self, "org_id", None), "has_prs": bool(github_prs)}
            )

            if selected_option == "open PR":
                pr_url = github_prs[0]["url"]
                try:
                    import webbrowser

                    webbrowser.open(pr_url)
                    # Debug details not needed for successful browser opens
                    # No pause - seamless flow back to collapsed state
                except Exception as e:
                    logger.error("Failed to open PR in browser", extra={"operation": "tui.open_pr", "agent_id": agent_id, "error": str(e)})
                    print(f"\n❌ Failed to open PR: {e}")
                    input("Press Enter to continue...")  # Only pause on errors
            elif selected_option == "pull locally":
                self._pull_agent_branch(agent_id)
            elif selected_option == "open trace":
                try:
                    import webbrowser

                    webbrowser.open(web_url)
                    # Debug details not needed for successful browser opens
                    # No pause - let it flow back naturally to collapsed state
                except Exception as e:
                    logger.error("Failed to open trace in browser", extra={"operation": "tui.open_trace", "agent_id": agent_id, "error": str(e)})
                    print(f"\n❌ Failed to open browser: {e}")
                    input("Press Enter to continue...")  # Only pause on errors

    def _open_agent_details(self):
        """Toggle the inline action menu."""
        self.show_action_menu = not self.show_action_menu
        if not self.show_action_menu:
            self.action_menu_selection = 0  # Reset selection when closing

    def _refresh(self):
        """Refresh the agent runs list."""
        # Indicate refresh and redraw immediately so the user sees it
        self.is_refreshing = True
        self._clear_and_redraw()

        if self._load_agent_runs():
            self.selected_index = 0  # Reset selection

        # Clear refresh indicator and redraw with updated data
        self.is_refreshing = False
        self._clear_and_redraw()

    def _clear_and_redraw(self):
        """Clear screen and redraw everything."""
        # Move cursor to top and clear screen from cursor down
        print("\033[H\033[J", end="")
        self._display_header()
        self._display_content()

        # Show appropriate instructions based on context
        if self.input_mode and self.current_tab == 2:  # new tab input mode
            print(f"\n{self._format_status_line('Type your prompt • [Enter] create • [B] cancel • [Tab] switch tabs • [Ctrl+C] quit')}")
        elif self.input_mode:  # other input modes
            print(f"\n{self._format_status_line('Type your prompt • [Enter] create • [B] cancel • [Ctrl+C] quit')}")
        elif self.show_action_menu:
            print(f"\n{self._format_status_line('[Enter] select • [↑↓] navigate • [C] close • [Q] quit')}")
        elif self.current_tab == 0:  # recent
            print(f"\n{self._format_status_line('[Tab] switch tabs • (↑↓) navigate • (←→) open/close • [Enter] actions • [R] refresh • [Q] quit')}")
        elif self.current_tab == 1:  # claude
            print(f"\n{self._format_status_line('[Tab] switch tabs • [Enter] launch claude code with telemetry • [Q] quit')}")
        elif self.current_tab == 2:  # new
            print(f"\n{self._format_status_line('[Tab] switch tabs • [Enter] start typing • [Q] quit')}")
        elif self.current_tab == 3:  # kanban
            print(f"\n{self._format_status_line('[Tab] switch tabs • [Enter] open web kanban • [Q] quit')}")

    def run(self):
        """Run the minimal TUI."""
        if not self.is_authenticated:
            # Automatically start login flow for first-time users
            from codegen.cli.auth.login import login_routine

            try:
                login_routine()
                # login_routine will launch TUI after successful authentication
                return
            except Exception:
                # If login fails, just exit gracefully
                return

        # Show UI immediately
        self._clear_and_redraw()

        # Start initial data load in background (non-blocking)
        def initial_load():
            self._load_agent_runs()
            if self.running:  # Only redraw if still running
                self._clear_and_redraw()

        load_thread = threading.Thread(target=initial_load, daemon=True)
        load_thread.start()

        # Main event loop
        while self.running:
            try:
                key = self._get_char()
                self._handle_keypress(key)
                if self.running:  # Only redraw if we're still running
                    self._clear_and_redraw()
            except KeyboardInterrupt:
                # This should be handled by the signal handler, but just in case
                break

        print()  # Add newline before exiting


def run_tui():
    """Run the minimal Codegen TUI."""
    logger.info("Starting TUI session", extra={"operation": "tui.start", "component": "run_tui"})

    try:
        tui = MinimalTUI()
        tui.run()
    except Exception as e:
        logger.error("TUI session crashed", extra={"operation": "tui.crash", "error_type": type(e).__name__, "error_message": str(e)}, exc_info=True)
        raise
    finally:
        logger.info("TUI session ended", extra={"operation": "tui.end", "component": "run_tui"})
