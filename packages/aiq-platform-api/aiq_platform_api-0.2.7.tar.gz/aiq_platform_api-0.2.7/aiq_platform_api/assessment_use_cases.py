# Example notebook: https://colab.research.google.com/drive/1XpDkCMb1myskcQOILK6XaaF1g0a_8666?usp=sharing
import os
import sys
from enum import Enum
from typing import Optional, Dict, Any, List

from aiq_platform_api.common_utils import (
    AttackIQRestClient,
    AttackIQLogger,
    AssessmentUtils,
)
from aiq_platform_api.env import ATTACKIQ_API_TOKEN, ATTACKIQ_PLATFORM_URL

logger = AttackIQLogger.get_logger(__name__)


def list_assessments(client: AttackIQRestClient, limit: Optional[int] = 10) -> int:
    """List assessments with basic information."""
    logger.info(f"Listing up to {limit} assessments")
    count = 0

    for assessment in AssessmentUtils.get_assessments(client, limit=limit):
        count += 1
        logger.info(f"Assessment {count}:")
        logger.info(f"  ID: {assessment.get('id', 'N/A')}")
        logger.info(f"  Name: {assessment.get('name', 'N/A')}")
        logger.info(f"  Status: {assessment.get('status', 'N/A')}")
        logger.info("---")

    logger.info(f"Total assessments listed: {count}")
    return count


def get_assessment_by_id(client: AttackIQRestClient, assessment_id: str) -> Optional[Dict[str, Any]]:
    """Get detailed information about an assessment by ID."""
    logger.info(f"Getting assessment with ID: {assessment_id}")
    assessment = AssessmentUtils.get_assessment_by_id(client, assessment_id)

    if assessment:
        logger.info(f"Assessment Name: {assessment.get('name')}")
        logger.info(f"Is Attack Graph: {assessment.get('is_attack_graph')}")  # Add more fields as needed

    return assessment


def list_assessment_runs(client: AttackIQRestClient, assessment_id: str, limit: Optional[int] = 10):
    """List recent runs for an assessment."""
    logger.info(f"Listing up to {limit} runs for assessment {assessment_id}")
    count = 0

    for run in AssessmentUtils.list_assessment_runs(client, assessment_id, limit=limit):
        count += 1
        logger.info(f"Run {count}:")
        logger.info(f"  ID: {run.get('id', 'N/A')}")
        logger.info(f"  Created: {run.get('created_at', 'N/A')}")
        logger.info(f"  Scenario Jobs In Progress: {run.get('scenario_jobs_in_progress', 'N/A')}")
        logger.info(f"  Integration Jobs In Progress: {run.get('integration_jobs_in_progress', 'N/A')}")
        logger.info("---")

    return count


def run_and_monitor_assessment(
    client: AttackIQRestClient,
    assessment_id: str,
    timeout: int = 600,
    check_interval: int = 10,
) -> Optional[str]:
    """Run an assessment and wait for it to complete."""
    logger.info(f"Running assessment {assessment_id} and monitoring completion")

    try:
        # Start the assessment
        run_id = AssessmentUtils.run_assessment(client, assessment_id)
        logger.info(f"Assessment started with run ID: {run_id}")

        # Wait for completion
        without_detection = True
        completed = AssessmentUtils.wait_for_run_completion(
            client, assessment_id, run_id, timeout, check_interval, without_detection
        )

        if completed:
            logger.info(f"Assessment run {run_id} completed successfully")
            return run_id
        else:
            logger.warning(f"Assessment run {run_id} did not complete within {timeout} seconds")
            return None

    except Exception as e:
        logger.error(f"Error running assessment: {str(e)}")
        return None


