from .audio_cls.src.model.net import ShortChunkCNN_Res
from .midi_cls.src.model.net import SAN
from .midi_cls.midi_helper.remi.midi2event import analyzer, corpus, event
from .midi_cls.midi_helper.magenta.processor import encode_midi