import argparse
import os
import sys
from typing import Optional

from eth_typing import ChecksumAddress
from prompt_toolkit import HTML, PromptSession, print_formatted_text
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.history import FileHistory
from prompt_toolkit.lexers import PygmentsLexer

from .operators import (
    SafeCliTerminationException,
    SafeOperator,
    SafeServiceNotAvailable,
    SafeTxServiceOperator,
)
from .prompt_parser import PromptParser
from .safe_completer import SafeCompleter
from .safe_lexer import SafeLexer


class SafeCli:
    def __init__(self, safe_address: ChecksumAddress, node_url: str, history: bool):
        """
        :param safe_address: Safe address
        :param node_url: Ethereum RPC url
        :param history: If `True` keep command history, otherwise history is not kept after closing the CLI
        """
        self.safe_address = safe_address
        self.node_url = node_url
        if history:
            self.session = PromptSession(
                history=FileHistory(os.path.join(sys.path[0], ".history"))
            )
        else:
            self.session = PromptSession()
        self.safe_operator = SafeOperator(safe_address, node_url)
        self.prompt_parser = PromptParser(self.safe_operator)

    def print_startup_info(self):
        print_formatted_text(
            HTML("<b><ansigreen>Loading Safe information...</ansigreen></b>")
        )
        self.safe_operator.print_info()

        print_formatted_text(
            HTML("\nUse the <b>tab key</b> to show options in interactive mode.")
        )
        print_formatted_text(
            HTML(
                "The <b>help</b> command displays all available options and the <b>exit</b> command terminates the safe-cli."
            )
        )

    def get_prompt_text(self):
        mode: Optional[str] = "blockchain"
        if isinstance(self.prompt_parser.safe_operator, SafeTxServiceOperator):
            mode = "tx-service"

        return HTML(
            f"<bold><ansiblue>{mode} > {self.safe_address}</ansiblue><ansired> > </ansired></bold>"
        )

    def get_bottom_toolbar(self):
        return HTML(
            f'<b><style fg="ansiyellow">network={self.safe_operator.network.name} '
            f"{self.safe_operator.safe_cli_info}</style></b>"
        )

    def parse_operator_mode(self, command: str) -> Optional[SafeOperator]:
        """
        Parse operator mode to switch between blockchain (default) and tx-service
        :param command:
        :return: SafeOperator if detected
        """
        split_command = command.split()
        try:
            if (split_command[0]) == "tx-service":
                print_formatted_text(
                    HTML("<b><ansigreen>Sending txs to tx service</ansigreen></b>")
                )
                return SafeTxServiceOperator(self.safe_address, self.node_url)
            elif split_command[0] == "blockchain":
                print_formatted_text(
                    HTML("<b><ansigreen>Sending txs to blockchain</ansigreen></b>")
                )
                return self.safe_operator
        except SafeServiceNotAvailable:
            print_formatted_text(
                HTML("<b><ansired>Mode not supported on this network</ansired></b>")
            )

    def get_command(self) -> str:
        return self.session.prompt(
            self.get_prompt_text,
            auto_suggest=AutoSuggestFromHistory(),
            bottom_toolbar=self.get_bottom_toolbar,
            lexer=PygmentsLexer(SafeLexer),
            completer=SafeCompleter(),
        )

    def loop(self):
        while True:
            try:
                command = self.get_command()
                if not command.strip():
                    continue

                new_operator = self.parse_operator_mode(command)
                if new_operator:
                    self.prompt_parser = PromptParser(new_operator)
                    new_operator.refresh_safe_cli_info()  # ClI info needs to be initialized
                else:
                    self.prompt_parser.process_command(command)
            except SafeCliTerminationException:
                break
            except EOFError:
                break
            except KeyboardInterrupt:
                continue
            except (argparse.ArgumentError, argparse.ArgumentTypeError, SystemExit):
                pass
