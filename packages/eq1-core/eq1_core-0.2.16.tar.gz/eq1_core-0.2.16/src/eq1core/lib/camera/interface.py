import abc


class CameraInterface(abc.ABC):
    @abc.abstractmethod
    def create(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def open(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def is_open(self):
        pass

    @abc.abstractmethod
    def close(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_trigger_mode(self):
        pass

    @abc.abstractmethod
    def get_trigger_source(self):
        pass

    @abc.abstractmethod
    def set_trigger_mode(self, mode: int):
        pass

    @abc.abstractmethod
    def set_trigger_source(self, source: int):
        pass

    @abc.abstractmethod
    def set_trigger_mode_on(self):
        pass

    @abc.abstractmethod
    def set_trigger_mode_off(self):
        pass

    @abc.abstractmethod
    def set_trigger_source_hardware(self):
        pass

    @abc.abstractmethod
    def set_trigger_source_software(self):
        pass

    @abc.abstractmethod
    def set_exposure_time(self, time_us: float):
        pass

    @abc.abstractmethod
    def set_pixel_format_mono(self):
        pass

    @abc.abstractmethod
    def set_pixel_format_rgb(self):
        pass

    @abc.abstractmethod
    def get_frame(self):
        pass
