# coding=utf-8
# Copyright (c) 2025 Jifeng Wu
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
from cowlist import COWList
from typing import Iterator, Text, Union


class NormalState(object):
    __slots__ = ['characters', 'quote']

    def __init__(self, characters, quote):
        # type: (COWList[Text], bool) -> None
        self.characters = characters  # type: COWList[Text]
        self.quote = quote  # type: bool

    def iterate_characters(self):
        # type: () -> Iterator[Text]
        if not self.characters or self.quote:
            yield u'"'
            for _ in self.characters:
                yield _
            yield u'"'
        else:
            for _ in self.characters:
                yield _


class BackslashState(object):
    __slots__ = ['characters', 'quote', 'backslash_count']

    def __init__(self, characters, quote, backslash_count):
        # type: (COWList[Text], bool, int) -> None
        self.characters = characters  # type: COWList[Text]
        self.quote = quote  # type: bool
        self.backslash_count = backslash_count  # type: int


WHITESPACE_CHARS = {u' ', u'\t', u'\n', u'\r', u'\x0b', u'\x0c'}


def escape_nt_command_line_argument(argument):
    # type: (Text) -> Text
    state = NormalState(characters=COWList(), quote=False)  # type: Union[NormalState, BackslashState]
    for character in argument:
        if isinstance(state, NormalState):
            if character == u'\\':
                state = BackslashState(characters=state.characters, quote=state.quote, backslash_count=1)
            elif character == u'"':
                state = NormalState(characters=state.characters.append(u'\\').append(u'"'), quote=True)
            elif character in WHITESPACE_CHARS:
                state = NormalState(characters=state.characters.append(character), quote=True)
            else:
                state = NormalState(characters=state.characters.append(character), quote=state.quote)
        else:
            if character == u'\\':
                state = BackslashState(
                    characters=state.characters,
                    quote=state.quote,
                    backslash_count=state.backslash_count + 1
                )
            elif character == u'"':
                state = NormalState(
                    characters=state.characters.extend(u'\\' * (state.backslash_count * 2 + 1)).append(u'"'),
                    quote=True
                )
            elif character in WHITESPACE_CHARS:
                state = NormalState(
                    characters=state.characters.extend(u'\\' * state.backslash_count).append(character),
                    quote=True
                )
            else:
                state = NormalState(
                    characters=state.characters.extend(u'\\' * state.backslash_count).append(character),
                    quote=state.quote
                )

    if isinstance(state, BackslashState):
        state = NormalState(
            characters=state.characters.extend(u'\\' * (state.backslash_count * 2)),
            quote=True
        )

    return u''.join(state.iterate_characters())
