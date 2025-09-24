import pandas as pd
import numpy as np
import time
import pyarrow as pa


def build_df_arc(df_block_model: pd.DataFrame, block_size: float):
    df_y = df_block_model.copy()
    df_arc = pd.DataFrame({"start": [], "end": []})
    df_surface = pd.DataFrame(
        {
            "id": [np.nan],
            "x": [np.nan],
            "y": [np.nan],
            "z": [np.nan],
            "value": [np.nan],
        }
    )
    for i in sorted(set(df_y["x"].to_list())):
        for j in sorted(set(df_y["y"].to_list())):
            df_group = df_y[(df_y["x"] == i) & (df_y["y"] == j)]
            z_max = df_group["z"].max()
            df_group = df_y[
                (df_y["x"] == i) & (df_y["y"] == j) & (df_y["z"] == z_max)
            ].reset_index()
            nueva_fila = pd.DataFrame(
                {
                    "id": [df_group.loc[0]["id"]],
                    "x": [df_group.loc[0]["x"]],
                    "y": [df_group.loc[0]["y"]],
                    "z": [df_group.loc[0]["z"]],
                    "value": [df_group.loc[0]["value"]],
                }
            )
            print("nueva_fila para df_surface surface")
            print(nueva_fila)
            df_surface = pd.concat([df_surface, nueva_fila], ignore_index=True)

    no_cone = pd.DataFrame(
        {
            "id": [np.nan],
            "x": [np.nan],
            "y": [np.nan],
            "z": [np.nan],
            "value": [np.nan],
        }
    )
    for i in sorted(set(df_y["z"].to_list()), reverse=True):
        counter = 0
        for j in df_y[df_y["z"] == i].index.tolist():
            if (
                df_y.loc[j]["x"] + block_size > df_y["x"].max()
                or df_y.loc[j]["x"] - block_size < df_y["x"].min()
                or df_y.loc[j]["y"] + block_size > df_y["y"].max()
                or df_y.loc[j]["y"] - block_size < df_y["y"].min()
            ) and df_y.loc[j]["id"] not in df_surface["id"].values:
                nueva_fila = pd.DataFrame(
                    {
                        "id": [df_y.loc[j]["id"]],
                        "x": [df_y.loc[j]["x"]],
                        "y": [df_y.loc[j]["y"]],
                        "z": [df_y.loc[j]["z"]],
                        "value": [df_y.loc[j]["value"]],
                    }
                )
                print("nueva_fila para df_surface surface")
                print(nueva_fila)
                no_cone = pd.concat([no_cone, nueva_fila], ignore_index=True)
            df_group = no_cone[
                (
                    (no_cone["x"] == df_y.loc[j]["x"] - block_size)
                    | (no_cone["x"] == df_y.loc[j]["x"])
                    | (no_cone["x"] == df_y.loc[j]["x"] + block_size)
                )
                & (
                    (no_cone["y"] == df_y.loc[j]["y"] - block_size)
                    | (no_cone["y"] == df_y.loc[j]["y"])
                    | (no_cone["y"] == df_y.loc[j]["y"] + block_size)
                )
                & ((no_cone["z"] == df_y.loc[j]["z"] + block_size))
            ]
            if len(df_group) > 0:
                nueva_fila = pd.DataFrame(
                    {
                        "id": [df_y.loc[j]["id"]],
                        "x": [df_y.loc[j]["x"]],
                        "y": [df_y.loc[j]["y"]],
                        "z": [df_y.loc[j]["z"]],
                        "value": [df_y.loc[j]["value"]],
                    }
                )
                print("nueva_fila para no_cone")
                print(nueva_fila)
                no_cone = pd.concat([no_cone, nueva_fila], ignore_index=True)
    df_surface = df_y[~df_y["id"].isin(no_cone["id"])]
    df_surface = df_surface.drop_duplicates()
    df_surface = df_surface.reset_index()
    for i in range(len(df_surface)):
        print(f"Tercer FOR {(i/len(df_surface))*100}% | i:{i}->{len(df_surface)}")
        df_group = df_surface[
            (
                (df_surface["x"] == df_surface.loc[i]["x"] - block_size)
                | (df_surface["x"] == df_surface.loc[i]["x"])
                | (df_surface["x"] == df_surface.loc[i]["x"] + block_size)
            )
            & (
                (df_surface["y"] == df_surface.loc[i]["y"] - block_size)
                | (df_surface["y"] == df_surface.loc[i]["y"])
                | (df_surface["y"] == df_surface.loc[i]["y"] + block_size)
            )
            & ((df_surface["z"] == df_surface.loc[i]["z"] + block_size))
        ]
        df_group.reset_index(drop=True, inplace=True)
        if len(df_group) > 0:
            for j in range(len(df_group)):
                nueva_fila = pd.DataFrame(
                    {
                        "start": [df_surface.loc[i]["id"]],
                        "end": [df_group.loc[j]["id"]],
                    }
                )
                df_arc = pd.concat([df_arc, nueva_fila], ignore_index=True)

    print("---")
    print("End")
    print("---")
    # print(df_surface)
    return df_arc


