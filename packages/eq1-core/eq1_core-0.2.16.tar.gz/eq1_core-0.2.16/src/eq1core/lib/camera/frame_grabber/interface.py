import abc


class CommonLineScanCameraInterface(abc.ABC):
    def __init__(self):
        pass

    @property
    @abc.abstractmethod
    def camera_serial_number(self):
        pass

    @property
    @abc.abstractmethod
    def frame_number(self):
        pass

    @abc.abstractmethod
    def open(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass

    @abc.abstractmethod
    def get_frame(self):
        pass

    @abc.abstractmethod
    def start_acquisition(self):
        pass

    @abc.abstractmethod
    def stop_acquisition(self):
        pass

    @abc.abstractmethod
    def on_acquisition(self):
        pass

    @abc.abstractmethod
    def set_interface_camera_type(self, camera_type: int = 0) -> bool:
        pass

    @abc.abstractmethod
    def get_interface_camera_type(self):
        pass

    @abc.abstractmethod
    def set_device_image_width(self, width: int) -> bool:
        pass

    @abc.abstractmethod
    def set_device_image_height(self, height: int) -> bool:
        pass

    @abc.abstractmethod
    def execute_stream_software_trigger(self, *args, **kwargs) -> bool:
        pass

    @abc.abstractmethod
    def is_connected(self) -> bool:
        pass

    @abc.abstractmethod
    def delete(self):
        pass