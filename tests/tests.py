from main import verify_cli_args, get_quality_stream
from pytube import YouTube


def test_cli_args():
    assert verify_cli_args(('www.g', '.', 'randomName')) is False, "Should be False because the url is invalid"
    assert verify_cli_args(('www.google.com', 'I dont know', 'randomName')) is False, ("Should be False, because of "
                                                                                       "'I dont know' input for "
                                                                                       "directory path")
    assert verify_cli_args(('https://www.google.com', '.', 'randomName')) is True, ("Should be True, all the "
                                                                                    "arguments are valid")


def test_youtube_stream():
    get_video = YouTube("https://www.youtube.com/watch?v=9b1rm1eECw8&t=2s")
    result = get_quality_stream(get_video)
    assert result is not None, "Should be not be Empty because the url is valid"


