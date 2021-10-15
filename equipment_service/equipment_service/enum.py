import enum


class StatusEnum(str, enum.Enum):
    def __init__(self, status):
        self.status = status


class EquipmentState(StatusEnum):
    activate = "activate"
    deactivate = "deactivate"
    remove = "remove"

    @classmethod
    def choices(cls):
        return [(i.name, i.value) for i in cls]
