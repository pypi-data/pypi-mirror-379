# vim: set filetype=python fileencoding=utf-8:
# -*- coding: utf-8 -*-

#============================================================================#
#                                                                            #
#  Licensed under the Apache License, Version 2.0 (the "License");           #
#  you may not use this file except in compliance with the License.          #
#  You may obtain a copy of the License at                                   #
#                                                                            #
#      http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                            #
#  Unless required by applicable law or agreed to in writing, software       #
#  distributed under the License is distributed on an "AS IS" BASIS,         #
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
#  See the License for the specific language governing permissions and       #
#  limitations under the License.                                            #
#                                                                            #
#============================================================================#


''' Immutable dictionaries.

    Dictionaries which cannot be modified after creation.

    .. note::

        While :py:class:`types.MappingProxyType` also provides a read-only view
        of a dictionary, it has important differences from
        :py:class:`Dictionary`:

        * A ``MappingProxyType`` is a view over a mutable dictionary, so its
          contents can still change if the underlying dictionary is modified.
        * ``Dictionary`` owns its data and guarantees that it will never
          change.
        * ``Dictionary`` provides set operations (union, intersection) that
          maintain immutability guarantees.

        Use ``MappingProxyType`` when you want to expose a read-only view of a
        dictionary that might need to change. Use ``Dictionary`` when you want
        to ensure that the data can never change, such as for configuration
        objects or other cases requiring strong immutability guarantees.

    * :py:class:`AbstractDictionary`:
      Base class defining the immutable dictionary interface. Implementations
      must provide ``__getitem__``, ``__iter__``, and ``__len__``.

    * :py:class:`Dictionary`:
      Standard implementation of an immutable dictionary. Supports all usual
      dict read operations but prevents any modifications.

    * :py:class:`ValidatorDictionary`:
      Validates entries before addition using a supplied predicate function.

    >>> from frigid import Dictionary
    >>> d = Dictionary( x = 1, y = 2 )
    >>> d[ 'z' ] = 3  # Attempt to add entry
    Traceback (most recent call last):
        ...
    frigid.exceptions.EntryImmutability: Cannot assign or delete entry for 'z'.
    >>> d[ 'x' ] = 4  # Attempt modification
    Traceback (most recent call last):
        ...
    frigid.exceptions.EntryImmutability: Cannot assign or delete entry for 'x'.
    >>> del d[ 'y' ]  # Attempt removal
    Traceback (most recent call last):
        ...
    frigid.exceptions.EntryImmutability: Cannot assign or delete entry for 'y'.
'''


from . import __
from . import classes as _classes


class AbstractDictionary( __.cabc.Mapping[ __.H, __.V ] ):
    ''' Abstract base class for immutable dictionaries.

        An immutable dictionary prevents modification or removal of entries
        after creation. This provides a clean interface for dictionaries
        that should never change.

        Implementations must provide __getitem__, __iter__, __len__.
    '''

    @__.abc.abstractmethod
    def __iter__( self ) -> __.cabc.Iterator[ __.H ]:
        raise NotImplementedError  # pragma: no coverage

    @__.abc.abstractmethod
    def __len__( self ) -> int:
        raise NotImplementedError  # pragma: no coverage

    @__.abc.abstractmethod
    def __getitem__( self, key: __.H ) -> __.V:
        raise NotImplementedError  # pragma: no coverage

    def __setitem__( self, key: __.H, value: __.V ) -> None:
        from .exceptions import EntryImmutability
        raise EntryImmutability( key )

    def __delitem__( self, key: __.H ) -> None:
        from .exceptions import EntryImmutability
        raise EntryImmutability( key )


class _DictionaryOperations( AbstractDictionary[ __.H, __.V ] ):
    ''' Mix-in providing additional dictionary operations. '''

    # TODO? Common __init__.

    def __or__( self, other: __.cabc.Mapping[ __.H, __.V ] ) -> __.typx.Self:
        if not isinstance( other, __.cabc.Mapping ): return NotImplemented
        conflicts = set( self.keys( ) ) & set( other.keys( ) )
        if conflicts:
            from .exceptions import EntryImmutability
            raise EntryImmutability( next( iter( conflicts ) ) )
        data = dict( self )
        data.update( other )
        return self.with_data( data )

    def __ror__( self, other: __.cabc.Mapping[ __.H, __.V ] ) -> __.typx.Self:
        if not isinstance( other, __.cabc.Mapping ): return NotImplemented
        return self | other

    def __and__(
        self,
        other: __.cabc.Set[ __.H ] | __.cabc.Mapping[ __.H, __.V ]
    ) -> __.typx.Self:
        if isinstance( other, __.cabc.Mapping ):
            return self.with_data(
                ( key, value ) for key, value in self.items( )
                if key in other and other[ key ] == value )
        if isinstance( other, ( __.cabc.Set, __.cabc.KeysView ) ):
            return self.with_data(
                ( key, self[ key ] ) for key in self.keys( ) & other )
        return NotImplemented

    def __rand__(
        self,
        other: __.cabc.Set[ __.H ] | __.cabc.Mapping[ __.H, __.V ]
    ) -> __.typx.Self:
        if not isinstance(
            other, ( __.cabc.Mapping, __.cabc.Set, __.cabc.KeysView )
        ): return NotImplemented
        return self & other

    @__.abc.abstractmethod
    def copy( self ) -> __.typx.Self:
        ''' Provides fresh copy of dictionary. '''
        raise NotImplementedError # pragma: no coverage

    @__.abc.abstractmethod
    def with_data(
        self,
        *iterables: __.DictionaryPositionalArgument[ __.H, __.V ],
        **entries: __.DictionaryNominativeArgument[ __.V ],
    ) -> __.typx.Self:
        ''' Creates new dictionary with same behavior but different data. '''
        raise NotImplementedError # pragma: no coverage


