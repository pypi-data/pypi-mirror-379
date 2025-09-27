from typing_extensions import Self, Type, Generic, Any, cast

from .common import _propert_setters_name, _propert_deleters_name, _check_feature_enabled
from .types import T, R, S, _NoValue, _CacheReset, _NoValueT, _AnyAction, _ArgCallable

class _base_property(Generic[T, R, S]):
    _cache: bool = False # cache feature
    _pass_instance: bool = False # autoproperty
    _pass_class: bool = False # classproperty (or autoproperty)
    _pass_self: bool = False # introspect feature
    _special_unwrap: type|None = None # automatic handling of special methods

    def __init__(self, getter: _ArgCallable, setter: _ArgCallable|None = None, deleter: _ArgCallable|None = None, *, cache_default: R|_NoValueT=_NoValue, check_metaclass: bool=True):
        self._ensure_metaclass = check_metaclass
        self._mcls_setter_enabled: bool|None = None
        self._mcls_deleter_enabled: bool|None = None

        self._cached_value_map: dict[Any, R] = {}
        self._cached_value_default = cache_default
        self._cached_value_defaults_read = set[Any]()

        self._set_getter(getter)
        self._set_setter(setter, can_be_none=True)
        self._set_deleter(deleter, can_be_none=True)

    def __init_subclass__(cls, *, pass_instance: bool|None=None, pass_class: bool|None=None, pass_self: bool|None=None, cache: bool|None=None, special_unwrap: type|None=None, **kwargs: dict[str, Any]) -> None:
        if pass_instance is not None:
            cls._pass_instance = pass_instance
        if pass_class is not None:
            cls._pass_class = pass_class
        if pass_self is not None:
            cls._pass_self = pass_self

        if cache is not None:
            cls._cache = cache
        if special_unwrap is not None:
            cls._special_unwrap = special_unwrap
        super().__init_subclass__(**kwargs)

    def _handle_special_method(self, func: _AnyAction) -> _AnyAction:
        if self._special_unwrap is None:
            return func
        if isinstance(func, self._special_unwrap):
            return func.__func__ # type: ignore
        return func

    def _get_args(self, instance: T|None, owner: Type[T]) -> list[Any]:
        args = list[Any]()
        if self._pass_instance and instance:
            args.append(instance)
        elif self._pass_class:
            args.append(owner)

        if self._pass_self:
            args.append(self)
        
        return args

    def getter(self, func: _ArgCallable) -> Self:
        """Create copy of this property with the new getter"""
        if self._getter or self._setter or self._deleter:
            return type(self)(func, self._setter, self._deleter)
        self._set_getter(func)
        return self

    def _set_getter(self, getter: _ArgCallable|None, *, can_be_none: bool=False) -> None:
        if (getter is None) and (not can_be_none):
            raise ValueError("Getter must not be None")
        getter = self._handle_special_method(getter)
        self._getter = getter

    def _get(self, instance: T|None, owner: Type[T]) -> R:
        if not self._getter:
            raise AttributeError("Property cannot be retrieved because no getter was declared")
        
        cache_key = self._get_cache_key(instance, owner)
        if self._cache and (cache_key in self._cached_value_map):
            return self._cached_value_map[cache_key]
        
        if self._cache and (cache_key not in self._cached_value_defaults_read) and (not isinstance(self._cached_value_default, _NoValueT)):
            self._cached_value_defaults_read.add(cache_key)
            self._cached_value_map[cache_key] = self._cached_value_default
            return self._cached_value_default
        
        value = cast(R, self._getter(*self._get_args(instance, owner)))
        
        if self._cache:
            self._cached_value_map[cache_key] = value
        
        return value

    def __get__(self, instance: T|None, owner: Type[T]) -> R:
        return self._get(instance, owner)

    def __call__(self, func: _ArgCallable) -> Self:
        return self.getter(func)
    
    def setter(self, func: _ArgCallable) -> Self:
        self._set_setter(func)
        return self

    def _set_setter(self, setter: _ArgCallable|None, *, can_be_none: bool = False) -> None:
        if (setter is None) and (not can_be_none):
            raise ValueError("Setter must not be None")
        if setter and (self._mcls_setter_enabled is False) and self._ensure_metaclass:
            raise AttributeError("You tried to declare a setter on a property, but the metaclass of the owner class does not allow setter features")
        setter = self._handle_special_method(setter)
        self._setter = setter

    def _set(self, instance: T|None, owner: Type[T], value: S) -> None:
        if not self._setter:
            raise AttributeError("Property cannot be set, because no setter was declared")
        new_value = self._setter(*self._get_args(instance, owner), value)
        if self._cache and (new_value is not _NoValue):
            cache_key = self._get_cache_key(instance, owner)
            if new_value is _CacheReset:
                self._reset_cache(cache_key)
            else:
                self._cached_value_map[cache_key] = new_value

    def __set__(self, instance: T, value: S) -> None: # type: ignore[misc]
        return self._set(instance, type(instance), value)

    def deleter(self, func: _ArgCallable) -> Self:
        self._set_deleter(func)
        return self

    def _set_deleter(self, deleter: _ArgCallable|None, *, can_be_none: bool = False) -> None:
        if (deleter is None) and (not can_be_none):
            raise ValueError("Deleter must not be None")
        if deleter and (self._mcls_deleter_enabled is False) and self._ensure_metaclass:
            raise AttributeError("You tried to declare a deleter on a property, but the metaclass of the owner class does not allow deleter features")
        deleter = self._handle_special_method(deleter)
        self._deleter = deleter

    def _del(self, instance: T|None, owner: Type[T]) -> None:
        reset_cache = True
        if self._deleter:
            reset_cache = self._deleter(*self._get_args(instance, owner))
        elif not self._cache:
            raise AttributeError("Property cannot be deleted because no deleter was declared")
        
        if reset_cache is True:
            cache_key = self._get_cache_key(instance, owner)
            self._reset_cache(cache_key)

    def __delete__(self, instance: T) -> None: # type: ignore[misc]
        self._del(instance, type(instance))

    def _reset_cache(self, key: Any) -> None:
        if key is None:
            self._cached_value_map.clear()
            return

        if key not in self._cached_value_map:
            return
        del self._cached_value_map[key]

    def _get_cache_key(self, instance: T|None, owner: Type[T]|None) -> Any:
        if owner is None:
            return None
        if self._pass_class:
            return owner
        return None

    def __set_name__(self, owner: Type[T], name: str) -> None:
        self._mcls_setter_enabled = _check_feature_enabled(owner, _propert_setters_name)
        self._mcls_deleter_enabled = _check_feature_enabled(owner, _propert_deleters_name)

        if not self._ensure_metaclass:
            return

        _unchecked_mods = []
        if self._setter and not self._mcls_setter_enabled:
            _unchecked_mods.append("setter")

        if self._deleter and not self._mcls_deleter_enabled:
            _unchecked_mods.append("deleter")

        if not _unchecked_mods:
            return

        _error_mods = " and a ".join(_unchecked_mods)
        _error_feat = "these features" if len(_unchecked_mods) > 1 else "this feature"
        raise AttributeError(f"You tried to declare a {_error_mods} on a property, but the metaclass of the owner class does not allow {_error_feat}")

class _cached_property_mixin(Generic[R]):
    NO_VALUE = _NoValue
    CACHE_RESET = _CacheReset
    def reset_cache(self, cls: Type[T]|None) -> None:
        """
        Reset this properties cache for the given class
        If you pass None, the cache for all classes (including subclasses and parent classes) will be reset
        """
        if not isinstance(self, _base_property):
            return
        cache_key = self._get_cache_key(None, cls)
        self._reset_cache(cache_key)
