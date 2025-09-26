import itertools
import platform
import time
import types
from typing import Any, Dict, Iterable, Mapping, Optional

from ..collectors.performance import PerformanceMonitor
from ..config import config
from ..flow_metrics import EndpointMetric
from ..investigation_manager import (
    safe_get_cpu_usage,
)
from ..native import RawInvestigation, set_investigation
from ..schemas.investigation import (
    HttpInvestigationContext,
    Investigation,
    InvestigationExceptionInfo,
    MachineMetrics,
    ObservabilityIdentifiers,
    SystemInfo,
)
from .limited_logger import limited_logger

total_investigations: int = 0
investigation_dedup: Dict[str, Dict[str, int]] = (
    dict()
)  # investigation_dedup[flow_id][dedup_key] = count


def open_investigation() -> Optional[RawInvestigation]:
    if not config.enable_investigation:
        return None

    raw_investigation = RawInvestigation(round(time.time() * 1000))
    set_investigation(raw_investigation)
    return raw_investigation


def reset_max_investigations() -> None:
    global total_investigations
    total_investigations = 0


def reset_investigation_dedup() -> None:
    global investigation_dedup
    investigation_dedup = dict()


def get_investigation_dedup_key(first_exception: Exception) -> str:
    key: str = f"{first_exception.__class__.__name__}"
    if first_exception.__traceback__ is not None:
        key += f":{first_exception.__traceback__.tb_frame.f_code.co_filename}:{first_exception.__traceback__.tb_frame.f_lineno}"

    return key


def minimize_object_with_defaults(
    obj: Any,
) -> Any:
    return minimize_object(
        obj,
        config.investigation_max_object_depth,
        config.investigation_max_string_length,
        config.investigation_max_array_length,
        config.investigation_max_dict_length,
    )


def minimize_object(
    obj: Any,
    max_depth: int,
    max_string_length: int,
    max_array_length: int,
    max_dict_length: int,
) -> Any:
    try:
        if obj is None or isinstance(obj, (int, float, bool, complex)):
            return obj

        if isinstance(obj, str):
            return obj[:max_string_length]

        if max_depth < 0:
            return None

        if isinstance(obj, dict):
            return {
                minimize_object(
                    key,
                    max_depth - 1,
                    max_string_length,
                    max_array_length,
                    max_dict_length,
                ): minimize_object(
                    value,
                    max_depth - 1,
                    max_string_length,
                    max_array_length,
                    max_dict_length,
                )
                for key, value in itertools.islice(obj.items(), max_dict_length)
            }

        if isinstance(obj, types.GeneratorType):
            return None

        # Both dict and generator are iterable which we don't want to slice with `itertools.islice` since:
        # 1. Itertating through dict will return just the keys and not the values
        # 2. Iterating through generator will change it internal state
        if isinstance(obj, Iterable):
            return [
                minimize_object(
                    item,
                    max_depth - 1,
                    max_string_length,
                    max_array_length,
                    max_dict_length,
                )
                for item in itertools.islice(obj, max_array_length)
            ]

    except Exception:
        pass

    # Drop anythig else including functions, Classes, etc
    return None


def minimize_exception_info_in_place(
    exception_info: InvestigationExceptionInfo,
) -> InvestigationExceptionInfo:
    exception_info.message = minimize_object_with_defaults(exception_info.message)
    return exception_info


def get_pod_name() -> Optional[str]:
    try:
        return platform.node()
    except Exception:
        return None


def get_node_name() -> Optional[str]:
    try:
        with open("/etc/machine-id", "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return None


def get_system_info() -> SystemInfo:
    return SystemInfo(
        pod_name=get_pod_name(),
        node_name=get_node_name(),
    )


def get_machine_metrics() -> Optional[MachineMetrics]:
    try:
        return MachineMetrics(
            cpu=safe_get_cpu_usage(),
            memory=PerformanceMonitor.get_memory_usage(),
            threads_count=PerformanceMonitor.get_thread_count(),
        )
    except Exception:
        limited_logger.log("Error getting machine metrics", exc_info=True)
        return None


def finish_base_http_investigation(
    raw_investigation: RawInvestigation,
    metric: Optional[EndpointMetric],
    path: Optional[str],
    apm_trace_ids: Optional[ObservabilityIdentifiers],
) -> Optional[Investigation]:
    if metric is None:
        return None

    if metric.status_code is None:
        return None

    if metric.status_code < 500:
        return None

    if raw_investigation.first_exception is None:
        limited_logger.log("No exception in investigation")
        return None

    if metric.flow_id is None:
        limited_logger.log("No flow id in metric")
        return None

    if total_investigations >= config.max_investigations:
        limited_logger.log("Max investigations reached")
        return None

    if investigation_dedup.get(metric.flow_id) is None:
        investigation_dedup[metric.flow_id] = dict()

    key = get_investigation_dedup_key(raw_investigation.first_exception)
    if investigation_dedup[metric.flow_id].get(key) is None:
        investigation_dedup[metric.flow_id][key] = 0

    if investigation_dedup[metric.flow_id][key] >= config.max_same_investigation:
        limited_logger.log("Max same investigation reached")
        return None

    investigation_dedup[metric.flow_id][key] += 1

    return Investigation(
        exceptions=[
            minimize_exception_info_in_place(
                InvestigationExceptionInfo(exception, execution_flow)
            )
            for exception, execution_flow in raw_investigation.exceptions.items()
        ],
        context=HttpInvestigationContext(
            status_code=metric.status_code,
            route=path or "unknown",
            method=metric.method or "unknown",
            timestamp=raw_investigation.start_time,
            query_params=None,
            path_params=None,
            body=None,
            observability_identifiers=apm_trace_ids,
            content_type=None,
            content_encoding=None,
            machine_metrics=get_machine_metrics(),
            system_info=get_system_info(),
        ),
        flow_id=metric.flow_id,
    )


def safe_get_header(
    headers: Optional[Mapping[str, str]], header_name: str
) -> Optional[str]:
    try:
        if headers is None:
            return None

        return headers.get(header_name)
    except Exception as e:
        limited_logger.log(
            "Failed to get header", data={"error": str(e), "header_name": header_name}
        )
    return None
