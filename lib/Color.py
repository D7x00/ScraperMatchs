from colorama import init, Fore, Style


class Color:
    """
     This File For Color Text
     Create file by K6s

    """
    file='\033[92m'
    ANSI_RED = '\033[91m'
    ANSI_GREEN = '\033[92m'
    ANSI_BLUE = '\033[94m'
    ANSI_YELLOW = '\033[93m'
    ANSI_1RESET = '\033[0m'
    fore = Fore
    Blue = Fore.BLUE
    ANSI_RESET = Style.RESET_ALL
    ANSI_BOLD = Fore.LIGHTWHITE_EX
    Green = Fore.GREEN
    Reset = Fore.RESET
    banner = Fore.LIGHTCYAN_EX

    @classmethod
    def ShowBanner(cls) -> str:  # banner
        return ("\n"
                " \n"
                "        ████████╗ ██████╗  ██████╗ ██╗     ███████╗    ██╗  ██╗ ██████╗ ███████╗██╗  ██╗    \n"
                "        ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝    ██║ ██╔╝██╔════╝ ██╔════╝╚██╗██╔╝    \n"
                "           ██║   ██║   ██║██║   ██║██║     ███████╗    █████╔╝ ███████╗ ███████╗ ╚███╔╝     \n"
                "           ██║   ██║   ██║██║   ██║██║     ╚════██║    ██╔═██╗ ██╔═══██╗╚════██║ ██╔██╗     \n"
                "           ██║   ╚██████╔╝╚██████╔╝███████╗███████║    ██║  ██╗╚██████╔╝███████║██╔╝ ██╗    \n"
                "           ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    \n"
                "                                                                                            \n"
                "           Github -> https://github.com/D7x00/ToolsK6sx.git                                 \n"
                "                                                                                            \n"
                "           { 1 } -->               Encryption Mode                                          \n"
                "           { 2 } -->               Soon Build                                               \n"
                "           { exit } -->            For  exit ToolsK6sx                                      \n")

    def __init__(self):
        init()

    @classmethod
    def format_message(cls, color, category: str, text: str) -> str:
        return f"{cls.ANSI_BOLD}[{color}{category}{Fore.RESET}]{cls.ANSI_RESET} {text} {cls.ANSI_RESET}"

    @classmethod
    def Error(cls, text: str) -> str:
        return cls.format_message(Fore.RED, "Error", text)

    @classmethod
    def Wrong(cls, text):
        return cls.format_message(Fore.YELLOW, "Wrong", text)

    @classmethod
    def Success(cls, text):
        return cls.format_message(Fore.GREEN, "Success", text)

    @classmethod
    def Required(cls, text):
        return cls.format_message(Fore.MAGENTA, "Required", text)

    @classmethod
    def INFO(cls, text):
        return cls.format_message(Fore.MAGENTA, "INFO", text)
