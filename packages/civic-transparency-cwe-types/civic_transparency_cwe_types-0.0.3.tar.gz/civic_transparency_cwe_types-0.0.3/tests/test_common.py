"""Test suite for Phase and MultiPhase validation results."""

from ci.transparency.cwe.types.common_result_validation_phase import (
    PhaseValidationResult,
    add_processed_item,
    set_phase_detail,
    set_phase_info,
    update_phase_details,
    get_phase_summary,
)
from ci.transparency.cwe.types.common_result_validation_multiphase import (
    MultiPhaseValidationResult,
    add_phase_result,
    get_multi_phase_summary,
)


class TestPhaseAndMultiPhase:
    def test_phase_result_flow(self):
        phase = PhaseValidationResult()
        phase = set_phase_info(phase, "ingest", "schema")
        phase = add_processed_item(phase, "doc1")
        phase = update_phase_details(phase, {"checked": 1})
        phase = set_phase_detail(phase, "notes", "ok")

        summary = get_phase_summary(phase)
        assert summary["phase_name"] == "ingest"
        assert summary["items_processed"] == 1
        assert summary["phase_details"]["checked"] == 1

    def test_multiphase_aggregation(self):
        p1 = PhaseValidationResult(phase_name="ingest")
        p2 = PhaseValidationResult(phase_name="validate")

        mp = MultiPhaseValidationResult()
        mp = add_phase_result(mp, p1)
        mp = add_phase_result(mp, p2)

        summary = get_multi_phase_summary(mp)
        assert summary["total_phases"] == 2
        assert isinstance(summary["phase_names"], list)
