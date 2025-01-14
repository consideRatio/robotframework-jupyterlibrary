from doit.reporter import ConsoleReporter

from datetime import datetime

from . import project as P


START = "::group::" if P.CI else ""
END = "::endgroup::" if P.CI else ""

TIMEFMT = "%H:%M:%S"
SKIP = "--------"


class GithubActionsReporter(ConsoleReporter):
    _gh_timings = {}

    def execute_task(self, task):
        start = datetime.now()
        title = task.title()
        self._gh_timings[title] = [start]
        self.outstream.write(f"""{START}[{start.strftime(TIMEFMT)}] 🎢  {title}\n""")

    def gh_outtro(self, task, emoji):
        title = task.title()
        try:
            sec = "??"
            start, end = self._gh_timings[title] = [
                *self._gh_timings[title],
                datetime.now(),
            ]
            delta = end - start
            sec = str(delta.seconds).rjust(7)
        except:
            pass
        self.outstream.write(f"{END}\n[{sec}s] {emoji} {task.title()} {emoji}\n")

    def add_failure(self, task, exception):
        super().add_failure(task, exception)
        self.gh_outtro(task, "⭕")

    def add_success(self, task):
        super().add_success(task)
        self.gh_outtro(task, "🏁 ")

    def skip_uptodate(self, task):
        self.outstream.write(f"{START}[{SKIP}] ⏩  {task.title()}{END}\n")

    skip_ignore = skip_uptodate
