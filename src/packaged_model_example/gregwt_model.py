"""
Run with:  uv run src/packaged_model_example/gregwt_model.py
Since this model is an optional dependency, provide a helpful error message
"""

try:
    import statsmodels
except ModuleNotFoundError as e:
    raise RuntimeError(
        "This model requires the extra gregwt dependencies. Install with: uv sync --group gregwt [--dev]"
    ) from e

import neworder


class MyGregwtModel(neworder.Model):
    """Dummy model that requires extra dependencies"""

    def __init__(self) -> None:
        super().__init__(neworder.NoTimeline())

    def step(self) -> None:
        pass


if __name__ == "__main__":
    m = MyGregwtModel()
    neworder.run(m)
