extends Node

func _ready() -> void:
    var machine := StateMachine.new("idle")
    machine.add_transition("idle", "start", "active")
    var transition := machine.trigger("start")
    print("CP-CODE-BOOTSTRAP-001 state=", transition.target)