def build_df_arc_2d(df_block_model: pd.DataFrame, block_size: float) -> pd.DataFrame:
    df_arc = pd.DataFrame({"start": [], "end": []})
    df_surface = pd.DataFrame({"id": []})
    for i in sorted(df_block_model["x"].unique()):
        df_group = df_block_model[df_block_model["x"] == i]
        z_max = df_group["z"].max()
        df_group = df_block_model[
            (df_block_model["x"] == i) & (df_block_model["z"] == z_max)
        ].reset_index()
        nueva_fila = pd.DataFrame({"id": [df_group.loc[0, "id"]]})
        df_surface = pd.concat([df_surface, nueva_fila], ignore_index=True)
        print(f"primer i: {i}")

    for i in sorted(set(df_block_model["z"].to_list()), reverse=True):
        for j in df_block_model[df_block_model["z"] == i].index.tolist():
            mask = (
                (df_block_model["z"] == df_block_model.loc[j]["z"] + block_size)
                & (df_block_model["x"] >= df_block_model.loc[j]["x"] - block_size)
                & (df_block_model["x"] <= df_block_model.loc[j]["x"] + block_size)
                & (df_block_model["id"].isin(df_surface["id"]))
            )
            if mask.sum() == 3:
                nueva_fila = pd.DataFrame({"id": [df_block_model.loc[j, "id"]]})
                df_surface = pd.concat([df_surface, nueva_fila], ignore_index=True)
        print(f"segundo i: {i}")
    for i in range(len(df_block_model)):
        mask = (
            (df_block_model["z"] == df_block_model.loc[i]["z"] + block_size)
            & (df_block_model["x"] >= df_block_model.loc[i]["x"] - block_size)
            & (df_block_model["x"] <= df_block_model.loc[i]["x"] + block_size)
            & (df_block_model["id"].isin(df_surface["id"]))
        )
        if mask.sum() == 3:
            for end_id in df_block_model[mask]["id"]:
                df_arc = pd.concat(
                    [
                        df_arc,
                        pd.DataFrame(
                            {"start": [df_block_model.loc[i, "id"]], "end": [end_id]}
                        ),
                    ],
                    ignore_index=True,
                )
        print(f"tercer i: {i}")
    return df_arc


def build_df_x():
    """
    Generates a Pandas DataFrame with the fields id, x, y and value, predefined with a single row of data.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing one row with the following values:
        - `id`: 0
        - `value`: 0

    Examples
    --------
        >>> df_x = build_df_x()
        >>> df_x
            id  value
        0    0      0
    """

    df_x = pd.DataFrame(
        {
            "id": [0],
            "value": [0],
        }
    )
    return df_x


def build_df_arc_positive():
    """
    Generates the Pandas DataFrame 'df_arc_positive' with the fields start_real, end_real, value, type and strength.

    The fields start_real, end_real and value are floats. The fields type and strength are strings.

    Returns
    -------
    pandas.DataFrame
       A empty DataFrame containing the fields start_real, end_real, value, type and strength
    """
    df_arc_positive = pd.DataFrame(
        {
            "start_real": pd.Series(dtype="float"),
            "end_real": pd.Series(dtype="float"),
            "value": pd.Series(dtype="float"),
            "type": pd.Series(dtype="string"),
            "strength": pd.Series(dtype="string"),
        }
    )
    return df_arc_positive


