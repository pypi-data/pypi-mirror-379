import subprocess
import json
import os
import m3u8
from concurrent.futures import ThreadPoolExecutor, as_completed
import pathlib

manifest = './1440/m3u8.m3u8'

def check_segments_parallel(file, segments, max_workers=4):
    """
    Проверяет список сегментов параллельно через check_hls_segment.
    Возвращает словарь {segment_path: [ошибки]} и показывает прогресс проверки.
    """
    results = {}
    total = len(segments)
    completed = 0

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(check_hls_segment, seg): seg for seg in segments}

        for future in as_completed(futures):
            seg = futures[future]
            try:
                errs = future.result()
                results[seg] = errs
            except Exception as e:
                results[seg] = [f"Ошибка при проверке сегмента: {e}"]

            completed += 1
            print(f"[{file}] Проверено {completed}/{total} сегментов", end="\r")

    print()  # Переход на новую строку после прогресса
    return results

# Поддерживаемые аудиокодеки для браузера
BROWSER_AUDIO_CODECS = {"aac", "mp3", "opus", "vorbis"}

def check_hls_segment(file_path: str) -> list[str]:
    """
    Проверяет HLS сегмент (TS/MP4) на корректность аудио и видео для браузера.
    Возвращает список ошибок. Если список пустой, сегмент рабочий.
    """
    errors = []

    try:
        # Получаем информацию о потоках через ffprobe
        cmd = [
            "ffprobe",
            "-v", "error",
            "-show_streams",
            "-of", "json",
            file_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        info = json.loads(result.stdout)

        streams = info.get("streams", [])
        if not streams:
            errors.append("Нет потоков в файле")
            return errors

        for stream in streams:
            codec_type = stream.get("codec_type")
            codec_name = stream.get("codec_name", "").lower()

            if codec_type == "audio":
                channels = int(stream.get("channels", 0))
                sample_rate = int(stream.get("sample_rate", 0))
                
                if channels <= 0:
                    errors.append(f"Аудио поток битый: channels={channels}")
                if sample_rate <= 0:
                    errors.append(f"Аудио поток битый: sample_rate={sample_rate}")
                if codec_name not in BROWSER_AUDIO_CODECS:
                    errors.append(f"Аудиокодек '{codec_name}' не поддерживается браузером")

            elif codec_type == "video":
                width = int(stream.get("width", 0))
                height = int(stream.get("height", 0))
                if width <= 0 or height <= 0:
                    errors.append(f"Видео поток битый: width={width}, height={height}")

    except subprocess.CalledProcessError as e:
        errors.append(f"FFprobe не смог обработать файл: {e}")
    except json.JSONDecodeError as e:
        errors.append(f"Не удалось распарсить JSON ffprobe: {e}")

    return errors


def check_hls_segments_exist(file_path: str) -> tuple[list[str], list[str]]:
    """
    Проверяет, что все локальные сегменты плейлиста .m3u8 существуют.
    Возвращает два списка:
      - segments: список всех сегментов (пути к файлам)
      - errors: список ошибок (отсутствующие сегменты)
    """
    errors = []
    segments = []

    try:
        file_url = pathlib.Path(file_path).as_uri()
        playlist = m3u8.load(file_url)
    except Exception as e:
        return [], [f"Не удалось загрузить плейлист: {e}"]

    base_path = os.path.dirname(file_path)

    for i, segment in enumerate(playlist.segments):
        seg_path = os.path.join(base_path, segment.uri)
        segments.append(seg_path)
        if not os.path.isfile(seg_path):
            errors.append(f"Сегмент {i} отсутствует: {seg_path}")

    return segments, errors