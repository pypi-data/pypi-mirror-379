"""
CLI Formatting Utilities
========================

Enhanced formatting utilities for better CLI user experience including colors,
progress indicators, tables, and interactive elements.
"""

import sys
import time
import threading
from enum import Enum
from dataclasses import dataclass
from typing import Any, Callable, Optional, Union
import shutil


class Color(Enum):
    pass
    """ANSI color codes for terminal output"""
    # Basic colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m']
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_blue = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m']
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m']
    
    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    STRIKETHROUGH = '\033[9m']
    
    # Reset
    RESET = '\033[0m']


class Icons:
    pass
    """Unicode icons for CLI output"""
    # Status icons
    SUCCESS = '✅'
    ERROR = '❌'
    WARNING = '⚠️'
    INFO = 'ℹ️'
    QUESTION = '❓'
    
    # Progress icons
    SPINNER = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    PROGRESS_FULL = '█'
    PROGRESS_EMPTY = '░'
    PROGRESS_PARTIAL = ['▏', '▎', '▍', '▌', '▋', '▊', '▉']
    
    # Action icons
    ROCKET = '🚀'
    GEAR = '⚙️'
    FOLDER = '📁'
    FILE = '📄'
    CHART = '📊'
    CLOCK = '🕐'
    CHECKMARK = '✓'
    CROSS = '✗'
    ARROW_RIGHT = '→'
    ARROW_DOWN = '↓'
    
    # Bot-specific icons
    BOT = '🤖'
    TRADING = '💹'
    MONEY = '💰'
    CHART_UP = '📈'
    CHART_DOWN = '📉'
    BALANCE = '⚖️'


@dataclass
class TableColumn:
    
        pass
    pass
    """Table column configuration"""
    header: str
    width: int
    align: str = 'left'  # 'left', 'center', 'right'
    formatter: Optional[Callable[[Any], str]] = None


class ColorFormatter:
    pass
    """Utility class for colored terminal output"""
    
    def __init__(self, use_colors: bool = None):
    pass
        if use_colors is None:
    
        pass
    pass
            # Auto-detect color support
            self.use_colors = self._supports_color()
        else:
    pass
            self.use_colors = use_colors
    
    def _supports_color(self) -> bool:
    pass
        """Check if terminal supports colors"""
        # Check if stdout is a TTY and not redirected
        if not sys.stdout.isatty():
    
        pass
    pass
            return False
        
        # Check TERM environment variable
        import os
        term = os.environ.get('TERM', '')
        if term in ('dumb', ''):
    
        pass
    pass
            return False
        
        # Check for NO_COLOR environment variable
        if os.environ.get('NO_COLOR'):
    
        pass
    pass
            return False
        
        # Check for FORCE_COLOR environment variable
        if os.environ.get('FORCE_COLOR'):
    
        pass
    pass
            return True
        
        return True
    
    def colorize(self, text: str, color: Color, reset: bool = True) -> str:
    pass
        """Apply color to text"""
        if not self.use_colors:
    
        pass
    pass
            return text
        
        result = f"{color.value}{text}"
        if reset:
    
        pass
    pass
            result += Color.RESET.value
        return result
    
    def success(self, text: str) -> str:
    pass
        """Format success message"""
        return self.colorize(f"{Icons.SUCCESS} {text}", Color.GREEN)
    
    def error(self, text: str) -> str:
    pass
        """Format error message"""
        return self.colorize(f"{Icons.ERROR} {text}", Color.RED)
    
    def warning(self, text: str) -> str:
    pass
        """Format warning message"""
        return self.colorize(f"{Icons.WARNING} {text}", Color.YELLOW)
    
    def info(self, text: str) -> str:
    pass
        """Format info message"""
        return self.colorize(f"{Icons.INFO} {text}", Color.CYAN)
    
    def highlight(self, text: str) -> str:
    pass
        """Highlight important text"""
        return self.colorize(text, Color.BOLD)
    
    def dim(self, text: str) -> str:
    pass
        """Dim less important text"""
        return self.colorize(text, Color.DIM)
    
    def code(self, text: str) -> str:
    pass
        """Format code/command text"""
        return self.colorize(text, Color.BRIGHT_BLACK)


