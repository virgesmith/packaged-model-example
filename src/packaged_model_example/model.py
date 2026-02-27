from pathlib import Path
import neworder

from packaged_model_example.environment import ModelConfig
import pandas as pd


class MyModel(neworder.Model):
    def __init__(self, config: ModelConfig, input_path: Path, output_path: Path) -> None:
        super().__init__(
            neworder.LinearTimeline(
                config.timeline.start_year,
                config.timeline.end_year,
                config.timeline.end_year - config.timeline.start_year,
            ),
        )
        self.output_path = output_path
        neworder.verbose(config.verbose)
        neworder.log(f"Initialised {config.name}")
        neworder.log(f"Reading inputs from {input_path}...")
        self.population = pd.read_csv(input_path / config.baseline.file)
        self.result = pd.DataFrame(columns=["average_working_age", "dependency_ratio"])

    def step(self) -> None:
        self.population.age += 1
        self.population["retired"] = self.population.age >= 70
        self.result.loc[self.timeline.time] = (
            self.population[~self.population.retired].age.mean(),
            self.population.retired.sum() / ((~self.population.retired).sum()),
        )

    def finalise(self) -> None:
        neworder.log(self.result)
        neworder.log(f"Writing outputs to {self.output_path}...")
        self.result.to_csv(self.output_path / "result.csv")
