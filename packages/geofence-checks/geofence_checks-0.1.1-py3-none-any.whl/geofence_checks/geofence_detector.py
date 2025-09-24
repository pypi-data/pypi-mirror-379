import pandas as pd
import h3
import numpy as np
from typing import Optional, Tuple
from shapely.geometry import Polygon
import json


def detect_geofence_check_events(
        trucks_df: pd.DataFrame,
        geofences_df: pd.DataFrame,
        already_inside: Optional[pd.DataFrame] = None,
        h3_res: int = 13
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Detects geofence entry and exit events for trucks using pandas DataFrames.

    Args:
        trucks_df: DataFrame with columns ['truck_no', 'latitude', 'longitude', 'timestamp']
        geofences_df: DataFrame with columns ['geofence_name', 'geofence_coordinates', 'dept_code', 'plant_code', 'geofence_type']
        already_inside: Optional DataFrame with previous inside states (columns: ['truck_no', 'geofence_name', 'dept_code', 'first_inside_fence', '_id'])
        h3_res: H3 resolution level.

    Returns:
        newly_entered_df: DataFrame of new entry/exit events.
        already_inside_updated_df: DataFrame of updated events from previous inside states with changes.
    """
    if trucks_df.empty or geofences_df.empty:
        return pd.DataFrame(), pd.DataFrame()

    df = trucks_df.copy()
    df["h3_cell"] = df.apply(
        lambda r: h3.geo_to_h3(r["latitude"], r["longitude"], h3_res), axis=1
    )

    # Prepare fence H3 cells
    fence_h3_map = {}
    for _, g in geofences_df.iterrows():
        coords = g["geofence_coordinates"]
        if isinstance(coords, Polygon):
            coordinates = [[(x, y) for x, y in coords.exterior.coords[:-1]]]
        elif isinstance(coords, dict) and coords.get("type") == "Polygon":
            coordinates = coords["coordinates"]
        elif isinstance(coords, str):
            parsed_coords = json.loads(coords)
            if isinstance(parsed_coords, list) and len(parsed_coords) > 0 and isinstance(parsed_coords[0], dict):
                coordinates = [[(p["lng"], p["lat"]) for p in parsed_coords]]
            else:
                coordinates = parsed_coords.get("coordinates", [])
        else:
            raise ValueError(f"Unsupported geofence_coordinates type: {type(coords)}")

        dept_code = (
            g["dept_code"][0]["value"] if isinstance(g.get("dept_code"), list) else g.get("dept_code", "SNDG")
        )
        key = (g["geofence_name"], dept_code)
        fence_h3_map[key] = {
            "cells": set(h3.polyfill({"type": "Polygon", "coordinates": coordinates}, h3_res)),
            "plant_code": g.get("plant_code", ""),
            "dept_code": dept_code,
            "location_type": g.get("geofence_type", {}).get("label", "")
        }

    # Prepare already_inside map if given
    already_inside_map = {}
    already_inside_ids = {}
    if already_inside is not None and not already_inside.empty:
        for _, a in already_inside.iterrows():
            dept = a.get("dept_code", "SNDG")
            key = (a["truck_no"], a["geofence_name"], dept)
            already_inside_map[key] = pd.to_datetime(a["first_inside_fence"])
            already_inside_ids[key] = a.get("_id")

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values(["truck_no", "timestamp"]).reset_index(drop=True)

    newly_entered = []
    already_inside_updated = []

    def add_result(truck, fence, meta, entry, exit_, exited, is_already=False, _id=None):
        entry = pd.to_datetime(entry)
        exit_ = pd.to_datetime(exit_) if exit_ is not None and pd.notna(exit_) else pd.NaT
        duration = (exit_ - entry).total_seconds() if pd.notna(exit_) and pd.notna(entry) else None
        record = {
            "truck_no": truck,
            "geofence_name": fence,
            "plant_code": meta["plant_code"],
            "dept_code": meta["dept_code"],
            "location_type": meta["location_type"],
            "first_inside_fence": entry,
            "first_outside_fence": exit_,
            "exited": exited,
            "geofence_duration": duration,
        }
        if is_already:
            if _id is not None:
                record["_id"] = _id
            already_inside_updated.append(record)
        else:
            newly_entered.append(record)

    # Process each truck
    for truck_no, tdf in df.groupby("truck_no"):
        h3_cells = tdf["h3_cell"].values
        timestamps = tdf["timestamp"].values

        for (fence_name, dept_code), meta in fence_h3_map.items():
            fence_cells = meta["cells"]
            inside = np.isin(h3_cells, list(fence_cells))
            key = (truck_no, fence_name, dept_code)

            if not inside.any():
                if key in already_inside_map:
                    entry_time = already_inside_map.pop(key)
                    exit_time = timestamps[0]
                    if exit_time > entry_time:
                        add_result(truck_no, fence_name, meta, entry_time, exit_time, True,
                                   is_already=True, _id=already_inside_ids.get(key))
                continue

            changes = np.diff(inside.astype(int))
            entry_idx = np.where(changes == 1)[0] + 1
            exit_idx = np.where(changes == -1)[0] + 1

            if key in already_inside_map:
                entry_time = already_inside_map.pop(key)
                _id = already_inside_ids.get(key)
                if exit_idx.size > 0:
                    first_exit_idx = exit_idx[0]
                    add_result(truck_no, fence_name, meta, entry_time, timestamps[first_exit_idx], True,
                               is_already=True, _id=_id)
                    exit_idx = exit_idx[1:]

            if inside[0]:
                entry_idx = np.insert(entry_idx, 0, 0)
            if inside[-1]:
                if exit_idx.size < entry_idx.size:
                    exit_idx = np.append(exit_idx, len(timestamps))

            for e_idx, x_idx in zip(entry_idx, exit_idx):
                entry_time = timestamps[e_idx]
                exit_time = timestamps[x_idx] if x_idx < len(timestamps) else pd.NaT
                add_result(truck_no, fence_name, meta, entry_time, exit_time, pd.notna(exit_time))

    return pd.DataFrame(newly_entered), pd.DataFrame(already_inside_updated)
