from ..action import ReportAction

class ReportActionBTSignal(ReportAction):
    """Warns when a low report rate is discovered and may impact usability."""

    def __init__(self, *args, **kwargs):
        super(ReportActionBTSignal, self).__init__(*args, **kwargs)

        # Check signal strength every 0.5 seconds
        self.timer_check = self.create_timer(0.5, self.check_signal)
        self.timer_reset = self.create_timer(5, self.reset_warning)

    def setup(self, device):
        self.reports = 0
        self.signal_warned = False

        if device.type == "bluetooth":
            self.enable()
        else:
            self.disable()

        # Get a handle on the action input that is actually sending the joy inputs to the local device
        self.action_input = None
        for i in self.controller.actions:
            try:
                x = i.enable_input
                self.action_input = i
                break
            except:
                pass

    def enable(self):
        self.timer_check.start()

    def disable(self):
        self.timer_check.stop()
        self.timer_reset.stop()

    def set_input_control(self, input_setting):
        if self.action_input:
            self.action_input.enable_input = input_setting

    def check_signal(self, report):
        rps = int(self.reports / 0.5)

        # If signal strength drops below 40%
        # Stop sending the messages it does receive and immediately publish zeroes
        # Roughly 250 reports/second normally
        if rps < 250 * 0.4:
            if not self.signal_warned:
                self.logger.warning("Signal strength is low ({0} reports/s)", rps)
                self.signal_warned = True
                self.timer_reset.start()
            self.set_input_control(False)
        else:
            self.set_input_control(True)

        self.reports = 0

        return True

    def reset_warning(self, report):
        self.signal_warned = False

    def handle_report(self, report):
        self.reports += 1
