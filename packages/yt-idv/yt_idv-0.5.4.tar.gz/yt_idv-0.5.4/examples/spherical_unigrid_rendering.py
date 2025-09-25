import argparse

import numpy as np
import yt

import yt_idv

# yt reminder: phi is the azimuthal angle (0 to 2pi)
# theta is the co-latitude, the angle from north (0 to pi)
# coord ordering here will be r, phi, theta
bbox_options = {
    "partial": np.array([[0.5, 1.0], [0.0, np.pi / 3], [np.pi / 4, np.pi / 2]]),
    "whole": np.array([[0.0, 1.0], [0.0, 2 * np.pi], [0, np.pi]]),
    "shell": np.array([[0.7, 1.0], [0.0, 2 * np.pi], [0, np.pi]]),
    "north_hemi": np.array([[0.1, 1.0], [0.0, 2 * np.pi], [0, 0.5 * np.pi]]),
    "north_shell": np.array([[0.8, 1.0], [0.0, 2 * np.pi], [0, 0.5 * np.pi]]),
    "south_hemi": np.array([[0.1, 1.0], [0.0, 2 * np.pi], [0.5 * np.pi, np.pi]]),
    "ew_hemi": np.array([[0.1, 1.0], [0.0, np.pi], [0.0, np.pi]]),
    "quadrant_shell": np.array([[0.6, 1.0], [0.0, np.pi / 2], [0.0, np.pi / 2]]),
}

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="spherical_amr_rendering",
        description="Loads an example spherical dataset in yt_idv",
    )

    msg = f"The geometry subset to generate: one of {list(bbox_options.keys())}"
    parser.add_argument("-d", "--domain", default="partial", help=msg)
    msg = (
        "The field to plot. Provide a comma-separated string with field_type,field "
        "e.g., to plot the field tuple ('index', 'phi'): \n "
        "    $ python amr_spherical_volume_rendering.py -f index,x "
        "\nIf a single string is provided, a field type of gas is assumed."
    )
    parser.add_argument("-f", "--field", default="index,phi", help=msg)
    parser.add_argument(
        "-np", "--nprocs", default=64, help="number of grids to decompose domain to"
    )
    parser.add_argument(
        "-sz", "--size", default=256, help="dimensions, will be (size, size size)"
    )

    args = parser.parse_args()

    sz = (int(args.size),) * 3
    fake_data = {"density": np.random.random(sz)}

    field = str(args.field).split(",")
    if len(field) == 1:
        field = ("gas", str(field).strip())
    elif len(field) == 2:
        field = (field[0].strip(), field[1].strip())
    else:
        raise RuntimeError(
            "Unexpected field formatting. Provide a single string"
            " to provide just a field (will assume field type "
            " of 'gas', or a comma separated string to provide a "
            "field type and a field"
        )

    if args.domain not in bbox_options:
        raise RuntimeError(
            f"domain must be one of {list(bbox_options.keys())}, found {args.domain}"
        )
    bbox = bbox_options[args.domain]

    nprocs = int(args.nprocs)

    ds = yt.load_uniform_grid(
        fake_data,
        sz,
        bbox=bbox,
        nprocs=nprocs,
        geometry="spherical",
        axis_order=("r", "phi", "theta"),
        length_unit=1,
    )

    phi_c = ds.quan(ds.domain_center[ds.coordinates.axis_id["phi"]].d, "")
    theta_c = ds.quan(ds.domain_center[ds.coordinates.axis_id["theta"]].d, "")
    rmax = ds.domain_right_edge[ds.coordinates.axis_id["r"]]
    phi_f = ds.quan(15.0 * np.pi / 180.0, "")
    theta_f = ds.quan(15.0 * np.pi / 180.0, "")
    min_val = ds.quan(0.1, "")

    def _tube(field, data):
        phi = data["index", "phi"]
        theta = data["index", "theta"]
        tube = (1 - min_val) * np.exp(-(((theta - theta_c) / theta_f) ** 2))
        tube = tube * np.exp(-(((phi - phi_c) / phi_f) ** 2))
        return tube + min_val

    ds.add_field(
        name=("stream", "tube"),
        function=_tube,
        sampling_type="local",
    )

    def _r_rev(field, data):
        r = data["index", "r"]
        return rmax - r

    ds.add_field(
        name=("stream", "r_rev"),
        function=_r_rev,
        sampling_type="local",
    )

    if field not in ds.field_list + ds.derived_field_list:
        spaces = " " * 8
        fld_list_str = f"\n{spaces}".join(str(fld) for fld in ds.field_list)
        drv_fld_list_str = f"\n{spaces}".join(str(fld) for fld in ds.derived_field_list)
        raise RuntimeError(
            f"field {field} not in field_list or derived_field_list:\n"
            f"\n    ds.field_list:\n{spaces}{fld_list_str}"
            f"\n    ds.derived_field_list:\n{spaces}{drv_fld_list_str}"
        )

    rc = yt_idv.render_context(height=800, width=800, gui=True)
    sg = rc.add_scene(ds, field, no_ghost=True)
    rc.scene.components[0].sample_factor = 5.0
    rc.scene.components[0].cmap_log = False
    rc.scene.components[0]._reset_cmap_bounds()

    rc.run()
