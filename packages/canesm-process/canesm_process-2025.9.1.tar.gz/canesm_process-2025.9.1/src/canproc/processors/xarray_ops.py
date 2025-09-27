from functools import partial
import functools
import xarray as xr
from typing import Callable, Any
import operator
import logging
import uuid


def xarray_method(f, *args, **kwargs):
    if kwargs is None:
        kwargs = {}
    try:
        if len(args) > 1:
            return getattr(args[0], f)(*args[1:], **kwargs)
        else:
            return getattr(args[0], f)(**kwargs)
    except AttributeError:
        raise AttributeError(f"xarray Dataset contains no function {f}.")


def assign_bounds_to_coords(data: xr.Dataset, postfix: str = "bnds") -> xr.Dataset:
    """
    Set any variables ending in `postfix` to coordinates
    """
    bnds = [bnd for bnd in data if postfix in bnd]
    return data.set_coords(bnds)


def array_name(data: xr.Dataset) -> str:
    """
    Get the name of a single array in a dataset.

    Raises
    ------
        ValueError if more than one variable is present in the dataset
    """
    try:
        (name,) = list(data.data_vars)
        return name
    except ValueError:
        raise ValueError(
            f"only xarray datasets with a single array are supported, found {list(data.data_vars)}"
        )


def to_array(data: Any) -> Any:
    """
    Convert an xarray dataset with a single variable to an array

    Parameters
    ----------
    data : Any
        input data

    Returns
    -------
    Any
        if input is an xr.Dataset it returns an xr.DataArray, else input

    Raises
    ------
    ValueError
        If the input dataset has more than one array there is no way to determine
        what array should be extracted and ValueError is raised
    """
    if isinstance(data, xr.Dataset):

        assign_bounds_to_coords(data, "bnds")
        name = array_name(data)
        return data[name]

    return data


def to_dataset(data):

    if isinstance(data, xr.DataArray):
        try:
            # TODO: is this neccessary or can we fix this at a higher level?
            # TODO: name is dropped if arrays have different names, e.g. FSO - FSR results in name=None
            if data.name is None:
                name = str(uuid.uuid4())
            else:
                name = data.name
            return data.to_dataset(name=name)
        except Exception as e:
            logging.error(f"could not convert {data} to dataset name = {data.name}")
            raise e

    return data


def xarray_operator(func: Callable[[Any, Any], Any]) -> Callable[[Any, Any], Any]:
    """
    Return a function that applies an operator to two xarray dataArrays.
    This wraps the operator so that it first renames the xarray datasets to a common name
    before applying the function. This is a convenience function so we can call

    >>> ds1 + ds2

    instead of

    >>> (ds1['var1'] + ds2['var2']).to_dataset()

    while maintaining coordinates such as bounds

    Parameters
    ----------
    func : Callable
        function that takes in two xarray objects

    Returns
    -------
    Callable[[Any, Any]]
        function that can be applied to xarray datasets
    """

    @functools.wraps(func)
    def wrapper(a, b):

        try:

            # get a common name
            try:
                name = array_name(a)
            except:
                name = array_name(b)

            # give dataset arrays a constistent name
            if isinstance(a, xr.Dataset):
                a = a.rename({array_name(a): name})

            if isinstance(b, xr.Dataset):
                b = b.rename({array_name(b): name})

            return func(a, b)

        except Exception as e:
            logging.error(f"could not perform {func} on {a}, {b}")
            raise e

    wrapper.__wrapper__ = "xarray"
    return wrapper


def xarray_factory(name: str) -> Callable:
    """
    Given a string return the xarray function. All strings should be prefaced with'xr'.
    If a method on a class is desired preface the function name with 'xr.self'. Supports
    all xarray methods and methods from the python `operater` module provided they are
    supported by xarray.

    Examples
    --------
    >>> xarray_factory('xr.concat')
    >>> xarray_factory('xr.self.resample)
    >>> xarray_factory('xr.add')

    Parameters
    ----------
    name : str
        name of the function

    Returns
    -------
    Callable
        xarray function
    """
    if "self" in name.split("."):
        # e.g. xr.self.resample
        return partial(xarray_method, name.split(".")[2])
    try:
        # e.g. xr.concat
        return getattr(xr, name.split(".")[1])
    except AttributeError:
        # e.g. dataset1 + dataset2
        return xarray_operator(getattr(operator, name.split(".")[1]))
