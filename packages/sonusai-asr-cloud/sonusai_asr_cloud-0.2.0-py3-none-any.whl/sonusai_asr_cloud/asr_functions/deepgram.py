from sonusai.datatypes import AudioT
from sonusai.utils import ASRResult


def deepgram_validate(**_config) -> None:
    from os import getenv

    key = getenv("DEEPGRAM_API_KEY")
    if key is None:
        raise OSError("DEEPGRAM_API_KEY environment variable does not exist")


def deepgram(audio: AudioT, **_config) -> ASRResult:
    import tempfile
    from os import getenv
    from os.path import join
    from random import random
    from time import sleep

    import httpx
    from deepgram import DeepgramClient
    from deepgram import FileSource
    from deepgram import PrerecordedOptions
    from sonusai.utils import ASRResult
    from sonusai.utils import float_to_int16
    from sonusai.utils import write_audio

    key = getenv("DEEPGRAM_API_KEY")
    if key is None:
        raise OSError("DEEPGRAM_API_KEY environment variable does not exist")

    client = DeepgramClient(key)
    with tempfile.TemporaryDirectory() as tmp:
        file = join(tmp, "asr.wav")
        write_audio(name=file, audio=float_to_int16(audio))

        with open(file, "rb") as audio:
            buffer_data = audio.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        options: PrerecordedOptions = PrerecordedOptions(
            model="nova-2",
            smart_format=False,
            utterances=False,
            punctuate=False,
            diarize=False,
        )

        retry = 5
        count = 0
        timeout = httpx.Timeout(300.0, connect=10.0)
        while True:
            try:
                results = client.listen.rest.v("1").transcribe_file(payload, options, timeout=timeout)["results"]
                return ASRResult(
                    text=results["channels"][0]["alternatives"][0]["transcript"],
                    confidence=results["channels"][0]["alternatives"][0]["confidence"],
                )
            except Exception as e:
                count += 1
                print(f"Warning: Deepgram exception: {e}")
                if count >= retry:
                    raise SystemError(f"Deepgram exception: {e.args}") from e
                sleep(count * (1 + random()))  # noqa: S311


"""
Deepgram results:
{'metadata': {'channels': 1,
              'created': '2023-01-30T21:49:44.048Z',
              'duration': 2.3795626,
              'model_info': {'c12089d0-0766-4ca0-9511-98fd2e443ebd': {'name': 'general',
                                                                      'tier': 'base',
                                                                      'version': '2022-01-18.1'}},
              'models': ['c12089d0-0766-4ca0-9511-98fd2e443ebd'],
              'request_id': 'e1154979-07f7-46a3-89e6-d5d796676d31',
              'sha256': '3cad2f30a83e351eab3c4dcaa2ec47185e8f2979c90abec0c2332a7eef7c2d40',
              'transaction_key': 'deprecated'},
 'results': {'channels': [{'alternatives': [{'confidence': 0.9794922,
                                             'transcript': 'the birch can canoe slid on the smooth planks',
                                             'words': [{'confidence': 0.9794922,
                                                        'end': 0.29625,
                                                        'start': 0.13825,
                                                        'word': 'the'},
                                                       {'confidence': 0.9902344,
                                                        'end': 0.57275,
                                                        'start': 0.29625,
                                                        'word': 'birch'},
                                                       {'confidence': 0.73535156,
                                                        'end': 0.73074996,
                                                        'start': 0.57275,
                                                        'word': 'can'},
                                                       {'confidence': 0.9550781,
                                                        'end': 1.08625,
                                                        'start': 0.73074996,
                                                        'word': 'canoe'},
                                                       {'confidence': 0.98876953,
                                                        'end': 1.2442499,
                                                        'start': 1.08625,
                                                        'word': 'slid'},
                                                       {'confidence': 0.9921875,
                                                        'end': 1.3627499,
                                                        'start': 1.2442499,
                                                        'word': 'on'},
                                                       {'confidence': 0.9584961,
                                                        'end': 1.5997499,
                                                        'start': 1.3627499,
                                                        'word': 'the'},
                                                       {'confidence': 0.9970703,
                                                        'end': 1.9947499,
                                                        'start': 1.5997499,
                                                        'word': 'smooth'},
                                                       {'confidence': 0.98828125,
                                                        'end': 2.23175,
                                                        'start': 1.9947499,
                                                        'word': 'planks'}]}]}]}}
"""