def filter_possible_arcs(df_arc: pd.DataFrame, df_x: pd.DataFrame, df_y: pd.DataFrame):
    """
    Create a copy of the DataFrame `df_arc`and filtered, keeping only the rows where `df_arc[start]` is in `df_x['id']`
    and `df_arc[end]` is in `df_y['id']`.

    Parameters
    ----------
    df_arc : pandas.DataFrame
        DataFrame containing the arcs between the nodes.
    df_x : pandas.DataFrame
        DataFrame with the `id` column used to validate values in `start`.
    df_y : pandas.DataFrame
        DataFrame with the `id` column used to validate values in `end`.

    Returns
    -------
    pandas.DataFrame
        Subset of `df_arc` where both `start` and `end` are valid.
    """
    # we use sets for faster lookup in large dataframes
    valid_starts = set(df_x["id"])
    valid_ends = set(df_y["id"])

    mask = df_arc["start"].isin(valid_starts) & df_arc["end"].isin(valid_ends)

    possible_arc = df_arc[mask].reset_index(drop=True)

    return possible_arc


def build_find_root(
    possible_arc: pd.DataFrame, df_arc_positive: pd.DataFrame, df_x: pd.DataFrame
):
    """
    Find the root arc (i.e., the arc between X₀ and Xₘ).

    Parameters
    ----------
    possible_arc : pandas.DataFrame
        DataFrame containing the arcs between nodes from `df_x` to `df_y`.
    df_arc_positive : pandas.DataFrame
        DataFrame containing the arcs selected by the Lerchs-Grossmann algorithm.

    Returns
    -------
    pandas.DataFrame
    A DataFrame with a single row representing the root arc of `possible_arc.loc[0]`.
    """
    # Inicializa find_root con el primer arco
    find_root = pd.DataFrame(
        {
            "start_real": [possible_arc.loc[0]["start"]],
            "end_real": [possible_arc.loc[0]["end"]],
        }
    )
    # Acumula todos los posibles arcos en una lista
    root_rows = [find_root]
    while True:
        mask = (
            (
                df_arc_positive["start_real"].isin(find_root["start_real"])
                | df_arc_positive["end_real"].isin(find_root["start_real"])
                | df_arc_positive["start_real"].isin(find_root["end_real"])
                | df_arc_positive["end_real"].isin(find_root["end_real"])
            )
            & ~(
                df_arc_positive["start_real"].isin(find_root["start_real"])
                & df_arc_positive["end_real"].isin(find_root["end_real"])
            )
            & (
                df_arc_positive["start_real"].isin(df_x["id"])
                & df_arc_positive["end_real"].isin(df_x["id"])
            )
        )
        possible_root = df_arc_positive[mask].reset_index(drop=True)
        if len(possible_root) == 0:
            break
        root_rows.append(possible_root)
        find_root = pd.concat(root_rows, ignore_index=True)
        find_root = find_root.drop_duplicates()
        mask = (find_root["end_real"].isin(df_x["id"])) & (find_root["start_real"] == 0)
        if len(find_root[mask]) > 0:
            break
    mask = (find_root["start_real"] == 0) & (find_root["end_real"].isin(df_x["id"]))
    find_root = find_root[mask].reset_index(drop=True)
    return find_root


