import json
import os
from pathlib import Path
from typing import Any, Optional

from pydantic import BaseModel, Field
from zen_garden.model.default_config import System  # type: ignore
from zen_garden.postprocess.results import Results  # type: ignore

from zen_temple.utils import get_variable_name

from ..config import config


class ScenarioDetail(BaseModel):
    """
    ScenarioDetail is the model that includes all the detail information of a scenario. It also contains the System-information from ZEN Garden.
    """

    system: System
    reference_carrier: dict[str, str]
    carriers_input: dict[str, list[str]]
    carriers_output: dict[str, list[str]]
    edges: dict[str, str]


class SolutionDetail(BaseModel):
    """
    SolutionDetail is the model that includes all the detail information of a solution. This includes the ScenarioDetail for all scenarios of a solution.
    """

    name: str
    folder_name: str
    scenarios: dict[str, ScenarioDetail]
    version: str

    @staticmethod
    def from_path(path: str) -> "SolutionDetail":
        """
        Generator that instanciates a SolutionDetail given the path of a solution.
        It creates a Solution-instance of ZEN Gardens soluion class and extracts the necessary dataframes from this soultion.

        :param path: Path to the results folder.
        """
        name = os.path.split(path)[-1]
        relative_path = os.path.relpath(path, start=config.SOLUTION_FOLDER)
        results = Results(path)
        results_version = results.get_analysis().zen_garden_version
        scenario_details = {}

        for scenario_name, scenario in results.solution_loader.scenarios.items():
            system = scenario.system
            reference_carriers = results.get_df(
                get_variable_name("set_reference_carriers", results_version),
                scenario_name=scenario_name,
            ).to_dict()

            df_input_carriers = results.get_df(
                get_variable_name("set_input_carriers", results_version),
                scenario_name=scenario_name,
            )

            df_output_carriers = results.get_df(
                get_variable_name("set_output_carriers", results_version),
                scenario_name=scenario_name,
            )

            edges = results.get_df(
                get_variable_name("set_nodes_on_edges", results_version),
                scenario_name=scenario_name,
            )

            edges_dict = edges.to_dict()
            carriers_input_dict = {
                key: val.split(",") for key, val in df_input_carriers.to_dict().items()
            }
            carriers_output_dict = {
                key: val.split(",") for key, val in df_output_carriers.to_dict().items()
            }

            for key in carriers_output_dict:
                if carriers_output_dict[key] == [""]:
                    carriers_output_dict[key] = []

            for key in carriers_input_dict:
                if carriers_input_dict[key] == [""]:
                    carriers_input_dict[key] = []

            scenario_details[scenario_name] = ScenarioDetail(
                system=system,
                reference_carrier=reference_carriers,
                carriers_input=carriers_input_dict,
                carriers_output=carriers_output_dict,
                edges=edges_dict,
            )

        version = results.get_analysis().zen_garden_version
        if version is None:
            version = "0.0.0"

        return SolutionDetail(
            name=name,
            folder_name=str(relative_path),
            scenarios=scenario_details,
            version=version,
        )


class SolutionList(BaseModel):
    """
    SolutionList defines the model of the data that is included in the solutions list endpoint.
    """

    folder_name: str
    name: str
    nodes: list[str] = Field(default=[])
    total_hours_per_year: int
    optimized_years: int
    technologies: list[str] = Field(default=[])
    carriers: list[str] = Field(default=[])
    scenarios: list[str] = Field(default=[])

    @staticmethod
    def from_path(path: str) -> "SolutionList":
        """
        Generator method to instantiate a SolutionList ins given the path of a solution.

        :param path: Path to the results folder.
        """
        with open(os.path.join(path, "scenarios.json"), "r") as f:
            scenarios_json: dict[str, Any] = json.load(f)

        scenarios = list(scenarios_json.keys())

        scenario_name = ""

        # TODO I think this needs to be more flexible for the different scenario types -> if subscenarios exist or not
        # TODO this is a quick fix for the current scenario structure
        if len(scenarios_json) > 1:
            first_scenario_name = scenarios[0]
            if scenarios_json[first_scenario_name]["sub_folder"] != "":
                scenario_name = (
                    "scenario_"
                    + scenarios_json[first_scenario_name]["base_scenario"]
                    + "/"
                    + "scenario_"
                    + scenarios_json[first_scenario_name]["sub_folder"]
                )
            else:
                scenario_name = (
                    "scenario_" + scenarios_json[first_scenario_name]["base_scenario"]
                )

        with open(os.path.join(path, scenario_name, "system.json")) as f:
            system: dict[str, Any] = json.load(f)

        relative_folder = path.replace(config.SOLUTION_FOLDER, "")

        if relative_folder[0] == "/":
            relative_folder = relative_folder[1:]

        system["folder_name"] = relative_folder

        # TODO this can change with the scenarios - it should be scenario dependent
        system["carriers"] = system["set_carriers"]
        system["technologies"] = system["set_technologies"]
        system["scenarios"] = scenarios
        system["nodes"] = system["set_nodes"]

        scenario_path = Path(path).relative_to(config.SOLUTION_FOLDER)
        system["name"] = ".".join(scenario_path.parts)
        solution = SolutionList(**system)

        return solution

