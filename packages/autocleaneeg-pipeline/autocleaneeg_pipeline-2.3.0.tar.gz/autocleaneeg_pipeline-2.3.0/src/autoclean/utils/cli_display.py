"""
Unified CLI display system for AutoClean EEG.

Provides consistent, professional console output throughout the CLI interface
without relying on the logging system. Uses Rich exclusively for clean,
visually appealing user interactions.
"""

from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

from autoclean.utils.icons import pick_icon

try:
    from rich.align import Align
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, TaskID
    from rich.prompt import Confirm, Prompt
    from rich.table import Table
    from rich.text import Text

    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    Console = None
    Panel = None
    Text = None
    Table = None
    Progress = None
    TaskID = None
    Confirm = None
    Prompt = None
    Align = None


class CLIDisplay:
    """Unified CLI display system using Rich for professional console output."""

    def __init__(self, console: Optional[Console] = None):
        """Initialize CLI display system."""
        if not RICH_AVAILABLE:
            raise ImportError("Rich library is required for CLI display system")

        # Lazy import to avoid circulars
        try:
            from autoclean.utils.console import get_console  # type: ignore

            self.console = console or get_console()
        except Exception:
            self.console = console or Console()

        # Status indicators with ASCII fallbacks
        self.SUCCESS = f"[success]{pick_icon('ok')}[/success]"
        self.WARNING = f"[warning]{pick_icon('warn')}[/warning]"
        self.ERROR = f"[error]{pick_icon('err')}[/error]"
        self.INFO = f"[info]{pick_icon('info')}[/info]"
        self.WORKING = f"[accent]{pick_icon('work')}[/accent]"
        self.ARROW = f"[muted]{pick_icon('arrow')}[/muted]"

        # Spacing constants
        self.SECTION_SPACING = "\n"
        self.ITEM_SPACING = ""

    def header(
        self, title: str, subtitle: Optional[str] = None, style: str = "title"
    ) -> None:
        """Display a section header."""
        text = Text()
        text.append(title, style=style)
        if subtitle:
            text.append(f"\n{subtitle}", style="subtitle")

        self.console.print(text)

    def success(self, message: str, details: Optional[str] = None) -> None:
        """Display a success message."""
        self.console.print(f"{self.SUCCESS} [success]{message}[/success]")
        if details:
            self.console.print(f"  [muted]{details}[/muted]")

    def warning(self, message: str, details: Optional[str] = None) -> None:
        """Display a warning message."""
        self.console.print(f"{self.WARNING} [warning]{message}[/warning]")
        if details:
            self.console.print(f"  [muted]{details}[/muted]")

    def error(self, message: str, details: Optional[str] = None) -> None:
        """Display an error message."""
        self.console.print(f"{self.ERROR} [error]{message}[/error]")
        if details:
            self.console.print(f"  [muted]{details}[/muted]")

    def info(self, message: str, details: Optional[str] = None) -> None:
        """Display an info message."""
        self.console.print(f"{self.INFO} [info]{message}[/info]")
        if details:
            self.console.print(f"  [muted]{details}[/muted]")

    def working(self, message: str) -> None:
        """Display a working/in-progress message."""
        self.console.print(f"{self.WORKING} [accent]{message}[/accent]")

    def step(self, message: str, status: str = "pending") -> None:
        """Display a step in a process."""
        if status == "completed":
            icon = self.SUCCESS
        elif status == "error":
            icon = self.ERROR
        elif status == "working":
            icon = self.WORKING
        else:
            icon = self.ARROW

        self.console.print(f"{icon} {message}")

    def list_item(
        self, message: str, value: Optional[str] = None, indent: int = 2
    ) -> None:
        """Display a list item with optional value."""
        spaces = " " * indent
        if value:
            self.console.print(f"{spaces}[bold]{message}:[/bold] {value}")
        else:
            self.console.print(f"{spaces}• {message}")

    def key_value(
        self, key: str, value: str, key_style: str = "bold", value_style: str = "dim"
    ) -> None:
        """Display a key-value pair."""
        self.console.print(
            f"[{key_style}]{key}:[/{key_style}] [{value_style}]{value}[/{value_style}]"
        )

    def separator(self, char: str = "─", length: int = 50, style: str = "dim") -> None:
        """Display a visual separator."""
        self.console.print(f"[{style}]{char * length}[/{style}]")

    def blank_line(self, count: int = 1) -> None:
        """Add blank lines for spacing."""
        for _ in range(count):
            self.console.print()

    def panel(
        self,
        content: Union[str, Text],
        title: Optional[str] = None,
        style: str = "blue",
        padding: tuple = (0, 2),
    ) -> None:
        """Display content in a panel."""
        panel = Panel(
            content,
            title=title,
            style=style,
            padding=padding,
            title_align="left" if title else "center",
        )
        self.console.print(panel)

    def table(
        self, headers: List[str], rows: List[List[str]], title: Optional[str] = None
    ) -> None:
        """Display a table."""
        table = Table(title=title, show_header=True, header_style="header")

        for header in headers:
            table.add_column(header)

        for row in rows:
            table.add_row(*row)

        self.console.print(table)

    def prompt_yes_no(self, question: str, default: bool = False) -> bool:
        """Prompt for yes/no confirmation."""
        return Confirm.ask(question, default=default, console=self.console)

    def prompt_text(
        self, question: str, default: Optional[str] = None, show_default: bool = True
    ) -> str:
        """Prompt for text input."""
        return Prompt.ask(
            question, default=default, show_default=show_default, console=self.console
        )

    def prompt_choice(
        self, question: str, choices: List[str], default: Optional[str] = None
    ) -> str:
        """Prompt for choice from a list."""
        return Prompt.ask(
            question, choices=choices, default=default, console=self.console
        )

    def workspace_info(self, workspace_path: Path, is_valid: bool = True) -> None:
        """Display workspace information in a clean format."""
        status_icon = self.SUCCESS if is_valid else self.WARNING
        status_text = (
            "[success]properly configured[/success]"
            if is_valid
            else "[warning]needs setup[/warning]"
        )

        self.console.print(f"{status_icon} Workspace is {status_text}")
        self.console.print()
        self.console.print(
            f"[header]Location:[/header] [accent]{workspace_path}[/accent]"
        )
        self.console.print()

    def system_info_table(self, info: Dict[str, str]) -> None:
        """Display system information in a clean table format."""
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column(style="header")
        table.add_column(style="accent")

        for key, value in info.items():
            # Add colors for specific values
            if "GPU" in key and (
                "✓" in value or "Apple" in value or "NVIDIA" in value or "CUDA" in value
            ):
                formatted_value = f"[success]{value}[/success]"
            elif "None detected" in value:
                formatted_value = f"[muted]{value}[/muted]"
            else:
                formatted_value = f"[accent]{value}[/accent]"

            table.add_row(f"{key}:", formatted_value)

        self.console.print(table)

    def setup_complete(
        self, workspace_path: Path, additional_info: Optional[List[str]] = None
    ) -> None:
        """Display setup completion message."""
        self.blank_line()
        self.success("Setup complete!", f"[accent]{workspace_path}[/accent]")

        if additional_info:
            self.blank_line()
            for info in additional_info:
                self.console.print(f"  [success]•[/success] [accent]{info}[/accent]")
        self.blank_line()

    def migration_prompt(self, old_path: Path, new_path: Path) -> bool:
        """Prompt for workspace migration."""
        self.console.print("\n[header]Workspace Migration[/header]")
        self.console.print(f"[warning]From:[/warning] [muted]{old_path}[/muted]")
        self.console.print(f"[success]To:[/success]   [accent]{new_path}[/accent]")
        self.console.print()

        return self.prompt_yes_no(
            "[bold]Migrate existing tasks and configuration?[/bold]", default=False
        )

    def centered(self, content: Union[str, Text], style: Optional[str] = None) -> None:
        """Display centered content."""
        if isinstance(content, str) and style:
            content = Text(content, style=style)
        self.console.print(Align.center(content))

    def boxed_header(
        self,
        main_text: str,
        subtitle: Optional[str] = None,
        title: Optional[str] = None,
        main_style: str = "brand",
        subtitle_style: str = "accent",
        box_style: str = "border",
    ) -> None:
        """Create a professional boxed header."""
        content = Text()
        content.append(main_text, style=main_style)
        if subtitle:
            content.append(f"\n{subtitle}", style=subtitle_style)

        panel = Panel(
            Align.center(content),
            style=box_style,
            padding=(0, 1),
            title=title,
            title_align="center" if title else None,
        )

        self.console.print(panel)