def build_df_arc_direct_tree(df_arc_positive: pd.DataFrame):
    """
    Rebuild the tree structure of `df_arc_positive` from the root to its outermost nodes.

    Parameters
    ----------
    df_arc_positive : pandas.DataFrame
        DataFrame containing the arcs selected by the Lerchs-Grossmann algorithm.

    Returns
    -------
    pandas.DataFrame
    A DataFrame representing the rebuilt tree structure, ordered from root to outermost nodes.
    """
    # Add the arcs with `start_real` == 0 from `df_arc_positive` to `df_arc_direct_tree`
    df_filtered = df_arc_positive[df_arc_positive["start_real"] == 0][
        ["start_real", "end_real"]
    ]
    df_filtered = df_filtered.rename(
        columns={"start_real": "start_tree", "end_real": "end_tree"}
    )
    df_filtered["value"] = np.nan
    # Create `df_arc_direct_tree`
    df_arc_direct_tree = df_filtered.reset_index(drop=True)

    while True:
        mask = ~(
            (
                df_arc_positive["start_real"].isin(df_arc_direct_tree["start_tree"])
                & df_arc_positive["end_real"].isin(df_arc_direct_tree["end_tree"])
            )
            | (
                df_arc_positive["end_real"].isin(df_arc_direct_tree["start_tree"])
                & df_arc_positive["start_real"].isin(df_arc_direct_tree["end_tree"])
            )
        )
        df_arc_positive_filtred = df_arc_positive[mask]
        # Identify the outermost nodes in the current tree structure
        last_blocks = set(
            df_arc_direct_tree[
                ~(df_arc_direct_tree["end_tree"].isin(df_arc_direct_tree["start_tree"]))
            ]["end_tree"]
        )

        added_rows_counter = 0
        # Add the arcs that are connected to `df_arc_direct_tree`, following the tree’s direction
        mask = df_arc_positive_filtred["start_real"].isin(last_blocks)
        new_rows = df_arc_positive_filtred[mask].reset_index(drop=True)
        new_rows = new_rows[["start_real", "end_real"]]
        new_rows = new_rows.rename(
            columns={"start_real": "start_tree", "end_real": "end_tree"}
        )
        new_rows["value"] = np.nan
        df_arc_direct_tree = pd.concat(
            [df_arc_direct_tree, new_rows], ignore_index=True
        )
        added_rows_counter = added_rows_counter + len(new_rows)

        # Add the arcs that are connected to `df_arc_direct_tree`, not following the tree’s direction.
        mask = df_arc_positive_filtred["end_real"].isin(last_blocks)
        new_rows = df_arc_positive_filtred[mask].reset_index(drop=True)
        new_rows = new_rows[["start_real", "end_real"]]
        new_rows = new_rows.rename(
            columns={"start_real": "end_tree", "end_real": "start_tree"}
        )
        new_rows["value"] = np.nan
        df_arc_direct_tree = pd.concat(
            [df_arc_direct_tree, new_rows], ignore_index=True
        )
        added_rows_counter = added_rows_counter + len(new_rows)

        if added_rows_counter == 0:
            break
    return df_arc_direct_tree


def Add_value_tree_to_positive(
    df_arc_positive: pd.DataFrame, df_arc_direct_tree: pd.DataFrame
):
    """
    Add values from `df_arc_direct_tree["value"]` to `df_arc_positive["value"]`.

    Parameters
    ----------
    df_arc_positive : pandas.DataFrame
        DataFrame containing the arcs selected by the Lerchs-Grossmann algorithm.
    df_arc_direct_tree:
        A DataFrame representing the rebuilt tree structure, ordered from root to outermost nodes.
    """
    # Primera condición: start_real == start_tree AND end_real == end_tree
    merged_direct = df_arc_positive.merge(
        df_arc_direct_tree,
        left_on=["start_real", "end_real"],
        right_on=["start_tree", "end_tree"],
        how="left",
    )

    # Segunda condición: start_real == end_tree AND end_real == start_tree
    merged_inverse = df_arc_positive.merge(
        df_arc_direct_tree,
        left_on=["start_real", "end_real"],
        right_on=["end_tree", "start_tree"],
        how="left",
    )

    # Llenar columna 'value' en df_arc_positive si está presente en cualquiera de los dos casos
    df_arc_positive["value"] = merged_direct["value_y"].combine_first(
        merged_inverse["value_y"]
    )


def classify_type_strength(
    df_arc_positive: pd.DataFrame, df_arc_direct_tree: pd.DataFrame
):
    """
    Compare `df_positive` and `df_arc_direct_tree` to classify the arcs in type (`p` or `m`) and the strength in (`strong` or `weak`)

    Parameters
    ----------
    df_arc_positive : pandas.DataFrame
        DataFrame containing the arcs selected by the Lerchs-Grossmann algorithm.
    df_arc_direct_tree:
        A DataFrame representing the rebuilt tree structure, ordered from root to outermost nodes.
    """
    # Optimización: usar sets para comparación rápida
    tree_pairs = set(
        zip(df_arc_direct_tree["start_tree"], df_arc_direct_tree["end_tree"])
    )
    arc_pairs = list(zip(df_arc_positive["start_real"], df_arc_positive["end_real"]))
    # Asignar tipo usando comprensión de listas y np.array
    type_arr = np.array(["p" if pair in tree_pairs else "m" for pair in arc_pairs])
    df_arc_positive["type"] = type_arr
    # Asignar strength vectorizado
    value_arr = df_arc_positive["value"].values.astype(float)
    strength_arr = np.where(
        (type_arr == "p") & (value_arr > 0),
        "strong",
        np.where(
            (type_arr == "p") & (value_arr <= 0),
            "weak",
            np.where((type_arr == "m") & (value_arr > 0), "weak", "strong"),
        ),
    )
    df_arc_positive["strength"] = strength_arr


