import sys
import importlib
from concurrent.futures import ThreadPoolExecutor
from types import ModuleType
from typing import Any, List, Callable
from tqdm import tqdm

import modules
import modules.globals                   

FRAME_PROCESSORS_MODULES: List[ModuleType] = []
FRAME_PROCESSORS_INTERFACE = [
    'pre_check',
    'pre_start',
    'process_frame',
    'process_image',
    'process_video'
]


def load_frame_processor_module(frame_processor: str) -> Any:
    print(f"\033[34m Debug: load_frame_processor_module function called for frame_processor: {frame_processor} \033[0m") # Debug: Function entry
    try:
        print(f"\033[34m Debug: Attempting to import module: modules.processors.frame.{frame_processor} \033[0m") # Debug: Module import attempt
        frame_processor_module = importlib.import_module(f'modules.processors.frame.{frame_processor}')
        print(f"\033[34m Debug: Successfully imported module: {frame_processor_module} \033[0m") # Debug: Module import success
        for method_name in FRAME_PROCESSORS_INTERFACE:
            if not hasattr(frame_processor_module, method_name):
                print(f"\033[34m Debug: Module {frame_processor_module} does not have method: {method_name}. Exiting. \033[0m") # Debug: Missing method
                sys.exit()
        print(f"\033[34m Debug: Module {frame_processor_module} passed interface check. \033[0m") # Debug: Interface check passed
    except ImportError:
        print(f"\033[34m Debug: ImportError occurred while loading frame processor {frame_processor}. \033[0m") # Debug: ImportError
        print(f"Frame processor {frame_processor} not found")
        sys.exit()
    print(f"\033[34m Debug: Returning loaded module: {frame_processor_module} \033[0m") # Debug: Function return
    return frame_processor_module


def get_frame_processors_modules(frame_processors: List[str]) -> List[ModuleType]:
    global FRAME_PROCESSORS_MODULES

    print("\033[31;32m Debug: get_frame_processors_modules function called with frame_processors:", frame_processors, "\033[0m") # Debug: Indicate function call and input
    if not FRAME_PROCESSORS_MODULES:
        print("\033[31;32m Debug: FRAME_PROCESSORS_MODULES is empty, loading modules. \033[0m") # Debug: Indicate modules are being loaded
        for frame_processor in frame_processors:
            print("\033[31;32m Debug: Loading frame processor module:", frame_processor, "\033[0m") # Debug: Indicate which module is being loaded
            frame_processor_module = load_frame_processor_module(frame_processor)
            print("\033[31;32m Debug: Loaded frame processor module:", frame_processor_module, "\033[0m") # Debug: Indicate loaded module
            FRAME_PROCESSORS_MODULES.append(frame_processor_module)
        print("\033[31;32m Debug: Finished loading frame processor modules. \033[0m") # Debug: Indicate module loading finished
    else:
        print("\033[31;32m Debug: FRAME_PROCESSORS_MODULES is not empty, skipping module loading. \033[0m") # Debug: Indicate modules are already loaded

    print("\033[31;32m Debug: Calling set_frame_processors_modules_from_ui with frame_processors:", frame_processors, "\033[0m") # Debug: Indicate calling set_frame_processors_modules_from_ui
    print("\033[31;32m Debug: frame_processors: ", frame_processors  , "\033[0m") # Debug: Indicate set_frame_processors_modules_from_ui finished
    set_frame_processors_modules_from_ui(frame_processors)
    print("\033[31;32m Debug: set_frame_processors_modules_from_ui call finished. \033[0m") # Debug: Indicate set_frame_processors_modules_from_ui finished
    print("\033[31;32m Debug: Returning FRAME_PROCESSORS_MODULES:", FRAME_PROCESSORS_MODULES, "\033[0m") # Debug: Indicate return value
    return FRAME_PROCESSORS_MODULES

def set_frame_processors_modules_from_ui(frame_processors: List[str]) -> None:
    global FRAME_PROCESSORS_MODULES
    print("\033[33m Debug: set_frame_processors_modules_from_ui function called with frame_processors:", frame_processors, "\033[0m") # Debug: Function entry
    print("\033[33m Debug: modules.globals.fp_ui:", modules.globals.fp_ui, "\033[0m") # Debug: Print fp_ui content
    for frame_processor, state in modules.globals.fp_ui.items():
        print(f"\033[33m Debug: Processing frame_processor: {frame_processor}, state: {state} \033[0m") # Debug: Iteration info
        if state == True and frame_processor not in frame_processors:
            print(f"\033[33m Debug: State is True and frame_processor '{frame_processor}' not in frame_processors. Loading module. \033[0m") # Debug: Condition True for loading
            frame_processor_module = load_frame_processor_module(frame_processor)
            print(f"\033[33m Debug: Loaded module: {frame_processor_module}. Appending to FRAME_PROCESSORS_MODULES and modules.globals.frame_processors. \033[0m") # Debug: Module loaded
            FRAME_PROCESSORS_MODULES.append(frame_processor_module)
            modules.globals.frame_processors.append(frame_processor)
        if state == False:
            print(f"\033[33m Debug: State is False for frame_processor '{frame_processor}'. Attempting to remove module. \033[0m") # Debug: State False - removal attempt
            try:
                frame_processor_module = load_frame_processor_module(frame_processor)
                print(f"\033[33m Debug: Loaded module for removal: {frame_processor_module}. Removing from FRAME_PROCESSORS_MODULES and modules.globals.frame_processors. \033[0m") # Debug: Module loaded for removal
                FRAME_PROCESSORS_MODULES.remove(frame_processor_module)
                modules.globals.frame_processors.remove(frame_processor)
                print(f"\033[33m Debug: Successfully removed module and frame processor '{frame_processor}'. \033[0m") # Debug: Removal success
            except Exception as e:
                print(f"\033[33m Debug: Error removing module for '{frame_processor}': {e} \033[0m") # Debug: Removal error
                pass
    print("\033[33m Debug: set_frame_processors_modules_from_ui function finished. \033[0m") # Debug: Function finish

def multi_process_frame(source_path: str, temp_frame_paths: List[str], process_frames: Callable[[str, List[str], Any], None], progress: Any = None) -> None:
    with ThreadPoolExecutor(max_workers=modules.globals.execution_threads) as executor:
        futures = []
        for path in temp_frame_paths:
            future = executor.submit(process_frames, source_path, [path], progress)
            futures.append(future)
        for future in futures:
            future.result()


def process_video(source_path: str, frame_paths: list[str], process_frames: Callable[[str, List[str], Any], None]) -> None:
    progress_bar_format = '{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]'
    total = len(frame_paths)
    with tqdm(total=total, desc='Processing', unit='frame', dynamic_ncols=True, bar_format=progress_bar_format) as progress:
        progress.set_postfix({'execution_providers': modules.globals.execution_providers, 'execution_threads': modules.globals.execution_threads, 'max_memory': modules.globals.max_memory})
        multi_process_frame(source_path, frame_paths, process_frames, progress)
