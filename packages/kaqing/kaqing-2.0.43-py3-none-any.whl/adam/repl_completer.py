import re

from typing import Iterable
from prompt_toolkit.completion import CompleteEvent, Completion, NestedCompleter, WordCompleter
from prompt_toolkit.document import Document

from adam.commands.postgres.postgres_utils import pg_table_names

class CompleterContext:
    # the singleton pattern
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'): cls.instance = super(CompleterContext, cls).__new__(cls)

        return cls.instance

    def __init__(self):
        if not hasattr(self, 'table_resolver'):
            self.table_resolver = None
            self.tables = []

    def produce(self, word: str):
        if match := re.match(r'^<pg_tables:(.*?):(.*?)>$', word):
            self.table_resolver = word
            self.tables = pg_table_names(match.group(1), match.group(2))

            return self.tables

        return None

    def is_table(self, word: str):
        if word in self.tables and self.table_resolver:
            return self.table_resolver

        return None

    def reset(self):
        self.table_resolver = None
        self.tables = []


class ReplCompleter(NestedCompleter):
    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        text = document.text_before_cursor.lstrip()
        stripped_len = len(document.text_before_cursor) - len(text)

        if " " in text:
            first_term = text.split()[0]
            completer = self.options.get(first_term)
            if table_resolver := CompleterContext().is_table(first_term):
                completer = self.options.get(table_resolver)

            if completer is not None:
                remaining_text = text[len(first_term) :].lstrip()
                move_cursor = len(text) - len(remaining_text) + stripped_len

                new_document = Document(
                    remaining_text,
                    cursor_position=document.cursor_position - move_cursor,
                )

                for c in completer.get_completions(new_document, complete_event):
                    if words := CompleterContext().produce(c.text):
                        for w in words:
                            yield Completion(w)
                    else:
                        yield c
        else:
            completer = WordCompleter(
                list(self.options.keys()), ignore_case=self.ignore_case
            )
            for c in completer.get_completions(document, complete_event):
                yield c
