from pathlib import Path
from shutil import copy
from unittest.mock import patch

import numpy as np
import pandas as pd
import pyomo.environ as pyo
import pytest
import yaml

from annular.satellite_model import MultiProfileBiddingStrategy
from tests.conftest import compare_objects


@pytest.fixture(scope="module")
def common_args():
    """Provides arguments for `SatelliteModel` that are common across subclasses."""
    common_args = {
        "rolling_horizon_step": 24,
        "ceiling_price": 200,
        "start_hour": 1,
        "num_hours": 2400,
    }

    return common_args


@pytest.fixture(scope="module")
def multi_profile_args(tmp_path_factory, data_dir):
    """Provides arguments specific to `MultiProfileBiddingStrategy`."""
    output_path = tmp_path_factory.mktemp("output")
    config_dict = {
        "demands_path": str(data_dir / "multi_profile/loads_generators_timeseries.csv"),
        "forecasts_path": str(data_dir / "multi_profile/forecast-prices.csv"),
        "carrier_prices_path": str(data_dir / "multi_profile/price_other_carriers.csv"),
        "cronian_config_path": str(data_dir / "multi_profile/prosumers/P01.yaml"),
        "floor_price": 0,
        "horizon_size": 48,
        "output_path": str(output_path),
    }
    return config_dict


@pytest.fixture
def multi_profile_bid_strategy(common_args, multi_profile_args):
    """Initialization of the multi profile bidding strategy."""
    input_args = common_args | multi_profile_args
    return MultiProfileBiddingStrategy(**input_args)


@pytest.fixture
def forecast_scenarios(multi_profile_bid_strategy):
    """Create a basic set of price forecast scenarios."""
    scaling_factor = multi_profile_bid_strategy.forecast_scaling_factor
    base_forecast = multi_profile_bid_strategy.base_forecast[:24]
    return multi_profile_bid_strategy.make_forecast_scenarios(base_forecast, scaling_factor)


@pytest.fixture
def model_with_objective(tmp_path, data_dir, request):
    """Creates a model with cost objective added, based on the test case data."""
    horizon_len = 2
    horizon = pd.date_range("2024-01-01", periods=horizon_len, freq="h", tz="UTC")

    case_data = request.param
    e_price = case_data.get("e_price", [0] * horizon_len)
    methane_price = case_data.get("methane_price", [0] * horizon_len)

    demands_df = pd.DataFrame({"heat demand": [0] * horizon_len}, index=horizon)
    forecast_df = pd.DataFrame({"e_price": e_price}, index=horizon)
    carrier_prices_df = pd.DataFrame({"methane": methane_price}, index=horizon)

    demands_file = tmp_path / "demands.csv"
    demands_df.to_csv(demands_file)

    forecasts_file = tmp_path / "forecasts.csv"
    forecast_df.to_csv(forecasts_file)

    carrier_file = tmp_path / "carriers.csv"
    carrier_prices_df.to_csv(carrier_file)

    output_path = tmp_path / "output"

    config_dict = {
        "demands_path": str(demands_file),
        "forecasts_path": str(forecasts_file),
        "carrier_prices_path": str(carrier_file),
        "cronian_config_path": str(data_dir / "multi_profile/prosumers/P01.yaml"),
        "floor_price": 0,
        "horizon_size": 48,
        "rolling_horizon_step": 24,
        "num_hours": 2400,
        "start_hour": 1,
    }
    common_settings = {
        "ceiling_price": 1000,
        "output_path": output_path,
    }
    input_args = common_settings | config_dict
    strategy = MultiProfileBiddingStrategy(**input_args)

    prosumer_id = strategy.cronian_config["id"]
    fixed_vars = {
        f"{prosumer_id}_electric_power": case_data.get("electric_power", [0] * horizon_len),
        f"{prosumer_id}_Gas boiler_methane_consumption": case_data.get("methane_consumption", [0] * horizon_len),
    }

    model = strategy._create_model(horizon, e_price)

    return model, horizon, fixed_vars, case_data["expected_cost"]


@pytest.fixture
def patched_strategy(multi_profile_bid_strategy):
    """Patch bidding strategy with a mock for _update_internal_state."""
    with patch.object(multi_profile_bid_strategy, "_update_internal_state"):
        yield multi_profile_bid_strategy


def test_multi_profile_strategy_successful_init(common_args, multi_profile_args):
    """Tests that MultiProfileBiddingStrategy initializes correctly with valid parameters."""
    input_args = common_args | multi_profile_args

    strategy = MultiProfileBiddingStrategy(**input_args)
    assert isinstance(strategy, MultiProfileBiddingStrategy)
    assert strategy.horizon_size == 48


