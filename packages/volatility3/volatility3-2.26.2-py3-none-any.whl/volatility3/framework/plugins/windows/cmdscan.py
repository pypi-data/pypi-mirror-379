# This file is Copyright 2024 Volatility Foundation and licensed under the Volatility Software License 1.0
# which is available at https://www.volatilityfoundation.org/license/vsl-v1.0
#

# This module attempts to locate windows console histories.

import logging
import struct
from typing import Tuple, Generator, Set, Dict, Any, Optional

from volatility3.framework import interfaces
from volatility3.framework import renderers
from volatility3.framework.configuration import requirements
from volatility3.framework.layers import scanners
from volatility3.framework.objects import utility
from volatility3.framework.renderers import format_hints
from volatility3.plugins.windows import pslist, consoles


vollog = logging.getLogger(__name__)


class CmdScan(interfaces.plugins.PluginInterface):
    """Looks for Windows Command History lists"""

    _required_framework_version = (2, 4, 0)
    _version = (2, 0, 0)

    @classmethod
    def get_requirements(cls):
        # Since we're calling the plugin, make sure we have the plugin's requirements
        return [
            requirements.ModuleRequirement(
                name="kernel",
                description="Windows kernel",
                architectures=["Intel32", "Intel64"],
            ),
            requirements.VersionRequirement(
                name="pslist", component=pslist.PsList, version=(3, 0, 0)
            ),
            requirements.VersionRequirement(
                name="consoles", component=consoles.Consoles, version=(3, 0, 0)
            ),
            requirements.VersionRequirement(
                name="bytes_scanner",
                component=scanners.BytesScanner,
                version=(1, 0, 0),
            ),
            requirements.BooleanRequirement(
                name="no_registry",
                description="Don't search the registry for possible values of CommandHistorySize",
                optional=True,
                default=False,
            ),
            requirements.ListRequirement(
                name="max_history",
                element_type=int,
                description="CommandHistorySize values to search for.",
                optional=True,
                default=[50],
            ),
        ]

    @classmethod
    def get_filtered_vads(
        cls,
        conhost_proc: interfaces.context.ContextInterface,
        size_filter: Optional[int] = 0x40000000,
    ) -> Generator[Tuple[int, int], None, None]:
        """
        Returns vads of a process with size smaller than size_filter

        Args:
            conhost_proc: the process object for conhost.exe
            size_filter: size above which vads will not be returned

        Returns:
            A list of tuples of:
            vad_base: the base address
            vad_size: the size of the VAD
        """
        for vad in conhost_proc.get_vad_root().traverse():
            base = vad.get_start()
            if vad.get_size() < size_filter:
                yield (base, vad.get_size())

    @classmethod
    def get_command_history(
        cls,
        context: interfaces.context.ContextInterface,
        config_path: str,
        kernel_module_name: str,
        procs: Generator[interfaces.objects.ObjectInterface, None, None],
        max_history: Set[int],
    ) -> Tuple[
        interfaces.context.ContextInterface,
        interfaces.context.ContextInterface,
        Dict[str, Any],
    ]:
        """Gets the list of commands from each Command History structure

        Args:
            context: The context to retrieve required elements (layers, symbol tables) from
            config_path: The config path where to find symbol files
            procs: List of process objects
            max_history: An initial set of CommandHistorySize values

        Returns:
            The conhost process object, the command history structure, a dictionary of properties for
            that command history structure.
        """

        conhost_symbol_table = None

        for conhost_proc, proc_layer_name in consoles.Consoles.find_conhost_proc(procs):
            if not conhost_proc:
                vollog.info(
                    "Unable to find a valid conhost.exe process in the process list. Analysis cannot proceed."
                )
                continue
            vollog.debug(
                f"Found conhost process {conhost_proc} with pid {conhost_proc.UniqueProcessId}"
            )

            conhostexe_base, conhostexe_size = consoles.Consoles.find_conhostexe(
                conhost_proc
            )
            if not conhostexe_base:
                vollog.info(
                    "Unable to find the location of conhost.exe. Analysis cannot proceed."
                )
                continue
            vollog.debug(f"Found conhost.exe base at {conhostexe_base:#x}")

            proc_layer = context.layers[proc_layer_name]

            if conhost_symbol_table is None:
                conhost_symbol_table = consoles.Consoles.create_conhost_symbol_table(
                    context,
                    config_path,
                    kernel_module_name,
                    proc_layer_name,
                    conhostexe_base,
                )

            conhost_module = context.module(
                conhost_symbol_table, proc_layer_name, offset=conhostexe_base
            )
            command_count_max_offset = conhost_module.get_type(
                "_COMMAND_HISTORY"
            ).relative_child_offset("CommandCountMax")

            sections = cls.get_filtered_vads(conhost_proc)
            found_history_for_proc = False
            # scan for potential _COMMAND_HISTORY structures by using the CommandHistorySize
            for max_history_value in max_history:
                max_history_bytes = struct.pack("H", max_history_value)
                vollog.debug(
                    f"Scanning for CommandHistorySize value: {max_history_bytes}"
                )
                for address in proc_layer.scan(
                    context,
                    scanners.BytesScanner(max_history_bytes),
                    sections=sections,
                ):
                    command_history = None
                    command_history_properties = []

                    try:
                        command_history = conhost_module.object(
                            "_COMMAND_HISTORY",
                            offset=address - command_count_max_offset,
                            absolute=True,
                        )

                        if not command_history.is_valid(max_history_value):
                            continue

                        vollog.debug(
                            f"Getting Command History properties for {command_history}"
                        )
                        command_history_properties.append(
                            {
                                "level": 0,
                                "name": "_COMMAND_HISTORY",
                                "address": command_history.vol.offset,
                                "data": None,
                            }
                        )
                        command_history_properties.append(
                            {
                                "level": 1,
                                "name": "_COMMAND_HISTORY.Application",
                                "address": command_history.Application.vol.offset,
                                "data": command_history.get_application(),
                            }
                        )
                        command_history_properties.append(
                            {
                                "level": 1,
                                "name": "_COMMAND_HISTORY.ProcessHandle",
                                "address": command_history.ConsoleProcessHandle.ProcessHandle.vol.offset,
                                "data": hex(
                                    command_history.ConsoleProcessHandle.ProcessHandle
                                ),
                            }
                        )
                        command_history_properties.append(
                            {
                                "level": 1,
                                "name": "_COMMAND_HISTORY.CommandCount",
                                "address": None,
                                "data": command_history.CommandCount,
                            }
                        )
                        command_history_properties.append(
                            {
                                "level": 1,
                                "name": "_COMMAND_HISTORY.LastDisplayed",
                                "address": command_history.LastDisplayed.vol.offset,
                                "data": command_history.LastDisplayed,
                            }
                        )
                        command_history_properties.append(
                            {
                                "level": 1,
                                "name": "_COMMAND_HISTORY.CommandCountMax",
                                "address": command_history.CommandCountMax.vol.offset,
                                "data": command_history.CommandCountMax,
                            }
                        )
                        command_history_properties.append(
                            {
                                "level": 1,
                                "name": "_COMMAND_HISTORY.CommandBucket",
                                "address": command_history.CommandBucket.vol.offset,
                                "data": "",
                            }
                        )

                        for (
                            cmd_index,
                            bucket_cmd,
                        ) in command_history.scan_command_bucket():
                            try:
                                command_history_properties.append(
                                    {
                                        "level": 2,
                                        "name": f"_COMMAND_HISTORY.CommandBucket_Command_{cmd_index}",
                                        "address": bucket_cmd.vol.offset,
                                        "data": bucket_cmd.get_command_string(),
                                    }
                                )
                            except Exception as e:
                                vollog.debug(
                                    f"reading {bucket_cmd} encountered exception {e}"
                                )
                    except Exception as e:
                        vollog.debug(
                            f"reading {command_history} encountered exception {e}"
                        )

                    if command_history and command_history_properties:
                        found_history_for_proc = True
                        yield conhost_proc, command_history, command_history_properties

            # if found_history_for_proc is still False, then none of the scanned locations found
            # a valid _COMMAND_HISTORY for the process, so yield the process and some empty data
            # so the process can at least be reported that it was found with no history
            if not found_history_for_proc:
                yield conhost_proc, command_history or None, []

    def _generator(
        self, procs: Generator[interfaces.objects.ObjectInterface, None, None]
    ):
        """
        Generates the command history to use in rendering

        Args:
            procs: the process list filtered to conhost.exe instances
        """

        max_history = set(self.config.get("max_history", [50]))
        no_registry = self.config.get("no_registry")

        if no_registry is False:
            max_history, _ = consoles.Consoles.get_console_settings_from_registry(
                context=self.context,
                config_path=self.config_path,
                kernel_module_name=self.config["kernel"],
                max_history=max_history,
                max_buffers=[],
            )

        vollog.debug(f"Possible CommandHistorySize values: {max_history}")

        proc = None
        for (
            proc,
            command_history,
            command_history_properties,
        ) in self.get_command_history(
            self.context,
            self.config_path,
            self.config["kernel"],
            procs,
            max_history,
        ):
            process_name = utility.array_to_string(proc.ImageFileName)
            process_pid = proc.UniqueProcessId

            if command_history and command_history_properties:
                for command_history_property in command_history_properties:
                    yield (
                        command_history_property["level"],
                        (
                            process_pid,
                            process_name,
                            format_hints.Hex(command_history.vol.offset),
                            command_history_property["name"],
                            (
                                renderers.NotApplicableValue()
                                if command_history_property["address"] is None
                                else format_hints.Hex(
                                    command_history_property["address"]
                                )
                            ),
                            str(command_history_property["data"]),
                        ),
                    )
            else:
                yield (
                    0,
                    (
                        process_pid,
                        process_name,
                        (
                            format_hints.Hex(command_history.vol.offset)
                            if command_history
                            else renderers.NotApplicableValue()
                        ),
                        "_COMMAND_HISTORY",
                        renderers.NotApplicableValue(),
                        "History Not Found",
                    ),
                )

        if proc is None:
            vollog.warn("No conhost.exe processes found.")

    def _conhost_proc_filter(self, proc: interfaces.objects.ObjectInterface):
        """
        Used to filter only conhost.exe processes
        """
        process_name = utility.array_to_string(proc.ImageFileName)

        return process_name != "conhost.exe"

    def run(self):
        return renderers.TreeGrid(
            [
                ("PID", int),
                ("Process", str),
                ("ConsoleInfo", format_hints.Hex),
                ("Property", str),
                ("Address", format_hints.Hex),
                ("Data", str),
            ],
            self._generator(
                pslist.PsList.list_processes(
                    context=self.context,
                    kernel_module_name=self.config["kernel"],
                    filter_func=self._conhost_proc_filter,
                )
            ),
        )
