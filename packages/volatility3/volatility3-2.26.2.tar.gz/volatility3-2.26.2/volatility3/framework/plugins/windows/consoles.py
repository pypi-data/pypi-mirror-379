# This file is Copyright 2024 Volatility Foundation and licensed under the Volatility Software License 1.0
# which is available at https://www.volatilityfoundation.org/license/vsl-v1.0
#

# This module attempts to locate windows console histories.

import logging
import os
import struct
from typing import Tuple, Optional, Generator, Set, Dict, Any, Type, List

from volatility3.framework import interfaces, symbols, exceptions
from volatility3.framework import renderers
from volatility3.framework.interfaces import configuration
from volatility3.framework.configuration import requirements
from volatility3.framework.layers import scanners
from volatility3.framework.objects import utility
from volatility3.framework.renderers import format_hints
from volatility3.framework.symbols import intermed
from volatility3.framework.symbols.windows.extensions import pe, consoles
from volatility3.plugins.windows import pslist, info, verinfo
from volatility3.plugins.windows.registry import hivelist


vollog = logging.getLogger(__name__)


class Consoles(interfaces.plugins.PluginInterface):
    """Looks for Windows console buffers"""

    _required_framework_version = (2, 4, 0)

    # 2.0.0 - change the signature of `get_console_settings_from_registry`
    _version = (3, 0, 0)

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
                name="verinfo", component=verinfo.VerInfo, version=(1, 0, 0)
            ),
            requirements.VersionRequirement(
                name="info", component=info.Info, version=(2, 0, 0)
            ),
            requirements.VersionRequirement(
                name="hivelist", component=hivelist.HiveList, version=(2, 0, 0)
            ),
            requirements.VersionRequirement(
                name="bytes_scanner",
                component=scanners.BytesScanner,
                version=(1, 0, 0),
            ),
            requirements.BooleanRequirement(
                name="no_registry",
                description="Don't search the registry for possible values of CommandHistorySize and HistoryBufferMax",
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
            requirements.ListRequirement(
                name="max_buffers",
                element_type=int,
                description="HistoryBufferMax values to search for.",
                optional=True,
                default=[4],
            ),
        ]

    @classmethod
    def find_conhost_proc(
        cls, proc_list: Generator[interfaces.objects.ObjectInterface, None, None]
    ) -> Generator[Tuple[interfaces.objects.ObjectInterface, str], None, None]:
        """
        Walks the process list and returns the conhost instances.

        Args:
            proc_list: The process list generator

        Return:
            The process object and layer name for conhost
        """

        for proc in proc_list:
            if utility.array_to_string(proc.ImageFileName).lower() == "conhost.exe":
                proc_id = "Unknown"
                try:
                    proc_id = proc.UniqueProcessId
                    proc_layer_name = proc.add_process_layer()

                    yield proc, proc_layer_name

                except exceptions.InvalidAddressException as excp:
                    vollog.debug(
                        f"Process {proc_id}: invalid address {excp.invalid_address} in layer {excp.layer_name}"
                    )

    @classmethod
    def find_conhostexe(
        cls, conhost_proc: interfaces.objects.ObjectInterface
    ) -> Tuple[Optional[int], Optional[int]]:
        """
        Finds the base address of conhost.exe

        Args:
            conhost_proc: the process object for conhost.exe

        Returns:
            A tuple of:
            conhostexe_base: the base address of conhost.exe
            conhostexe_size: the size of the VAD for conhost.exe
        """
        for vad in conhost_proc.get_vad_root().traverse():
            filename = vad.get_file_name()
            if isinstance(filename, str) and filename.lower().endswith("conhost.exe"):
                base = vad.get_start()
                return base, vad.get_size()

        return None, None

    @classmethod
    def determine_conhost_version(
        cls,
        context: interfaces.context.ContextInterface,
        config_path: str,
        kernel_module_name: str,
        conhost_layer_name: str,
        conhost_base: int,
    ) -> Tuple[Optional[str], Dict[str, Type]]:
        """Tries to determine which symbol filename to use for the image's console information. This is similar to the
        netstat plugin.

        Args:
            context: The context to retrieve required elements (layers, symbol tables) from
            config_path: The config path where to find symbol files
            kernel_module_name: The name of the module for the kernel
            conhost_layer_name: The name of the conhot process memory layer
            conhost_base: the base address of conhost.exe

        Returns:
            The filename of the symbol table to use and the associated class types.
        """

        kernel = context.modules[kernel_module_name]

        is_64bit = symbols.symbol_table_is_64bit(
            context=context, symbol_table_name=kernel.symbol_table_name
        )

        if is_64bit:
            arch = "x64"
        else:
            arch = "x86"

        vers = info.Info.get_version_structure(context, kernel_module_name)

        kuser = info.Info.get_kuser_structure(context, kernel_module_name)

        try:
            vers_minor_version = int(vers.MinorVersion)
            nt_major_version = int(kuser.NtMajorVersion)
            nt_minor_version = int(kuser.NtMinorVersion)
        except ValueError:
            # vers struct exists, but is not an int anymore?
            raise NotImplementedError(
                "Kernel Debug Structure version format not supported!"
            )
        except Exception:
            # unsure what to raise here. Also, it might be useful to add some kind of fallback,
            # either to a user-provided version or to another method to determine conhost.exe's version
            raise exceptions.VolatilityException(
                "Kernel Debug Structure missing VERSION/KUSER structure, unable to determine Windows version!"
            )

        vollog.debug(
            f"Determined OS Version: {kuser.NtMajorVersion}.{kuser.NtMinorVersion} {vers.MajorVersion}.{vers.MinorVersion}"
        )

        if nt_major_version == 10 and arch == "x64":
            # win10 x64 has an additional class type we have to include.
            class_types = consoles.win10_x64_class_types
        else:
            # default to general class types
            class_types = consoles.class_types

        # these versions are listed explicitly because symbol files differ based on
        # version *and* architecture. this is currently the clearest way to show
        # the differences, even if it introduces a fair bit of redundancy.
        # furthermore, it is easy to append new versions.
        if arch == "x86":
            version_dict = {}
        else:
            version_dict = {
                (10, 0, 17763, 1): "consoles-win10-17763-x64",
                (10, 0, 17763, 3232): "consoles-win10-17763-3232-x64",
                (10, 0, 18362, 0): "consoles-win10-18362-x64",
                (10, 0, 19041, 0): "consoles-win10-19041-x64",
                (10, 0, 20348, 1): "consoles-win10-20348-x64",
                (10, 0, 20348, 1970): "consoles-win10-20348-1970-x64",
                (10, 0, 20348, 2461): "consoles-win10-20348-2461-x64",
                (10, 0, 20348, 2520): "consoles-win10-20348-2461-x64",
                (10, 0, 22000, 0): "consoles-win10-22000-x64",
                (10, 0, 22621, 1): "consoles-win10-22621-x64",
                (10, 0, 22621, 3527): "consoles-win10-22621-3527-x64",
                (10, 0, 25398, 0): "consoles-win10-22000-x64",
            }

        # we do not need to check for conhost's specific FileVersion in every case
        conhost_mod_version = 0  # keep it 0 as a default

        # we need to define additional version numbers (which are then found via conhost.exe's FileVersion header) in case there is
        # ambiguity _within_ an OS version. If such a version number (last number of the tuple) is defined for the current OS
        # we need to inspect conhost.exe's headers to see if we can grab the precise version
        if [
            (a, b, c, d)
            for a, b, c, d in version_dict
            if (a, b, c) == (nt_major_version, nt_minor_version, vers_minor_version)
            and d != 0
        ]:
            vollog.debug(
                "Requiring further version inspection due to OS version by checking conhost.exe's FileVersion header"
            )

            pe_table_name = intermed.IntermediateSymbolTable.create(
                context,
                configuration.path_join(config_path, "conhost"),
                "windows",
                "pe",
                class_types=pe.class_types,
            )

            try:
                (major, minor, product, build) = (
                    verinfo.VerInfo.get_version_information(
                        context, pe_table_name, conhost_layer_name, conhost_base
                    )
                )
                conhost_mod_version = build
                vollog.debug(
                    f"Found conhost.exe version {major}.{minor}.{product}.{build} in {conhost_layer_name} at base {conhost_base:#x}"
                )
            except (exceptions.InvalidAddressException, TypeError, AttributeError):
                # the following is IntelLayer specific and might need to be adapted to other architectures.
                physical_layer_name = context.layers[kernel.layer_name].config.get(
                    "memory_layer", None
                )
                if physical_layer_name:
                    ver = verinfo.VerInfo.find_version_info(
                        context, physical_layer_name, "CONHOST.EXE"
                    )

                    if ver:
                        conhost_mod_version = ver[3]
                        vollog.debug(
                            f"Determined conhost.exe's FileVersion: {conhost_mod_version}"
                        )
                    else:
                        vollog.debug("Could not determine conhost.exe's FileVersion.")
            else:
                vollog.debug(
                    "Unable to retrieve physical memory layer, skipping FileVersion check."
                )

        # when determining the symbol file we have to consider the following cases:
        # the determined version's symbol file is found by intermed.create -> proceed
        # the determined version's symbol file is not found by intermed -> intermed will throw an exc and abort
        # the determined version has no mapped symbol file -> if win10 use latest, otherwise throw exc
        # windows version cannot be determined -> throw exc

        filename = version_dict.get(
            (
                nt_major_version,
                nt_minor_version,
                vers_minor_version,
                conhost_mod_version,
            )
        )

        if not filename:
            # no match on filename means that we possibly have a version newer than those listed here.
            # try to grab the latest supported version of the current image NT version. If that symbol
            # version does not work, support has to be added manually.
            current_versions = [
                (nt_maj, nt_min, vers_min, conhost_ver)
                for nt_maj, nt_min, vers_min, conhost_ver in version_dict
                if nt_maj == nt_major_version
                and nt_min == nt_minor_version
                and vers_min <= vers_minor_version
                and conhost_ver <= conhost_mod_version
            ]
            current_versions.sort()

            if current_versions:
                latest_version = current_versions[-1]

                filename = version_dict.get(latest_version)

                vollog.debug(
                    f"Unable to find exact matching symbol file, going with latest: {filename}"
                )

            else:
                raise NotImplementedError(
                    f"This version of Windows is not supported: {nt_major_version}.{nt_minor_version} {vers.MajorVersion}.{vers_minor_version}!"
                )

        vollog.debug(f"Determined symbol filename: {filename}")

        return filename, class_types

    @classmethod
    def create_conhost_symbol_table(
        cls,
        context: interfaces.context.ContextInterface,
        config_path: str,
        kernel_module_name: str,
        conhost_layer_name: str,
        conhost_base: int,
    ) -> str:
        """Creates a symbol table for conhost structures.

        Args:
            context: The context to retrieve required elements (layers, symbol tables) from
            config_path: The config path where to find symbol files
            kernel_module_name: The name of the module of the kernel

        Returns:
            The name of the constructed symbol table
        """
        kernel = context.modules[kernel_module_name]

        table_mapping = {"nt_symbols": kernel.symbol_table_name}

        symbol_filename, class_types = cls.determine_conhost_version(
            context,
            config_path,
            kernel_module_name,
            conhost_layer_name,
            conhost_base,
        )

        if symbol_filename is None:
            raise ValueError(
                "Symbol filename could not be determined for conhost version"
            )

        vollog.debug(f"Using symbol file '{symbol_filename}' and types {class_types}")

        return intermed.IntermediateSymbolTable.create(
            context,
            configuration.path_join(config_path, "conhost"),
            os.path.join("windows", "consoles"),
            symbol_filename,
            class_types=class_types,
            table_mapping=table_mapping,
        )

    @classmethod
    def get_console_info(
        cls,
        context: interfaces.context.ContextInterface,
        config_path: str,
        kernel_module_name: str,
        procs: Generator[interfaces.objects.ObjectInterface, None, None],
        max_history: Set[int],
        max_buffers: Set[int],
    ) -> Generator[
        Tuple[
            interfaces.objects.ObjectInterface,
            Optional[interfaces.objects.ObjectInterface],
            List[Any],
        ],
        None,
        None,
    ]:
        """Gets the Console Information structure and its related properties for each conhost process

        Args:
            context: The context to retrieve required elements (layers, symbol tables) from
            config_path: The config path where to find symbol files
            kernel_module_name: The name of the module for the kernel
            procs: list of process objects
            max_history: an initial set of CommandHistorySize values
            max_buffers: an initial list of HistoryBufferMax values

        Returns:
            The conhost process object, the console information structure, a dictionary of properties for
            that console information structure.
        """

        conhost_symbol_table = None

        for conhost_proc, proc_layer_name in cls.find_conhost_proc(procs):
            if not conhost_proc:
                vollog.info(
                    "Unable to find a valid conhost.exe process in the process list. Analysis cannot proceed."
                )
                continue
            vollog.debug(
                f"Found conhost process {conhost_proc} with pid {conhost_proc.UniqueProcessId}"
            )

            conhostexe_base, conhostexe_size = cls.find_conhostexe(conhost_proc)
            if not conhostexe_base:
                vollog.info(
                    "Unable to find the location of conhost.exe. Analysis cannot proceed."
                )
                continue
            if conhostexe_size is None:
                vollog.info(
                    "Unable to determine the size of conhost.exe.  Analysis cannot proceed."
                )
                continue
            vollog.debug(f"Found conhost.exe base at {conhostexe_base:#x}")

            proc_layer = context.layers[proc_layer_name]

            if conhost_symbol_table is None:
                conhost_symbol_table = cls.create_conhost_symbol_table(
                    context,
                    config_path,
                    kernel_module_name,
                    proc_layer_name,
                    conhostexe_base,
                )

            conhost_module = context.module(
                conhost_symbol_table, proc_layer_name, offset=conhostexe_base
            )

            found_console_info_for_proc = False
            console_info = None
            # scan for potential _CONSOLE_INFORMATION structures by using the CommandHistorySize
            for max_history_value in max_history:
                max_history_bytes = struct.pack("H", max_history_value)
                vollog.debug(
                    f"Scanning for CommandHistorySize value: {max_history_bytes}"
                )
                for address in proc_layer.scan(
                    context,
                    scanners.BytesScanner(max_history_bytes),
                    sections=[(conhostexe_base, conhostexe_size)],
                ):
                    console_info = None
                    console_properties = []

                    try:
                        console_info = conhost_module.object(
                            "_CONSOLE_INFORMATION",
                            offset=address
                            - conhost_module.get_type(
                                "_CONSOLE_INFORMATION"
                            ).relative_child_offset("CommandHistorySize"),
                            absolute=True,
                        )

                        if not any(
                            [
                                console_info.is_valid(max_buffer)
                                for max_buffer in max_buffers
                            ]
                        ):
                            continue

                        vollog.debug(
                            f"Getting Console Information properties for {console_info}"
                        )
                        console_properties.append(
                            {
                                "level": 0,
                                "name": "_CONSOLE_INFORMATION",
                                "address": console_info.vol.offset,
                                "data": "",
                            }
                        )
                        console_properties.append(
                            {
                                "level": 1,
                                "name": "_CONSOLE_INFORMATION.ScreenX",
                                "address": console_info.ScreenX.vol.offset,
                                "data": console_info.ScreenX,
                            }
                        )
                        console_properties.append(
                            {
                                "level": 1,
                                "name": "_CONSOLE_INFORMATION.ScreenY",
                                "address": console_info.ScreenY.vol.offset,
                                "data": console_info.ScreenY,
                            }
                        )
                        console_properties.append(
                            {
                                "level": 1,
                                "name": "_CONSOLE_INFORMATION.CommandHistorySize",
                                "address": console_info.CommandHistorySize.vol.offset,
                                "data": console_info.CommandHistorySize,
                            }
                        )
                        console_properties.append(
                            {
                                "level": 1,
                                "name": "_CONSOLE_INFORMATION.HistoryBufferCount",
                                "address": console_info.HistoryBufferCount.vol.offset,
                                "data": console_info.HistoryBufferCount,
                            }
                        )
                        console_properties.append(
                            {
                                "level": 1,
                                "name": "_CONSOLE_INFORMATION.HistoryBufferMax",
                                "address": console_info.HistoryBufferMax.vol.offset,
                                "data": console_info.HistoryBufferMax,
                            }
                        )
                        console_properties.append(
                            {
                                "level": 1,
                                "name": "_CONSOLE_INFORMATION.Title",
                                "address": console_info.Title.vol.offset,
                                "data": console_info.get_title(),
                            }
                        )
                        console_properties.append(
                            {
                                "level": 1,
                                "name": "_CONSOLE_INFORMATION.OriginalTitle",
                                "address": console_info.OriginalTitle.vol.offset,
                                "data": console_info.get_original_title(),
                            }
                        )

                        vollog.debug(
                            f"Getting ConsoleProcessList entries for {console_info.ConsoleProcessList}"
                        )
                        console_properties.append(
                            {
                                "level": 1,
                                "name": "_CONSOLE_INFORMATION.ProcessCount",
                                "address": console_info.ProcessCount.vol.offset,
                                "data": console_info.ProcessCount,
                            }
                        )
                        console_properties.append(
                            {
                                "level": 1,
                                "name": "_CONSOLE_INFORMATION.ConsoleProcessList",
                                "address": console_info.ConsoleProcessList.vol.offset,
                                "data": "",
                            }
                        )
                        for index, attached_proc in enumerate(
                            console_info.get_processes()
                        ):
                            console_properties.append(
                                {
                                    "level": 2,
                                    "name": f"_CONSOLE_INFORMATION.ConsoleProcessList.ConsoleProcess_{index}",
                                    "address": attached_proc.ConsoleProcess.dereference().vol.offset,
                                    "data": "",
                                }
                            )
                            console_properties.append(
                                {
                                    "level": 2,
                                    "name": f"_CONSOLE_INFORMATION.ConsoleProcessList.ConsoleProcess_{index}_ProcessId",
                                    "address": attached_proc.ConsoleProcess.ProcessId.vol.offset,
                                    "data": attached_proc.ConsoleProcess.ProcessId,
                                }
                            )
                            console_properties.append(
                                {
                                    "level": 2,
                                    "name": f"_CONSOLE_INFORMATION.ConsoleProcessList.ConsoleProcess_{index}_ProcessHandle",
                                    "address": attached_proc.ConsoleProcess.ProcessHandle.vol.offset,
                                    "data": hex(
                                        attached_proc.ConsoleProcess.ProcessHandle
                                    ),
                                }
                            )

                        vollog.debug(
                            f"Getting ExeAliasList entries for {console_info.ExeAliasList}"
                        )
                        console_properties.append(
                            {
                                "level": 1,
                                "name": "_CONSOLE_INFORMATION.ExeAliasList",
                                "address": console_info.ExeAliasList.vol.offset,
                                "data": "",
                            }
                        )
                        if console_info.ExeAliasList:
                            for index, exe_alias_list in enumerate(
                                console_info.get_exe_aliases()
                            ):
                                try:
                                    console_properties.append(
                                        {
                                            "level": 2,
                                            "name": f"_CONSOLE_INFORMATION.ExeAliasList.AliasList_{index}",
                                            "address": exe_alias_list.vol.offset,
                                            "data": "",
                                        }
                                    )
                                    console_properties.append(
                                        {
                                            "level": 2,
                                            "name": f"_CONSOLE_INFORMATION.ExeAliasList.AliasList_{index}.ExeName",
                                            "address": exe_alias_list.ExeName.vol.offset,
                                            "data": exe_alias_list.get_exename(),
                                        }
                                    )
                                    for alias_index, alias in enumerate(
                                        exe_alias_list.get_aliases()
                                    ):
                                        console_properties.append(
                                            {
                                                "level": 3,
                                                "name": f"_CONSOLE_INFORMATION.ExeAliasList.AliasList_{index}.Alias_{alias_index}.Source",
                                                "address": alias.Source.vol.offset,
                                                "data": alias.get_source(),
                                            }
                                        )
                                        console_properties.append(
                                            {
                                                "level": 3,
                                                "name": f"_CONSOLE_INFORMATION.ExeAliasList.AliasList_{index}.Alias_{alias_index}.Target",
                                                "address": alias.Target.vol.offset,
                                                "data": alias.get_target(),
                                            }
                                        )
                                except Exception as e:
                                    vollog.debug(
                                        f"reading {exe_alias_list} encountered exception {e}"
                                    )

                        vollog.debug(
                            f"Getting HistoryList entries for {console_info.HistoryList}"
                        )
                        console_properties.append(
                            {
                                "level": 1,
                                "name": "_CONSOLE_INFORMATION.HistoryList",
                                "address": console_info.HistoryList.vol.offset,
                                "data": "",
                            }
                        )
                        for index, command_history in enumerate(
                            console_info.get_histories()
                        ):
                            try:
                                console_properties.append(
                                    {
                                        "level": 2,
                                        "name": f"_CONSOLE_INFORMATION.HistoryList.CommandHistory_{index}",
                                        "address": command_history.vol.offset,
                                        "data": "",
                                    }
                                )
                                console_properties.append(
                                    {
                                        "level": 2,
                                        "name": f"_CONSOLE_INFORMATION.HistoryList.CommandHistory_{index}_Application",
                                        "address": command_history.Application.vol.offset,
                                        "data": command_history.get_application(),
                                    }
                                )
                                console_properties.append(
                                    {
                                        "level": 2,
                                        "name": f"_CONSOLE_INFORMATION.HistoryList.CommandHistory_{index}_ProcessHandle",
                                        "address": command_history.ConsoleProcessHandle.ProcessHandle.vol.offset,
                                        "data": hex(
                                            command_history.ConsoleProcessHandle.ProcessHandle
                                        ),
                                    }
                                )
                                console_properties.append(
                                    {
                                        "level": 2,
                                        "name": f"_CONSOLE_INFORMATION.HistoryList.CommandHistory_{index}_CommandCount",
                                        "address": None,
                                        "data": command_history.CommandCount,
                                    }
                                )
                                console_properties.append(
                                    {
                                        "level": 2,
                                        "name": f"_CONSOLE_INFORMATION.HistoryList.CommandHistory_{index}_LastDisplayed",
                                        "address": command_history.LastDisplayed.vol.offset,
                                        "data": command_history.LastDisplayed,
                                    }
                                )
                                for (
                                    cmd_index,
                                    bucket_cmd,
                                ) in command_history.get_commands():
                                    try:
                                        console_properties.append(
                                            {
                                                "level": 3,
                                                "name": f"_CONSOLE_INFORMATION.HistoryList.CommandHistory_{index}_Command_{cmd_index}",
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

                        try:
                            vollog.debug(
                                f"Getting ScreenBuffer entries for {console_info}"
                            )
                            console_properties.append(
                                {
                                    "level": 1,
                                    "name": "_CONSOLE_INFORMATION.CurrentScreenBuffer",
                                    "address": console_info.CurrentScreenBuffer.vol.offset,
                                    "data": "",
                                }
                            )
                            for screen_index, screen_info in enumerate(
                                console_info.get_screens()
                            ):
                                try:
                                    console_properties.append(
                                        {
                                            "level": 2,
                                            "name": f"_CONSOLE_INFORMATION.ScreenBuffer_{screen_index}",
                                            "address": screen_info,
                                            "data": "",
                                        }
                                    )
                                    console_properties.append(
                                        {
                                            "level": 2,
                                            "name": f"_CONSOLE_INFORMATION.ScreenBuffer_{screen_index}.ScreenX",
                                            "address": None,
                                            "data": screen_info.ScreenX,
                                        }
                                    )
                                    console_properties.append(
                                        {
                                            "level": 2,
                                            "name": f"_CONSOLE_INFORMATION.ScreenBuffer_{screen_index}.ScreenY",
                                            "address": None,
                                            "data": screen_info.ScreenY,
                                        }
                                    )
                                    console_properties.append(
                                        {
                                            "level": 2,
                                            "name": f"_CONSOLE_INFORMATION.ScreenBuffer_{screen_index}.Dump",
                                            "address": None,
                                            "data": "\n".join(screen_info.get_buffer()),
                                        }
                                    )
                                except Exception as e:
                                    vollog.debug(
                                        f"reading {screen_info} encountered exception {e}"
                                    )
                        except Exception as e:
                            vollog.debug(
                                f"reading _CONSOLE_INFORMATION.CurrentScreenBuffer encountered exception {e}"
                            )

                    except exceptions.PagedInvalidAddressException as exp:
                        vollog.debug(
                            f"Required memory at {exp.invalid_address:#x} is not valid"
                        )
                        continue

                    if console_info and console_properties:
                        found_console_info_for_proc = True
                        yield conhost_proc, console_info, console_properties

            if not found_console_info_for_proc:
                yield conhost_proc, console_info or None, []

    @classmethod
    def get_console_settings_from_registry(
        cls,
        context: interfaces.context.ContextInterface,
        config_path: str,
        kernel_module_name: str,
        max_history: Set[int],
        max_buffers: Set[int],
    ) -> Tuple[Set[int], Set[int]]:
        """
        Walks the Registry user hives and extracts any CommandHistorySize and HistoryBufferMax values
        for scanning

        Args:
            context: The context to retrieve required elements (layers, symbol tables) from
            config_path: The config path where to find symbol files
            kernel_module_name: The name of the module for the kernel
            max_history: an initial set of CommandHistorySize values
            max_buffers: an initial list of HistoryBufferMax values

        Returns:
            The updated max_history and max_buffers sets.
        """
        vollog.debug(
            f"Possible CommandHistorySize values before checking Registry: {max_history}"
        )
        vollog.debug(
            f"Possible HistoryBufferMax values before checking Registry: {max_buffers}"
        )

        for hive in hivelist.HiveList.list_hives(
            context=context,
            base_config_path=config_path,
            kernel_module_name=kernel_module_name,
            hive_offsets=None,
        ):
            try:
                for value in hive.get_key("Console").get_values():
                    val_name = str(value.get_name())
                    if val_name == "HistoryBufferSize":
                        max_history.add(value.decode_data())
                    elif val_name == "NumberOfHistoryBuffers":
                        max_buffers.add(value.decode_data())
            except Exception:
                continue

        return max_history, max_buffers

    def _generator(
        self, procs: Generator[interfaces.objects.ObjectInterface, None, None]
    ):
        """
        Generates the console information to use in rendering

        Args:
            procs: the process list filtered to conhost.exe instances
        """

        max_history = set(self.config.get("max_history", [50]))
        max_buffers = set(self.config.get("max_buffers", [4]))
        no_registry = self.config.get("no_registry")

        if no_registry is False:
            max_history, max_buffers = self.get_console_settings_from_registry(
                self.context,
                self.config_path,
                self.config["kernel"],
                max_history,
                max_buffers,
            )

        vollog.debug(f"Possible CommandHistorySize values: {max_history}")
        vollog.debug(f"Possible HistoryBufferMax values: {max_buffers}")

        proc = None
        for proc, console_info, console_properties in self.get_console_info(
            self.context,
            self.config_path,
            self.config["kernel"],
            procs,
            max_history,
            max_buffers,
        ):
            process_name = utility.array_to_string(proc.ImageFileName)
            process_pid = proc.UniqueProcessId

            if console_info and console_properties:
                for console_property in console_properties:
                    yield (
                        console_property["level"],
                        (
                            process_pid,
                            process_name,
                            format_hints.Hex(console_info.vol.offset),
                            console_property["name"],
                            (
                                renderers.NotApplicableValue()
                                if console_property["address"] is None
                                else format_hints.Hex(console_property["address"])
                            ),
                            (
                                str(console_property["data"])
                                if console_property["data"]
                                else renderers.NotAvailableValue()
                            ),
                        ),
                    )
            else:
                yield (
                    0,
                    (
                        process_pid,
                        process_name,
                        (
                            format_hints.Hex(console_info.vol.offset)
                            if console_info
                            else renderers.NotApplicableValue()
                        ),
                        "_CONSOLE_INFORMATION",
                        renderers.NotApplicableValue(),
                        "Console Information Not Found",
                    ),
                )

        if proc is None:
            vollog.warn("No conhost.exe processes found.")

    def _conhost_proc_filter(self, proc: interfaces.objects.ObjectInterface) -> bool:
        """
        Used to filter to only conhost.exe processes
        """
        process_name = utility.array_to_string(proc.ImageFileName)

        return process_name.lower() != "conhost.exe"

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
