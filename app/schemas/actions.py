from enum import Enum


class Action(Enum):
    search = "search"
    select = "select"
    init = "init"
    confirm = "confirm"
    update = "update"
    status = "status"
    track = "track"
    cancel = "cancel"
    rating = "rating"
    support = "support"
    on_search = "on_search"
    on_select = "on_select"
    on_init = "on_init"
    on_confirm = "on_confirm"
    on_update = "on_update"
    on_status = "on_status"
    on_track = "on_track"
    on_cancel = "on_cancel"
    on_rating = "on_rating"
    on_support = "on_support"


class Domain(Enum):
    RETAIL = "retail"
    LOGISTICS = "logistics"