def test_init_equivalence(tmp_path, common_args, multi_profile_args):
    """Test that initialization from file is the same as with kwargs."""
    input_args = common_args | multi_profile_args
    strategy = MultiProfileBiddingStrategy(**input_args)

    config_file = tmp_path / "config.yaml"

    # Copy files to the tmp_path and replace absolute path with relative to config file
    args_to_config_file = multi_profile_args.copy()
    for key, value in args_to_config_file.items():
        if key.endswith("_path") and key != "output_path":
            orig_path = Path(value)
            copy(orig_path, tmp_path / orig_path.name)
            args_to_config_file[key] = orig_path.name

    with config_file.open("w") as f:
        yaml.dump(args_to_config_file, f)

    strategy_from_file = MultiProfileBiddingStrategy.from_file(config_file, **common_args)
    assert isinstance(strategy, type(strategy_from_file))

    attrs_strategy = vars(strategy).keys()
    attrs_from_file = vars(strategy_from_file).keys()
    assert set(attrs_strategy) ^ set(attrs_from_file) == set()
    ignore_attrs = ["solver"]
    for attr_name, expected_value in vars(strategy).items():
        if attr_name in ignore_attrs:
            continue
        attr_other = getattr(strategy_from_file, attr_name)
        compare_objects(attr_other, expected_value)


# Parameterized fixture with invalid args that trigger errors when initializing the strategy.
@pytest.mark.parametrize(
    "invalid_args, error_message",
    [
        (
            {"horizon_size": 23},  # Will overwrite the multi_profile_args['horizon_size']) in the tests below.
            "horizon_size must be at least 24",
        ),
        (
            {"forecast_scaling_factor": 0},
            "forecast_scaling_factor cannot be less than or equal to 0.",
        ),
        (
            {"forecast_scaling_factor": -1},
            "forecast_scaling_factor cannot be less than or equal to 0.",
        ),
    ],
    ids=[
        "Horizon size shorter than 24",
        "Zero scaling_factor",
        "Negative scaling_factor",
    ],
)
def test_multi_profile_strategy_init_error(common_args, multi_profile_args, invalid_args, error_message):
    """Test that MultiProfileBiddingStrategy raises ValueError with invalid parameters."""
    # Overwrite any valid args from multi_profile_args with invalid args from the invalid_case fixture.
    input_args = common_args | multi_profile_args | invalid_args

    # Test that a ValueError is raised with the expected error message for args with invalid values.
    with pytest.raises(ValueError, match=error_message):
        MultiProfileBiddingStrategy(**input_args)


@pytest.mark.parametrize("base_forecast_length", [23, 25])
def test_make_forecast_scenarios_length_error(base_forecast_length):
    """Test that make_forecast_scenarios raises ValueError if base_forecast length is not 24."""
    base_forecast = pd.Series(range(base_forecast_length))
    with pytest.raises(ValueError, match="Forecast length must be 24 to represent a full day with hourly resolution"):
        MultiProfileBiddingStrategy.make_forecast_scenarios(base_forecast, 1.5)


@pytest.mark.integration
@pytest.mark.gurobi
def test_determine_profiles(multi_profile_bid_strategy, forecast_scenarios):
    """Test determine_profiles method of MultiProfileBiddingStrategy."""
    profiles = multi_profile_bid_strategy._determine_profiles(forecast_scenarios)
    assert isinstance(profiles, dict)
    assert len(profiles) == len(forecast_scenarios)
    for profile in profiles.values():
        assert len(profile) == 24, f"Profile length {len(profile)} is not 24 as expected."


