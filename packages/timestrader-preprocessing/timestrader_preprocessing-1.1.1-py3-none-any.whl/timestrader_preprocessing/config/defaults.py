"""Canonical normalization parameter management for Story 1.7."""

from __future__ import annotations

import asyncio
import hashlib
import json
import logging
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from importlib import resources
from importlib.abc import Traversable
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from .. import __version__ as PACKAGE_VERSION


@dataclass
class ParameterVersion:
    """Parameter version metadata"""
    version: str
    created_date: str
    checksum: str
    dataset_info: Dict[str, Any]
    file_path: str
    loaded_at: float
    

class ParameterManager:
    """Load and track TimesTrader normalization parameters with fallbacks."""

    def __init__(self, parameter_path: Optional[str] = "data/parameters") -> None:
        self.parameter_path = Path(parameter_path) if parameter_path else None
        if self.parameter_path:
            self.parameter_path.mkdir(parents=True, exist_ok=True)

        self._current_version: Optional[ParameterVersion] = None
        self._normalization_params: Dict[str, Dict[str, float]] = {}
        self._rolling_window: int = 288
        self._is_loaded = False

        self._packaged_artifact = "normalization_story_1_7.json"
        self._drift_threshold = 0.1
        self._drift_alerts: List[Dict[str, Any]] = []

        self.logger = logging.getLogger(__name__)

    async def load_parameters(
        self,
        version: Optional[str] = None,
        allow_packaged_fallback: bool = True,
    ) -> bool:
        """Load parameters from disk or bundled Story 1.7 artifacts."""

        try:
            parameter_data: Optional[Dict[str, Any]] = None
            parameter_file: Optional[Path] = None

            if self.parameter_path:
                self.logger.info(
                    "Loading normalization parameters from %s", self.parameter_path
                )
                parameter_file = self._find_parameter_file(version)
                if parameter_file:
                    parameter_data = await self._load_parameter_file(parameter_file)
                    if parameter_data and not self._validate_checksum(
                        parameter_file, parameter_data.get("checksum")
                    ):
                        self.logger.error("Parameter file checksum validation failed")
                        parameter_data = None

            if parameter_data is None and allow_packaged_fallback:
                self.logger.info("Falling back to packaged Story 1.7 normalization artifact")
                parameter_data = await self._load_packaged_parameters()
                if parameter_data:
                    parameter_file = None

            if not parameter_data:
                self.logger.error("No normalization parameters available")
                return False

            self._normalization_params = parameter_data["parameters"]
            self._rolling_window = parameter_data.get("rolling_window", 288)

            source_path = (
                str(parameter_file)
                if parameter_file is not None
                else f"pkg://{self._packaged_artifact}"
            )

            self._current_version = ParameterVersion(
                version=parameter_data["version"],
                created_date=parameter_data["created_date"],
                checksum=parameter_data["checksum"],
                dataset_info=parameter_data.get("dataset_info", {}),
                file_path=source_path,
                loaded_at=time.time(),
            )

            self._is_loaded = True

            self.logger.info(
                "Loaded normalization parameters v%s from %s",
                self._current_version.version,
                source_path,
            )

            return True

        except Exception as exc:  # pragma: no cover - defensive logging
            self.logger.error("Failed to load parameters: %s", exc)
            return False

    async def _load_packaged_parameters(self) -> Optional[Dict[str, Any]]:
        """Load bundled normalization parameters shipped with the package."""

        try:
            artifact_path = resources.files("timestrader_preprocessing.config").joinpath(
                self._packaged_artifact
            )

            data = await asyncio.to_thread(
                lambda: json.loads(artifact_path.read_text(encoding="utf-8"))
            )

            if not self._validate_checksum(artifact_path, data.get("checksum")):
                self.logger.error("Packaged normalization artifact failed checksum validation")
                return None

            return data

        except FileNotFoundError:
            self.logger.error("Packaged normalization artifact not found: %s", self._packaged_artifact)
            return None
        except Exception as exc:  # pragma: no cover - defensive logging
            self.logger.error("Unable to load packaged parameters: %s", exc)
            return None
    
    def _find_parameter_file(self, version: Optional[str] = None) -> Optional[Path]:
        """
        Find parameter file for specified version or latest
        
        Args:
            version: Version to find (latest if None)
            
        Returns:
            Path to parameter file or None
        """
        if not self.parameter_path:
            return None

        try:
            if version:
                file_path = self.parameter_path / f"normalization_params_v{version}.json"
                return file_path if file_path.exists() else None

            parameter_files = list(self.parameter_path.glob("normalization_params_v*.json"))
            if not parameter_files:
                return None

            parameter_files.sort(key=lambda file: file.stat().st_mtime, reverse=True)
            return parameter_files[0]

        except Exception as exc:  # pragma: no cover - defensive logging
            self.logger.error("Error finding parameter file: %s", exc)
            return None
    
    async def _load_parameter_file(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """
        Load parameter file with async I/O
        
        Args:
            file_path: Path to parameter file
            
        Returns:
            Parameter data or None
        """
        try:
            # Use asyncio for non-blocking file I/O
            loop = asyncio.get_event_loop()
            
            def read_file():
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            
            data = await loop.run_in_executor(None, read_file)
            
            # Validate required fields
            required_fields = ['version', 'created_date', 'checksum', 'parameters']
            for field in required_fields:
                if field not in data:
                    self.logger.error(f"Missing required field in parameter file: {field}")
                    return None
            
            return data
            
        except Exception as e:
            self.logger.error(f"Error loading parameter file {file_path}: {e}")
            return None
    
    def _validate_checksum(
        self, file_path: Path | Traversable, expected_checksum: Optional[str]
    ) -> bool:
        """
        Validate parameter file integrity using checksum
        
        Args:
            file_path: Path to parameter file
            expected_checksum: Expected SHA256 checksum
            
        Returns:
            Checksum validation result
        """
        if not expected_checksum:
            return False

        try:
            if isinstance(file_path, Traversable):
                with file_path.open("r", encoding="utf-8") as stream:
                    data = json.load(stream)
            else:
                with open(file_path, "r", encoding="utf-8") as stream:
                    data = json.load(stream)
            
            # Remove checksum field for validation
            validation_data = {k: v for k, v in data.items() if k != 'checksum'}
            data_str = json.dumps(validation_data, sort_keys=True)
            
            calculated_checksum = hashlib.sha256(data_str.encode()).hexdigest()
            
            is_valid = calculated_checksum == expected_checksum
            
            if not is_valid:
                self.logger.warning(
                    "Checksum mismatch - Expected: %s..., Calculated: %s...",
                    expected_checksum[:16],
                    calculated_checksum[:16],
                )

            return is_valid

        except Exception as exc:  # pragma: no cover - defensive logging
            self.logger.error("Error validating checksum: %s", exc)
            return False
    
    def get_normalization_params(self, indicator: str) -> Optional[Dict[str, float]]:
        """
        Get normalization parameters for specific indicator
        
        Args:
            indicator: Technical indicator name (vwap, rsi, atr, ema9, ema21, stochastic)
            
        Returns:
            Dictionary with 'mean' and 'std' values or None
        """
        if not self._is_loaded:
            self.logger.warning("Parameters not loaded")
            return None
        
        return self._normalization_params.get(indicator)
    
    def get_all_normalization_params(self) -> Dict[str, Dict[str, float]]:
        """
        Get all normalization parameters
        
        Returns:
            Dictionary of all indicator normalization parameters
        """
        if not self._is_loaded:
            return {}
        
        return self._normalization_params.copy()
    
    def get_rolling_window(self) -> int:
        """Get rolling window size used for normalization"""
        return self._rolling_window
    
    def get_version(self) -> str:
        """Get current parameter version"""
        if not self._current_version:
            return "unknown"
        return self._current_version.version
    
    def get_version_info(self) -> Optional[Dict[str, Any]]:
        """Get detailed version information"""
        if not self._current_version:
            return None
        
        return {
            'version': self._current_version.version,
            'created_date': self._current_version.created_date,
            'checksum': self._current_version.checksum,
            'dataset_info': self._current_version.dataset_info,
            'loaded_at': self._current_version.loaded_at,
            'age_hours': (time.time() - self._current_version.loaded_at) / 3600
        }
    
    def get_age_hours(self) -> float:
        """Get age of loaded parameters in hours"""
        if not self._current_version:
            return 0
        return (time.time() - self._current_version.loaded_at) / 3600
    
    def is_loaded(self) -> bool:
        """Check if parameters are loaded"""
        return self._is_loaded
    
    def detect_parameter_drift(
        self,
        current_stats: Dict[str, Dict[str, float]],
        threshold: float = None
    ) -> Dict[str, Any]:
        """
        Detect parameter drift compared to training distribution
        
        Args:
            current_stats: Current statistics {indicator: {mean, std}}
            threshold: Drift threshold (default: 0.1 = 10%)
            
        Returns:
            Drift analysis results
        """
        if not self._is_loaded:
            return {'error': 'Parameters not loaded'}
        
        threshold = threshold or self._drift_threshold
        drift_results = {
            'overall_drift': False,
            'drift_indicators': [],
            'drift_scores': {},
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
        
        try:
            for indicator, current_stat in current_stats.items():
                if indicator not in self._normalization_params:
                    continue
                
                training_params = self._normalization_params[indicator]
                
                # Calculate drift scores for mean and std
                mean_drift = abs(current_stat['mean'] - training_params['mean']) / abs(training_params['mean'])
                std_drift = abs(current_stat['std'] - training_params['std']) / abs(training_params['std'])
                
                # Overall drift score (max of mean and std drift)
                overall_drift = max(mean_drift, std_drift)
                
                drift_results['drift_scores'][indicator] = {
                    'mean_drift': mean_drift,
                    'std_drift': std_drift,
                    'overall_drift': overall_drift,
                    'exceeds_threshold': overall_drift > threshold
                }
                
                # Track indicators with significant drift
                if overall_drift > threshold:
                    drift_results['overall_drift'] = True
                    drift_results['drift_indicators'].append(indicator)
            
            # Log drift alert if necessary
            if drift_results['overall_drift']:
                alert_msg = f"Parameter drift detected: {drift_results['drift_indicators']}"
                self.logger.warning(alert_msg)
                self._drift_alerts.append({
                    'timestamp': time.time(),
                    'message': alert_msg,
                    'drift_scores': drift_results['drift_scores']
                })
            
            return drift_results
            
        except Exception as exc:  # pragma: no cover - defensive logging
            self.logger.error("Error detecting parameter drift: %s", exc)
            return {'error': str(exc)}
    
    def get_drift_alerts(self, max_alerts: int = 10) -> List[Dict[str, Any]]:
        """
        Get recent drift alerts
        
        Args:
            max_alerts: Maximum number of alerts to return
            
        Returns:
            List of recent drift alerts
        """
        return self._drift_alerts[-max_alerts:] if self._drift_alerts else []
    
    async def hot_reload(self) -> bool:
        """
        Hot reload parameters if newer version available
        
        Returns:
            True if parameters were reloaded
        """
        try:
            # Find latest parameter file
            latest_file = self._find_parameter_file()
            if not latest_file:
                return False
            
            # Check if newer than current
            if self._current_version and latest_file.stat().st_mtime <= self._current_version.loaded_at:
                return False
            
            self.logger.info("Newer parameter version detected, performing hot reload")
            
            # Load new parameters
            success = await self.load_parameters()
            
            if success:
                self.logger.info("Hot reload completed successfully")
            else:
                self.logger.error("Hot reload failed")
            
            return success
            
        except Exception as exc:  # pragma: no cover - defensive logging
            self.logger.error("Error during hot reload: %s", exc)
            return False
    
    def create_parameter_snapshot(self) -> Dict[str, Any]:
        """
        Create snapshot of current parameter state for backup/monitoring
        
        Returns:
            Parameter snapshot
        """
        if not self._is_loaded:
            return {}
        
        return {
            'version_info': self.get_version_info(),
            'parameters': self._normalization_params.copy(),
            'rolling_window': self._rolling_window,
            'drift_alerts_count': len(self._drift_alerts),
            'snapshot_timestamp': datetime.now(timezone.utc).isoformat()
        }
    
    def get_health_status(self) -> Dict[str, Any]:
        """
        Get parameter manager health status
        
        Returns:
            Health status information
        """
        try:
            health = {
                'is_loaded': self._is_loaded,
                'has_version': self._current_version is not None,
                'age_hours': self.get_age_hours(),
                'drift_alerts_count': len(self._drift_alerts)
            }
            
            # Parameter file existence check
            if self._current_version:
                health['file_exists'] = Path(self._current_version.file_path).exists()
            
            # Health score calculation
            health_score = 1.0
            if not health['is_loaded']:
                health_score *= 0.0
            elif not health['has_version']:
                health_score *= 0.5
            elif health['age_hours'] > 168:  # >1 week old
                health_score *= 0.8
            elif health['drift_alerts_count'] > 5:
                health_score *= 0.9
            
            health['health_score'] = health_score
            health['healthy'] = health_score > 0.8
            
            return health
            
        except Exception as e:
            return {
                'healthy': False,
                'error': str(e),
                'is_loaded': False,
                'health_score': 0.0
            }


class ParameterFileGenerator:
    """
    Utility for generating parameter files in Story 1.1a format
    (For testing and development purposes)
    """
    
    @staticmethod
    def create_sample_parameters(
        output_path: Path,
        version: str = PACKAGE_VERSION,
    ) -> bool:
        """
        Create sample parameter file for testing
        
        Args:
            output_path: Output file path
            version: Parameter version
            
        Returns:
            Success status
        """
        try:
            # Sample normalization parameters
            parameters = {
                "vwap": {"mean": 4567.23, "std": 125.45},
                "rsi": {"mean": 50.12, "std": 28.67},
                "atr": {"mean": 12.34, "std": 4.56},
                "ema9": {"mean": 4565.78, "std": 123.89},
                "ema21": {"mean": 4564.12, "std": 122.34},
                "stochastic": {"mean": 49.87, "std": 27.91}
            }
            
            # Create parameter data structure
            param_data = {
                "version": version,
                "created_date": datetime.now(timezone.utc).isoformat(),
                "dataset_info": {
                    "total_candles": 441682,
                    "date_range": "2020-07-27 to 2025-05-02",
                    "quality_score": 0.995
                },
                "parameters": parameters,
                "rolling_window": 288,
                "validation_passed": True
            }
            
            # Calculate checksum
            checksum_data = {k: v for k, v in param_data.items() if k != 'checksum'}
            checksum_str = json.dumps(checksum_data, sort_keys=True)
            checksum = hashlib.sha256(checksum_str.encode()).hexdigest()
            param_data["checksum"] = checksum
            
            # Write to file
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(param_data, f, indent=2)
            
            return True
            
        except Exception as exc:  # pragma: no cover - defensive logging
            logging.error("Error creating sample parameters: %s", exc)
            return False


@dataclass(frozen=True)
class ColabConfig:
    """Story 1.7 defaults optimized for Google Colab retraining."""

    environment: str = "colab"
    indicators: Tuple[str, ...] = (
        "vwap",
        "rsi",
        "atr",
        "ema9",
        "ema21",
        "stochastic",
    )
    normalization_method: str = "zscore"
    normalization_window: int = 288
    seq_len: int = 64
    d_model: int = 384
    quality_threshold: float = 0.995
    artifact_name: str = "normalization_story_1_7.json"


@dataclass(frozen=True)
class ProductionConfig:
    """Story 1.7 defaults for live inference pipelines."""

    environment: str = "production"
    indicators: Tuple[str, ...] = (
        "vwap",
        "rsi",
        "atr",
        "ema9",
        "ema21",
        "stochastic",
    )
    normalization_method: str = "zscore"
    normalization_window: int = 288
    seq_len: int = 64
    d_model: int = 384
    quality_threshold: float = 0.999
    artifact_name: str = "normalization_story_1_7.json"


def get_default_config(environment: str = "colab") -> ColabConfig | ProductionConfig:
    """Return the canonical configuration for the requested environment."""

    env = environment.lower()
    if env in {"prod", "production", "live"}:
        return ProductionConfig()
    return ColabConfig()
