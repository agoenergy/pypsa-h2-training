# SPDX-FileCopyrightText: 2020-2025 PyPSA-H2-Training Developers

# SPDX-License-Identifier: GPL-2.0-or-later

# coding: utf-8

import pypsa
import pandas as pd

solver = "highs"

if __name__ == "__main__":

    # Create empty PyPSA network
    network = pypsa.Network()

    # Set snapshots to the year 2023 and at hourly resolution
    snapshots = pd.date_range("01-01-2023", "01-01-2024", freq="h", inclusive="left")
    network.set_snapshots(snapshots)

    # Add a carrier for electricity
    network.add(class_name="Carrier", name="electricity")

    # Add a bus for electricity
    network.add(class_name="Bus", name="electricity", carrier="electricity")

    # Add an electricity load
    network.add(class_name="Load", bus="electricity", name="electricity_load", p_set=10)

    # Creating a power plant
    network.add(
        class_name="Generator",
        name="power_plant",
        bus="electricity",
        carrier="electricity",
        p_nom=10,  # unit: MW
        p_nom_extendable=True,
        capital_cost=100,  # unit: $/kW
        marginal_cost=1, # unit: $/MWh
    )

    # solve the network
    network, status = network.optimize(solver_name=solver)

    print("==================================================================")
    if network == "ok" and status == "optimal":
        print(f"SOLVER TESTING RESULTS: {solver} solved the network successfully.")
    else:
        print(f"SOLVER TESTING RESULTS: {solver} did not solve the network successfully. Please recheck your installation and model assumptions.")