class ProgressIndicator:
    pass
    """Progress indicator for long-running operations"""
    
    def __init__(self, message: str = "Processing", use_colors: bool = None):
    pass
        self.message = message
        self.formatter = ColorFormatter(use_colors)
        self._stop_event = threading.Event()
        self._thread = None
        self._spinner_index = 0
    
    def start(self) -> None:
    pass
        """Start the progress indicator"""
        if self._thread and self._thread.is_alive():
    
        pass
    pass
            return
        
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._animate)
        self._thread.daemon = True
        self._thread.start()
    
    def stop(self, success_message: str = None, error_message: str = None) -> None:
    pass
        """Stop the progress indicator"""
        if self._thread and self._thread.is_alive():
    
        pass
    pass
            self._stop_event.set()
            self._thread.join(timeout=1.0)
        
        # Clear the line
        sys.stdout.write('\r' + ' ' * 80 + '\r')
        sys.stdout.flush()
        
        # Show final message
        if success_message:
    
        pass
    pass
            print(self.formatter.success(success_message))
        elif error_message:
    
        pass
    pass
            print(self.formatter.error(error_message))
    
    def _animate(self) -> None:
    pass
        """Animate the spinner"""
        while not self._stop_event.is_set():
    pass
            spinner_char = Icons.SPINNER[self._spinner_index % len(Icons.SPINNER)]
            message = f"{spinner_char} {self.message}..."
            
            sys.stdout.write(f'\r{message}')
            sys.stdout.flush()
            
            self._spinner_index += 1
            time.sleep(0.1)
    
    def __enter__(self):
    pass
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
    pass
        if exc_type:
    
        pass
    pass
            self.stop(error_message="Operation failed")
        else:
    pass
            self.stop(success_message="Operation completed")


class ProgressBar:
    pass
    """Progress bar for operations with known progress"""
    
    def __init__(self, total: int, message: str = "Progress", width: int = 40, use_colors: bool = None):
    pass
        self.total = total
        self.current = 0
        self.message = message
        self.width = width
        self.formatter = ColorFormatter(use_colors)
    
    def update(self, increment: int = 1, message: str = None) -> None:
    pass
        """Update progress"""
        self.current = min(self.current + increment, self.total)
        if message:
    
        pass
    pass
            self.message = message
        self._render()
    
    def set_progress(self, current: int, message: str = None) -> None:
    pass
        """Set absolute progress"""
        self.current = min(max(current, 0), self.total)
        if message:
    
        pass
    pass
            self.message = message
        self._render()
    
    def _render(self) -> None:
    pass
        """Render the progress bar"""
        if self.total == 0:
    
        pass
    pass
            percentage = 100
            filled_width = self.width
        else:
    pass
            percentage = (self.current / self.total) * 100
            filled_width = int((self.current / self.total) * self.width)
        
        # Create progress bar
        filled = Icons.PROGRESS_FULL * filled_width
        empty = Icons.PROGRESS_EMPTY * (self.width - filled_width)
        
        if self.formatter.use_colors:
    
        pass
    pass
            filled = self.formatter.colorize(filled, Color.GREEN, reset=False)
            empty = self.formatter.colorize(empty, Color.DIM, reset=False)
        
        # Format message
        progress_text = f"{self.message} [{filled}{empty}] {percentage:.1f}% ({self.current}/{self.total})"
        
        if self.formatter.use_colors:
    
        pass
    pass
            progress_text += Color.RESET.value
        
        sys.stdout.write(f'\r{progress_text}')
        sys.stdout.flush()
        
        if self.current >= self.total:
    
        pass
    pass
            print()  # New line when complete
    
    def finish(self, message: str = "Complete") -> None:
    pass
        """Finish the progress bar"""
        self.set_progress(self.total, message)


