# ================================== LICENSE ===================================
# Magnopy - Python package for magnons.
# Copyright (C) 2023-2025 Magnopy Team
#
# e-mail: anry@uv.es, web: magnopy.org
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ================================ END LICENSE =================================


import numpy as np

from magnopy._data_validation import _validate_atom_index, _validated_units
from magnopy._constants._units import _PARAMETER_UNITS


@property
def _p31(spinham) -> list:
    r"""
    Parameters of (three spins & one site) term of the Hamiltonian.

    .. math::

        \boldsymbol{J}_{3,1}(\boldsymbol{r}_{\alpha})

    of the term

    .. math::

        C_{3,1}
        \sum_{\mu, \alpha, i, j, u}
        J^{iju}_{3,1}(\boldsymbol{r}_{\alpha})
        S_{\mu,\alpha}^i
        S_{\mu,\alpha}^j
        S_{\mu,\alpha}^u

    Returns
    -------
    parameters : list
        List of parameters. The list has a form of

        .. code-block:: python

            [[alpha, J], ...]

        ``0 <= len(parameters) <= len(spinham.atoms.names)``.

        where ``alpha`` is an index of the atom to which the parameter is assigned and
        ``J`` is a (3, 3, 3) :numpy:`ndarray`. The parameters are sorted by the index of
        an atom ``alpha`` in the ascending order.

    See Also
    --------
    add_31
    remove_31
    """

    return spinham._31


def _add_31(spinham, alpha: int, parameter, units=None, replace=False) -> None:
    r"""
    Adds a (three spins & one site) parameter to the Hamiltonian.

    Parameters
    ----------
    alpha : int
        Index of an atom, with which the parameter is associated.

        ``0 <= alpha < len(spinham.atoms.names)``.
    parameter : (3, 3, 3) |array-like|_
        Value of the parameter (:math:`3\times3\times3` tensor). Given in the units of ``units``.
    units : str, optional
        Units in which the ``parameter`` is given. Parameters have the the units of energy.
        By default assumes :py:attr:`.SpinHamiltonian.units`. For the list of the supported
        units see :ref:`user-guide_usage_units_parameter-units`. If given ``units`` are different from
        :py:attr:`.SpinHamiltonian.units`, then the parameter's value will be converted
        automatically from ``units`` to :py:attr:`.SpinHamiltonian.units`.

        .. versionadded:: 0.3.0

    replace : bool, default False
        Whether to replace the value of the parameter if an atom already has a
        parameter associated with it.

    Raises
    ------
    ValueError
        If an atom already has a parameter associated with it.

    See Also
    --------
    p31
    remove_31
    """

    _validate_atom_index(index=alpha, atoms=spinham.atoms)
    spinham._reset_internals()

    parameter = np.array(parameter)

    if units is not None:
        units = _validated_units(units=units, supported_units=_PARAMETER_UNITS)
        parameter = (
            parameter * _PARAMETER_UNITS[units] / _PARAMETER_UNITS[spinham._units]
        )

    # TD-BINARY_SEARCH
    # Try to find the place for the new one inside the list
    index = 0
    while index < len(spinham._31):
        # If already present in the model
        if spinham._31[index][0] == alpha:
            # Either replace
            if replace:
                spinham._31[index] = [alpha, parameter]
                return
            # Or raise an error
            raise ValueError(
                f"On-site cubic anisotropy already set "
                f"for atom {alpha} ('{spinham.atoms.names[alpha]}')"
            )

        # If it should be inserted before current element
        if spinham._31[index][0] > alpha:
            spinham._31.insert(index, [alpha, parameter])
            return

        index += 1

    # If it should be inserted at the end or at the beginning of the list
    spinham._31.append([alpha, parameter])


def _remove_31(spinham, alpha: int) -> None:
    r"""
    Removes a (three spins & one site) parameter from the Hamiltonian.

    Parameters
    ----------
    alpha : int
        Index of an atom, with which the parameter is associated.

        ``0 <= alpha < len(spinham.atoms.names)``.

    See Also
    --------
    p31
    add_31
    """

    _validate_atom_index(index=alpha, atoms=spinham.atoms)

    for i in range(len(spinham._31)):
        # As the list is sorted, there is no point in resuming the search
        # when a larger element is found
        if spinham._31[i][0] > alpha:
            return

        if spinham._31[i][0] == alpha:
            del spinham._31[i]
            spinham._reset_internals()
            return
