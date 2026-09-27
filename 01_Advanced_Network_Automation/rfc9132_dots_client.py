"""
RFC 9132 - Distributed Denial-of-Service Open Threat Signaling (DOTS)
Signal Channel Specification.
Module provides production-grade signal client engines for mitigation telemetry.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any
import ipaddress


class DOTSValidationError(Exception):
    """Raised when mitigation payload elements violate RFC 9132 criteria."""
    pass


@dataclass(frozen=True)
class InterfaceTelemetry:
    """Enforces mathematical typing and validation onto structural metrics."""
    interface_name: str
    ingress_mbps: float
    egress_mbps: float
    threshold_mbps: float
    target_ips: List[str]

    def validate_targets(self) -> None:
        """Enforces networking layers are syntactically sound before execution."""
        if not self.target_ips:
            raise DOTSValidationError("Target IP list cannot be empty.")
        for ip in self.target_ips:
            try:
                ipaddress.ip_address(ip)
            except ValueError as err:
                raise DOTSValidationError(f"Invalid network target address: {ip}") from err

    @property
    def is_threshold_crossed(self) -> bool:
        """Deterministic state monitoring evaluation rule."""
        return (self.ingress_mbps + self.egress_mbps) >= self.threshold_mbps


@dataclass
class DOTSSignalPayload:
    """Structures standard data formatting frames strictly matching RFC 9132 specifications."""
    mitigation_id: int
    target_clnt: List[str]
    severity: int = 3  # Default operational severity: High
    cbor_frame: Dict[str, Any] = field(init=False)

    def __post_init__(self) -> None:
        """Auto-assembles payload structures immediately following initialization validation."""
        if not (1 <= self.severity <= 5):
            raise DOTSValidationError("RFC 9132 Severity indexes must fall inside 1-5.")

        # Build strict payload mapping layout
        self.cbor_frame = {
            "ietf-dots-signal-channel:mitigation-scope": {
                "scope": [
                    {
                        "mid": self.mitigation_id,
                        "target-prefix": self.target_clnt,
                        "client-side-mitigation": True
                    }
                ],
                "mitigation-start-hint": True
            }
        }


def detect_attach_telemetry(interface_data: Dict[str, Any]) -> InterfaceTelemetry:
    """
    Step 1: Read local network telemetry.
    Parses live engineering interface structures and validates metrics.
    """
    telemetry = InterfaceTelemetry(
        interface_name=interface_data.get("interface", "eth0"),
        ingress_mbps=float(interface_data.get("ingress", 0.0)),
        egress_mbps=float(interface_data.get("egress", 0.0)),
        threshold_mbps=float(interface_data.get("threshold", 1000.0)),
        target_ips=interface_data.get("targets", [])
    )
    telemetry.validate_targets()
    return telemetry


def build_dots_signal_payload(telemetry: InterfaceTelemetry, mitigation_id: int) -> DOTSSignalPayload:
    """
    Step 2: Construct the RFC payload.
    Converts telemetry violations into validated structural output profiles.
    """
    if not telemetry.is_threshold_crossed:
        raise DOTSValidationError("Payload assembly rejected: Interface thresholds running clear.")

    return DOTSSignalPayload(
        mitigation_id=mitigation_id,
        target_clnt=telemetry.target_ips
    )
