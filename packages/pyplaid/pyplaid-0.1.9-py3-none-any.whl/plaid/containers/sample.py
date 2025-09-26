"""Implementation of the `Sample` container."""

# -*- coding: utf-8 -*-
#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.
#
#

# %% Imports
import sys

if sys.version_info >= (3, 11):
    from typing import Self
else:  # pragma: no cover
    from typing import TypeVar

    Self = TypeVar("Self")

import copy
import logging
import shutil
from pathlib import Path
from typing import Any, Optional, Union

import CGNS.MAP as CGM
import CGNS.PAT.cgnskeywords as CGK
import CGNS.PAT.cgnslib as CGL
import CGNS.PAT.cgnsutils as CGU
import numpy as np
from pydantic import BaseModel, ConfigDict, PrivateAttr
from pydantic import Field as PydanticField

from plaid.constants import (
    AUTHORIZED_FEATURE_INFOS,
    AUTHORIZED_FEATURE_TYPES,
    CGNS_FIELD_LOCATIONS,
)
from plaid.containers.features import SampleMeshes, SampleScalars
from plaid.containers.utils import _check_names, get_feature_type_and_details_from
from plaid.types import (
    CGNSNode,
    CGNSTree,
    Feature,
    FeatureIdentifier,
    Field,
    Scalar,
    TimeSequence,
    TimeSeries,
)
from plaid.utils import cgns_helper as CGH
from plaid.utils.base import safe_len
from plaid.utils.deprecation import deprecated

logger = logging.getLogger(__name__)


