# -----------------------------------------------------------------------------
# Nom du projet : cfContext
# Fichier        : cfcontext.py
# Auteur         : Jimmy Cogordan (Jimw)
# Date           : 2024-05-15
# Description    : `cfcontext` is a lightweight library for managing shared 
#                  contexts within a Python application. It allows you to 
#                  create, replace, and handle dynamic contextual objects that 
#                  are inherited across the call stack frames, ensuring 
#                  consistency throughout nested function calls and asynchronous
#                  tasks.
# Version        : 1.1
# -----------------------------------------------------------------------------
# Copyright (c) 2024 Jimmy Cogordan (Jimw). Tous droits réservés.
#
# Ce fichier fait partie de cfContext. Vous ne pouvez pas redistribuer et/ou
# modifier ce fichier sans l'autorisation expresse préalable de Jimmy Cogordan 
# (Jimw).
#
# cfContext est distribué dans l'espoir qu'il sera utile,
# mais SANS AUCUNE GARANTIE ; sans même la garantie implicite de
# COMMERCIALISATION ou D'ADÉQUATION À UN BUT PARTICULIER.
# -----------------------------------------------------------------------------


from sys import _getframe
from types import FrameType
from typing import Any, Callable, Generator, Optional, TypeVar

__all__ = ['Context', 'copy_context', 'replace_context', 'get_context', 'clear_context', 'update_context']

_no_value = object()
T = TypeVar('T')

