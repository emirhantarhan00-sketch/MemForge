print("1")
from memforge.models.observation import Observation, ObservationSource
print("2")
obs = Observation(
    source=ObservationSource.USER,
    raw_content=" I started learning Python."
)
print("3")
print(obs)