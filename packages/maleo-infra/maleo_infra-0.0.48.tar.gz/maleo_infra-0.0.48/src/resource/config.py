from pydantic import BaseModel, Field
from typing import Annotated


class MeasurementConfig(BaseModel):
    interval: Annotated[float, Field(60.0, ge=5.0, description="Monitor interval")] = (
        60.0
    )
    window: Annotated[int, Field(5, ge=5, description="Smoothing window")] = 5


class ThresholdConfig(BaseModel):
    low: Annotated[float, Field(10.0, ge=0.0, description="Low threshold")] = 10.0
    normal: Annotated[float, Field(75.0, ge=0.0, description="Normal threshold")] = 75.0
    high: Annotated[float, Field(85.0, ge=0.0, description="High threshold")] = 85.0
    critical: Annotated[
        float, Field(95.0, ge=0.0, description="Critical threshold")
    ] = 95.0


class CPUUsageConfig(BaseModel):
    threshold: Annotated[
        ThresholdConfig, Field(default_factory=ThresholdConfig, description="Threshold")
    ] = ThresholdConfig()


class MemoryUsageConfig(BaseModel):
    limit: Annotated[
        float,
        Field(
            128.0, description="Memory limit (MB) applied to raw memory value", ge=0.0
        ),
    ] = 128.0
    threshold: Annotated[
        ThresholdConfig, Field(default_factory=ThresholdConfig, description="Threshold")
    ] = ThresholdConfig()


class UsageConfig(BaseModel):
    cpu: Annotated[
        CPUUsageConfig, Field(default_factory=CPUUsageConfig, description="CPU Usage")
    ] = CPUUsageConfig()
    memory: Annotated[
        MemoryUsageConfig,
        Field(default_factory=MemoryUsageConfig, description="Memory Usage"),
    ] = MemoryUsageConfig()


class Config(BaseModel):
    measurement: Annotated[
        MeasurementConfig,
        Field(
            default_factory=MeasurementConfig,
            description="Resource usage configuration",
        ),
    ] = MeasurementConfig()

    retention: Annotated[
        int,
        Field(
            3600,
            description="Monitor data retention (s)",
            ge=60,
            le=7200,
            multiple_of=60,
        ),
    ] = 3600

    usage: Annotated[
        UsageConfig, Field(default_factory=UsageConfig, description="Usage config")
    ] = UsageConfig()


class ConfigMixin(BaseModel):
    resource: Annotated[
        Config, Field(default_factory=Config, description="Resource config")
    ] = Config()