class SetupDisplay(CLIDisplay):
    """Specialized display methods for setup wizard."""

    def __init__(self, console: Optional[Console] = None):
        """Initialize setup display system."""
        super().__init__(console)

    def welcome_header(self, is_first_time: bool = True) -> None:
        """Display welcome header for setup."""
        # Simple branding constants
        PRODUCT_NAME = "AutoClean EEG"
        TAGLINE = "Professional EEG Processing & Analysis Platform"
        LOGO_ICON = "🧠"

        self.blank_line()

        if is_first_time:
            # Create branding content
            branding_text = Text()
            branding_text.append(f"{LOGO_ICON} Welcome to AutoClean", style="brand")
            branding_text.append(f"\n{TAGLINE}", style="accent")

            # Create panel with branding
            branding_panel = Panel(
                Align.center(branding_text),
                style="border",
                padding=(0, 1),
                title_align="center",
            )

            self.console.print(branding_panel)
            self.blank_line()
            self.console.print(
                "[muted]Let's set up your workspace for EEG processing.[/muted]"
            )
            self.console.print(
                "[muted]This workspace will contain your custom tasks, configuration, and results.[/muted]"
            )
        else:
            # Reconfiguration – concise, action-oriented header
            self.console.print("[header]⚙️ Change Workspace Folder[/header]")
            self.console.print(
                "[muted]Pick current, use the recommended default, or choose another folder.[/muted]"
            )

        self.blank_line()

    def setup_progress(self, step: str, details: Optional[str] = None) -> None:
        """Display setup progress."""
        self.working(step)
        if details:
            self.console.print(f"  {details}", style="muted")

    def workspace_location_prompt(self, default_dir: Path, current_dir: Optional[Path] = None) -> Path:
        """Prompt for workspace location with clear choices."""
        from pathlib import Path as _Path

        self.console.print("[header]Select Workspace Folder[/header]")
        self.console.print(
            "[muted]Where AutoClean stores your tasks, configuration, and results.[/muted]"
        )
        self.blank_line()

        home = str(_Path.home())

        def _short(p: _Path) -> str:
            s = str(p)
            return s.replace(home, "~", 1) if s.startswith(home) else s

        # Show options table when possible
        try:
            from rich.table import Table as _Table

            tbl = _Table(show_header=False, box=None, padding=(0, 1))
            tbl.add_column("Option", style="accent", no_wrap=True)
            tbl.add_column("Description", style="muted")
            idx = 1
            if current_dir is not None:
                tbl.add_row(f"{idx})", f"Keep current: {_short(current_dir)}")
                idx += 1
            tbl.add_row(f"{idx})", f"Use recommended: {_short(default_dir)}")
            idx += 1
            tbl.add_row(f"{idx})", "Choose another folder…")
            self.console.print(tbl)
            self.blank_line()
        except Exception:
            pass

        # Build choices with numeric shortcuts
        default_choice = "current" if current_dir is not None else "default"
        choice_entries: List[Tuple[str, str]] = []
        idx = 1
        if current_dir is not None:
            choice_entries.append(("current", str(idx)))
            idx += 1
        choice_entries.append(("default", str(idx)))
        idx += 1
        choice_entries.append(("custom", str(idx)))

        choice_aliases: Dict[str, str] = {}
        prompt_choices: List[str] = []
        for name, number in choice_entries:
            prompt_choices.extend([name, number])
            choice_aliases[name] = name
            choice_aliases[name.lower()] = name
            choice_aliases[number] = name

        self.console.print("[muted]Enter the number or name of an option.[/muted]")

        # Ask for choice
        try:
            raw_choice = self.prompt_choice(
                "Select an option",
                choices=prompt_choices,
                default=default_choice,
            )
        except (EOFError, KeyboardInterrupt):
            raw_choice = default_choice

        choice = choice_aliases.get(
            raw_choice.lower(), choice_aliases.get(raw_choice, default_choice)
        )

        if choice == "current" and current_dir is not None:
            chosen_dir = current_dir
            self.success("Keeping current workspace", _short(chosen_dir))
        elif choice == "default":
            chosen_dir = default_dir
            self.success("Using recommended default", _short(chosen_dir))
        else:
            # Custom path entry
            try:
                response = self.prompt_text(
                    "Enter folder path",
                    default=str(current_dir or default_dir),
                    show_default=True,
                ).strip()
                chosen_dir = _Path(response).expanduser()
                self.success("Using custom folder", _short(chosen_dir))
            except (EOFError, KeyboardInterrupt):
                chosen_dir = default_dir
                self.warning("Using recommended default due to interrupt", _short(chosen_dir))

        self.blank_line()
        return chosen_dir

    def compliance_status_display(self, is_enabled: bool, is_permanent: bool) -> None:
        """Display compliance status information."""
        if is_permanent:
            self.warning("FDA 21 CFR Part 11 compliance mode is permanently enabled")
            self.info("You can only configure workspace location in compliance mode")
        elif is_enabled:
            self.info("FDA 21 CFR Part 11 compliance mode is currently enabled")
        else:
            self.console.print("[muted]Current compliance mode: disabled[/muted]")
        self.blank_line()

    def setup_complete_summary(self, workspace_path: Path) -> None:
        """Display setup completion summary."""
        self.blank_line()
        self.separator("═", 50, "border")
        self.success("Setup complete!", str(workspace_path))

        # Additional files created
        created_files = [
            "📋 Template task created",
            "📄 Example script added",
            "🔧 Built-in task examples copied",
        ]

        self.blank_line()
        self.console.print("[title]Files Created:[/title]")
        for file_info in created_files:
            self.console.print(f"  [success]•[/success] [accent]{file_info}[/accent]")

        self.blank_line()
        self.separator("═", 50, "border")


# Global instances for easy import
from autoclean.utils.console import get_console as _get_console  # type: ignore

cli_display = CLIDisplay(_get_console())
setup_display = SetupDisplay(_get_console())