def main(
    df_block_model: pd.DataFrame,
    df_arc: pd.DataFrame,
    vervose: bool = True,
    id: str = "id",
    value: str = "value",
):
    """
    Main function that applies all steps of the Lerchs-Grossmann algorithm.

    Parameters
    ----------
    df_arc : pandas.DataFrame
        DataFrame containing the arcs between the blocks.
    df_block_model : pandas.DataFrame
        DataFrame containing the data of blocks that are part of the Block Model.
    """
    time_start = time.time()
    mask = df_block_model["id"].isin(df_arc["start"]) | df_block_model["id"].isin(
        df_arc["end"]
    )
    df_block_model = df_block_model[mask].reset_index(drop=True)
    df = df_block_model[[id, value]].rename(columns={id: "id", value: "value"})
    df["id"] = df["id"].astype(int)
    df["value"] = df["value"].astype(float)

    df_arc["start"] = df_arc["start"].astype(int)
    df_arc["end"] = df_arc["end"].astype(int)

    df_y = df[df["value"] < 0].copy()
    print(f"builded df_y time:{time.time()-time_start} seconds")

    df_x_0 = build_df_x()
    df_x = pd.concat([df_x_0, df[df["value"] > 0].copy()], ignore_index=True)
    print(f"builded df_x time:{time.time()-time_start} seconds")

    print(f"filtered df_y time:{time.time()-time_start} seconds")
    print(f"Start for len:{len(df_y)}")
    # Create df_arc_positive directly
    df_arc_positive = pd.DataFrame(
        {
            "start_real": 0,
            "end_real": df["id"],
            "value": df["value"],
            "type": "NaN",
            "strength": "NaN",
        }
    )
    print(f"builded df_arc_positive time:{time.time()-time_start} seconds")

    counter_cicle = 0

    time_cicle = time.time()
    while True:
        # Find possible arcs between `df_x` and `df_y`.
        possible_arc = filter_possible_arcs(df_arc, df_x, df_y)
        if len(possible_arc) == 0:
            print("\nAlgoritm completed !!!")
            print("------------------------")
            print("df_arc_positive")
            print(df_arc_positive)
            print("\ndf_x")
            print(df_x)
            print("\ndf_y_copy")
            print(df_y)
            break
        counter_cicle += 1
        if vervose:
            print("\n---------------")
        print(
            f"Counter cicle {counter_cicle} -> time cicle {time.time()-time_cicle} seconds"
        )
        if vervose:
            print("---------------")
            print("possible_arc")
            print(possible_arc)
            print("df_arc_positive")
            print(df_arc_positive)
        time_cicle = time.time()
        # Reset the columns `type` and `strength`
        df_arc_positive["value"] = np.nan
        df_arc_positive[["type", "strength"]] = "NaN"

        # Find the root, the arc from X₀ to Xₘ
        find_root = build_find_root(possible_arc, df_arc_positive, df_x)
        if vervose:
            print("\nFind the root, the arc from X₀ to Xₘ")
            print("Root")
            print(find_root.loc[len(find_root) - 1])
        # Remove the arc X₀ to Xₘ
        mask = ~(
            df_arc_positive["start_real"].isin(find_root["start_real"])
            & df_arc_positive["end_real"].isin(find_root["end_real"])
        )
        df_arc_positive = df_arc_positive[mask].reset_index(drop=True)
        if vervose:
            print("df_arc_positive")
            print(df_arc_positive)

        # Add the first arc from `possible_arc` to `df_arc_positive` (i.e.,add the arc from Xₗ to X₀)
        new_row = pd.DataFrame(
            {
                "start_real": [possible_arc.loc[0]["start"]],
                "end_real": [possible_arc.loc[0]["end"]],
                "value": [np.nan],
                "type": [np.nan],
                "strength": [np.nan],
            }
        )
        df_arc_positive = pd.concat([df_arc_positive, new_row], ignore_index=True)
        if vervose:
            print("\nAdd the arc from Xₖ to Xₗ")
            print("df_arc_positive")
            print(df_arc_positive)

        # Create `df_arc_direct_tree`
        df_arc_direct_tree = build_df_arc_direct_tree(df_arc_positive)
        if vervose:
            print("\nCreate `df_arc_direct_tree`")
            print("df_arc_direct_tree")
            print(df_arc_direct_tree)

        # Identify and filter the outermost nodes in `df_arc_direct_tree`
        start_tree_set = set(df_arc_direct_tree["start_tree"])
        filtro = ~df_arc_direct_tree["end_tree"].isin(start_tree_set)
        # Optimización: asigna directamente usando .map sobre la columna filtrada
        dict_y_id_value = dict(zip(df_block_model["id"], df_block_model["value"]))
        df_arc_direct_tree.loc[filtro, "value"] = df_arc_direct_tree.loc[
            filtro, "end_tree"
        ].map(dict_y_id_value)
        if vervose:
            print("\nAdd `value` of the outermost nodes in `df_arc_direct_tree`")
            print("df_arc_direct_tree")
            print(df_arc_direct_tree)

        # Compute the values of the arcs at the middle and root of the tree based on the sum of the outermost arcs and the node values.
        y_values = df_block_model.set_index("id")["value"].to_dict()
        while df_arc_direct_tree["value"].isna().any():
            for i, row in df_arc_direct_tree[
                df_arc_direct_tree["value"].isna()
            ].iterrows():
                # Buscar hijos del nodo actual
                children = df_arc_direct_tree[
                    df_arc_direct_tree["start_tree"] == row["end_tree"]
                ]

                # Si alguno de los hijos tiene NaN, no se puede calcular aún
                if children["value"].isna().any():
                    continue

                # Sumar valores de los hijos
                children_sum = children["value"].sum()

                # Buscar valor del nodo destino en df_block_model
                node_value = y_values.get(row["end_tree"], 0)

                # Asignar el valor calculado
                df_arc_direct_tree.at[i, "value"] = children_sum + node_value

        if vervose:
            print(
                "\nCompute the values of the arcs at the middle and root of the tree based on the sum of the outermost arcs and the node values."
            )
            print("df_arc_direct_tree")
            print(df_arc_direct_tree)

        # Add `values` from `df_arc_direct_tree` to `df_arc_positive`
        Add_value_tree_to_positive(df_arc_positive, df_arc_direct_tree)
        if vervose:
            print("\nAdd `values` from `df_arc_direct_tree` to `df_arc_positive`")
            print("df_arc_positive")
            print(df_arc_positive)

        # Compare `df_positive` and `df_arc_direct_tree` to classify the arcs in type (`p` or `m`) and the strength in (`strong` or `weak`)
        classify_type_strength(df_arc_positive, df_arc_direct_tree)
        if vervose:
            print(
                "\nCompare `df_positive` and `df_arc_direct_tree` to classify the arcs in type (`p` or `m`) and the strength in (`strong` or `weak`)"
            )
            print("df_arc_positive")
            print(df_arc_positive)

        # If there is a `strong` arc and `start_real` is not 0, a new arc is added with `start_real` set to 0 and the same end_real. The original arc is removed.
        while (
            len(
                df_arc_positive[
                    (df_arc_positive["start_real"] != 0)
                    & (df_arc_positive["strength"] == "strong")
                ]
            )
            > 0
        ):
            cond_p_strong = (
                (df_arc_positive["start_real"] != 0)
                & (df_arc_positive["strength"] == "strong")
                & (df_arc_positive["type"] == "p")
            )
            df_arc_positive.loc[cond_p_strong, "start_real"] = 0

            cond_m_strong = (
                (df_arc_positive["start_real"] != 0)
                & (df_arc_positive["strength"] == "strong")
                & (df_arc_positive["type"] == "m")
            )
            df_arc_positive.loc[cond_m_strong, "end_real"] = df_arc_positive.loc[
                cond_m_strong, "start_real"
            ]
            df_arc_positive.loc[cond_m_strong, "start_real"] = 0

            # Reset the columns `type` and `strength`
            df_arc_positive["value"] = np.nan
            df_arc_positive[["type", "strength"]] = "NaN"

            # Create `df_arc_direct_tree`
            df_arc_direct_tree = build_df_arc_direct_tree(df_arc_positive)

            # Identify and filter the outermost nodes in `df_arc_direct_tree`
            start_tree_set = set(df_arc_direct_tree["start_tree"])
            filtro = ~df_arc_direct_tree["end_tree"].isin(start_tree_set)
            # Optimización: asigna directamente usando .map sobre la columna filtrada
            dict_y_id_value = dict(zip(df_block_model["id"], df_block_model["value"]))
            df_arc_direct_tree.loc[filtro, "value"] = df_arc_direct_tree.loc[
                filtro, "end_tree"
            ].map(dict_y_id_value)
            # Compute the values of the arcs at the middle and root of the tree based on the sum of the outermost arcs and the node values.
            y_values = df_block_model.set_index("id")["value"].to_dict()
            while df_arc_direct_tree["value"].isna().any():
                for i, row in df_arc_direct_tree[
                    df_arc_direct_tree["value"].isna()
                ].iterrows():
                    # Buscar hijos del nodo actual
                    children = df_arc_direct_tree[
                        df_arc_direct_tree["start_tree"] == row["end_tree"]
                    ]

                    # Si alguno de los hijos tiene NaN, no se puede calcular aún
                    if children["value"].isna().any():
                        continue

                    # Sumar valores de los hijos
                    children_sum = children["value"].sum()

                    # Buscar valor del nodo destino en df_block_model
                    node_value = y_values.get(row["end_tree"], 0)

                    # Asignar el valor calculado
                    df_arc_direct_tree.at[i, "value"] = children_sum + node_value
            Add_value_tree_to_positive(df_arc_positive, df_arc_direct_tree)
            classify_type_strength(df_arc_positive, df_arc_direct_tree)
            if vervose:
                print(
                    "\nIf there is a `strong` arc and `start_real` is not 0, a new arc is added with `start_real` set to 0 and the same end_real. The original arc is removed."
                )
                print("df_arc_positive")
                print(df_arc_positive)
                print("df_x")
                print(df_x)
                print("df_y")
                print(df_y)
        mask = ~((df_arc_positive["start_real"] == 0) & (df_arc_positive["value"] <= 0))
        df_arc_direct_tree_x = build_df_arc_direct_tree(df_arc_positive[mask])
        # Optimización: usar sets para el filtro y evitar copia innecesaria
        tree_ids = set(df_arc_direct_tree_x["start_tree"]).union(
            df_arc_direct_tree_x["end_tree"]
        )
        mask = df["id"].isin(tree_ids)
        df_x = pd.concat([df_x_0, df[mask]], ignore_index=True)
        if vervose:
            print("df_x")
            print(df_x)
        df_y = df[~mask].copy()
        if vervose:
            print("df_y")
            print(df_y)

    mask = df_block_model["id"].isin(df_x["id"])
    df_return = df_block_model[mask].reset_index(drop=True)
    time_end = time.time()
    print(f"Runtime: {time_end - time_start:.4f} seconds")

    return df_return


if __name__ == "__main__":
    df_block_model = pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "x": [1, 2, 3, 4, 5, 2, 3, 4, 3],
            "y": [1, 1, 1, 1, 1, 1, 1, 1, 1],
            "z": [3, 3, 3, 3, 3, 2, 2, 2, 1],
            "value": [-1, -1, -1, -1, -1, -1, -1, 3, 5],
        }
    )

    df_arc = pd.DataFrame(
        {
            "start": [6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9],
            "end": [1, 2, 3, 2, 3, 4, 3, 4, 5, 6, 7, 8],
        }
    )

    df_pit = main(df_block_model, df_arc, False)
    # df_pit.to_csv("df_pit.csv", index=False)