class Dictionary( # noqa: PLW1641
    _DictionaryOperations[ __.H, __.V ],
    metaclass = _classes.AbstractBaseClass,
    class_mutables = _classes.abc_class_mutables,
):
    ''' Immutable dictionary. '''

    __slots__ = ( '_data_', )

    _data_: __.ImmutableDictionary[ __.H, __.V ]
    _dynadoc_fragments_ = ( 'dictionary entries protect', )

    def __init__(
        self,
        *iterables: __.DictionaryPositionalArgument[ __.H, __.V ],
        **entries: __.DictionaryNominativeArgument[ __.V ],
    ) -> None:
        self._data_ = __.ImmutableDictionary( *iterables, **entries )
        super( ).__init__( )

    def __iter__( self ) -> __.cabc.Iterator[ __.H ]:
        return iter( self._data_ )

    def __len__( self ) -> int:
        return len( self._data_ )

    def __repr__( self ) -> str:
        return "{fqname}( {contents} )".format(
            fqname = __.ccutils.qualify_class_name( type( self ) ),
            contents = self._data_.__repr__( ) )

    def __str__( self ) -> str:
        return str( self._data_ )

    def __contains__( self, key: __.typx.Any ) -> bool:
        return key in self._data_

    def __getitem__( self, key: __.H ) -> __.V:
        return self._data_[ key ]

    def __eq__( self, other: __.typx.Any ) -> __.ComparisonResult:
        if isinstance( other, __.cabc.Mapping ):
            return self._data_ == other
        return NotImplemented

    def __ne__( self, other: __.typx.Any ) -> __.ComparisonResult:
        if isinstance( other, __.cabc.Mapping ):
            return self._data_ != other
        return NotImplemented

    def copy( self ) -> __.typx.Self:
        ''' Provides fresh copy of dictionary. '''
        return type( self )( self )

    def get( # pyright: ignore
        self, key: __.H, default: __.Absential[ __.V ] = __.absent
    ) -> __.typx.Annotated[
        __.V,
        __.typx.Doc(
            'Value of entry, if it exists. '
            'Else, supplied default value or ``None``.' )
    ]:
        ''' Retrieves entry associated with key, if it exists. '''
        if __.is_absent( default ):
            return self._data_.get( key ) # pyright: ignore
        return self._data_.get( key, default )

    def keys( self ) -> __.cabc.KeysView[ __.H ]:
        ''' Provides iterable view over dictionary keys. '''
        return self._data_.keys( )

    def items( self ) -> __.cabc.ItemsView[ __.H, __.V ]:
        ''' Provides iterable view over dictionary items. '''
        return self._data_.items( )

    def values( self ) -> __.cabc.ValuesView[ __.V ]:
        ''' Provides iterable view over dictionary values. '''
        return self._data_.values( )

    def with_data(
        self,
        *iterables: __.DictionaryPositionalArgument[ __.H, __.V ],
        **entries: __.DictionaryNominativeArgument[ __.V ],
    ) -> __.typx.Self:
        return type( self )( *iterables, **entries )


class ValidatorDictionary( Dictionary[ __.H, __.V ] ):
    ''' Immutable dictionary with validation of entries on initialization. '''

    __slots__ = ( '_validator_', )

    _dynadoc_fragments_ = (
        'dictionary entries protect', 'dictionary entries validate' )
    _validator_: __.DictionaryValidator[ __.H, __.V ]

    def __init__(
        self,
        validator: __.DictionaryValidator[ __.H, __.V ],
        /,
        *iterables: __.DictionaryPositionalArgument[ __.H, __.V ],
        **entries: __.DictionaryNominativeArgument[ __.V ],
    ) -> None:
        self._validator_ = validator
        entries_: list[ tuple[ __.H, __.V ] ] = [ ]
        from itertools import chain
        # Collect entries in case an iterable is a generator
        # which would be consumed during validation, before initialization.
        for key, value in chain.from_iterable( map( # pyright: ignore
            lambda element: ( # pyright: ignore
                element.items( )
                if isinstance( element, __.cabc.Mapping )
                else element
            ),
            ( *iterables, entries )
        ) ):
            if not self._validator_( key, value ): # pyright: ignore
                from .exceptions import EntryInvalidity
                raise EntryInvalidity( key, value )
            entries_.append( ( key, value ) ) # pyright: ignore
        super( ).__init__( entries_ )

    def __repr__( self ) -> str:
        return "{fqname}( {validator}, {contents} )".format(
            fqname = __.ccutils.qualify_class_name( type( self ) ),
            validator = self._validator_.__repr__( ),
            contents = self._data_.__repr__( ) )

    def copy( self ) -> __.typx.Self:
        ''' Provides fresh copy of dictionary. '''
        return type( self )( self._validator_, self )

    def with_data(
        self,
        *iterables: __.DictionaryPositionalArgument[ __.H, __.V ],
        **entries: __.DictionaryNominativeArgument[ __.V ],
    ) -> __.typx.Self:
        ''' Creates new dictionary with same behavior but different data. '''
        return type( self )( self._validator_, *iterables, **entries )