class Context:
    __slots__ = ('__frame__', '_previous_context', '__dict__')

    @classmethod
    def _get_context(cls, frame: Optional[FrameType]) -> Optional['Context']:
        """
        Retrieves the nearest Context instance from the call stack (starting from the given frame).
        If no Context is found, returns None.
        """
        while frame is not None:
            ctx = frame.f_locals.get('__CFCONTEXT__')
            if ctx is not None:
                return ctx
            frame = frame.f_back

        return None

    @classmethod
    def _set_context(cls, frame: FrameType, data: dict, derive_from=None) -> 'Context':
        """
        Sets the context for the given frame with the provided data.
        If derive_from is provided, it will be used as the base context.
        """
        # If derive_from is provided, use it as the base context
        if derive_from is not None:
            ctx = derive_from
        else: # Else try to get the existing context from the frame
            ctx = cls._get_context(frame)
            # If no context exists, create a new one
            if ctx is None:
                ctx = cls.create()
        
        # If the context is not associated with the current frame, create a copy
        if ctx.__frame__ is not frame:
            ctx = ctx.copy()
            object.__setattr__(ctx, '__frame__', frame)
            frame.f_locals['__CFCONTEXT__'] = ctx
        
        assert ctx.__frame__ is frame
        assert frame.f_locals['__CFCONTEXT__'] is ctx

        # Update the context with the new data
        ctx.__dict__.update(data)
        for k in Context.__slots__: # Prevent overwriting reserved attributes
            ctx.__dict__.pop(k, None)
        return ctx

    def __new__(cls, __frame_num=1, __create_only=False, **kwargs):
        """
        Creates a new Context instance or updates an existing one.
        If __create_only is True, a new Context instance is created without
        associating it with any frame.
        """
        __frame_num = kwargs.pop('__frame_num', 1) 
        __create_only = kwargs.pop('__create_only', False)

        if __create_only:
            ctx = super().__new__(cls)
            object.__setattr__(ctx, '__dict__', kwargs)
            return ctx
        
        f = _getframe(__frame_num)
        return cls._set_context(f, kwargs)

    @staticmethod
    def create(**kwargs) -> 'Context':
        """
        Creates a new Context instance without associating it with any frame.
        """
        return Context(__create_only=True, **kwargs)

    def __init__(self, __frame_num=1, __create_only=False, **kwargs):
        # Initialization is handled in __new__
        pass

    def __getattr__(self, name: str):
        # default behavior for inexistent attributes
        return None

    def __setattr__(self, name: str, value) -> None:
        if name in Context.__slots__:
            # Prevent setting reserved attributes
            raise AttributeError(f'{name} attribute is reserved. Do not set manually.')
        if self.__frame__ is None:
            # If the context is not associated with any frame, set the attribute directly
            return object.__setattr__(self, name, value)
        f = _getframe(1)
        self._set_context(f, {name: value}, self)

    def __repr__(self) -> str:
        args = ",".join([f"{k}={repr(v)}" for k, v in self.items()])
        return f"{self.__class__.__qualname__}({args})"

    def __getitem__(self, k):
        """Gets an attribute from the context."""
        if k in Context.__slots__:
            raise KeyError(k)
        return getattr(self, k)

    def __setitem__(self, k, v):
        """Sets an attribute in the context."""
        if k in Context.__slots__:
            raise KeyError(k)
        setattr(self, k, v)

    def keys(self) -> Generator[str, None, None]:
        """Yields the keys of the context attributes."""
        for k in self.__dict__:
            if k not in Context.__slots__:
                yield k

    def __iter__(self) -> Generator[str, None, None]:
        return self.keys()

    def items(self) -> Generator[tuple[str, Any], None, None]:
        """Yields key-value pairs of the context attributes."""
        for k, v in self.__dict__.items():
            if k not in Context.__slots__:
                yield k, v

    def __len__(self):
        return len(self.__dict__)

    def __eq__(self, other):
        if self is other:
            return True
        
        if not isinstance(other, self.__class__):
            return False

        if len(self) != len(other):
            return False

        for k, v in self.__dict__.items():
            #if k not in Context.__slots__:
            if k not in other or v != other[k]:
                return False

        return True
    
    def __contains__(self, k):
        if k in Context.__slots__:
            return False
        return k in self.__dict__

    def copy(self) -> 'Context':
        """Returns a shallow copy of the context."""
        ctx = self.__class__(__create_only=True)
        object.__setattr__(ctx,'__dict__',self.__dict__.copy())
        #ctx.__dict__.pop('__frame__', None)
        return ctx

    def to_dict(self) -> dict[str, Any]:
        """Returns a dictionary representation of the context."""
        result = self.__dict__.copy()
        #result.pop('__frame__', None)
        return result

    def update(self, d: dict[str, Any]) -> None:
        if self.__frame__ is None:
            self.__dict__.update(d)
            for k in Context.__slots__: # Prevent overwriting reserved attributes
                self.__dict__.pop(k, None)
        else:
            f = _getframe(1)
            self._set_context(f, d)

    def clear(self) -> None:
        """Clears the context."""
        if self.__frame__ is None:
            self.__dict__.clear()
        else:
            f = _getframe(1)
            self._set_context(f, {}, self.__class__(__create_only=True))

    def run(self, callable: Callable[..., T], *args, **kwargs) -> T:
        """Runs a callable within the context."""
        self.__class__._set_context(_getframe(0), {}, self)
        return callable(*args, **kwargs)
    
    def apply(self) -> 'Context':
        """Applies the context to the current frame."""
        return self._set_context(_getframe(1), {}, self)
    
    def __enter__(self) -> 'Context':
        """
        Enters a copy of the context, saving the current context.
        """
        ctx = self.copy()
        frame = _getframe(1)
        object.__setattr__(ctx, '_previous_context', self._get_context(frame))
        object.__setattr__(ctx, '__frame__', frame)
        frame.f_locals['__CFCONTEXT__'] = ctx
        if '__cfcontext_cleanup__' in frame.f_locals:
            previous_cleanup = frame.f_locals['__cfcontext_cleanup__']
            def cleanup():
                object.__setattr__(ctx, '__frame__', None)
                if ctx._previous_context:
                    if ctx._previous_context.__frame__ is frame:
                        frame.f_locals['__CFCONTEXT__'] = ctx._previous_context
                    else:
                        del frame.f_locals['__CFCONTEXT__']
                    object.__setattr__(ctx, '_previous_context', None)
                frame.f_locals['__cfcontext_cleanup__'] = previous_cleanup
        else:
            def cleanup():
                object.__setattr__(ctx, '__frame__', None)
                if ctx._previous_context:
                    if ctx._previous_context.__frame__ is frame:
                        frame.f_locals['__CFCONTEXT__'] = ctx._previous_context
                    else:
                        del frame.f_locals['__CFCONTEXT__']
                    object.__setattr__(ctx, '_previous_context', None)
                del frame.f_locals['__cfcontext_cleanup__']
        frame.f_locals['__cfcontext_cleanup__'] = cleanup
        return ctx

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        frame = _getframe(1)
        if '__cfcontext_cleanup__' in frame.f_locals:
            frame.f_locals['__cfcontext_cleanup__']()


def replace_context(ctx: Context):
    """Replaces the current context with the provided one."""
    f = _getframe(1)
    Context._set_context(f, {}, ctx)

def copy_context() -> Context:
    """Returns a copy of the current context."""
    return Context().copy()

def get_context() -> Context | None:
    """Returns the current context."""
    return Context._get_context(_getframe(1))

def clear_context() -> None:
    """Clears the current context."""
    f = _getframe(1)
    ctx = Context._get_context(f)
    if ctx is not None:
        ctx.clear()

def update_context(d: dict[str, Any]) -> None:
    """Updates the current context with the provided dictionary."""
    f = _getframe(1)
    Context._set_context(f, d)

