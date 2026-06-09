class Image:
    # --- Constructor ---
    def __init__(self) -> None:
        self.__route = ""
        self.__weight = 0
        self.__height = 0
        self.__channels = 0

    # =============================
    #       GETTERS Y SETTERS
    # =============================

    @property
    def route(self) -> str:
        return self.__route

    @route.setter
    def route(self, route: str) -> None:
        self.__route = route

    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int) -> None:
        self.__weight = weight

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int) -> None:
        self.__height = height

    @property
    def channels(self) -> int:
        return self.__channels

    @channels.setter
    def channels(self, channels: int) -> None:
        self.__channels = channels
