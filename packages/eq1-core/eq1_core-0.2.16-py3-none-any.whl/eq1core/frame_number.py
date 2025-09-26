from typing import List
from .data import FrameInfo


class FrameNumberTrackerProducer:
    def __init__(self, frame_infos: List[FrameInfo]):
        self._frame_counter_dict = {}

        for frame_info in frame_infos:
            if not isinstance(frame_info, FrameInfo):
                raise TypeError(
                    f'frame_info type error. expected {FrameInfo}, got {type(frame_info)}')

            self._frame_counter_dict[frame_info.camera_number] = FrameNumberTracker(frame_info)

    def get_frame_number_by_camera_number(self, camera_number: int) -> int:
        if camera_number not in self._frame_counter_dict:
            raise ValueError(
                f'camera_number {camera_number} is not in frame_counter_dict')

        return self._frame_counter_dict[camera_number].frame_number

    def increase_frame_number_by_camera_number(self, camera_number: int):
        if camera_number not in self._frame_counter_dict:
            raise ValueError(
                f'camera_number {camera_number} is not in frame_counter_dict')

        if not callable(self._frame_counter_dict[camera_number].increase_frame_number):
            raise TypeError(
                f'frame_counter_dict[{camera_number}].increase_frame_number is not callable')

        self._frame_counter_dict[camera_number].increase_frame_number()

        return self._frame_counter_dict[camera_number].frame_number

    def reset_frame_number_by_camera_number(self, camera_number: int):
        if camera_number not in self._frame_counter_dict:
            raise ValueError(
                f'camera_number {camera_number} is not in frame_counter_dict')

        self._frame_counter_dict[camera_number].reset_frame_number()


class FrameNumberTracker:
    def __init__(self, frame_info: FrameInfo):
        if not isinstance(frame_info, FrameInfo):
            raise TypeError(
                f'frame_info type error. expected {FrameInfo}, got {type(frame_info)}')

        self._camera_number = frame_info.camera_number
        self._number_of_frames = frame_info.number_of_frames
        self._current_frame_number = 0

    @property
    def frame_number(self):
        return self._current_frame_number

    def increase_frame_number(self):
        self._current_frame_number += 1
        if self._current_frame_number > self._number_of_frames:
            self._current_frame_number = 1

    def reset_frame_number(self):
        self._current_frame_number = 0