def get_run_results(client: AttackIQRestClient, run_id: str, limit: Optional[int] = 10) -> List[Dict[str, Any]]:
    """Get results for a completed run and return them as a list."""
    logger.info(f"Getting results for run {run_id}")
    results_generator = AssessmentUtils.get_results_by_run_id(client, run_id, limit=limit)
    collected_results = []
    for i, result in enumerate(results_generator):
        logger.info(f"Result {i + 1}:")
        logger.info(f"  ID: {result.get('id', 'N/A')}")
        logger.info(f"  Status: {result.get('status', 'N/A')}")
        logger.info(f"  Start Time: {result.get('start_time', 'N/A')}")
        logger.info(f"  End Time: {result.get('end_time', 'N/A')}")
        logger.info("---")
        collected_results.append(result)
    return collected_results


def get_detailed_result(client: AttackIQRestClient, result_id: str) -> Optional[Dict[str, Any]]:
    """Get detailed information about a specific result, including intermediate results."""
    logger.info(f"Getting detailed information for result {result_id}")
    result = AssessmentUtils.get_result_details(client, result_id)

    if not result:
        logger.error(f"Could not retrieve detailed result for result ID: {result_id}")
        return None

    logger.info("--- Detailed Result ---")
    logger.info(f"  Result ID: {result.get('id', 'N/A')}")
    logger.info(f"  Overall Outcome: {result.get('outcome', 'N/A')}")
    logger.info(f"  Detection Outcome: {result.get('detection_outcome', 'N/A')}")
    logger.info(f"  Run Started At: {result.get('run_started_at', 'N/A')}")

    # Log intermediate results
    intermediate_results = result.get("intermediate_results")
    if intermediate_results and isinstance(intermediate_results, list):
        logger.info("--- Intermediate Results (Nodes/Steps) ---")
        for i, step in enumerate(intermediate_results):
            logger.info(f"  Step {i + 1}:")
            logger.info(f"    Node ID: {step.get('node_id', 'N/A')}")
            logger.info(f"    Scenario Name: {step.get('scenario_name', 'N/A')}")
            logger.info(f"    Outcome: {step.get('outcome', 'N/A')}")

    return result


def list_assets_in_assessment(client: AttackIQRestClient, assessment_id: str, limit: Optional[int] = 10):
    """List assets associated with an assessment."""
    logger.info(f"Listing assets for assessment {assessment_id}")
    count = 0

    for asset in AssessmentUtils.get_assets_in_assessment(client, assessment_id, limit=limit):
        count += 1
        logger.info(f"Asset {count}:")
        logger.info(f"  ID: {asset.get('id', 'N/A')}")
        logger.info(f"  Name: {asset.get('name', 'N/A')}")
        logger.info(f"  Type: {asset.get('type', 'N/A')}")
        logger.info(f"  IP Address: {asset.get('ipv4_address', 'N/A')}")
        logger.info("---")

    return count


def get_recent_run_id(client: AttackIQRestClient, assessment_id: str) -> Optional[str]:
    """Get the most recent run ID for an assessment."""
    run = AssessmentUtils.get_most_recent_run(client, assessment_id)
    return run.get("id") if run else None


def get_last_run_details(client: AttackIQRestClient, assessment_id: str) -> Optional[Dict[str, Any]]:
    """Get detailed information about the most recent run of an assessment."""
    return AssessmentUtils.get_most_recent_run(client, assessment_id)


def assessment_workflow_demo(client: AttackIQRestClient, assessment_id: str, run_assessment: bool):
    """Demonstrate a complete assessment workflow."""
    logger.info(f"Starting assessment workflow demo for assessment {assessment_id}")

    # Step 1: Get assessment metadata
    metadata = get_assessment_by_id(client, assessment_id)
    if not metadata:
        logger.error("Could not get assessment metadata. Aborting workflow.")
        return

    # Step 2: List recent runs
    list_assessment_runs(client, assessment_id)

    # Step 3: Run the assessment and wait for completion
    run_id = None
    if run_assessment:
        run_id = run_and_monitor_assessment(client, assessment_id, timeout=60, check_interval=60)

    # If we didn't run an assessment or it didn't complete, get the most recent run
    if not run_id:
        run_id = get_recent_run_id(client, assessment_id)
        if not run_id:
            logger.error("No runs found for assessment. Aborting workflow.")
            return

    # Step 4: Get results for the run
    results = get_run_results(client, run_id)
    if not results:
        logger.error("No results found for run. Aborting workflow.")
        return

    # Step 5: Get detailed results including intermediate results
    for result in results:
        get_detailed_result(client, result["id"])


