import click

from adam.commands.command import Command
from adam.commands.deploy.undeploy_frontend import UndeployFrontend
from adam.commands.deploy.undeploy_pg_agent import UndeployPgAgent
from adam.commands.deploy.undeploy_pod import UndeployPod
from adam.repl_state import ReplState
from adam.utils import lines_to_tabular, log, log2

class Undeploy(Command):
    COMMAND = 'undeploy'
    reaper_login = None

    # the singleton pattern
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'): cls.instance = super(Undeploy, cls).__new__(cls)

        return cls.instance

    def __init__(self, successor: Command=None):
        super().__init__(successor)

    def command(self):
        return Undeploy.COMMAND

    def run(self, cmd: str, state: ReplState):
        if not(args := self.args(cmd)):
            return super().run(cmd, state)

        state, args = self.apply_state(args, state)

        if state.in_repl:
            log(lines_to_tabular([c.help(ReplState()) for c in Undeploy.cmd_list()], separator='\t'))

            return 'command-missing'
        else:
            # head with the Chain of Responsibility pattern
            cmds = Command.chain(Undeploy.cmd_list())
            if not cmds.run(cmd, state):
                log2('* Command is missing.')
                Command.display_help()

    def cmd_list():
        return [UndeployFrontend(), UndeployPod(), UndeployPgAgent()]

    def completion(self, state: ReplState):
        if state.sts:
            return super().completion(state)

        return {}

    def help(self, _: ReplState):
        return None

class UndeployCommandHelper(click.Command):
    def get_help(self, ctx: click.Context):
        log(super().get_help(ctx))
        log()
        log('Sub-Commands:')

        log(lines_to_tabular([c.help(ReplState()).replace(f'{Undeploy.COMMAND} ', '  ', 1) for c in Undeploy.cmd_list()], separator='\t'))