"""
-----------------------------------------------------------------------
File: utils/helper_functions.py
Creation Time: Aug 13th 2025, 11:39 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2025 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
"""

import time


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        func_run_log = (
            f"Function {func.__name__} took {execution_time:.4f} seconds to execute"
        )
        print(func_run_log)
        # if 'is_st' in kwargs and kwargs['is_st']:
        #     st.write(func_run_log)

        return result

    return wrapper