if __name__ == "__main__":
    if not ATTACKIQ_PLATFORM_URL or not ATTACKIQ_API_TOKEN:
        logger.error("Missing ATTACKIQ_PLATFORM_URL or ATTACKIQ_API_TOKEN")
        sys.exit(1)

    class TestChoice(Enum):
        LIST_ASSESSMENTS = "list_assessments"
        GET_RECENT_RUN = "get_recent_run"
        RUN_ASSESSMENT = "run_assessment"
        WORKFLOW_DEMO = "workflow_demo"
        GET_RESULTS = "get_results"
        ALL = "all"

    client = AttackIQRestClient(ATTACKIQ_PLATFORM_URL, ATTACKIQ_API_TOKEN)
    assessment_id = os.environ.get("ASSESSMENT_ID") or os.environ.get("ATTACKIQ_ATOMIC_ASSESSMENT_ID")

    # Change this to test different functionalities
    # choice: TestChoice = TestChoice.GET_RECENT_RUN
    # choice = TestChoice.LIST_ASSESSMENTS
    choice = TestChoice.RUN_ASSESSMENT
    # choice = TestChoice.WORKFLOW_DEMO
    # choice = TestChoice.GET_RESULTS
    # choice = TestChoice.ALL

    if choice == TestChoice.LIST_ASSESSMENTS:
        list_assessments(client, limit=5)

    elif choice == TestChoice.GET_RECENT_RUN:
        if not assessment_id:
            logger.error("ASSESSMENT_ID required for this test")
        else:
            run = AssessmentUtils.get_most_recent_run(client, assessment_id)
            if run:
                logger.info(f"Recent run: {run.get('id')}")
                logger.info(f"  Created: {run.get('created_at', 'N/A')}")
                logger.info(f"  Scenarios: {run.get('scenario_jobs_in_progress', 0)}")
                logger.info(f"  Integrations: {run.get('integration_jobs_in_progress', 0)}")
            else:
                logger.info("No runs found")

    elif choice == TestChoice.RUN_ASSESSMENT:
        if not assessment_id:
            logger.error("ASSESSMENT_ID required for this test")
        else:
            run_id = run_and_monitor_assessment(client, assessment_id)
            if run_id:
                results = list(AssessmentUtils.get_results_by_run_id(client, run_id, limit=3))
                logger.info(f"Completed with {len(results)} results")

    elif choice == TestChoice.WORKFLOW_DEMO:
        if not assessment_id:
            logger.error("ASSESSMENT_ID required for this test")
        else:
            assessment_workflow_demo(client, assessment_id, run_assessment=True)

    elif choice == TestChoice.GET_RESULTS:
        if not assessment_id:
            logger.error("ASSESSMENT_ID required for this test")
        else:
            run = AssessmentUtils.get_most_recent_run(client, assessment_id)
            if run:
                run_id = run.get("id")
                results = get_run_results(client, run_id)
                logger.info(f"Retrieved {len(results)} results")

    elif choice == TestChoice.ALL:
        list_assessments(client, limit=3)
        if assessment_id:
            get_assessment_by_id(client, assessment_id)
            run = AssessmentUtils.get_most_recent_run(client, assessment_id)
            if run:
                logger.info(f"Most recent run: {run.get('id')}")
            list_assessment_runs(client, assessment_id, limit=3)
            assessment_workflow_demo(client, assessment_id, run_assessment=False)