def test_make_forecast_scenarios_values(multi_profile_bid_strategy, forecast_scenarios):
    """Test that make_forecast_scenarios generates the expected scenarios."""
    base_forecast = multi_profile_bid_strategy.base_forecast[:24]
    scaling_factor = multi_profile_bid_strategy.forecast_scaling_factor

    assert isinstance(forecast_scenarios, dict)
    assert all(isinstance(val, pd.DataFrame) for val in forecast_scenarios.values())
    assert len(forecast_scenarios) == 13
    assert all(len(df) == 24 for df in forecast_scenarios.values())
    assert all("e_price" in df.columns for df in forecast_scenarios.values())

    # Check specific outputs
    base_values = base_forecast["e_price"].values
    assert np.allclose(forecast_scenarios["base_forecast"]["e_price"].values, base_values)
    assert np.allclose(forecast_scenarios["scale_up"]["e_price"].values, base_values * scaling_factor)
    assert np.allclose(forecast_scenarios["scale_down"]["e_price"].values, base_values / scaling_factor)

    # Check Peak-mid and valley-mid scaling using normalized values
    peak_vals = forecast_scenarios["peak_mid"]["e_price"].values
    norm_peak_vals = (peak_vals - peak_vals.min()) / (peak_vals.max() - peak_vals.min())
    assert norm_peak_vals[12] > norm_peak_vals[0]
    assert norm_peak_vals[12] > norm_peak_vals[-1]

    valley_vals = forecast_scenarios["valley_mid"]["e_price"].values
    norm_valley_vals = (valley_vals - valley_vals.min()) / (valley_vals.max() - valley_vals.min())
    assert norm_valley_vals[12] < norm_valley_vals[0]
    assert norm_valley_vals[12] < norm_valley_vals[-1]

    # Check boosted scenarios
    # Check day_period_boost: hours 8–18 inclusive should be scaled
    day_boost_vals = forecast_scenarios["day_period_boost"]["e_price"].values
    assert np.allclose(day_boost_vals[8:19], base_values[8:19] * scaling_factor)
    assert np.allclose(day_boost_vals[:8], base_values[:8])  # Early morning unchanged
    assert np.allclose(day_boost_vals[19:], base_values[19:])  # Evening unchanged

    # Check morning_evening_boost: hours <8 and >= 19 should be scaled
    mor_eve_boost_vals = forecast_scenarios["morning_evening_boost"]["e_price"].values
    assert np.allclose(mor_eve_boost_vals[:8], base_values[:8] * scaling_factor)
    assert np.allclose(mor_eve_boost_vals[19:], base_values[19:] * scaling_factor)
    assert np.allclose(mor_eve_boost_vals[8:19], base_values[8:19])  # Day period unchanged

    # Check base_min... and base_max... boost scenarios
    base_min = base_values.min()
    base_max = base_values.max()

    base_min_day_boost_vals = forecast_scenarios["base_min_day_period_boost"]["e_price"].values
    assert np.allclose(base_min_day_boost_vals[:8], base_min)
    assert np.allclose(base_min_day_boost_vals[8:19], base_min * scaling_factor)
    assert np.allclose(base_min_day_boost_vals[19:], base_min)

    base_max_mor_eve_boost_vals = forecast_scenarios["base_max_morning_evening_boost"]["e_price"].values
    assert np.allclose(base_max_mor_eve_boost_vals[:8], base_max * scaling_factor)
    assert np.allclose(base_max_mor_eve_boost_vals[8:19], base_max)
    assert np.allclose(base_max_mor_eve_boost_vals[19:], base_max * scaling_factor)


def test_create_model(multi_profile_bid_strategy):
    """Test create_model method of MultiProfileBiddingStrategy."""
    prosumer_id = multi_profile_bid_strategy.cronian_config["id"]
    horizon = pd.date_range(start="2024-01-01 00:00:00", periods=2, freq="h", tz="UTC")
    e_price = [20, 10]
    model = multi_profile_bid_strategy._create_model(horizon, e_price)

    assert isinstance(model, pyo.ConcreteModel)
    assert model.name == f"Optimization model of satellite--{prosumer_id}"

    expected_model_attributes = [
        "time",
        "e_price",
        f"{prosumer_id}_Heat pump_electricity_consumption",
        f"{prosumer_id}_Heat pump_heat_supply",
        f"{prosumer_id}_Gas boiler_methane_consumption",
        f"{prosumer_id}_Gas boiler_heat_supply",
        f"{prosumer_id}_Heat storage_energy_capacity",
        f"{prosumer_id}_Heat storage_charge_capacity",
        f"{prosumer_id}_Heat storage_discharge_capacity",
        f"{prosumer_id}_space heating_base_demand",
        f"{prosumer_id}_space heating_local_heat_balance_constraint",
        f"{prosumer_id}_electric_power",
    ]

    for attr in expected_model_attributes:
        assert hasattr(model, attr), f"Model does not have expected attribute: {attr}"

    assert len(model.time) == len(horizon), "Model time set does not match the horizon length."
    assert len(model.e_price) == len(horizon), "Model e_price set does not match the horizon length."
    assert hasattr(model, "cost_objective"), "Cost objective has not been added."


