import sys
from pathlib import Path

# Projenin kök dizinindeki 'src' klasörünü öncelikli kılalım
src_path = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(src_path))

from memforge.engines.observation_engine import ObservationEngine
from memforge.models.observation import ObservationSource

print("--- TEST BAŞLADI ---")

engine = ObservationEngine()

obs1 = engine.capture("  I started learning Python.  ")
print("Engine Test 1 - Raw Content:", obs1.raw_content)

obs2 = engine.capture(
    raw_content="System booted",
    source=ObservationSource.SYSTEM,
    context={"version": "0.1"},
)
print("Engine Test 2 - Source & Context:", obs2.source, obs2.context)

print("--- TEST BİTTİ ---")