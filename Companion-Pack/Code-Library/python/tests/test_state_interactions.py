import unittest
from asteria_code import InteractionRouter, StateMachine

class StateInteractionTests(unittest.TestCase):
    def test_state_machine(self):
        machine = StateMachine("idle")
        machine.add_transition("idle", "start", "active")
        self.assertTrue(machine.can_trigger("start"))
        transition = machine.trigger("start")
        self.assertEqual((transition.source, transition.target), ("idle", "active"))
        self.assertIsNone(machine.trigger("missing"))
        self.assertEqual(machine.current_state, "active")

    def test_interaction_router(self):
        router = InteractionRouter()
        router.register("double", lambda value: value * 2)
        self.assertEqual(router.dispatch("double", 4).value, 8)
        self.assertEqual(router.dispatch("missing").error_code, "unknown_action")

    def test_handler_error_is_bounded(self):
        router = InteractionRouter()
        router.register("boom", lambda _: 1 / 0)
        self.assertEqual(router.dispatch("boom").error_code, "handler_error:ZeroDivisionError")