class Table:
    pass
    """Enhanced table formatter"""
    
    def __init__(self, columns: list[TableColumn], use_colors: bool = None):
    pass
        self.columns = columns
        self.formatter = ColorFormatter(use_colors)
        self.rows = []
    
    def add_row(self, *values) -> None:
    pass
        """Add a row to the table"""
        if len(values) != len(self.columns):
    
        pass
    pass
            raise ValueError(f"Expected {len(self.columns)} values, got {len(values)}")
        self.rows.append(list(values))
    
    def render(self) -> str:
    pass
        """Render the table as a string"""
        if not self.rows:
    
        pass
    pass
            return "No data to display"
        
        lines = []
        
        # Calculate actual column widths
        widths = []
        for i, col in enumerate(self.columns):
    pass
            max_width = len(col.header)
            for row in self.rows:
    pass
                value = row[i]
                if col.formatter:
    
        pass
    pass
                    value = col.formatter(value)
                max_width = max(max_width, len(str(value)))
            widths.append(max(col.width, max_width))
        
        # Header
        header_parts = []
        for i, col in enumerate(self.columns):
    pass
            header = self._align_text(col.header, widths[i], col.align)
            if self.formatter.use_colors:
    
        pass
    pass
                header = self.formatter.colorize(header, Color.BOLD)
            header_parts.append(header)
        
        lines.append("│ " + " │ ".join(header_parts) + " │")
        
        # Separator
        separator_parts = []
        for width in widths:
    pass
            separator_parts.append("─" * width)
        lines.append("├─" + "─┼─".join(separator_parts) + "─┤")
        
        # Rows
        for row in self.rows:
    pass
            row_parts = []
            for i, (value, col) in enumerate(zip(row, self.columns)):
    pass
                if col.formatter:
    
        pass
    pass
                    formatted_value = col.formatter(value)
                else:
    pass
                    formatted_value = str(value)
                
                aligned_value = self._align_text(formatted_value, widths[i], col.align)
                row_parts.append(aligned_value)
            
            lines.append("│ " + " │ ".join(row_parts) + " │")
        
        # Top and bottom borders
        top_border = "┌─" + "─┬─".join("─" * w for w in widths) + "─┐"
        bottom_border = "└─" + "─┴─".join("─" * w for w in widths) + "─┘"
        
        return "\n".join([top_border] + lines + [bottom_border])
    
    def _align_text(self, text: str, width: int, align: str) -> str:
    pass
        """Align text within specified width"""
        if align == 'center':
    
        pass
    pass
            return text.center(width)
        elif align == 'right':
    
        pass
    pass
            return text.rjust(width)
        else:  # left
            return text.ljust(width)
    
    def print(self) -> None:
    pass
        """Print the table"""
        print(self.render())


class InteractivePrompt:
    pass
    """Interactive prompt utilities"""
    
    def __init__(self, use_colors: bool = None):
    pass
        self.formatter = ColorFormatter(use_colors)
    
    def confirm(self, message: str, default: bool = False) -> bool:
    pass
        """Ask for yes/no confirmation"""
        default_text = "Y/n" if default else "y/N"
        prompt = f"{Icons.QUESTION} {message} ({default_text}): "
        
        if self.formatter.use_colors:
    
        pass
    pass
            prompt = self.formatter.colorize(prompt, Color.YELLOW)
        
        while True:
    pass
            try:
    pass
                response = input(prompt).strip().lower()
                
                if not response:
    
        pass
    pass
                    return default
                
                if response in ('y', 'yes', 'true', '1'):
    
        pass
    pass
                    return True
                elif response in ('n', 'no', 'false', '0'):
    
        pass
    pass
                    return False
                else:
    pass
                    print(self.formatter.error("Please enter 'y' or 'n'"))
            
            except KeyboardInterrupt:
    pass
    pass
                print("\nOperation cancelled")
                return False
            except EOFError:
    pass
    pass
                return default
    
    def select(self, message: str, options: list[str], default: int = 0) -> int:
    pass
        """Select from a list of options"""
        
        for i, option in enumerate(options):
    pass
            marker = "●" if i == default else "○"
            if self.formatter.use_colors:
    
        pass
    pass
                if i == default:
    
        pass
    pass
                    option_text = self.formatter.colorize(f"{marker} {option}", Color.GREEN)
                else:
    pass
                    option_text = f"{marker} {option}"
            else:
    pass
                option_text = f"{marker} {option}"
            
            print(f"  {i + 1}. {option_text}")
        
        prompt = f"\nSelect option (1-{len(options)}) [default: {default + 1}]: "
        
        while True:
    pass
            try:
    pass
                response = input(prompt).strip()
                
                if not response:
    
        pass
    pass
                    return default
                
                try:
    pass
                    choice = int(response) - 1
                    if 0 <= choice < len(options):
    
        pass
    pass
                        return choice
                    else:
    pass
                        print(self.formatter.error(f"Please enter a number between 1 and {len(options)}"))
                except ValueError:
    pass
    pass
                    print(self.formatter.error("Please enter a valid number"))
            
            except KeyboardInterrupt:
    pass
    pass
                print("\nOperation cancelled")
                return default
            except EOFError:
    pass
    pass
                return default
    
    def input_text(self, message: str, default: str = "", required: bool = False, 
                   validator: Optional[Callable[[str], bool]] = None) -> str:
    pass
        """Get text input with validation"""
        default_text = f" [default: {default}]" if default else ""
        required_text = " (required)" if required else ""
        prompt = f"{Icons.QUESTION} {message}{default_text}{required_text}: "
        
        if self.formatter.use_colors:
    
        pass
    pass
            prompt = self.formatter.colorize(prompt, Color.CYAN)
        
        while True:
    pass
            try:
    pass
                response = input(prompt).strip()
                
                if not response:
    
        pass
    pass
                    if default:
    
        pass
    pass
                        return default
                    elif required:
    
        pass
    pass
                        print(self.formatter.error("This field is required"))
                        continue
                    else:
    pass
                        return ""
                
                if validator and not validator(response):
    
        pass
    pass
                    print(self.formatter.error("Invalid input format"))
                    continue
                
                return response
            
            except KeyboardInterrupt:
    pass
    pass
                print("\nOperation cancelled")
                return default if not required else ""
            except EOFError:
    
        pass
    pass
    pass
                return default if not required else ""
    
    def input_password(self, message: str, required: bool = True) -> str:
    pass
        """Get password input (hidden)"""
        import get
        prompt = f"{Icons.QUESTION} {message}: "
        if self.formatter.use_colors:
    
        pass
    pass
            prompt = self.formatter.colorize(prompt, Color.CYAN)
        
        while True:
    pass
            try:
    pass
                password = getpass.getpass(prompt)
                
                if not password and required:
    
        pass
    pass
                    print(self.formatter.error("Password is required"))
                    continue
                
                return password
            
            except KeyboardInterrupt:
    pass
    pass
                print("\nOperation cancelled")
                return ""
            except EOFError:
    pass
    pass
                return ""


