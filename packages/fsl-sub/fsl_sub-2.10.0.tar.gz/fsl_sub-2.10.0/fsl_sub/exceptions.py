# fsl_sub python module
# Copyright (c) 2018-2021 University of Oxford (Duncan Mortimer)


class BadOS(Exception):
    pass


class ArgumentError(Exception):
    pass


class LoadModuleError(Exception):
    pass


class NoModule(Exception):
    pass


class PluginError(Exception):
    pass


class BadCoprocessor(Exception):
    pass


class BadConfiguration(Exception):
    pass


class MissingConfiguration(Exception):
    pass


class UnrecognisedModule(Exception):
    pass


class BadSubmission(Exception):
    pass


class GridOutputError(Exception):
    pass


class CommandError(Exception):
    pass


class ShellBadSubmission(BadSubmission):
    def __init__(self, message, rc):
        super(ShellBadSubmission, self).__init__(message)
        self.rc = rc


class UnknownJobId(Exception):
    pass


class NotAFslDir(Exception):
    pass


class NoFsl(Exception):
    pass


class NoCondaEnvFile(Exception):
    pass


class NoChannelFound(Exception):
    pass


class UpdateError(Exception):
    pass


class NoCondaEnv(Exception):
    pass


class PackageError(Exception):
    pass


class InstallError(Exception):
    pass


CONFIG_ERROR = 1
SUBMISSION_ERROR = 2
RUNNER_ERROR = 3
