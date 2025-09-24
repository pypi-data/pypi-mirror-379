#
# Copyright (c) 2025 CESNET z.s.p.o.
#
# This file is a part of oarepo-runtime (see https://github.com/oarepo/oarepo-runtime).
#
# oarepo-runtime is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Typed invenio generators."""

from __future__ import annotations

from abc import ABC, abstractmethod
from itertools import chain
from typing import TYPE_CHECKING, Any, override

from invenio_records_permissions.generators import (
    ConditionalGenerator as InvenioConditionalGenerator,
)
from invenio_records_permissions.generators import Generator as InvenioGenerator
from invenio_search.engine import dsl

if TYPE_CHECKING:
    from collections.abc import Sequence

    from flask_principal import Need
    from invenio_records_resources.records.api import Record


class Generator(InvenioGenerator):
    """Custom generator for the service.

    This class will be removed when invenio has proper type stubs.
    """

    @override
    def needs(self, **kwargs: Any) -> Sequence[Need]:  # type: ignore[reportIncompatibleMethodOverride]
        return super().needs(**kwargs)  # type: ignore[no-any-return]

    @override
    def excludes(self, **kwargs: Any) -> Sequence[Need]:  # type: ignore[reportIncompatibleMethodOverride]
        return super().excludes(**kwargs)  # type: ignore[no-any-return]

    @override
    def query_filter(self, **kwargs: Any) -> dsl.query.Query:  # type: ignore[reportIncompatibleMethodOverride]
        return super().query_filter(**kwargs)  # type: ignore[no-any-return]


class ConditionalGenerator(InvenioConditionalGenerator, ABC):
    """Typed conditional generator.

    This class will be removed when invenio has proper type stubs.
    """

    def __init__(self, then_: Sequence[InvenioGenerator], else_: Sequence[InvenioGenerator]) -> None:
        """Initialize the conditional generator."""
        super().__init__(then_=then_, else_=else_)

    @abstractmethod
    def _condition(self, **kwargs: Any) -> bool:
        """Condition to choose generators set."""
        raise NotImplementedError  # pragma: no cover

    def _generators(self, record: Record, **kwargs: Any) -> Sequence[InvenioGenerator]:
        """Get the "then" or "else" generators."""
        return super()._generators(record=record, **kwargs)  # type: ignore[no-any-return]

    @override
    def needs(self, **kwargs: Any) -> Sequence[Need]:  # type: ignore[override]
        return super().needs(**kwargs)  # type: ignore[no-any-return]

    @override
    def excludes(self, **kwargs: Any) -> Sequence[Need]:  # type: ignore[override]
        return super().excludes(**kwargs)  # type: ignore[no-any-return]

    @abstractmethod
    def _query_instate(self, **context: Any) -> dsl.query.Query:
        raise NotImplementedError  # pragma: no cover

    @override
    def query_filter(self, **context: Any) -> dsl.query.Query:  # type: ignore[reportIncompatibleMethodOverride]
        """Apply then or else filter."""
        then_query = super()._make_query(self.then_, **context)
        else_query = super()._make_query(self.else_, **context)

        q_instate = self._query_instate(**context)
        q_outstate = ~q_instate

        if then_query and else_query:
            ret = (q_instate & then_query) | (q_outstate & else_query)
        elif then_query:
            ret = q_instate & then_query
        elif else_query:
            ret = q_outstate & else_query
        else:
            ret = dsl.Q("match_none")

        return ret


class AggregateGenerator(Generator, ABC):
    """Superclass for generators aggregating multiple generators."""

    @abstractmethod
    def _generators(self, **context: Any) -> Sequence[InvenioGenerator]:
        """Return the generators."""
        raise NotImplementedError  # pragma: no cover

    @override
    def needs(self, **context: Any) -> Sequence[Need]:
        """Get the needs from the policy."""
        needs = [generator.needs(**context) for generator in self._generators(**context)]
        return list(chain.from_iterable(needs))

    @override
    def excludes(self, **context: Any) -> Sequence[Need]:
        """Get the excludes from the policy."""
        excludes = [generator.excludes(**context) for generator in self._generators(**context)]
        return list(chain.from_iterable(excludes))

    @override
    def query_filter(self, **context: Any) -> dsl.query.Query:
        """Search filters."""
        return ConditionalGenerator._make_query(self._generators(**context), **context)  # noqa SLF001 # type: ignore[reportReturnType]