class Sample(BaseModel):
    """Represents a single sample. It contains data and information related to a single observation or measurement within a dataset.

    By default, the sample is empty but:
        - You can provide a path to a folder containing the sample data, and it will be loaded during initialization.
        - You can provide `SampleMeshes` and `SampleScalars` instances to initialize the sample with existing data.
        - You can also provide a dictionary of time series data.

    The default `SampleMeshes` instance is initialized with:
        - `meshes=None`, `links=None`, and `paths=None` (i.e., no mesh data).
        - `mesh_base_name="Base"` and `mesh_zone_name="Zone"`.

    The default `SampleScalars` instance is initialized with:
        - `scalars=None` (i.e., no scalar data).
    """

    # Pydantic configuration
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        revalidate_instances="always",
    )

    # Attributes
    path: Optional[Union[str, Path]] = PydanticField(
        None,
        description="Path to the folder containing the sample data. If provided, the sample will be loaded from this path during initialization. Defaults to None.",
    )

    meshes: Optional[SampleMeshes] = PydanticField(
        default_factory=lambda _: SampleMeshes(
            meshes=None,
            mesh_base_name="Base",
            mesh_zone_name="Zone",
            links=None,
            paths=None,
        ),
        description="An instance of SampleMeshes containing mesh data. Defaults to an empty `SampleMeshes` object.",
    )
    scalars: Optional[SampleScalars] = PydanticField(
        default_factory=lambda _: SampleScalars(scalars=None),
        description="An instance of SampleScalars containing scalar data. Defaults to an empty `SampleScalars` object.",
    )
    time_series: Optional[dict[str, TimeSeries]] = PydanticField(
        None,
        description="A dictionary mapping time series names to their corresponding data. Defaults to None.",
    )

    # Private attributes
    _extra_data: Optional[dict] = PrivateAttr(default=None)

    def model_post_init(self, _context: Any) -> None:
        """Post-initialization processing for the Sample model."""
        # Load if path is provided
        if self.path is not None:
            path = Path(self.path)
            self.load(path)

    def copy(self) -> Self:  # pyright: ignore[reportIncompatibleMethodOverride]
        """Create a deep copy of the current `Sample` instance.

        Usage of `model_copy(deep=True)` from Pydantic to ensure all internal data is deeply copied.

        Returns:
            A new `Sample` instance with all internal data (scalars, time series, fields, meshes, etc.)
            deeply copied to ensure full isolation from the original.

        Note:
            This operation may be memory-intensive for large samples.
        """
        return self.model_copy(deep=True)

    def get_scalar(self, name: str) -> Optional[Scalar]:
        """Retrieve a scalar value associated with the given name.

        Args:
            name (str): The name of the scalar value to retrieve.

        Returns:
            Scalar or None: The scalar value associated with the given name, or None if the name is not found.
        """
        return self.scalars.get(name)

    def add_scalar(self, name: str, value: Scalar) -> None:
        """Add a scalar value to a dictionary.

        Args:
            name (str): The name of the scalar value.
            value (Scalar): The scalar value to add or update in the dictionary.
        """
        self.scalars.add(name, value)

    def del_scalar(self, name: str) -> Scalar:
        """Delete a scalar value from the dictionary.

        Args:
            name (str): The name of the scalar value to be deleted.

        Raises:
            KeyError: Raised when there is no scalar / there is no scalar with the provided name.

        Returns:
            Scalar: The value of the deleted scalar.
        """
        return self.scalars.remove(name)

    def get_scalar_names(self) -> list[str]:
        """Get a set of scalar names available in the object.

        Returns:
            list[str]: A set containing the names of the available scalars.
        """
        return self.scalars.get_names()

    # -------------------------------------------------------------------------#

    def get_mesh(
        self, time: Optional[float] = None, apply_links: bool = False, in_memory=False
    ) -> Optional[CGNSTree]:
        """Retrieve the CGNS tree structure for a specified time step, if available.

        Args:
            time (float, optional): The time step for which to retrieve the CGNS tree structure. If a specific time is not provided, the method will display the tree structure for the default time step.
            apply_links (bool, optional): Activates the following of the CGNS links to reconstruct the complete CGNS tree - in this case, a deepcopy of the tree is made to prevent from modifying the existing tree.
            in_memory (bool, optional): Active if apply_links == True, ONLY WORKING if linked mesh is in the current sample. This option follows the link in memory from current sample.

        Returns:
            CGNSTree: The CGNS tree structure for the specified time step if available; otherwise, returns None.
        """
        return self.meshes.get_mesh(time, apply_links, in_memory)

    def set_default_base(self, base_name: str, time: Optional[float] = None) -> None:
        """Set the default base for the specified time (that will also be set as default if provided).

        The default base is a reference point for various operations in the system.

        Args:
            base_name (str): The name of the base to be set as the default.
            time (float, optional): The time at which the base should be set as default. If not provided, the default base and active zone will be set with the default time.

        Raises:
            ValueError: If the specified base does not exist at the given time.

        Note:
            - Setting the default base and is important for synchronizing operations with a specific base in the system's data.
            - The available mesh base can be obtained using the `get_base_names` method.

        Example:
            .. code-block:: python

                from plaid import Sample
                sample = Sample("path_to_plaid_sample")
                print(sample)
                >>> Sample(2 scalars, 1 timestamp, 5 fields)
                print(sample.get_physical_dim("BaseA", 0.5))
                >>> 3

                # Set "BaseA" as the default base for the default time
                sample.set_default_base("BaseA")

                # You can now use class functions with "BaseA" as default base
                print(sample.get_physical_dim(0.5))
                >>> 3

                # Set "BaseB" as the default base for a specific time
                sample.set_default_base("BaseB", 0.5)

                # You can now use class functions with "BaseB" as default base and 0.5 as default time
                print(sample.get_physical_dim()) # Physical dim of the base "BaseB"
                >>> 3
        """
        if time is not None:
            self.set_default_time(time)
        if base_name in (self.meshes._default_active_base, None):
            return
        if not self.meshes.has_base(base_name, time):
            raise ValueError(f"base {base_name} does not exist at time {time}")

        self.meshes._default_active_base = base_name

    def set_default_zone_base(
        self, zone_name: str, base_name: str, time: Optional[float] = None
    ) -> None:
        """Set the default base and active zone for the specified time (that will also be set as default if provided).

        The default base and active zone serve as reference points for various operations in the system.

        Args:
            zone_name (str): The name of the zone to be set as the active zone.
            base_name (str): The name of the base to be set as the default.
            time (float, optional): The time at which the base and zone should be set as default. If not provided, the default base and active zone will be set with the default time.

        Raises:
            ValueError: If the specified base or zone does not exist at the given time

        Note:
            - Setting the default base and zone are important for synchronizing operations with a specific base/zone in the system's data.
            - The available mesh bases and zones can be obtained using the `get_base_names` and `get_base_zones` methods, respectively.

        Example:
            .. code-block:: python

                from plaid import Sample
                sample = Sample("path_to_plaid_sample")
                print(sample)
                >>> Sample(2 scalars, 1 timestamp, 5 fields)
                print(sample.get_zone_type("ZoneX", "BaseA", 0.5))
                >>> Structured

                # Set "BaseA" as the default base and "ZoneX" as the active zone for the default time
                sample.set_default_zone_base("ZoneX", "BaseA")

                # You can now use class functions with "BaseA" as default base with "ZoneX" as default zone
                print(sample.get_zone_type(0.5)) # type of the zone "ZoneX" of base "BaseA"
                >>> Structured

                # Set "BaseB" as the default base and "ZoneY" as the active zone for a specific time
                sample.set_default_zone_base("ZoneY", "BaseB", 0.5)

                # You can now use class functions with "BaseB" as default base with "ZoneY" as default zone and 0.5 as default time
                print(sample.get_zone_type()) # type of the zone "ZoneY" of base "BaseB" at 0.5
                >>> Unstructured
        """
        self.set_default_base(base_name, time)
        if zone_name in (self.meshes._default_active_zone, None):
            return
        if not self.meshes.has_zone(zone_name, base_name, time):
            raise ValueError(
                f"zone {zone_name} does not exist for the base {base_name} at time {time}"
            )

        self.meshes._default_active_zone = zone_name

    def init_base(
        self,
        topological_dim: int,
        physical_dim: int,
        base_name: Optional[str] = None,
        time: Optional[float] = None,
    ) -> CGNSNode:
        """Create a Base node named `base_name` if it doesn't already exists.

        Args:
            topological_dim (int): Cell dimension, see [CGNS standard](https://pycgns.github.io/PAT/lib.html#CGNS.PAT.cgnslib.newCGNSBase).
            physical_dim (int): Ambient space dimension, see [CGNS standard](https://pycgns.github.io/PAT/lib.html#CGNS.PAT.cgnslib.newCGNSBase).
            base_name (str): If not specified, uses `mesh_base_name` specified in Sample initialization. Defaults to None.
            time (float, optional): The time at which to initialize the base. If a specific time is not provided, the method will display the tree structure for the default time step.

        Returns:
            CGNSNode: The created Base node.
        """
        return self.meshes.init_base(topological_dim, physical_dim, base_name, time)

    def init_zone(
        self,
        zone_shape: np.ndarray,
        zone_type: str = CGK.Unstructured_s,
        zone_name: Optional[str] = None,
        base_name: Optional[str] = None,
        time: Optional[float] = None,
    ) -> CGNSNode:
        """Initialize a new zone within a CGNS base.

        Args:
            zone_shape (np.ndarray): An array specifying the shape or dimensions of the zone.
            zone_type (str, optional): The type of the zone. Defaults to CGK.Unstructured_s.
            zone_name (str, optional): The name of the zone to initialize. If not provided, uses `mesh_zone_name` specified in Sample initialization. Defaults to None.
            base_name (str, optional): The name of the base to which the zone will be added. If not provided, the zone will be added to the currently active base. Defaults to None.
            time (float, optional): The time at which to initialize the zone. If a specific time is not provided, the method will display the tree structure for the default time step.

        Raises:
            KeyError: If the specified base does not exist. You can create a base using `Sample.init_base(base_name)`.

        Returns:
            CGLNode: The newly initialized zone node within the CGNS tree.
        """
        return self.meshes.init_zone(zone_shape, zone_type, zone_name, base_name, time)

    def set_default_time(self, time: float) -> None:
        """Set the default time for the system.

        This function sets the default time to be used for various operations in the system.

        Args:
            time (float): The time value to be set as the default.

        Raises:
            ValueError: If the specified time does not exist in the available mesh times.

        Note:
            - Setting the default time is important for synchronizing operations with a specific time point in the system's data.
            - The available mesh times can be obtained using the `get_all_mesh_times` method.

        Example:
            .. code-block:: python

                from plaid import Sample
                sample = Sample("path_to_plaid_sample")
                print(sample)
                >>> Sample(2 scalars, 1 timestamp, 5 fields)
                print(sample.show_tree(0.5))
                >>> ...

                # Set the default time to 0.5 seconds
                sample.set_default_time(0.5)

                # You can now use class functions with 0.5 as default time
                print(sample.show_tree()) # show the cgns tree at the time 0.5
                >>> ...
        """
        if time in (self.meshes._default_active_time, None):
            return
        if time not in self.meshes.get_all_mesh_times():
            raise ValueError(f"time {time} does not exist in mesh times")

        self.meshes._default_active_time = time

    def get_field_names(
        self,
        location: str = None,
        zone_name: Optional[str] = None,
        base_name: Optional[str] = None,
        time: Optional[float] = None,
    ) -> list[str]:
        """Get a set of field names associated with a specified zone, base, location, and time.

        Args:
            location (str, optional): The desired grid location where the field is defined. Defaults to None.
                Possible values : :py:const:`plaid.constants.CGNS_FIELD_LOCATIONS`
            zone_name (str, optional): The name of the zone to search for. Defaults to None.
            base_name (str, optional): The name of the base to search for. Defaults to None.
            time (float, optional): The specific time at which to retrieve field names. If a specific time is not provided, the method will display the tree structure for the default time step.

        Returns:
            set[str]: A set containing the names of the fields that match the specified criteria.
        """
        return self.meshes.get_field_names(
            location=location, zone_name=zone_name, base_name=base_name, time=time
        )

    # -------------------------------------------------------------------------#

    def link_tree(
        self,
        path_linked_sample: Union[str, Path],
        linked_sample: "Sample",
        linked_time: float,
        time: float,
    ) -> CGNSTree:
        """Link the geometrical features of the CGNS tree of the current sample at a given time, to the ones of another sample.

        Args:
            path_linked_sample (Union[str,Path]): The absolute path of the folder containing the linked CGNS
            linked_sample (Sample): The linked sample
            linked_time (float): The time step of the linked CGNS in the linked sample
            time (float): The time step the current sample to which the CGNS tree is linked.

        Returns:
            CGNSTree: The deleted CGNS tree.
        """
        # see https://pycgns.github.io/MAP/sids-to-python.html#links
        # difficulty is to link only the geometrical objects, which can be complex

        # https://pycgns.github.io/MAP/examples.html#save-with-links
        # When you load a file all the linked-to files are resolved to produce a full CGNS/Python tree with actual node data.

        path_linked_sample = Path(path_linked_sample)

        if linked_time not in linked_sample.meshes.data:  # pragma: no cover
            raise KeyError(
                f"There is no CGNS tree for time {linked_time} in linked_sample."
            )
        if time in self.meshes.data:  # pragma: no cover
            raise KeyError(f"A CGNS tree is already linked in self for time {time}.")

        tree = CGL.newCGNSTree()

        base_names = linked_sample.meshes.get_base_names(time=linked_time)

        for bn in base_names:
            base_node = linked_sample.meshes.get_base(bn, time=linked_time)
            base = [bn, base_node[1], [], "CGNSBase_t"]
            tree[2].append(base)

            family = [
                "Bulk",
                np.array([b"B", b"u", b"l", b"k"], dtype="|S1"),
                [],
                "FamilyName_t",
            ]  # maybe get this from linked_sample as well ?
            base[2].append(family)

            zone_names = linked_sample.meshes.get_zone_names(bn, time=linked_time)
            for zn in zone_names:
                zone_node = linked_sample.meshes.get_zone(
                    zone_name=zn, base_name=bn, time=linked_time
                )
                grid = [
                    zn,
                    zone_node[1],
                    [
                        [
                            "ZoneType",
                            np.array(
                                [
                                    b"U",
                                    b"n",
                                    b"s",
                                    b"t",
                                    b"r",
                                    b"u",
                                    b"c",
                                    b"t",
                                    b"u",
                                    b"r",
                                    b"e",
                                    b"d",
                                ],
                                dtype="|S1",
                            ),
                            [],
                            "ZoneType_t",
                        ]
                    ],
                    "Zone_t",
                ]
                base[2].append(grid)
                zone_family = [
                    "FamilyName",
                    np.array([b"B", b"u", b"l", b"k"], dtype="|S1"),
                    [],
                    "FamilyName_t",
                ]
                grid[2].append(zone_family)

        def find_feature_roots(sample: Sample, time: float, Type_t: str):
            Types_t = CGU.getAllNodesByTypeSet(sample.meshes.get_mesh(time), Type_t)
            # in case the type is not present in the tree
            if Types_t == []:  # pragma: no cover
                return []
            types = [Types_t[0]]
            for t in Types_t[1:]:
                for tt in types:
                    if tt not in t:  # pragma: no cover
                        types.append(t)
            return types

        feature_paths = []
        for feature in ["ZoneBC_t", "Elements_t", "GridCoordinates_t"]:
            feature_paths += find_feature_roots(linked_sample, linked_time, feature)

        self.meshes.add_tree(tree, time=time)

        dname = path_linked_sample.parent
        bname = path_linked_sample.name
        self.meshes._links[time] = [[str(dname), bname, fp, fp] for fp in feature_paths]

        return tree

    def show_tree(self, time: Optional[float] = None) -> None:
        """Display the structure of the CGNS tree for a specified time.

        Args:
            time (float, optional): The time step for which you want to display the CGNS tree structure. Defaults to None. If a specific time is not provided, the method will display the tree structure for the default time step.

        Examples:
            .. code-block:: python

                # To display the CGNS tree structure for the default time step:
                sample.show_tree()

                # To display the CGNS tree structure for a specific time step:
                sample.show_tree(0.5)
        """
        self.meshes.show_tree(time)

    def add_field(
        self,
        name: str,
        field: Field,
        location: str = "Vertex",
        zone_name: Optional[str] = None,
        base_name: Optional[str] = None,
        time: Optional[float] = None,
        warning_overwrite=True,
    ) -> None:
        """Add a field to a specified zone in the grid.

        Args:
            name (str): The name of the field to be added.
            field (Field): The field data to be added.
            zone_name (str, optional): The name of the zone where the field will be added. Defaults to None.
            base_name (str, optional): The name of the base where the zone is located. Defaults to None.
            location (str, optional): The grid location where the field will be stored. Defaults to 'Vertex'.
                Possible values : :py:const:`plaid.constants.CGNS_FIELD_LOCATIONS`
            time (float, optional): The time associated with the field. Defaults to 0.
            warning_overwrite (bool, optional): Show warning if an preexisting field is being overwritten

        Raises:
            KeyError: Raised if the specified zone does not exist in the given base.
        """
        self.meshes.add_field(
            name,
            field,
            location=location,
            zone_name=zone_name,
            base_name=base_name,
            time=time,
            warning_overwrite=warning_overwrite,
        )

    def get_field(
        self,
        name: str,
        location: str = "Vertex",
        zone_name: Optional[str] = None,
        base_name: Optional[str] = None,
        time: Optional[float] = None,
    ) -> Field:
        """Retrieve a field with a specified name from a given zone, base, location, and time.

        Args:
            name (str): The name of the field to retrieve.
            location (str, optional): The location at which to retrieve the field. Defaults to 'Vertex'.
                Possible values : :py:const:`plaid.constants.CGNS_FIELD_LOCATIONS`
            zone_name (str, optional): The name of the zone to search for. Defaults to None.
            base_name (str, optional): The name of the base to search for. Defaults to None.
            time (float, optional): The time value to consider when searching for the field. If a specific time is not provided, the method will display the tree structure for the default time step.

        Returns:
            Field: A set containing the names of the fields that match the specified criteria.
        """
        return self.meshes.get_field(
            name=name,
            location=location,
            zone_name=zone_name,
            base_name=base_name,
            time=time,
        )

    def del_field(
        self,
        name: str,
        location: str = "Vertex",
        zone_name: Optional[str] = None,
        base_name: Optional[str] = None,
        time: Optional[float] = None,
    ) -> CGNSTree:
        """Delete a field from a specified zone in the grid.

        Args:
            name (str): The name of the field to be deleted.
            location (str, optional): The grid location where the field is stored. Defaults to 'Vertex'.
                Possible values : :py:const:`plaid.constants.CGNS_FIELD_LOCATIONS`
            zone_name (str, optional): The name of the zone from which the field will be deleted. Defaults to None.
            base_name (str, optional): The name of the base where the zone is located. Defaults to None.
            time (float, optional): The time associated with the field. Defaults to 0.

        Raises:
            KeyError: Raised if the specified zone or field does not exist in the given base.

        Returns:
            CGNSTree: The tree at the provided time (without the deleted node)
        """
        return self.meshes.del_field(
            name=name,
            location=location,
            zone_name=zone_name,
            base_name=base_name,
            time=time,
        )

    def get_nodes(
        self,
        zone_name: Optional[str] = None,
        base_name: Optional[str] = None,
        time: Optional[float] = None,
    ) -> Optional[np.ndarray]:
        """Get grid node coordinates from a specified base, zone, and time.

        Args:
            zone_name (str, optional): The name of the zone to search for. Defaults to None.
            base_name (str, optional): The name of the base to search for. Defaults to None.
            time (float, optional):  The time value to consider when searching for the zone. If a specific time is not provided, the method will display the tree structure for the default time step.

        Raises:
            TypeError: Raised if multiple <GridCoordinates> nodes are found. Only one is expected.

        Returns:
            Optional[np.ndarray]: A NumPy array containing the grid node coordinates.
            If no matching zone or grid coordinates are found, None is returned.

        Seealso:
            This function can also be called using `get_points()` or `get_vertices()`.
        """
        return self.meshes.get_nodes(zone_name, base_name, time)

    def set_nodes(
        self,
        nodes: np.ndarray,
        zone_name: Optional[str] = None,
        base_name: Optional[str] = None,
        time: Optional[float] = None,
    ) -> None:
        """Set the coordinates of nodes for a specified base and zone at a given time.

        Args:
            nodes (np.ndarray): A numpy array containing the new node coordinates.
            zone_name (str, optional): The name of the zone where the nodes should be updated. Defaults to None.
            base_name (str, optional): The name of the base where the nodes should be updated. Defaults to None.
            time (float, optional): The time at which the node coordinates should be updated. If a specific time is not provided, the method will display the tree structure for the default time step.

        Raises:
            KeyError: Raised if the specified base or zone do not exist. You should first
            create the base and zone using the `Sample.init_zone(zone_name,base_name)` method.

        Seealso:
            This function can also be called using `set_points()` or `set_vertices()`
        """
        self.meshes.set_nodes(nodes, zone_name, base_name, time)

    # -------------------------------------------------------------------------#
    def get_time_series_names(self) -> set[str]:
        """Get the names of time series associated with the object.

        Returns:
            set[str]: A set of strings containing the names of the time series.
        """
        if self.time_series is None:
            return []
        else:
            return list(self.time_series.keys())

    def get_time_series(self, name: str) -> Optional[TimeSeries]:
        """Retrieve a time series by name.

        Args:
            name (str): The name of the time series to retrieve.

        Returns:
            TimeSeries or None: If a time series with the given name exists, it returns the corresponding time series, or None otherwise.

        """
        if (self.time_series is None) or (name not in self.time_series):
            return None
        else:
            return self.time_series[name]

    def add_time_series(
        self, name: str, time_sequence: TimeSequence, values: Field
    ) -> None:
        """Add a time series to the sample.

        Args:
            name (str): A descriptive name for the time series.
            time_sequence (TimeSequence): The time sequence, array of time points.
            values (Field): The values corresponding to the time sequence.

        Example:
            .. code-block:: python

                from plaid import Sample
                sample.add_time_series('stuff', np.arange(2), np.random.randn(2))
                print(sample.get_time_series('stuff'))
                >>> (array([0, 1]), array([-0.59630135, -1.15572306]))

        Raises:
            TypeError: Raised if the length of `time_sequence` is not equal to the length of `values`.
        """
        _check_names([name])
        assert len(time_sequence) == len(values), (
            "time sequence and values do not have the same size"
        )
        if self.time_series is None:
            self.time_series = {name: (time_sequence, values)}
        else:
            self.time_series[name] = (time_sequence, values)

    def del_time_series(self, name: str) -> tuple[TimeSequence, Field]:
        """Delete a time series from the sample.

        Args:
            name (str): The name of the time series to be deleted.

        Raises:
            KeyError: Raised when there is no time series / there is no time series with the provided name.

        Returns:
            tuple[TimeSequence, Field]: A tuple containing the time sequence and values of the deleted time series.
        """
        if self.time_series is None:
            raise KeyError("There is no time series inside this sample.")

        if name not in self.time_series:
            raise KeyError(f"There is no time series with name {name}.")

        return self.time_series.pop(name)

    # -------------------------------------------------------------------------#

    def del_all_fields(
        self,
    ) -> Self:
        """Delete alls field from sample, while keeping geometrical info.

        Returns:
            Sample: The sample with deleted fields
        """
        all_features_identifiers = self.get_all_features_identifiers()
        # Delete all fields in the sample
        for feat_id in all_features_identifiers:
            if feat_id["type"] == "field":
                self.del_field(
                    name=feat_id["name"],
                    location=feat_id["location"],
                    zone_name=feat_id["zone_name"],
                    base_name=feat_id["base_name"],
                    time=feat_id["time"],
                )
        return self

    # -------------------------------------------------------------------------#
    def get_all_features_identifiers(
        self,
    ) -> list[FeatureIdentifier]:
        """Get all features identifiers from the sample.

        Returns:
            list[FeatureIdentifier]: A list of dictionaries containing the identifiers of all features in the sample.
        """
        all_features_identifiers = []
        for sn in self.get_scalar_names():
            all_features_identifiers.append({"type": "scalar", "name": sn})
        for tsn in self.get_time_series_names():
            all_features_identifiers.append({"type": "time_series", "name": tsn})
        for t in self.meshes.get_all_mesh_times():
            for bn in self.meshes.get_base_names(time=t):
                for zn in self.meshes.get_zone_names(base_name=bn, time=t):
                    if (
                        self.meshes.get_nodes(base_name=bn, zone_name=zn, time=t)
                        is not None
                    ):
                        all_features_identifiers.append(
                            {
                                "type": "nodes",
                                "base_name": bn,
                                "zone_name": zn,
                                "time": t,
                            }
                        )
                    for loc in CGNS_FIELD_LOCATIONS:
                        for fn in self.meshes.get_field_names(
                            location=loc, zone_name=zn, base_name=bn, time=t
                        ):
                            all_features_identifiers.append(
                                {
                                    "type": "field",
                                    "name": fn,
                                    "base_name": bn,
                                    "zone_name": zn,
                                    "location": loc,
                                    "time": t,
                                }
                            )
        return all_features_identifiers

    def get_all_features_identifiers_by_type(
        self, feature_type: str
    ) -> list[FeatureIdentifier]:
        """Get all features identifiers of a given type from the sample.

        Args:
            feature_type (str): Type of features to return

        Returns:
            list[FeatureIdentifier]: A list of dictionaries containing the identifiers of a given type of all features in the sample.
        """
        assert feature_type in AUTHORIZED_FEATURE_TYPES, "feature_type not known"
        all_features_identifiers = self.get_all_features_identifiers()
        return [
            feat_id
            for feat_id in all_features_identifiers
            if feat_id["type"] == feature_type
        ]

    def get_feature_from_string_identifier(
        self, feature_string_identifier: str
    ) -> Feature:
        """Retrieve a specific feature from its encoded string identifier.

        The `feature_string_identifier` must follow the format:
            "<feature_type>::<detail1>/<detail2>/.../<detailN>"

        Supported feature types:
            - "scalar": expects 1 detail → `scalars.get(name)`
            - "time_series": expects 1 detail → `get_time_series(name)`
            - "field": up to 5 details → `get_field(name, base_name, zone_name, location, time)`
            - "nodes": up to 3 details → `get_nodes(base_name, zone_name, time)`

        Args:
            feature_string_identifier (str): Structured identifier of the feature.

        Returns:
            Feature: The retrieved feature object.

        Raises:
            AssertionError: If `feature_type` is unknown.

        Warnings:
            - If "time" is present in a field/nodes identifier, it is cast to float.
            - `name` is required for scalar, time_series and field features.
            - The order of the details must be respected. One cannot specify a detail in the feature_string_identifier string without specified the previous ones.
        """
        splitted_identifier = feature_string_identifier.split("::")

        feature_type = splitted_identifier[0]
        feature_details = [detail for detail in splitted_identifier[1].split("/")]

        assert feature_type in AUTHORIZED_FEATURE_TYPES, "feature_type not known"

        arg_names = AUTHORIZED_FEATURE_INFOS[feature_type]
        assert len(arg_names) >= len(feature_details), "Too much details provided"

        if feature_type == "scalar":
            val = self.get_scalar(feature_details[0])
            if val is None:
                raise KeyError(
                    f"Unknown scalar {feature_details[0]}"
                )  # pragma: no cover
            return val
        elif feature_type == "time_series":
            return self.get_time_series(feature_details[0])
        elif feature_type == "field":
            kwargs = {arg_names[i]: detail for i, detail in enumerate(feature_details)}
            for k in kwargs:
                if kwargs[k] == "":
                    kwargs[k] = None
            if "time" in kwargs:
                kwargs["time"] = float(kwargs["time"])
            return self.get_field(**kwargs)
        elif feature_type == "nodes":
            kwargs = {arg_names[i]: detail for i, detail in enumerate(feature_details)}
            for k in kwargs:
                if kwargs[k] == "":
                    kwargs[k] = None
            if "time" in kwargs:
                kwargs["time"] = float(kwargs["time"])
            return self.get_nodes(**kwargs).flatten()

    def get_feature_from_identifier(
        self, feature_identifier: FeatureIdentifier
    ) -> Feature:
        """Retrieve a feature object based on a structured identifier dictionary.

        The `feature_identifier` must include a `"type"` key specifying the feature kind:
            - `"scalar"`       → calls `scalars.get(name)`
            - `"time_series"`  → calls `get_time_series(name)`
            - `"field"`        → calls `get_field(name, base_name, zone_name, location, time)`
            - `"nodes"`        → calls `get_nodes(base_name, zone_name, time)`

        Required keys:
            - `"type"`: one of `"scalar"`, `"time_series"`, `"field"`, or `"nodes"`
            - `"name"`: required for all types except `"nodes"`

        Optional keys depending on type:
            - `"base_name"`, `"zone_name"`, `"location"`, `"time"`: used in `"field"` and `"nodes"`

        Any omitted optional keys will rely on the default values mechanics of the class.

        Args:
            feature_identifier ( dict[str:Union[str, float]]):
                A dictionary encoding the feature type and its relevant parameters.

        Returns:
            Feature: The corresponding feature instance retrieved via the appropriate accessor.
        """
        feature_type, feature_details = get_feature_type_and_details_from(
            feature_identifier
        )

        if feature_type == "scalar":
            return self.get_scalar(**feature_details)
        elif feature_type == "time_series":
            return self.get_time_series(**feature_details)
        elif feature_type == "field":
            return self.get_field(**feature_details)
        elif feature_type == "nodes":
            return self.get_nodes(**feature_details).flatten()

    def get_features_from_identifiers(
        self, feature_identifiers: list[FeatureIdentifier]
    ) -> list[Feature]:
        """Retrieve features based on a list of structured identifier dictionaries.

        Elements of `feature_identifiers` must include a `"type"` key specifying the feature kind:
            - `"scalar"`       → calls `scalars.get(name)`
            - `"time_series"`  → calls `get_time_series(name)`
            - `"field"`        → calls `get_field(name, base_name, zone_name, location, time)`
            - `"nodes"`        → calls `get_nodes(base_name, zone_name, time)`

        Required keys:
            - `"type"`: one of `"scalar"`, `"time_series"`, `"field"`, or `"nodes"`
            - `"name"`: required for all types except `"nodes"`

        Optional keys depending on type:
            - `"base_name"`, `"zone_name"`, `"location"`, `"time"`: used in `"field"` and `"nodes"`

        Any omitted optional keys will rely on the default values mechanics of the class.

        Args:
            feature_identifiers (list[FeatureIdentifier]):
                A dictionary encoding the feature type and its relevant parameters.

        Returns:
            list[Feature]: List of corresponding feature instance retrieved via the appropriate accessor.
        """
        all_features_info = [
            get_feature_type_and_details_from(feat_id)
            for feat_id in feature_identifiers
        ]

        features = []
        for feature_type, feature_details in all_features_info:
            if feature_type == "scalar":
                features.append(self.get_scalar(**feature_details))
            elif feature_type == "time_series":
                features.append(self.get_time_series(**feature_details))
            elif feature_type == "field":
                features.append(self.get_field(**feature_details))
            elif feature_type == "nodes":
                features.append(self.get_nodes(**feature_details).flatten())
        return features

    def _add_feature(
        self,
        feature_identifier: FeatureIdentifier,
        feature: Feature,
    ) -> Self:
        """Add a feature to current sample.

        This method applies updates to scalars, time series, fields, or nodes
        using feature identifiers, and corresponding feature data.

        Args:
            feature_identifier (dict): A feature identifier.
            feature (Feature): A feature corresponding to the identifiers.

        Returns:
            Self: The updated sample

        Raises:
            AssertionError: If types are inconsistent or identifiers contain unexpected keys.
        """
        feature_type, feature_details = get_feature_type_and_details_from(
            feature_identifier
        )

        if feature_type == "scalar":
            if safe_len(feature) == 1:
                feature = feature[0]
            self.add_scalar(**feature_details, value=feature)
        elif feature_type == "time_series":
            self.add_time_series(
                **feature_details, time_sequence=feature[0], values=feature[1]
            )
        elif feature_type == "field":
            self.add_field(**feature_details, field=feature, warning_overwrite=False)
        elif feature_type == "nodes":
            physical_dim_arg = {
                k: v for k, v in feature_details.items() if k in ["base_name", "time"]
            }
            phys_dim = self.meshes.get_physical_dim(**physical_dim_arg)
            self.set_nodes(**feature_details, nodes=feature.reshape((-1, phys_dim)))

        return self

    def update_features_from_identifier(
        self,
        feature_identifiers: Union[FeatureIdentifier, list[FeatureIdentifier]],
        features: Union[Feature, list[Feature]],
        in_place: bool = False,
    ) -> Self:
        """Update one or several features of the sample by their identifier(s).

        This method applies updates to scalars, time series, fields, or nodes
        using feature identifiers, and corresponding feature data. When `in_place=False`, a deep copy of the sample is created
        before applying updates, ensuring full isolation from the original.

        Args:
            feature_identifiers (FeatureIdentifier or list of FeatureIdentifier): One or more feature identifiers.
            features (Feature or list of Feature): One or more features corresponding
                to the identifiers.
            in_place (bool, optional): If True, modifies the current sample in place.
                If False, returns a deep copy with updated features.

        Returns:
            Self: The updated sample (either the current instance or a new copy).

        Raises:
            AssertionError: If types are inconsistent or identifiers contain unexpected keys.
        """
        if not isinstance(feature_identifiers, list):
            feature_identifiers = [feature_identifiers]
            features = [features]
        assert len(feature_identifiers) == len(features)
        for i_id, feat_id in enumerate(feature_identifiers):
            feature_identifiers[i_id] = FeatureIdentifier(feat_id)

        sample = self if in_place else self.copy()

        for feat_id, feat in zip(feature_identifiers, features):
            sample._add_feature(feat_id, feat)

        return sample

    def extract_sample_from_identifier(
        self,
        feature_identifiers: Union[FeatureIdentifier, list[FeatureIdentifier]],
    ) -> Self:
        """Extract features of the sample by their identifier(s) and return a new sample containing these features.

        This method applies updates to scalars, time series, fields, or nodes
        using feature identifiers

        Args:
            feature_identifiers (dict or list of dict): One or more feature identifiers.

        Returns:
            Self: New sample containing the provided feature identifiers

        Raises:
            AssertionError: If types are inconsistent or identifiers contain unexpected keys.
        """
        assert isinstance(feature_identifiers, dict) or isinstance(
            feature_identifiers, list
        ), "Check types of feature_identifiers argument"
        if isinstance(feature_identifiers, dict):
            feature_identifiers = [feature_identifiers]

        feature_types = set([feat_id["type"] for feat_id in feature_identifiers])

        # if field or node features are to extract, copy the source sample and delete all fields
        if "field" in feature_types or "nodes" in feature_types:
            source_sample = self.copy()
            source_sample.del_all_fields()

        sample = Sample()

        for feat_id in feature_identifiers:
            feature = self.get_feature_from_identifier(feat_id)

            if feature is not None:
                # if trying to add a field or nodes, must check if the corresponding tree exists, and add it if not
                if feat_id["type"] in ["field", "nodes"]:
                    # get time of current feature
                    time = self.meshes.get_time_assignment(time=feat_id.get("time"))

                    # if the constructed sample does not have a tree, add the one from the source sample, with no field
                    if not sample.meshes.get_mesh(time):
                        sample.meshes.add_tree(source_sample.meshes.get_mesh(time))

                sample._add_feature(feat_id, feature)

        sample._extra_data = copy.deepcopy(self._extra_data)

        return sample

    @deprecated(
        "Use extract_sample_from_identifier() instead",
        version="0.1.8",
        removal="0.2",
    )
    def from_features_identifier(
        self,
        feature_identifiers: Union[FeatureIdentifier, list[FeatureIdentifier]],
    ) -> Self:
        """DEPRECATED: Use extract_sample_from_identifier() instead."""
        return self.extract_sample_from_identifier(
            feature_identifiers
        )  # pragma: no cover

    def merge_features(self, sample: Self, in_place: bool = False) -> Self:
        """Merge features from another sample into the current sample.

        This method applies updates to scalars, time series, fields, or nodes
        using features from another sample. When `in_place=False`, a deep copy of the sample is created
        before applying updates, ensuring full isolation from the original.

        Args:
            sample (Sample): The sample from which features will be merged.
            in_place (bool, optional): If True, modifies the current sample in place.
                If False, returns a deep copy with updated features.

        Returns:
            Self: The updated sample (either the current instance or a new copy).
        """
        merged_dataset = self if in_place else self.copy()

        all_features_identifiers = sample.get_all_features_identifiers()
        all_features = sample.get_features_from_identifiers(all_features_identifiers)

        feature_types = set([feat_id["type"] for feat_id in all_features_identifiers])

        # if field or node features are to extract, copy the source sample and delete all fields
        if "field" in feature_types or "nodes" in feature_types:
            source_sample = sample.copy()
            source_sample.del_all_fields()

        for feat_id in all_features_identifiers:
            # if trying to add a field or nodes, must check if the corresponding tree exists, and add it if not
            if feat_id["type"] in ["field", "nodes"]:
                # get time of current feature
                time = sample.meshes.get_time_assignment(time=feat_id.get("time"))

                # if the constructed sample does not have a tree, add the one from the source sample, with no field
                if not merged_dataset.meshes.get_mesh(time):
                    merged_dataset.meshes.add_tree(source_sample.get_mesh(time))

        return merged_dataset.update_features_from_identifier(
            feature_identifiers=all_features_identifiers,
            features=all_features,
            in_place=in_place,
        )

    # -------------------------------------------------------------------------#
    def save(self, path: Union[str, Path], overwrite: bool = False) -> None:
        """Save the Sample in directory `path`.

        Args:
            path (Union[str,Path]): relative or absolute directory path.
            overwrite (bool): target directory overwritten if True.
        """
        path = Path(path)

        if path.is_dir():
            if overwrite:
                shutil.rmtree(path)
                logger.warning(f"Existing {path} directory has been reset.")
            elif len(list(path.glob("*"))):
                raise ValueError(
                    f"directory {path} already exists and is not empty. Set `overwrite` to True if needed."
                )

        path.mkdir(exist_ok=True)

        mesh_dir = path / "meshes"

        if self.meshes.data:
            mesh_dir.mkdir()
            for i, time in enumerate(self.meshes.data.keys()):
                outfname = mesh_dir / f"mesh_{i:09d}.cgns"
                status = CGM.save(
                    str(outfname),
                    self.meshes.data[time],
                    links=self.meshes._links.get(time),
                )
                logger.debug(f"save -> {status=}")

        scalars_names = self.get_scalar_names()
        if len(scalars_names) > 0:
            scalars = []
            for s_name in scalars_names:
                scalars.append(self.get_scalar(s_name))
            scalars = np.array(scalars).reshape((1, -1))
            header = ",".join(scalars_names)
            np.savetxt(
                path / "scalars.csv",
                scalars,
                header=header,
                delimiter=",",
                comments="",
            )

        time_series_names = self.get_time_series_names()
        if len(time_series_names) > 0:
            for ts_name in time_series_names:
                ts = self.get_time_series(ts_name)
                data = np.vstack((ts[0], ts[1])).T
                header = ",".join(["t", ts_name])
                np.savetxt(
                    path / f"time_series_{ts_name}.csv",
                    data,
                    header=header,
                    delimiter=",",
                    comments="",
                )

    @classmethod
    def load_from_dir(cls, path: Union[str, Path]) -> Self:
        """Load the Sample from directory `path`.

        This is a class method, you don't need to instantiate a `Sample` first.

        Args:
            path (Union[str,Path]): Relative or absolute directory path.

        Returns:
            Sample

        Example:
            .. code-block:: python

                from plaid import Sample
                sample = Sample.load_from_dir(dir_path)
                print(sample)
                >>> Sample(2 scalars, 1 timestamp, 5 fields)

        Note:
            It calls 'load' function during execution.
        """
        path = Path(path)
        instance = cls()
        instance.load(path)
        return instance

    def load(self, path: Union[str, Path]) -> None:
        """Load the Sample from directory `path`.

        Args:
            path (Union[str,Path]): Relative or absolute directory path.

        Raises:
            FileNotFoundError: Triggered if the provided directory does not exist.
            FileExistsError: Triggered if the provided path is a file instead of a directory.

        Example:
            .. code-block:: python

                from plaid import Sample
                sample = Sample()
                sample.load(path)
                print(sample)
                >>> Sample(3 scalars, 1 timestamp, 3 fields)

        """
        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(f'Directory "{path}" does not exist. Abort')

        if not path.is_dir():
            raise FileExistsError(f'"{path}" is not a directory. Abort')

        meshes_dir = path / "meshes"
        if meshes_dir.is_dir():
            meshes_names = list(meshes_dir.glob("*"))
            nb_meshes = len(meshes_names)
            # self.meshes = {}
            self.meshes._links = {}
            self.meshes._paths = {}
            for i in range(nb_meshes):
                tree, links, paths = CGM.load(str(meshes_dir / f"mesh_{i:09d}.cgns"))
                time = CGH.get_time_values(tree)

                (
                    self.meshes.data[time],
                    self.meshes._links[time],
                    self.meshes._paths[time],
                ) = (
                    tree,
                    links,
                    paths,
                )
                for i in range(len(self.meshes._links[time])):  # pragma: no cover
                    self.meshes._links[time][i][0] = str(
                        meshes_dir / self.meshes._links[time][i][0]
                    )

        scalars_fname = path / "scalars.csv"
        if scalars_fname.is_file():
            names = np.loadtxt(
                scalars_fname, dtype=str, max_rows=1, delimiter=","
            ).reshape((-1,))
            scalars = np.loadtxt(
                scalars_fname, dtype=float, skiprows=1, delimiter=","
            ).reshape((-1,))
            for name, value in zip(names, scalars):
                self.add_scalar(name, value)

        time_series_files = list(path.glob("time_series_*.csv"))
        for ts_fname in time_series_files:
            names = np.loadtxt(ts_fname, dtype=str, max_rows=1, delimiter=",").reshape(
                (-1,)
            )
            assert names[0] == "t"
            times_and_val = np.loadtxt(ts_fname, dtype=float, skiprows=1, delimiter=",")
            self.add_time_series(names[1], times_and_val[:, 0], times_and_val[:, 1])

    # # -------------------------------------------------------------------------#
    def __str__(self) -> str:
        """Return a string representation of the sample.

        Returns:
            str: A string representation of the overview of sample content.
        """
        # TODO rewrite using self.get_all_features_identifiers()
        str_repr = "Sample("

        # scalars
        nb_scalars = len(self.get_scalar_names())
        str_repr += f"{nb_scalars} scalar{'' if nb_scalars == 1 else 's'}, "

        # time series
        nb_ts = len(self.get_time_series_names())
        str_repr += f"{nb_ts} time series, "

        # fields
        times = self.meshes.get_all_mesh_times()
        nb_timestamps = len(times)
        str_repr += f"{nb_timestamps} timestamp{'' if nb_timestamps == 1 else 's'}, "

        field_names = set()
        for time in times:
            ## Need to include all possible location within the count
            base_names = self.meshes.get_base_names(time=time)
            for bn in base_names:
                zone_names = self.meshes.get_zone_names(base_name=bn)
                for zn in zone_names:
                    for location in CGNS_FIELD_LOCATIONS:
                        field_names = field_names.union(
                            self.meshes.get_field_names(
                                location=location, zone_name=zn, base_name=bn, time=time
                            )
                        )
        nb_fields = len(field_names)
        str_repr += f"{nb_fields} field{'' if nb_fields == 1 else 's'}, "

        # CGNS tree
        if not self.meshes.data:
            str_repr += "no tree, "
        else:
            # TODO
            pass

        if str_repr[-2:] == ", ":
            str_repr = str_repr[:-2]
        str_repr = str_repr + ")"

        return str_repr

    def summarize(self) -> str:
        """Provide detailed summary of the Sample content, showing feature names and mesh information.

        This provides more detailed information than the __repr__ method,
        including the name of each feature.

        Returns:
            str: A detailed string representation of the sample content.

        Example:
            .. code-block:: bash

                Sample Summary:
                ==================================================
                Scalars (8):
                - Pr: 0.9729006564945664
                - Q: 0.2671142611487964
                - Tr: 0.9983394202616822
                - angle_in: 45.5066666666667
                - angle_out: 61.89519547386746
                - eth_is: 0.21238326882538008
                - mach_out: 0.81003
                - power: 0.0019118127462776008

                Meshes (1 timestamps):
                Time: 0.0
                    Base: Base_2_2
                        Nodes (36421)
                        Tags (6): Intrado (122), Extrado (122), Inflow (121), Outflow (121), Periodic_1 (120), Periodic_2 (238)
                        Fields (7): ro, sdf, rou, nut, mach, roe, rov
                        Elements (36000)
                        QUAD_4 (36000)
                    Base: Base_1_2
                        Nodes (244)
                        Fields (1): M_iso
                        Elements (242)
                        BAR_2 (242)
        """
        summary = "Sample Summary:\n"
        summary += "=" * 50 + "\n"

        # Scalars with names
        scalar_names = self.get_scalar_names()
        if scalar_names:
            summary += f"Scalars ({len(scalar_names)}):\n"
            for name in scalar_names:
                value = self.get_scalar(name)
                summary += f"  - {name}: {value}\n"
            summary += "\n"

        # Time series with names
        ts_names = self.get_time_series_names()
        if ts_names:
            summary += f"Time Series ({len(ts_names)}):\n"
            for name in ts_names:
                ts = self.get_time_series(name)
                if ts is not None:
                    summary += f"  - {name}: {len(ts[0])} time points\n"
            summary += "\n"

        # Mesh information
        times = self.meshes.get_all_mesh_times()
        summary += f"Meshes ({len(times)} timestamps):\n"
        if times:
            for time in times:
                summary += f"    Time: {time}\n"
                base_names = self.meshes.get_base_names(time=time)
                for base_name in base_names:
                    summary += f"        Base: {base_name}\n"
                    zone_names = self.meshes.get_zone_names(
                        base_name=base_name, time=time
                    )
                    for zone_name in zone_names:
                        summary += f"            Zone: {zone_name}\n"
                        # Nodes, nodal tags and fields at verticies
                        nodes = self.get_nodes(
                            zone_name=zone_name, base_name=base_name, time=time
                        )
                        if nodes is not None:
                            nb_nodes = nodes.shape[0]
                            nodal_tags = self.meshes.get_nodal_tags(
                                zone_name=zone_name, base_name=base_name, time=time
                            )
                            summary += f"                Nodes ({nb_nodes})\n"
                            if len(nodal_tags) > 0:
                                summary += f"                Tags ({len(nodal_tags)}): {', '.join([f'{k} ({len(v)})' for k, v in nodal_tags.items()])}\n"

                        for location in CGNS_FIELD_LOCATIONS:
                            field_names = self.get_field_names(
                                location=location,
                                zone_name=zone_name,
                                base_name=base_name,
                                time=time,
                            )
                            if field_names:
                                summary += f"                Location: {location}\n                    Fields ({len(field_names)}): {', '.join(field_names)}\n"

                        # Elements and fields at elements
                        elements = self.meshes.get_elements(
                            zone_name=zone_name, base_name=base_name, time=time
                        )
                        summary += f"                Elements ({sum([v.shape[0] for v in elements.values()])})\n"
                        if len(elements) > 0:
                            summary += f"                    {', '.join([f'{k} ({v.shape[0]})' for k, v in elements.items()])}\n"

        return summary

    def check_completeness(self) -> str:
        """Check the completeness of features in this sample.

        Returns:
            str: A report on feature completeness.

        Example:
            .. code-block:: bash

                Sample Completeness Check:
                ==============================
                Has scalars: True
                Has time series: False
                Has meshes: True
                Total unique fields: 8
                Field names: M_iso, mach, nut, ro, roe, rou, rov, sdf
        """
        report = "Sample Completeness Check:\n"
        report += "=" * 30 + "\n"

        # Check if sample has basic features
        has_scalars = len(self.get_scalar_names()) > 0
        has_time_series = len(self.get_time_series_names()) > 0
        has_meshes = len(self.meshes.get_all_mesh_times()) > 0

        report += f"Has scalars: {has_scalars}\n"
        report += f"Has time series: {has_time_series}\n"
        report += f"Has meshes: {has_meshes}\n"

        if has_meshes:
            times = self.meshes.get_all_mesh_times()
            total_fields = set()
            for time in times:
                base_names = self.meshes.get_base_names(time=time)
                for base_name in base_names:
                    zone_names = self.meshes.get_zone_names(
                        base_name=base_name, time=time
                    )
                    for zone_name in zone_names:
                        for location in CGNS_FIELD_LOCATIONS:
                            field_names = self.get_field_names(
                                location=location,
                                zone_name=zone_name,
                                base_name=base_name,
                                time=time,
                            )
                            total_fields.update(field_names)

            report += f"Total unique fields: {len(total_fields)}\n"
            if total_fields:
                report += f"Field names: {', '.join(sorted(total_fields))}\n"

        return report