class Banner:
    pass
    """Banner and header utilities"""
    
    def __init__(self, use_colors: bool = None):
    pass
        self.formatter = ColorFormatter(use_colors)
    
    def print_header(self, title: str, subtitle: str = "", width: int = None) -> None:
    pass
        """Print a formatted header"""
        if width is None:
    
        pass
    pass
            width = min(80, shutil.get_terminal_size().columns)
        
        # Title
        title_line = f" {title} "
        if self.formatter.use_colors:
    
        pass
    pass
            title_line = self.formatter.colorize(title_line, Color.BOLD)
        
        # Create border
        border = "═" * width
        title_border = "═" * ((width - len(title) - 2) // 2)
        
        print(f"\n╔{border}╗")
        print(f"║{title_border}{title_line}{title_border}║")
        
        if subtitle:
    
        pass
    pass
            subtitle_line = f" {subtitle} "
            subtitle_border = " " * ((width - len(subtitle) - 2) // 2)
            if self.formatter.use_colors:
    
        pass
    pass
                subtitle_line = self.formatter.colorize(subtitle_line, Color.DIM)
            print(f"║{subtitle_border}{subtitle_line}{subtitle_border}║")
        
        print(f"╚{border}╝\n")
    
    def print_section(self, title: str) -> None:
    pass
        """Print a section header"""
        if self.formatter.use_colors:
    
        pass
    pass
            title = self.formatter.colorize(f"📋 {title}", Color.BOLD)
        else:
    pass
            title = f"📋 {title}"
        
        print(f"\n{title}")
        print("─" * (len(title) + 2))
    
    def print_subsection(self, title: str) -> None:
    pass
        """Print a subsection header"""
        if self.formatter.use_colors:
    
        pass
    pass
            title = self.formatter.colorize(f"  📌 {title}", Color.CYAN)
        else:
    pass
            title = f"  📌 {title}"
        
        print(f"\n{title}")


def format_file_size(size_bytes: int) -> str:
    pass
    """Format file size in human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
    pass
        if size_bytes < 1024.0:
    
        pass
    pass
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"


def format_duration(seconds: float) -> str:
    pass
    """Format duration in human-readable format"""
    if seconds < 60:
    
        pass
    pass
        return f"{seconds:.1f}s"
    elif seconds < 3600:
    
        pass
    pass
        minutes = seconds / 60
        return f"{minutes:.1f}m"
    elif seconds < 86400:
    
        pass
    pass
        hours = seconds / 3600
        return f"{hours:.1f}h"
    else:
    pass
        days = seconds / 86400
        return f"{days:.1f}d"


def format_percentage(value: float, total: float) -> str:
    pass
    """Format percentage with proper handling of edge cases"""
    if total == 0:
    
        pass
    pass
        return "0.0%"
    percentage = (value / total) * 100
    return f"{percentage:.1f}%"


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    pass
    """Truncate text to maximum length with suffix"""
    if len(text) <= max_length:
    
        pass
    pass
        return text
    return text[:max_length - len(suffix)] + suffix


def format_money(amount: float, currency: str = "USD") -> str:
    pass
    """Format monetary amounts"""
    if currency == "USD":
    
        pass
    pass
        return f"${amount:,.2f}"
    elif currency == "EUR":
    
        pass
    pass
        return f"€{amount:,.2f}"
    elif currency == "GBP":
    
        pass
    pass
        return f"£{amount:,.2f}"
    else:
    pass
        return f"{amount:,.2f} {currency}"