TEST_CASES = {
    "electricity_consumption_cost": {
        "e_price": [100, 200],
        "electric_power": [-2, -1],
        "expected_cost": 400.0,  # -1 * ((100 * -2) + (200 * -1))
    },
    "electricity_production_revenue": {
        "e_price": [100, 200],
        "electric_power": [2, 1],
        "expected_cost": -400.0,  # -1 * ((100 * 2) + (200 * 1))
    },
    "mixed_electricity_consumption_and_revenue": {
        "e_price": [100, 200],
        "electric_power": [-2, 2],
        "expected_cost": -200,  # -1 * ((100 * -2) + (200* 2))
    },
    "zero_electricity_activity": {
        "e_price": [100, 200],
        "electric_power": [0, 0],
        "expected_cost": 0.0,
    },
    "methane_consumption_cost": {
        "methane_price": [10, 25],
        "methane_consumption": [5, 2],
        "expected_cost": 100.0,  # (10* 5) + (25 * 2)
    },
    "zero_methane_consumption_cost": {
        "methane_price": [10, 25],
        "methane_consumption": [0, 0],
        "expected_cost": 0.0,
    },
}


@pytest.mark.parametrize("model_with_objective", TEST_CASES.values(), indirect=True, ids=TEST_CASES.keys())
def test_objective_costs(model_with_objective):
    """Test the cost objective for electricity consumption and production."""
    model, horizon, fixed_vars, expected_cost = model_with_objective

    for var_name, values in fixed_vars.items():
        if not hasattr(model, var_name):
            raise ValueError(f"Variable '{var_name}' not found in model.")
        var = getattr(model, var_name)
        for t, val in zip(horizon, values):
            var[t].fix(val)

    actual_cost = pyo.value(model.cost_objective)
    assert actual_cost == pytest.approx(expected_cost)


@pytest.mark.integration
@pytest.mark.gurobi
def test_multi_profile_bids(multi_profile_bid_strategy):
    """Test that 'determine_bids' returns a bids table in correct format."""
    bids = multi_profile_bid_strategy.determine_bids()
    assert isinstance(bids, pd.DataFrame)
    assert len(bids.index.get_level_values("timestamp").unique()) == 24
    assert len(bids.index.get_level_values("exclusive_group_id").unique()) == 1
    assert len(bids.index.get_level_values("profile_block_id").unique()) == 13


@pytest.mark.integration
@pytest.mark.gurobi
def test_demand_bids_values(data_dir, common_args, multi_profile_args):
    """Test that demand values for a known case are correct.

    In this case, demand is so high that the heat pump is always on at maximum capacity (=10_000).
    """
    # Replace default prosumer with one **without** a battery: all bids are demand-only
    input_args = (
        common_args | multi_profile_args | {"cronian_config_path": str(data_dir / "multi_profile/prosumers/P02.yaml")}
    )
    strategy = MultiProfileBiddingStrategy(**input_args)
    bids = strategy.determine_bids()
    assert (bids["quantity"] == 10_000).all()


@pytest.mark.gurobi
def test_meet_demand(patched_strategy):
    """Test that meeting demand correctly fixes the electric power."""
    market_price = list(range(24, 0, -1))
    demand_met = range(1, 25)
    patched_strategy.meet_demand(market_price=market_price, demand_met=demand_met)
    horizon, model = patched_strategy._update_internal_state.call_args.args
    electric_power = getattr(model, f"{patched_strategy.cronian_config['id']}_electric_power")
    assert all(electric_power[t].value == -demand for t, demand in zip(horizon, demand_met))
    assert all(model.e_price[t] == price for t, price in zip(horizon, market_price))


@pytest.mark.gurobi
def test_update_internal_state(multi_profile_bid_strategy):
    """Test that energy levels of storage assets are updated correctly."""
    # Confirm initial values
    assert multi_profile_bid_strategy.cronian_config["assets"]["Heat storage"]["initial_energy"] == 1_000
    assert multi_profile_bid_strategy.cronian_config["assets"]["Battery"]["initial_energy"] == 0

    multi_profile_bid_strategy.meet_demand(market_price=[0] * 24, demand_met=[11_000] * 24)

    # All stored heat energy should be used
    assert multi_profile_bid_strategy.cronian_config["assets"]["Heat storage"]["initial_energy"] == 0
    # The heat pump can only consume 10_000 power per hour, so 1_000 should charge the battery
    assert multi_profile_bid_strategy.cronian_config["assets"]["Battery"]["initial_energy"] == 1_000 * 0.9 * 24
