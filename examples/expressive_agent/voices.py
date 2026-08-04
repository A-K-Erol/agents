"""The expressive-capable TTS voices this demo can switch between.

Every voice here publishes ``lk.expression``, so a frontend always has a mood to
render. Two things are required for that, and both are why this list is short:

- a LiveKit Inference TTS whose model declares a markup dialect. deepgram and
  rime have none, so they synthesize fine but render no tags.
- an expression or emotion tag in that dialect, which is what becomes the
  attribute. xai steers delivery through prosody and sound tags only, so its
  speech is expressive but nothing reaches the frontend.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Voice:
    provider: str
    model: str
    voice: str
    label: str


VOICES: dict[str, Voice] = {
    "fishaudio": Voice(
        provider="fishaudio",
        model="fishaudio/s2.1-pro",
        voice="9a9cf47702da476aa4629e2506d4a857",
        label="Fish Audio S2.1 Pro (Hannah)",
    ),
    "inworld": Voice(
        provider="inworld",
        model="inworld/inworld-tts-2",
        voice="Ashley",
        label="Inworld TTS 2 (Ashley)",
    ),
    "cartesia": Voice(
        provider="cartesia",
        model="cartesia/sonic-3",
        voice="9626c31c-bec5-4cca-baa8-f8ba9e84c8bc",
        label="Cartesia Sonic 3 (Jacqueline)",
    ),
}

DEFAULT_VOICE = "fishaudio"


def resolve(provider: str | None) -> Voice:
    """Pick a voice by provider name, falling back to the default."""
    return VOICES.get(provider or "", VOICES[DEFAULT_VOICE])
