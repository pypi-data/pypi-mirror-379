import copy
import datetime
from typing import Any, Dict, List, Literal, Optional, Union

from lseg_analytics._client.client import Client
from lseg_analytics.common._resource_base import ResourceBase
from lseg_analytics.exceptions import (
    LibraryException,
    ResourceNotFound,
    check_exception_and_raise,
    check_id,
)
from lseg_analytics_basic_client._types import JobStoreInputData
from lseg_analytics_basic_client.models import (
    ActualVsProjectedGlobalSettings,
    ActualVsProjectedRequest,
    ActualVsProjectedRequestItem,
    ApimCurveShift,
    ApimError,
    Balloon,
    BondIndicRequest,
    BulkCompact,
    BulkComposite,
    BulkDefaultSettings,
    BulkGlobalSettings,
    BulkJsonInputItem,
    BulkMeta,
    BulkResultItem,
    BulkResultRequest,
    BulkTemplateDataSource,
    CapVolatility,
    CapVolItem,
    CashflowFloaterSettings,
    CashFlowGlobalSettings,
    CashFlowInput,
    CashflowMbsSettings,
    CashflowPrepaySettings,
    CashFlowRequestData,
    CashflowVolatility,
    CloCallInfo,
    CloSettings,
    CmbsPrepayment,
    CmbsSettings,
    CMOModification,
    CollateralDetailsRequest,
    CollateralDetailsRequestInfo,
    ColumnDetail,
    ConvertiblePricing,
    CurveDetailsRequest,
    CurveMultiShift,
    CurvePoint,
    CurveSearch,
    CurveTypeAndCurrency,
    CustomScenario,
    DataItems,
    DataTable,
    DataTableColumnDetail,
    DefaultDials,
    Distribution,
    ExtraSettings,
    FloaterSettings,
    HecmSettings,
    HorizonInfo,
    IdentifierInfo,
    IdTypeEnum,
    IndexLinkerSettings,
    IndexProjection,
    InterpolationTypeAndVector,
    JobCreationRequest,
    JobResponse,
    JobResubmissionRequest,
    JobStatusResponse,
    JobTimelineEntry,
    JsonRef,
    JsonScenRef,
    LookbackSettings,
    LookupDetails,
    LossSettings,
    MappedResponseRefData,
    MarketSettingsRequest,
    MarketSettingsRequestInfo,
    MbsSettings,
    ModifyClass,
    ModifyCollateral,
    MonthRatePair,
    MuniSettings,
    OptionModel,
    OriginChannel,
    Partials,
    PrepayDialsInput,
    PrepayDialsSettings,
    PrepayModelSeller,
    PrepayModelServicer,
    PricingScenario,
    PyCalcGlobalSettings,
    PyCalcInput,
    PyCalcRequest,
    RefDataMeta,
    RequestId,
    RestPrepaySettings,
    ResultResponseBulkResultItem,
    Results,
    ReturnAttributionCurveTypeAndCurrency,
    ReturnAttributionGlobalSettings,
    ReturnAttributionInput,
    ReturnAttributionRequest,
    ScalarAndVector,
    ScalarAndVectorWithCollateral,
    ScenAbsoluteCurvePoint,
    Scenario,
    ScenarioCalcFloaterSettings,
    ScenarioCalcGlobalSettings,
    ScenarioCalcInput,
    ScenarioCalcRequest,
    ScenarioDefinition,
    ScenarioSettlement,
    ScenarioVolatility,
    ScenCalcExtraSettings,
    ScenPartials,
    ScheduleItem,
    SensitivityShocks,
    SettlementInfo,
    SqlSettings,
    StateHomePriceAppreciation,
    StoreType,
    StructureNote,
    Summary,
    SwaptionVolatility,
    SwaptionVolItem,
    SystemScenario,
    TermAndValue,
    TermRatePair,
    UDIExtension,
    UserCurve,
    UserLoan,
    UserLoanCollateral,
    UserLoanDeal,
    UserScenario,
    UserScenarioCurve,
    UserScenarioInput,
    UserScenCurveDefinition,
    UserVol,
    Vector,
    Volatility,
    VolItem,
    WalSensitivityInput,
    WalSensitivityPrepayType,
    WalSensitivityRequest,
    YBPortUserBond,
    YbRestCurveType,
    YbRestFrequency,
)

from ._logger import logger

__all__ = [
    "ActualVsProjectedGlobalSettings",
    "ActualVsProjectedRequestItem",
    "ApimCurveShift",
    "ApimError",
    "Balloon",
    "BulkDefaultSettings",
    "BulkGlobalSettings",
    "BulkJsonInputItem",
    "BulkMeta",
    "BulkResultItem",
    "BulkTemplateDataSource",
    "CMOModification",
    "CapVolItem",
    "CapVolatility",
    "CashFlowGlobalSettings",
    "CashFlowInput",
    "CashflowFloaterSettings",
    "CashflowMbsSettings",
    "CashflowPrepaySettings",
    "CashflowVolatility",
    "CloCallInfo",
    "CloSettings",
    "CmbsPrepayment",
    "CmbsSettings",
    "CollateralDetailsRequestInfo",
    "ColumnDetail",
    "ConvertiblePricing",
    "CurveMultiShift",
    "CurvePoint",
    "CurveSearch",
    "CurveTypeAndCurrency",
    "CustomScenario",
    "DataItems",
    "DataTable",
    "DataTableColumnDetail",
    "DefaultDials",
    "Distribution",
    "ExtraSettings",
    "FloaterSettings",
    "HecmSettings",
    "HorizonInfo",
    "IdTypeEnum",
    "IdentifierInfo",
    "IndexLinkerSettings",
    "IndexProjection",
    "InterpolationTypeAndVector",
    "JobResponse",
    "JobStatusResponse",
    "JobStoreInputData",
    "JobTimelineEntry",
    "JsonRef",
    "JsonScenRef",
    "LookbackSettings",
    "LookupDetails",
    "LossSettings",
    "MappedResponseRefData",
    "MarketSettingsRequestInfo",
    "MbsSettings",
    "ModifyClass",
    "ModifyCollateral",
    "MonthRatePair",
    "MuniSettings",
    "OptionModel",
    "OriginChannel",
    "Partials",
    "PrepayDialsInput",
    "PrepayDialsSettings",
    "PrepayModelSeller",
    "PrepayModelServicer",
    "PricingScenario",
    "PyCalcGlobalSettings",
    "PyCalcInput",
    "RefDataMeta",
    "RequestId",
    "RestPrepaySettings",
    "ResultResponseBulkResultItem",
    "Results",
    "ReturnAttributionCurveTypeAndCurrency",
    "ReturnAttributionGlobalSettings",
    "ReturnAttributionInput",
    "ScalarAndVector",
    "ScalarAndVectorWithCollateral",
    "ScenAbsoluteCurvePoint",
    "ScenCalcExtraSettings",
    "ScenPartials",
    "Scenario",
    "ScenarioCalcFloaterSettings",
    "ScenarioCalcGlobalSettings",
    "ScenarioCalcInput",
    "ScenarioDefinition",
    "ScenarioSettlement",
    "ScenarioVolatility",
    "ScheduleItem",
    "SensitivityShocks",
    "SettlementInfo",
    "SqlSettings",
    "StateHomePriceAppreciation",
    "StoreType",
    "StructureNote",
    "Summary",
    "SwaptionVolItem",
    "SwaptionVolatility",
    "SystemScenario",
    "TermAndValue",
    "TermRatePair",
    "UDIExtension",
    "UserCurve",
    "UserLoan",
    "UserLoanCollateral",
    "UserLoanDeal",
    "UserScenCurveDefinition",
    "UserScenario",
    "UserScenarioCurve",
    "UserScenarioInput",
    "UserVol",
    "Vector",
    "VolItem",
    "Volatility",
    "WalSensitivityInput",
    "WalSensitivityPrepayType",
    "YBPortUserBond",
    "YbRestCurveType",
    "YbRestFrequency",
    "abort_job",
    "bulk_compact_request",
    "bulk_composite_request",
    "bulk_yb_port_udi_request",
    "bulk_zip_request",
    "close_job",
    "create_job",
    "get_cash_flow_async",
    "get_cash_flow_sync",
    "get_csv_bulk_result",
    "get_formatted_result",
    "get_job",
    "get_job_data",
    "get_job_object_meta",
    "get_job_status",
    "get_json_result",
    "get_result",
    "get_tba_pricing_sync",
    "post_cash_flow_async",
    "post_cash_flow_sync",
    "post_csv_bulk_results_sync",
    "post_json_bulk_request_sync",
    "post_market_setting_sync",
    "request_actual_vs_projected_async",
    "request_actual_vs_projected_async_get",
    "request_actual_vs_projected_sync",
    "request_actual_vs_projected_sync_get",
    "request_bond_indic_async",
    "request_bond_indic_async_get",
    "request_bond_indic_sync",
    "request_bond_indic_sync_get",
    "request_collateral_details_async",
    "request_collateral_details_async_get",
    "request_collateral_details_sync",
    "request_collateral_details_sync_get",
    "request_curve_async",
    "request_curve_sync",
    "request_curves_async",
    "request_curves_sync",
    "request_get_scen_calc_sys_scen_async",
    "request_get_scen_calc_sys_scen_sync",
    "request_historical_data_async",
    "request_historical_data_sync",
    "request_index_catalogue_info_async",
    "request_index_catalogue_info_sync",
    "request_index_data_by_ticker_async",
    "request_index_data_by_ticker_sync",
    "request_index_providers_async",
    "request_index_providers_sync",
    "request_mbs_history_async",
    "request_mbs_history_sync",
    "request_mortgage_model_async",
    "request_mortgage_model_sync",
    "request_py_calculation_async",
    "request_py_calculation_async_by_id",
    "request_py_calculation_sync",
    "request_py_calculation_sync_by_id",
    "request_return_attribution_async",
    "request_return_attribution_sync",
    "request_scenario_calculation_async",
    "request_scenario_calculation_sync",
    "request_volatility_async",
    "request_volatility_sync",
    "request_wal_sensitivity_asyn_get",
    "request_wal_sensitivity_async",
    "request_wal_sensitivity_sync",
    "request_wal_sensitivity_sync_get",
    "resubmit_job",
    "upload_csv_job_data_async",
    "upload_csv_job_data_sync",
    "upload_csv_job_data_with_name_async",
    "upload_csv_job_data_with_name_sync",
    "upload_json_job_data_async",
    "upload_json_job_data_sync",
    "upload_json_job_data_with_name_async",
    "upload_json_job_data_with_name_sync",
    "upload_text_job_data_async",
    "upload_text_job_data_sync",
    "upload_text_job_data_with_name_async",
    "upload_text_job_data_with_name_sync",
]


def abort_job(*, job_ref: str) -> JobResponse:
    """
    Abort a job

    Parameters
    ----------
    job_ref : str
        Job reference. This can be of the form J-number or job name.

    Returns
    --------
    JobResponse


    Examples
    --------
    >>> # create temp job
    >>> job_response = create_job(
    >>>     name="close_Job"
    >>> )
    >>>
    >>> # abort job
    >>> response = abort_job(job_ref="close_Job")
    >>>
    >>> print(js.dumps(response.as_dict(), indent=4))
    {
        "id": "J-3638",
        "sequence": 0,
        "asOf": "2025-08-19",
        "closed": true,
        "onHold": false,
        "aborted": true,
        "exitStatus": "NEVER_STARTED",
        "actualHold": false,
        "name": "close_Job",
        "priority": 0,
        "order": "FAST",
        "requestCount": 0,
        "pendingCount": 0,
        "runningCount": 0,
        "okCount": 0,
        "errorCount": 0,
        "abortedCount": 0,
        "skipCount": 0,
        "startAfter": "2025-08-19T02:31:22.850Z",
        "stopAfter": "2025-08-20T02:31:22.850Z",
        "createdAt": "2025-08-19T02:31:22.852Z",
        "updatedAt": "2025-08-19T02:31:22.852Z"
    }

    """

    try:
        logger.info("Calling abort_job")

        response = Client().yield_book_rest.abort_job(job_ref=job_ref)

        output = response
        logger.info("Called abort_job")

        return output
    except Exception as err:
        logger.error("Error abort_job.")
        check_exception_and_raise(err, logger)


def bulk_compact_request(
    *,
    path: Optional[str] = None,
    name_expr: Optional[str] = None,
    body: Optional[str] = None,
    requests: Optional[List[Dict[str, Any]]] = None,
    data_source: Optional[BulkTemplateDataSource] = None,
    params: Optional[Dict[str, Any]] = None,
    create_job: Optional[bool] = None,
    chain_job: Optional[str] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> ResultResponseBulkResultItem:
    """
    Bulk compact request.

    Parameters
    ----------
    path : str, optional
        URL to which each individual request should be posted.i.e "/bond/py" for PY calculation.
    name_expr : str, optional
        Name of each request. This can be a valid JSON path expression, i.e "concat($.CUSIP,"_PY")" will give each request the name CUSIP_PY. Name should be unique within a single job.
    body : str, optional
        POST body associated with the calculation. This is specific to each request type. Refer to individual calculation section for more details.
    requests : List[Dict[str, Any]], optional
        List of key value pairs. This values provided will be used to update corresponding variables in the body of the request.
    data_source : BulkTemplateDataSource, optional

    params : Dict[str, Any], optional

    create_job : bool, optional
        Boolean with `true` and `false` values.
    chain_job : str, optional
        A sequence of textual characters.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    ResultResponseBulkResultItem


    Examples
    --------


    """

    try:
        logger.info("Calling bulk_compact_request")

        response = Client().yield_book_rest.bulk_compact_request(
            body=BulkCompact(
                path=path,
                name_expr=name_expr,
                body=body,
                requests=requests,
                data_source=data_source,
                params=params,
            ),
            create_job=create_job,
            chain_job=chain_job,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
            content_type="application/json",
        )

        output = response
        logger.info("Called bulk_compact_request")

        return output
    except Exception as err:
        logger.error("Error bulk_compact_request.")
        check_exception_and_raise(err, logger)


def bulk_composite_request(
    *,
    requests: List[BulkJsonInputItem],
    create_job: Optional[bool] = None,
    chain_job: Optional[str] = None,
    partial: Optional[bool] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> ResultResponseBulkResultItem:
    """
    Bulk composite request.

    Parameters
    ----------
    requests : List[BulkJsonInputItem]

    create_job : bool, optional
        Boolean with `true` and `false` values.
    chain_job : str, optional
        A sequence of textual characters.
    partial : bool, optional
        Boolean with `true` and `false` values.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    ResultResponseBulkResultItem


    Examples
    --------


    """

    try:
        logger.info("Calling bulk_composite_request")

        response = Client().yield_book_rest.bulk_composite_request(
            body=BulkComposite(requests=requests),
            create_job=create_job,
            chain_job=chain_job,
            partial=partial,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
            content_type="application/json",
        )

        output = response
        logger.info("Called bulk_composite_request")

        return output
    except Exception as err:
        logger.error("Error bulk_composite_request.")
        check_exception_and_raise(err, logger)


def bulk_yb_port_udi_request(
    *,
    data: str,
    prefix: Optional[str] = None,
    suffix: Optional[str] = None,
    create_job: Optional[bool] = None,
    chain_job: Optional[str] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> ResultResponseBulkResultItem:
    """
    Bulk YB Port UDI request.

    Parameters
    ----------
    data : str
        A sequence of textual characters.
    prefix : str, optional
        A sequence of textual characters.
    suffix : str, optional
        A sequence of textual characters.
    create_job : bool, optional
        Boolean with `true` and `false` values.
    chain_job : str, optional
        A sequence of textual characters.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    ResultResponseBulkResultItem


    Examples
    --------


    """

    try:
        logger.info("Calling bulk_yb_port_udi_request")

        response = Client().yield_book_rest.bulk_yb_port_udi_request(
            prefix=prefix,
            suffix=suffix,
            create_job=create_job,
            chain_job=chain_job,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
            content_type="text/plain",
            data=data,
        )

        output = response
        logger.info("Called bulk_yb_port_udi_request")

        return output
    except Exception as err:
        logger.error("Error bulk_yb_port_udi_request.")
        check_exception_and_raise(err, logger)


def bulk_zip_request(
    *,
    data: bytes,
    default_target: Optional[str] = None,
    create_job: Optional[bool] = None,
    chain_job: Optional[str] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> ResultResponseBulkResultItem:
    """
    Bulk zip request.

    Parameters
    ----------
    data : bytes
        Represent a byte array
    default_target : str, optional
        A sequence of textual characters.
    create_job : bool, optional
        Boolean with `true` and `false` values.
    chain_job : str, optional
        A sequence of textual characters.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    ResultResponseBulkResultItem


    Examples
    --------


    """

    try:
        logger.info("Calling bulk_zip_request")

        response = Client().yield_book_rest.bulk_zip_request(
            default_target=default_target,
            create_job=create_job,
            chain_job=chain_job,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
            content_type="application/zip",
            data=data,
        )

        output = response
        logger.info("Called bulk_zip_request")

        return output
    except Exception as err:
        logger.error("Error bulk_zip_request.")
        check_exception_and_raise(err, logger)


def close_job(*, job_ref: str) -> JobResponse:
    """
    Close a job

    Parameters
    ----------
    job_ref : str
        Job reference. This can be of the form J-number or job name.

    Returns
    --------
    JobResponse


    Examples
    --------
    >>> # create temp job
    >>> job_response = create_job(
    >>>     name="close_Job"
    >>> )
    >>>
    >>> # close job
    >>> response = close_job(job_ref="close_Job")
    >>>
    >>> print(js.dumps(response.as_dict(), indent=4))
    {
        "id": "J-3637",
        "sequence": 0,
        "asOf": "2025-08-19",
        "closed": true,
        "onHold": false,
        "aborted": false,
        "exitStatus": "NEVER_STARTED",
        "actualHold": false,
        "name": "close_Job",
        "priority": 0,
        "order": "FAST",
        "requestCount": 0,
        "pendingCount": 0,
        "runningCount": 0,
        "okCount": 0,
        "errorCount": 0,
        "abortedCount": 0,
        "skipCount": 0,
        "startAfter": "2025-08-19T02:31:17.445Z",
        "stopAfter": "2025-08-20T02:31:17.445Z",
        "createdAt": "2025-08-19T02:31:17.448Z",
        "updatedAt": "2025-08-19T02:31:17.766Z"
    }

    """

    try:
        logger.info("Calling close_job")

        response = Client().yield_book_rest.close_job(job_ref=job_ref)

        output = response
        logger.info("Called close_job")

        return output
    except Exception as err:
        logger.error("Error close_job.")
        check_exception_and_raise(err, logger)


def create_job(
    *,
    priority: Optional[int] = None,
    hold: Optional[bool] = None,
    start_after: Optional[datetime.datetime] = None,
    stop_after: Optional[datetime.datetime] = None,
    name: Optional[str] = None,
    asof: Optional[Union[str, datetime.date]] = None,
    order: Optional[Literal["FAST", "FIFO", "NONE"]] = None,
    chain: Optional[str] = None,
    desc: Optional[str] = None,
) -> JobResponse:
    """
    Create a new job

    Parameters
    ----------
    priority : int, optional
        Control priority of job. Requests within jobs of higher priority are processed prior to jobs with lower priority.
    hold : bool, optional
        When set to true, suspends the excution of all requests in the job, processing resumes only after the job is updated and the value is set to false.
    start_after : datetime.datetime, optional
        An instant in coordinated universal time (UTC)"
    stop_after : datetime.datetime, optional
        An instant in coordinated universal time (UTC)"
    name : str, optional
        Optional. Unique name associated with a job. There can only be one active job with this name. Job name can be used for all future job references. If a previously open job exists with the same name, the older job is closed before a new job is created.
    asof : Union[str, datetime.date], optional
        A date on a calendar without a time zone, e.g. "April 10th"
    order : Literal["FAST","FIFO","NONE"], optional

    chain : str, optional
        A sequence of textual characters.
    desc : str, optional
        User defined description of the job.

    Returns
    --------
    JobResponse


    Examples
    --------
    >>> # create job
    >>> job_response = create_job(
    >>>     priority=0,
    >>>     hold=True,
    >>>     start_after=datetime(2025, 3, 3, 10, 10, 15, 263),
    >>>     stop_after=datetime(2025, 3, 10, 20, 10, 15, 263),
    >>>     name="myJob",
    >>>     asof="2025-03-10",
    >>>     order="FAST",
    >>>     chain="string",
    >>>     desc="string",
    >>> )
    >>>
    >>> print(js.dumps(job_response.as_dict(), indent=4))
    {
        "id": "J-8157",
        "sequence": 0,
        "asOf": "2025-03-10",
        "closed": true,
        "onHold": true,
        "aborted": true,
        "exitStatus": "NEVER_STARTED",
        "actualHold": true,
        "name": "myJob",
        "chain": "string",
        "description": "string",
        "priority": 0,
        "order": "FAST",
        "requestCount": 0,
        "pendingCount": 0,
        "runningCount": 0,
        "okCount": 0,
        "errorCount": 0,
        "abortedCount": 0,
        "skipCount": 0,
        "startAfter": "2025-03-03T10:10:15Z",
        "stopAfter": "2025-03-10T20:10:15Z",
        "createdAt": "2025-09-18T08:57:19.153Z",
        "updatedAt": "2025-09-18T08:57:19.153Z"
    }

    """

    try:
        logger.info("Calling create_job")

        response = Client().yield_book_rest.create_job(
            body=JobCreationRequest(
                priority=priority,
                hold=hold,
                start_after=start_after,
                stop_after=stop_after,
                name=name,
                asof=asof,
                order=order,
                chain=chain,
                desc=desc,
            )
        )

        output = response
        logger.info("Called create_job")

        return output
    except Exception as err:
        logger.error("Error create_job.")
        check_exception_and_raise(err, logger)


def get_cash_flow_async(
    *,
    id: str,
    id_type: Optional[str] = None,
    pricing_date: Optional[str] = None,
    par_amount: Optional[str] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Get cash flow request async.

    Parameters
    ----------
    id : str
        Security reference ID.
    id_type : str, optional
        A sequence of textual characters.
    pricing_date : str, optional
        A sequence of textual characters.
    par_amount : str, optional
        A sequence of textual characters.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------
    >>> # Formulate and execute the get request by using instrument ID, Par_amount and job in which the calculation will be done
    >>> cf_async_get_response = get_cash_flow_async(
    >>>             id="999818LH",
    >>>             par_amount="10000"
    >>>         )
    >>>
    >>> cf_async_get_result = {}
    >>>
    >>> attempt = 1
    >>>
    >>> while attempt < 10:
    >>>
    >>>     try:
    >>>         time.sleep(10)
    >>>
    >>>         cf_async_get_result = get_result(request_id_parameter=cf_async_get_response.request_id)
    >>>
    >>>         break
    >>>
    >>>     except Exception as error:
    >>>         print(f"Attempt " + str(attempt) + " resulted in error retrieving results from:" + cf_async_get_response.request_id)
    >>>
    >>>         attempt+=1
    >>>
    >>> # Print output to a file, as CF output is too long for terminal printout
    >>> # print(js.dumps(cf_async_get_result, indent=4), file=open('.\\CF_async_get_output.json', 'w+'))
    >>>
    >>>
    >>> # Print onyl payment information
    >>> for paymentInfo in cf_async_get_result["data"]["cashFlow"]["dataPaymentList"]:
    >>>     print(js.dumps(paymentInfo, indent=4))
    {
        "date": "2025-10-20",
        "totalCashFlow": 143643.11083,
        "interestPayment": 41666.666667,
        "principalBalance": 9898023.555837,
        "principalPayment": 101976.444163,
        "endPrincipalBalance": 9898023.555837,
        "beginPrincipalBalance": 10000000.0,
        "prepayPrincipalPayment": 57528.797683,
        "scheduledPrincipalPayment": 44447.64648
    }
    {
        "date": "2025-11-20",
        "totalCashFlow": 142775.491344,
        "interestPayment": 41241.764816,
        "principalBalance": 9796489.829309,
        "principalPayment": 101533.726528,
        "endPrincipalBalance": 9796489.829309,
        "beginPrincipalBalance": 9898023.555837,
        "prepayPrincipalPayment": 57145.169785,
        "scheduledPrincipalPayment": 44388.556743
    }
    {
        "date": "2025-12-20",
        "totalCashFlow": 134860.061834,
        "interestPayment": 40818.707622,
        "principalBalance": 9702448.475097,
        "principalPayment": 94041.354212,
        "endPrincipalBalance": 9702448.475097,
        "beginPrincipalBalance": 9796489.829309,
        "prepayPrincipalPayment": 49712.737659,
        "scheduledPrincipalPayment": 44328.616553
    }
    {
        "date": "2026-01-20",
        "totalCashFlow": 139412.98894,
        "interestPayment": 40426.868646,
        "principalBalance": 9603462.354803,
        "principalPayment": 98986.120294,
        "endPrincipalBalance": 9603462.354803,
        "beginPrincipalBalance": 9702448.475097,
        "prepayPrincipalPayment": 54686.114506,
        "scheduledPrincipalPayment": 44300.005788
    }
    {
        "date": "2026-02-20",
        "totalCashFlow": 129907.051581,
        "interestPayment": 40014.426478,
        "principalBalance": 9513569.7297,
        "principalPayment": 89892.625103,
        "endPrincipalBalance": 9513569.7297,
        "beginPrincipalBalance": 9603462.354803,
        "prepayPrincipalPayment": 45646.333606,
        "scheduledPrincipalPayment": 44246.291497
    }
    {
        "date": "2026-03-20",
        "totalCashFlow": 129554.906715,
        "interestPayment": 39639.873874,
        "principalBalance": 9423654.696859,
        "principalPayment": 89915.032841,
        "endPrincipalBalance": 9423654.696859,
        "beginPrincipalBalance": 9513569.7297,
        "prepayPrincipalPayment": 45682.965703,
        "scheduledPrincipalPayment": 44232.067138
    }
    {
        "date": "2026-04-20",
        "totalCashFlow": 136313.476005,
        "interestPayment": 39265.227904,
        "principalBalance": 9326606.448758,
        "principalPayment": 97048.248101,
        "endPrincipalBalance": 9326606.448758,
        "beginPrincipalBalance": 9423654.696859,
        "prepayPrincipalPayment": 52832.586331,
        "scheduledPrincipalPayment": 44215.66177
    }
    {
        "date": "2026-05-20",
        "totalCashFlow": 139322.71775,
        "interestPayment": 38860.860203,
        "principalBalance": 9226144.591211,
        "principalPayment": 100461.857547,
        "endPrincipalBalance": 9226144.591211,
        "beginPrincipalBalance": 9326606.448758,
        "prepayPrincipalPayment": 56298.503597,
        "scheduledPrincipalPayment": 44163.35395
    }
    {
        "date": "2026-06-20",
        "totalCashFlow": 138392.384431,
        "interestPayment": 38442.26913,
        "principalBalance": 9126194.475909,
        "principalPayment": 99950.115301,
        "endPrincipalBalance": 9126194.475909,
        "beginPrincipalBalance": 9226144.591211,
        "prepayPrincipalPayment": 55858.182044,
        "scheduledPrincipalPayment": 44091.933257
    }
    {
        "date": "2026-07-20",
        "totalCashFlow": 142662.258004,
        "interestPayment": 38025.810316,
        "principalBalance": 9021558.028222,
        "principalPayment": 104636.447687,
        "endPrincipalBalance": 9021558.028222,
        "beginPrincipalBalance": 9126194.475909,
        "prepayPrincipalPayment": 60616.632624,
        "scheduledPrincipalPayment": 44019.815063
    }
    {
        "date": "2026-08-20",
        "totalCashFlow": 140971.010132,
        "interestPayment": 37589.825118,
        "principalBalance": 8918176.843208,
        "principalPayment": 103381.185014,
        "endPrincipalBalance": 8918176.843208,
        "beginPrincipalBalance": 9021558.028222,
        "prepayPrincipalPayment": 59459.494936,
        "scheduledPrincipalPayment": 43921.690078
    }
    {
        "date": "2026-09-20",
        "totalCashFlow": 136866.207597,
        "interestPayment": 37159.07018,
        "principalBalance": 8818469.705791,
        "principalPayment": 99707.137417,
        "endPrincipalBalance": 8818469.705791,
        "beginPrincipalBalance": 8918176.843208,
        "prepayPrincipalPayment": 55881.095876,
        "scheduledPrincipalPayment": 43826.04154
    }
    {
        "date": "2026-10-20",
        "totalCashFlow": 134542.82725,
        "interestPayment": 36743.623774,
        "principalBalance": 8720670.502316,
        "principalPayment": 97799.203476,
        "endPrincipalBalance": 8720670.502316,
        "beginPrincipalBalance": 8818469.705791,
        "prepayPrincipalPayment": 54054.244536,
        "scheduledPrincipalPayment": 43744.95894
    }
    {
        "date": "2026-11-20",
        "totalCashFlow": 131928.871146,
        "interestPayment": 36336.127093,
        "principalBalance": 8625077.758263,
        "principalPayment": 95592.744053,
        "endPrincipalBalance": 8625077.758263,
        "beginPrincipalBalance": 8720670.502316,
        "prepayPrincipalPayment": 51922.710962,
        "scheduledPrincipalPayment": 43670.033091
    }
    {
        "date": "2026-12-20",
        "totalCashFlow": 127543.986637,
        "interestPayment": 35937.823993,
        "principalBalance": 8533471.595619,
        "principalPayment": 91606.162644,
        "endPrincipalBalance": 8533471.595619,
        "beginPrincipalBalance": 8625077.758263,
        "prepayPrincipalPayment": 48003.194726,
        "scheduledPrincipalPayment": 43602.967918
    }
    {
        "date": "2027-01-20",
        "totalCashFlow": 130113.494613,
        "interestPayment": 35556.131648,
        "principalBalance": 8438914.232655,
        "principalPayment": 94557.362964,
        "endPrincipalBalance": 8438914.232655,
        "beginPrincipalBalance": 8533471.595619,
        "prepayPrincipalPayment": 51004.270252,
        "scheduledPrincipalPayment": 43553.092713
    }
    {
        "date": "2027-02-20",
        "totalCashFlow": 119829.637295,
        "interestPayment": 35162.142636,
        "principalBalance": 8354246.737995,
        "principalPayment": 84667.494659,
        "endPrincipalBalance": 8354246.737995,
        "beginPrincipalBalance": 8438914.232655,
        "prepayPrincipalPayment": 41182.323517,
        "scheduledPrincipalPayment": 43485.171142
    }
    {
        "date": "2027-03-20",
        "totalCashFlow": 120605.050635,
        "interestPayment": 34809.361408,
        "principalBalance": 8268451.048769,
        "principalPayment": 85795.689226,
        "endPrincipalBalance": 8268451.048769,
        "beginPrincipalBalance": 8354246.737995,
        "prepayPrincipalPayment": 42330.185483,
        "scheduledPrincipalPayment": 43465.503744
    }
    {
        "date": "2027-04-20",
        "totalCashFlow": 127458.449304,
        "interestPayment": 34451.87937,
        "principalBalance": 8175444.478835,
        "principalPayment": 93006.569934,
        "endPrincipalBalance": 8175444.478835,
        "beginPrincipalBalance": 8268451.048769,
        "prepayPrincipalPayment": 49568.936245,
        "scheduledPrincipalPayment": 43437.633689
    }
    {
        "date": "2027-05-20",
        "totalCashFlow": 129416.800315,
        "interestPayment": 34064.351995,
        "principalBalance": 8080092.030516,
        "principalPayment": 95352.448319,
        "endPrincipalBalance": 8080092.030516,
        "beginPrincipalBalance": 8175444.478835,
        "prepayPrincipalPayment": 51983.384311,
        "scheduledPrincipalPayment": 43369.064008
    }
    {
        "date": "2027-06-20",
        "totalCashFlow": 128431.220868,
        "interestPayment": 33667.050127,
        "principalBalance": 7985327.859775,
        "principalPayment": 94764.170741,
        "endPrincipalBalance": 7985327.859775,
        "beginPrincipalBalance": 8080092.030516,
        "prepayPrincipalPayment": 51479.502688,
        "scheduledPrincipalPayment": 43284.668052
    }
    {
        "date": "2027-07-20",
        "totalCashFlow": 132194.532629,
        "interestPayment": 33272.199416,
        "principalBalance": 7886405.526562,
        "principalPayment": 98922.333213,
        "endPrincipalBalance": 7886405.526562,
        "beginPrincipalBalance": 7985327.859775,
        "prepayPrincipalPayment": 55722.465511,
        "scheduledPrincipalPayment": 43199.867702
    }
    {
        "date": "2027-08-20",
        "totalCashFlow": 128714.546851,
        "interestPayment": 32860.023027,
        "principalBalance": 7790551.002739,
        "principalPayment": 95854.523823,
        "endPrincipalBalance": 7790551.002739,
        "beginPrincipalBalance": 7886405.526562,
        "prepayPrincipalPayment": 52765.786026,
        "scheduledPrincipalPayment": 43088.737798
    }
    {
        "date": "2027-09-20",
        "totalCashFlow": 127971.327413,
        "interestPayment": 32460.629178,
        "principalBalance": 7695040.304503,
        "principalPayment": 95510.698235,
        "endPrincipalBalance": 7695040.304503,
        "beginPrincipalBalance": 7790551.002739,
        "prepayPrincipalPayment": 52520.31433,
        "scheduledPrincipalPayment": 42990.383906
    }
    {
        "date": "2027-10-20",
        "totalCashFlow": 124043.250752,
        "interestPayment": 32062.667935,
        "principalBalance": 7603059.721687,
        "principalPayment": 91980.582816,
        "endPrincipalBalance": 7603059.721687,
        "beginPrincipalBalance": 7695040.304503,
        "prepayPrincipalPayment": 49090.550692,
        "scheduledPrincipalPayment": 42890.032124
    }
    {
        "date": "2027-11-20",
        "totalCashFlow": 120139.358706,
        "interestPayment": 31679.415507,
        "principalBalance": 7514599.778489,
        "principalPayment": 88459.943199,
        "endPrincipalBalance": 7514599.778489,
        "beginPrincipalBalance": 7603059.721687,
        "prepayPrincipalPayment": 45654.360288,
        "scheduledPrincipalPayment": 42805.582911
    }
    {
        "date": "2027-12-20",
        "totalCashFlow": 118785.58524,
        "interestPayment": 31310.83241,
        "principalBalance": 7427125.025659,
        "principalPayment": 87474.752829,
        "endPrincipalBalance": 7427125.025659,
        "beginPrincipalBalance": 7514599.778489,
        "prepayPrincipalPayment": 44737.263198,
        "scheduledPrincipalPayment": 42737.489631
    }
    {
        "date": "2028-01-20",
        "totalCashFlow": 118271.964361,
        "interestPayment": 30946.354274,
        "principalBalance": 7339799.415572,
        "principalPayment": 87325.610087,
        "endPrincipalBalance": 7339799.415572,
        "beginPrincipalBalance": 7427125.025659,
        "prepayPrincipalPayment": 44653.903081,
        "scheduledPrincipalPayment": 42671.707006
    }
    {
        "date": "2028-02-20",
        "totalCashFlow": 111263.692309,
        "interestPayment": 30582.497565,
        "principalBalance": 7259118.220828,
        "principalPayment": 80681.194744,
        "endPrincipalBalance": 7259118.220828,
        "beginPrincipalBalance": 7339799.415572,
        "prepayPrincipalPayment": 38077.723036,
        "scheduledPrincipalPayment": 42603.471707
    }
    {
        "date": "2028-03-20",
        "totalCashFlow": 111876.56821,
        "interestPayment": 30246.32592,
        "principalBalance": 7177487.978538,
        "principalPayment": 81630.24229,
        "endPrincipalBalance": 7177487.978538,
        "beginPrincipalBalance": 7259118.220828,
        "prepayPrincipalPayment": 39059.425379,
        "scheduledPrincipalPayment": 42570.816911
    }
    {
        "date": "2028-04-20",
        "totalCashFlow": 117312.831305,
        "interestPayment": 29906.199911,
        "principalBalance": 7090081.347143,
        "principalPayment": 87406.631395,
        "endPrincipalBalance": 7090081.347143,
        "beginPrincipalBalance": 7177487.978538,
        "prepayPrincipalPayment": 44876.754919,
        "scheduledPrincipalPayment": 42529.876476
    }
    {
        "date": "2028-05-20",
        "totalCashFlow": 114992.681511,
        "interestPayment": 29542.005613,
        "principalBalance": 7004630.671245,
        "principalPayment": 85450.675898,
        "endPrincipalBalance": 7004630.671245,
        "beginPrincipalBalance": 7090081.347143,
        "prepayPrincipalPayment": 42999.17551,
        "scheduledPrincipalPayment": 42451.500388
    }
    {
        "date": "2028-06-20",
        "totalCashFlow": 120297.03831,
        "interestPayment": 29185.96113,
        "principalBalance": 6913519.594066,
        "principalPayment": 91111.07718,
        "endPrincipalBalance": 6913519.594066,
        "beginPrincipalBalance": 7004630.671245,
        "prepayPrincipalPayment": 48729.77154,
        "scheduledPrincipalPayment": 42381.30564
    }
    {
        "date": "2028-07-20",
        "totalCashFlow": 120517.77979,
        "interestPayment": 28806.331642,
        "principalBalance": 6821808.145918,
        "principalPayment": 91711.448148,
        "endPrincipalBalance": 6821808.145918,
        "beginPrincipalBalance": 6913519.594066,
        "prepayPrincipalPayment": 49438.446375,
        "scheduledPrincipalPayment": 42273.001773
    }
    {
        "date": "2028-08-20",
        "totalCashFlow": 115897.669089,
        "interestPayment": 28424.200608,
        "principalBalance": 6734334.677437,
        "principalPayment": 87473.468481,
        "endPrincipalBalance": 6734334.677437,
        "beginPrincipalBalance": 6821808.145918,
        "prepayPrincipalPayment": 45316.809299,
        "scheduledPrincipalPayment": 42156.659182
    }
    {
        "date": "2028-09-20",
        "totalCashFlow": 117957.545179,
        "interestPayment": 28059.727823,
        "principalBalance": 6644436.860081,
        "principalPayment": 89897.817356,
        "endPrincipalBalance": 6644436.860081,
        "beginPrincipalBalance": 6734334.677437,
        "prepayPrincipalPayment": 47835.553293,
        "scheduledPrincipalPayment": 42062.264063
    }
    {
        "date": "2028-10-20",
        "totalCashFlow": 111734.515729,
        "interestPayment": 27685.153584,
        "principalBalance": 6560387.497936,
        "principalPayment": 84049.362145,
        "endPrincipalBalance": 6560387.497936,
        "beginPrincipalBalance": 6644436.860081,
        "prepayPrincipalPayment": 42100.870862,
        "scheduledPrincipalPayment": 41948.491283
    }
    {
        "date": "2028-11-20",
        "totalCashFlow": 110704.416081,
        "interestPayment": 27334.947908,
        "principalBalance": 6477018.029763,
        "principalPayment": 83369.468173,
        "endPrincipalBalance": 6477018.029763,
        "beginPrincipalBalance": 6560387.497936,
        "prepayPrincipalPayment": 41501.939606,
        "scheduledPrincipalPayment": 41867.528567
    }
    {
        "date": "2028-12-20",
        "totalCashFlow": 108224.886164,
        "interestPayment": 26987.575124,
        "principalBalance": 6395780.718723,
        "principalPayment": 81237.31104,
        "endPrincipalBalance": 6395780.718723,
        "beginPrincipalBalance": 6477018.029763,
        "prepayPrincipalPayment": 39450.179215,
        "scheduledPrincipalPayment": 41787.131825
    }
    {
        "date": "2029-01-20",
        "totalCashFlow": 106558.334344,
        "interestPayment": 26649.086328,
        "principalBalance": 6315871.470708,
        "principalPayment": 79909.248016,
        "endPrincipalBalance": 6315871.470708,
        "beginPrincipalBalance": 6395780.718723,
        "prepayPrincipalPayment": 38192.434632,
        "scheduledPrincipalPayment": 41716.813384
    }
    {
        "date": "2029-02-20",
        "totalCashFlow": 102419.550007,
        "interestPayment": 26316.131128,
        "principalBalance": 6239768.051828,
        "principalPayment": 76103.41888,
        "endPrincipalBalance": 6239768.051828,
        "beginPrincipalBalance": 6315871.470708,
        "prepayPrincipalPayment": 34451.792517,
        "scheduledPrincipalPayment": 41651.626362
    }
    {
        "date": "2029-03-20",
        "totalCashFlow": 101060.0852,
        "interestPayment": 25999.033549,
        "principalBalance": 6164707.000177,
        "principalPayment": 75061.051651,
        "endPrincipalBalance": 6164707.000177,
        "beginPrincipalBalance": 6239768.051828,
        "prepayPrincipalPayment": 33452.767161,
        "scheduledPrincipalPayment": 41608.28449
    }
    {
        "date": "2029-04-20",
        "totalCashFlow": 105055.455272,
        "interestPayment": 25686.279167,
        "principalBalance": 6085337.824073,
        "principalPayment": 79369.176104,
        "endPrincipalBalance": 6085337.824073,
        "beginPrincipalBalance": 6164707.000177,
        "prepayPrincipalPayment": 37800.26812,
        "scheduledPrincipalPayment": 41568.907984
    }
    {
        "date": "2029-05-20",
        "totalCashFlow": 106265.784886,
        "interestPayment": 25355.574267,
        "principalBalance": 6004427.613454,
        "principalPayment": 80910.210619,
        "endPrincipalBalance": 6004427.613454,
        "beginPrincipalBalance": 6085337.824073,
        "prepayPrincipalPayment": 39413.049522,
        "scheduledPrincipalPayment": 41497.161097
    }
    {
        "date": "2029-06-20",
        "totalCashFlow": 108985.472115,
        "interestPayment": 25018.448389,
        "principalBalance": 5920460.589728,
        "principalPayment": 83967.023726,
        "endPrincipalBalance": 5920460.589728,
        "beginPrincipalBalance": 6004427.613454,
        "prepayPrincipalPayment": 42555.984804,
        "scheduledPrincipalPayment": 41411.038921
    }
    {
        "date": "2029-07-20",
        "totalCashFlow": 107766.829588,
        "interestPayment": 24668.585791,
        "principalBalance": 5837362.345931,
        "principalPayment": 83098.243797,
        "endPrincipalBalance": 5837362.345931,
        "beginPrincipalBalance": 5920460.589728,
        "prepayPrincipalPayment": 41798.749253,
        "scheduledPrincipalPayment": 41299.494544
    }
    {
        "date": "2029-08-20",
        "totalCashFlow": 106291.831009,
        "interestPayment": 24322.343108,
        "principalBalance": 5755392.85803,
        "principalPayment": 81969.487901,
        "endPrincipalBalance": 5755392.85803,
        "beginPrincipalBalance": 5837362.345931,
        "prepayPrincipalPayment": 40780.116845,
        "scheduledPrincipalPayment": 41189.371056
    }
    {
        "date": "2029-09-20",
        "totalCashFlow": 106706.737869,
        "interestPayment": 23980.803575,
        "principalBalance": 5672666.923735,
        "principalPayment": 82725.934294,
        "endPrincipalBalance": 5672666.923735,
        "beginPrincipalBalance": 5755392.85803,
        "prepayPrincipalPayment": 41643.333578,
        "scheduledPrincipalPayment": 41082.600716
    }
    {
        "date": "2029-10-20",
        "totalCashFlow": 100223.59303,
        "interestPayment": 23636.112182,
        "principalBalance": 5596079.442887,
        "principalPayment": 76587.480848,
        "endPrincipalBalance": 5596079.442887,
        "beginPrincipalBalance": 5672666.923735,
        "prepayPrincipalPayment": 35621.766867,
        "scheduledPrincipalPayment": 40965.713981
    }
    {
        "date": "2029-11-20",
        "totalCashFlow": 101386.318502,
        "interestPayment": 23316.997679,
        "principalBalance": 5518010.122064,
        "principalPayment": 78069.320823,
        "endPrincipalBalance": 5518010.122064,
        "beginPrincipalBalance": 5596079.442887,
        "prepayPrincipalPayment": 37180.562109,
        "scheduledPrincipalPayment": 40888.758715
    }
    {
        "date": "2029-12-20",
        "totalCashFlow": 98190.897838,
        "interestPayment": 22991.708842,
        "principalBalance": 5442810.933068,
        "principalPayment": 75199.188996,
        "endPrincipalBalance": 5442810.933068,
        "beginPrincipalBalance": 5518010.122064,
        "prepayPrincipalPayment": 34402.343785,
        "scheduledPrincipalPayment": 40796.845211
    }
    {
        "date": "2030-01-20",
        "totalCashFlow": 96717.162794,
        "interestPayment": 22678.378888,
        "principalBalance": 5368772.149161,
        "principalPayment": 74038.783906,
        "endPrincipalBalance": 5368772.149161,
        "beginPrincipalBalance": 5442810.933068,
        "prepayPrincipalPayment": 33316.764252,
        "scheduledPrincipalPayment": 40722.019654
    }
    {
        "date": "2030-02-20",
        "totalCashFlow": 93141.66824,
        "interestPayment": 22369.883955,
        "principalBalance": 5298000.364876,
        "principalPayment": 70771.784285,
        "endPrincipalBalance": 5298000.364876,
        "beginPrincipalBalance": 5368772.149161,
        "prepayPrincipalPayment": 30119.805875,
        "scheduledPrincipalPayment": 40651.97841
    }
    {
        "date": "2030-03-20",
        "totalCashFlow": 91930.898095,
        "interestPayment": 22075.00152,
        "principalBalance": 5228144.468302,
        "principalPayment": 69855.896575,
        "endPrincipalBalance": 5228144.468302,
        "beginPrincipalBalance": 5298000.364876,
        "prepayPrincipalPayment": 29252.834139,
        "scheduledPrincipalPayment": 40603.062436
    }
    {
        "date": "2030-04-20",
        "totalCashFlow": 94783.377283,
        "interestPayment": 21783.935285,
        "principalBalance": 5155145.026303,
        "principalPayment": 72999.441998,
        "endPrincipalBalance": 5155145.026303,
        "beginPrincipalBalance": 5228144.468302,
        "prepayPrincipalPayment": 32441.612514,
        "scheduledPrincipalPayment": 40557.829484
    }
    {
        "date": "2030-05-20",
        "totalCashFlow": 96634.588759,
        "interestPayment": 21479.770943,
        "principalBalance": 5079990.208487,
        "principalPayment": 75154.817816,
        "endPrincipalBalance": 5079990.208487,
        "beginPrincipalBalance": 5155145.026303,
        "prepayPrincipalPayment": 34670.263585,
        "scheduledPrincipalPayment": 40484.554231
    }
    {
        "date": "2030-06-20",
        "totalCashFlow": 98329.245993,
        "interestPayment": 21166.625869,
        "principalBalance": 5002827.588363,
        "principalPayment": 77162.620124,
        "endPrincipalBalance": 5002827.588363,
        "beginPrincipalBalance": 5079990.208487,
        "prepayPrincipalPayment": 36772.554392,
        "scheduledPrincipalPayment": 40390.065732
    }
    {
        "date": "2030-07-20",
        "totalCashFlow": 96125.359657,
        "interestPayment": 20845.114952,
        "principalBalance": 4927547.343658,
        "principalPayment": 75280.244705,
        "endPrincipalBalance": 4927547.343658,
        "beginPrincipalBalance": 5002827.588363,
        "prepayPrincipalPayment": 35005.467309,
        "scheduledPrincipalPayment": 40274.777396
    }
    {
        "date": "2030-08-20",
        "totalCashFlow": 96916.719418,
        "interestPayment": 20531.447265,
        "principalBalance": 4851162.071505,
        "principalPayment": 76385.272153,
        "endPrincipalBalance": 4851162.071505,
        "beginPrincipalBalance": 4927547.343658,
        "prepayPrincipalPayment": 36215.631651,
        "scheduledPrincipalPayment": 40169.640501
    }
    {
        "date": "2030-09-20",
        "totalCashFlow": 95139.016155,
        "interestPayment": 20213.175298,
        "principalBalance": 4776236.230647,
        "principalPayment": 74925.840857,
        "endPrincipalBalance": 4776236.230647,
        "beginPrincipalBalance": 4851162.071505,
        "prepayPrincipalPayment": 34875.431615,
        "scheduledPrincipalPayment": 40050.409243
    }
    {
        "date": "2030-10-20",
        "totalCashFlow": 91552.428074,
        "interestPayment": 19900.984294,
        "principalBalance": 4704584.786867,
        "principalPayment": 71651.44378,
        "endPrincipalBalance": 4704584.786867,
        "beginPrincipalBalance": 4776236.230647,
        "prepayPrincipalPayment": 31713.430933,
        "scheduledPrincipalPayment": 39938.012847
    }
    {
        "date": "2030-11-20",
        "totalCashFlow": 91486.524033,
        "interestPayment": 19602.436612,
        "principalBalance": 4632700.699447,
        "principalPayment": 71884.087421,
        "endPrincipalBalance": 4632700.699447,
        "beginPrincipalBalance": 4704584.786867,
        "prepayPrincipalPayment": 32035.966669,
        "scheduledPrincipalPayment": 39848.120752
    }
    {
        "date": "2030-12-20",
        "totalCashFlow": 87935.036582,
        "interestPayment": 19302.919581,
        "principalBalance": 4564068.582446,
        "principalPayment": 68632.117001,
        "endPrincipalBalance": 4564068.582446,
        "beginPrincipalBalance": 4632700.699447,
        "prepayPrincipalPayment": 28880.565113,
        "scheduledPrincipalPayment": 39751.551888
    }
    {
        "date": "2031-01-20",
        "totalCashFlow": 88217.232246,
        "interestPayment": 19016.952427,
        "principalBalance": 4494868.302627,
        "principalPayment": 69200.279819,
        "endPrincipalBalance": 4494868.302627,
        "beginPrincipalBalance": 4564068.582446,
        "prepayPrincipalPayment": 29521.916936,
        "scheduledPrincipalPayment": 39678.362883
    }
    {
        "date": "2031-02-20",
        "totalCashFlow": 84378.157293,
        "interestPayment": 18728.617928,
        "principalBalance": 4429218.763261,
        "principalPayment": 65649.539366,
        "endPrincipalBalance": 4429218.763261,
        "beginPrincipalBalance": 4494868.302627,
        "prepayPrincipalPayment": 26053.678099,
        "scheduledPrincipalPayment": 39595.861266
    }
    {
        "date": "2031-03-20",
        "totalCashFlow": 83292.546975,
        "interestPayment": 18455.07818,
        "principalBalance": 4364381.294467,
        "principalPayment": 64837.468795,
        "endPrincipalBalance": 4364381.294467,
        "beginPrincipalBalance": 4429218.763261,
        "prepayPrincipalPayment": 25297.002124,
        "scheduledPrincipalPayment": 39540.466671
    }
    {
        "date": "2031-04-20",
        "totalCashFlow": 85536.197841,
        "interestPayment": 18184.92206,
        "principalBalance": 4297030.018686,
        "principalPayment": 67351.275781,
        "endPrincipalBalance": 4297030.018686,
        "beginPrincipalBalance": 4364381.294467,
        "prepayPrincipalPayment": 27862.750502,
        "scheduledPrincipalPayment": 39488.525279
    }
    {
        "date": "2031-05-20",
        "totalCashFlow": 86946.951693,
        "interestPayment": 17904.291745,
        "principalBalance": 4227987.358738,
        "principalPayment": 69042.659948,
        "endPrincipalBalance": 4227987.358738,
        "beginPrincipalBalance": 4297030.018686,
        "prepayPrincipalPayment": 29632.963404,
        "scheduledPrincipalPayment": 39409.696544
    }
    {
        "date": "2031-06-20",
        "totalCashFlow": 87371.126866,
        "interestPayment": 17616.613995,
        "principalBalance": 4158232.845867,
        "principalPayment": 69754.512871,
        "endPrincipalBalance": 4158232.845867,
        "beginPrincipalBalance": 4227987.358738,
        "prepayPrincipalPayment": 30443.976192,
        "scheduledPrincipalPayment": 39310.536679
    }
    {
        "date": "2031-07-20",
        "totalCashFlow": 87203.05642,
        "interestPayment": 17325.970191,
        "principalBalance": 4088355.759638,
        "principalPayment": 69877.086229,
        "endPrincipalBalance": 4088355.759638,
        "beginPrincipalBalance": 4158232.845867,
        "prepayPrincipalPayment": 30677.628775,
        "scheduledPrincipalPayment": 39199.457454
    }
    {
        "date": "2031-08-20",
        "totalCashFlow": 86817.175778,
        "interestPayment": 17034.815665,
        "principalBalance": 4018573.399526,
        "principalPayment": 69782.360112,
        "endPrincipalBalance": 4018573.399526,
        "beginPrincipalBalance": 4088355.759638,
        "prepayPrincipalPayment": 30700.740251,
        "scheduledPrincipalPayment": 39081.619861
    }
    {
        "date": "2031-09-20",
        "totalCashFlow": 84457.799707,
        "interestPayment": 16744.055831,
        "principalBalance": 3950859.65565,
        "principalPayment": 67713.743876,
        "endPrincipalBalance": 3950859.65565,
        "beginPrincipalBalance": 4018573.399526,
        "prepayPrincipalPayment": 28754.868328,
        "scheduledPrincipalPayment": 38958.875548
    }
    {
        "date": "2031-10-20",
        "totalCashFlow": 82957.942528,
        "interestPayment": 16461.915232,
        "principalBalance": 3884363.628353,
        "principalPayment": 66496.027296,
        "endPrincipalBalance": 3884363.628353,
        "beginPrincipalBalance": 3950859.65565,
        "prepayPrincipalPayment": 27645.569448,
        "scheduledPrincipalPayment": 38850.457848
    }
    {
        "date": "2031-11-20",
        "totalCashFlow": 82030.707809,
        "interestPayment": 16184.848451,
        "principalBalance": 3818517.768996,
        "principalPayment": 65845.859357,
        "endPrincipalBalance": 3818517.768996,
        "beginPrincipalBalance": 3884363.628353,
        "prepayPrincipalPayment": 27097.324558,
        "scheduledPrincipalPayment": 38748.534799
    }
    {
        "date": "2031-12-20",
        "totalCashFlow": 78391.102623,
        "interestPayment": 15910.490704,
        "principalBalance": 3756037.157077,
        "principalPayment": 62480.611919,
        "endPrincipalBalance": 3756037.157077,
        "beginPrincipalBalance": 3818517.768996,
        "prepayPrincipalPayment": 23832.932722,
        "scheduledPrincipalPayment": 38647.679197
    }
    {
        "date": "2032-01-20",
        "totalCashFlow": 79793.650718,
        "interestPayment": 15650.154821,
        "principalBalance": 3691893.66118,
        "principalPayment": 64143.495897,
        "endPrincipalBalance": 3691893.66118,
        "beginPrincipalBalance": 3756037.157077,
        "prepayPrincipalPayment": 25567.641145,
        "scheduledPrincipalPayment": 38575.854752
    }
    {
        "date": "2032-02-20",
        "totalCashFlow": 75463.202131,
        "interestPayment": 15382.890255,
        "principalBalance": 3631813.349304,
        "principalPayment": 60080.311876,
        "endPrincipalBalance": 3631813.349304,
        "beginPrincipalBalance": 3691893.66118,
        "prepayPrincipalPayment": 21598.33121,
        "scheduledPrincipalPayment": 38481.980666
    }
    {
        "date": "2032-03-20",
        "totalCashFlow": 74990.530157,
        "interestPayment": 15132.555622,
        "principalBalance": 3571955.374769,
        "principalPayment": 59857.974535,
        "endPrincipalBalance": 3571955.374769,
        "beginPrincipalBalance": 3631813.349304,
        "prepayPrincipalPayment": 21432.303809,
        "scheduledPrincipalPayment": 38425.670726
    }
    {
        "date": "2032-04-20",
        "totalCashFlow": 77535.854092,
        "interestPayment": 14883.147395,
        "principalBalance": 3509302.668072,
        "principalPayment": 62652.706697,
        "endPrincipalBalance": 3509302.668072,
        "beginPrincipalBalance": 3571955.374769,
        "prepayPrincipalPayment": 24285.291727,
        "scheduledPrincipalPayment": 38367.41497
    }
    {
        "date": "2032-05-20",
        "totalCashFlow": 77996.497322,
        "interestPayment": 14622.09445,
        "principalBalance": 3445928.2652,
        "principalPayment": 63374.402872,
        "endPrincipalBalance": 3445928.2652,
        "beginPrincipalBalance": 3509302.668072,
        "prepayPrincipalPayment": 25100.161478,
        "scheduledPrincipalPayment": 38274.241394
    }
    {
        "date": "2032-06-20",
        "totalCashFlow": 77225.080123,
        "interestPayment": 14358.034438,
        "principalBalance": 3383061.219516,
        "principalPayment": 62867.045684,
        "endPrincipalBalance": 3383061.219516,
        "beginPrincipalBalance": 3445928.2652,
        "prepayPrincipalPayment": 24699.539401,
        "scheduledPrincipalPayment": 38167.506283
    }
    {
        "date": "2032-07-20",
        "totalCashFlow": 78361.356148,
        "interestPayment": 14096.088415,
        "principalBalance": 3318795.951783,
        "principalPayment": 64265.267733,
        "endPrincipalBalance": 3318795.951783,
        "beginPrincipalBalance": 3383061.219516,
        "prepayPrincipalPayment": 26204.83891,
        "scheduledPrincipalPayment": 38060.428823
    }
    {
        "date": "2032-08-20",
        "totalCashFlow": 76542.97884,
        "interestPayment": 13828.316466,
        "principalBalance": 3256081.289409,
        "principalPayment": 62714.662374,
        "endPrincipalBalance": 3256081.289409,
        "beginPrincipalBalance": 3318795.951783,
        "prepayPrincipalPayment": 24783.413999,
        "scheduledPrincipalPayment": 37931.248375
    }
    {
        "date": "2032-09-20",
        "totalCashFlow": 75837.987278,
        "interestPayment": 13567.005373,
        "principalBalance": 3193810.307503,
        "principalPayment": 62270.981906,
        "endPrincipalBalance": 3193810.307503,
        "beginPrincipalBalance": 3256081.289409,
        "prepayPrincipalPayment": 24457.803318,
        "scheduledPrincipalPayment": 37813.178588
    }
    {
        "date": "2032-10-20",
        "totalCashFlow": 73889.728862,
        "interestPayment": 13307.542948,
        "principalBalance": 3133228.121589,
        "principalPayment": 60582.185914,
        "endPrincipalBalance": 3133228.121589,
        "beginPrincipalBalance": 3193810.307503,
        "prepayPrincipalPayment": 22888.447332,
        "scheduledPrincipalPayment": 37693.738582
    }
    {
        "date": "2032-11-20",
        "totalCashFlow": 71982.842493,
        "interestPayment": 13055.117173,
        "principalBalance": 3074300.396269,
        "principalPayment": 58927.72532,
        "endPrincipalBalance": 3074300.396269,
        "beginPrincipalBalance": 3133228.121589,
        "prepayPrincipalPayment": 21339.888996,
        "scheduledPrincipalPayment": 37587.836324
    }
    {
        "date": "2032-12-20",
        "totalCashFlow": 71100.391235,
        "interestPayment": 12809.584984,
        "principalBalance": 3016009.590019,
        "principalPayment": 58290.806251,
        "endPrincipalBalance": 3016009.590019,
        "beginPrincipalBalance": 3074300.396269,
        "prepayPrincipalPayment": 20795.036768,
        "scheduledPrincipalPayment": 37495.769483
    }
    {
        "date": "2033-01-20",
        "totalCashFlow": 70541.347015,
        "interestPayment": 12566.706625,
        "principalBalance": 2958034.949629,
        "principalPayment": 57974.64039,
        "endPrincipalBalance": 2958034.949629,
        "beginPrincipalBalance": 3016009.590019,
        "prepayPrincipalPayment": 20568.985003,
        "scheduledPrincipalPayment": 37405.655387
    }
    {
        "date": "2033-02-20",
        "totalCashFlow": 67523.582244,
        "interestPayment": 12325.145623,
        "principalBalance": 2902836.513009,
        "principalPayment": 55198.43662,
        "endPrincipalBalance": 2902836.513009,
        "beginPrincipalBalance": 2958034.949629,
        "prepayPrincipalPayment": 17884.854567,
        "scheduledPrincipalPayment": 37313.582053
    }
    {
        "date": "2033-03-20",
        "totalCashFlow": 67043.633495,
        "interestPayment": 12095.152138,
        "principalBalance": 2847888.031651,
        "principalPayment": 54948.481358,
        "endPrincipalBalance": 2847888.031651,
        "beginPrincipalBalance": 2902836.513009,
        "prepayPrincipalPayment": 17697.430895,
        "scheduledPrincipalPayment": 37251.050463
    }
    {
        "date": "2033-04-20",
        "totalCashFlow": 69134.863254,
        "interestPayment": 11866.200132,
        "principalBalance": 2790619.368529,
        "principalPayment": 57268.663122,
        "endPrincipalBalance": 2790619.368529,
        "beginPrincipalBalance": 2847888.031651,
        "prepayPrincipalPayment": 20082.000681,
        "scheduledPrincipalPayment": 37186.662441
    }
    {
        "date": "2033-05-20",
        "totalCashFlow": 68416.587212,
        "interestPayment": 11627.580702,
        "principalBalance": 2733830.362019,
        "principalPayment": 56789.006509,
        "endPrincipalBalance": 2733830.362019,
        "beginPrincipalBalance": 2790619.368529,
        "prepayPrincipalPayment": 19702.815341,
        "scheduledPrincipalPayment": 37086.191168
    }
    {
        "date": "2033-06-20",
        "totalCashFlow": 68956.413497,
        "interestPayment": 11390.959842,
        "principalBalance": 2676264.908364,
        "principalPayment": 57565.453656,
        "endPrincipalBalance": 2676264.908364,
        "beginPrincipalBalance": 2733830.362019,
        "prepayPrincipalPayment": 20579.858323,
        "scheduledPrincipalPayment": 36985.595333
    }
    {
        "date": "2033-07-20",
        "totalCashFlow": 69168.399027,
        "interestPayment": 11151.103785,
        "principalBalance": 2618247.613122,
        "principalPayment": 58017.295242,
        "endPrincipalBalance": 2618247.613122,
        "beginPrincipalBalance": 2676264.908364,
        "prepayPrincipalPayment": 21149.692712,
        "scheduledPrincipalPayment": 36867.60253
    }
    {
        "date": "2033-08-20",
        "totalCashFlow": 67115.782482,
        "interestPayment": 10909.365055,
        "principalBalance": 2562041.195694,
        "principalPayment": 56206.417428,
        "endPrincipalBalance": 2562041.195694,
        "beginPrincipalBalance": 2618247.613122,
        "prepayPrincipalPayment": 19470.57732,
        "scheduledPrincipalPayment": 36735.840108
    }
    {
        "date": "2033-09-20",
        "totalCashFlow": 67437.066686,
        "interestPayment": 10675.171649,
        "principalBalance": 2505279.300657,
        "principalPayment": 56761.895037,
        "endPrincipalBalance": 2505279.300657,
        "beginPrincipalBalance": 2562041.195694,
        "prepayPrincipalPayment": 20139.975262,
        "scheduledPrincipalPayment": 36621.919775
    }
    {
        "date": "2033-10-20",
        "totalCashFlow": 65312.13937,
        "interestPayment": 10438.663753,
        "principalBalance": 2450405.82504,
        "principalPayment": 54873.475617,
        "endPrincipalBalance": 2450405.82504,
        "beginPrincipalBalance": 2505279.300657,
        "prepayPrincipalPayment": 18381.035987,
        "scheduledPrincipalPayment": 36492.439631
    }
    {
        "date": "2033-11-20",
        "totalCashFlow": 63719.671675,
        "interestPayment": 10210.024271,
        "principalBalance": 2396896.177636,
        "principalPayment": 53509.647404,
        "endPrincipalBalance": 2396896.177636,
        "beginPrincipalBalance": 2450405.82504,
        "prepayPrincipalPayment": 17126.819745,
        "scheduledPrincipalPayment": 36382.827658
    }
    {
        "date": "2033-12-20",
        "totalCashFlow": 62916.843889,
        "interestPayment": 9987.067407,
        "principalBalance": 2343966.401154,
        "principalPayment": 52929.776483,
        "endPrincipalBalance": 2343966.401154,
        "beginPrincipalBalance": 2396896.177636,
        "prepayPrincipalPayment": 16643.4168,
        "scheduledPrincipalPayment": 36286.359682
    }
    {
        "date": "2034-01-20",
        "totalCashFlow": 62363.597316,
        "interestPayment": 9766.526671,
        "principalBalance": 2291369.330509,
        "principalPayment": 52597.070644,
        "endPrincipalBalance": 2291369.330509,
        "beginPrincipalBalance": 2343966.401154,
        "prepayPrincipalPayment": 16405.310387,
        "scheduledPrincipalPayment": 36191.760257
    }
    {
        "date": "2034-02-20",
        "totalCashFlow": 59944.527889,
        "interestPayment": 9547.37221,
        "principalBalance": 2240972.174831,
        "principalPayment": 50397.155679,
        "endPrincipalBalance": 2240972.174831,
        "beginPrincipalBalance": 2291369.330509,
        "prepayPrincipalPayment": 14301.865492,
        "scheduledPrincipalPayment": 36095.290186
    }
    {
        "date": "2034-03-20",
        "totalCashFlow": 59464.058425,
        "interestPayment": 9337.384062,
        "principalBalance": 2190845.500467,
        "principalPayment": 50126.674364,
        "endPrincipalBalance": 2190845.500467,
        "beginPrincipalBalance": 2240972.174831,
        "prepayPrincipalPayment": 14099.781086,
        "scheduledPrincipalPayment": 36026.893278
    }
    {
        "date": "2034-04-20",
        "totalCashFlow": 60921.204541,
        "interestPayment": 9128.522919,
        "principalBalance": 2139052.818844,
        "principalPayment": 51792.681623,
        "endPrincipalBalance": 2139052.818844,
        "beginPrincipalBalance": 2190845.500467,
        "prepayPrincipalPayment": 15835.977136,
        "scheduledPrincipalPayment": 35956.704487
    }
    {
        "date": "2034-05-20",
        "totalCashFlow": 60067.722657,
        "interestPayment": 8912.720079,
        "principalBalance": 2087897.816266,
        "principalPayment": 51155.002579,
        "endPrincipalBalance": 2087897.816266,
        "beginPrincipalBalance": 2139052.818844,
        "prepayPrincipalPayment": 15302.815125,
        "scheduledPrincipalPayment": 35852.187454
    }
    {
        "date": "2034-06-20",
        "totalCashFlow": 60925.598495,
        "interestPayment": 8699.574234,
        "principalBalance": 2035671.792005,
        "principalPayment": 52226.024261,
        "endPrincipalBalance": 2035671.792005,
        "beginPrincipalBalance": 2087897.816266,
        "prepayPrincipalPayment": 16475.424894,
        "scheduledPrincipalPayment": 35750.599367
    }
    {
        "date": "2034-07-20",
        "totalCashFlow": 60547.156175,
        "interestPayment": 8481.9658,
        "principalBalance": 1983606.60163,
        "principalPayment": 52065.190375,
        "endPrincipalBalance": 1983606.60163,
        "beginPrincipalBalance": 2035671.792005,
        "prepayPrincipalPayment": 16442.911014,
        "scheduledPrincipalPayment": 35622.27936
    }
    {
        "date": "2034-08-20",
        "totalCashFlow": 58914.685674,
        "interestPayment": 8265.027507,
        "principalBalance": 1932956.943463,
        "principalPayment": 50649.658167,
        "endPrincipalBalance": 1932956.943463,
        "beginPrincipalBalance": 1983606.60163,
        "prepayPrincipalPayment": 15162.139392,
        "scheduledPrincipalPayment": 35487.518775
    }
    {
        "date": "2034-09-20",
        "totalCashFlow": 59046.888015,
        "interestPayment": 8053.987264,
        "principalBalance": 1881964.042713,
        "principalPayment": 50992.90075,
        "endPrincipalBalance": 1881964.042713,
        "beginPrincipalBalance": 1932956.943463,
        "prepayPrincipalPayment": 15624.009376,
        "scheduledPrincipalPayment": 35368.891375
    }
    {
        "date": "2034-10-20",
        "totalCashFlow": 57038.156912,
        "interestPayment": 7841.516845,
        "principalBalance": 1832767.402646,
        "principalPayment": 49196.640067,
        "endPrincipalBalance": 1832767.402646,
        "beginPrincipalBalance": 1881964.042713,
        "prepayPrincipalPayment": 13961.989922,
        "scheduledPrincipalPayment": 35234.650145
    }
    {
        "date": "2034-11-20",
        "totalCashFlow": 56416.303626,
        "interestPayment": 7636.530844,
        "principalBalance": 1783987.629865,
        "principalPayment": 48779.772782,
        "endPrincipalBalance": 1783987.629865,
        "beginPrincipalBalance": 1832767.402646,
        "prepayPrincipalPayment": 13655.027276,
        "scheduledPrincipalPayment": 35124.745506
    }
    {
        "date": "2034-12-20",
        "totalCashFlow": 55437.596378,
        "interestPayment": 7433.281791,
        "principalBalance": 1735983.315277,
        "principalPayment": 48004.314587,
        "endPrincipalBalance": 1735983.315277,
        "beginPrincipalBalance": 1783987.629865,
        "prepayPrincipalPayment": 12990.390002,
        "scheduledPrincipalPayment": 35013.924585
    }
    {
        "date": "2035-01-20",
        "totalCashFlow": 54699.374373,
        "interestPayment": 7233.263814,
        "principalBalance": 1688517.204718,
        "principalPayment": 47466.11056,
        "endPrincipalBalance": 1688517.204718,
        "beginPrincipalBalance": 1735983.315277,
        "prepayPrincipalPayment": 12556.726129,
        "scheduledPrincipalPayment": 34909.38443
    }
    {
        "date": "2035-02-20",
        "totalCashFlow": 53365.369483,
        "interestPayment": 7035.488353,
        "principalBalance": 1642187.323588,
        "principalPayment": 46329.88113,
        "endPrincipalBalance": 1642187.323588,
        "beginPrincipalBalance": 1688517.204718,
        "prepayPrincipalPayment": 11523.119094,
        "scheduledPrincipalPayment": 34806.762036
    }
    {
        "date": "2035-03-20",
        "totalCashFlow": 52730.388774,
        "interestPayment": 6842.447182,
        "principalBalance": 1596299.381996,
        "principalPayment": 45887.941592,
        "endPrincipalBalance": 1596299.381996,
        "beginPrincipalBalance": 1642187.323588,
        "prepayPrincipalPayment": 11169.039523,
        "scheduledPrincipalPayment": 34718.902069
    }
    {
        "date": "2035-04-20",
        "totalCashFlow": 53328.476004,
        "interestPayment": 6651.247425,
        "principalBalance": 1549622.153417,
        "principalPayment": 46677.228579,
        "endPrincipalBalance": 1549622.153417,
        "beginPrincipalBalance": 1596299.381996,
        "prepayPrincipalPayment": 12045.273419,
        "scheduledPrincipalPayment": 34631.95516
    }
    {
        "date": "2035-05-20",
        "totalCashFlow": 53230.032693,
        "interestPayment": 6456.758973,
        "principalBalance": 1502848.879696,
        "principalPayment": 46773.27372,
        "endPrincipalBalance": 1502848.879696,
        "beginPrincipalBalance": 1549622.153417,
        "prepayPrincipalPayment": 12254.655132,
        "scheduledPrincipalPayment": 34518.618588
    }
    {
        "date": "2035-06-20",
        "totalCashFlow": 53441.588709,
        "interestPayment": 6261.870332,
        "principalBalance": 1455669.161319,
        "principalPayment": 47179.718377,
        "endPrincipalBalance": 1455669.161319,
        "beginPrincipalBalance": 1502848.879696,
        "prepayPrincipalPayment": 12787.076312,
        "scheduledPrincipalPayment": 34392.642065
    }
    {
        "date": "2035-07-20",
        "totalCashFlow": 52751.096574,
        "interestPayment": 6065.288172,
        "principalBalance": 1408983.352917,
        "principalPayment": 46685.808402,
        "endPrincipalBalance": 1408983.352917,
        "beginPrincipalBalance": 1455669.161319,
        "prepayPrincipalPayment": 12440.084956,
        "scheduledPrincipalPayment": 34245.723446
    }
    {
        "date": "2035-08-20",
        "totalCashFlow": 52000.581102,
        "interestPayment": 5870.76397,
        "principalBalance": 1362853.535786,
        "principalPayment": 46129.817132,
        "endPrincipalBalance": 1362853.535786,
        "beginPrincipalBalance": 1408983.352917,
        "prepayPrincipalPayment": 12031.898735,
        "scheduledPrincipalPayment": 34097.918397
    }
    {
        "date": "2035-09-20",
        "totalCashFlow": 51647.749001,
        "interestPayment": 5678.556399,
        "principalBalance": 1316884.343184,
        "principalPayment": 45969.192602,
        "endPrincipalBalance": 1316884.343184,
        "beginPrincipalBalance": 1362853.535786,
        "prepayPrincipalPayment": 12018.41909,
        "scheduledPrincipalPayment": 33950.773512
    }
    {
        "date": "2035-10-20",
        "totalCashFlow": 49863.356467,
        "interestPayment": 5487.018097,
        "principalBalance": 1272508.004814,
        "principalPayment": 44376.33837,
        "endPrincipalBalance": 1272508.004814,
        "beginPrincipalBalance": 1316884.343184,
        "prepayPrincipalPayment": 10582.055443,
        "scheduledPrincipalPayment": 33794.282927
    }
    {
        "date": "2035-11-20",
        "totalCashFlow": 49677.616501,
        "interestPayment": 5302.116687,
        "principalBalance": 1228132.504999,
        "principalPayment": 44375.499814,
        "endPrincipalBalance": 1228132.504999,
        "beginPrincipalBalance": 1272508.004814,
        "prepayPrincipalPayment": 10709.947007,
        "scheduledPrincipalPayment": 33665.552808
    }
    {
        "date": "2035-12-20",
        "totalCashFlow": 48608.767567,
        "interestPayment": 5117.218771,
        "principalBalance": 1184640.956203,
        "principalPayment": 43491.548796,
        "endPrincipalBalance": 1184640.956203,
        "beginPrincipalBalance": 1228132.504999,
        "prepayPrincipalPayment": 9967.687949,
        "scheduledPrincipalPayment": 33523.860847
    }
    {
        "date": "2036-01-20",
        "totalCashFlow": 47895.417395,
        "interestPayment": 4936.003984,
        "principalBalance": 1141681.542792,
        "principalPayment": 42959.413411,
        "endPrincipalBalance": 1141681.542792,
        "beginPrincipalBalance": 1184640.956203,
        "prepayPrincipalPayment": 9566.504578,
        "scheduledPrincipalPayment": 33392.908833
    }
    {
        "date": "2036-02-20",
        "totalCashFlow": 46794.371141,
        "interestPayment": 4757.006428,
        "principalBalance": 1099644.17808,
        "principalPayment": 42037.364712,
        "endPrincipalBalance": 1099644.17808,
        "beginPrincipalBalance": 1141681.542792,
        "prepayPrincipalPayment": 8773.748794,
        "scheduledPrincipalPayment": 33263.615918
    }
    {
        "date": "2036-03-20",
        "totalCashFlow": 46303.072097,
        "interestPayment": 4581.850742,
        "principalBalance": 1057922.956724,
        "principalPayment": 41721.221355,
        "endPrincipalBalance": 1057922.956724,
        "beginPrincipalBalance": 1099644.17808,
        "prepayPrincipalPayment": 8573.22918,
        "scheduledPrincipalPayment": 33147.992175
    }
    {
        "date": "2036-04-20",
        "totalCashFlow": 46243.062364,
        "interestPayment": 4408.01232,
        "principalBalance": 1016087.90668,
        "principalPayment": 41835.050045,
        "endPrincipalBalance": 1016087.90668,
        "beginPrincipalBalance": 1057922.956724,
        "prepayPrincipalPayment": 8806.379383,
        "scheduledPrincipalPayment": 33028.670661
    }
    {
        "date": "2036-05-20",
        "totalCashFlow": 46100.522185,
        "interestPayment": 4233.699611,
        "principalBalance": 974221.084106,
        "principalPayment": 41866.822574,
        "endPrincipalBalance": 974221.084106,
        "beginPrincipalBalance": 1016087.90668,
        "prepayPrincipalPayment": 8975.416666,
        "scheduledPrincipalPayment": 32891.405909
    }
    {
        "date": "2036-06-20",
        "totalCashFlow": 45716.738785,
        "interestPayment": 4059.254517,
        "principalBalance": 932563.599838,
        "principalPayment": 41657.484268,
        "endPrincipalBalance": 932563.599838,
        "beginPrincipalBalance": 974221.084106,
        "prepayPrincipalPayment": 8920.492465,
        "scheduledPrincipalPayment": 32736.991803
    }
    {
        "date": "2036-07-20",
        "totalCashFlow": 45191.411673,
        "interestPayment": 3885.681666,
        "principalBalance": 891257.869831,
        "principalPayment": 41305.730007,
        "endPrincipalBalance": 891257.869831,
        "beginPrincipalBalance": 932563.599838,
        "prepayPrincipalPayment": 8733.808814,
        "scheduledPrincipalPayment": 32571.921193
    }
    {
        "date": "2036-08-20",
        "totalCashFlow": 44611.006034,
        "interestPayment": 3713.574458,
        "principalBalance": 850360.438255,
        "principalPayment": 40897.431576,
        "endPrincipalBalance": 850360.438255,
        "beginPrincipalBalance": 891257.869831,
        "prepayPrincipalPayment": 8497.253938,
        "scheduledPrincipalPayment": 32400.177639
    }
    {
        "date": "2036-09-20",
        "totalCashFlow": 43651.191264,
        "interestPayment": 3543.168493,
        "principalBalance": 810252.415483,
        "principalPayment": 40108.022771,
        "endPrincipalBalance": 810252.415483,
        "beginPrincipalBalance": 850360.438255,
        "prepayPrincipalPayment": 7884.845473,
        "scheduledPrincipalPayment": 32223.177298
    }
    {
        "date": "2036-10-20",
        "totalCashFlow": 42871.457082,
        "interestPayment": 3376.051731,
        "principalBalance": 770757.010132,
        "principalPayment": 39495.405351,
        "endPrincipalBalance": 770757.010132,
        "beginPrincipalBalance": 810252.415483,
        "prepayPrincipalPayment": 7439.971808,
        "scheduledPrincipalPayment": 32055.433543
    }
    {
        "date": "2036-11-20",
        "totalCashFlow": 42211.073456,
        "interestPayment": 3211.487542,
        "principalBalance": 731757.424218,
        "principalPayment": 38999.585913,
        "endPrincipalBalance": 731757.424218,
        "beginPrincipalBalance": 770757.010132,
        "prepayPrincipalPayment": 7108.542525,
        "scheduledPrincipalPayment": 31891.043389
    }
    {
        "date": "2036-12-20",
        "totalCashFlow": 41093.608155,
        "interestPayment": 3048.989268,
        "principalBalance": 693712.805331,
        "principalPayment": 38044.618888,
        "endPrincipalBalance": 693712.805331,
        "beginPrincipalBalance": 731757.424218,
        "prepayPrincipalPayment": 6319.056078,
        "scheduledPrincipalPayment": 31725.562809
    }
    {
        "date": "2037-01-20",
        "totalCashFlow": 40851.668197,
        "interestPayment": 2890.470022,
        "principalBalance": 655751.607156,
        "principalPayment": 37961.198175,
        "endPrincipalBalance": 655751.607156,
        "beginPrincipalBalance": 693712.805331,
        "prepayPrincipalPayment": 6381.325723,
        "scheduledPrincipalPayment": 31579.872452
    }
    {
        "date": "2037-02-20",
        "totalCashFlow": 39690.614787,
        "interestPayment": 2732.298363,
        "principalBalance": 618793.290732,
        "principalPayment": 36958.316424,
        "endPrincipalBalance": 618793.290732,
        "beginPrincipalBalance": 655751.607156,
        "prepayPrincipalPayment": 5542.837976,
        "scheduledPrincipalPayment": 31415.478449
    }
    {
        "date": "2037-03-20",
        "totalCashFlow": 39168.190421,
        "interestPayment": 2578.305378,
        "principalBalance": 582203.405689,
        "principalPayment": 36589.885043,
        "endPrincipalBalance": 582203.405689,
        "beginPrincipalBalance": 618793.290732,
        "prepayPrincipalPayment": 5313.976137,
        "scheduledPrincipalPayment": 31275.908906
    }
    {
        "date": "2037-04-20",
        "totalCashFlow": 39024.809076,
        "interestPayment": 2425.847524,
        "principalBalance": 545604.444137,
        "principalPayment": 36598.961552,
        "endPrincipalBalance": 545604.444137,
        "beginPrincipalBalance": 582203.405689,
        "prepayPrincipalPayment": 5467.243148,
        "scheduledPrincipalPayment": 31131.718404
    }
    {
        "date": "2037-05-20",
        "totalCashFlow": 38623.219048,
        "interestPayment": 2273.351851,
        "principalBalance": 509254.576939,
        "principalPayment": 36349.867198,
        "endPrincipalBalance": 509254.576939,
        "beginPrincipalBalance": 545604.444137,
        "prepayPrincipalPayment": 5389.077731,
        "scheduledPrincipalPayment": 30960.789466
    }
    {
        "date": "2037-06-20",
        "totalCashFlow": 37985.186879,
        "interestPayment": 2121.894071,
        "principalBalance": 473391.284131,
        "principalPayment": 35863.292808,
        "endPrincipalBalance": 473391.284131,
        "beginPrincipalBalance": 509254.576939,
        "prepayPrincipalPayment": 5089.609737,
        "scheduledPrincipalPayment": 30773.683072
    }
    {
        "date": "2037-07-20",
        "totalCashFlow": 37585.68091,
        "interestPayment": 1972.463684,
        "principalBalance": 437778.066905,
        "principalPayment": 35613.217226,
        "endPrincipalBalance": 437778.066905,
        "beginPrincipalBalance": 473391.284131,
        "prepayPrincipalPayment": 5030.626984,
        "scheduledPrincipalPayment": 30582.590242
    }
    {
        "date": "2037-08-20",
        "totalCashFlow": 36871.390778,
        "interestPayment": 1824.075279,
        "principalBalance": 402730.751405,
        "principalPayment": 35047.3155,
        "endPrincipalBalance": 402730.751405,
        "beginPrincipalBalance": 437778.066905,
        "prepayPrincipalPayment": 4676.863306,
        "scheduledPrincipalPayment": 30370.452193
    }
    {
        "date": "2037-09-20",
        "totalCashFlow": 36064.651027,
        "interestPayment": 1678.044798,
        "principalBalance": 368344.145176,
        "principalPayment": 34386.60623,
        "endPrincipalBalance": 368344.145176,
        "beginPrincipalBalance": 402730.751405,
        "prepayPrincipalPayment": 4230.446091,
        "scheduledPrincipalPayment": 30156.160138
    }
    {
        "date": "2037-10-20",
        "totalCashFlow": 35341.623503,
        "interestPayment": 1534.767272,
        "principalBalance": 334537.288944,
        "principalPayment": 33806.856232,
        "endPrincipalBalance": 334537.288944,
        "beginPrincipalBalance": 368344.145176,
        "prepayPrincipalPayment": 3859.69157,
        "scheduledPrincipalPayment": 29947.164662
    }
    {
        "date": "2037-11-20",
        "totalCashFlow": 34615.519934,
        "interestPayment": 1393.905371,
        "principalBalance": 301315.674381,
        "principalPayment": 33221.614563,
        "endPrincipalBalance": 301315.674381,
        "beginPrincipalBalance": 334537.288944,
        "prepayPrincipalPayment": 3483.536538,
        "scheduledPrincipalPayment": 29738.078026
    }
    {
        "date": "2037-12-20",
        "totalCashFlow": 33849.813851,
        "interestPayment": 1255.481977,
        "principalBalance": 268721.342507,
        "principalPayment": 32594.331874,
        "endPrincipalBalance": 268721.342507,
        "beginPrincipalBalance": 301315.674381,
        "prepayPrincipalPayment": 3064.572056,
        "scheduledPrincipalPayment": 29529.759818
    }
    {
        "date": "2038-01-20",
        "totalCashFlow": 33283.757989,
        "interestPayment": 1119.67226,
        "principalBalance": 236557.256779,
        "principalPayment": 32164.085728,
        "endPrincipalBalance": 236557.256779,
        "beginPrincipalBalance": 268721.342507,
        "prepayPrincipalPayment": 2836.638507,
        "scheduledPrincipalPayment": 29327.447221
    }
    {
        "date": "2038-02-20",
        "totalCashFlow": 32393.56878,
        "interestPayment": 985.655237,
        "principalBalance": 205149.343235,
        "principalPayment": 31407.913544,
        "endPrincipalBalance": 205149.343235,
        "beginPrincipalBalance": 236557.256779,
        "prepayPrincipalPayment": 2298.289401,
        "scheduledPrincipalPayment": 29109.624143
    }
    {
        "date": "2038-03-20",
        "totalCashFlow": 31790.112143,
        "interestPayment": 854.78893,
        "principalBalance": 174214.020022,
        "principalPayment": 30935.323213,
        "endPrincipalBalance": 174214.020022,
        "beginPrincipalBalance": 205149.343235,
        "prepayPrincipalPayment": 2019.379013,
        "scheduledPrincipalPayment": 28915.944201
    }
    {
        "date": "2038-04-20",
        "totalCashFlow": 31265.863285,
        "interestPayment": 725.89175,
        "principalBalance": 143674.048487,
        "principalPayment": 30539.971535,
        "endPrincipalBalance": 143674.048487,
        "beginPrincipalBalance": 174214.020022,
        "prepayPrincipalPayment": 1827.445969,
        "scheduledPrincipalPayment": 28712.525566
    }
    {
        "date": "2038-05-20",
        "totalCashFlow": 30567.483992,
        "interestPayment": 598.641869,
        "principalBalance": 113705.206364,
        "principalPayment": 29968.842123,
        "endPrincipalBalance": 113705.206364,
        "beginPrincipalBalance": 143674.048487,
        "prepayPrincipalPayment": 1490.060679,
        "scheduledPrincipalPayment": 28478.781444
    }
    {
        "date": "2038-06-20",
        "totalCashFlow": 29841.556843,
        "interestPayment": 473.771693,
        "principalBalance": 84337.421214,
        "principalPayment": 29367.78515,
        "endPrincipalBalance": 84337.421214,
        "beginPrincipalBalance": 113705.206364,
        "prepayPrincipalPayment": 1131.585127,
        "scheduledPrincipalPayment": 28236.200022
    }
    {
        "date": "2038-07-20",
        "totalCashFlow": 29126.135077,
        "interestPayment": 351.405922,
        "principalBalance": 55562.692059,
        "principalPayment": 28774.729155,
        "endPrincipalBalance": 55562.692059,
        "beginPrincipalBalance": 84337.421214,
        "prepayPrincipalPayment": 787.684259,
        "scheduledPrincipalPayment": 27987.044896
    }
    {
        "date": "2038-08-20",
        "totalCashFlow": 28339.059168,
        "interestPayment": 231.511217,
        "principalBalance": 27455.144108,
        "principalPayment": 28107.547951,
        "endPrincipalBalance": 27455.144108,
        "beginPrincipalBalance": 55562.692059,
        "prepayPrincipalPayment": 388.223908,
        "scheduledPrincipalPayment": 27719.324044
    }
    {
        "date": "2038-09-20",
        "totalCashFlow": 27569.540542,
        "interestPayment": 114.396434,
        "principalBalance": 0.0,
        "principalPayment": 27455.144108,
        "endPrincipalBalance": 0.0,
        "beginPrincipalBalance": 27455.144108,
        "prepayPrincipalPayment": 0.0,
        "scheduledPrincipalPayment": 27455.144108
    }

    """

    try:
        logger.info("Calling get_cash_flow_async")

        response = Client().yield_book_rest.get_cash_flow_async(
            id=id,
            id_type=id_type,
            pricing_date=pricing_date,
            par_amount=par_amount,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called get_cash_flow_async")

        return output
    except Exception as err:
        logger.error("Error get_cash_flow_async.")
        check_exception_and_raise(err, logger)


def get_cash_flow_sync(
    *,
    id: str,
    id_type: Optional[str] = None,
    pricing_date: Optional[str] = None,
    par_amount: Optional[str] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Get cash flow sync.

    Parameters
    ----------
    id : str
        Security reference ID.
    id_type : str, optional
        A sequence of textual characters.
    pricing_date : str, optional
        A sequence of textual characters.
    par_amount : str, optional
        A sequence of textual characters.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------
    >>> # Formulate and execute the get request by using instrument ID and Par_amount
    >>> cf_sync_get_response = get_cash_flow_sync(
    >>>             id='01F002628', #01F002628
    >>>             par_amount="10000"
    >>>         )
    >>>
    >>> # Print full output to a file, as CF output is too long for terminal printout
    >>> # print(js.dumps(cf_sync_get_response, indent=4), file=open('.\\CF_sync_get_output.json', 'w+'))
    >>>
    >>> # Print onyl payment information
    >>> for paymentInfo in cf_sync_get_response["data"]["cashFlow"]["dataPaymentList"]:
    >>>     print(js.dumps(paymentInfo, indent=4))
    {
        "date": "2026-03-25",
        "totalCashFlow": 44637.115742,
        "interestPayment": 4166.666667,
        "principalBalance": 9959529.550924,
        "principalPayment": 40470.449076,
        "endPrincipalBalance": 9959529.550924,
        "beginPrincipalBalance": 10000000.0,
        "prepayPrincipalPayment": 15510.346058,
        "scheduledPrincipalPayment": 24960.103018
    }
    {
        "date": "2026-04-25",
        "totalCashFlow": 48170.979212,
        "interestPayment": 4149.80398,
        "principalBalance": 9915508.375692,
        "principalPayment": 44021.175232,
        "endPrincipalBalance": 9915508.375692,
        "beginPrincipalBalance": 9959529.550924,
        "prepayPrincipalPayment": 19073.923391,
        "scheduledPrincipalPayment": 24947.251841
    }
    {
        "date": "2026-05-25",
        "totalCashFlow": 50416.007165,
        "interestPayment": 4131.461823,
        "principalBalance": 9869223.83035,
        "principalPayment": 46284.545342,
        "endPrincipalBalance": 9869223.83035,
        "beginPrincipalBalance": 9915508.375692,
        "prepayPrincipalPayment": 21359.254205,
        "scheduledPrincipalPayment": 24925.291137
    }
    {
        "date": "2026-06-25",
        "totalCashFlow": 50868.01161,
        "interestPayment": 4112.176596,
        "principalBalance": 9822467.995335,
        "principalPayment": 46755.835014,
        "endPrincipalBalance": 9822467.995335,
        "beginPrincipalBalance": 9869223.83035,
        "prepayPrincipalPayment": 21858.46363,
        "scheduledPrincipalPayment": 24897.371385
    }
    {
        "date": "2026-07-25",
        "totalCashFlow": 53653.653613,
        "interestPayment": 4092.694998,
        "principalBalance": 9772907.036721,
        "principalPayment": 49560.958615,
        "endPrincipalBalance": 9772907.036721,
        "beginPrincipalBalance": 9822467.995335,
        "prepayPrincipalPayment": 24692.992484,
        "scheduledPrincipalPayment": 24867.966131
    }
    {
        "date": "2026-08-25",
        "totalCashFlow": 53661.320385,
        "interestPayment": 4072.044599,
        "principalBalance": 9723317.760935,
        "principalPayment": 49589.275786,
        "endPrincipalBalance": 9723317.760935,
        "beginPrincipalBalance": 9772907.036721,
        "prepayPrincipalPayment": 24758.145802,
        "scheduledPrincipalPayment": 24831.129984
    }
    {
        "date": "2026-09-25",
        "totalCashFlow": 52350.554473,
        "interestPayment": 4051.3824,
        "principalBalance": 9675018.588862,
        "principalPayment": 48299.172073,
        "endPrincipalBalance": 9675018.588862,
        "beginPrincipalBalance": 9723317.760935,
        "prepayPrincipalPayment": 23505.308082,
        "scheduledPrincipalPayment": 24793.863991
    }
    {
        "date": "2026-10-25",
        "totalCashFlow": 51710.109422,
        "interestPayment": 4031.257745,
        "principalBalance": 9627339.737185,
        "principalPayment": 47678.851677,
        "endPrincipalBalance": 9627339.737185,
        "beginPrincipalBalance": 9675018.588862,
        "prepayPrincipalPayment": 22919.313659,
        "scheduledPrincipalPayment": 24759.538018
    }
    {
        "date": "2026-11-25",
        "totalCashFlow": 50772.994289,
        "interestPayment": 4011.391557,
        "principalBalance": 9580578.134453,
        "principalPayment": 46761.602732,
        "endPrincipalBalance": 9580578.134453,
        "beginPrincipalBalance": 9627339.737185,
        "prepayPrincipalPayment": 22035.138553,
        "scheduledPrincipalPayment": 24726.464179
    }
    {
        "date": "2026-12-25",
        "totalCashFlow": 48984.768102,
        "interestPayment": 3991.907556,
        "principalBalance": 9535585.273907,
        "principalPayment": 44992.860546,
        "endPrincipalBalance": 9535585.273907,
        "beginPrincipalBalance": 9580578.134453,
        "prepayPrincipalPayment": 20297.438612,
        "scheduledPrincipalPayment": 24695.421935
    }
    {
        "date": "2027-01-25",
        "totalCashFlow": 50577.469607,
        "interestPayment": 3973.160531,
        "principalBalance": 9488980.964831,
        "principalPayment": 46604.309076,
        "endPrincipalBalance": 9488980.964831,
        "beginPrincipalBalance": 9535585.273907,
        "prepayPrincipalPayment": 21935.672382,
        "scheduledPrincipalPayment": 24668.636694
    }
    {
        "date": "2027-02-25",
        "totalCashFlow": 45557.230703,
        "interestPayment": 3953.742069,
        "principalBalance": 9447377.476196,
        "principalPayment": 41603.488635,
        "endPrincipalBalance": 9447377.476196,
        "beginPrincipalBalance": 9488980.964831,
        "prepayPrincipalPayment": 16966.109661,
        "scheduledPrincipalPayment": 24637.378974
    }
    {
        "date": "2027-03-25",
        "totalCashFlow": 46422.801029,
        "interestPayment": 3936.407282,
        "principalBalance": 9404891.082448,
        "principalPayment": 42486.393748,
        "endPrincipalBalance": 9404891.082448,
        "beginPrincipalBalance": 9447377.476196,
        "prepayPrincipalPayment": 17867.562661,
        "scheduledPrincipalPayment": 24618.831087
    }
    {
        "date": "2027-04-25",
        "totalCashFlow": 50509.820631,
        "interestPayment": 3918.704618,
        "principalBalance": 9358299.966435,
        "principalPayment": 46591.116014,
        "endPrincipalBalance": 9358299.966435,
        "beginPrincipalBalance": 9404891.082448,
        "prepayPrincipalPayment": 21993.3715,
        "scheduledPrincipalPayment": 24597.744514
    }
    {
        "date": "2027-05-25",
        "totalCashFlow": 52159.072279,
        "interestPayment": 3899.291653,
        "principalBalance": 9310040.185808,
        "principalPayment": 48259.780627,
        "endPrincipalBalance": 9310040.185808,
        "beginPrincipalBalance": 9358299.966435,
        "prepayPrincipalPayment": 23694.146291,
        "scheduledPrincipalPayment": 24565.634336
    }
    {
        "date": "2027-06-25",
        "totalCashFlow": 52278.297829,
        "interestPayment": 3879.183411,
        "principalBalance": 9261641.07139,
        "principalPayment": 48399.114418,
        "endPrincipalBalance": 9261641.07139,
        "beginPrincipalBalance": 9310040.185808,
        "prepayPrincipalPayment": 23870.316917,
        "scheduledPrincipalPayment": 24528.797501
    }
    {
        "date": "2027-07-25",
        "totalCashFlow": 54945.056444,
        "interestPayment": 3859.017113,
        "principalBalance": 9210555.032058,
        "principalPayment": 51086.039331,
        "endPrincipalBalance": 9210555.032058,
        "beginPrincipalBalance": 9261641.07139,
        "prepayPrincipalPayment": 26594.813002,
        "scheduledPrincipalPayment": 24491.226329
    }
    {
        "date": "2027-08-25",
        "totalCashFlow": 53578.170436,
        "interestPayment": 3837.731263,
        "principalBalance": 9160814.592885,
        "principalPayment": 49740.439173,
        "endPrincipalBalance": 9160814.592885,
        "beginPrincipalBalance": 9210555.032058,
        "prepayPrincipalPayment": 25294.287648,
        "scheduledPrincipalPayment": 24446.151525
    }
    {
        "date": "2027-09-25",
        "totalCashFlow": 53767.659416,
        "interestPayment": 3817.00608,
        "principalBalance": 9110863.939549,
        "principalPayment": 49950.653336,
        "endPrincipalBalance": 9110863.939549,
        "beginPrincipalBalance": 9160814.592885,
        "prepayPrincipalPayment": 25546.420563,
        "scheduledPrincipalPayment": 24404.232773
    }
    {
        "date": "2027-10-25",
        "totalCashFlow": 52136.840621,
        "interestPayment": 3796.193308,
        "principalBalance": 9062523.292237,
        "principalPayment": 48340.647313,
        "endPrincipalBalance": 9062523.292237,
        "beginPrincipalBalance": 9110863.939549,
        "prepayPrincipalPayment": 23979.301496,
        "scheduledPrincipalPayment": 24361.345817
    }
    {
        "date": "2027-11-25",
        "totalCashFlow": 50431.951306,
        "interestPayment": 3776.051372,
        "principalBalance": 9015867.392303,
        "principalPayment": 46655.899934,
        "endPrincipalBalance": 9015867.392303,
        "beginPrincipalBalance": 9062523.292237,
        "prepayPrincipalPayment": 22333.534332,
        "scheduledPrincipalPayment": 24322.365602
    }
    {
        "date": "2027-12-25",
        "totalCashFlow": 50234.767014,
        "interestPayment": 3756.611413,
        "principalBalance": 8969389.236702,
        "principalPayment": 46478.1556,
        "endPrincipalBalance": 8969389.236702,
        "beginPrincipalBalance": 9015867.392303,
        "prepayPrincipalPayment": 22190.617748,
        "scheduledPrincipalPayment": 24287.537853
    }
    {
        "date": "2028-01-25",
        "totalCashFlow": 50522.135786,
        "interestPayment": 3737.245515,
        "principalBalance": 8922604.346432,
        "principalPayment": 46784.89027,
        "endPrincipalBalance": 8922604.346432,
        "beginPrincipalBalance": 8969389.236702,
        "prepayPrincipalPayment": 22532.055356,
        "scheduledPrincipalPayment": 24252.834915
    }
    {
        "date": "2028-02-25",
        "totalCashFlow": 46489.472956,
        "interestPayment": 3717.751811,
        "principalBalance": 8879832.625287,
        "principalPayment": 42771.721145,
        "endPrincipalBalance": 8879832.625287,
        "beginPrincipalBalance": 8922604.346432,
        "prepayPrincipalPayment": 18554.777373,
        "scheduledPrincipalPayment": 24216.943772
    }
    {
        "date": "2028-03-25",
        "totalCashFlow": 47550.997068,
        "interestPayment": 3699.930261,
        "principalBalance": 8835981.558479,
        "principalPayment": 43851.066808,
        "endPrincipalBalance": 8835981.558479,
        "beginPrincipalBalance": 8879832.625287,
        "prepayPrincipalPayment": 19659.446443,
        "scheduledPrincipalPayment": 24191.620364
    }
    {
        "date": "2028-04-25",
        "totalCashFlow": 51883.964591,
        "interestPayment": 3681.658983,
        "principalBalance": 8787779.252871,
        "principalPayment": 48202.305608,
        "endPrincipalBalance": 8787779.252871,
        "beginPrincipalBalance": 8835981.558479,
        "prepayPrincipalPayment": 24039.24677,
        "scheduledPrincipalPayment": 24163.058838
    }
    {
        "date": "2028-05-25",
        "totalCashFlow": 51165.743375,
        "interestPayment": 3661.574689,
        "principalBalance": 8740275.084185,
        "principalPayment": 47504.168687,
        "endPrincipalBalance": 8740275.084185,
        "beginPrincipalBalance": 8787779.252871,
        "prepayPrincipalPayment": 23381.927147,
        "scheduledPrincipalPayment": 24122.24154
    }
    {
        "date": "2028-06-25",
        "totalCashFlow": 55719.097174,
        "interestPayment": 3641.781285,
        "principalBalance": 8688197.768295,
        "principalPayment": 52077.315889,
        "endPrincipalBalance": 8688197.768295,
        "beginPrincipalBalance": 8740275.084185,
        "prepayPrincipalPayment": 27994.373545,
        "scheduledPrincipalPayment": 24082.942344
    }
    {
        "date": "2028-07-25",
        "totalCashFlow": 56819.152259,
        "interestPayment": 3620.082403,
        "principalBalance": 8634998.69844,
        "principalPayment": 53199.069856,
        "endPrincipalBalance": 8634998.69844,
        "beginPrincipalBalance": 8688197.768295,
        "prepayPrincipalPayment": 29168.470472,
        "scheduledPrincipalPayment": 24030.599384
    }
    {
        "date": "2028-08-25",
        "totalCashFlow": 54323.025402,
        "interestPayment": 3597.916124,
        "principalBalance": 8584273.589162,
        "principalPayment": 50725.109278,
        "endPrincipalBalance": 8584273.589162,
        "beginPrincipalBalance": 8634998.69844,
        "prepayPrincipalPayment": 26750.462834,
        "scheduledPrincipalPayment": 23974.646444
    }
    {
        "date": "2028-09-25",
        "totalCashFlow": 56701.102664,
        "interestPayment": 3576.780662,
        "principalBalance": 8531149.26716,
        "principalPayment": 53124.322002,
        "endPrincipalBalance": 8531149.26716,
        "beginPrincipalBalance": 8584273.589162,
        "prepayPrincipalPayment": 29199.25767,
        "scheduledPrincipalPayment": 23925.064332
    }
    {
        "date": "2028-10-25",
        "totalCashFlow": 52805.220215,
        "interestPayment": 3554.645528,
        "principalBalance": 8481898.692473,
        "principalPayment": 49250.574687,
        "endPrincipalBalance": 8481898.692473,
        "beginPrincipalBalance": 8531149.26716,
        "prepayPrincipalPayment": 25382.281561,
        "scheduledPrincipalPayment": 23868.293126
    }
    {
        "date": "2028-11-25",
        "totalCashFlow": 52749.889863,
        "interestPayment": 3534.124455,
        "principalBalance": 8432682.927066,
        "principalPayment": 49215.765407,
        "endPrincipalBalance": 8432682.927066,
        "beginPrincipalBalance": 8481898.692473,
        "prepayPrincipalPayment": 25393.896978,
        "scheduledPrincipalPayment": 23821.868429
    }
    {
        "date": "2028-12-25",
        "totalCashFlow": 51593.187717,
        "interestPayment": 3513.617886,
        "principalBalance": 8384603.357235,
        "principalPayment": 48079.569831,
        "endPrincipalBalance": 8384603.357235,
        "beginPrincipalBalance": 8432682.927066,
        "prepayPrincipalPayment": 24304.482452,
        "scheduledPrincipalPayment": 23775.087379
    }
    {
        "date": "2029-01-25",
        "totalCashFlow": 50992.947468,
        "interestPayment": 3493.584732,
        "principalBalance": 8337103.9945,
        "principalPayment": 47499.362735,
        "endPrincipalBalance": 8337103.9945,
        "beginPrincipalBalance": 8384603.357235,
        "prepayPrincipalPayment": 23768.298968,
        "scheduledPrincipalPayment": 23731.063768
    }
    {
        "date": "2029-02-25",
        "totalCashFlow": 48009.60611,
        "interestPayment": 3473.793331,
        "principalBalance": 8292568.18172,
        "principalPayment": 44535.812779,
        "endPrincipalBalance": 8292568.18172,
        "beginPrincipalBalance": 8337103.9945,
        "prepayPrincipalPayment": 20847.562127,
        "scheduledPrincipalPayment": 23688.250652
    }
    {
        "date": "2029-03-25",
        "totalCashFlow": 47671.240019,
        "interestPayment": 3455.236742,
        "principalBalance": 8248352.178444,
        "principalPayment": 44216.003276,
        "endPrincipalBalance": 8248352.178444,
        "beginPrincipalBalance": 8292568.18172,
        "prepayPrincipalPayment": 20562.542294,
        "scheduledPrincipalPayment": 23653.460982
    }
    {
        "date": "2029-04-25",
        "totalCashFlow": 52059.845403,
        "interestPayment": 3436.813408,
        "principalBalance": 8199729.146448,
        "principalPayment": 48623.031996,
        "endPrincipalBalance": 8199729.146448,
        "beginPrincipalBalance": 8248352.178444,
        "prepayPrincipalPayment": 25003.812987,
        "scheduledPrincipalPayment": 23619.219008
    }
    {
        "date": "2029-05-25",
        "totalCashFlow": 54179.621946,
        "interestPayment": 3416.553811,
        "principalBalance": 8148966.078314,
        "principalPayment": 50763.068135,
        "endPrincipalBalance": 8148966.078314,
        "beginPrincipalBalance": 8199729.146448,
        "prepayPrincipalPayment": 27191.124789,
        "scheduledPrincipalPayment": 23571.943345
    }
    {
        "date": "2029-06-25",
        "totalCashFlow": 57827.768994,
        "interestPayment": 3395.402533,
        "principalBalance": 8094533.711853,
        "principalPayment": 54432.366461,
        "endPrincipalBalance": 8094533.711853,
        "beginPrincipalBalance": 8148966.078314,
        "prepayPrincipalPayment": 30914.342953,
        "scheduledPrincipalPayment": 23518.023508
    }
    {
        "date": "2029-07-25",
        "totalCashFlow": 57650.842821,
        "interestPayment": 3372.72238,
        "principalBalance": 8040255.591411,
        "principalPayment": 54278.120441,
        "endPrincipalBalance": 8040255.591411,
        "beginPrincipalBalance": 8094533.711853,
        "prepayPrincipalPayment": 30825.169632,
        "scheduledPrincipalPayment": 23452.95081
    }
    {
        "date": "2029-08-25",
        "totalCashFlow": 57097.963859,
        "interestPayment": 3350.106496,
        "principalBalance": 7986507.734048,
        "principalPayment": 53747.857363,
        "endPrincipalBalance": 7986507.734048,
        "beginPrincipalBalance": 8040255.591411,
        "prepayPrincipalPayment": 30360.141494,
        "scheduledPrincipalPayment": 23387.715868
    }
    {
        "date": "2029-09-25",
        "totalCashFlow": 58375.410503,
        "interestPayment": 3327.711556,
        "principalBalance": 7931460.035102,
        "principalPayment": 55047.698947,
        "endPrincipalBalance": 7931460.035102,
        "beginPrincipalBalance": 7986507.734048,
        "prepayPrincipalPayment": 31724.283182,
        "scheduledPrincipalPayment": 23323.415765
    }
    {
        "date": "2029-10-25",
        "totalCashFlow": 52710.07247,
        "interestPayment": 3304.775015,
        "principalBalance": 7882054.737646,
        "principalPayment": 49405.297456,
        "endPrincipalBalance": 7882054.737646,
        "beginPrincipalBalance": 7931460.035102,
        "prepayPrincipalPayment": 26150.600688,
        "scheduledPrincipalPayment": 23254.696768
    }
    {
        "date": "2029-11-25",
        "totalCashFlow": 54633.378368,
        "interestPayment": 3284.189474,
        "principalBalance": 7830705.548752,
        "principalPayment": 51349.188894,
        "endPrincipalBalance": 7830705.548752,
        "beginPrincipalBalance": 7882054.737646,
        "prepayPrincipalPayment": 28147.246474,
        "scheduledPrincipalPayment": 23201.94242
    }
    {
        "date": "2029-12-25",
        "totalCashFlow": 52174.521902,
        "interestPayment": 3262.793979,
        "principalBalance": 7781793.820829,
        "principalPayment": 48911.727923,
        "endPrincipalBalance": 7781793.820829,
        "beginPrincipalBalance": 7830705.548752,
        "prepayPrincipalPayment": 25768.803392,
        "scheduledPrincipalPayment": 23142.924532
    }
    {
        "date": "2030-01-25",
        "totalCashFlow": 51364.879127,
        "interestPayment": 3242.414092,
        "principalBalance": 7733671.355794,
        "principalPayment": 48122.465035,
        "endPrincipalBalance": 7733671.355794,
        "beginPrincipalBalance": 7781793.820829,
        "prepayPrincipalPayment": 25031.89591,
        "scheduledPrincipalPayment": 23090.569126
    }
    {
        "date": "2030-02-25",
        "totalCashFlow": 47981.274788,
        "interestPayment": 3222.363065,
        "principalBalance": 7688912.444071,
        "principalPayment": 44758.911723,
        "endPrincipalBalance": 7688912.444071,
        "beginPrincipalBalance": 7733671.355794,
        "prepayPrincipalPayment": 21718.8646,
        "scheduledPrincipalPayment": 23040.047123
    }
    {
        "date": "2030-03-25",
        "totalCashFlow": 47445.546842,
        "interestPayment": 3203.713518,
        "principalBalance": 7644670.610747,
        "principalPayment": 44241.833324,
        "endPrincipalBalance": 7644670.610747,
        "beginPrincipalBalance": 7688912.444071,
        "prepayPrincipalPayment": 21242.751639,
        "scheduledPrincipalPayment": 22999.081685
    }
    {
        "date": "2030-04-25",
        "totalCashFlow": 51484.524111,
        "interestPayment": 3185.279421,
        "principalBalance": 7596371.366058,
        "principalPayment": 48299.24469,
        "endPrincipalBalance": 7596371.366058,
        "beginPrincipalBalance": 7644670.610747,
        "prepayPrincipalPayment": 25340.003988,
        "scheduledPrincipalPayment": 22959.240701
    }
    {
        "date": "2030-05-25",
        "totalCashFlow": 54595.089219,
        "interestPayment": 3165.154736,
        "principalBalance": 7544941.431575,
        "principalPayment": 51429.934483,
        "endPrincipalBalance": 7544941.431575,
        "beginPrincipalBalance": 7596371.366058,
        "prepayPrincipalPayment": 28523.190308,
        "scheduledPrincipalPayment": 22906.744174
    }
    {
        "date": "2030-06-25",
        "totalCashFlow": 57656.339632,
        "interestPayment": 3143.725596,
        "principalBalance": 7490428.81754,
        "principalPayment": 54512.614035,
        "endPrincipalBalance": 7490428.81754,
        "beginPrincipalBalance": 7544941.431575,
        "prepayPrincipalPayment": 31668.369939,
        "scheduledPrincipalPayment": 22844.244097
    }
    {
        "date": "2030-07-25",
        "totalCashFlow": 56078.158764,
        "interestPayment": 3121.012007,
        "principalBalance": 7437471.670783,
        "principalPayment": 52957.146757,
        "endPrincipalBalance": 7437471.670783,
        "beginPrincipalBalance": 7490428.81754,
        "prepayPrincipalPayment": 30185.382058,
        "scheduledPrincipalPayment": 22771.764699
    }
    {
        "date": "2030-08-25",
        "totalCashFlow": 58017.552668,
        "interestPayment": 3098.946529,
        "principalBalance": 7382553.064645,
        "principalPayment": 54918.606138,
        "endPrincipalBalance": 7382553.064645,
        "beginPrincipalBalance": 7437471.670783,
        "prepayPrincipalPayment": 32215.263598,
        "scheduledPrincipalPayment": 22703.34254
    }
    {
        "date": "2030-09-25",
        "totalCashFlow": 56787.971437,
        "interestPayment": 3076.063777,
        "principalBalance": 7328841.156985,
        "principalPayment": 53711.90766,
        "endPrincipalBalance": 7328841.156985,
        "beginPrincipalBalance": 7382553.064645,
        "prepayPrincipalPayment": 31083.658746,
        "scheduledPrincipalPayment": 22628.248914
    }
    {
        "date": "2030-10-25",
        "totalCashFlow": 53207.628744,
        "interestPayment": 3053.683815,
        "principalBalance": 7278687.212056,
        "principalPayment": 50153.944929,
        "endPrincipalBalance": 7278687.212056,
        "beginPrincipalBalance": 7328841.156985,
        "prepayPrincipalPayment": 27597.791856,
        "scheduledPrincipalPayment": 22556.153073
    }
    {
        "date": "2030-11-25",
        "totalCashFlow": 53967.169068,
        "interestPayment": 3032.786338,
        "principalBalance": 7227752.829327,
        "principalPayment": 50934.38273,
        "endPrincipalBalance": 7227752.829327,
        "beginPrincipalBalance": 7278687.212056,
        "prepayPrincipalPayment": 28440.023035,
        "scheduledPrincipalPayment": 22494.359694
    }
    {
        "date": "2030-12-25",
        "totalCashFlow": 50291.138143,
        "interestPayment": 3011.563679,
        "principalBalance": 7180473.254863,
        "principalPayment": 47279.574464,
        "endPrincipalBalance": 7180473.254863,
        "beginPrincipalBalance": 7227752.829327,
        "prepayPrincipalPayment": 24850.039689,
        "scheduledPrincipalPayment": 22429.534775
    }
    {
        "date": "2031-01-25",
        "totalCashFlow": 51512.65407,
        "interestPayment": 2991.863856,
        "principalBalance": 7131952.46465,
        "principalPayment": 48520.790214,
        "endPrincipalBalance": 7131952.46465,
        "beginPrincipalBalance": 7180473.254863,
        "prepayPrincipalPayment": 26145.327897,
        "scheduledPrincipalPayment": 22375.462317
    }
    {
        "date": "2031-02-25",
        "totalCashFlow": 46947.429024,
        "interestPayment": 2971.64686,
        "principalBalance": 7087976.682486,
        "principalPayment": 43975.782163,
        "endPrincipalBalance": 7087976.682486,
        "beginPrincipalBalance": 7131952.46465,
        "prepayPrincipalPayment": 21658.824757,
        "scheduledPrincipalPayment": 22316.957406
    }
    {
        "date": "2031-03-25",
        "totalCashFlow": 46359.183705,
        "interestPayment": 2953.323618,
        "principalBalance": 7044570.822399,
        "principalPayment": 43405.860087,
        "endPrincipalBalance": 7044570.822399,
        "beginPrincipalBalance": 7087976.682486,
        "prepayPrincipalPayment": 21133.713146,
        "scheduledPrincipalPayment": 22272.146941
    }
    {
        "date": "2031-04-25",
        "totalCashFlow": 50463.570747,
        "interestPayment": 2935.237843,
        "principalBalance": 6997042.489494,
        "principalPayment": 47528.332905,
        "endPrincipalBalance": 6997042.489494,
        "beginPrincipalBalance": 7044570.822399,
        "prepayPrincipalPayment": 25299.671796,
        "scheduledPrincipalPayment": 22228.661109
    }
    {
        "date": "2031-05-25",
        "totalCashFlow": 53620.365013,
        "interestPayment": 2915.434371,
        "principalBalance": 6946337.558852,
        "principalPayment": 50704.930642,
        "endPrincipalBalance": 6946337.558852,
        "beginPrincipalBalance": 6997042.489494,
        "prepayPrincipalPayment": 28533.282182,
        "scheduledPrincipalPayment": 22171.64846
    }
    {
        "date": "2031-06-25",
        "totalCashFlow": 55448.337901,
        "interestPayment": 2894.307316,
        "principalBalance": 6893783.528267,
        "principalPayment": 52554.030585,
        "endPrincipalBalance": 6893783.528267,
        "beginPrincipalBalance": 6946337.558852,
        "prepayPrincipalPayment": 30450.082445,
        "scheduledPrincipalPayment": 22103.94814
    }
    {
        "date": "2031-07-25",
        "totalCashFlow": 56398.344454,
        "interestPayment": 2872.409803,
        "principalBalance": 6840257.593617,
        "principalPayment": 53525.93465,
        "endPrincipalBalance": 6840257.593617,
        "beginPrincipalBalance": 6893783.528267,
        "prepayPrincipalPayment": 31496.267374,
        "scheduledPrincipalPayment": 22029.667277
    }
    {
        "date": "2031-08-25",
        "totalCashFlow": 56966.188441,
        "interestPayment": 2850.107331,
        "principalBalance": 6786141.512507,
        "principalPayment": 54116.08111,
        "endPrincipalBalance": 6786141.512507,
        "beginPrincipalBalance": 6840257.593617,
        "prepayPrincipalPayment": 32164.543087,
        "scheduledPrincipalPayment": 21951.538023
    }
    {
        "date": "2031-09-25",
        "totalCashFlow": 54418.102498,
        "interestPayment": 2827.558964,
        "principalBalance": 6734550.968972,
        "principalPayment": 51590.543534,
        "endPrincipalBalance": 6734550.968972,
        "beginPrincipalBalance": 6786141.512507,
        "prepayPrincipalPayment": 29719.800949,
        "scheduledPrincipalPayment": 21870.742585
    }
    {
        "date": "2031-10-25",
        "totalCashFlow": 53142.252714,
        "interestPayment": 2806.062904,
        "principalBalance": 6684214.779162,
        "principalPayment": 50336.18981,
        "endPrincipalBalance": 6684214.779162,
        "beginPrincipalBalance": 6734550.968972,
        "prepayPrincipalPayment": 28538.857565,
        "scheduledPrincipalPayment": 21797.332245
    }
    {
        "date": "2031-11-25",
        "totalCashFlow": 52666.379229,
        "interestPayment": 2785.089491,
        "principalBalance": 6634333.489425,
        "principalPayment": 49881.289737,
        "endPrincipalBalance": 6634333.489425,
        "beginPrincipalBalance": 6684214.779162,
        "prepayPrincipalPayment": 28154.018481,
        "scheduledPrincipalPayment": 21727.271257
    }
    {
        "date": "2031-12-25",
        "totalCashFlow": 47826.131919,
        "interestPayment": 2764.305621,
        "principalBalance": 6589271.663127,
        "principalPayment": 45061.826299,
        "endPrincipalBalance": 6589271.663127,
        "beginPrincipalBalance": 6634333.489425,
        "prepayPrincipalPayment": 23403.832163,
        "scheduledPrincipalPayment": 21657.994136
    }
    {
        "date": "2032-01-25",
        "totalCashFlow": 51144.691418,
        "interestPayment": 2745.52986,
        "principalBalance": 6540872.501568,
        "principalPayment": 48399.161558,
        "endPrincipalBalance": 6540872.501568,
        "beginPrincipalBalance": 6589271.663127,
        "prepayPrincipalPayment": 26795.339653,
        "scheduledPrincipalPayment": 21603.821905
    }
    {
        "date": "2032-02-25",
        "totalCashFlow": 44622.959229,
        "interestPayment": 2725.363542,
        "principalBalance": 6498974.905882,
        "principalPayment": 41897.595686,
        "endPrincipalBalance": 6498974.905882,
        "beginPrincipalBalance": 6540872.501568,
        "prepayPrincipalPayment": 20359.502756,
        "scheduledPrincipalPayment": 21538.09293
    }
    {
        "date": "2032-03-25",
        "totalCashFlow": 44826.511946,
        "interestPayment": 2707.906211,
        "principalBalance": 6456856.300147,
        "principalPayment": 42118.605735,
        "endPrincipalBalance": 6456856.300147,
        "beginPrincipalBalance": 6498974.905882,
        "prepayPrincipalPayment": 20625.40957,
        "scheduledPrincipalPayment": 21493.196165
    }
    {
        "date": "2032-04-25",
        "totalCashFlow": 50427.549487,
        "interestPayment": 2690.356792,
        "principalBalance": 6409119.107452,
        "principalPayment": 47737.192695,
        "endPrincipalBalance": 6409119.107452,
        "beginPrincipalBalance": 6456856.300147,
        "prepayPrincipalPayment": 26290.117087,
        "scheduledPrincipalPayment": 21447.075609
    }
    {
        "date": "2032-05-25",
        "totalCashFlow": 52619.649872,
        "interestPayment": 2670.466295,
        "principalBalance": 6359169.923874,
        "principalPayment": 49949.183577,
        "endPrincipalBalance": 6359169.923874,
        "beginPrincipalBalance": 6409119.107452,
        "prepayPrincipalPayment": 28567.474736,
        "scheduledPrincipalPayment": 21381.708842
    }
    {
        "date": "2032-06-25",
        "totalCashFlow": 52580.811692,
        "interestPayment": 2649.654135,
        "principalBalance": 6309238.766318,
        "principalPayment": 49931.157557,
        "endPrincipalBalance": 6309238.766318,
        "beginPrincipalBalance": 6359169.923874,
        "prepayPrincipalPayment": 28622.899777,
        "scheduledPrincipalPayment": 21308.25778
    }
    {
        "date": "2032-07-25",
        "totalCashFlow": 56093.030919,
        "interestPayment": 2628.849486,
        "principalBalance": 6255774.584885,
        "principalPayment": 53464.181433,
        "endPrincipalBalance": 6255774.584885,
        "beginPrincipalBalance": 6309238.766318,
        "prepayPrincipalPayment": 32230.059639,
        "scheduledPrincipalPayment": 21234.121794
    }
    {
        "date": "2032-08-25",
        "totalCashFlow": 53947.916974,
        "interestPayment": 2606.572744,
        "principalBalance": 6204433.240655,
        "principalPayment": 51341.34423,
        "endPrincipalBalance": 6204433.240655,
        "beginPrincipalBalance": 6255774.584885,
        "prepayPrincipalPayment": 30194.055435,
        "scheduledPrincipalPayment": 21147.288795
    }
    {
        "date": "2032-09-25",
        "totalCashFlow": 53847.389446,
        "interestPayment": 2585.180517,
        "principalBalance": 6153171.031726,
        "principalPayment": 51262.208929,
        "endPrincipalBalance": 6153171.031726,
        "beginPrincipalBalance": 6204433.240655,
        "prepayPrincipalPayment": 30195.413881,
        "scheduledPrincipalPayment": 21066.795048
    }
    {
        "date": "2032-10-25",
        "totalCashFlow": 51277.783217,
        "interestPayment": 2563.821263,
        "principalBalance": 6104457.069772,
        "principalPayment": 48713.961954,
        "endPrincipalBalance": 6104457.069772,
        "beginPrincipalBalance": 6153171.031726,
        "prepayPrincipalPayment": 27728.205586,
        "scheduledPrincipalPayment": 20985.756368
    }
    {
        "date": "2032-11-25",
        "totalCashFlow": 48595.298593,
        "interestPayment": 2543.523779,
        "principalBalance": 6058405.294958,
        "principalPayment": 46051.774814,
        "endPrincipalBalance": 6058405.294958,
        "beginPrincipalBalance": 6104457.069772,
        "prepayPrincipalPayment": 25139.149462,
        "scheduledPrincipalPayment": 20912.625352
    }
    {
        "date": "2032-12-25",
        "totalCashFlow": 48041.352152,
        "interestPayment": 2524.33554,
        "principalBalance": 6012888.278345,
        "principalPayment": 45517.016612,
        "endPrincipalBalance": 6012888.278345,
        "beginPrincipalBalance": 6058405.294958,
        "prepayPrincipalPayment": 24669.114944,
        "scheduledPrincipalPayment": 20847.901668
    }
    {
        "date": "2033-01-25",
        "totalCashFlow": 48056.969105,
        "interestPayment": 2505.370116,
        "principalBalance": 5967336.679357,
        "principalPayment": 45551.598989,
        "endPrincipalBalance": 5967336.679357,
        "beginPrincipalBalance": 6012888.278345,
        "prepayPrincipalPayment": 24767.252825,
        "scheduledPrincipalPayment": 20784.346163
    }
    {
        "date": "2033-02-25",
        "totalCashFlow": 42614.232352,
        "interestPayment": 2486.390283,
        "principalBalance": 5927208.837288,
        "principalPayment": 40127.842069,
        "endPrincipalBalance": 5927208.837288,
        "beginPrincipalBalance": 5967336.679357,
        "prepayPrincipalPayment": 19407.843281,
        "scheduledPrincipalPayment": 20719.998787
    }
    {
        "date": "2033-03-25",
        "totalCashFlow": 42764.1775,
        "interestPayment": 2469.670349,
        "principalBalance": 5886914.330137,
        "principalPayment": 40294.507151,
        "endPrincipalBalance": 5886914.330137,
        "beginPrincipalBalance": 5927208.837288,
        "prepayPrincipalPayment": 19620.618882,
        "scheduledPrincipalPayment": 20673.88827
    }
    {
        "date": "2033-04-25",
        "totalCashFlow": 48683.518573,
        "interestPayment": 2452.880971,
        "principalBalance": 5840683.692535,
        "principalPayment": 46230.637602,
        "endPrincipalBalance": 5840683.692535,
        "beginPrincipalBalance": 5886914.330137,
        "prepayPrincipalPayment": 25603.96111,
        "scheduledPrincipalPayment": 20626.676492
    }
    {
        "date": "2033-05-25",
        "totalCashFlow": 48616.422493,
        "interestPayment": 2433.618205,
        "principalBalance": 5794500.888247,
        "principalPayment": 46182.804287,
        "endPrincipalBalance": 5794500.888247,
        "beginPrincipalBalance": 5840683.692535,
        "prepayPrincipalPayment": 25624.762511,
        "scheduledPrincipalPayment": 20558.041777
    }
    {
        "date": "2033-06-25",
        "totalCashFlow": 51426.402836,
        "interestPayment": 2414.37537,
        "principalBalance": 5745488.860781,
        "principalPayment": 49012.027466,
        "endPrincipalBalance": 5745488.860781,
        "beginPrincipalBalance": 5794500.888247,
        "prepayPrincipalPayment": 28523.177987,
        "scheduledPrincipalPayment": 20488.849479
    }
    {
        "date": "2033-07-25",
        "totalCashFlow": 53544.251451,
        "interestPayment": 2393.953692,
        "principalBalance": 5694338.563022,
        "principalPayment": 51150.297759,
        "endPrincipalBalance": 5694338.563022,
        "beginPrincipalBalance": 5745488.860781,
        "prepayPrincipalPayment": 30741.424508,
        "scheduledPrincipalPayment": 20408.873251
    }
    {
        "date": "2033-08-25",
        "totalCashFlow": 50151.212446,
        "interestPayment": 2372.641068,
        "principalBalance": 5646559.991644,
        "principalPayment": 47778.571379,
        "endPrincipalBalance": 5646559.991644,
        "beginPrincipalBalance": 5694338.563022,
        "prepayPrincipalPayment": 27458.140649,
        "scheduledPrincipalPayment": 20320.430729
    }
    {
        "date": "2033-09-25",
        "totalCashFlow": 52431.698349,
        "interestPayment": 2352.73333,
        "principalBalance": 5596481.026625,
        "principalPayment": 50078.965019,
        "endPrincipalBalance": 5596481.026625,
        "beginPrincipalBalance": 5646559.991644,
        "prepayPrincipalPayment": 29835.805784,
        "scheduledPrincipalPayment": 20243.159235
    }
    {
        "date": "2033-10-25",
        "totalCashFlow": 48708.549508,
        "interestPayment": 2331.867094,
        "principalBalance": 5550104.344211,
        "principalPayment": 46376.682414,
        "endPrincipalBalance": 5550104.344211,
        "beginPrincipalBalance": 5596481.026625,
        "prepayPrincipalPayment": 26219.895861,
        "scheduledPrincipalPayment": 20156.786553
    }
    {
        "date": "2033-11-25",
        "totalCashFlow": 46076.016207,
        "interestPayment": 2312.543477,
        "principalBalance": 5506340.871481,
        "principalPayment": 43763.47273,
        "endPrincipalBalance": 5506340.871481,
        "beginPrincipalBalance": 5550104.344211,
        "prepayPrincipalPayment": 23680.565531,
        "scheduledPrincipalPayment": 20082.907199
    }
    {
        "date": "2033-12-25",
        "totalCashFlow": 45511.715382,
        "interestPayment": 2294.308696,
        "principalBalance": 5463123.464795,
        "principalPayment": 43217.406686,
        "endPrincipalBalance": 5463123.464795,
        "beginPrincipalBalance": 5506340.871481,
        "prepayPrincipalPayment": 23199.668064,
        "scheduledPrincipalPayment": 20017.738622
    }
    {
        "date": "2034-01-25",
        "totalCashFlow": 45488.73479,
        "interestPayment": 2276.301444,
        "principalBalance": 5419911.031449,
        "principalPayment": 43212.433347,
        "endPrincipalBalance": 5419911.031449,
        "beginPrincipalBalance": 5463123.464795,
        "prepayPrincipalPayment": 23258.578835,
        "scheduledPrincipalPayment": 19953.854512
    }
    {
        "date": "2034-02-25",
        "totalCashFlow": 40221.694264,
        "interestPayment": 2258.296263,
        "principalBalance": 5381947.633447,
        "principalPayment": 37963.398001,
        "endPrincipalBalance": 5381947.633447,
        "beginPrincipalBalance": 5419911.031449,
        "prepayPrincipalPayment": 18074.109549,
        "scheduledPrincipalPayment": 19889.288453
    }
    {
        "date": "2034-03-25",
        "totalCashFlow": 40463.277906,
        "interestPayment": 2242.478181,
        "principalBalance": 5343726.833722,
        "principalPayment": 38220.799725,
        "endPrincipalBalance": 5343726.833722,
        "beginPrincipalBalance": 5381947.633447,
        "prepayPrincipalPayment": 18377.432929,
        "scheduledPrincipalPayment": 19843.366797
    }
    {
        "date": "2034-04-25",
        "totalCashFlow": 46275.377459,
        "interestPayment": 2226.552847,
        "principalBalance": 5299678.009111,
        "principalPayment": 44048.824611,
        "endPrincipalBalance": 5299678.009111,
        "beginPrincipalBalance": 5343726.833722,
        "prepayPrincipalPayment": 24252.867258,
        "scheduledPrincipalPayment": 19795.957353
    }
    {
        "date": "2034-05-25",
        "totalCashFlow": 45801.601667,
        "interestPayment": 2208.19917,
        "principalBalance": 5256084.606614,
        "principalPayment": 43593.402497,
        "endPrincipalBalance": 5256084.606614,
        "beginPrincipalBalance": 5299678.009111,
        "prepayPrincipalPayment": 23867.09766,
        "scheduledPrincipalPayment": 19726.304836
    }
    {
        "date": "2034-06-25",
        "totalCashFlow": 50385.740195,
        "interestPayment": 2190.035253,
        "principalBalance": 5207888.901671,
        "principalPayment": 48195.704943,
        "endPrincipalBalance": 5207888.901671,
        "beginPrincipalBalance": 5256084.606614,
        "prepayPrincipalPayment": 28538.114066,
        "scheduledPrincipalPayment": 19657.590877
    }
    {
        "date": "2034-07-25",
        "totalCashFlow": 51379.554878,
        "interestPayment": 2169.953709,
        "principalBalance": 5158679.300503,
        "principalPayment": 49209.601169,
        "endPrincipalBalance": 5158679.300503,
        "beginPrincipalBalance": 5207888.901671,
        "prepayPrincipalPayment": 29638.77755,
        "scheduledPrincipalPayment": 19570.823619
    }
    {
        "date": "2034-08-25",
        "totalCashFlow": 48200.548301,
        "interestPayment": 2149.449709,
        "principalBalance": 5112628.20191,
        "principalPayment": 46051.098593,
        "endPrincipalBalance": 5112628.20191,
        "beginPrincipalBalance": 5158679.300503,
        "prepayPrincipalPayment": 26571.805414,
        "scheduledPrincipalPayment": 19479.293179
    }
    {
        "date": "2034-09-25",
        "totalCashFlow": 50557.098665,
        "interestPayment": 2130.261751,
        "principalBalance": 5064201.364996,
        "principalPayment": 48426.836914,
        "endPrincipalBalance": 5064201.364996,
        "beginPrincipalBalance": 5112628.20191,
        "prepayPrincipalPayment": 29028.073779,
        "scheduledPrincipalPayment": 19398.763135
    }
    {
        "date": "2034-10-25",
        "totalCashFlow": 45906.208905,
        "interestPayment": 2110.083902,
        "principalBalance": 5020405.239993,
        "principalPayment": 43796.125003,
        "endPrincipalBalance": 5020405.239993,
        "beginPrincipalBalance": 5064201.364996,
        "prepayPrincipalPayment": 24487.830242,
        "scheduledPrincipalPayment": 19308.294761
    }
    {
        "date": "2034-11-25",
        "totalCashFlow": 45533.149661,
        "interestPayment": 2091.835517,
        "principalBalance": 4976963.925848,
        "principalPayment": 43441.314144,
        "endPrincipalBalance": 4976963.925848,
        "beginPrincipalBalance": 5020405.239993,
        "prepayPrincipalPayment": 24206.726357,
        "scheduledPrincipalPayment": 19234.587787
    }
    {
        "date": "2034-12-25",
        "totalCashFlow": 44056.327602,
        "interestPayment": 2073.734969,
        "principalBalance": 4934981.333216,
        "principalPayment": 41982.592633,
        "endPrincipalBalance": 4934981.333216,
        "beginPrincipalBalance": 4976963.925848,
        "prepayPrincipalPayment": 22821.165279,
        "scheduledPrincipalPayment": 19161.427354
    }
    {
        "date": "2035-01-25",
        "totalCashFlow": 43146.848584,
        "interestPayment": 2056.242222,
        "principalBalance": 4893890.726854,
        "principalPayment": 41090.606362,
        "endPrincipalBalance": 4893890.726854,
        "beginPrincipalBalance": 4934981.333216,
        "prepayPrincipalPayment": 21997.512661,
        "scheduledPrincipalPayment": 19093.0937
    }
    {
        "date": "2035-02-25",
        "totalCashFlow": 39760.399208,
        "interestPayment": 2039.121136,
        "principalBalance": 4856169.448782,
        "principalPayment": 37721.278071,
        "endPrincipalBalance": 4856169.448782,
        "beginPrincipalBalance": 4893890.726854,
        "prepayPrincipalPayment": 18693.822101,
        "scheduledPrincipalPayment": 19027.455971
    }
    {
        "date": "2035-03-25",
        "totalCashFlow": 39199.657889,
        "interestPayment": 2023.403937,
        "principalBalance": 4818993.194831,
        "principalPayment": 37176.253952,
        "endPrincipalBalance": 4818993.194831,
        "beginPrincipalBalance": 4856169.448782,
        "prepayPrincipalPayment": 18202.019023,
        "scheduledPrincipalPayment": 18974.234929
    }
    {
        "date": "2035-04-25",
        "totalCashFlow": 43511.716519,
        "interestPayment": 2007.913831,
        "principalBalance": 4777489.392143,
        "principalPayment": 41503.802688,
        "endPrincipalBalance": 4777489.392143,
        "beginPrincipalBalance": 4818993.194831,
        "prepayPrincipalPayment": 22581.275992,
        "scheduledPrincipalPayment": 18922.526696
    }
    {
        "date": "2035-05-25",
        "totalCashFlow": 45490.818419,
        "interestPayment": 1990.62058,
        "principalBalance": 4733989.194304,
        "principalPayment": 43500.197839,
        "endPrincipalBalance": 4733989.194304,
        "beginPrincipalBalance": 4777489.392143,
        "prepayPrincipalPayment": 24647.071344,
        "scheduledPrincipalPayment": 18853.126495
    }
    {
        "date": "2035-06-25",
        "totalCashFlow": 48903.394077,
        "interestPayment": 1972.495498,
        "principalBalance": 4687058.295724,
        "principalPayment": 46930.898579,
        "endPrincipalBalance": 4687058.295724,
        "beginPrincipalBalance": 4733989.194304,
        "prepayPrincipalPayment": 28155.883767,
        "scheduledPrincipalPayment": 18775.014812
    }
    {
        "date": "2035-07-25",
        "totalCashFlow": 48571.623578,
        "interestPayment": 1952.940957,
        "principalBalance": 4640439.613102,
        "principalPayment": 46618.682622,
        "endPrincipalBalance": 4640439.613102,
        "beginPrincipalBalance": 4687058.295724,
        "prepayPrincipalPayment": 27936.338233,
        "scheduledPrincipalPayment": 18682.344389
    }
    {
        "date": "2035-08-25",
        "totalCashFlow": 47850.688367,
        "interestPayment": 1933.516505,
        "principalBalance": 4594522.441241,
        "principalPayment": 45917.171862,
        "endPrincipalBalance": 4594522.441241,
        "beginPrincipalBalance": 4640439.613102,
        "prepayPrincipalPayment": 27327.281411,
        "scheduledPrincipalPayment": 18589.890451
    }
    {
        "date": "2035-09-25",
        "totalCashFlow": 48896.845914,
        "interestPayment": 1914.384351,
        "principalBalance": 4547539.979677,
        "principalPayment": 46982.461563,
        "endPrincipalBalance": 4547539.979677,
        "beginPrincipalBalance": 4594522.441241,
        "prepayPrincipalPayment": 28483.236258,
        "scheduledPrincipalPayment": 18499.225305
    }
    {
        "date": "2035-10-25",
        "totalCashFlow": 43203.988519,
        "interestPayment": 1894.808325,
        "principalBalance": 4506230.799483,
        "principalPayment": 41309.180194,
        "endPrincipalBalance": 4506230.799483,
        "beginPrincipalBalance": 4547539.979677,
        "prepayPrincipalPayment": 22905.952345,
        "scheduledPrincipalPayment": 18403.227849
    }
    {
        "date": "2035-11-25",
        "totalCashFlow": 44868.540734,
        "interestPayment": 1877.596166,
        "principalBalance": 4463239.854916,
        "principalPayment": 42990.944567,
        "endPrincipalBalance": 4463239.854916,
        "beginPrincipalBalance": 4506230.799483,
        "prepayPrincipalPayment": 24661.717329,
        "scheduledPrincipalPayment": 18329.227238
    }
    {
        "date": "2035-12-25",
        "totalCashFlow": 42387.678598,
        "interestPayment": 1859.683273,
        "principalBalance": 4422711.859591,
        "principalPayment": 40527.995325,
        "endPrincipalBalance": 4422711.859591,
        "beginPrincipalBalance": 4463239.854916,
        "prepayPrincipalPayment": 22280.502016,
        "scheduledPrincipalPayment": 18247.493309
    }
    {
        "date": "2036-01-25",
        "totalCashFlow": 41466.062345,
        "interestPayment": 1842.796608,
        "principalBalance": 4383088.593854,
        "principalPayment": 39623.265737,
        "endPrincipalBalance": 4383088.593854,
        "beginPrincipalBalance": 4422711.859591,
        "prepayPrincipalPayment": 21448.325367,
        "scheduledPrincipalPayment": 18174.940369
    }
    {
        "date": "2036-02-25",
        "totalCashFlow": 38140.993989,
        "interestPayment": 1826.286914,
        "principalBalance": 4346773.886779,
        "principalPayment": 36314.707075,
        "endPrincipalBalance": 4346773.886779,
        "beginPrincipalBalance": 4383088.593854,
        "prepayPrincipalPayment": 18209.431327,
        "scheduledPrincipalPayment": 18105.275748
    }
    {
        "date": "2036-03-25",
        "totalCashFlow": 38371.579163,
        "interestPayment": 1811.155786,
        "principalBalance": 4310213.463403,
        "principalPayment": 36560.423376,
        "endPrincipalBalance": 4310213.463403,
        "beginPrincipalBalance": 4346773.886779,
        "prepayPrincipalPayment": 18511.896548,
        "scheduledPrincipalPayment": 18048.526828
    }
    {
        "date": "2036-04-25",
        "totalCashFlow": 41278.4664,
        "interestPayment": 1795.922276,
        "principalBalance": 4270730.919279,
        "principalPayment": 39482.544123,
        "endPrincipalBalance": 4270730.919279,
        "beginPrincipalBalance": 4310213.463403,
        "prepayPrincipalPayment": 21492.4821,
        "scheduledPrincipalPayment": 17990.062024
    }
    {
        "date": "2036-05-25",
        "totalCashFlow": 44156.38456,
        "interestPayment": 1779.471216,
        "principalBalance": 4228354.005935,
        "principalPayment": 42376.913344,
        "endPrincipalBalance": 4228354.005935,
        "beginPrincipalBalance": 4270730.919279,
        "prepayPrincipalPayment": 24458.287279,
        "scheduledPrincipalPayment": 17918.626065
    }
    {
        "date": "2036-06-25",
        "totalCashFlow": 45782.200722,
        "interestPayment": 1761.814169,
        "principalBalance": 4184333.619383,
        "principalPayment": 44020.386552,
        "endPrincipalBalance": 4184333.619383,
        "beginPrincipalBalance": 4228354.005935,
        "prepayPrincipalPayment": 26186.254148,
        "scheduledPrincipalPayment": 17834.132404
    }
    {
        "date": "2036-07-25",
        "totalCashFlow": 46584.226476,
        "interestPayment": 1743.472341,
        "principalBalance": 4139492.865248,
        "principalPayment": 44840.754134,
        "endPrincipalBalance": 4139492.865248,
        "beginPrincipalBalance": 4184333.619383,
        "prepayPrincipalPayment": 27099.074882,
        "scheduledPrincipalPayment": 17741.679253
    }
    {
        "date": "2036-08-25",
        "totalCashFlow": 47008.05892,
        "interestPayment": 1724.788694,
        "principalBalance": 4094209.595022,
        "principalPayment": 45283.270227,
        "endPrincipalBalance": 4094209.595022,
        "beginPrincipalBalance": 4139492.865248,
        "prepayPrincipalPayment": 27638.620268,
        "scheduledPrincipalPayment": 17644.649958
    }
    {
        "date": "2036-09-25",
        "totalCashFlow": 44594.582354,
        "interestPayment": 1705.920665,
        "principalBalance": 4051320.933332,
        "principalPayment": 42888.66169,
        "endPrincipalBalance": 4051320.933332,
        "beginPrincipalBalance": 4094209.595022,
        "prepayPrincipalPayment": 25344.069479,
        "scheduledPrincipalPayment": 17544.592211
    }
    {
        "date": "2036-10-25",
        "totalCashFlow": 43370.619838,
        "interestPayment": 1688.050389,
        "principalBalance": 4009638.363883,
        "principalPayment": 41682.569449,
        "endPrincipalBalance": 4009638.363883,
        "beginPrincipalBalance": 4051320.933332,
        "prepayPrincipalPayment": 24228.887572,
        "scheduledPrincipalPayment": 17453.681878
    }
    {
        "date": "2036-11-25",
        "totalCashFlow": 42821.111555,
        "interestPayment": 1670.682652,
        "principalBalance": 3968487.934979,
        "principalPayment": 41150.428904,
        "endPrincipalBalance": 3968487.934979,
        "beginPrincipalBalance": 4009638.363883,
        "prepayPrincipalPayment": 23783.508529,
        "scheduledPrincipalPayment": 17366.920374
    }
    {
        "date": "2036-12-25",
        "totalCashFlow": 38502.608513,
        "interestPayment": 1653.53664,
        "principalBalance": 3931638.863106,
        "principalPayment": 36849.071874,
        "endPrincipalBalance": 3931638.863106,
        "beginPrincipalBalance": 3968487.934979,
        "prepayPrincipalPayment": 19567.630206,
        "scheduledPrincipalPayment": 17281.441667
    }
    {
        "date": "2037-01-25",
        "totalCashFlow": 41310.169207,
        "interestPayment": 1638.18286,
        "principalBalance": 3891966.876758,
        "principalPayment": 39671.986348,
        "endPrincipalBalance": 3891966.876758,
        "beginPrincipalBalance": 3931638.863106,
        "prepayPrincipalPayment": 22458.215519,
        "scheduledPrincipalPayment": 17213.770829
    }
    {
        "date": "2037-02-25",
        "totalCashFlow": 35529.217557,
        "interestPayment": 1621.652865,
        "principalBalance": 3858059.312066,
        "principalPayment": 33907.564692,
        "endPrincipalBalance": 3858059.312066,
        "beginPrincipalBalance": 3891966.876758,
        "prepayPrincipalPayment": 16774.726226,
        "scheduledPrincipalPayment": 17132.838466
    }
    {
        "date": "2037-03-25",
        "totalCashFlow": 35664.057136,
        "interestPayment": 1607.524713,
        "principalBalance": 3824002.779644,
        "principalPayment": 34056.532422,
        "endPrincipalBalance": 3824002.779644,
        "beginPrincipalBalance": 3858059.312066,
        "prepayPrincipalPayment": 16980.095087,
        "scheduledPrincipalPayment": 17076.437335
    }
    {
        "date": "2037-04-25",
        "totalCashFlow": 40020.742873,
        "interestPayment": 1593.334492,
        "principalBalance": 3785575.371263,
        "principalPayment": 38427.408381,
        "endPrincipalBalance": 3785575.371263,
        "beginPrincipalBalance": 3824002.779644,
        "prepayPrincipalPayment": 21408.752699,
        "scheduledPrincipalPayment": 17018.655682
    }
    {
        "date": "2037-05-25",
        "totalCashFlow": 42333.660262,
        "interestPayment": 1577.323071,
        "principalBalance": 3744819.034072,
        "principalPayment": 40756.33719,
        "endPrincipalBalance": 3744819.034072,
        "beginPrincipalBalance": 3785575.371263,
        "prepayPrincipalPayment": 23815.758638,
        "scheduledPrincipalPayment": 16940.578552
    }
    {
        "date": "2037-06-25",
        "totalCashFlow": 42252.44392,
        "interestPayment": 1560.341264,
        "principalBalance": 3704126.931417,
        "principalPayment": 40692.102656,
        "endPrincipalBalance": 3704126.931417,
        "beginPrincipalBalance": 3744819.034072,
        "prepayPrincipalPayment": 23841.044591,
        "scheduledPrincipalPayment": 16851.058065
    }
    {
        "date": "2037-07-25",
        "totalCashFlow": 45193.169141,
        "interestPayment": 1543.386221,
        "principalBalance": 3660477.148497,
        "principalPayment": 43649.78292,
        "endPrincipalBalance": 3660477.148497,
        "beginPrincipalBalance": 3704126.931417,
        "prepayPrincipalPayment": 26889.049557,
        "scheduledPrincipalPayment": 16760.733362
    }
    {
        "date": "2037-08-25",
        "totalCashFlow": 44355.462499,
        "interestPayment": 1525.198812,
        "principalBalance": 3617646.884809,
        "principalPayment": 42830.263687,
        "endPrincipalBalance": 3617646.884809,
        "beginPrincipalBalance": 3660477.148497,
        "prepayPrincipalPayment": 26174.421335,
        "scheduledPrincipalPayment": 16655.842353
    }
    {
        "date": "2037-09-25",
        "totalCashFlow": 42017.744527,
        "interestPayment": 1507.352869,
        "principalBalance": 3577136.493151,
        "principalPayment": 40510.391658,
        "endPrincipalBalance": 3577136.493151,
        "beginPrincipalBalance": 3617646.884809,
        "prepayPrincipalPayment": 23956.966912,
        "scheduledPrincipalPayment": 16553.424747
    }
    {
        "date": "2037-10-25",
        "totalCashFlow": 40813.005819,
        "interestPayment": 1490.473539,
        "principalBalance": 3537813.960871,
        "principalPayment": 39322.53228,
        "endPrincipalBalance": 3537813.960871,
        "beginPrincipalBalance": 3577136.493151,
        "prepayPrincipalPayment": 22862.103938,
        "scheduledPrincipalPayment": 16460.428342
    }
    {
        "date": "2037-11-25",
        "totalCashFlow": 39348.236222,
        "interestPayment": 1474.08915,
        "principalBalance": 3499939.8138,
        "principalPayment": 37874.147071,
        "endPrincipalBalance": 3499939.8138,
        "beginPrincipalBalance": 3537813.960871,
        "prepayPrincipalPayment": 21502.370343,
        "scheduledPrincipalPayment": 16371.776729
    }
    {
        "date": "2037-12-25",
        "totalCashFlow": 37050.01069,
        "interestPayment": 1458.308256,
        "principalBalance": 3464348.111365,
        "principalPayment": 35591.702434,
        "endPrincipalBalance": 3464348.111365,
        "beginPrincipalBalance": 3499939.8138,
        "prepayPrincipalPayment": 19302.944039,
        "scheduledPrincipalPayment": 16288.758395
    }
    {
        "date": "2038-01-25",
        "totalCashFlow": 38729.6068,
        "interestPayment": 1443.47838,
        "principalBalance": 3427061.982945,
        "principalPayment": 37286.12842,
        "endPrincipalBalance": 3427061.982945,
        "beginPrincipalBalance": 3464348.111365,
        "prepayPrincipalPayment": 21070.752753,
        "scheduledPrincipalPayment": 16215.375667
    }
    {
        "date": "2038-02-25",
        "totalCashFlow": 32632.516442,
        "interestPayment": 1427.942493,
        "principalBalance": 3395857.408996,
        "principalPayment": 31204.573949,
        "endPrincipalBalance": 3395857.408996,
        "beginPrincipalBalance": 3427061.982945,
        "prepayPrincipalPayment": 15071.498945,
        "scheduledPrincipalPayment": 16133.075004
    }
    {
        "date": "2038-03-25",
        "totalCashFlow": 33385.979992,
        "interestPayment": 1414.940587,
        "principalBalance": 3363886.369591,
        "principalPayment": 31971.039405,
        "endPrincipalBalance": 3363886.369591,
        "beginPrincipalBalance": 3395857.408996,
        "prepayPrincipalPayment": 15892.518826,
        "scheduledPrincipalPayment": 16078.520579
    }
    {
        "date": "2038-04-25",
        "totalCashFlow": 38192.34559,
        "interestPayment": 1401.619321,
        "principalBalance": 3327095.643322,
        "principalPayment": 36790.726269,
        "endPrincipalBalance": 3327095.643322,
        "beginPrincipalBalance": 3363886.369591,
        "prepayPrincipalPayment": 20771.140989,
        "scheduledPrincipalPayment": 16019.58528
    }
    {
        "date": "2038-05-25",
        "totalCashFlow": 39033.610028,
        "interestPayment": 1386.289851,
        "principalBalance": 3289448.323145,
        "principalPayment": 37647.320176,
        "endPrincipalBalance": 3289448.323145,
        "beginPrincipalBalance": 3327095.643322,
        "prepayPrincipalPayment": 21710.541535,
        "scheduledPrincipalPayment": 15936.778642
    }
    {
        "date": "2038-06-25",
        "totalCashFlow": 39369.923164,
        "interestPayment": 1370.603468,
        "principalBalance": 3251449.003449,
        "principalPayment": 37999.319696,
        "endPrincipalBalance": 3251449.003449,
        "beginPrincipalBalance": 3289448.323145,
        "prepayPrincipalPayment": 22150.543049,
        "scheduledPrincipalPayment": 15848.776647
    }
    {
        "date": "2038-07-25",
        "totalCashFlow": 42041.040751,
        "interestPayment": 1354.770418,
        "principalBalance": 3210762.733116,
        "principalPayment": 40686.270333,
        "endPrincipalBalance": 3210762.733116,
        "beginPrincipalBalance": 3251449.003449,
        "prepayPrincipalPayment": 24928.335699,
        "scheduledPrincipalPayment": 15757.934634
    }
    {
        "date": "2038-08-25",
        "totalCashFlow": 40209.930452,
        "interestPayment": 1337.817805,
        "principalBalance": 3171890.620469,
        "principalPayment": 38872.112647,
        "endPrincipalBalance": 3171890.620469,
        "beginPrincipalBalance": 3210762.733116,
        "prepayPrincipalPayment": 23219.291871,
        "scheduledPrincipalPayment": 15652.820776
    }
    {
        "date": "2038-09-25",
        "totalCashFlow": 39980.30513,
        "interestPayment": 1321.621092,
        "principalBalance": 3133231.936431,
        "principalPayment": 38658.684038,
        "endPrincipalBalance": 3133231.936431,
        "beginPrincipalBalance": 3171890.620469,
        "prepayPrincipalPayment": 23103.427877,
        "scheduledPrincipalPayment": 15555.256161
    }
    {
        "date": "2038-10-25",
        "totalCashFlow": 37879.767856,
        "interestPayment": 1305.513307,
        "principalBalance": 3096657.681882,
        "principalPayment": 36574.254549,
        "endPrincipalBalance": 3096657.681882,
        "beginPrincipalBalance": 3133231.936431,
        "prepayPrincipalPayment": 21116.773408,
        "scheduledPrincipalPayment": 15457.481141
    }
    {
        "date": "2038-11-25",
        "totalCashFlow": 35688.708609,
        "interestPayment": 1290.274034,
        "principalBalance": 3062259.247308,
        "principalPayment": 34398.434575,
        "endPrincipalBalance": 3062259.247308,
        "beginPrincipalBalance": 3096657.681882,
        "prepayPrincipalPayment": 19029.654899,
        "scheduledPrincipalPayment": 15368.779676
    }
    {
        "date": "2038-12-25",
        "totalCashFlow": 35201.301402,
        "interestPayment": 1275.941353,
        "principalBalance": 3028333.887259,
        "principalPayment": 33925.360049,
        "endPrincipalBalance": 3028333.887259,
        "beginPrincipalBalance": 3062259.247308,
        "prepayPrincipalPayment": 18635.58576,
        "scheduledPrincipalPayment": 15289.77429
    }
    {
        "date": "2039-01-25",
        "totalCashFlow": 35112.713994,
        "interestPayment": 1261.805786,
        "principalBalance": 2994482.979051,
        "principalPayment": 33850.908207,
        "endPrincipalBalance": 2994482.979051,
        "beginPrincipalBalance": 3028333.887259,
        "prepayPrincipalPayment": 18638.818347,
        "scheduledPrincipalPayment": 15212.08986
    }
    {
        "date": "2039-02-25",
        "totalCashFlow": 30888.95432,
        "interestPayment": 1247.701241,
        "principalBalance": 2964841.725972,
        "principalPayment": 29641.253079,
        "endPrincipalBalance": 2964841.725972,
        "beginPrincipalBalance": 2994482.979051,
        "prepayPrincipalPayment": 14507.515518,
        "scheduledPrincipalPayment": 15133.737561
    }
    {
        "date": "2039-03-25",
        "totalCashFlow": 30971.072463,
        "interestPayment": 1235.350719,
        "principalBalance": 2935106.004228,
        "principalPayment": 29735.721744,
        "endPrincipalBalance": 2935106.004228,
        "beginPrincipalBalance": 2964841.725972,
        "prepayPrincipalPayment": 14659.988209,
        "scheduledPrincipalPayment": 15075.733536
    }
    {
        "date": "2039-04-25",
        "totalCashFlow": 35368.658961,
        "interestPayment": 1222.960835,
        "principalBalance": 2900960.306103,
        "principalPayment": 34145.698126,
        "endPrincipalBalance": 2900960.306103,
        "beginPrincipalBalance": 2935106.004228,
        "prepayPrincipalPayment": 19129.263361,
        "scheduledPrincipalPayment": 15016.434765
    }
    {
        "date": "2039-05-25",
        "totalCashFlow": 35313.891682,
        "interestPayment": 1208.733461,
        "principalBalance": 2866855.147881,
        "principalPayment": 34105.158221,
        "endPrincipalBalance": 2866855.147881,
        "beginPrincipalBalance": 2900960.306103,
        "prepayPrincipalPayment": 19171.55522,
        "scheduledPrincipalPayment": 14933.603002
    }
    {
        "date": "2039-06-25",
        "totalCashFlow": 37367.218056,
        "interestPayment": 1194.522978,
        "principalBalance": 2830682.452804,
        "principalPayment": 36172.695077,
        "endPrincipalBalance": 2830682.452804,
        "beginPrincipalBalance": 2866855.147881,
        "prepayPrincipalPayment": 21322.841843,
        "scheduledPrincipalPayment": 14849.853235
    }
    {
        "date": "2039-07-25",
        "totalCashFlow": 38876.537232,
        "interestPayment": 1179.451022,
        "principalBalance": 2792985.366593,
        "principalPayment": 37697.08621,
        "endPrincipalBalance": 2792985.366593,
        "beginPrincipalBalance": 2830682.452804,
        "prepayPrincipalPayment": 22942.904041,
        "scheduledPrincipalPayment": 14754.182169
    }
    {
        "date": "2039-08-25",
        "totalCashFlow": 36266.22216,
        "interestPayment": 1163.743903,
        "principalBalance": 2757882.888336,
        "principalPayment": 35102.478257,
        "endPrincipalBalance": 2757882.888336,
        "beginPrincipalBalance": 2792985.366593,
        "prepayPrincipalPayment": 20453.26274,
        "scheduledPrincipalPayment": 14649.215517
    }
    {
        "date": "2039-09-25",
        "totalCashFlow": 37835.855237,
        "interestPayment": 1149.11787,
        "principalBalance": 2721196.150969,
        "principalPayment": 36686.737367,
        "endPrincipalBalance": 2721196.150969,
        "beginPrincipalBalance": 2757882.888336,
        "prepayPrincipalPayment": 22130.21764,
        "scheduledPrincipalPayment": 14556.519727
    }
    {
        "date": "2039-10-25",
        "totalCashFlow": 34999.316506,
        "interestPayment": 1133.83173,
        "principalBalance": 2687330.666193,
        "principalPayment": 33865.484777,
        "endPrincipalBalance": 2687330.666193,
        "beginPrincipalBalance": 2721196.150969,
        "prepayPrincipalPayment": 19411.350731,
        "scheduledPrincipalPayment": 14454.134046
    }
    {
        "date": "2039-11-25",
        "totalCashFlow": 32967.906702,
        "interestPayment": 1119.721111,
        "principalBalance": 2655482.480601,
        "principalPayment": 31848.185592,
        "endPrincipalBalance": 2655482.480601,
        "beginPrincipalBalance": 2687330.666193,
        "prepayPrincipalPayment": 17482.76069,
        "scheduledPrincipalPayment": 14365.424901
    }
    {
        "date": "2039-12-25",
        "totalCashFlow": 32497.382496,
        "interestPayment": 1106.451034,
        "principalBalance": 2624091.549138,
        "principalPayment": 31390.931463,
        "endPrincipalBalance": 2624091.549138,
        "beginPrincipalBalance": 2655482.480601,
        "prepayPrincipalPayment": 17104.598756,
        "scheduledPrincipalPayment": 14286.332706
    }
    {
        "date": "2040-01-25",
        "totalCashFlow": 32385.898891,
        "interestPayment": 1093.371479,
        "principalBalance": 2592799.021727,
        "principalPayment": 31292.527412,
        "endPrincipalBalance": 2592799.021727,
        "beginPrincipalBalance": 2624091.549138,
        "prepayPrincipalPayment": 17083.928923,
        "scheduledPrincipalPayment": 14208.598489
    }
    {
        "date": "2040-02-25",
        "totalCashFlow": 28534.837552,
        "interestPayment": 1080.332926,
        "principalBalance": 2565344.517101,
        "principalPayment": 27454.504626,
        "endPrincipalBalance": 2565344.517101,
        "beginPrincipalBalance": 2592799.021727,
        "prepayPrincipalPayment": 13324.209896,
        "scheduledPrincipalPayment": 14130.29473
    }
    {
        "date": "2040-03-25",
        "totalCashFlow": 29159.066126,
        "interestPayment": 1068.893549,
        "principalBalance": 2537254.344524,
        "principalPayment": 28090.172577,
        "endPrincipalBalance": 2537254.344524,
        "beginPrincipalBalance": 2565344.517101,
        "prepayPrincipalPayment": 14018.24733,
        "scheduledPrincipalPayment": 14071.925247
    }
    {
        "date": "2040-04-25",
        "totalCashFlow": 31516.8106,
        "interestPayment": 1057.18931,
        "principalBalance": 2506794.723234,
        "principalPayment": 30459.62129,
        "endPrincipalBalance": 2506794.723234,
        "beginPrincipalBalance": 2537254.344524,
        "prepayPrincipalPayment": 16450.438067,
        "scheduledPrincipalPayment": 14009.183223
    }
    {
        "date": "2040-05-25",
        "totalCashFlow": 32805.095436,
        "interestPayment": 1044.497801,
        "principalBalance": 2475034.1256,
        "principalPayment": 31760.597634,
        "endPrincipalBalance": 2475034.1256,
        "beginPrincipalBalance": 2506794.723234,
        "prepayPrincipalPayment": 17828.250306,
        "scheduledPrincipalPayment": 13932.347329
    }
    {
        "date": "2040-06-25",
        "totalCashFlow": 35056.954331,
        "interestPayment": 1031.264219,
        "principalBalance": 2441008.435487,
        "principalPayment": 34025.690112,
        "endPrincipalBalance": 2441008.435487,
        "beginPrincipalBalance": 2475034.1256,
        "prepayPrincipalPayment": 20178.573942,
        "scheduledPrincipalPayment": 13847.11617
    }
    {
        "date": "2040-07-25",
        "totalCashFlow": 34659.531714,
        "interestPayment": 1017.086848,
        "principalBalance": 2407365.990621,
        "principalPayment": 33642.444866,
        "endPrincipalBalance": 2407365.990621,
        "beginPrincipalBalance": 2441008.435487,
        "prepayPrincipalPayment": 19894.551452,
        "scheduledPrincipalPayment": 13747.893414
    }
    {
        "date": "2040-08-25",
        "totalCashFlow": 33981.391061,
        "interestPayment": 1003.069163,
        "principalBalance": 2374387.668723,
        "principalPayment": 32978.321898,
        "endPrincipalBalance": 2374387.668723,
        "beginPrincipalBalance": 2407365.990621,
        "prepayPrincipalPayment": 19328.906973,
        "scheduledPrincipalPayment": 13649.414924
    }
    {
        "date": "2040-09-25",
        "totalCashFlow": 34503.685984,
        "interestPayment": 989.328195,
        "principalBalance": 2340873.310934,
        "principalPayment": 33514.357789,
        "endPrincipalBalance": 2340873.310934,
        "beginPrincipalBalance": 2374387.668723,
        "prepayPrincipalPayment": 19961.056538,
        "scheduledPrincipalPayment": 13553.301251
    }
    {
        "date": "2040-10-25",
        "totalCashFlow": 30473.380558,
        "interestPayment": 975.36388,
        "principalBalance": 2311375.294256,
        "principalPayment": 29498.016679,
        "endPrincipalBalance": 2311375.294256,
        "beginPrincipalBalance": 2340873.310934,
        "prepayPrincipalPayment": 16045.311096,
        "scheduledPrincipalPayment": 13452.705582
    }
    {
        "date": "2040-11-25",
        "totalCashFlow": 31421.481934,
        "interestPayment": 963.073039,
        "principalBalance": 2280916.885361,
        "principalPayment": 30458.408895,
        "endPrincipalBalance": 2280916.885361,
        "beginPrincipalBalance": 2311375.294256,
        "prepayPrincipalPayment": 17084.530062,
        "scheduledPrincipalPayment": 13373.878833
    }
    {
        "date": "2040-12-25",
        "totalCashFlow": 29631.540699,
        "interestPayment": 950.382036,
        "principalBalance": 2252235.726697,
        "principalPayment": 28681.158664,
        "endPrincipalBalance": 2252235.726697,
        "beginPrincipalBalance": 2280916.885361,
        "prepayPrincipalPayment": 15392.880605,
        "scheduledPrincipalPayment": 13288.278059
    }
    {
        "date": "2041-01-25",
        "totalCashFlow": 28873.914182,
        "interestPayment": 938.431553,
        "principalBalance": 2224300.244067,
        "principalPayment": 27935.48263,
        "endPrincipalBalance": 2224300.244067,
        "beginPrincipalBalance": 2252235.726697,
        "prepayPrincipalPayment": 14723.658682,
        "scheduledPrincipalPayment": 13211.823948
    }
    {
        "date": "2041-02-25",
        "totalCashFlow": 26541.339358,
        "interestPayment": 926.791768,
        "principalBalance": 2198685.696478,
        "principalPayment": 25614.547589,
        "endPrincipalBalance": 2198685.696478,
        "beginPrincipalBalance": 2224300.244067,
        "prepayPrincipalPayment": 12475.93182,
        "scheduledPrincipalPayment": 13138.615769
    }
    {
        "date": "2041-03-25",
        "totalCashFlow": 26072.297824,
        "interestPayment": 916.11904,
        "principalBalance": 2173529.517695,
        "principalPayment": 25156.178783,
        "endPrincipalBalance": 2173529.517695,
        "beginPrincipalBalance": 2198685.696478,
        "prepayPrincipalPayment": 12078.085562,
        "scheduledPrincipalPayment": 13078.093222
    }
    {
        "date": "2041-04-25",
        "totalCashFlow": 28348.145042,
        "interestPayment": 905.637299,
        "principalBalance": 2146087.009951,
        "principalPayment": 27442.507743,
        "endPrincipalBalance": 2146087.009951,
        "beginPrincipalBalance": 2173529.517695,
        "prepayPrincipalPayment": 14423.138835,
        "scheduledPrincipalPayment": 13019.368908
    }
    {
        "date": "2041-05-25",
        "totalCashFlow": 30072.317963,
        "interestPayment": 894.202921,
        "principalBalance": 2116908.894909,
        "principalPayment": 29178.115042,
        "endPrincipalBalance": 2116908.894909,
        "beginPrincipalBalance": 2146087.009951,
        "prepayPrincipalPayment": 16232.189562,
        "scheduledPrincipalPayment": 12945.925481
    }
    {
        "date": "2041-06-25",
        "totalCashFlow": 31683.604979,
        "interestPayment": 882.045373,
        "principalBalance": 2086107.335303,
        "principalPayment": 30801.559606,
        "endPrincipalBalance": 2086107.335303,
        "beginPrincipalBalance": 2116908.894909,
        "prepayPrincipalPayment": 17940.763742,
        "scheduledPrincipalPayment": 12860.795864
    }
    {
        "date": "2041-07-25",
        "totalCashFlow": 30532.60437,
        "interestPayment": 869.21139,
        "principalBalance": 2056443.942323,
        "principalPayment": 29663.39298,
        "endPrincipalBalance": 2056443.942323,
        "beginPrincipalBalance": 2086107.335303,
        "prepayPrincipalPayment": 16898.975913,
        "scheduledPrincipalPayment": 12764.417067
    }
    {
        "date": "2041-08-25",
        "totalCashFlow": 31390.558456,
        "interestPayment": 856.851643,
        "principalBalance": 2025910.23551,
        "principalPayment": 30533.706813,
        "endPrincipalBalance": 2025910.23551,
        "beginPrincipalBalance": 2056443.942323,
        "prepayPrincipalPayment": 17860.139429,
        "scheduledPrincipalPayment": 12673.567384
    }
    {
        "date": "2041-09-25",
        "totalCashFlow": 30395.411418,
        "interestPayment": 844.129265,
        "principalBalance": 1996358.953357,
        "principalPayment": 29551.282153,
        "endPrincipalBalance": 1996358.953357,
        "beginPrincipalBalance": 2025910.23551,
        "prepayPrincipalPayment": 16975.380515,
        "scheduledPrincipalPayment": 12575.901638
    }
    {
        "date": "2041-10-25",
        "totalCashFlow": 28160.043807,
        "interestPayment": 831.816231,
        "principalBalance": 1969030.72578,
        "principalPayment": 27328.227577,
        "endPrincipalBalance": 1969030.72578,
        "beginPrincipalBalance": 1996358.953357,
        "prepayPrincipalPayment": 14845.369907,
        "scheduledPrincipalPayment": 12482.857669
    }
    {
        "date": "2041-11-25",
        "totalCashFlow": 28298.903862,
        "interestPayment": 820.429469,
        "principalBalance": 1941552.251388,
        "principalPayment": 27478.474393,
        "endPrincipalBalance": 1941552.251388,
        "beginPrincipalBalance": 1969030.72578,
        "prepayPrincipalPayment": 15076.12043,
        "scheduledPrincipalPayment": 12402.353963
    }
    {
        "date": "2041-12-25",
        "totalCashFlow": 26137.224473,
        "interestPayment": 808.980105,
        "principalBalance": 1916224.007019,
        "principalPayment": 25328.244368,
        "endPrincipalBalance": 1916224.007019,
        "beginPrincipalBalance": 1941552.251388,
        "prepayPrincipalPayment": 13008.632862,
        "scheduledPrincipalPayment": 12319.611506
    }
    {
        "date": "2042-01-25",
        "totalCashFlow": 26557.424257,
        "interestPayment": 798.42667,
        "principalBalance": 1890465.009432,
        "principalPayment": 25758.997587,
        "endPrincipalBalance": 1890465.009432,
        "beginPrincipalBalance": 1916224.007019,
        "prepayPrincipalPayment": 13509.709657,
        "scheduledPrincipalPayment": 12249.287931
    }
    {
        "date": "2042-02-25",
        "totalCashFlow": 23961.46663,
        "interestPayment": 787.693754,
        "principalBalance": 1867291.236555,
        "principalPayment": 23173.772876,
        "endPrincipalBalance": 1867291.236555,
        "beginPrincipalBalance": 1890465.009432,
        "prepayPrincipalPayment": 10998.730997,
        "scheduledPrincipalPayment": 12175.041879
    }
    {
        "date": "2042-03-25",
        "totalCashFlow": 23528.557055,
        "interestPayment": 778.038015,
        "principalBalance": 1844540.717516,
        "principalPayment": 22750.519039,
        "endPrincipalBalance": 1844540.717516,
        "beginPrincipalBalance": 1867291.236555,
        "prepayPrincipalPayment": 10634.162666,
        "scheduledPrincipalPayment": 12116.356374
    }
    {
        "date": "2042-04-25",
        "totalCashFlow": 25455.250177,
        "interestPayment": 768.558632,
        "principalBalance": 1819854.025971,
        "principalPayment": 24686.691545,
        "endPrincipalBalance": 1819854.025971,
        "beginPrincipalBalance": 1844540.717516,
        "prepayPrincipalPayment": 12627.239229,
        "scheduledPrincipalPayment": 12059.452316
    }
    {
        "date": "2042-05-25",
        "totalCashFlow": 27180.194391,
        "interestPayment": 758.272511,
        "principalBalance": 1793432.104091,
        "principalPayment": 26421.921881,
        "endPrincipalBalance": 1793432.104091,
        "beginPrincipalBalance": 1819854.025971,
        "prepayPrincipalPayment": 14433.093322,
        "scheduledPrincipalPayment": 11988.828559
    }
    {
        "date": "2042-06-25",
        "totalCashFlow": 27617.521486,
        "interestPayment": 747.263377,
        "principalBalance": 1766561.845982,
        "principalPayment": 26870.258109,
        "endPrincipalBalance": 1766561.845982,
        "beginPrincipalBalance": 1793432.104091,
        "prepayPrincipalPayment": 14964.753711,
        "scheduledPrincipalPayment": 11905.504398
    }
    {
        "date": "2042-07-25",
        "totalCashFlow": 27868.968949,
        "interestPayment": 736.067436,
        "principalBalance": 1739428.944468,
        "principalPayment": 27132.901513,
        "endPrincipalBalance": 1739428.944468,
        "beginPrincipalBalance": 1766561.845982,
        "prepayPrincipalPayment": 15315.105492,
        "scheduledPrincipalPayment": 11817.796021
    }
    {
        "date": "2042-08-25",
        "totalCashFlow": 27898.121784,
        "interestPayment": 724.76206,
        "principalBalance": 1712255.584745,
        "principalPayment": 27173.359724,
        "endPrincipalBalance": 1712255.584745,
        "beginPrincipalBalance": 1739428.944468,
        "prepayPrincipalPayment": 15446.504639,
        "scheduledPrincipalPayment": 11726.855085
    }
    {
        "date": "2042-09-25",
        "totalCashFlow": 26433.607346,
        "interestPayment": 713.439827,
        "principalBalance": 1686535.417226,
        "principalPayment": 25720.167519,
        "endPrincipalBalance": 1686535.417226,
        "beginPrincipalBalance": 1712255.584745,
        "prepayPrincipalPayment": 14086.050012,
        "scheduledPrincipalPayment": 11634.117507
    }
    {
        "date": "2042-10-25",
        "totalCashFlow": 25626.047114,
        "interestPayment": 702.723091,
        "principalBalance": 1661612.093203,
        "principalPayment": 24923.324024,
        "endPrincipalBalance": 1661612.093203,
        "beginPrincipalBalance": 1686535.417226,
        "prepayPrincipalPayment": 13373.552067,
        "scheduledPrincipalPayment": 11549.771956
    }
    {
        "date": "2042-11-25",
        "totalCashFlow": 25168.148641,
        "interestPayment": 692.338372,
        "principalBalance": 1637136.282934,
        "principalPayment": 24475.810269,
        "endPrincipalBalance": 1637136.282934,
        "beginPrincipalBalance": 1661612.093203,
        "prepayPrincipalPayment": 13006.319956,
        "scheduledPrincipalPayment": 11469.490313
    }
    {
        "date": "2042-12-25",
        "totalCashFlow": 22832.675494,
        "interestPayment": 682.140118,
        "principalBalance": 1614985.747557,
        "principalPayment": 22150.535376,
        "endPrincipalBalance": 1614985.747557,
        "beginPrincipalBalance": 1637136.282934,
        "prepayPrincipalPayment": 10759.593646,
        "scheduledPrincipalPayment": 11390.94173
    }
    {
        "date": "2043-01-25",
        "totalCashFlow": 24104.064402,
        "interestPayment": 672.910728,
        "principalBalance": 1591554.593883,
        "principalPayment": 23431.153674,
        "endPrincipalBalance": 1591554.593883,
        "beginPrincipalBalance": 1614985.747557,
        "prepayPrincipalPayment": 12103.813041,
        "scheduledPrincipalPayment": 11327.340633
    }
    {
        "date": "2043-02-25",
        "totalCashFlow": 21079.073088,
        "interestPayment": 663.147747,
        "principalBalance": 1571138.668543,
        "principalPayment": 20415.92534,
        "endPrincipalBalance": 1571138.668543,
        "beginPrincipalBalance": 1591554.593883,
        "prepayPrincipalPayment": 9162.368975,
        "scheduledPrincipalPayment": 11253.556365
    }
    {
        "date": "2043-03-25",
        "totalCashFlow": 21045.45834,
        "interestPayment": 654.641112,
        "principalBalance": 1550747.851315,
        "principalPayment": 20390.817228,
        "endPrincipalBalance": 1550747.851315,
        "beginPrincipalBalance": 1571138.668543,
        "prepayPrincipalPayment": 9190.852952,
        "scheduledPrincipalPayment": 11199.964276
    }
    {
        "date": "2043-04-25",
        "totalCashFlow": 22853.341552,
        "interestPayment": 646.144938,
        "principalBalance": 1528540.654701,
        "principalPayment": 22207.196613,
        "endPrincipalBalance": 1528540.654701,
        "beginPrincipalBalance": 1550747.851315,
        "prepayPrincipalPayment": 11061.622439,
        "scheduledPrincipalPayment": 11145.574175
    }
    {
        "date": "2043-05-25",
        "totalCashFlow": 24062.924974,
        "interestPayment": 636.891939,
        "principalBalance": 1505114.621667,
        "principalPayment": 23426.033034,
        "endPrincipalBalance": 1505114.621667,
        "beginPrincipalBalance": 1528540.654701,
        "prepayPrincipalPayment": 12349.010212,
        "scheduledPrincipalPayment": 11077.022823
    }
    {
        "date": "2043-06-25",
        "totalCashFlow": 23886.739779,
        "interestPayment": 627.131092,
        "principalBalance": 1481855.01298,
        "principalPayment": 23259.608686,
        "endPrincipalBalance": 1481855.01298,
        "beginPrincipalBalance": 1505114.621667,
        "prepayPrincipalPayment": 12261.285216,
        "scheduledPrincipalPayment": 10998.323471
    }
    {
        "date": "2043-07-25",
        "totalCashFlow": 25144.182171,
        "interestPayment": 617.439589,
        "principalBalance": 1457328.270398,
        "principalPayment": 24526.742582,
        "endPrincipalBalance": 1457328.270398,
        "beginPrincipalBalance": 1481855.01298,
        "prepayPrincipalPayment": 13607.312957,
        "scheduledPrincipalPayment": 10919.429625
    }
    {
        "date": "2043-08-25",
        "totalCashFlow": 24586.591638,
        "interestPayment": 607.220113,
        "principalBalance": 1433348.898873,
        "principalPayment": 23979.371525,
        "endPrincipalBalance": 1433348.898873,
        "beginPrincipalBalance": 1457328.270398,
        "prepayPrincipalPayment": 13149.686043,
        "scheduledPrincipalPayment": 10829.685483
    }
    {
        "date": "2043-09-25",
        "totalCashFlow": 23335.89403,
        "interestPayment": 597.228708,
        "principalBalance": 1410610.23355,
        "principalPayment": 22738.665323,
        "endPrincipalBalance": 1410610.23355,
        "beginPrincipalBalance": 1433348.898873,
        "prepayPrincipalPayment": 11996.250901,
        "scheduledPrincipalPayment": 10742.414421
    }
    {
        "date": "2043-10-25",
        "totalCashFlow": 22636.738643,
        "interestPayment": 587.754264,
        "principalBalance": 1388561.249171,
        "principalPayment": 22048.984379,
        "endPrincipalBalance": 1388561.249171,
        "beginPrincipalBalance": 1410610.23355,
        "prepayPrincipalPayment": 11386.060632,
        "scheduledPrincipalPayment": 10662.923747
    }
    {
        "date": "2043-11-25",
        "totalCashFlow": 21824.927341,
        "interestPayment": 578.567187,
        "principalBalance": 1367314.889017,
        "principalPayment": 21246.360154,
        "endPrincipalBalance": 1367314.889017,
        "beginPrincipalBalance": 1388561.249171,
        "prepayPrincipalPayment": 10659.143293,
        "scheduledPrincipalPayment": 10587.216861
    }
    {
        "date": "2043-12-25",
        "totalCashFlow": 20666.265555,
        "interestPayment": 569.714537,
        "principalBalance": 1347218.337999,
        "principalPayment": 20096.551018,
        "endPrincipalBalance": 1347218.337999,
        "beginPrincipalBalance": 1367314.889017,
        "prepayPrincipalPayment": 9580.287188,
        "scheduledPrincipalPayment": 10516.26383
    }
    {
        "date": "2044-01-25",
        "totalCashFlow": 21298.746235,
        "interestPayment": 561.340974,
        "principalBalance": 1326480.932738,
        "principalPayment": 20737.405261,
        "endPrincipalBalance": 1326480.932738,
        "beginPrincipalBalance": 1347218.337999,
        "prepayPrincipalPayment": 10284.519151,
        "scheduledPrincipalPayment": 10452.886111
    }
    {
        "date": "2044-02-25",
        "totalCashFlow": 18471.481598,
        "interestPayment": 552.700389,
        "principalBalance": 1308562.151529,
        "principalPayment": 17918.781209,
        "endPrincipalBalance": 1308562.151529,
        "beginPrincipalBalance": 1326480.932738,
        "prepayPrincipalPayment": 7535.510618,
        "scheduledPrincipalPayment": 10383.270591
    }
    {
        "date": "2044-03-25",
        "totalCashFlow": 19029.0846,
        "interestPayment": 545.23423,
        "principalBalance": 1290078.301158,
        "principalPayment": 18483.850371,
        "endPrincipalBalance": 1290078.301158,
        "beginPrincipalBalance": 1308562.151529,
        "prepayPrincipalPayment": 8149.276743,
        "scheduledPrincipalPayment": 10334.573628
    }
    {
        "date": "2044-04-25",
        "totalCashFlow": 20709.262734,
        "interestPayment": 537.532625,
        "principalBalance": 1269906.57105,
        "principalPayment": 20171.730108,
        "endPrincipalBalance": 1269906.57105,
        "beginPrincipalBalance": 1290078.301158,
        "prepayPrincipalPayment": 9891.3314,
        "scheduledPrincipalPayment": 10280.398708
    }
    {
        "date": "2044-05-25",
        "totalCashFlow": 20574.065341,
        "interestPayment": 529.127738,
        "principalBalance": 1249861.633447,
        "principalPayment": 20044.937603,
        "endPrincipalBalance": 1249861.633447,
        "beginPrincipalBalance": 1269906.57105,
        "prepayPrincipalPayment": 9833.368293,
        "scheduledPrincipalPayment": 10211.569309
    }
    {
        "date": "2044-06-25",
        "totalCashFlow": 21404.739174,
        "interestPayment": 520.775681,
        "principalBalance": 1228977.669953,
        "principalPayment": 20883.963494,
        "endPrincipalBalance": 1228977.669953,
        "beginPrincipalBalance": 1249861.633447,
        "prepayPrincipalPayment": 10741.55321,
        "scheduledPrincipalPayment": 10142.410283
    }
    {
        "date": "2044-07-25",
        "totalCashFlow": 21958.752112,
        "interestPayment": 512.074029,
        "principalBalance": 1207530.99187,
        "principalPayment": 21446.678083,
        "endPrincipalBalance": 1207530.99187,
        "beginPrincipalBalance": 1228977.669953,
        "prepayPrincipalPayment": 11381.673293,
        "scheduledPrincipalPayment": 10065.00479
    }
    {
        "date": "2044-08-25",
        "totalCashFlow": 20641.870813,
        "interestPayment": 503.137913,
        "principalBalance": 1187392.25897,
        "principalPayment": 20138.7329,
        "endPrincipalBalance": 1187392.25897,
        "beginPrincipalBalance": 1207530.99187,
        "prepayPrincipalPayment": 10157.32424,
        "scheduledPrincipalPayment": 9981.40866
    }
    {
        "date": "2044-09-25",
        "totalCashFlow": 21208.897022,
        "interestPayment": 494.746775,
        "principalBalance": 1166678.108723,
        "principalPayment": 20714.150247,
        "endPrincipalBalance": 1166678.108723,
        "beginPrincipalBalance": 1187392.25897,
        "prepayPrincipalPayment": 10807.092355,
        "scheduledPrincipalPayment": 9907.057893
    }
    {
        "date": "2044-10-25",
        "totalCashFlow": 19827.41613,
        "interestPayment": 486.115879,
        "principalBalance": 1147336.808471,
        "principalPayment": 19341.300251,
        "endPrincipalBalance": 1147336.808471,
        "beginPrincipalBalance": 1166678.108723,
        "prepayPrincipalPayment": 9514.945321,
        "scheduledPrincipalPayment": 9826.35493
    }
    {
        "date": "2044-11-25",
        "totalCashFlow": 18827.307099,
        "interestPayment": 478.057004,
        "principalBalance": 1128987.558375,
        "principalPayment": 18349.250096,
        "endPrincipalBalance": 1128987.558375,
        "beginPrincipalBalance": 1147336.808471,
        "prepayPrincipalPayment": 8593.563974,
        "scheduledPrincipalPayment": 9755.686121
    }
    {
        "date": "2044-12-25",
        "totalCashFlow": 18520.581927,
        "interestPayment": 470.411483,
        "principalBalance": 1110937.387931,
        "principalPayment": 18050.170444,
        "endPrincipalBalance": 1110937.387931,
        "beginPrincipalBalance": 1128987.558375,
        "prepayPrincipalPayment": 8358.095739,
        "scheduledPrincipalPayment": 9692.074706
    }
    {
        "date": "2045-01-25",
        "totalCashFlow": 18369.33144,
        "interestPayment": 462.890578,
        "principalBalance": 1093030.947069,
        "principalPayment": 17906.440862,
        "endPrincipalBalance": 1093030.947069,
        "beginPrincipalBalance": 1110937.387931,
        "prepayPrincipalPayment": 8276.719095,
        "scheduledPrincipalPayment": 9629.721767
    }
    {
        "date": "2045-02-25",
        "totalCashFlow": 16664.709001,
        "interestPayment": 455.429561,
        "principalBalance": 1076821.66763,
        "principalPayment": 16209.279439,
        "endPrincipalBalance": 1076821.66763,
        "beginPrincipalBalance": 1093030.947069,
        "prepayPrincipalPayment": 6641.972885,
        "scheduledPrincipalPayment": 9567.306554
    }
    {
        "date": "2045-03-25",
        "totalCashFlow": 16609.125637,
        "interestPayment": 448.675695,
        "principalBalance": 1060661.217688,
        "principalPayment": 16160.449942,
        "endPrincipalBalance": 1060661.217688,
        "beginPrincipalBalance": 1076821.66763,
        "prepayPrincipalPayment": 6641.889137,
        "scheduledPrincipalPayment": 9518.560806
    }
    {
        "date": "2045-04-25",
        "totalCashFlow": 18124.622835,
        "interestPayment": 441.942174,
        "principalBalance": 1042978.537027,
        "principalPayment": 17682.680661,
        "endPrincipalBalance": 1042978.537027,
        "beginPrincipalBalance": 1060661.217688,
        "prepayPrincipalPayment": 8213.500946,
        "scheduledPrincipalPayment": 9469.179714
    }
    {
        "date": "2045-05-25",
        "totalCashFlow": 17840.640834,
        "interestPayment": 434.57439,
        "principalBalance": 1025572.470583,
        "principalPayment": 17406.066444,
        "endPrincipalBalance": 1025572.470583,
        "beginPrincipalBalance": 1042978.537027,
        "prepayPrincipalPayment": 8001.087614,
        "scheduledPrincipalPayment": 9404.97883
    }
    {
        "date": "2045-06-25",
        "totalCashFlow": 18924.49206,
        "interestPayment": 427.321863,
        "principalBalance": 1007075.300386,
        "principalPayment": 18497.170197,
        "endPrincipalBalance": 1007075.300386,
        "beginPrincipalBalance": 1025572.470583,
        "prepayPrincipalPayment": 9155.276067,
        "scheduledPrincipalPayment": 9341.89413
    }
    {
        "date": "2045-07-25",
        "totalCashFlow": 18986.70377,
        "interestPayment": 419.614708,
        "principalBalance": 988508.211324,
        "principalPayment": 18567.089061,
        "endPrincipalBalance": 988508.211324,
        "beginPrincipalBalance": 1007075.300386,
        "prepayPrincipalPayment": 9299.713088,
        "scheduledPrincipalPayment": 9267.375974
    }
    {
        "date": "2045-08-25",
        "totalCashFlow": 17942.485873,
        "interestPayment": 411.878421,
        "principalBalance": 970977.603873,
        "principalPayment": 17530.607451,
        "endPrincipalBalance": 970977.603873,
        "beginPrincipalBalance": 988508.211324,
        "prepayPrincipalPayment": 8340.041208,
        "scheduledPrincipalPayment": 9190.566244
    }
    {
        "date": "2045-09-25",
        "totalCashFlow": 18346.23951,
        "interestPayment": 404.574002,
        "principalBalance": 953035.938364,
        "principalPayment": 17941.665509,
        "endPrincipalBalance": 953035.938364,
        "beginPrincipalBalance": 970977.603873,
        "prepayPrincipalPayment": 8819.875765,
        "scheduledPrincipalPayment": 9121.789743
    }
    {
        "date": "2045-10-25",
        "totalCashFlow": 16985.252215,
        "interestPayment": 397.098308,
        "principalBalance": 936447.784457,
        "principalPayment": 16588.153908,
        "endPrincipalBalance": 936447.784457,
        "beginPrincipalBalance": 953035.938364,
        "prepayPrincipalPayment": 7540.592997,
        "scheduledPrincipalPayment": 9047.560911
    }
    {
        "date": "2045-11-25",
        "totalCashFlow": 16718.289497,
        "interestPayment": 390.186577,
        "principalBalance": 920119.681536,
        "principalPayment": 16328.102921,
        "endPrincipalBalance": 920119.681536,
        "beginPrincipalBalance": 936447.784457,
        "prepayPrincipalPayment": 7343.4648,
        "scheduledPrincipalPayment": 8984.638121
    }
    {
        "date": "2045-12-25",
        "totalCashFlow": 16208.598558,
        "interestPayment": 383.383201,
        "principalBalance": 904294.466179,
        "principalPayment": 15825.215357,
        "endPrincipalBalance": 904294.466179,
        "beginPrincipalBalance": 920119.681536,
        "prepayPrincipalPayment": 6902.430881,
        "scheduledPrincipalPayment": 8922.784476
    }
    {
        "date": "2046-01-25",
        "totalCashFlow": 15843.11513,
        "interestPayment": 376.789361,
        "principalBalance": 888828.14041,
        "principalPayment": 15466.325769,
        "endPrincipalBalance": 888828.14041,
        "beginPrincipalBalance": 904294.466179,
        "prepayPrincipalPayment": 6601.908346,
        "scheduledPrincipalPayment": 8864.417424
    }
    {
        "date": "2046-02-25",
        "totalCashFlow": 14922.03337,
        "interestPayment": 370.345059,
        "principalBalance": 874276.452098,
        "principalPayment": 14551.688312,
        "endPrincipalBalance": 874276.452098,
        "beginPrincipalBalance": 888828.14041,
        "prepayPrincipalPayment": 5743.461585,
        "scheduledPrincipalPayment": 8808.226727
    }
    {
        "date": "2046-03-25",
        "totalCashFlow": 14682.009553,
        "interestPayment": 364.281855,
        "principalBalance": 859958.7244,
        "principalPayment": 14317.727698,
        "endPrincipalBalance": 859958.7244,
        "beginPrincipalBalance": 874276.452098,
        "prepayPrincipalPayment": 5557.872626,
        "scheduledPrincipalPayment": 8759.855073
    }
    {
        "date": "2046-04-25",
        "totalCashFlow": 15505.302097,
        "interestPayment": 358.316135,
        "principalBalance": 844811.738438,
        "principalPayment": 15146.985962,
        "endPrincipalBalance": 844811.738438,
        "beginPrincipalBalance": 859958.7244,
        "prepayPrincipalPayment": 6434.315617,
        "scheduledPrincipalPayment": 8712.670345
    }
    {
        "date": "2046-05-25",
        "totalCashFlow": 15792.622884,
        "interestPayment": 352.004891,
        "principalBalance": 829371.120446,
        "principalPayment": 15440.617993,
        "endPrincipalBalance": 829371.120446,
        "beginPrincipalBalance": 844811.738438,
        "prepayPrincipalPayment": 6784.797033,
        "scheduledPrincipalPayment": 8655.82096
    }
    {
        "date": "2046-06-25",
        "totalCashFlow": 16353.672491,
        "interestPayment": 345.5713,
        "principalBalance": 813363.019255,
        "principalPayment": 16008.101191,
        "endPrincipalBalance": 813363.019255,
        "beginPrincipalBalance": 829371.120446,
        "prepayPrincipalPayment": 7413.572604,
        "scheduledPrincipalPayment": 8594.528587
    }
    {
        "date": "2046-07-25",
        "totalCashFlow": 16112.401029,
        "interestPayment": 338.901258,
        "principalBalance": 797589.519483,
        "principalPayment": 15773.499771,
        "endPrincipalBalance": 797589.519483,
        "beginPrincipalBalance": 813363.019255,
        "prepayPrincipalPayment": 7247.72853,
        "scheduledPrincipalPayment": 8525.771241
    }
    {
        "date": "2046-08-25",
        "totalCashFlow": 15794.437938,
        "interestPayment": 332.328966,
        "principalBalance": 782127.410512,
        "principalPayment": 15462.108971,
        "endPrincipalBalance": 782127.410512,
        "beginPrincipalBalance": 797589.519483,
        "prepayPrincipalPayment": 7004.313055,
        "scheduledPrincipalPayment": 8457.795916
    }
    {
        "date": "2046-09-25",
        "totalCashFlow": 15827.366208,
        "interestPayment": 325.886421,
        "principalBalance": 766625.930725,
        "principalPayment": 15501.479787,
        "endPrincipalBalance": 766625.930725,
        "beginPrincipalBalance": 782127.410512,
        "prepayPrincipalPayment": 7110.023047,
        "scheduledPrincipalPayment": 8391.45674
    }
    {
        "date": "2046-10-25",
        "totalCashFlow": 14569.47294,
        "interestPayment": 319.427471,
        "principalBalance": 752375.885256,
        "principalPayment": 14250.045469,
        "endPrincipalBalance": 752375.885256,
        "beginPrincipalBalance": 766625.930725,
        "prepayPrincipalPayment": 5927.03882,
        "scheduledPrincipalPayment": 8323.006649
    }
    {
        "date": "2046-11-25",
        "totalCashFlow": 14737.637985,
        "interestPayment": 313.489952,
        "principalBalance": 737951.737223,
        "principalPayment": 14424.148033,
        "endPrincipalBalance": 737951.737223,
        "beginPrincipalBalance": 752375.885256,
        "prepayPrincipalPayment": 6157.593541,
        "scheduledPrincipalPayment": 8266.554492
    }
    {
        "date": "2046-12-25",
        "totalCashFlow": 14140.521232,
        "interestPayment": 307.479891,
        "principalBalance": 724118.695881,
        "principalPayment": 13833.041342,
        "endPrincipalBalance": 724118.695881,
        "beginPrincipalBalance": 737951.737223,
        "prepayPrincipalPayment": 5626.353838,
        "scheduledPrincipalPayment": 8206.687504
    }
    {
        "date": "2047-01-25",
        "totalCashFlow": 13841.764621,
        "interestPayment": 301.716123,
        "principalBalance": 710578.647384,
        "principalPayment": 13540.048498,
        "endPrincipalBalance": 710578.647384,
        "beginPrincipalBalance": 724118.695881,
        "prepayPrincipalPayment": 5388.152052,
        "scheduledPrincipalPayment": 8151.896446
    }
    {
        "date": "2047-02-25",
        "totalCashFlow": 13131.021677,
        "interestPayment": 296.074436,
        "principalBalance": 697743.700143,
        "principalPayment": 12834.94724,
        "endPrincipalBalance": 697743.700143,
        "beginPrincipalBalance": 710578.647384,
        "prepayPrincipalPayment": 4735.971875,
        "scheduledPrincipalPayment": 8098.975365
    }
    {
        "date": "2047-03-25",
        "totalCashFlow": 12927.22274,
        "interestPayment": 290.726542,
        "principalBalance": 685107.203945,
        "principalPayment": 12636.496198,
        "endPrincipalBalance": 685107.203945,
        "beginPrincipalBalance": 697743.700143,
        "prepayPrincipalPayment": 4583.742885,
        "scheduledPrincipalPayment": 8052.753313
    }
    {
        "date": "2047-04-25",
        "totalCashFlow": 13439.354995,
        "interestPayment": 285.461335,
        "principalBalance": 671953.310285,
        "principalPayment": 13153.89366,
        "endPrincipalBalance": 671953.310285,
        "beginPrincipalBalance": 685107.203945,
        "prepayPrincipalPayment": 5146.327074,
        "scheduledPrincipalPayment": 8007.566586
    }
    {
        "date": "2047-05-25",
        "totalCashFlow": 13783.660213,
        "interestPayment": 279.980546,
        "principalBalance": 658449.630618,
        "principalPayment": 13503.679667,
        "endPrincipalBalance": 658449.630618,
        "beginPrincipalBalance": 671953.310285,
        "prepayPrincipalPayment": 5548.697143,
        "scheduledPrincipalPayment": 7954.982524
    }
    {
        "date": "2047-06-25",
        "totalCashFlow": 14083.632741,
        "interestPayment": 274.354013,
        "principalBalance": 644640.35189,
        "principalPayment": 13809.278728,
        "endPrincipalBalance": 644640.35189,
        "beginPrincipalBalance": 658449.630618,
        "prepayPrincipalPayment": 5912.554762,
        "scheduledPrincipalPayment": 7896.723965
    }
    {
        "date": "2047-07-25",
        "totalCashFlow": 13685.482292,
        "interestPayment": 268.600147,
        "principalBalance": 631223.469744,
        "principalPayment": 13416.882146,
        "endPrincipalBalance": 631223.469744,
        "beginPrincipalBalance": 644640.35189,
        "prepayPrincipalPayment": 5583.776618,
        "scheduledPrincipalPayment": 7833.105527
    }
    {
        "date": "2047-08-25",
        "totalCashFlow": 13789.451675,
        "interestPayment": 263.009779,
        "principalBalance": 617697.027848,
        "principalPayment": 13526.441896,
        "endPrincipalBalance": 617697.027848,
        "beginPrincipalBalance": 631223.469744,
        "prepayPrincipalPayment": 5753.932182,
        "scheduledPrincipalPayment": 7772.509714
    }
    {
        "date": "2047-09-25",
        "totalCashFlow": 13441.639543,
        "interestPayment": 257.373762,
        "principalBalance": 604512.762066,
        "principalPayment": 13184.265782,
        "endPrincipalBalance": 604512.762066,
        "beginPrincipalBalance": 617697.027848,
        "prepayPrincipalPayment": 5475.468206,
        "scheduledPrincipalPayment": 7708.797576
    }
    {
        "date": "2047-10-25",
        "totalCashFlow": 12805.950815,
        "interestPayment": 251.880318,
        "principalBalance": 591958.691569,
        "principalPayment": 12554.070497,
        "endPrincipalBalance": 591958.691569,
        "beginPrincipalBalance": 604512.762066,
        "prepayPrincipalPayment": 4906.511874,
        "scheduledPrincipalPayment": 7647.558624
    }
    {
        "date": "2047-11-25",
        "totalCashFlow": 12749.073242,
        "interestPayment": 246.649455,
        "principalBalance": 579456.267781,
        "principalPayment": 12502.423787,
        "endPrincipalBalance": 579456.267781,
        "beginPrincipalBalance": 591958.691569,
        "prepayPrincipalPayment": 4909.830961,
        "scheduledPrincipalPayment": 7592.592826
    }
    {
        "date": "2047-12-25",
        "totalCashFlow": 12151.361628,
        "interestPayment": 241.440112,
        "principalBalance": 567546.346265,
        "principalPayment": 11909.921516,
        "endPrincipalBalance": 567546.346265,
        "beginPrincipalBalance": 579456.267781,
        "prepayPrincipalPayment": 4373.278986,
        "scheduledPrincipalPayment": 7536.64253
    }
    {
        "date": "2048-01-25",
        "totalCashFlow": 12164.666565,
        "interestPayment": 236.477644,
        "principalBalance": 555618.157345,
        "principalPayment": 11928.188921,
        "endPrincipalBalance": 555618.157345,
        "beginPrincipalBalance": 567546.346265,
        "prepayPrincipalPayment": 4441.385949,
        "scheduledPrincipalPayment": 7486.802972
    }
    {
        "date": "2048-02-25",
        "totalCashFlow": 11496.354147,
        "interestPayment": 231.507566,
        "principalBalance": 544353.310763,
        "principalPayment": 11264.846582,
        "endPrincipalBalance": 544353.310763,
        "beginPrincipalBalance": 555618.157345,
        "prepayPrincipalPayment": 3829.678571,
        "scheduledPrincipalPayment": 7435.168011
    }
    {
        "date": "2048-03-25",
        "totalCashFlow": 11321.968956,
        "interestPayment": 226.813879,
        "principalBalance": 533258.155686,
        "principalPayment": 11095.155077,
        "endPrincipalBalance": 533258.155686,
        "beginPrincipalBalance": 544353.310763,
        "prepayPrincipalPayment": 3704.23927,
        "scheduledPrincipalPayment": 7390.915807
    }
    {
        "date": "2048-04-25",
        "totalCashFlow": 11775.192455,
        "interestPayment": 222.190898,
        "principalBalance": 521705.154129,
        "principalPayment": 11553.001557,
        "endPrincipalBalance": 521705.154129,
        "beginPrincipalBalance": 533258.155686,
        "prepayPrincipalPayment": 4205.42628,
        "scheduledPrincipalPayment": 7347.575276
    }
    {
        "date": "2048-05-25",
        "totalCashFlow": 11941.567118,
        "interestPayment": 217.377148,
        "principalBalance": 509980.964158,
        "principalPayment": 11724.189971,
        "endPrincipalBalance": 509980.964158,
        "beginPrincipalBalance": 521705.154129,
        "prepayPrincipalPayment": 4427.776811,
        "scheduledPrincipalPayment": 7296.413159
    }
    {
        "date": "2048-06-25",
        "totalCashFlow": 11802.84422,
        "interestPayment": 212.492068,
        "principalBalance": 498390.612006,
        "principalPayment": 11590.352152,
        "endPrincipalBalance": 498390.612006,
        "beginPrincipalBalance": 509980.964158,
        "prepayPrincipalPayment": 4349.20791,
        "scheduledPrincipalPayment": 7241.144242
    }
    {
        "date": "2048-07-25",
        "totalCashFlow": 12021.675395,
        "interestPayment": 207.662755,
        "principalBalance": 486576.599366,
        "principalPayment": 11814.01264,
        "endPrincipalBalance": 486576.599366,
        "beginPrincipalBalance": 498390.612006,
        "prepayPrincipalPayment": 4628.034015,
        "scheduledPrincipalPayment": 7185.978626
    }
    {
        "date": "2048-08-25",
        "totalCashFlow": 11786.85144,
        "interestPayment": 202.74025,
        "principalBalance": 474992.488176,
        "principalPayment": 11584.11119,
        "endPrincipalBalance": 474992.488176,
        "beginPrincipalBalance": 486576.599366,
        "prepayPrincipalPayment": 4458.422582,
        "scheduledPrincipalPayment": 7125.688609
    }
    {
        "date": "2048-09-25",
        "totalCashFlow": 11390.634228,
        "interestPayment": 197.913537,
        "principalBalance": 463799.767485,
        "principalPayment": 11192.720691,
        "endPrincipalBalance": 463799.767485,
        "beginPrincipalBalance": 474992.488176,
        "prepayPrincipalPayment": 4125.940419,
        "scheduledPrincipalPayment": 7066.780272
    }
    {
        "date": "2048-10-25",
        "totalCashFlow": 11133.690513,
        "interestPayment": 193.249903,
        "principalBalance": 452859.326875,
        "principalPayment": 10940.440609,
        "endPrincipalBalance": 452859.326875,
        "beginPrincipalBalance": 463799.767485,
        "prepayPrincipalPayment": 3928.675433,
        "scheduledPrincipalPayment": 7011.765176
    }
    {
        "date": "2048-11-25",
        "totalCashFlow": 10858.685573,
        "interestPayment": 188.691386,
        "principalBalance": 442189.332689,
        "principalPayment": 10669.994187,
        "endPrincipalBalance": 442189.332689,
        "beginPrincipalBalance": 452859.326875,
        "prepayPrincipalPayment": 3711.293671,
        "scheduledPrincipalPayment": 6958.700516
    }
    {
        "date": "2048-12-25",
        "totalCashFlow": 10503.296595,
        "interestPayment": 184.245555,
        "principalBalance": 431870.281649,
        "principalPayment": 10319.05104,
        "endPrincipalBalance": 431870.281649,
        "beginPrincipalBalance": 442189.332689,
        "prepayPrincipalPayment": 3411.080453,
        "scheduledPrincipalPayment": 6907.970587
    }
    {
        "date": "2049-01-25",
        "totalCashFlow": 10571.923682,
        "interestPayment": 179.945951,
        "principalBalance": 421478.303918,
        "principalPayment": 10391.977731,
        "endPrincipalBalance": 421478.303918,
        "beginPrincipalBalance": 431870.281649,
        "prepayPrincipalPayment": 3531.002012,
        "scheduledPrincipalPayment": 6860.975719
    }
    {
        "date": "2049-02-25",
        "totalCashFlow": 9853.573361,
        "interestPayment": 175.61596,
        "principalBalance": 411800.346517,
        "principalPayment": 9677.957401,
        "endPrincipalBalance": 411800.346517,
        "beginPrincipalBalance": 421478.303918,
        "prepayPrincipalPayment": 2866.895594,
        "scheduledPrincipalPayment": 6811.061807
    }
    {
        "date": "2049-03-25",
        "totalCashFlow": 9879.264671,
        "interestPayment": 171.583478,
        "principalBalance": 402092.665325,
        "principalPayment": 9707.681193,
        "endPrincipalBalance": 402092.665325,
        "beginPrincipalBalance": 411800.346517,
        "prepayPrincipalPayment": 2936.663395,
        "scheduledPrincipalPayment": 6771.017798
    }
    {
        "date": "2049-04-25",
        "totalCashFlow": 10282.194265,
        "interestPayment": 167.538611,
        "principalBalance": 391978.00967,
        "principalPayment": 10114.655655,
        "endPrincipalBalance": 391978.00967,
        "beginPrincipalBalance": 402092.665325,
        "prepayPrincipalPayment": 3385.729087,
        "scheduledPrincipalPayment": 6728.926567
    }
    {
        "date": "2049-05-25",
        "totalCashFlow": 10281.027179,
        "interestPayment": 163.324171,
        "principalBalance": 381860.306661,
        "principalPayment": 10117.703009,
        "endPrincipalBalance": 381860.306661,
        "beginPrincipalBalance": 391978.00967,
        "prepayPrincipalPayment": 3439.45087,
        "scheduledPrincipalPayment": 6678.252139
    }
    {
        "date": "2049-06-25",
        "totalCashFlow": 10227.75619,
        "interestPayment": 159.108461,
        "principalBalance": 371791.658932,
        "principalPayment": 10068.647729,
        "endPrincipalBalance": 371791.658932,
        "beginPrincipalBalance": 381860.306661,
        "prepayPrincipalPayment": 3443.115852,
        "scheduledPrincipalPayment": 6625.531877
    }
    {
        "date": "2049-07-25",
        "totalCashFlow": 10375.595222,
        "interestPayment": 154.913191,
        "principalBalance": 361570.976901,
        "principalPayment": 10220.682031,
        "endPrincipalBalance": 361570.976901,
        "beginPrincipalBalance": 371791.658932,
        "prepayPrincipalPayment": 3649.107088,
        "scheduledPrincipalPayment": 6571.574943
    }
    {
        "date": "2049-08-25",
        "totalCashFlow": 10121.592848,
        "interestPayment": 150.654574,
        "principalBalance": 351600.038627,
        "principalPayment": 9970.938275,
        "endPrincipalBalance": 351600.038627,
        "beginPrincipalBalance": 361570.976901,
        "prepayPrincipalPayment": 3458.246419,
        "scheduledPrincipalPayment": 6512.691855
    }
    {
        "date": "2049-09-25",
        "totalCashFlow": 10010.07792,
        "interestPayment": 146.500016,
        "principalBalance": 341736.460723,
        "principalPayment": 9863.577904,
        "endPrincipalBalance": 341736.460723,
        "beginPrincipalBalance": 351600.038627,
        "prepayPrincipalPayment": 3407.6013,
        "scheduledPrincipalPayment": 6455.976604
    }
    {
        "date": "2049-10-25",
        "totalCashFlow": 9742.875058,
        "interestPayment": 142.390192,
        "principalBalance": 332135.975857,
        "principalPayment": 9600.484866,
        "endPrincipalBalance": 332135.975857,
        "beginPrincipalBalance": 341736.460723,
        "prepayPrincipalPayment": 3201.589426,
        "scheduledPrincipalPayment": 6398.89544
    }
    {
        "date": "2049-11-25",
        "totalCashFlow": 9480.049931,
        "interestPayment": 138.38999,
        "principalBalance": 322794.315915,
        "principalPayment": 9341.659941,
        "endPrincipalBalance": 322794.315915,
        "beginPrincipalBalance": 332135.975857,
        "prepayPrincipalPayment": 2997.2552,
        "scheduledPrincipalPayment": 6344.404741
    }
    {
        "date": "2049-12-25",
        "totalCashFlow": 9355.242103,
        "interestPayment": 134.497632,
        "principalBalance": 313573.571444,
        "principalPayment": 9220.744471,
        "endPrincipalBalance": 313573.571444,
        "beginPrincipalBalance": 322794.315915,
        "prepayPrincipalPayment": 2928.159768,
        "scheduledPrincipalPayment": 6292.584703
    }
    {
        "date": "2050-01-25",
        "totalCashFlow": 9262.977542,
        "interestPayment": 130.655655,
        "principalBalance": 304441.249557,
        "principalPayment": 9132.321887,
        "endPrincipalBalance": 304441.249557,
        "beginPrincipalBalance": 313573.571444,
        "prepayPrincipalPayment": 2891.459773,
        "scheduledPrincipalPayment": 6240.862114
    }
    {
        "date": "2050-02-25",
        "totalCashFlow": 8870.040255,
        "interestPayment": 126.850521,
        "principalBalance": 295698.059822,
        "principalPayment": 8743.189735,
        "endPrincipalBalance": 295698.059822,
        "beginPrincipalBalance": 304441.249557,
        "prepayPrincipalPayment": 2554.60341,
        "scheduledPrincipalPayment": 6188.586324
    }
    {
        "date": "2050-03-25",
        "totalCashFlow": 8797.546952,
        "interestPayment": 123.207525,
        "principalBalance": 287023.720395,
        "principalPayment": 8674.339427,
        "endPrincipalBalance": 287023.720395,
        "beginPrincipalBalance": 295698.059822,
        "prepayPrincipalPayment": 2532.368555,
        "scheduledPrincipalPayment": 6141.970872
    }
    {
        "date": "2050-04-25",
        "totalCashFlow": 9017.256529,
        "interestPayment": 119.593217,
        "principalBalance": 278126.057083,
        "principalPayment": 8897.663312,
        "endPrincipalBalance": 278126.057083,
        "beginPrincipalBalance": 287023.720395,
        "prepayPrincipalPayment": 2803.066297,
        "scheduledPrincipalPayment": 6094.597015
    }
    {
        "date": "2050-05-25",
        "totalCashFlow": 8910.705411,
        "interestPayment": 115.885857,
        "principalBalance": 269331.237529,
        "principalPayment": 8794.819554,
        "endPrincipalBalance": 269331.237529,
        "beginPrincipalBalance": 278126.057083,
        "prepayPrincipalPayment": 2754.748269,
        "scheduledPrincipalPayment": 6040.071285
    }
    {
        "date": "2050-06-25",
        "totalCashFlow": 8939.383459,
        "interestPayment": 112.221349,
        "principalBalance": 260504.075418,
        "principalPayment": 8827.16211,
        "endPrincipalBalance": 260504.075418,
        "beginPrincipalBalance": 269331.237529,
        "prepayPrincipalPayment": 2842.015791,
        "scheduledPrincipalPayment": 5985.146319
    }
    {
        "date": "2050-07-25",
        "totalCashFlow": 8922.020527,
        "interestPayment": 108.543365,
        "principalBalance": 251690.598256,
        "principalPayment": 8813.477162,
        "endPrincipalBalance": 251690.598256,
        "beginPrincipalBalance": 260504.075418,
        "prepayPrincipalPayment": 2886.754951,
        "scheduledPrincipalPayment": 5926.722211
    }
    {
        "date": "2050-08-25",
        "totalCashFlow": 8650.136345,
        "interestPayment": 104.871083,
        "principalBalance": 243145.332994,
        "principalPayment": 8545.265262,
        "endPrincipalBalance": 243145.332994,
        "beginPrincipalBalance": 251690.598256,
        "prepayPrincipalPayment": 2679.644874,
        "scheduledPrincipalPayment": 5865.620388
    }
    {
        "date": "2050-09-25",
        "totalCashFlow": 8633.621993,
        "interestPayment": 101.310555,
        "principalBalance": 234613.021557,
        "principalPayment": 8532.311438,
        "endPrincipalBalance": 234613.021557,
        "beginPrincipalBalance": 243145.332994,
        "prepayPrincipalPayment": 2724.586535,
        "scheduledPrincipalPayment": 5807.724903
    }
    {
        "date": "2050-10-25",
        "totalCashFlow": 8358.535002,
        "interestPayment": 97.755426,
        "principalBalance": 226352.24198,
        "principalPayment": 8260.779577,
        "endPrincipalBalance": 226352.24198,
        "beginPrincipalBalance": 234613.021557,
        "prepayPrincipalPayment": 2513.745888,
        "scheduledPrincipalPayment": 5747.033689
    }
    {
        "date": "2050-11-25",
        "totalCashFlow": 8141.38968,
        "interestPayment": 94.313434,
        "principalBalance": 218305.165734,
        "principalPayment": 8047.076246,
        "endPrincipalBalance": 218305.165734,
        "beginPrincipalBalance": 226352.24198,
        "prepayPrincipalPayment": 2357.244267,
        "scheduledPrincipalPayment": 5689.831978
    }
    {
        "date": "2050-12-25",
        "totalCashFlow": 8011.526875,
        "interestPayment": 90.960486,
        "principalBalance": 210384.599345,
        "principalPayment": 7920.56639,
        "endPrincipalBalance": 210384.599345,
        "beginPrincipalBalance": 218305.165734,
        "prepayPrincipalPayment": 2285.652914,
        "scheduledPrincipalPayment": 5634.913476
    }
    {
        "date": "2051-01-25",
        "totalCashFlow": 7902.56753,
        "interestPayment": 87.66025,
        "principalBalance": 202569.692064,
        "principalPayment": 7814.90728,
        "endPrincipalBalance": 202569.692064,
        "beginPrincipalBalance": 210384.599345,
        "prepayPrincipalPayment": 2234.747873,
        "scheduledPrincipalPayment": 5580.159407
    }
    {
        "date": "2051-02-25",
        "totalCashFlow": 7610.293261,
        "interestPayment": 84.404038,
        "principalBalance": 195043.802842,
        "principalPayment": 7525.889223,
        "endPrincipalBalance": 195043.802842,
        "beginPrincipalBalance": 202569.692064,
        "prepayPrincipalPayment": 2000.869145,
        "scheduledPrincipalPayment": 5525.020078
    }
    {
        "date": "2051-03-25",
        "totalCashFlow": 7515.740222,
        "interestPayment": 81.268251,
        "principalBalance": 187609.330871,
        "principalPayment": 7434.471971,
        "endPrincipalBalance": 187609.330871,
        "beginPrincipalBalance": 195043.802842,
        "prepayPrincipalPayment": 1959.858333,
        "scheduledPrincipalPayment": 5474.613638
    }
    {
        "date": "2051-04-25",
        "totalCashFlow": 7580.80624,
        "interestPayment": 78.170555,
        "principalBalance": 180106.695185,
        "principalPayment": 7502.635685,
        "endPrincipalBalance": 180106.695185,
        "beginPrincipalBalance": 187609.330871,
        "prepayPrincipalPayment": 2078.977497,
        "scheduledPrincipalPayment": 5423.658189
    }
    {
        "date": "2051-05-25",
        "totalCashFlow": 7460.570936,
        "interestPayment": 75.044456,
        "principalBalance": 172721.168706,
        "principalPayment": 7385.52648,
        "endPrincipalBalance": 172721.168706,
        "beginPrincipalBalance": 180106.695185,
        "prepayPrincipalPayment": 2018.174171,
        "scheduledPrincipalPayment": 5367.352309
    }
    {
        "date": "2051-06-25",
        "totalCashFlow": 7471.860173,
        "interestPayment": 71.967154,
        "principalBalance": 165321.275686,
        "principalPayment": 7399.893019,
        "endPrincipalBalance": 165321.275686,
        "beginPrincipalBalance": 172721.168706,
        "prepayPrincipalPayment": 2089.005208,
        "scheduledPrincipalPayment": 5310.887812
    }
    {
        "date": "2051-07-25",
        "totalCashFlow": 7366.99443,
        "interestPayment": 68.883865,
        "principalBalance": 158023.165121,
        "principalPayment": 7298.110565,
        "endPrincipalBalance": 158023.165121,
        "beginPrincipalBalance": 165321.275686,
        "prepayPrincipalPayment": 2048.030764,
        "scheduledPrincipalPayment": 5250.079801
    }
    {
        "date": "2051-08-25",
        "totalCashFlow": 7150.626545,
        "interestPayment": 65.842985,
        "principalBalance": 150938.381561,
        "principalPayment": 7084.78356,
        "endPrincipalBalance": 150938.381561,
        "beginPrincipalBalance": 158023.165121,
        "prepayPrincipalPayment": 1896.477037,
        "scheduledPrincipalPayment": 5188.306522
    }
    {
        "date": "2051-09-25",
        "totalCashFlow": 7099.631339,
        "interestPayment": 62.890992,
        "principalBalance": 143901.641214,
        "principalPayment": 7036.740347,
        "endPrincipalBalance": 143901.641214,
        "beginPrincipalBalance": 150938.381561,
        "prepayPrincipalPayment": 1907.476375,
        "scheduledPrincipalPayment": 5129.263972
    }
    {
        "date": "2051-10-25",
        "totalCashFlow": 6873.629641,
        "interestPayment": 59.959017,
        "principalBalance": 137087.970591,
        "principalPayment": 6813.670623,
        "endPrincipalBalance": 137087.970591,
        "beginPrincipalBalance": 143901.641214,
        "prepayPrincipalPayment": 1746.234649,
        "scheduledPrincipalPayment": 5067.435975
    }
    {
        "date": "2051-11-25",
        "totalCashFlow": 6756.478609,
        "interestPayment": 57.119988,
        "principalBalance": 130388.61197,
        "principalPayment": 6699.358621,
        "endPrincipalBalance": 130388.61197,
        "beginPrincipalBalance": 137087.970591,
        "prepayPrincipalPayment": 1690.447868,
        "scheduledPrincipalPayment": 5008.910753
    }
    {
        "date": "2051-12-25",
        "totalCashFlow": 6613.517654,
        "interestPayment": 54.328588,
        "principalBalance": 123829.422905,
        "principalPayment": 6559.189065,
        "endPrincipalBalance": 123829.422905,
        "beginPrincipalBalance": 130388.61197,
        "prepayPrincipalPayment": 1609.23531,
        "scheduledPrincipalPayment": 4949.953755
    }
    {
        "date": "2052-01-25",
        "totalCashFlow": 6484.771771,
        "interestPayment": 51.595593,
        "principalBalance": 117396.246727,
        "principalPayment": 6433.176178,
        "endPrincipalBalance": 117396.246727,
        "beginPrincipalBalance": 123829.422905,
        "prepayPrincipalPayment": 1541.634645,
        "scheduledPrincipalPayment": 4891.541532
    }
    {
        "date": "2052-02-25",
        "totalCashFlow": 6311.675134,
        "interestPayment": 48.915103,
        "principalBalance": 111133.486696,
        "principalPayment": 6262.760031,
        "endPrincipalBalance": 111133.486696,
        "beginPrincipalBalance": 117396.246727,
        "prepayPrincipalPayment": 1429.591779,
        "scheduledPrincipalPayment": 4833.168252
    }
    {
        "date": "2052-03-25",
        "totalCashFlow": 6208.033942,
        "interestPayment": 46.305619,
        "principalBalance": 104971.758373,
        "principalPayment": 6161.728323,
        "endPrincipalBalance": 104971.758373,
        "beginPrincipalBalance": 111133.486696,
        "prepayPrincipalPayment": 1384.972445,
        "scheduledPrincipalPayment": 4776.755878
    }
    {
        "date": "2052-04-25",
        "totalCashFlow": 6145.610057,
        "interestPayment": 43.738233,
        "principalBalance": 98869.886549,
        "principalPayment": 6101.871824,
        "endPrincipalBalance": 98869.886549,
        "beginPrincipalBalance": 104971.758373,
        "prepayPrincipalPayment": 1382.407648,
        "scheduledPrincipalPayment": 4719.464176
    }
    {
        "date": "2052-05-25",
        "totalCashFlow": 6070.627844,
        "interestPayment": 41.195786,
        "principalBalance": 92840.454491,
        "principalPayment": 6029.432058,
        "endPrincipalBalance": 92840.454491,
        "beginPrincipalBalance": 98869.886549,
        "prepayPrincipalPayment": 1370.197608,
        "scheduledPrincipalPayment": 4659.23445
    }
    {
        "date": "2052-06-25",
        "totalCashFlow": 5983.802483,
        "interestPayment": 38.683523,
        "principalBalance": 86895.335531,
        "principalPayment": 5945.11896,
        "endPrincipalBalance": 86895.335531,
        "beginPrincipalBalance": 92840.454491,
        "prepayPrincipalPayment": 1348.86553,
        "scheduledPrincipalPayment": 4596.25343
    }
    {
        "date": "2052-07-25",
        "totalCashFlow": 5828.974854,
        "interestPayment": 36.20639,
        "principalBalance": 81102.567067,
        "principalPayment": 5792.768464,
        "endPrincipalBalance": 81102.567067,
        "beginPrincipalBalance": 86895.335531,
        "prepayPrincipalPayment": 1262.056943,
        "scheduledPrincipalPayment": 4530.711521
    }
    {
        "date": "2052-08-25",
        "totalCashFlow": 5718.048543,
        "interestPayment": 33.792736,
        "principalBalance": 75418.31126,
        "principalPayment": 5684.255807,
        "endPrincipalBalance": 75418.31126,
        "beginPrincipalBalance": 81102.567067,
        "prepayPrincipalPayment": 1218.320313,
        "scheduledPrincipalPayment": 4465.935494
    }
    {
        "date": "2052-09-25",
        "totalCashFlow": 5567.223094,
        "interestPayment": 31.424296,
        "principalBalance": 69882.512462,
        "principalPayment": 5535.798797,
        "endPrincipalBalance": 69882.512462,
        "beginPrincipalBalance": 75418.31126,
        "prepayPrincipalPayment": 1136.281838,
        "scheduledPrincipalPayment": 4399.51696
    }
    {
        "date": "2052-10-25",
        "totalCashFlow": 5395.761705,
        "interestPayment": 29.117714,
        "principalBalance": 64515.868471,
        "principalPayment": 5366.643992,
        "endPrincipalBalance": 64515.868471,
        "beginPrincipalBalance": 69882.512462,
        "prepayPrincipalPayment": 1033.008628,
        "scheduledPrincipalPayment": 4333.635364
    }
    {
        "date": "2052-11-25",
        "totalCashFlow": 5270.499645,
        "interestPayment": 26.881612,
        "principalBalance": 59272.250437,
        "principalPayment": 5243.618034,
        "endPrincipalBalance": 59272.250437,
        "beginPrincipalBalance": 64515.868471,
        "prepayPrincipalPayment": 973.834945,
        "scheduledPrincipalPayment": 4269.783088
    }
    {
        "date": "2052-12-25",
        "totalCashFlow": 5106.540378,
        "interestPayment": 24.696771,
        "principalBalance": 54190.40683,
        "principalPayment": 5081.843607,
        "endPrincipalBalance": 54190.40683,
        "beginPrincipalBalance": 59272.250437,
        "prepayPrincipalPayment": 876.702717,
        "scheduledPrincipalPayment": 4205.140891
    }
    {
        "date": "2053-01-25",
        "totalCashFlow": 4985.49648,
        "interestPayment": 22.579336,
        "principalBalance": 49227.489686,
        "principalPayment": 4962.917144,
        "endPrincipalBalance": 49227.489686,
        "beginPrincipalBalance": 54190.40683,
        "prepayPrincipalPayment": 820.414101,
        "scheduledPrincipalPayment": 4142.503043
    }
    {
        "date": "2053-02-25",
        "totalCashFlow": 4824.035033,
        "interestPayment": 20.511454,
        "principalBalance": 44423.966107,
        "principalPayment": 4803.523579,
        "endPrincipalBalance": 44423.966107,
        "beginPrincipalBalance": 49227.489686,
        "prepayPrincipalPayment": 724.682463,
        "scheduledPrincipalPayment": 4078.841116
    }
    {
        "date": "2053-03-25",
        "totalCashFlow": 4693.225116,
        "interestPayment": 18.509986,
        "principalBalance": 39749.250977,
        "principalPayment": 4674.71513,
        "endPrincipalBalance": 39749.250977,
        "beginPrincipalBalance": 44423.966107,
        "prepayPrincipalPayment": 657.163034,
        "scheduledPrincipalPayment": 4017.552097
    }
    {
        "date": "2053-04-25",
        "totalCashFlow": 4586.236817,
        "interestPayment": 16.562188,
        "principalBalance": 35179.576348,
        "principalPayment": 4569.674629,
        "endPrincipalBalance": 35179.576348,
        "beginPrincipalBalance": 39749.250977,
        "prepayPrincipalPayment": 613.346428,
        "scheduledPrincipalPayment": 3956.328201
    }
    {
        "date": "2053-05-25",
        "totalCashFlow": 4468.76246,
        "interestPayment": 14.658157,
        "principalBalance": 30725.472045,
        "principalPayment": 4454.104303,
        "endPrincipalBalance": 30725.472045,
        "beginPrincipalBalance": 35179.576348,
        "prepayPrincipalPayment": 561.521066,
        "scheduledPrincipalPayment": 3892.583237
    }
    {
        "date": "2053-06-25",
        "totalCashFlow": 4334.905132,
        "interestPayment": 12.80228,
        "principalBalance": 26403.369193,
        "principalPayment": 4322.102852,
        "endPrincipalBalance": 26403.369193,
        "beginPrincipalBalance": 30725.472045,
        "prepayPrincipalPayment": 495.399473,
        "scheduledPrincipalPayment": 3826.703379
    }
    {
        "date": "2053-07-25",
        "totalCashFlow": 4197.96236,
        "interestPayment": 11.001404,
        "principalBalance": 22216.408237,
        "principalPayment": 4186.960956,
        "endPrincipalBalance": 22216.408237,
        "beginPrincipalBalance": 26403.369193,
        "prepayPrincipalPayment": 426.821927,
        "scheduledPrincipalPayment": 3760.139029
    }
    {
        "date": "2053-08-25",
        "totalCashFlow": 4058.719497,
        "interestPayment": 9.256837,
        "principalBalance": 18166.945578,
        "principalPayment": 4049.46266,
        "endPrincipalBalance": 18166.945578,
        "beginPrincipalBalance": 22216.408237,
        "prepayPrincipalPayment": 356.35878,
        "scheduledPrincipalPayment": 3693.10388
    }
    {
        "date": "2053-09-25",
        "totalCashFlow": 3912.786741,
        "interestPayment": 7.569561,
        "principalBalance": 14261.728398,
        "principalPayment": 3905.21718,
        "endPrincipalBalance": 14261.728398,
        "beginPrincipalBalance": 18166.945578,
        "prepayPrincipalPayment": 279.389744,
        "scheduledPrincipalPayment": 3625.827436
    }
    {
        "date": "2053-10-25",
        "totalCashFlow": 3773.017643,
        "interestPayment": 5.942387,
        "principalBalance": 10494.653141,
        "principalPayment": 3767.075256,
        "endPrincipalBalance": 10494.653141,
        "beginPrincipalBalance": 14261.728398,
        "prepayPrincipalPayment": 207.209311,
        "scheduledPrincipalPayment": 3559.865945
    }
    {
        "date": "2053-11-25",
        "totalCashFlow": 3636.548042,
        "interestPayment": 4.372772,
        "principalBalance": 6862.477871,
        "principalPayment": 3632.17527,
        "endPrincipalBalance": 6862.477871,
        "beginPrincipalBalance": 10494.653141,
        "prepayPrincipalPayment": 137.599004,
        "scheduledPrincipalPayment": 3494.576266
    }
    {
        "date": "2053-12-25",
        "totalCashFlow": 3498.692278,
        "interestPayment": 2.859366,
        "principalBalance": 3366.644959,
        "principalPayment": 3495.832912,
        "endPrincipalBalance": 3366.644959,
        "beginPrincipalBalance": 6862.477871,
        "prepayPrincipalPayment": 66.38015,
        "scheduledPrincipalPayment": 3429.452762
    }
    {
        "date": "2054-01-25",
        "totalCashFlow": 3368.047728,
        "interestPayment": 1.402769,
        "principalBalance": 0.0,
        "principalPayment": 3366.644959,
        "endPrincipalBalance": 0.0,
        "beginPrincipalBalance": 3366.644959,
        "prepayPrincipalPayment": 0.0,
        "scheduledPrincipalPayment": 3366.644959
    }

    """

    try:
        logger.info("Calling get_cash_flow_sync")

        response = Client().yield_book_rest.get_cash_flow_sync(
            id=id,
            id_type=id_type,
            pricing_date=pricing_date,
            par_amount=par_amount,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called get_cash_flow_sync")

        return output
    except Exception as err:
        logger.error("Error get_cash_flow_sync.")
        check_exception_and_raise(err, logger)


def get_csv_bulk_result(*, ids: List[str], fields: List[str], job: Optional[str] = None) -> str:
    """
    Retrieve bulk results with multiple request id or request name.

    Parameters
    ----------
    ids : List[str]
          Ids can be provided comma separated. Different formats for id are:
          1) RequestId R-number
          2) Request name R:name. In this case also provide jobid (J-number) or jobname (J:name)
          3) Jobid J-number
          4) Job name J:name - only 1 active job with the jobname
          5) Tag name T:name. In this case also provide jobid (J-number) or jobname (J:name)
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    fields : List[str]


    Returns
    --------
    str
        A sequence of textual characters.

    Examples
    --------


    """

    try:
        logger.info("Calling get_csv_bulk_result")

        response = Client().yield_book_rest.get_csv_bulk_result(ids=ids, job=job, fields=fields)

        output = response
        logger.info("Called get_csv_bulk_result")

        return output
    except Exception as err:
        logger.error("Error get_csv_bulk_result.")
        check_exception_and_raise(err, logger)


def get_formatted_result(*, request_id_parameter: str, format: str, job: Optional[str] = None) -> Any:
    """
    Retrieve single formatted result using request id or request name.

    Parameters
    ----------
    request_id_parameter : str
        Unique request id. This can be of the format R-number or request name. If request name is used, corresponding job information should be passed in the query parameter.
    format : str
        Only "html" format supported for now.
    job : str, optional
        Job reference. This can be of the form J-number or job name.

    Returns
    --------
    Any


    Examples
    --------
    >>> # link a request to the job
    >>> indic_response = request_bond_indic_async_get(id="999818YT",
    >>>                                               id_type=IdTypeEnum.CUSIP
    >>>         )
    >>>
    >>> # provide a window of time for job to finish
    >>> time.sleep(10)
    >>>
    >>> # get result
    >>> response = get_formatted_result(request_id_parameter=indic_response['requestId'], format="html")
    >>>
    >>> print(response)


    <!DOCTYPE HTML>
    <html>
       <head>
          <style>
             html,
    body {
        font-family: Arial, sans-serif;
        font-size: 11px;
    }

    html,
    body,
    div,
    span {
        box-sizing: content-box;
    }
    * {
        box-sizing: border-box;
    }
    *:before {
        box-sizing: border-box;
    }
    *:after {
        box-sizing: border-box;
    }

    button,
    input[type="button"] {
        font-size: 11px;
        cursor: pointer;
        outline: 0;
        border: none;
        border-radius: 3px;
        padding: 0 10px;
    }

    textarea {
        font-family: Arial, sans-serif;
        font-size: 11px;
        color: #5b6974;
        padding-left: 5px;
        padding-right: 5px;
    }
             .main-container {
        padding: 5px;
        margin: 0 auto;
    }
    .main-container .root-container {
        display: flex;
    }
    .main-container .section-container {
        display: flex;
        flex-direction: row;
        width: 1375px;
        flex-wrap: wrap;
        margin: 0 auto;
    }

    .section-container .json-group {
        margin: 5px 10px 15px 5px;
        padding: 15px 20px 15px 15px;
        border: solid #e9ebec;
        overflow: auto;
        width: 1315px;
    }

    .main-container .section-column-container {
        display: flex;
        flex-direction: column;
    }

    .main-container .top-info {
        padding-left: 10px;
        width: 1375px;
        margin: 0 auto;
    }
    .main-container .top-info label {
        font-size: 12px;
        font-weight: bold;
        margin-right: 5px;
    }
    .section-container .section-group {
        margin: 5px 10px 15px 5px;
        padding: 15px 20px 15px 15px;
        border: solid #e9ebec;
        overflow: auto;
        min-width: 400px;
    }
    .section-container .section-group .header {
        padding: 5px;
        padding-top: 1px;
        font-weight: bold;
        /* text-transform: uppercase; */
    }
    .section-container .section-group table {
        width: 100%;
        font-size: 11px;
    }
    .section-container .section-group table td {
        padding: 3px;
        border-bottom: 1px solid rgba(0, 0, 0, 0.08);
    }
    .section-container .key-value-table td:nth-child(1) {
        width: 60%;
    }
    .section-container .key-value-table td:nth-child(1) span:nth-child(2) {
        background-color: #f3df9d;
    }
    .section-container .key-value-table td:nth-child(2) {
        width: 40%;
        text-align: right;
    }

    .section-container .partial-table td:nth-child(1),
    .section-container .partial-table th:nth-child(1) {
        width: 20%;
        text-align: center;
    }
    .section-container .partial-table th span:nth-child(3) {
        background-color: #f3df9d;
    }
    .section-container .partial-table td:nth-child(2),
    .section-container .partial-table td:nth-child(3),
    .section-container .partial-table th:nth-child(2),
    .section-container .partial-table th:nth-child(3) {
        width: 40%;
        text-align: right;
    }

    .section-container .regular-table th {
        text-align: right;
    }
    .section-container .regular-table th:nth-child(1) {
        text-align: left;
    }
    .section-container .regular-table td {
        padding: 3px;
        border-bottom: 1px solid rgba(0, 0, 0, 0.08);
        text-align: right;
    }
    .section-container .regular-table th span:nth-child(3) {
        background-color: #f3df9d;
    }
    .section-container .regular-table td:nth-child(1) {
        text-align: left;
    }
    .section-container .prepayment-model-projection-table {
        width: calc(66.66% - 55px);
    }
    .section-container .prepayment-model-projection-table td {
        width: 16%;
    }
    .section-container .prepayment-model-projection-table td:nth-child(1) {
        width: 20%;
    }

    .section-container .flat-table table,
    .section-container .flat-table table th,
    .section-container .flat-table table td {
        padding: 10px;
        border: 1px solid rgba(0, 0, 0, 0.25);
        border-collapse: collapse;
        text-align: center;
    }

    /* Indic Layoyut*/
    .section-container .indic-bond-description {
        min-height: 436px;
    }
    .section-container .indic-bond-row {
        min-height: 190px;
    }

    .section-container .indic-mort-collatral {
        min-height: 532px;
    }
    .section-container .indic-mort-row {
        min-height: 140px;
    }

          </style>
       </head>
       <body>
          <div class="main-container">

    <div class="root-container">
      <div class="section-container section-column-container">
        <div class="section-group key-value-table indic-mort-collatral">
          <div class="header">COLLATERAL</div>
          <table>
            <tbody>
              <tr>
                <td>Ticker</td>
                <td>GNMA</td>
              </tr>
              <tr>
                <td>Original Term</td>
                <td>360</td>
              </tr>
              <tr>
                <td>Issue Date</td>
                <td>2013-05-01</td>
              </tr>
              <tr>
                <td>Gross WAC</td>
                <td>4.0000</td>
              </tr>
              <tr>
                <td>Coupon</td>
                <td>3.500000</td>
              </tr>
              <tr>
                <td>Credit Score</td>
                <td>692</td>
              </tr>
              <tr>
                <td>Original LTV</td>
                <td>90.0000</td>
              </tr>
              <tr>
                <td>Current LTV</td>
                <td>27.5000</td>
              </tr>
              <tr>
                <td>Original TPO</td>
                <td></td>
              </tr>
              <tr>
                <td>Current TPO</td>
                <td></td>
              </tr>
              <tr>
                <td>SATO</td>
                <td>22.3000</td>
              </tr>
              <tr>
                <td>Security Type</td>
                <td>MORT</td>
              </tr>
              <tr>
                <td>Security Sub Type</td>
                <td>MPGNMA</td>
              </tr>
              <tr>
                <td>Maturity</td>
                <td>2041-12-01</td>
              </tr>
              <tr>
                <td>WAM</td>
                <td>196</td>
              </tr>
              <tr>
                <td>WALA</td>
                <td>147</td>
              </tr>
              <tr>
                <td>Weighted Avg Loan Size</td>
                <td>101863.0000</td>
              </tr>
              <tr>
                <td>Weighted Average Original Loan Size</td>
                <td></td>
              </tr>
              <tr>
                <td>Current Loan Size</td>
                <td></td>
              </tr>
              <tr>
                <td>Original Loan Size</td>
                <td>182051.000000</td>
              </tr>
              <tr>
                <td>Servicer</td>
                <td></td>
              </tr>
              <tr>
                <td>Delay</td>
                <td>44</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="section-container section-column-container">
        <div class="section-group key-value-table indic-mort-row">
          <div class="header">DISCLOSURE INFORMATION</div>
          <table>
            <tbody>
              <tr>
                <td>Credit Score</td>
                <td>MORT</td>
              </tr>
              <tr>
                <td>LTV</td>
                <td>692</td>
              </tr>
              <tr>
                <td>Load Size</td>
                <td></td>
              </tr>
              <tr>
                <td>% Refinance</td>
                <td></td>
              </tr>
              <tr>
                <td>% Refinance</td>
                <td>0.0000</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="section-group key-value-table indic-mort-row">
          <div class="header">Ratings</div>
          <table>
            <tbody>

              <tr>
                <td>Moody's</td>
                <td>Aaa</td>
              </tr>


            </tbody>
          </table>
        </div>
        <div class="section-group key-value-table indic-mort-row">
          <div class="header">Sector</div>
          <table>
            <tbody>
              <tr>
                <td>GLIC Code</td>
                <td>MBS</td>
              </tr>
              <tr>
                <td>COBS Code</td>
                <td>MTGE</td>
              </tr>
              <tr>
                <td>Market Type</td>
                <td>DOMC</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="section-container section-column-container">
        <div class="section-group partial-table indic-mort-collatral">
          <div class="header">PREPAY HISTORY</div>

          <h4>PSA</h4>
          <table>
            <tbody>
              <thead>
                <tr>
                  <th>Month</th>
                  <th>Value</th>
                </tr>
              </thead>

              <tr>
                <td>1</td>
                <td>104.2558</td>
              </tr>

              <tr>
                <td>3</td>
                <td>101.9675</td>
              </tr>

              <tr>
                <td>6</td>
                <td>101.3512</td>
              </tr>

              <tr>
                <td>12</td>
                <td>101.4048</td>
              </tr>

              <tr>
                <td>24</td>
                <td>0.0000</td>
              </tr>

            </tbody>
          </table>

          <h4>CPR</h4>
          <table>
            <tbody>
              <thead>
                <tr>
                  <th>Month</th>
                  <th>Value</th>
                </tr>
              </thead>

              <tr>
                <td>1</td>
                <td>6.2554</td>
              </tr>

              <tr>
                <td>3</td>
                <td>6.1180</td>
              </tr>

              <tr>
                <td>6</td>
                <td>6.0811</td>
              </tr>

              <tr>
                <td>12</td>
                <td>6.0843</td>
              </tr>

              <tr>
                <td>24</td>
                <td>0.0000</td>
              </tr>

            </tbody>
          </table>

        </div>
      </div>
    </div>

          </div>
          <div style="page-break-before: always;">
             <div class="main-container">
                <div class="section-container">
                   <details>
                      <summary>Show json</summary>
                      <div class="json-group">
                         <pre>{
      &quot;data&quot; : {
        &quot;cusip&quot; : &quot;999818YT8&quot;,
        &quot;indic&quot; : {
          &quot;ltv&quot; : 90.0000,
          &quot;wam&quot; : 196,
          &quot;figi&quot; : &quot;BBG0033WXBV4&quot;,
          &quot;cusip&quot; : &quot;999818YT8&quot;,
          &quot;moody&quot; : [ {
            &quot;value&quot; : &quot;Aaa&quot;
          } ],
          &quot;source&quot; : &quot;CITI&quot;,
          &quot;ticker&quot; : &quot;GNMA&quot;,
          &quot;country&quot; : &quot;US&quot;,
          &quot;loanAge&quot; : 147,
          &quot;lockout&quot; : 0,
          &quot;putFlag&quot; : false,
          &quot;callFlag&quot; : false,
          &quot;cobsCode&quot; : &quot;MTGE&quot;,
          &quot;country2&quot; : &quot;US&quot;,
          &quot;country3&quot; : &quot;USA&quot;,
          &quot;currency&quot; : &quot;USD&quot;,
          &quot;dayCount&quot; : &quot;30/360 eom&quot;,
          &quot;glicCode&quot; : &quot;MBS&quot;,
          &quot;grossWAC&quot; : 4.0000,
          &quot;ioPeriod&quot; : 0,
          &quot;poolCode&quot; : &quot;NA&quot;,
          &quot;sinkFlag&quot; : false,
          &quot;cmaTicker&quot; : &quot;N/A&quot;,
          &quot;datedDate&quot; : &quot;2013-05-01&quot;,
          &quot;gnma2Flag&quot; : false,
          &quot;percentVA&quot; : 11.040,
          &quot;currentLTV&quot; : 27.5000,
          &quot;extendFlag&quot; : &quot;N&quot;,
          &quot;isoCountry&quot; : &quot;US&quot;,
          &quot;marketType&quot; : &quot;DOMC&quot;,
          &quot;percentDTI&quot; : 34.000000,
          &quot;percentFHA&quot; : 80.910,
          &quot;percentInv&quot; : 0.0000,
          &quot;percentPIH&quot; : 0.140,
          &quot;percentRHS&quot; : 7.900,
          &quot;securityID&quot; : &quot;999818YT&quot;,
          &quot;serviceFee&quot; : 0.5000,
          &quot;vPointType&quot; : &quot;MPGNMA&quot;,
          &quot;adjustedLTV&quot; : 27.5000,
          &quot;combinedLTV&quot; : 90.700000,
          &quot;creditScore&quot; : 692,
          &quot;description&quot; : &quot;30-YR GNMA-2013 PROD&quot;,
          &quot;esgBondFlag&quot; : false,
          &quot;indexRating&quot; : &quot;AA+&quot;,
          &quot;issueAmount&quot; : 8597.24000000,
          &quot;lowerRating&quot; : &quot;AA+&quot;,
          &quot;paymentFreq&quot; : 12,
          &quot;percentHARP&quot; : 0.000,
          &quot;percentRefi&quot; : 63.7000,
          &quot;tierCapital&quot; : &quot;NA&quot;,
          &quot;balloonMonth&quot; : 0,
          &quot;deliveryFlag&quot; : &quot;N&quot;,
          &quot;indexCountry&quot; : &quot;US&quot;,
          &quot;industryCode&quot; : &quot;MT&quot;,
          &quot;issuerTicker&quot; : &quot;GNMA&quot;,
          &quot;lowestRating&quot; : &quot;AA+&quot;,
          &quot;maturityDate&quot; : &quot;2041-12-01&quot;,
          &quot;middleRating&quot; : &quot;AA+&quot;,
          &quot;modifiedDate&quot; : &quot;2025-08-13&quot;,
          &quot;originalTerm&quot; : 360,
          &quot;parentTicker&quot; : &quot;GNMA&quot;,
          &quot;percentHARP2&quot; : 0.000,
          &quot;percentJumbo&quot; : 0.000,
          &quot;securityType&quot; : &quot;MORT&quot;,
          &quot;currentCoupon&quot; : 3.500000,
          &quot;dataStateList&quot; : [ {
            &quot;state&quot; : &quot;PR&quot;,
            &quot;percent&quot; : 17.1300
          }, {
            &quot;state&quot; : &quot;TX&quot;,
            &quot;percent&quot; : 10.0300
          }, {
            &quot;state&quot; : &quot;FL&quot;,
            &quot;percent&quot; : 5.6600
          }, {
            &quot;state&quot; : &quot;CA&quot;,
            &quot;percent&quot; : 4.9500
          }, {
            &quot;state&quot; : &quot;OH&quot;,
            &quot;percent&quot; : 4.7700
          }, {
            &quot;state&quot; : &quot;NY&quot;,
            &quot;percent&quot; : 4.7600
          }, {
            &quot;state&quot; : &quot;GA&quot;,
            &quot;percent&quot; : 4.4100
          }, {
            &quot;state&quot; : &quot;PA&quot;,
            &quot;percent&quot; : 3.3800
          }, {
            &quot;state&quot; : &quot;MI&quot;,
            &quot;percent&quot; : 3.0800
          }, {
            &quot;state&quot; : &quot;NC&quot;,
            &quot;percent&quot; : 2.7300
          }, {
            &quot;state&quot; : &quot;IL&quot;,
            &quot;percent&quot; : 2.6800
          }, {
            &quot;state&quot; : &quot;VA&quot;,
            &quot;percent&quot; : 2.6800
          }, {
            &quot;state&quot; : &quot;NJ&quot;,
            &quot;percent&quot; : 2.4000
          }, {
            &quot;state&quot; : &quot;IN&quot;,
            &quot;percent&quot; : 2.3700
          }, {
            &quot;state&quot; : &quot;MD&quot;,
            &quot;percent&quot; : 2.2300
          }, {
            &quot;state&quot; : &quot;MO&quot;,
            &quot;percent&quot; : 2.1100
          }, {
            &quot;state&quot; : &quot;AZ&quot;,
            &quot;percent&quot; : 1.7200
          }, {
            &quot;state&quot; : &quot;TN&quot;,
            &quot;percent&quot; : 1.6600
          }, {
            &quot;state&quot; : &quot;WA&quot;,
            &quot;percent&quot; : 1.4900
          }, {
            &quot;state&quot; : &quot;AL&quot;,
            &quot;percent&quot; : 1.4800
          }, {
            &quot;state&quot; : &quot;OK&quot;,
            &quot;percent&quot; : 1.2300
          }, {
            &quot;state&quot; : &quot;LA&quot;,
            &quot;percent&quot; : 1.2200
          }, {
            &quot;state&quot; : &quot;MN&quot;,
            &quot;percent&quot; : 1.1800
          }, {
            &quot;state&quot; : &quot;SC&quot;,
            &quot;percent&quot; : 1.1100
          }, {
            &quot;state&quot; : &quot;CT&quot;,
            &quot;percent&quot; : 1.0800
          }, {
            &quot;state&quot; : &quot;CO&quot;,
            &quot;percent&quot; : 1.0400
          }, {
            &quot;state&quot; : &quot;KY&quot;,
            &quot;percent&quot; : 1.0400
          }, {
            &quot;state&quot; : &quot;WI&quot;,
            &quot;percent&quot; : 1.0000
          }, {
            &quot;state&quot; : &quot;MS&quot;,
            &quot;percent&quot; : 0.9600
          }, {
            &quot;state&quot; : &quot;NM&quot;,
            &quot;percent&quot; : 0.9500
          }, {
            &quot;state&quot; : &quot;OR&quot;,
            &quot;percent&quot; : 0.8900
          }, {
            &quot;state&quot; : &quot;AR&quot;,
            &quot;percent&quot; : 0.7500
          }, {
            &quot;state&quot; : &quot;NV&quot;,
            &quot;percent&quot; : 0.7000
          }, {
            &quot;state&quot; : &quot;MA&quot;,
            &quot;percent&quot; : 0.6700
          }, {
            &quot;state&quot; : &quot;IA&quot;,
            &quot;percent&quot; : 0.6100
          }, {
            &quot;state&quot; : &quot;UT&quot;,
            &quot;percent&quot; : 0.5900
          }, {
            &quot;state&quot; : &quot;KS&quot;,
            &quot;percent&quot; : 0.5800
          }, {
            &quot;state&quot; : &quot;DE&quot;,
            &quot;percent&quot; : 0.4500
          }, {
            &quot;state&quot; : &quot;ID&quot;,
            &quot;percent&quot; : 0.4000
          }, {
            &quot;state&quot; : &quot;NE&quot;,
            &quot;percent&quot; : 0.3800
          }, {
            &quot;state&quot; : &quot;WV&quot;,
            &quot;percent&quot; : 0.2700
          }, {
            &quot;state&quot; : &quot;ME&quot;,
            &quot;percent&quot; : 0.1900
          }, {
            &quot;state&quot; : &quot;NH&quot;,
            &quot;percent&quot; : 0.1600
          }, {
            &quot;state&quot; : &quot;HI&quot;,
            &quot;percent&quot; : 0.1500
          }, {
            &quot;state&quot; : &quot;MT&quot;,
            &quot;percent&quot; : 0.1300
          }, {
            &quot;state&quot; : &quot;AK&quot;,
            &quot;percent&quot; : 0.1200
          }, {
            &quot;state&quot; : &quot;RI&quot;,
            &quot;percent&quot; : 0.1200
          }, {
            &quot;state&quot; : &quot;WY&quot;,
            &quot;percent&quot; : 0.0800
          }, {
            &quot;state&quot; : &quot;SD&quot;,
            &quot;percent&quot; : 0.0700
          }, {
            &quot;state&quot; : &quot;VT&quot;,
            &quot;percent&quot; : 0.0600
          }, {
            &quot;state&quot; : &quot;DC&quot;,
            &quot;percent&quot; : 0.0400
          }, {
            &quot;state&quot; : &quot;ND&quot;,
            &quot;percent&quot; : 0.0400
          } ],
          &quot;delinquencies&quot; : {
            &quot;del30Days&quot; : {
              &quot;percent&quot; : 3.1400
            },
            &quot;del60Days&quot; : {
              &quot;percent&quot; : 0.5700
            },
            &quot;del90Days&quot; : {
              &quot;percent&quot; : 0.2100
            },
            &quot;del90PlusDays&quot; : {
              &quot;percent&quot; : 0.5900
            },
            &quot;del120PlusDays&quot; : {
              &quot;percent&quot; : 0.3800
            }
          },
          &quot;greenBondFlag&quot; : false,
          &quot;highestRating&quot; : &quot;AAA&quot;,
          &quot;incomeCountry&quot; : &quot;US&quot;,
          &quot;issuerCountry&quot; : &quot;US&quot;,
          &quot;percentSecond&quot; : 0.000,
          &quot;poolAgeMethod&quot; : &quot;Calculated&quot;,
          &quot;prepayEffDate&quot; : &quot;2025-05-01&quot;,
          &quot;seniorityType&quot; : &quot;NA&quot;,
          &quot;assetClassCode&quot; : &quot;CO&quot;,
          &quot;cgmiSectorCode&quot; : &quot;MTGE&quot;,
          &quot;cleanPayMonths&quot; : 0,
          &quot;collateralType&quot; : &quot;GNMA&quot;,
          &quot;fullPledgeFlag&quot; : false,
          &quot;gpmPercentStep&quot; : 0.0000,
          &quot;incomeCountry3&quot; : &quot;USA&quot;,
          &quot;instrumentType&quot; : &quot;NA&quot;,
          &quot;issuerCountry2&quot; : &quot;US&quot;,
          &quot;issuerCountry3&quot; : &quot;USA&quot;,
          &quot;lowestRatingNF&quot; : &quot;AA+&quot;,
          &quot;poolIssuerName&quot; : &quot;NA&quot;,
          &quot;vPointCategory&quot; : &quot;RP&quot;,
          &quot;amortizedFHALTV&quot; : 63.0000,
          &quot;bloombergTicker&quot; : &quot;GNSF 3.5 2013&quot;,
          &quot;industrySubCode&quot; : &quot;MT&quot;,
          &quot;originationDate&quot; : &quot;2013-05-01&quot;,
          &quot;originationYear&quot; : 2013,
          &quot;percent2To4Unit&quot; : 2.7000,
          &quot;percentHAMPMods&quot; : 0.900000,
          &quot;percentPurchase&quot; : 31.8000,
          &quot;percentStateHFA&quot; : 0.400000,
          &quot;poolOriginalWAM&quot; : 0,
          &quot;preliminaryFlag&quot; : false,
          &quot;redemptionValue&quot; : 100.0000,
          &quot;securitySubType&quot; : &quot;MPGNMA&quot;,
          &quot;dataQuartileList&quot; : [ {
            &quot;ltvlow&quot; : 17.000,
            &quot;ltvhigh&quot; : 87.000,
            &quot;loanSizeLow&quot; : 22000.000,
            &quot;loanSizeHigh&quot; : 101000.000,
            &quot;percentDTILow&quot; : 10.000,
            &quot;creditScoreLow&quot; : 300.000,
            &quot;percentDTIHigh&quot; : 24.500,
            &quot;creditScoreHigh&quot; : 655.000,
            &quot;originalLoanAgeLow&quot; : 0,
            &quot;originationYearLow&quot; : 20101101,
            &quot;originalLoanAgeHigh&quot; : 0,
            &quot;originationYearHigh&quot; : 20130401
          }, {
            &quot;ltvlow&quot; : 87.000,
            &quot;ltvhigh&quot; : 93.000,
            &quot;loanSizeLow&quot; : 101000.000,
            &quot;loanSizeHigh&quot; : 132000.000,
            &quot;percentDTILow&quot; : 24.500,
            &quot;creditScoreLow&quot; : 655.000,
            &quot;percentDTIHigh&quot; : 34.700,
            &quot;creditScoreHigh&quot; : 691.000,
            &quot;originalLoanAgeLow&quot; : 0,
            &quot;originationYearLow&quot; : 20130401,
            &quot;originalLoanAgeHigh&quot; : 0,
            &quot;originationYearHigh&quot; : 20130501
          }, {
            &quot;ltvlow&quot; : 93.000,
            &quot;ltvhigh&quot; : 97.000,
            &quot;loanSizeLow&quot; : 132000.000,
            &quot;loanSizeHigh&quot; : 183000.000,
            &quot;percentDTILow&quot; : 34.700,
            &quot;creditScoreLow&quot; : 691.000,
            &quot;percentDTIHigh&quot; : 43.600,
            &quot;creditScoreHigh&quot; : 739.000,
            &quot;originalLoanAgeLow&quot; : 0,
            &quot;originationYearLow&quot; : 20130501,
            &quot;originalLoanAgeHigh&quot; : 1,
            &quot;originationYearHigh&quot; : 20130701
          }, {
            &quot;ltvlow&quot; : 97.000,
            &quot;ltvhigh&quot; : 118.000,
            &quot;loanSizeLow&quot; : 183000.000,
            &quot;loanSizeHigh&quot; : 743000.000,
            &quot;percentDTILow&quot; : 43.600,
            &quot;creditScoreLow&quot; : 739.000,
            &quot;percentDTIHigh&quot; : 65.000,
            &quot;creditScoreHigh&quot; : 832.000,
            &quot;originalLoanAgeLow&quot; : 1,
            &quot;originationYearLow&quot; : 20130701,
            &quot;originalLoanAgeHigh&quot; : 43,
            &quot;originationYearHigh&quot; : 20141101
          } ],
          &quot;gpmNumberOfSteps&quot; : 0,
          &quot;percentHARPOwner&quot; : 0.000,
          &quot;percentPrincipal&quot; : 100.0000,
          &quot;securityCalcType&quot; : &quot;GNMA&quot;,
          &quot;assetClassSubCode&quot; : &quot;MBS&quot;,
          &quot;forbearanceAmount&quot; : 0.000000,
          &quot;modifiedTimeStamp&quot; : &quot;2025-08-13T19:37:00Z&quot;,
          &quot;outstandingAmount&quot; : 1079.93000000,
          &quot;parentDescription&quot; : &quot;NA&quot;,
          &quot;poolIsBalloonFlag&quot; : false,
          &quot;prepaymentOptions&quot; : {
            &quot;prepayType&quot; : [ &quot;CPR&quot;, &quot;PSA&quot;, &quot;VEC&quot; ]
          },
          &quot;reperformerMonths&quot; : 1,
          &quot;dataPPMHistoryList&quot; : [ {
            &quot;prepayType&quot; : &quot;PSA&quot;,
            &quot;dataPPMHistoryDetailList&quot; : [ {
              &quot;month&quot; : &quot;1&quot;,
              &quot;prepayRate&quot; : 104.2558
            }, {
              &quot;month&quot; : &quot;3&quot;,
              &quot;prepayRate&quot; : 101.9675
            }, {
              &quot;month&quot; : &quot;6&quot;,
              &quot;prepayRate&quot; : 101.3512
            }, {
              &quot;month&quot; : &quot;12&quot;,
              &quot;prepayRate&quot; : 101.4048
            }, {
              &quot;month&quot; : &quot;24&quot;,
              &quot;prepayRate&quot; : 0.0000
            } ]
          }, {
            &quot;prepayType&quot; : &quot;CPR&quot;,
            &quot;dataPPMHistoryDetailList&quot; : [ {
              &quot;month&quot; : &quot;1&quot;,
              &quot;prepayRate&quot; : 6.2554
            }, {
              &quot;month&quot; : &quot;3&quot;,
              &quot;prepayRate&quot; : 6.1180
            }, {
              &quot;month&quot; : &quot;6&quot;,
              &quot;prepayRate&quot; : 6.0811
            }, {
              &quot;month&quot; : &quot;12&quot;,
              &quot;prepayRate&quot; : 6.0843
            }, {
              &quot;month&quot; : &quot;24&quot;,
              &quot;prepayRate&quot; : 0.0000
            } ]
          } ],
          &quot;daysToFirstPayment&quot; : 44,
          &quot;issuerLowestRating&quot; : &quot;NA&quot;,
          &quot;issuerMiddleRating&quot; : &quot;NA&quot;,
          &quot;newCurrentLoanSize&quot; : 101863.000,
          &quot;originationChannel&quot; : {
            &quot;broker&quot; : 4.650,
            &quot;retail&quot; : 61.970,
            &quot;unknown&quot; : 0.000,
            &quot;unspecified&quot; : 0.000,
            &quot;correspondence&quot; : 33.370
          },
          &quot;percentMultiFamily&quot; : 2.700000,
          &quot;percentRefiCashout&quot; : 5.8000,
          &quot;percentRegularMods&quot; : 3.600000,
          &quot;percentReperformer&quot; : 0.500000,
          &quot;relocationLoanFlag&quot; : false,
          &quot;socialDensityScore&quot; : 0.000,
          &quot;umbsfhlgPercentage&quot; : 0.00,
          &quot;umbsfnmaPercentage&quot; : 0.00,
          &quot;industryDescription&quot; : &quot;Mortgage&quot;,
          &quot;issuerHighestRating&quot; : &quot;NA&quot;,
          &quot;newOriginalLoanSize&quot; : 182051.000,
          &quot;socialCriteriaShare&quot; : 0.000,
          &quot;spreadAtOrigination&quot; : 22.3000,
          &quot;weightedAvgLoanSize&quot; : 101863.0000,
          &quot;poolOriginalLoanSize&quot; : 182051.000000,
          &quot;cgmiSectorDescription&quot; : &quot;Mortgage&quot;,
          &quot;cleanPayAverageMonths&quot; : 0,
          &quot;expModelAvailableFlag&quot; : true,
          &quot;fhfaImpliedCurrentLTV&quot; : 27.5000,
          &quot;percentRefiNonCashout&quot; : 57.9000,
          &quot;prepayPenaltySchedule&quot; : &quot;0.000&quot;,
          &quot;defaultHorizonPYMethod&quot; : &quot;OAS Change&quot;,
          &quot;industrySubDescription&quot; : &quot;Mortgage Asset Backed&quot;,
          &quot;actualPrepayHistoryList&quot; : {
            &quot;date&quot; : &quot;2025-10-01&quot;,
            &quot;genericValue&quot; : 0.957500
          },
          &quot;adjustedCurrentLoanSize&quot; : 101863.00,
          &quot;forbearanceModification&quot; : 0.000000,
          &quot;percentTwoPlusBorrowers&quot; : 44.000,
          &quot;poolAvgOriginalLoanTerm&quot; : 0,
          &quot;adjustedOriginalLoanSize&quot; : 182040.00,
          &quot;assetClassSubDescription&quot; : &quot;Collateralized Asset Backed - Mortgage&quot;,
          &quot;mortgageInsurancePremium&quot; : {
            &quot;annual&quot; : {
              &quot;va&quot; : 0.000,
              &quot;fha&quot; : 0.797,
              &quot;pih&quot; : 0.000,
              &quot;rhs&quot; : 0.399
            },
            &quot;upfront&quot; : {
              &quot;va&quot; : 0.500,
              &quot;fha&quot; : 0.693,
              &quot;pih&quot; : 1.000,
              &quot;rhs&quot; : 1.996
            }
          },
          &quot;percentReperformerAndMod&quot; : 0.100,
          &quot;reperformerMonthsForMods&quot; : 2,
          &quot;originalLoanSizeRemaining&quot; : 150891.000,
          &quot;percentFirstTimeHomeBuyer&quot; : 20.800000,
          &quot;current3rdPartyOrigination&quot; : 38.020,
          &quot;adjustedSpreadAtOrigination&quot; : 22.3000,
          &quot;dataPrepayModelServicerList&quot; : [ {
            &quot;percent&quot; : 23.8400,
            &quot;servicer&quot; : &quot;FREE&quot;
          }, {
            &quot;percent&quot; : 11.4000,
            &quot;servicer&quot; : &quot;NSTAR&quot;
          }, {
            &quot;percent&quot; : 11.3900,
            &quot;servicer&quot; : &quot;WELLS&quot;
          }, {
            &quot;percent&quot; : 11.1500,
            &quot;servicer&quot; : &quot;BCPOP&quot;
          }, {
            &quot;percent&quot; : 7.2300,
            &quot;servicer&quot; : &quot;QUICK&quot;
          }, {
            &quot;percent&quot; : 7.1300,
            &quot;servicer&quot; : &quot;PENNY&quot;
          }, {
            &quot;percent&quot; : 6.5100,
            &quot;servicer&quot; : &quot;LAKEV&quot;
          }, {
            &quot;percent&quot; : 6.3400,
            &quot;servicer&quot; : &quot;CARRG&quot;
          }, {
            &quot;percent&quot; : 5.5000,
            &quot;servicer&quot; : &quot;USB&quot;
          }, {
            &quot;percent&quot; : 2.4100,
            &quot;servicer&quot; : &quot;PNC&quot;
          }, {
            &quot;percent&quot; : 1.3400,
            &quot;servicer&quot; : &quot;MNTBK&quot;
          }, {
            &quot;percent&quot; : 1.1700,
            &quot;servicer&quot; : &quot;NWRES&quot;
          }, {
            &quot;percent&quot; : 0.9500,
            &quot;servicer&quot; : &quot;FIFTH&quot;
          }, {
            &quot;percent&quot; : 0.7500,
            &quot;servicer&quot; : &quot;DEPOT&quot;
          }, {
            &quot;percent&quot; : 0.6000,
            &quot;servicer&quot; : &quot;BOKF&quot;
          }, {
            &quot;percent&quot; : 0.5100,
            &quot;servicer&quot; : &quot;JPM&quot;
          }, {
            &quot;percent&quot; : 0.4800,
            &quot;servicer&quot; : &quot;TRUIS&quot;
          }, {
            &quot;percent&quot; : 0.4200,
            &quot;servicer&quot; : &quot;CITI&quot;
          }, {
            &quot;percent&quot; : 0.3800,
            &quot;servicer&quot; : &quot;GUILD&quot;
          }, {
            &quot;percent&quot; : 0.2100,
            &quot;servicer&quot; : &quot;REGNS&quot;
          }, {
            &quot;percent&quot; : 0.2000,
            &quot;servicer&quot; : &quot;CNTRL&quot;
          }, {
            &quot;percent&quot; : 0.0900,
            &quot;servicer&quot; : &quot;COLNL&quot;
          }, {
            &quot;percent&quot; : 0.0600,
            &quot;servicer&quot; : &quot;HFAGY&quot;
          }, {
            &quot;percent&quot; : 0.0600,
            &quot;servicer&quot; : &quot;MNSRC&quot;
          }, {
            &quot;percent&quot; : 0.0300,
            &quot;servicer&quot; : &quot;HOMBR&quot;
          } ],
          &quot;nonWeightedOriginalLoanSize&quot; : 0.000,
          &quot;original3rdPartyOrigination&quot; : 0.000,
          &quot;percentHARPDec2010Extension&quot; : 0.000,
          &quot;percentHARPOneYearExtension&quot; : 0.000,
          &quot;percentDownPaymentAssistance&quot; : 5.600,
          &quot;percentAmortizedFHALTVUnder78&quot; : 95.40,
          &quot;loanPerformanceImpliedCurrentLTV&quot; : 44.8000,
          &quot;reperformerMonthsForReperformers&quot; : 28
        },
        &quot;ticker&quot; : &quot;GNMA&quot;,
        &quot;country&quot; : &quot;US&quot;,
        &quot;currency&quot; : &quot;USD&quot;,
        &quot;identifier&quot; : &quot;999818YT&quot;,
        &quot;description&quot; : &quot;30-YR GNMA-2013 PROD&quot;,
        &quot;issuerTicker&quot; : &quot;GNMA&quot;,
        &quot;maturityDate&quot; : &quot;2041-12-01&quot;,
        &quot;securityType&quot; : &quot;MORT&quot;,
        &quot;currentCoupon&quot; : 3.500000,
        &quot;securitySubType&quot; : &quot;MPGNMA&quot;
      },
      &quot;meta&quot; : {
        &quot;status&quot; : &quot;DONE&quot;,
        &quot;requestId&quot; : &quot;R-20901&quot;,
        &quot;timeStamp&quot; : &quot;2025-08-18T22:33:24Z&quot;,
        &quot;responseType&quot; : &quot;BOND_INDIC&quot;
      }
    }</pre>
                      </div>
                   </details>
                </div>
             </div>
          </div>
       </body>
    </html>

    """

    try:
        logger.info("Calling get_formatted_result")

        response = Client().yield_book_rest.get_formatted_result(
            request_id_parameter=request_id_parameter, format=format, job=job
        )

        output = response
        logger.info("Called get_formatted_result")

        return output
    except Exception as err:
        logger.error("Error get_formatted_result.")
        check_exception_and_raise(err, logger)


def get_job(*, job_ref: str) -> JobResponse:
    """
    Get job details

    Parameters
    ----------
    job_ref : str
        Job reference. This can be of the form J-number or job name.

    Returns
    --------
    JobResponse


    Examples
    --------
    >>> # get job
    >>> response = get_job(job_ref='myJob')
    >>>
    >>> print(js.dumps(response.as_dict(), indent=4))
    {
        "id": "J-8157",
        "sequence": 0,
        "asOf": "2025-03-10",
        "closed": true,
        "onHold": true,
        "aborted": true,
        "exitStatus": "NEVER_STARTED",
        "actualHold": true,
        "name": "myJob",
        "chain": "string",
        "description": "string",
        "priority": 0,
        "order": "FAST",
        "requestCount": 0,
        "pendingCount": 0,
        "runningCount": 0,
        "okCount": 0,
        "errorCount": 0,
        "abortedCount": 0,
        "skipCount": 0,
        "startAfter": "2025-03-03T10:10:15Z",
        "stopAfter": "2025-03-10T20:10:15Z",
        "createdAt": "2025-09-18T08:57:19.153Z",
        "updatedAt": "2025-09-18T08:57:19.171Z"
    }

    """

    try:
        logger.info("Calling get_job")

        response = Client().yield_book_rest.get_job(job_ref=job_ref)

        output = response
        logger.info("Called get_job")

        return output
    except Exception as err:
        logger.error("Error get_job.")
        check_exception_and_raise(err, logger)


def get_job_data(*, job: str, store_type: Union[str, StoreType], request_name: str) -> Any:
    """
    Retrieve job data body using request id or request name.

    Parameters
    ----------
    job : str
        Job reference. This can be of the form J-number or job name.
    store_type : Union[str, StoreType]
        Job store object type. Should be one of the enumerated types.
    request_name : str
        Unique request id. This can be of the format R-number or request name. If request name is used, corresponding job information should be passed in the query parameter.

    Returns
    --------
    Any


    Examples
    --------


    """

    try:
        logger.info("Calling get_job_data")

        response = Client().yield_book_rest.get_job_data(job=job, store_type=store_type, request_name=request_name)

        output = response
        logger.info("Called get_job_data")

        return output
    except Exception as err:
        logger.error("Error get_job_data.")
        check_exception_and_raise(err, logger)


def get_job_object_meta(*, job: str, store_type: Union[str, StoreType], request_id_parameter: str) -> Dict[str, Any]:
    """
    Retrieve job object metadata using request id or request name.

    Parameters
    ----------
    job : str
        Job reference. This can be of the form J-number or job name.
    store_type : Union[str, StoreType]
        Job store object type. Should be one of the enumerated types.
    request_id_parameter : str
        Unique request id. This can be of the format R-number or request name. If request name is used, corresponding job information should be passed in the query parameter.

    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling get_job_object_meta")

        response = Client().yield_book_rest.get_job_object_meta(
            job=job, store_type=store_type, request_id_parameter=request_id_parameter
        )

        output = response
        logger.info("Called get_job_object_meta")

        return output
    except Exception as err:
        logger.error("Error get_job_object_meta.")
        check_exception_and_raise(err, logger)


def get_job_status(*, job_ref: str) -> JobStatusResponse:
    """
    Get job status

    Parameters
    ----------
    job_ref : str
        Job reference. This can be of the form J-number or job name.

    Returns
    --------
    JobStatusResponse


    Examples
    --------
    >>> # create temp job
    >>> job_response = create_job(
    >>>     name="status_Job"
    >>> )
    >>>
    >>> # get job status
    >>> response = get_job_status(job_ref="status_Job")
    >>>
    >>> print(js.dumps(response.as_dict(), indent=4))
    {
        "id": "J-8158",
        "name": "status_Job",
        "jobStatus": "EMPTY",
        "requestCount": 0,
        "pendingCount": 0,
        "runningCount": 0,
        "okCount": 0,
        "errorCount": 0,
        "abortedCount": 0,
        "skippedCount": 0
    }

    """

    try:
        logger.info("Calling get_job_status")

        response = Client().yield_book_rest.get_job_status(job_ref=job_ref)

        output = response
        logger.info("Called get_job_status")

        return output
    except Exception as err:
        logger.error("Error get_job_status.")
        check_exception_and_raise(err, logger)


def get_json_result(
    *, ids: List[str], job: Optional[str] = None, fields: Optional[List[str]] = None, format: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve json result using request id or request name.

    Parameters
    ----------
    ids : List[str]
          Ids can be provided comma separated. Different formats for id are:
          1) RequestId R-number
          2) Request name R:name. In this case also provide jobid (J-number) or jobname (J:name)
          3) Jobid J-number
          4) Job name J:name - only 1 active job with the jobname
          5) Tag name T:name. In this case also provide jobid (J-number) or jobname (J:name)
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    fields : List[str], optional

    format : str, optional
        A sequence of textual characters.

    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling get_json_result")

        response = Client().yield_book_rest.get_json_result(ids=ids, job=job, fields=fields, format=format)

        output = response
        logger.info("Called get_json_result")

        return output
    except Exception as err:
        logger.error("Error get_json_result.")
        check_exception_and_raise(err, logger)


def get_result(*, request_id_parameter: str, job: Optional[str] = None) -> Dict[str, Any]:
    """
    Retrieve single result using request id or request name.

    Parameters
    ----------
    request_id_parameter : str
        Unique request id. This can be of the format R-number or request name. If request name is used, corresponding job information should be passed in the query parameter.
    job : str, optional
        Job reference. This can be of the form J-number or job name.

    Returns
    --------
    Dict[str, Any]


    Examples
    --------
    >>> # link a request to the job
    >>> indic_response = request_bond_indic_async_get(id="999818YT",
    >>>                                               id_type=IdTypeEnum.CUSIP
    >>>         )
    >>>
    >>> # provide a window of time for job to finish
    >>> time.sleep(10)
    >>>
    >>> # get result
    >>> response = get_result(request_id_parameter=indic_response['requestId'])
    >>>
    >>> print(js.dumps(response, indent=4))
    {
        "data": {
            "cusip": "999818YT8",
            "indic": {
                "ltv": 90.0,
                "wam": 196,
                "figi": "BBG0033WXBV4",
                "cusip": "999818YT8",
                "moody": [
                    {
                        "value": "Aaa"
                    }
                ],
                "source": "CITI",
                "ticker": "GNMA",
                "country": "US",
                "loanAge": 147,
                "lockout": 0,
                "putFlag": false,
                "callFlag": false,
                "cobsCode": "MTGE",
                "country2": "US",
                "country3": "USA",
                "currency": "USD",
                "dayCount": "30/360 eom",
                "glicCode": "MBS",
                "grossWAC": 4.0,
                "ioPeriod": 0,
                "poolCode": "NA",
                "sinkFlag": false,
                "cmaTicker": "N/A",
                "datedDate": "2013-05-01",
                "gnma2Flag": false,
                "percentVA": 11.04,
                "currentLTV": 27.5,
                "extendFlag": "N",
                "isoCountry": "US",
                "marketType": "DOMC",
                "percentDTI": 34.0,
                "percentFHA": 80.91,
                "percentInv": 0.0,
                "percentPIH": 0.14,
                "percentRHS": 7.9,
                "securityID": "999818YT",
                "serviceFee": 0.5,
                "vPointType": "MPGNMA",
                "adjustedLTV": 27.5,
                "combinedLTV": 90.7,
                "creditScore": 692,
                "description": "30-YR GNMA-2013 PROD",
                "esgBondFlag": false,
                "indexRating": "AA+",
                "issueAmount": 8597.24,
                "lowerRating": "AA+",
                "paymentFreq": 12,
                "percentHARP": 0.0,
                "percentRefi": 63.7,
                "tierCapital": "NA",
                "balloonMonth": 0,
                "deliveryFlag": "N",
                "indexCountry": "US",
                "industryCode": "MT",
                "issuerTicker": "GNMA",
                "lowestRating": "AA+",
                "maturityDate": "2041-12-01",
                "middleRating": "AA+",
                "modifiedDate": "2025-08-13",
                "originalTerm": 360,
                "parentTicker": "GNMA",
                "percentHARP2": 0.0,
                "percentJumbo": 0.0,
                "securityType": "MORT",
                "currentCoupon": 3.5,
                "dataStateList": [
                    {
                        "state": "PR",
                        "percent": 17.13
                    },
                    {
                        "state": "TX",
                        "percent": 10.03
                    },
                    {
                        "state": "FL",
                        "percent": 5.66
                    },
                    {
                        "state": "CA",
                        "percent": 4.95
                    },
                    {
                        "state": "OH",
                        "percent": 4.77
                    },
                    {
                        "state": "NY",
                        "percent": 4.76
                    },
                    {
                        "state": "GA",
                        "percent": 4.41
                    },
                    {
                        "state": "PA",
                        "percent": 3.38
                    },
                    {
                        "state": "MI",
                        "percent": 3.08
                    },
                    {
                        "state": "NC",
                        "percent": 2.73
                    },
                    {
                        "state": "IL",
                        "percent": 2.68
                    },
                    {
                        "state": "VA",
                        "percent": 2.68
                    },
                    {
                        "state": "NJ",
                        "percent": 2.4
                    },
                    {
                        "state": "IN",
                        "percent": 2.37
                    },
                    {
                        "state": "MD",
                        "percent": 2.23
                    },
                    {
                        "state": "MO",
                        "percent": 2.11
                    },
                    {
                        "state": "AZ",
                        "percent": 1.72
                    },
                    {
                        "state": "TN",
                        "percent": 1.66
                    },
                    {
                        "state": "WA",
                        "percent": 1.49
                    },
                    {
                        "state": "AL",
                        "percent": 1.48
                    },
                    {
                        "state": "OK",
                        "percent": 1.23
                    },
                    {
                        "state": "LA",
                        "percent": 1.22
                    },
                    {
                        "state": "MN",
                        "percent": 1.18
                    },
                    {
                        "state": "SC",
                        "percent": 1.11
                    },
                    {
                        "state": "CT",
                        "percent": 1.08
                    },
                    {
                        "state": "CO",
                        "percent": 1.04
                    },
                    {
                        "state": "KY",
                        "percent": 1.04
                    },
                    {
                        "state": "WI",
                        "percent": 1.0
                    },
                    {
                        "state": "MS",
                        "percent": 0.96
                    },
                    {
                        "state": "NM",
                        "percent": 0.95
                    },
                    {
                        "state": "OR",
                        "percent": 0.89
                    },
                    {
                        "state": "AR",
                        "percent": 0.75
                    },
                    {
                        "state": "NV",
                        "percent": 0.7
                    },
                    {
                        "state": "MA",
                        "percent": 0.67
                    },
                    {
                        "state": "IA",
                        "percent": 0.61
                    },
                    {
                        "state": "UT",
                        "percent": 0.59
                    },
                    {
                        "state": "KS",
                        "percent": 0.58
                    },
                    {
                        "state": "DE",
                        "percent": 0.45
                    },
                    {
                        "state": "ID",
                        "percent": 0.4
                    },
                    {
                        "state": "NE",
                        "percent": 0.38
                    },
                    {
                        "state": "WV",
                        "percent": 0.27
                    },
                    {
                        "state": "ME",
                        "percent": 0.19
                    },
                    {
                        "state": "NH",
                        "percent": 0.16
                    },
                    {
                        "state": "HI",
                        "percent": 0.15
                    },
                    {
                        "state": "MT",
                        "percent": 0.13
                    },
                    {
                        "state": "AK",
                        "percent": 0.12
                    },
                    {
                        "state": "RI",
                        "percent": 0.12
                    },
                    {
                        "state": "WY",
                        "percent": 0.08
                    },
                    {
                        "state": "SD",
                        "percent": 0.07
                    },
                    {
                        "state": "VT",
                        "percent": 0.06
                    },
                    {
                        "state": "DC",
                        "percent": 0.04
                    },
                    {
                        "state": "ND",
                        "percent": 0.04
                    }
                ],
                "delinquencies": {
                    "del30Days": {
                        "percent": 3.14
                    },
                    "del60Days": {
                        "percent": 0.57
                    },
                    "del90Days": {
                        "percent": 0.21
                    },
                    "del90PlusDays": {
                        "percent": 0.59
                    },
                    "del120PlusDays": {
                        "percent": 0.38
                    }
                },
                "greenBondFlag": false,
                "highestRating": "AAA",
                "incomeCountry": "US",
                "issuerCountry": "US",
                "percentSecond": 0.0,
                "poolAgeMethod": "Calculated",
                "prepayEffDate": "2025-05-01",
                "seniorityType": "NA",
                "assetClassCode": "CO",
                "cgmiSectorCode": "MTGE",
                "cleanPayMonths": 0,
                "collateralType": "GNMA",
                "fullPledgeFlag": false,
                "gpmPercentStep": 0.0,
                "incomeCountry3": "USA",
                "instrumentType": "NA",
                "issuerCountry2": "US",
                "issuerCountry3": "USA",
                "lowestRatingNF": "AA+",
                "poolIssuerName": "NA",
                "vPointCategory": "RP",
                "amortizedFHALTV": 63.0,
                "bloombergTicker": "GNSF 3.5 2013",
                "industrySubCode": "MT",
                "originationDate": "2013-05-01",
                "originationYear": 2013,
                "percent2To4Unit": 2.7,
                "percentHAMPMods": 0.9,
                "percentPurchase": 31.8,
                "percentStateHFA": 0.4,
                "poolOriginalWAM": 0,
                "preliminaryFlag": false,
                "redemptionValue": 100.0,
                "securitySubType": "MPGNMA",
                "dataQuartileList": [
                    {
                        "ltvlow": 17.0,
                        "ltvhigh": 87.0,
                        "loanSizeLow": 22000.0,
                        "loanSizeHigh": 101000.0,
                        "percentDTILow": 10.0,
                        "creditScoreLow": 300.0,
                        "percentDTIHigh": 24.5,
                        "creditScoreHigh": 655.0,
                        "originalLoanAgeLow": 0,
                        "originationYearLow": 20101101,
                        "originalLoanAgeHigh": 0,
                        "originationYearHigh": 20130401
                    },
                    {
                        "ltvlow": 87.0,
                        "ltvhigh": 93.0,
                        "loanSizeLow": 101000.0,
                        "loanSizeHigh": 132000.0,
                        "percentDTILow": 24.5,
                        "creditScoreLow": 655.0,
                        "percentDTIHigh": 34.7,
                        "creditScoreHigh": 691.0,
                        "originalLoanAgeLow": 0,
                        "originationYearLow": 20130401,
                        "originalLoanAgeHigh": 0,
                        "originationYearHigh": 20130501
                    },
                    {
                        "ltvlow": 93.0,
                        "ltvhigh": 97.0,
                        "loanSizeLow": 132000.0,
                        "loanSizeHigh": 183000.0,
                        "percentDTILow": 34.7,
                        "creditScoreLow": 691.0,
                        "percentDTIHigh": 43.6,
                        "creditScoreHigh": 739.0,
                        "originalLoanAgeLow": 0,
                        "originationYearLow": 20130501,
                        "originalLoanAgeHigh": 1,
                        "originationYearHigh": 20130701
                    },
                    {
                        "ltvlow": 97.0,
                        "ltvhigh": 118.0,
                        "loanSizeLow": 183000.0,
                        "loanSizeHigh": 743000.0,
                        "percentDTILow": 43.6,
                        "creditScoreLow": 739.0,
                        "percentDTIHigh": 65.0,
                        "creditScoreHigh": 832.0,
                        "originalLoanAgeLow": 1,
                        "originationYearLow": 20130701,
                        "originalLoanAgeHigh": 43,
                        "originationYearHigh": 20141101
                    }
                ],
                "gpmNumberOfSteps": 0,
                "percentHARPOwner": 0.0,
                "percentPrincipal": 100.0,
                "securityCalcType": "GNMA",
                "assetClassSubCode": "MBS",
                "forbearanceAmount": 0.0,
                "modifiedTimeStamp": "2025-08-13T19:37:00Z",
                "outstandingAmount": 1079.93,
                "parentDescription": "NA",
                "poolIsBalloonFlag": false,
                "prepaymentOptions": {
                    "prepayType": [
                        "CPR",
                        "PSA",
                        "VEC"
                    ]
                },
                "reperformerMonths": 1,
                "dataPPMHistoryList": [
                    {
                        "prepayType": "PSA",
                        "dataPPMHistoryDetailList": [
                            {
                                "month": "1",
                                "prepayRate": 104.2558
                            },
                            {
                                "month": "3",
                                "prepayRate": 101.9675
                            },
                            {
                                "month": "6",
                                "prepayRate": 101.3512
                            },
                            {
                                "month": "12",
                                "prepayRate": 101.4048
                            },
                            {
                                "month": "24",
                                "prepayRate": 0.0
                            }
                        ]
                    },
                    {
                        "prepayType": "CPR",
                        "dataPPMHistoryDetailList": [
                            {
                                "month": "1",
                                "prepayRate": 6.2554
                            },
                            {
                                "month": "3",
                                "prepayRate": 6.118
                            },
                            {
                                "month": "6",
                                "prepayRate": 6.0811
                            },
                            {
                                "month": "12",
                                "prepayRate": 6.0843
                            },
                            {
                                "month": "24",
                                "prepayRate": 0.0
                            }
                        ]
                    }
                ],
                "daysToFirstPayment": 44,
                "issuerLowestRating": "NA",
                "issuerMiddleRating": "NA",
                "newCurrentLoanSize": 101863.0,
                "originationChannel": {
                    "broker": 4.65,
                    "retail": 61.97,
                    "unknown": 0.0,
                    "unspecified": 0.0,
                    "correspondence": 33.37
                },
                "percentMultiFamily": 2.7,
                "percentRefiCashout": 5.8,
                "percentRegularMods": 3.6,
                "percentReperformer": 0.5,
                "relocationLoanFlag": false,
                "socialDensityScore": 0.0,
                "umbsfhlgPercentage": 0.0,
                "umbsfnmaPercentage": 0.0,
                "industryDescription": "Mortgage",
                "issuerHighestRating": "NA",
                "newOriginalLoanSize": 182051.0,
                "socialCriteriaShare": 0.0,
                "spreadAtOrigination": 22.3,
                "weightedAvgLoanSize": 101863.0,
                "poolOriginalLoanSize": 182051.0,
                "cgmiSectorDescription": "Mortgage",
                "cleanPayAverageMonths": 0,
                "expModelAvailableFlag": true,
                "fhfaImpliedCurrentLTV": 27.5,
                "percentRefiNonCashout": 57.9,
                "prepayPenaltySchedule": "0.000",
                "defaultHorizonPYMethod": "OAS Change",
                "industrySubDescription": "Mortgage Asset Backed",
                "actualPrepayHistoryList": {
                    "date": "2025-10-01",
                    "genericValue": 0.9575
                },
                "adjustedCurrentLoanSize": 101863.0,
                "forbearanceModification": 0.0,
                "percentTwoPlusBorrowers": 44.0,
                "poolAvgOriginalLoanTerm": 0,
                "adjustedOriginalLoanSize": 182040.0,
                "assetClassSubDescription": "Collateralized Asset Backed - Mortgage",
                "mortgageInsurancePremium": {
                    "annual": {
                        "va": 0.0,
                        "fha": 0.797,
                        "pih": 0.0,
                        "rhs": 0.399
                    },
                    "upfront": {
                        "va": 0.5,
                        "fha": 0.693,
                        "pih": 1.0,
                        "rhs": 1.996
                    }
                },
                "percentReperformerAndMod": 0.1,
                "reperformerMonthsForMods": 2,
                "originalLoanSizeRemaining": 150891.0,
                "percentFirstTimeHomeBuyer": 20.8,
                "current3rdPartyOrigination": 38.02,
                "adjustedSpreadAtOrigination": 22.3,
                "dataPrepayModelServicerList": [
                    {
                        "percent": 23.84,
                        "servicer": "FREE"
                    },
                    {
                        "percent": 11.4,
                        "servicer": "NSTAR"
                    },
                    {
                        "percent": 11.39,
                        "servicer": "WELLS"
                    },
                    {
                        "percent": 11.15,
                        "servicer": "BCPOP"
                    },
                    {
                        "percent": 7.23,
                        "servicer": "QUICK"
                    },
                    {
                        "percent": 7.13,
                        "servicer": "PENNY"
                    },
                    {
                        "percent": 6.51,
                        "servicer": "LAKEV"
                    },
                    {
                        "percent": 6.34,
                        "servicer": "CARRG"
                    },
                    {
                        "percent": 5.5,
                        "servicer": "USB"
                    },
                    {
                        "percent": 2.41,
                        "servicer": "PNC"
                    },
                    {
                        "percent": 1.34,
                        "servicer": "MNTBK"
                    },
                    {
                        "percent": 1.17,
                        "servicer": "NWRES"
                    },
                    {
                        "percent": 0.95,
                        "servicer": "FIFTH"
                    },
                    {
                        "percent": 0.75,
                        "servicer": "DEPOT"
                    },
                    {
                        "percent": 0.6,
                        "servicer": "BOKF"
                    },
                    {
                        "percent": 0.51,
                        "servicer": "JPM"
                    },
                    {
                        "percent": 0.48,
                        "servicer": "TRUIS"
                    },
                    {
                        "percent": 0.42,
                        "servicer": "CITI"
                    },
                    {
                        "percent": 0.38,
                        "servicer": "GUILD"
                    },
                    {
                        "percent": 0.21,
                        "servicer": "REGNS"
                    },
                    {
                        "percent": 0.2,
                        "servicer": "CNTRL"
                    },
                    {
                        "percent": 0.09,
                        "servicer": "COLNL"
                    },
                    {
                        "percent": 0.06,
                        "servicer": "HFAGY"
                    },
                    {
                        "percent": 0.06,
                        "servicer": "MNSRC"
                    },
                    {
                        "percent": 0.03,
                        "servicer": "HOMBR"
                    }
                ],
                "nonWeightedOriginalLoanSize": 0.0,
                "original3rdPartyOrigination": 0.0,
                "percentHARPDec2010Extension": 0.0,
                "percentHARPOneYearExtension": 0.0,
                "percentDownPaymentAssistance": 5.6,
                "percentAmortizedFHALTVUnder78": 95.4,
                "loanPerformanceImpliedCurrentLTV": 44.8,
                "reperformerMonthsForReperformers": 28
            },
            "ticker": "GNMA",
            "country": "US",
            "currency": "USD",
            "identifier": "999818YT",
            "description": "30-YR GNMA-2013 PROD",
            "issuerTicker": "GNMA",
            "maturityDate": "2041-12-01",
            "securityType": "MORT",
            "currentCoupon": 3.5,
            "securitySubType": "MPGNMA"
        },
        "meta": {
            "status": "DONE",
            "requestId": "R-20900",
            "timeStamp": "2025-08-18T22:33:09Z",
            "responseType": "BOND_INDIC"
        }
    }

    """

    try:
        logger.info("Calling get_result")

        response = Client().yield_book_rest.get_result(request_id_parameter=request_id_parameter, job=job)

        output = response
        logger.info("Called get_result")

        return output
    except Exception as err:
        logger.error("Error get_result.")
        check_exception_and_raise(err, logger)


def get_tba_pricing_sync(
    *,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Get tba-pricing sync.

    Parameters
    ----------
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling get_tba_pricing_sync")

        response = Client().yield_book_rest.get_tba_pricing_sync(job=job, name=name, pri=pri, tags=tags)

        output = response
        logger.info("Called get_tba_pricing_sync")

        return output
    except Exception as err:
        logger.error("Error get_tba_pricing_sync.")
        check_exception_and_raise(err, logger)


def post_cash_flow_async(
    *,
    global_settings: Optional[CashFlowGlobalSettings] = None,
    input: Optional[List[CashFlowInput]] = None,
    keywords: Optional[List[str]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Post cash flow request async.

    Parameters
    ----------
    global_settings : CashFlowGlobalSettings, optional

    input : List[CashFlowInput], optional

    keywords : List[str], optional
        Optional. Used to specify the keywords a user will retrieve in the response. All keywords are returned by default.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------
    >>> # post_cash_flow_async
    >>> global_settings = CashFlowGlobalSettings(
    >>>         )
    >>>
    >>> input = CashFlowInput(
    >>>             identifier="01F002628",
    >>>             par_amount="10000"
    >>>         )
    >>>
    >>> cf_async_post_response = post_cash_flow_async(
    >>>             global_settings=global_settings,
    >>>             input=[input]
    >>>         )
    >>>
    >>> cf_async_post_result = {}
    >>>
    >>> attempt = 1
    >>>
    >>> while attempt < 10:
    >>>
    >>>     try:
    >>>         time.sleep(10)
    >>>
    >>>         cf_async_post_result = get_result(request_id_parameter=cf_async_post_response.request_id)
    >>>
    >>>         break
    >>>
    >>>     except Exception as error:
    >>>         print(f"Attempt " + str(attempt) + " resulted in error retrieving results from:" + cf_async_post_response.request_id)
    >>>
    >>>         attempt+=1
    >>>
    >>> # Print output to a file, as CF output is too long for terminal printout
    >>> # print(js.dumps(cf_async_post_result, indent=4), file=open('.\\CF_async_post_output.json', 'w+'))
    >>>
    >>> # Print onyl payment information
    >>> for paymentInfo in cf_async_post_result["results"][0]["cashFlow"]["dataPaymentList"]:
    >>>     print(js.dumps(paymentInfo, indent=4))
    {
        "date": "2026-03-25",
        "totalCashFlow": 43240.102925,
        "interestPayment": 4166.666667,
        "principalBalance": 9960926.563741,
        "principalPayment": 39073.436259,
        "endPrincipalBalance": 9960926.563741,
        "beginPrincipalBalance": 10000000.0,
        "prepayPrincipalPayment": 14113.333241,
        "scheduledPrincipalPayment": 24960.103018
    }
    {
        "date": "2026-04-25",
        "totalCashFlow": 46525.285989,
        "interestPayment": 4150.386068,
        "principalBalance": 9918551.66382,
        "principalPayment": 42374.899921,
        "endPrincipalBalance": 9918551.66382,
        "beginPrincipalBalance": 9960926.563741,
        "prepayPrincipalPayment": 17424.148754,
        "scheduledPrincipalPayment": 24950.751166
    }
    {
        "date": "2026-05-25",
        "totalCashFlow": 48712.807936,
        "interestPayment": 4132.72986,
        "principalBalance": 9873971.585744,
        "principalPayment": 44580.078076,
        "endPrincipalBalance": 9873971.585744,
        "beginPrincipalBalance": 9918551.66382,
        "prepayPrincipalPayment": 19647.136818,
        "scheduledPrincipalPayment": 24932.941259
    }
    {
        "date": "2026-06-25",
        "totalCashFlow": 49212.075446,
        "interestPayment": 4114.154827,
        "principalBalance": 9828873.665125,
        "principalPayment": 45097.920619,
        "endPrincipalBalance": 9828873.665125,
        "beginPrincipalBalance": 9873971.585744,
        "prepayPrincipalPayment": 20188.571937,
        "scheduledPrincipalPayment": 24909.348682
    }
    {
        "date": "2026-07-25",
        "totalCashFlow": 51737.961794,
        "interestPayment": 4095.364027,
        "principalBalance": 9781231.067359,
        "principalPayment": 47642.597767,
        "endPrincipalBalance": 9781231.067359,
        "beginPrincipalBalance": 9828873.665125,
        "prepayPrincipalPayment": 22758.414125,
        "scheduledPrincipalPayment": 24884.183641
    }
    {
        "date": "2026-08-25",
        "totalCashFlow": 51667.218557,
        "interestPayment": 4075.512945,
        "principalBalance": 9733639.361746,
        "principalPayment": 47591.705612,
        "endPrincipalBalance": 9733639.361746,
        "beginPrincipalBalance": 9781231.067359,
        "prepayPrincipalPayment": 22739.425823,
        "scheduledPrincipalPayment": 24852.27979
    }
    {
        "date": "2026-09-25",
        "totalCashFlow": 50398.345822,
        "interestPayment": 4055.683067,
        "principalBalance": 9687296.698992,
        "principalPayment": 46342.662754,
        "endPrincipalBalance": 9687296.698992,
        "beginPrincipalBalance": 9733639.361746,
        "prepayPrincipalPayment": 21522.479314,
        "scheduledPrincipalPayment": 24820.18344
    }
    {
        "date": "2026-10-25",
        "totalCashFlow": 49757.462556,
        "interestPayment": 4036.373625,
        "principalBalance": 9641575.61006,
        "principalPayment": 45721.088932,
        "endPrincipalBalance": 9641575.61006,
        "beginPrincipalBalance": 9687296.698992,
        "prepayPrincipalPayment": 20930.129751,
        "scheduledPrincipalPayment": 24790.959181
    }
    {
        "date": "2026-11-25",
        "totalCashFlow": 48882.03192,
        "interestPayment": 4017.323171,
        "principalBalance": 9596710.901311,
        "principalPayment": 44864.708749,
        "endPrincipalBalance": 9596710.901311,
        "beginPrincipalBalance": 9641575.61006,
        "prepayPrincipalPayment": 20101.681738,
        "scheduledPrincipalPayment": 24763.02701
    }
    {
        "date": "2026-12-25",
        "totalCashFlow": 47270.138842,
        "interestPayment": 3998.629542,
        "principalBalance": 9553439.392012,
        "principalPayment": 43271.509299,
        "endPrincipalBalance": 9553439.392012,
        "beginPrincipalBalance": 9596710.901311,
        "prepayPrincipalPayment": 18534.502663,
        "scheduledPrincipalPayment": 24737.006636
    }
    {
        "date": "2027-01-25",
        "totalCashFlow": 48743.633434,
        "interestPayment": 3980.599747,
        "principalBalance": 9508676.358324,
        "principalPayment": 44763.033688,
        "endPrincipalBalance": 9508676.358324,
        "beginPrincipalBalance": 9553439.392012,
        "prepayPrincipalPayment": 20048.208245,
        "scheduledPrincipalPayment": 24714.825442
    }
    {
        "date": "2027-02-25",
        "totalCashFlow": 44132.795776,
        "interestPayment": 3961.948483,
        "principalBalance": 9468505.511031,
        "principalPayment": 40170.847293,
        "endPrincipalBalance": 9468505.511031,
        "beginPrincipalBalance": 9508676.358324,
        "prepayPrincipalPayment": 15482.330807,
        "scheduledPrincipalPayment": 24688.516486
    }
    {
        "date": "2027-03-25",
        "totalCashFlow": 44952.113459,
        "interestPayment": 3945.21063,
        "principalBalance": 9427498.608202,
        "principalPayment": 41006.902829,
        "endPrincipalBalance": 9427498.608202,
        "beginPrincipalBalance": 9468505.511031,
        "prepayPrincipalPayment": 16333.014398,
        "scheduledPrincipalPayment": 24673.888432
    }
    {
        "date": "2027-04-25",
        "totalCashFlow": 48717.535794,
        "interestPayment": 3928.12442,
        "principalBalance": 9382709.196828,
        "principalPayment": 44789.411374,
        "endPrincipalBalance": 9382709.196828,
        "beginPrincipalBalance": 9427498.608202,
        "prepayPrincipalPayment": 20132.538675,
        "scheduledPrincipalPayment": 24656.872699
    }
    {
        "date": "2027-05-25",
        "totalCashFlow": 50259.380717,
        "interestPayment": 3909.462165,
        "principalBalance": 9336359.278276,
        "principalPayment": 46349.918552,
        "endPrincipalBalance": 9336359.278276,
        "beginPrincipalBalance": 9382709.196828,
        "prepayPrincipalPayment": 21720.209733,
        "scheduledPrincipalPayment": 24629.708819
    }
    {
        "date": "2027-06-25",
        "totalCashFlow": 50404.111406,
        "interestPayment": 3890.149699,
        "principalBalance": 9289845.316569,
        "principalPayment": 46513.961707,
        "endPrincipalBalance": 9289845.316569,
        "beginPrincipalBalance": 9336359.278276,
        "prepayPrincipalPayment": 21915.822326,
        "scheduledPrincipalPayment": 24598.139381
    }
    {
        "date": "2027-07-25",
        "totalCashFlow": 52864.921712,
        "interestPayment": 3870.768882,
        "principalBalance": 9240851.163739,
        "principalPayment": 48994.15283,
        "endPrincipalBalance": 9240851.163739,
        "beginPrincipalBalance": 9289845.316569,
        "prepayPrincipalPayment": 24428.343979,
        "scheduledPrincipalPayment": 24565.808851
    }
    {
        "date": "2027-08-25",
        "totalCashFlow": 51614.130553,
        "interestPayment": 3850.354652,
        "principalBalance": 9193087.387838,
        "principalPayment": 47763.775901,
        "endPrincipalBalance": 9193087.387838,
        "beginPrincipalBalance": 9240851.163739,
        "prepayPrincipalPayment": 23237.21404,
        "scheduledPrincipalPayment": 24526.561861
    }
    {
        "date": "2027-09-25",
        "totalCashFlow": 51834.039123,
        "interestPayment": 3830.453078,
        "principalBalance": 9145083.801794,
        "principalPayment": 48003.586044,
        "endPrincipalBalance": 9145083.801794,
        "beginPrincipalBalance": 9193087.387838,
        "prepayPrincipalPayment": 23513.37917,
        "scheduledPrincipalPayment": 24490.206874
    }
    {
        "date": "2027-10-25",
        "totalCashFlow": 50332.989459,
        "interestPayment": 3810.451584,
        "principalBalance": 9098561.263919,
        "principalPayment": 46522.537875,
        "endPrincipalBalance": 9098561.263919,
        "beginPrincipalBalance": 9145083.801794,
        "prepayPrincipalPayment": 22069.692294,
        "scheduledPrincipalPayment": 24452.845581
    }
    {
        "date": "2027-11-25",
        "totalCashFlow": 48763.226545,
        "interestPayment": 3791.067193,
        "principalBalance": 9053589.104568,
        "principalPayment": 44972.159351,
        "endPrincipalBalance": 9053589.104568,
        "beginPrincipalBalance": 9098561.263919,
        "prepayPrincipalPayment": 20553.073587,
        "scheduledPrincipalPayment": 24419.085764
    }
    {
        "date": "2027-12-25",
        "totalCashFlow": 48590.414778,
        "interestPayment": 3772.328794,
        "principalBalance": 9008771.018584,
        "principalPayment": 44818.085984,
        "endPrincipalBalance": 9008771.018584,
        "beginPrincipalBalance": 9053589.104568,
        "prepayPrincipalPayment": 20428.930897,
        "scheduledPrincipalPayment": 24389.155088
    }
    {
        "date": "2028-01-25",
        "totalCashFlow": 48860.144183,
        "interestPayment": 3753.654591,
        "principalBalance": 8963664.528992,
        "principalPayment": 45106.489591,
        "endPrincipalBalance": 8963664.528992,
        "beginPrincipalBalance": 9008771.018584,
        "prepayPrincipalPayment": 20747.168067,
        "scheduledPrincipalPayment": 24359.321525
    }
    {
        "date": "2028-02-25",
        "totalCashFlow": 45091.584517,
        "interestPayment": 3734.86022,
        "principalBalance": 8922307.804696,
        "principalPayment": 41356.724296,
        "endPrincipalBalance": 8922307.804696,
        "beginPrincipalBalance": 8963664.528992,
        "prepayPrincipalPayment": 17028.338607,
        "scheduledPrincipalPayment": 24328.385689
    }
    {
        "date": "2028-03-25",
        "totalCashFlow": 46059.668455,
        "interestPayment": 3717.628252,
        "principalBalance": 8879965.764493,
        "principalPayment": 42342.040203,
        "endPrincipalBalance": 8879965.764493,
        "beginPrincipalBalance": 8922307.804696,
        "prepayPrincipalPayment": 18034.703309,
        "scheduledPrincipalPayment": 24307.336894
    }
    {
        "date": "2028-04-25",
        "totalCashFlow": 50023.616913,
        "interestPayment": 3699.985735,
        "principalBalance": 8833642.133316,
        "principalPayment": 46323.631178,
        "endPrincipalBalance": 8833642.133316,
        "beginPrincipalBalance": 8879965.764493,
        "prepayPrincipalPayment": 22040.292216,
        "scheduledPrincipalPayment": 24283.338962
    }
    {
        "date": "2028-05-25",
        "totalCashFlow": 49358.349604,
        "interestPayment": 3680.684222,
        "principalBalance": 8787964.467934,
        "principalPayment": 45677.665382,
        "endPrincipalBalance": 8787964.467934,
        "beginPrincipalBalance": 8833642.133316,
        "prepayPrincipalPayment": 21429.531344,
        "scheduledPrincipalPayment": 24248.134038
    }
    {
        "date": "2028-06-25",
        "totalCashFlow": 53490.274903,
        "interestPayment": 3661.651862,
        "principalBalance": 8738135.844892,
        "principalPayment": 49828.623042,
        "endPrincipalBalance": 8738135.844892,
        "beginPrincipalBalance": 8787964.467934,
        "prepayPrincipalPayment": 25614.277433,
        "scheduledPrincipalPayment": 24214.345608
    }
    {
        "date": "2028-07-25",
        "totalCashFlow": 54451.047812,
        "interestPayment": 3640.889935,
        "principalBalance": 8687325.687015,
        "principalPayment": 50810.157877,
        "endPrincipalBalance": 8687325.687015,
        "beginPrincipalBalance": 8738135.844892,
        "prepayPrincipalPayment": 26641.435266,
        "scheduledPrincipalPayment": 24168.722611
    }
    {
        "date": "2028-08-25",
        "totalCashFlow": 52122.889362,
        "interestPayment": 3619.719036,
        "principalBalance": 8638822.516689,
        "principalPayment": 48503.170326,
        "endPrincipalBalance": 8638822.516689,
        "beginPrincipalBalance": 8687325.687015,
        "prepayPrincipalPayment": 24383.240589,
        "scheduledPrincipalPayment": 24119.929738
    }
    {
        "date": "2028-09-25",
        "totalCashFlow": 54212.911945,
        "interestPayment": 3599.509382,
        "principalBalance": 8588209.114126,
        "principalPayment": 50613.402563,
        "endPrincipalBalance": 8588209.114126,
        "beginPrincipalBalance": 8638822.516689,
        "prepayPrincipalPayment": 26536.305961,
        "scheduledPrincipalPayment": 24077.096602
    }
    {
        "date": "2028-10-25",
        "totalCashFlow": 50634.241212,
        "interestPayment": 3578.420464,
        "principalBalance": 8541153.293378,
        "principalPayment": 47055.820748,
        "endPrincipalBalance": 8541153.293378,
        "beginPrincipalBalance": 8588209.114126,
        "prepayPrincipalPayment": 23027.886628,
        "scheduledPrincipalPayment": 24027.93412
    }
    {
        "date": "2028-11-25",
        "totalCashFlow": 50526.503693,
        "interestPayment": 3558.813872,
        "principalBalance": 8494185.603558,
        "principalPayment": 46967.68982,
        "endPrincipalBalance": 8494185.603558,
        "beginPrincipalBalance": 8541153.293378,
        "prepayPrincipalPayment": 22979.40166,
        "scheduledPrincipalPayment": 23988.288161
    }
    {
        "date": "2028-12-25",
        "totalCashFlow": 49443.760337,
        "interestPayment": 3539.244001,
        "principalBalance": 8448281.087222,
        "principalPayment": 45904.516336,
        "endPrincipalBalance": 8448281.087222,
        "beginPrincipalBalance": 8494185.603558,
        "prepayPrincipalPayment": 21956.028448,
        "scheduledPrincipalPayment": 23948.487887
    }
    {
        "date": "2029-01-25",
        "totalCashFlow": 48864.189905,
        "interestPayment": 3520.11712,
        "principalBalance": 8402937.014437,
        "principalPayment": 45344.072785,
        "endPrincipalBalance": 8402937.014437,
        "beginPrincipalBalance": 8448281.087222,
        "prepayPrincipalPayment": 21432.78102,
        "scheduledPrincipalPayment": 23911.291765
    }
    {
        "date": "2029-02-25",
        "totalCashFlow": 46103.869307,
        "interestPayment": 3501.223756,
        "principalBalance": 8360334.368886,
        "principalPayment": 42602.645551,
        "endPrincipalBalance": 8360334.368886,
        "beginPrincipalBalance": 8402937.014437,
        "prepayPrincipalPayment": 18727.343246,
        "scheduledPrincipalPayment": 23875.302305
    }
    {
        "date": "2029-03-25",
        "totalCashFlow": 45798.432977,
        "interestPayment": 3483.472654,
        "principalBalance": 8318019.408563,
        "principalPayment": 42314.960323,
        "endPrincipalBalance": 8318019.408563,
        "beginPrincipalBalance": 8360334.368886,
        "prepayPrincipalPayment": 18468.205198,
        "scheduledPrincipalPayment": 23846.755126
    }
    {
        "date": "2029-04-25",
        "totalCashFlow": 49682.462983,
        "interestPayment": 3465.84142,
        "principalBalance": 8271802.787,
        "principalPayment": 46216.621563,
        "endPrincipalBalance": 8271802.787,
        "beginPrincipalBalance": 8318019.408563,
        "prepayPrincipalPayment": 22397.909913,
        "scheduledPrincipalPayment": 23818.71165
    }
    {
        "date": "2029-05-25",
        "totalCashFlow": 51530.569551,
        "interestPayment": 3446.584495,
        "principalBalance": 8223718.801943,
        "principalPayment": 48083.985057,
        "endPrincipalBalance": 8223718.801943,
        "beginPrincipalBalance": 8271802.787,
        "prepayPrincipalPayment": 24304.850017,
        "scheduledPrincipalPayment": 23779.135039
    }
    {
        "date": "2029-06-25",
        "totalCashFlow": 54720.498394,
        "interestPayment": 3426.549501,
        "principalBalance": 8172424.85305,
        "principalPayment": 51293.948893,
        "endPrincipalBalance": 8172424.85305,
        "beginPrincipalBalance": 8223718.801943,
        "prepayPrincipalPayment": 27560.188039,
        "scheduledPrincipalPayment": 23733.760854
    }
    {
        "date": "2029-07-25",
        "totalCashFlow": 54516.415883,
        "interestPayment": 3405.177022,
        "principalBalance": 8121313.614189,
        "principalPayment": 51111.238861,
        "endPrincipalBalance": 8121313.614189,
        "beginPrincipalBalance": 8172424.85305,
        "prepayPrincipalPayment": 27432.607713,
        "scheduledPrincipalPayment": 23678.631147
    }
    {
        "date": "2029-08-25",
        "totalCashFlow": 53965.10817,
        "interestPayment": 3383.880673,
        "principalBalance": 8070732.386692,
        "principalPayment": 50581.227497,
        "endPrincipalBalance": 8070732.386692,
        "beginPrincipalBalance": 8121313.614189,
        "prepayPrincipalPayment": 26957.72783,
        "scheduledPrincipalPayment": 23623.499667
    }
    {
        "date": "2029-09-25",
        "totalCashFlow": 55024.239624,
        "interestPayment": 3362.805161,
        "principalBalance": 8019070.952228,
        "principalPayment": 51661.434463,
        "endPrincipalBalance": 8019070.952228,
        "beginPrincipalBalance": 8070732.386692,
        "prepayPrincipalPayment": 28092.053045,
        "scheduledPrincipalPayment": 23569.381418
    }
    {
        "date": "2029-10-25",
        "totalCashFlow": 50013.075696,
        "interestPayment": 3341.279563,
        "principalBalance": 7972399.156095,
        "principalPayment": 46671.796133,
        "endPrincipalBalance": 7972399.156095,
        "beginPrincipalBalance": 8019070.952228,
        "prepayPrincipalPayment": 23160.227957,
        "scheduledPrincipalPayment": 23511.568176
    }
    {
        "date": "2029-11-25",
        "totalCashFlow": 51638.915542,
        "interestPayment": 3321.832982,
        "principalBalance": 7924082.073535,
        "principalPayment": 48317.082561,
        "endPrincipalBalance": 7924082.073535,
        "beginPrincipalBalance": 7972399.156095,
        "prepayPrincipalPayment": 24849.198573,
        "scheduledPrincipalPayment": 23467.883988
    }
    {
        "date": "2029-12-25",
        "totalCashFlow": 49457.453825,
        "interestPayment": 3301.700864,
        "principalBalance": 7877926.320574,
        "principalPayment": 46155.752961,
        "endPrincipalBalance": 7877926.320574,
        "beginPrincipalBalance": 7924082.073535,
        "prepayPrincipalPayment": 22736.862764,
        "scheduledPrincipalPayment": 23418.890197
    }
    {
        "date": "2030-01-25",
        "totalCashFlow": 48730.207454,
        "interestPayment": 3282.4693,
        "principalBalance": 7832478.582419,
        "principalPayment": 45447.738154,
        "endPrincipalBalance": 7832478.582419,
        "beginPrincipalBalance": 7877926.320574,
        "prepayPrincipalPayment": 22071.919357,
        "scheduledPrincipalPayment": 23375.818797
    }
    {
        "date": "2030-02-25",
        "totalCashFlow": 45761.832171,
        "interestPayment": 3263.532743,
        "principalBalance": 7789980.282991,
        "principalPayment": 42498.299428,
        "endPrincipalBalance": 7789980.282991,
        "beginPrincipalBalance": 7832478.582419,
        "prepayPrincipalPayment": 19163.887178,
        "scheduledPrincipalPayment": 23334.41225
    }
    {
        "date": "2030-03-25",
        "totalCashFlow": 45343.540324,
        "interestPayment": 3245.825118,
        "principalBalance": 7747882.567786,
        "principalPayment": 42097.715206,
        "endPrincipalBalance": 7747882.567786,
        "beginPrincipalBalance": 7789980.282991,
        "prepayPrincipalPayment": 18796.319312,
        "scheduledPrincipalPayment": 23301.395894
    }
    {
        "date": "2030-04-25",
        "totalCashFlow": 48905.852954,
        "interestPayment": 3228.284403,
        "principalBalance": 7702204.999235,
        "principalPayment": 45677.56855,
        "endPrincipalBalance": 7702204.999235,
        "beginPrincipalBalance": 7747882.567786,
        "prepayPrincipalPayment": 22408.351359,
        "scheduledPrincipalPayment": 23269.217192
    }
    {
        "date": "2030-05-25",
        "totalCashFlow": 51651.372428,
        "interestPayment": 3209.252083,
        "principalBalance": 7653762.87889,
        "principalPayment": 48442.120345,
        "endPrincipalBalance": 7653762.87889,
        "beginPrincipalBalance": 7702204.999235,
        "prepayPrincipalPayment": 25216.236434,
        "scheduledPrincipalPayment": 23225.883911
    }
    {
        "date": "2030-06-25",
        "totalCashFlow": 54367.252657,
        "interestPayment": 3189.067866,
        "principalBalance": 7602584.694099,
        "principalPayment": 51178.184791,
        "endPrincipalBalance": 7602584.694099,
        "beginPrincipalBalance": 7653762.87889,
        "prepayPrincipalPayment": 28004.455869,
        "scheduledPrincipalPayment": 23173.728921
    }
    {
        "date": "2030-07-25",
        "totalCashFlow": 53022.4596,
        "interestPayment": 3167.743623,
        "principalBalance": 7552729.978122,
        "principalPayment": 49854.715977,
        "endPrincipalBalance": 7552729.978122,
        "beginPrincipalBalance": 7602584.694099,
        "prepayPrincipalPayment": 26741.98452,
        "scheduledPrincipalPayment": 23112.731457
    }
    {
        "date": "2030-08-25",
        "totalCashFlow": 54735.527373,
        "interestPayment": 3146.970824,
        "principalBalance": 7501141.421573,
        "principalPayment": 51588.556549,
        "endPrincipalBalance": 7501141.421573,
        "beginPrincipalBalance": 7552729.978122,
        "prepayPrincipalPayment": 28533.380893,
        "scheduledPrincipalPayment": 23055.175656
    }
    {
        "date": "2030-09-25",
        "totalCashFlow": 53683.341855,
        "interestPayment": 3125.475592,
        "principalBalance": 7450583.555311,
        "principalPayment": 50557.866262,
        "endPrincipalBalance": 7450583.555311,
        "beginPrincipalBalance": 7501141.421573,
        "prepayPrincipalPayment": 27566.132408,
        "scheduledPrincipalPayment": 22991.733854
    }
    {
        "date": "2030-10-25",
        "totalCashFlow": 50556.776602,
        "interestPayment": 3104.409815,
        "principalBalance": 7403131.188524,
        "principalPayment": 47452.366787,
        "endPrincipalBalance": 7403131.188524,
        "beginPrincipalBalance": 7450583.555311,
        "prepayPrincipalPayment": 24521.524168,
        "scheduledPrincipalPayment": 22930.84262
    }
    {
        "date": "2030-11-25",
        "totalCashFlow": 51238.256481,
        "interestPayment": 3084.637995,
        "principalBalance": 7354977.570038,
        "principalPayment": 48153.618486,
        "endPrincipalBalance": 7354977.570038,
        "beginPrincipalBalance": 7403131.188524,
        "prepayPrincipalPayment": 25274.671917,
        "scheduledPrincipalPayment": 22878.946569
    }
    {
        "date": "2030-12-25",
        "totalCashFlow": 48030.303667,
        "interestPayment": 3064.573988,
        "principalBalance": 7310011.840358,
        "principalPayment": 44965.72968,
        "endPrincipalBalance": 7310011.840358,
        "beginPrincipalBalance": 7354977.570038,
        "prepayPrincipalPayment": 22141.384538,
        "scheduledPrincipalPayment": 22824.345142
    }
    {
        "date": "2031-01-25",
        "totalCashFlow": 49119.137794,
        "interestPayment": 3045.838267,
        "principalBalance": 7263938.540831,
        "principalPayment": 46073.299527,
        "endPrincipalBalance": 7263938.540831,
        "beginPrincipalBalance": 7310011.840358,
        "prepayPrincipalPayment": 23294.174995,
        "scheduledPrincipalPayment": 22779.124531
    }
    {
        "date": "2031-02-25",
        "totalCashFlow": 45056.369989,
        "interestPayment": 3026.641059,
        "principalBalance": 7221908.811901,
        "principalPayment": 42029.728931,
        "endPrincipalBalance": 7221908.811901,
        "beginPrincipalBalance": 7263938.540831,
        "prepayPrincipalPayment": 19299.767139,
        "scheduledPrincipalPayment": 22729.961791
    }
    {
        "date": "2031-03-25",
        "totalCashFlow": 44575.81083,
        "interestPayment": 3009.128672,
        "principalBalance": 7180342.129742,
        "principalPayment": 41566.682158,
        "endPrincipalBalance": 7180342.129742,
        "beginPrincipalBalance": 7221908.811901,
        "prepayPrincipalPayment": 18873.687887,
        "scheduledPrincipalPayment": 22692.994272
    }
    {
        "date": "2031-04-25",
        "totalCashFlow": 48230.977805,
        "interestPayment": 2991.809221,
        "principalBalance": 7135102.961158,
        "principalPayment": 45239.168584,
        "endPrincipalBalance": 7135102.961158,
        "beginPrincipalBalance": 7180342.129742,
        "prepayPrincipalPayment": 22582.090408,
        "scheduledPrincipalPayment": 22657.078177
    }
    {
        "date": "2031-05-25",
        "totalCashFlow": 51044.970602,
        "interestPayment": 2972.959567,
        "principalBalance": 7087030.950123,
        "principalPayment": 48072.011035,
        "endPrincipalBalance": 7087030.950123,
        "beginPrincipalBalance": 7135102.961158,
        "prepayPrincipalPayment": 25462.887992,
        "scheduledPrincipalPayment": 22609.123043
    }
    {
        "date": "2031-06-25",
        "totalCashFlow": 52698.165462,
        "interestPayment": 2952.929563,
        "principalBalance": 7037285.714223,
        "principalPayment": 49745.2359,
        "endPrincipalBalance": 7037285.714223,
        "beginPrincipalBalance": 7087030.950123,
        "prepayPrincipalPayment": 27193.58717,
        "scheduledPrincipalPayment": 22551.64873
    }
    {
        "date": "2031-07-25",
        "totalCashFlow": 53566.042314,
        "interestPayment": 2932.202381,
        "principalBalance": 6986651.87429,
        "principalPayment": 50633.839933,
        "endPrincipalBalance": 6986651.87429,
        "beginPrincipalBalance": 7037285.714223,
        "prepayPrincipalPayment": 28145.599306,
        "scheduledPrincipalPayment": 22488.240627
    }
    {
        "date": "2031-08-25",
        "totalCashFlow": 54079.589714,
        "interestPayment": 2911.104948,
        "principalBalance": 6935483.389524,
        "principalPayment": 51168.484767,
        "endPrincipalBalance": 6935483.389524,
        "beginPrincipalBalance": 6986651.87429,
        "prepayPrincipalPayment": 28747.142855,
        "scheduledPrincipalPayment": 22421.341912
    }
    {
        "date": "2031-09-25",
        "totalCashFlow": 51839.685154,
        "interestPayment": 2889.784746,
        "principalBalance": 6886533.489116,
        "principalPayment": 48949.900408,
        "endPrincipalBalance": 6886533.489116,
        "beginPrincipalBalance": 6935483.389524,
        "prepayPrincipalPayment": 26597.850773,
        "scheduledPrincipalPayment": 22352.049635
    }
    {
        "date": "2031-10-25",
        "totalCashFlow": 50713.051089,
        "interestPayment": 2869.388954,
        "principalBalance": 6838689.82698,
        "principalPayment": 47843.662135,
        "endPrincipalBalance": 6838689.82698,
        "beginPrincipalBalance": 6886533.489116,
        "prepayPrincipalPayment": 25554.416843,
        "scheduledPrincipalPayment": 22289.245292
    }
    {
        "date": "2031-11-25",
        "totalCashFlow": 50296.938159,
        "interestPayment": 2849.454095,
        "principalBalance": 6791242.342916,
        "principalPayment": 47447.484064,
        "endPrincipalBalance": 6791242.342916,
        "beginPrincipalBalance": 6838689.82698,
        "prepayPrincipalPayment": 25218.086323,
        "scheduledPrincipalPayment": 22229.397741
    }
    {
        "date": "2031-12-25",
        "totalCashFlow": 46013.709933,
        "interestPayment": 2829.68431,
        "principalBalance": 6748058.317293,
        "principalPayment": 43184.025623,
        "endPrincipalBalance": 6748058.317293,
        "beginPrincipalBalance": 6791242.342916,
        "prepayPrincipalPayment": 21013.797511,
        "scheduledPrincipalPayment": 22170.228113
    }
    {
        "date": "2032-01-25",
        "totalCashFlow": 48960.734385,
        "interestPayment": 2811.690966,
        "principalBalance": 6701909.273873,
        "principalPayment": 46149.04342,
        "endPrincipalBalance": 6701909.273873,
        "beginPrincipalBalance": 6748058.317293,
        "prepayPrincipalPayment": 24024.617908,
        "scheduledPrincipalPayment": 22124.425512
    }
    {
        "date": "2032-02-25",
        "totalCashFlow": 43117.465396,
        "interestPayment": 2792.462197,
        "principalBalance": 6661584.270674,
        "principalPayment": 40325.003199,
        "endPrincipalBalance": 6661584.270674,
        "beginPrincipalBalance": 6701909.273873,
        "prepayPrincipalPayment": 18256.640803,
        "scheduledPrincipalPayment": 22068.362396
    }
    {
        "date": "2032-03-25",
        "totalCashFlow": 43328.440831,
        "interestPayment": 2775.660113,
        "principalBalance": 6621031.489956,
        "principalPayment": 40552.780718,
        "endPrincipalBalance": 6621031.489956,
        "beginPrincipalBalance": 6661584.270674,
        "prepayPrincipalPayment": 18521.808207,
        "scheduledPrincipalPayment": 22030.972511
    }
    {
        "date": "2032-04-25",
        "totalCashFlow": 48343.702661,
        "interestPayment": 2758.763121,
        "principalBalance": 6575446.550415,
        "principalPayment": 45584.93954,
        "endPrincipalBalance": 6575446.550415,
        "beginPrincipalBalance": 6621031.489956,
        "prepayPrincipalPayment": 23592.540086,
        "scheduledPrincipalPayment": 21992.399455
    }
    {
        "date": "2032-05-25",
        "totalCashFlow": 50329.941026,
        "interestPayment": 2739.769396,
        "principalBalance": 6527856.378786,
        "principalPayment": 47590.17163,
        "endPrincipalBalance": 6527856.378786,
        "beginPrincipalBalance": 6575446.550415,
        "prepayPrincipalPayment": 25653.571406,
        "scheduledPrincipalPayment": 21936.600223
    }
    {
        "date": "2032-06-25",
        "totalCashFlow": 50337.994489,
        "interestPayment": 2719.940158,
        "principalBalance": 6480238.324454,
        "principalPayment": 47618.054332,
        "endPrincipalBalance": 6480238.324454,
        "beginPrincipalBalance": 6527856.378786,
        "prepayPrincipalPayment": 25744.563273,
        "scheduledPrincipalPayment": 21873.491058
    }
    {
        "date": "2032-07-25",
        "totalCashFlow": 53506.618977,
        "interestPayment": 2700.099302,
        "principalBalance": 6429431.804779,
        "principalPayment": 50806.519675,
        "endPrincipalBalance": 6429431.804779,
        "beginPrincipalBalance": 6480238.324454,
        "prepayPrincipalPayment": 28996.888603,
        "scheduledPrincipalPayment": 21809.631072
    }
    {
        "date": "2032-08-25",
        "totalCashFlow": 51619.849886,
        "interestPayment": 2678.929919,
        "principalBalance": 6380490.884812,
        "principalPayment": 48940.919967,
        "endPrincipalBalance": 6380490.884812,
        "beginPrincipalBalance": 6429431.804779,
        "prepayPrincipalPayment": 27206.592856,
        "scheduledPrincipalPayment": 21734.327111
    }
    {
        "date": "2032-09-25",
        "totalCashFlow": 51558.956426,
        "interestPayment": 2658.537869,
        "principalBalance": 6331590.466255,
        "principalPayment": 48900.418557,
        "endPrincipalBalance": 6331590.466255,
        "beginPrincipalBalance": 6380490.884812,
        "prepayPrincipalPayment": 27235.829938,
        "scheduledPrincipalPayment": 21664.588619
    }
    {
        "date": "2032-10-25",
        "totalCashFlow": 49279.257658,
        "interestPayment": 2638.162694,
        "principalBalance": 6284949.371291,
        "principalPayment": 46641.094963,
        "endPrincipalBalance": 6284949.371291,
        "beginPrincipalBalance": 6331590.466255,
        "prepayPrincipalPayment": 25046.828485,
        "scheduledPrincipalPayment": 21594.266479
    }
    {
        "date": "2032-11-25",
        "totalCashFlow": 46896.42984,
        "interestPayment": 2618.728905,
        "principalBalance": 6240671.670356,
        "principalPayment": 44277.700935,
        "endPrincipalBalance": 6240671.670356,
        "beginPrincipalBalance": 6284949.371291,
        "prepayPrincipalPayment": 22746.745757,
        "scheduledPrincipalPayment": 21530.955178
    }
    {
        "date": "2032-12-25",
        "totalCashFlow": 46428.656327,
        "interestPayment": 2600.279863,
        "principalBalance": 6196843.293892,
        "principalPayment": 43828.376464,
        "endPrincipalBalance": 6196843.293892,
        "beginPrincipalBalance": 6240671.670356,
        "prepayPrincipalPayment": 22353.268248,
        "scheduledPrincipalPayment": 21475.108216
    }
    {
        "date": "2033-01-25",
        "totalCashFlow": 46471.346264,
        "interestPayment": 2582.018039,
        "principalBalance": 6152953.965667,
        "principalPayment": 43889.328225,
        "endPrincipalBalance": 6152953.965667,
        "beginPrincipalBalance": 6196843.293892,
        "prepayPrincipalPayment": 22469.117142,
        "scheduledPrincipalPayment": 21420.211083
    }
    {
        "date": "2033-02-25",
        "totalCashFlow": 41532.531414,
        "interestPayment": 2563.730819,
        "principalBalance": 6113985.165072,
        "principalPayment": 38968.800595,
        "endPrincipalBalance": 6113985.165072,
        "beginPrincipalBalance": 6152953.965667,
        "prepayPrincipalPayment": 17604.294861,
        "scheduledPrincipalPayment": 21364.505735
    }
    {
        "date": "2033-03-25",
        "totalCashFlow": 41716.758299,
        "interestPayment": 2547.493819,
        "principalBalance": 6074815.900591,
        "principalPayment": 39169.264481,
        "endPrincipalBalance": 6074815.900591,
        "beginPrincipalBalance": 6113985.165072,
        "prepayPrincipalPayment": 17843.907191,
        "scheduledPrincipalPayment": 21325.35729
    }
    {
        "date": "2033-04-25",
        "totalCashFlow": 47123.92888,
        "interestPayment": 2531.173292,
        "principalBalance": 6030223.145003,
        "principalPayment": 44592.755588,
        "endPrincipalBalance": 6030223.145003,
        "beginPrincipalBalance": 6074815.900591,
        "prepayPrincipalPayment": 23307.706188,
        "scheduledPrincipalPayment": 21285.0494
    }
    {
        "date": "2033-05-25",
        "totalCashFlow": 47126.584901,
        "interestPayment": 2512.592977,
        "principalBalance": 5985609.153079,
        "principalPayment": 44613.991924,
        "endPrincipalBalance": 5985609.153079,
        "beginPrincipalBalance": 6030223.145003,
        "prepayPrincipalPayment": 23388.809075,
        "scheduledPrincipalPayment": 21225.182849
    }
    {
        "date": "2033-06-25",
        "totalCashFlow": 49739.130562,
        "interestPayment": 2494.003814,
        "principalBalance": 5938364.02633,
        "principalPayment": 47245.126749,
        "endPrincipalBalance": 5938364.02633,
        "beginPrincipalBalance": 5985609.153079,
        "prepayPrincipalPayment": 26080.535122,
        "scheduledPrincipalPayment": 21164.591627
    }
    {
        "date": "2033-07-25",
        "totalCashFlow": 51726.070624,
        "interestPayment": 2474.318344,
        "principalBalance": 5889112.27405,
        "principalPayment": 49251.75228,
        "endPrincipalBalance": 5889112.27405,
        "beginPrincipalBalance": 5938364.02633,
        "prepayPrincipalPayment": 28157.756335,
        "scheduledPrincipalPayment": 21093.995945
    }
    {
        "date": "2033-08-25",
        "totalCashFlow": 48679.523222,
        "interestPayment": 2453.796781,
        "principalBalance": 5842886.547609,
        "principalPayment": 46225.726441,
        "endPrincipalBalance": 5842886.547609,
        "beginPrincipalBalance": 5889112.27405,
        "prepayPrincipalPayment": 25210.239445,
        "scheduledPrincipalPayment": 21015.486996
    }
    {
        "date": "2033-09-25",
        "totalCashFlow": 50799.38027,
        "interestPayment": 2434.536062,
        "principalBalance": 5794521.703401,
        "principalPayment": 48364.844208,
        "endPrincipalBalance": 5794521.703401,
        "beginPrincipalBalance": 5842886.547609,
        "prepayPrincipalPayment": 27417.845867,
        "scheduledPrincipalPayment": 20946.998341
    }
    {
        "date": "2033-10-25",
        "totalCashFlow": 47413.541394,
        "interestPayment": 2414.384043,
        "principalBalance": 5749522.54605,
        "principalPayment": 44999.157351,
        "endPrincipalBalance": 5749522.54605,
        "beginPrincipalBalance": 5794521.703401,
        "prepayPrincipalPayment": 24129.089786,
        "scheduledPrincipalPayment": 20870.067565
    }
    {
        "date": "2033-11-25",
        "totalCashFlow": 45035.554016,
        "interestPayment": 2395.634394,
        "principalBalance": 5706882.626428,
        "principalPayment": 42639.919622,
        "endPrincipalBalance": 5706882.626428,
        "beginPrincipalBalance": 5749522.54605,
        "prepayPrincipalPayment": 21835.422883,
        "scheduledPrincipalPayment": 20804.496739
    }
    {
        "date": "2033-12-25",
        "totalCashFlow": 44560.694913,
        "interestPayment": 2377.867761,
        "principalBalance": 5664699.799276,
        "principalPayment": 42182.827152,
        "endPrincipalBalance": 5664699.799276,
        "beginPrincipalBalance": 5706882.626428,
        "prepayPrincipalPayment": 21436.039507,
        "scheduledPrincipalPayment": 20746.787645
    }
    {
        "date": "2034-01-25",
        "totalCashFlow": 44579.282921,
        "interestPayment": 2360.291583,
        "principalBalance": 5622480.807939,
        "principalPayment": 42218.991337,
        "endPrincipalBalance": 5622480.807939,
        "beginPrincipalBalance": 5664699.799276,
        "prepayPrincipalPayment": 21528.886789,
        "scheduledPrincipalPayment": 20690.104548
    }
    {
        "date": "2034-02-25",
        "totalCashFlow": 39696.216446,
        "interestPayment": 2342.700337,
        "principalBalance": 5585127.291829,
        "principalPayment": 37353.51611,
        "endPrincipalBalance": 5585127.291829,
        "beginPrincipalBalance": 5622480.807939,
        "prepayPrincipalPayment": 16720.863293,
        "scheduledPrincipalPayment": 20632.652817
    }
    {
        "date": "2034-03-25",
        "totalCashFlow": 39982.107978,
        "interestPayment": 2327.136372,
        "principalBalance": 5547472.320223,
        "principalPayment": 37654.971607,
        "endPrincipalBalance": 5547472.320223,
        "beginPrincipalBalance": 5585127.291829,
        "prepayPrincipalPayment": 17062.476657,
        "scheduledPrincipalPayment": 20592.494949
    }
    {
        "date": "2034-04-25",
        "totalCashFlow": 45444.51209,
        "interestPayment": 2311.4468,
        "principalBalance": 5504339.254932,
        "principalPayment": 43133.06529,
        "endPrincipalBalance": 5504339.254932,
        "beginPrincipalBalance": 5547472.320223,
        "prepayPrincipalPayment": 22582.328157,
        "scheduledPrincipalPayment": 20550.737133
    }
    {
        "date": "2034-05-25",
        "totalCashFlow": 45091.013024,
        "interestPayment": 2293.47469,
        "principalBalance": 5461541.716598,
        "principalPayment": 42797.538335,
        "endPrincipalBalance": 5461541.716598,
        "beginPrincipalBalance": 5504339.254932,
        "prepayPrincipalPayment": 22309.449459,
        "scheduledPrincipalPayment": 20488.088876
    }
    {
        "date": "2034-06-25",
        "totalCashFlow": 49451.227253,
        "interestPayment": 2275.642382,
        "principalBalance": 5414366.131727,
        "principalPayment": 47175.584871,
        "endPrincipalBalance": 5414366.131727,
        "beginPrincipalBalance": 5461541.716598,
        "prepayPrincipalPayment": 26749.590874,
        "scheduledPrincipalPayment": 20425.993997
    }
    {
        "date": "2034-07-25",
        "totalCashFlow": 50460.734362,
        "interestPayment": 2255.985888,
        "principalBalance": 5366161.383253,
        "principalPayment": 48204.748474,
        "endPrincipalBalance": 5366161.383253,
        "beginPrincipalBalance": 5414366.131727,
        "prepayPrincipalPayment": 27858.00019,
        "scheduledPrincipalPayment": 20346.748284
    }
    {
        "date": "2034-08-25",
        "totalCashFlow": 47535.237805,
        "interestPayment": 2235.900576,
        "principalBalance": 5320862.046024,
        "principalPayment": 45299.337229,
        "endPrincipalBalance": 5320862.046024,
        "beginPrincipalBalance": 5366161.383253,
        "prepayPrincipalPayment": 25036.586873,
        "scheduledPrincipalPayment": 20262.750356
    }
    {
        "date": "2034-09-25",
        "totalCashFlow": 49798.374966,
        "interestPayment": 2217.025853,
        "principalBalance": 5273280.69691,
        "principalPayment": 47581.349114,
        "endPrincipalBalance": 5273280.69691,
        "beginPrincipalBalance": 5320862.046024,
        "prepayPrincipalPayment": 27392.487646,
        "scheduledPrincipalPayment": 20188.861468
    }
    {
        "date": "2034-10-25",
        "totalCashFlow": 45462.428272,
        "interestPayment": 2197.20029,
        "principalBalance": 5230015.468929,
        "principalPayment": 43265.227982,
        "endPrincipalBalance": 5230015.468929,
        "beginPrincipalBalance": 5273280.69691,
        "prepayPrincipalPayment": 23159.775865,
        "scheduledPrincipalPayment": 20105.452117
    }
    {
        "date": "2034-11-25",
        "totalCashFlow": 45142.142227,
        "interestPayment": 2179.173112,
        "principalBalance": 5187052.499814,
        "principalPayment": 42962.969115,
        "endPrincipalBalance": 5187052.499814,
        "beginPrincipalBalance": 5230015.468929,
        "prepayPrincipalPayment": 22925.305449,
        "scheduledPrincipalPayment": 20037.663666
    }
    {
        "date": "2034-12-25",
        "totalCashFlow": 43795.139435,
        "interestPayment": 2161.271875,
        "principalBalance": 5145418.632253,
        "principalPayment": 41633.86756,
        "endPrincipalBalance": 5145418.632253,
        "beginPrincipalBalance": 5187052.499814,
        "prepayPrincipalPayment": 21663.594289,
        "scheduledPrincipalPayment": 19970.273271
    }
    {
        "date": "2035-01-25",
        "totalCashFlow": 42973.543419,
        "interestPayment": 2143.92443,
        "principalBalance": 5104589.013264,
        "principalPayment": 40829.618989,
        "endPrincipalBalance": 5104589.013264,
        "beginPrincipalBalance": 5145418.632253,
        "prepayPrincipalPayment": 20922.358264,
        "scheduledPrincipalPayment": 19907.260725
    }
    {
        "date": "2035-02-25",
        "totalCashFlow": 39724.252466,
        "interestPayment": 2126.912089,
        "principalBalance": 5066991.672887,
        "principalPayment": 37597.340377,
        "endPrincipalBalance": 5066991.672887,
        "beginPrincipalBalance": 5104589.013264,
        "prepayPrincipalPayment": 17750.689089,
        "scheduledPrincipalPayment": 19846.651288
    }
    {
        "date": "2035-03-25",
        "totalCashFlow": 39254.199039,
        "interestPayment": 2111.24653,
        "principalBalance": 5029848.720379,
        "principalPayment": 37142.952508,
        "endPrincipalBalance": 5029848.720379,
        "beginPrincipalBalance": 5066991.672887,
        "prepayPrincipalPayment": 17344.983884,
        "scheduledPrincipalPayment": 19797.968625
    }
    {
        "date": "2035-04-25",
        "totalCashFlow": 43444.953704,
        "interestPayment": 2095.7703,
        "principalBalance": 4988499.536975,
        "principalPayment": 41349.183404,
        "endPrincipalBalance": 4988499.536975,
        "beginPrincipalBalance": 5029848.720379,
        "prepayPrincipalPayment": 21598.699674,
        "scheduledPrincipalPayment": 19750.48373
    }
    {
        "date": "2035-05-25",
        "totalCashFlow": 45408.239694,
        "interestPayment": 2078.541474,
        "principalBalance": 4945169.838755,
        "principalPayment": 43329.69822,
        "endPrincipalBalance": 4945169.838755,
        "beginPrincipalBalance": 4988499.536975,
        "prepayPrincipalPayment": 23643.874752,
        "scheduledPrincipalPayment": 19685.823467
    }
    {
        "date": "2035-06-25",
        "totalCashFlow": 48749.315864,
        "interestPayment": 2060.487433,
        "principalBalance": 4898481.010324,
        "principalPayment": 46688.828431,
        "endPrincipalBalance": 4898481.010324,
        "beginPrincipalBalance": 4945169.838755,
        "prepayPrincipalPayment": 27076.270573,
        "scheduledPrincipalPayment": 19612.557858
    }
    {
        "date": "2035-07-25",
        "totalCashFlow": 48483.379891,
        "interestPayment": 2041.033754,
        "principalBalance": 4852038.664187,
        "principalPayment": 46442.346137,
        "endPrincipalBalance": 4852038.664187,
        "beginPrincipalBalance": 4898481.010324,
        "prepayPrincipalPayment": 26917.282986,
        "scheduledPrincipalPayment": 19525.063151
    }
    {
        "date": "2035-08-25",
        "totalCashFlow": 47817.051327,
        "interestPayment": 2021.682777,
        "principalBalance": 4806243.295637,
        "principalPayment": 45795.36855,
        "endPrincipalBalance": 4806243.295637,
        "beginPrincipalBalance": 4852038.664187,
        "prepayPrincipalPayment": 26357.799106,
        "scheduledPrincipalPayment": 19437.569444
    }
    {
        "date": "2035-09-25",
        "totalCashFlow": 48847.447408,
        "interestPayment": 2002.601373,
        "principalBalance": 4759398.449601,
        "principalPayment": 46844.846035,
        "endPrincipalBalance": 4759398.449601,
        "beginPrincipalBalance": 4806243.295637,
        "prepayPrincipalPayment": 27493.155248,
        "scheduledPrincipalPayment": 19351.690787
    }
    {
        "date": "2035-10-25",
        "totalCashFlow": 43375.42713,
        "interestPayment": 1983.082687,
        "principalBalance": 4718006.105159,
        "principalPayment": 41392.344442,
        "endPrincipalBalance": 4718006.105159,
        "beginPrincipalBalance": 4759398.449601,
        "prepayPrincipalPayment": 22131.756414,
        "scheduledPrincipalPayment": 19260.588028
    }
    {
        "date": "2035-11-25",
        "totalCashFlow": 44988.733907,
        "interestPayment": 1965.835877,
        "principalBalance": 4674983.207129,
        "principalPayment": 43022.89803,
        "endPrincipalBalance": 4674983.207129,
        "beginPrincipalBalance": 4718006.105159,
        "prepayPrincipalPayment": 23832.268464,
        "scheduledPrincipalPayment": 19190.629566
    }
    {
        "date": "2035-12-25",
        "totalCashFlow": 42622.154548,
        "interestPayment": 1947.90967,
        "principalBalance": 4634308.962251,
        "principalPayment": 40674.244878,
        "endPrincipalBalance": 4634308.962251,
        "beginPrincipalBalance": 4674983.207129,
        "prepayPrincipalPayment": 21561.060831,
        "scheduledPrincipalPayment": 19113.184047
    }
    {
        "date": "2036-01-25",
        "totalCashFlow": 41741.136678,
        "interestPayment": 1930.962068,
        "principalBalance": 4594498.78764,
        "principalPayment": 39810.174611,
        "endPrincipalBalance": 4594498.78764,
        "beginPrincipalBalance": 4634308.962251,
        "prepayPrincipalPayment": 20765.68523,
        "scheduledPrincipalPayment": 19044.48938
    }
    {
        "date": "2036-02-25",
        "totalCashFlow": 38460.524851,
        "interestPayment": 1914.374495,
        "principalBalance": 4557952.637285,
        "principalPayment": 36546.150356,
        "endPrincipalBalance": 4557952.637285,
        "beginPrincipalBalance": 4594498.78764,
        "prepayPrincipalPayment": 17567.600027,
        "scheduledPrincipalPayment": 18978.550329
    }
    {
        "date": "2036-03-25",
        "totalCashFlow": 38716.150694,
        "interestPayment": 1899.146932,
        "principalBalance": 4521135.633523,
        "principalPayment": 36817.003762,
        "endPrincipalBalance": 4521135.633523,
        "beginPrincipalBalance": 4557952.637285,
        "prepayPrincipalPayment": 17891.627701,
        "scheduledPrincipalPayment": 18925.37606
    }
    {
        "date": "2036-04-25",
        "totalCashFlow": 41580.832562,
        "interestPayment": 1883.806514,
        "principalBalance": 4481438.607475,
        "principalPayment": 39697.026048,
        "endPrincipalBalance": 4481438.607475,
        "beginPrincipalBalance": 4521135.633523,
        "prepayPrincipalPayment": 20826.612516,
        "scheduledPrincipalPayment": 18870.413532
    }
    {
        "date": "2036-05-25",
        "totalCashFlow": 44422.485524,
        "interestPayment": 1867.266086,
        "principalBalance": 4438883.388038,
        "principalPayment": 42555.219437,
        "endPrincipalBalance": 4438883.388038,
        "beginPrincipalBalance": 4481438.607475,
        "prepayPrincipalPayment": 23752.531055,
        "scheduledPrincipalPayment": 18802.688383
    }
    {
        "date": "2036-06-25",
        "totalCashFlow": 46050.883204,
        "interestPayment": 1849.534745,
        "principalBalance": 4394682.039579,
        "principalPayment": 44201.348459,
        "endPrincipalBalance": 4394682.039579,
        "beginPrincipalBalance": 4438883.388038,
        "prepayPrincipalPayment": 25479.256137,
        "scheduledPrincipalPayment": 18722.092322
    }
    {
        "date": "2036-07-25",
        "totalCashFlow": 46864.0773,
        "interestPayment": 1831.117516,
        "principalBalance": 4349649.079795,
        "principalPayment": 45032.959784,
        "endPrincipalBalance": 4349649.079795,
        "beginPrincipalBalance": 4394682.039579,
        "prepayPrincipalPayment": 26399.397966,
        "scheduledPrincipalPayment": 18633.561818
    }
    {
        "date": "2036-08-25",
        "totalCashFlow": 47287.297728,
        "interestPayment": 1812.353783,
        "principalBalance": 4304174.13585,
        "principalPayment": 45474.943945,
        "endPrincipalBalance": 4304174.13585,
        "beginPrincipalBalance": 4349649.079795,
        "prepayPrincipalPayment": 26934.499993,
        "scheduledPrincipalPayment": 18540.443951
    }
    {
        "date": "2036-09-25",
        "totalCashFlow": 44940.360976,
        "interestPayment": 1793.40589,
        "principalBalance": 4261027.180764,
        "principalPayment": 43146.955086,
        "endPrincipalBalance": 4261027.180764,
        "beginPrincipalBalance": 4304174.13585,
        "prepayPrincipalPayment": 24702.618453,
        "scheduledPrincipalPayment": 18444.336634
    }
    {
        "date": "2036-10-25",
        "totalCashFlow": 43748.395585,
        "interestPayment": 1775.427992,
        "principalBalance": 4219054.21317,
        "principalPayment": 41972.967593,
        "endPrincipalBalance": 4219054.21317,
        "beginPrincipalBalance": 4261027.180764,
        "prepayPrincipalPayment": 23615.840595,
        "scheduledPrincipalPayment": 18357.126999
    }
    {
        "date": "2036-11-25",
        "totalCashFlow": 43206.70855,
        "interestPayment": 1757.939255,
        "principalBalance": 4177605.443876,
        "principalPayment": 41448.769294,
        "endPrincipalBalance": 4177605.443876,
        "beginPrincipalBalance": 4219054.21317,
        "prepayPrincipalPayment": 23174.807424,
        "scheduledPrincipalPayment": 18273.96187
    }
    {
        "date": "2036-12-25",
        "totalCashFlow": 39006.126143,
        "interestPayment": 1740.668935,
        "principalBalance": 4140339.986668,
        "principalPayment": 37265.457208,
        "endPrincipalBalance": 4140339.986668,
        "beginPrincipalBalance": 4177605.443876,
        "prepayPrincipalPayment": 19073.37852,
        "scheduledPrincipalPayment": 18192.078688
    }
    {
        "date": "2037-01-25",
        "totalCashFlow": 41754.749319,
        "interestPayment": 1725.141661,
        "principalBalance": 4100310.379011,
        "principalPayment": 40029.607658,
        "endPrincipalBalance": 4100310.379011,
        "beginPrincipalBalance": 4140339.986668,
        "prepayPrincipalPayment": 21902.087261,
        "scheduledPrincipalPayment": 18127.520397
    }
    {
        "date": "2037-02-25",
        "totalCashFlow": 36050.686313,
        "interestPayment": 1708.462658,
        "principalBalance": 4065968.155355,
        "principalPayment": 34342.223655,
        "endPrincipalBalance": 4065968.155355,
        "beginPrincipalBalance": 4100310.379011,
        "prepayPrincipalPayment": 16292.235665,
        "scheduledPrincipalPayment": 18049.98799
    }
    {
        "date": "2037-03-25",
        "totalCashFlow": 36214.400713,
        "interestPayment": 1694.153398,
        "principalBalance": 4031447.908041,
        "principalPayment": 34520.247315,
        "endPrincipalBalance": 4031447.908041,
        "beginPrincipalBalance": 4065968.155355,
        "prepayPrincipalPayment": 16523.569505,
        "scheduledPrincipalPayment": 17996.67781
    }
    {
        "date": "2037-04-25",
        "totalCashFlow": 40527.71527,
        "interestPayment": 1679.769962,
        "principalBalance": 3992599.962732,
        "principalPayment": 38847.945308,
        "endPrincipalBalance": 3992599.962732,
        "beginPrincipalBalance": 4031447.908041,
        "prepayPrincipalPayment": 20906.058809,
        "scheduledPrincipalPayment": 17941.8865
    }
    {
        "date": "2037-05-25",
        "totalCashFlow": 42850.180168,
        "interestPayment": 1663.583318,
        "principalBalance": 3951413.365881,
        "principalPayment": 41186.596851,
        "endPrincipalBalance": 3951413.365881,
        "beginPrincipalBalance": 3992599.962732,
        "prepayPrincipalPayment": 23319.57621,
        "scheduledPrincipalPayment": 17867.020641
    }
    {
        "date": "2037-06-25",
        "totalCashFlow": 42819.868823,
        "interestPayment": 1646.422236,
        "principalBalance": 3910239.919294,
        "principalPayment": 41173.446587,
        "endPrincipalBalance": 3910239.919294,
        "beginPrincipalBalance": 3951413.365881,
        "prepayPrincipalPayment": 23392.748652,
        "scheduledPrincipalPayment": 17780.697936
    }
    {
        "date": "2037-07-25",
        "totalCashFlow": 45750.271249,
        "interestPayment": 1629.266633,
        "principalBalance": 3866118.914678,
        "principalPayment": 44121.004616,
        "endPrincipalBalance": 3866118.914678,
        "beginPrincipalBalance": 3910239.919294,
        "prepayPrincipalPayment": 26427.634523,
        "scheduledPrincipalPayment": 17693.370093
    }
    {
        "date": "2037-08-25",
        "totalCashFlow": 44939.863185,
        "interestPayment": 1610.882881,
        "principalBalance": 3822789.934374,
        "principalPayment": 43328.980304,
        "endPrincipalBalance": 3822789.934374,
        "beginPrincipalBalance": 3866118.914678,
        "prepayPrincipalPayment": 25737.430201,
        "scheduledPrincipalPayment": 17591.550103
    }
    {
        "date": "2037-09-25",
        "totalCashFlow": 42643.126396,
        "interestPayment": 1592.829139,
        "principalBalance": 3781739.637117,
        "principalPayment": 41050.297257,
        "endPrincipalBalance": 3781739.637117,
        "beginPrincipalBalance": 3822789.934374,
        "prepayPrincipalPayment": 23558.190505,
        "scheduledPrincipalPayment": 17492.106752
    }
    {
        "date": "2037-10-25",
        "totalCashFlow": 41464.889299,
        "interestPayment": 1575.724849,
        "principalBalance": 3741850.472667,
        "principalPayment": 39889.16445,
        "endPrincipalBalance": 3741850.472667,
        "beginPrincipalBalance": 3781739.637117,
        "prepayPrincipalPayment": 22487.241313,
        "scheduledPrincipalPayment": 17401.923137
    }
    {
        "date": "2037-11-25",
        "totalCashFlow": 40022.923218,
        "interestPayment": 1559.104364,
        "principalBalance": 3703386.653812,
        "principalPayment": 38463.818855,
        "endPrincipalBalance": 3703386.653812,
        "beginPrincipalBalance": 3741850.472667,
        "prepayPrincipalPayment": 21147.831873,
        "scheduledPrincipalPayment": 17315.986982
    }
    {
        "date": "2037-12-25",
        "totalCashFlow": 37773.533213,
        "interestPayment": 1543.077772,
        "principalBalance": 3667156.198372,
        "principalPayment": 36230.45544,
        "endPrincipalBalance": 3667156.198372,
        "beginPrincipalBalance": 3703386.653812,
        "prepayPrincipalPayment": 18994.853214,
        "scheduledPrincipalPayment": 17235.602226
    }
    {
        "date": "2038-01-25",
        "totalCashFlow": 39450.92825,
        "interestPayment": 1527.981749,
        "principalBalance": 3629233.251871,
        "principalPayment": 37922.946501,
        "endPrincipalBalance": 3629233.251871,
        "beginPrincipalBalance": 3667156.198372,
        "prepayPrincipalPayment": 20758.298643,
        "scheduledPrincipalPayment": 17164.647858
    }
    {
        "date": "2038-02-25",
        "totalCashFlow": 33368.78178,
        "interestPayment": 1512.180522,
        "principalBalance": 3597376.650613,
        "principalPayment": 31856.601258,
        "endPrincipalBalance": 3597376.650613,
        "beginPrincipalBalance": 3629233.251871,
        "prepayPrincipalPayment": 14771.794345,
        "scheduledPrincipalPayment": 17084.806914
    }
    {
        "date": "2038-03-25",
        "totalCashFlow": 34149.173318,
        "interestPayment": 1498.906938,
        "principalBalance": 3564726.384233,
        "principalPayment": 32650.26638,
        "endPrincipalBalance": 3564726.384233,
        "beginPrincipalBalance": 3597376.650613,
        "prepayPrincipalPayment": 15617.60348,
        "scheduledPrincipalPayment": 17032.662901
    }
    {
        "date": "2038-04-25",
        "totalCashFlow": 38977.169449,
        "interestPayment": 1485.30266,
        "principalBalance": 3527234.517444,
        "principalPayment": 37491.866789,
        "endPrincipalBalance": 3527234.517444,
        "beginPrincipalBalance": 3564726.384233,
        "prepayPrincipalPayment": 20515.83608,
        "scheduledPrincipalPayment": 16976.030709
    }
    {
        "date": "2038-05-25",
        "totalCashFlow": 39876.104124,
        "interestPayment": 1469.681049,
        "principalBalance": 3488828.094369,
        "principalPayment": 38406.423075,
        "endPrincipalBalance": 3488828.094369,
        "beginPrincipalBalance": 3527234.517444,
        "prepayPrincipalPayment": 21510.979796,
        "scheduledPrincipalPayment": 16895.443278
    }
    {
        "date": "2038-06-25",
        "totalCashFlow": 40266.167431,
        "interestPayment": 1453.678373,
        "principalBalance": 3450015.605311,
        "principalPayment": 38812.489058,
        "endPrincipalBalance": 3450015.605311,
        "beginPrincipalBalance": 3488828.094369,
        "prepayPrincipalPayment": 22003.087664,
        "scheduledPrincipalPayment": 16809.401394
    }
    {
        "date": "2038-07-25",
        "totalCashFlow": 42980.979507,
        "interestPayment": 1437.506502,
        "principalBalance": 3408472.132307,
        "principalPayment": 41543.473004,
        "endPrincipalBalance": 3408472.132307,
        "beginPrincipalBalance": 3450015.605311,
        "prepayPrincipalPayment": 24823.19834,
        "scheduledPrincipalPayment": 16720.274664
    }
    {
        "date": "2038-08-25",
        "totalCashFlow": 41168.586846,
        "interestPayment": 1420.196722,
        "principalBalance": 3368723.742182,
        "principalPayment": 39748.390124,
        "endPrincipalBalance": 3368723.742182,
        "beginPrincipalBalance": 3408472.132307,
        "prepayPrincipalPayment": 23131.714324,
        "scheduledPrincipalPayment": 16616.6758
    }
    {
        "date": "2038-09-25",
        "totalCashFlow": 40949.848397,
        "interestPayment": 1403.634893,
        "principalBalance": 3329177.528678,
        "principalPayment": 39546.213504,
        "endPrincipalBalance": 3329177.528678,
        "beginPrincipalBalance": 3368723.742182,
        "prepayPrincipalPayment": 23025.668815,
        "scheduledPrincipalPayment": 16520.544689
    }
    {
        "date": "2038-10-25",
        "totalCashFlow": 38836.244437,
        "interestPayment": 1387.157304,
        "principalBalance": 3291728.441544,
        "principalPayment": 37449.087134,
        "endPrincipalBalance": 3291728.441544,
        "beginPrincipalBalance": 3329177.528678,
        "prepayPrincipalPayment": 21024.92834,
        "scheduledPrincipalPayment": 16424.158794
    }
    {
        "date": "2038-11-25",
        "totalCashFlow": 36631.289714,
        "interestPayment": 1371.553517,
        "principalBalance": 3256468.705348,
        "principalPayment": 35259.736197,
        "endPrincipalBalance": 3256468.705348,
        "beginPrincipalBalance": 3291728.441544,
        "prepayPrincipalPayment": 18922.816082,
        "scheduledPrincipalPayment": 16336.920115
    }
    {
        "date": "2038-12-25",
        "totalCashFlow": 36154.194884,
        "interestPayment": 1356.861961,
        "principalBalance": 3221671.372424,
        "principalPayment": 34797.332924,
        "endPrincipalBalance": 3221671.372424,
        "beginPrincipalBalance": 3256468.705348,
        "prepayPrincipalPayment": 18537.876272,
        "scheduledPrincipalPayment": 16259.456651
    }
    {
        "date": "2039-01-25",
        "totalCashFlow": 36069.971954,
        "interestPayment": 1342.363072,
        "principalBalance": 3186943.763542,
        "principalPayment": 34727.608882,
        "endPrincipalBalance": 3186943.763542,
        "beginPrincipalBalance": 3221671.372424,
        "prepayPrincipalPayment": 18544.335755,
        "scheduledPrincipalPayment": 16183.273127
    }
    {
        "date": "2039-02-25",
        "totalCashFlow": 31781.406695,
        "interestPayment": 1327.893235,
        "principalBalance": 3156490.250082,
        "principalPayment": 30453.51346,
        "endPrincipalBalance": 3156490.250082,
        "beginPrincipalBalance": 3186943.763542,
        "prepayPrincipalPayment": 14347.10348,
        "scheduledPrincipalPayment": 16106.40998
    }
    {
        "date": "2039-03-25",
        "totalCashFlow": 31892.820585,
        "interestPayment": 1315.204271,
        "principalBalance": 3125912.633768,
        "principalPayment": 30577.616314,
        "endPrincipalBalance": 3125912.633768,
        "beginPrincipalBalance": 3156490.250082,
        "prepayPrincipalPayment": 14527.38149,
        "scheduledPrincipalPayment": 16050.234824
    }
    {
        "date": "2039-04-25",
        "totalCashFlow": 36359.880339,
        "interestPayment": 1302.463597,
        "principalBalance": 3090855.217027,
        "principalPayment": 35057.416741,
        "endPrincipalBalance": 3090855.217027,
        "beginPrincipalBalance": 3125912.633768,
        "prepayPrincipalPayment": 19064.787147,
        "scheduledPrincipalPayment": 15992.629594
    }
    {
        "date": "2039-05-25",
        "totalCashFlow": 36357.868051,
        "interestPayment": 1287.85634,
        "principalBalance": 3055785.205317,
        "principalPayment": 35070.011711,
        "endPrincipalBalance": 3055785.205317,
        "beginPrincipalBalance": 3090855.217027,
        "prepayPrincipalPayment": 19158.865098,
        "scheduledPrincipalPayment": 15911.146612
    }
    {
        "date": "2039-06-25",
        "totalCashFlow": 38478.956215,
        "interestPayment": 1273.243836,
        "principalBalance": 3018579.492937,
        "principalPayment": 37205.712379,
        "endPrincipalBalance": 3018579.492937,
        "beginPrincipalBalance": 3055785.205317,
        "prepayPrincipalPayment": 21377.231527,
        "scheduledPrincipalPayment": 15828.480853
    }
    {
        "date": "2039-07-25",
        "totalCashFlow": 40042.901245,
        "interestPayment": 1257.741455,
        "principalBalance": 2979794.333148,
        "principalPayment": 38785.15979,
        "endPrincipalBalance": 2979794.333148,
        "beginPrincipalBalance": 3018579.492937,
        "prepayPrincipalPayment": 23051.614091,
        "scheduledPrincipalPayment": 15733.545699
    }
    {
        "date": "2039-08-25",
        "totalCashFlow": 37418.147193,
        "interestPayment": 1241.580972,
        "principalBalance": 2943617.766926,
        "principalPayment": 36176.566221,
        "endPrincipalBalance": 2943617.766926,
        "beginPrincipalBalance": 2979794.333148,
        "prepayPrincipalPayment": 20547.537188,
        "scheduledPrincipalPayment": 15629.029033
    }
    {
        "date": "2039-09-25",
        "totalCashFlow": 39022.136406,
        "interestPayment": 1226.507403,
        "principalBalance": 2905822.137923,
        "principalPayment": 37795.629004,
        "endPrincipalBalance": 2905822.137923,
        "beginPrincipalBalance": 2943617.766926,
        "prepayPrincipalPayment": 22258.772716,
        "scheduledPrincipalPayment": 15536.856287
    }
    {
        "date": "2039-10-25",
        "totalCashFlow": 36159.709427,
        "interestPayment": 1210.759224,
        "principalBalance": 2870873.18772,
        "principalPayment": 34948.950203,
        "endPrincipalBalance": 2870873.18772,
        "beginPrincipalBalance": 2905822.137923,
        "prepayPrincipalPayment": 19514.141257,
        "scheduledPrincipalPayment": 15434.808946
    }
    {
        "date": "2039-11-25",
        "totalCashFlow": 34103.673156,
        "interestPayment": 1196.197162,
        "principalBalance": 2837965.711726,
        "principalPayment": 32907.475994,
        "endPrincipalBalance": 2837965.711726,
        "beginPrincipalBalance": 2870873.18772,
        "prepayPrincipalPayment": 17560.904134,
        "scheduledPrincipalPayment": 15346.57186
    }
    {
        "date": "2039-12-25",
        "totalCashFlow": 33646.840683,
        "interestPayment": 1182.485713,
        "principalBalance": 2805501.356756,
        "principalPayment": 32464.35497,
        "endPrincipalBalance": 2805501.356756,
        "beginPrincipalBalance": 2837965.711726,
        "prepayPrincipalPayment": 17196.273684,
        "scheduledPrincipalPayment": 15268.081286
    }
    {
        "date": "2040-01-25",
        "totalCashFlow": 33547.017347,
        "interestPayment": 1168.958899,
        "principalBalance": 2773123.298308,
        "principalPayment": 32378.058448,
        "endPrincipalBalance": 2773123.298308,
        "beginPrincipalBalance": 2805501.356756,
        "prepayPrincipalPayment": 17187.185115,
        "scheduledPrincipalPayment": 15190.873333
    }
    {
        "date": "2040-02-25",
        "totalCashFlow": 29601.916925,
        "interestPayment": 1155.468041,
        "principalBalance": 2744676.849424,
        "principalPayment": 28446.448884,
        "endPrincipalBalance": 2744676.849424,
        "beginPrincipalBalance": 2773123.298308,
        "prepayPrincipalPayment": 13333.418835,
        "scheduledPrincipalPayment": 15113.030049
    }
    {
        "date": "2040-03-25",
        "totalCashFlow": 30267.269444,
        "interestPayment": 1143.615354,
        "principalBalance": 2715553.195334,
        "principalPayment": 29123.65409,
        "endPrincipalBalance": 2715553.195334,
        "beginPrincipalBalance": 2744676.849424,
        "prepayPrincipalPayment": 14068.020355,
        "scheduledPrincipalPayment": 15055.633734
    }
    {
        "date": "2040-04-25",
        "totalCashFlow": 32713.670347,
        "interestPayment": 1131.480498,
        "principalBalance": 2683971.005485,
        "principalPayment": 31582.189849,
        "endPrincipalBalance": 2683971.005485,
        "beginPrincipalBalance": 2715553.195334,
        "prepayPrincipalPayment": 16588.548259,
        "scheduledPrincipalPayment": 14993.64159
    }
    {
        "date": "2040-05-25",
        "totalCashFlow": 34077.116898,
        "interestPayment": 1118.321252,
        "principalBalance": 2651012.209839,
        "principalPayment": 32958.795645,
        "endPrincipalBalance": 2651012.209839,
        "beginPrincipalBalance": 2683971.005485,
        "prepayPrincipalPayment": 18041.732065,
        "scheduledPrincipalPayment": 14917.06358
    }
    {
        "date": "2040-06-25",
        "totalCashFlow": 36429.695317,
        "interestPayment": 1104.588421,
        "principalBalance": 2615687.102943,
        "principalPayment": 35325.106896,
        "endPrincipalBalance": 2615687.102943,
        "beginPrincipalBalance": 2651012.209839,
        "prepayPrincipalPayment": 20493.443099,
        "scheduledPrincipalPayment": 14831.663798
    }
    {
        "date": "2040-07-25",
        "totalCashFlow": 36067.227276,
        "interestPayment": 1089.869626,
        "principalBalance": 2580709.745293,
        "principalPayment": 34977.35765,
        "endPrincipalBalance": 2580709.745293,
        "beginPrincipalBalance": 2615687.102943,
        "prepayPrincipalPayment": 20245.664398,
        "scheduledPrincipalPayment": 14731.693252
    }
    {
        "date": "2040-08-25",
        "totalCashFlow": 35398.172053,
        "interestPayment": 1075.295727,
        "principalBalance": 2546386.868968,
        "principalPayment": 34322.876326,
        "endPrincipalBalance": 2546386.868968,
        "beginPrincipalBalance": 2580709.745293,
        "prepayPrincipalPayment": 19690.627531,
        "scheduledPrincipalPayment": 14632.248794
    }
    {
        "date": "2040-09-25",
        "totalCashFlow": 35956.807875,
        "interestPayment": 1060.994529,
        "principalBalance": 2511491.055622,
        "principalPayment": 34895.813346,
        "endPrincipalBalance": 2511491.055622,
        "beginPrincipalBalance": 2546386.868968,
        "prepayPrincipalPayment": 20360.719186,
        "scheduledPrincipalPayment": 14535.09416
    }
    {
        "date": "2040-10-25",
        "totalCashFlow": 31830.123939,
        "interestPayment": 1046.454607,
        "principalBalance": 2480707.386289,
        "principalPayment": 30783.669333,
        "endPrincipalBalance": 2480707.386289,
        "beginPrincipalBalance": 2511491.055622,
        "prepayPrincipalPayment": 16350.444952,
        "scheduledPrincipalPayment": 14433.224381
    }
    {
        "date": "2040-11-25",
        "totalCashFlow": 32815.802359,
        "interestPayment": 1033.628078,
        "principalBalance": 2448925.212008,
        "principalPayment": 31782.174281,
        "endPrincipalBalance": 2448925.212008,
        "beginPrincipalBalance": 2480707.386289,
        "prepayPrincipalPayment": 17428.520815,
        "scheduledPrincipalPayment": 14353.653466
    }
    {
        "date": "2040-12-25",
        "totalCashFlow": 30997.524237,
        "interestPayment": 1020.385505,
        "principalBalance": 2418948.073276,
        "principalPayment": 29977.138732,
        "endPrincipalBalance": 2418948.073276,
        "beginPrincipalBalance": 2448925.212008,
        "prepayPrincipalPayment": 15710.069479,
        "scheduledPrincipalPayment": 14267.069253
    }
    {
        "date": "2041-01-25",
        "totalCashFlow": 30232.634645,
        "interestPayment": 1007.895031,
        "principalBalance": 2389723.333662,
        "principalPayment": 29224.739615,
        "endPrincipalBalance": 2389723.333662,
        "beginPrincipalBalance": 2418948.073276,
        "prepayPrincipalPayment": 15034.965558,
        "scheduledPrincipalPayment": 14189.774056
    }
    {
        "date": "2041-02-25",
        "totalCashFlow": 27797.515588,
        "interestPayment": 995.718056,
        "principalBalance": 2362921.536129,
        "principalPayment": 26801.797533,
        "endPrincipalBalance": 2362921.536129,
        "beginPrincipalBalance": 2389723.333662,
        "prepayPrincipalPayment": 12686.051801,
        "scheduledPrincipalPayment": 14115.745732
    }
    {
        "date": "2041-03-25",
        "totalCashFlow": 27347.155821,
        "interestPayment": 984.55064,
        "principalBalance": 2336558.930948,
        "principalPayment": 26362.605181,
        "endPrincipalBalance": 2336558.930948,
        "beginPrincipalBalance": 2362921.536129,
        "prepayPrincipalPayment": 12307.613976,
        "scheduledPrincipalPayment": 14054.991205
    }
    {
        "date": "2041-04-25",
        "totalCashFlow": 29746.940035,
        "interestPayment": 973.566221,
        "principalBalance": 2307785.557134,
        "principalPayment": 28773.373814,
        "endPrincipalBalance": 2307785.557134,
        "beginPrincipalBalance": 2336558.930948,
        "prepayPrincipalPayment": 14777.464189,
        "scheduledPrincipalPayment": 13995.909625
    }
    {
        "date": "2041-05-25",
        "totalCashFlow": 31585.391852,
        "interestPayment": 961.577315,
        "principalBalance": 2277161.742598,
        "principalPayment": 30623.814536,
        "endPrincipalBalance": 2277161.742598,
        "beginPrincipalBalance": 2307785.557134,
        "prepayPrincipalPayment": 16702.46852,
        "scheduledPrincipalPayment": 13921.346017
    }
    {
        "date": "2041-06-25",
        "totalCashFlow": 33309.672079,
        "interestPayment": 948.817393,
        "principalBalance": 2244800.887912,
        "principalPayment": 32360.854686,
        "endPrincipalBalance": 2244800.887912,
        "beginPrincipalBalance": 2277161.742598,
        "prepayPrincipalPayment": 18526.479295,
        "scheduledPrincipalPayment": 13834.375391
    }
    {
        "date": "2041-07-25",
        "totalCashFlow": 32145.593043,
        "interestPayment": 935.333703,
        "principalBalance": 2213590.628572,
        "principalPayment": 31210.259339,
        "endPrincipalBalance": 2213590.628572,
        "beginPrincipalBalance": 2244800.887912,
        "prepayPrincipalPayment": 17474.83246,
        "scheduledPrincipalPayment": 13735.426879
    }
    {
        "date": "2041-08-25",
        "totalCashFlow": 33062.86634,
        "interestPayment": 922.329429,
        "principalBalance": 2181450.091661,
        "principalPayment": 32140.536911,
        "endPrincipalBalance": 2181450.091661,
        "beginPrincipalBalance": 2213590.628572,
        "prepayPrincipalPayment": 18498.497168,
        "scheduledPrincipalPayment": 13642.039744
    }
    {
        "date": "2041-09-25",
        "totalCashFlow": 32038.59487,
        "interestPayment": 908.937538,
        "principalBalance": 2150320.434329,
        "principalPayment": 31129.657332,
        "endPrincipalBalance": 2150320.434329,
        "beginPrincipalBalance": 2181450.091661,
        "prepayPrincipalPayment": 17588.237134,
        "scheduledPrincipalPayment": 13541.420198
    }
    {
        "date": "2041-10-25",
        "totalCashFlow": 29719.56796,
        "interestPayment": 895.966848,
        "principalBalance": 2121496.833217,
        "principalPayment": 28823.601112,
        "endPrincipalBalance": 2121496.833217,
        "beginPrincipalBalance": 2150320.434329,
        "prepayPrincipalPayment": 15378.051213,
        "scheduledPrincipalPayment": 13445.549899
    }
    {
        "date": "2041-11-25",
        "totalCashFlow": 29879.438934,
        "interestPayment": 883.957014,
        "principalBalance": 2092501.351297,
        "principalPayment": 28995.48192,
        "endPrincipalBalance": 2092501.351297,
        "beginPrincipalBalance": 2121496.833217,
        "prepayPrincipalPayment": 15632.788128,
        "scheduledPrincipalPayment": 13362.693792
    }
    {
        "date": "2041-12-25",
        "totalCashFlow": 27640.078237,
        "interestPayment": 871.875563,
        "principalBalance": 2065733.148623,
        "principalPayment": 26768.202674,
        "endPrincipalBalance": 2065733.148623,
        "beginPrincipalBalance": 2092501.351297,
        "prepayPrincipalPayment": 13490.783174,
        "scheduledPrincipalPayment": 13277.419501
    }
    {
        "date": "2042-01-25",
        "totalCashFlow": 28100.736751,
        "interestPayment": 860.722145,
        "principalBalance": 2038493.134017,
        "principalPayment": 27240.014606,
        "endPrincipalBalance": 2038493.134017,
        "beginPrincipalBalance": 2065733.148623,
        "prepayPrincipalPayment": 14035.003066,
        "scheduledPrincipalPayment": 13205.01154
    }
    {
        "date": "2042-02-25",
        "totalCashFlow": 25351.089324,
        "interestPayment": 849.372139,
        "principalBalance": 2013991.416832,
        "principalPayment": 24501.717185,
        "endPrincipalBalance": 2013991.416832,
        "beginPrincipalBalance": 2038493.134017,
        "prepayPrincipalPayment": 11373.339165,
        "scheduledPrincipalPayment": 13128.37802
    }
    {
        "date": "2042-03-25",
        "totalCashFlow": 24928.628397,
        "interestPayment": 839.16309,
        "principalBalance": 1989901.951525,
        "principalPayment": 24089.465307,
        "endPrincipalBalance": 1989901.951525,
        "beginPrincipalBalance": 2013991.416832,
        "prepayPrincipalPayment": 11021.210467,
        "scheduledPrincipalPayment": 13068.25484
    }
    {
        "date": "2042-04-25",
        "totalCashFlow": 27004.194757,
        "interestPayment": 829.125813,
        "principalBalance": 1963726.882581,
        "principalPayment": 26175.068944,
        "endPrincipalBalance": 1963726.882581,
        "beginPrincipalBalance": 1989901.951525,
        "prepayPrincipalPayment": 13165.257087,
        "scheduledPrincipalPayment": 13009.811857
    }
    {
        "date": "2042-05-25",
        "totalCashFlow": 28878.794295,
        "interestPayment": 818.219534,
        "principalBalance": 1935666.307821,
        "principalPayment": 28060.574761,
        "endPrincipalBalance": 1935666.307821,
        "beginPrincipalBalance": 1963726.882581,
        "prepayPrincipalPayment": 15123.941055,
        "scheduledPrincipalPayment": 12936.633705
    }
    {
        "date": "2042-06-25",
        "totalCashFlow": 29389.496558,
        "interestPayment": 806.527628,
        "principalBalance": 1907083.338891,
        "principalPayment": 28582.96893,
        "endPrincipalBalance": 1907083.338891,
        "beginPrincipalBalance": 1935666.307821,
        "prepayPrincipalPayment": 15733.258206,
        "scheduledPrincipalPayment": 12849.710724
    }
    {
        "date": "2042-07-25",
        "totalCashFlow": 29693.792698,
        "interestPayment": 794.618058,
        "principalBalance": 1878184.164251,
        "principalPayment": 28899.174641,
        "endPrincipalBalance": 1878184.164251,
        "beginPrincipalBalance": 1907083.338891,
        "prepayPrincipalPayment": 16141.329821,
        "scheduledPrincipalPayment": 12757.844819
    }
    {
        "date": "2042-08-25",
        "totalCashFlow": 29747.748473,
        "interestPayment": 782.576735,
        "principalBalance": 1849218.992512,
        "principalPayment": 28965.171738,
        "endPrincipalBalance": 1849218.992512,
        "beginPrincipalBalance": 1878184.164251,
        "prepayPrincipalPayment": 16302.858864,
        "scheduledPrincipalPayment": 12662.312874
    }
    {
        "date": "2042-09-25",
        "totalCashFlow": 28200.53265,
        "interestPayment": 770.507914,
        "principalBalance": 1821788.967776,
        "principalPayment": 27430.024737,
        "endPrincipalBalance": 1821788.967776,
        "beginPrincipalBalance": 1849218.992512,
        "prepayPrincipalPayment": 14865.293603,
        "scheduledPrincipalPayment": 12564.731134
    }
    {
        "date": "2042-10-25",
        "totalCashFlow": 27352.694639,
        "interestPayment": 759.078737,
        "principalBalance": 1795195.351873,
        "principalPayment": 26593.615903,
        "endPrincipalBalance": 1795195.351873,
        "beginPrincipalBalance": 1821788.967776,
        "prepayPrincipalPayment": 14117.597365,
        "scheduledPrincipalPayment": 12476.018538
    }
    {
        "date": "2042-11-25",
        "totalCashFlow": 26870.54728,
        "interestPayment": 747.998063,
        "principalBalance": 1769072.802656,
        "principalPayment": 26122.549217,
        "endPrincipalBalance": 1769072.802656,
        "beginPrincipalBalance": 1795195.351873,
        "prepayPrincipalPayment": 13730.983351,
        "scheduledPrincipalPayment": 12391.565866
    }
    {
        "date": "2042-12-25",
        "totalCashFlow": 24390.87582,
        "interestPayment": 737.113668,
        "principalBalance": 1745419.040504,
        "principalPayment": 23653.762152,
        "endPrincipalBalance": 1745419.040504,
        "beginPrincipalBalance": 1769072.802656,
        "prepayPrincipalPayment": 11344.826468,
        "scheduledPrincipalPayment": 12308.935683
    }
    {
        "date": "2043-01-25",
        "totalCashFlow": 25765.893417,
        "interestPayment": 727.257934,
        "principalBalance": 1720380.405021,
        "principalPayment": 25038.635483,
        "endPrincipalBalance": 1720380.405021,
        "beginPrincipalBalance": 1745419.040504,
        "prepayPrincipalPayment": 12796.449414,
        "scheduledPrincipalPayment": 12242.186069
    }
    {
        "date": "2043-02-25",
        "totalCashFlow": 22503.312682,
        "interestPayment": 716.825169,
        "principalBalance": 1698593.917508,
        "principalPayment": 21786.487514,
        "endPrincipalBalance": 1698593.917508,
        "beginPrincipalBalance": 1720380.405021,
        "prepayPrincipalPayment": 9622.030239,
        "scheduledPrincipalPayment": 12164.457274
    }
    {
        "date": "2043-03-25",
        "totalCashFlow": 22491.948413,
        "interestPayment": 707.747466,
        "principalBalance": 1676809.71656,
        "principalPayment": 21784.200948,
        "endPrincipalBalance": 1676809.71656,
        "beginPrincipalBalance": 1698593.917508,
        "prepayPrincipalPayment": 9675.663633,
        "scheduledPrincipalPayment": 12108.537315
    }
    {
        "date": "2043-04-25",
        "totalCashFlow": 24469.84531,
        "interestPayment": 698.670715,
        "principalBalance": 1653038.541965,
        "principalPayment": 23771.174595,
        "endPrincipalBalance": 1653038.541965,
        "beginPrincipalBalance": 1676809.71656,
        "prepayPrincipalPayment": 11719.565394,
        "scheduledPrincipalPayment": 12051.6092
    }
    {
        "date": "2043-05-25",
        "totalCashFlow": 25814.123919,
        "interestPayment": 688.766059,
        "principalBalance": 1627913.184105,
        "principalPayment": 25125.35786,
        "endPrincipalBalance": 1627913.184105,
        "beginPrincipalBalance": 1653038.541965,
        "prepayPrincipalPayment": 13146.124204,
        "scheduledPrincipalPayment": 11979.233656
    }
    {
        "date": "2043-06-25",
        "totalCashFlow": 25653.933773,
        "interestPayment": 678.29716,
        "principalBalance": 1602937.547492,
        "principalPayment": 24975.636613,
        "endPrincipalBalance": 1602937.547492,
        "beginPrincipalBalance": 1627913.184105,
        "prepayPrincipalPayment": 13079.987257,
        "scheduledPrincipalPayment": 11895.649357
    }
    {
        "date": "2043-07-25",
        "totalCashFlow": 27028.211923,
        "interestPayment": 667.890645,
        "principalBalance": 1576577.226214,
        "principalPayment": 26360.321278,
        "endPrincipalBalance": 1576577.226214,
        "beginPrincipalBalance": 1602937.547492,
        "prepayPrincipalPayment": 14548.663869,
        "scheduledPrincipalPayment": 11811.657409
    }
    {
        "date": "2043-08-25",
        "totalCashFlow": 26431.063104,
        "interestPayment": 656.907178,
        "principalBalance": 1550803.070287,
        "principalPayment": 25774.155927,
        "endPrincipalBalance": 1550803.070287,
        "beginPrincipalBalance": 1576577.226214,
        "prepayPrincipalPayment": 14058.308615,
        "scheduledPrincipalPayment": 11715.847312
    }
    {
        "date": "2043-09-25",
        "totalCashFlow": 25081.186524,
        "interestPayment": 646.167946,
        "principalBalance": 1526368.051709,
        "principalPayment": 24435.018578,
        "endPrincipalBalance": 1526368.051709,
        "beginPrincipalBalance": 1550803.070287,
        "prepayPrincipalPayment": 12812.329029,
        "scheduledPrincipalPayment": 11622.689549
    }
    {
        "date": "2043-10-25",
        "totalCashFlow": 24328.886761,
        "interestPayment": 635.986688,
        "principalBalance": 1502675.151636,
        "principalPayment": 23692.900073,
        "endPrincipalBalance": 1502675.151636,
        "beginPrincipalBalance": 1526368.051709,
        "prepayPrincipalPayment": 12154.95305,
        "scheduledPrincipalPayment": 11537.947023
    }
    {
        "date": "2043-11-25",
        "totalCashFlow": 23448.659548,
        "interestPayment": 626.114647,
        "principalBalance": 1479852.606734,
        "principalPayment": 22822.544902,
        "endPrincipalBalance": 1479852.606734,
        "beginPrincipalBalance": 1502675.151636,
        "prepayPrincipalPayment": 11365.255775,
        "scheduledPrincipalPayment": 11457.289126
    }
    {
        "date": "2043-12-25",
        "totalCashFlow": 22204.836817,
        "interestPayment": 616.605253,
        "principalBalance": 1458264.37517,
        "principalPayment": 21588.231564,
        "endPrincipalBalance": 1458264.37517,
        "beginPrincipalBalance": 1479852.606734,
        "prepayPrincipalPayment": 10206.41998,
        "scheduledPrincipalPayment": 11381.811584
    }
    {
        "date": "2044-01-25",
        "totalCashFlow": 22894.646676,
        "interestPayment": 607.610156,
        "principalBalance": 1435977.338651,
        "principalPayment": 22287.036519,
        "endPrincipalBalance": 1435977.338651,
        "beginPrincipalBalance": 1458264.37517,
        "prepayPrincipalPayment": 10972.559123,
        "scheduledPrincipalPayment": 11314.477396
    }
    {
        "date": "2044-02-25",
        "totalCashFlow": 19813.534953,
        "interestPayment": 598.323891,
        "principalBalance": 1416762.127589,
        "principalPayment": 19215.211062,
        "endPrincipalBalance": 1416762.127589,
        "beginPrincipalBalance": 1435977.338651,
        "prepayPrincipalPayment": 7974.837452,
        "scheduledPrincipalPayment": 11240.373609
    }
    {
        "date": "2044-03-25",
        "totalCashFlow": 20428.102309,
        "interestPayment": 590.317553,
        "principalBalance": 1396924.342834,
        "principalPayment": 19837.784756,
        "endPrincipalBalance": 1396924.342834,
        "beginPrincipalBalance": 1416762.127589,
        "prepayPrincipalPayment": 8648.684946,
        "scheduledPrincipalPayment": 11189.099809
    }
    {
        "date": "2044-04-25",
        "totalCashFlow": 22269.580479,
        "interestPayment": 582.05181,
        "principalBalance": 1375236.814164,
        "principalPayment": 21687.52867,
        "endPrincipalBalance": 1375236.814164,
        "beginPrincipalBalance": 1396924.342834,
        "prepayPrincipalPayment": 10555.693341,
        "scheduledPrincipalPayment": 11131.835329
    }
    {
        "date": "2044-05-25",
        "totalCashFlow": 22146.471175,
        "interestPayment": 573.015339,
        "principalBalance": 1353663.358329,
        "principalPayment": 21573.455835,
        "endPrincipalBalance": 1353663.358329,
        "beginPrincipalBalance": 1375236.814164,
        "prepayPrincipalPayment": 10514.905258,
        "scheduledPrincipalPayment": 11058.550577
    }
    {
        "date": "2044-06-25",
        "totalCashFlow": 23068.541019,
        "interestPayment": 564.026399,
        "principalBalance": 1331158.843709,
        "principalPayment": 22504.51462,
        "endPrincipalBalance": 1331158.843709,
        "beginPrincipalBalance": 1353663.358329,
        "prepayPrincipalPayment": 11519.771351,
        "scheduledPrincipalPayment": 10984.743269
    }
    {
        "date": "2044-07-25",
        "totalCashFlow": 23684.193336,
        "interestPayment": 554.649518,
        "principalBalance": 1308029.299891,
        "principalPayment": 23129.543818,
        "endPrincipalBalance": 1308029.299891,
        "beginPrincipalBalance": 1331158.843709,
        "prepayPrincipalPayment": 12227.702014,
        "scheduledPrincipalPayment": 10901.841804
    }
    {
        "date": "2044-08-25",
        "totalCashFlow": 22252.063102,
        "interestPayment": 545.012208,
        "principalBalance": 1286322.248997,
        "principalPayment": 21707.050894,
        "endPrincipalBalance": 1286322.248997,
        "beginPrincipalBalance": 1308029.299891,
        "prepayPrincipalPayment": 10894.926759,
        "scheduledPrincipalPayment": 10812.124135
    }
    {
        "date": "2044-09-25",
        "totalCashFlow": 22869.015094,
        "interestPayment": 535.967604,
        "principalBalance": 1263989.201506,
        "principalPayment": 22333.04749,
        "endPrincipalBalance": 1263989.201506,
        "beginPrincipalBalance": 1286322.248997,
        "prepayPrincipalPayment": 11600.563012,
        "scheduledPrincipalPayment": 10732.484479
    }
    {
        "date": "2044-10-25",
        "totalCashFlow": 21367.787698,
        "interestPayment": 526.662167,
        "principalBalance": 1243148.075975,
        "principalPayment": 20841.125531,
        "endPrincipalBalance": 1243148.075975,
        "beginPrincipalBalance": 1263989.201506,
        "prepayPrincipalPayment": 10195.167208,
        "scheduledPrincipalPayment": 10645.958323
    }
    {
        "date": "2044-11-25",
        "totalCashFlow": 20279.691057,
        "interestPayment": 517.978365,
        "principalBalance": 1223386.363283,
        "principalPayment": 19761.712692,
        "endPrincipalBalance": 1223386.363283,
        "beginPrincipalBalance": 1243148.075975,
        "prepayPrincipalPayment": 9191.353281,
        "scheduledPrincipalPayment": 10570.359412
    }
    {
        "date": "2044-12-25",
        "totalCashFlow": 19955.604039,
        "interestPayment": 509.744318,
        "principalBalance": 1203940.503562,
        "principalPayment": 19445.859721,
        "endPrincipalBalance": 1203940.503562,
        "beginPrincipalBalance": 1223386.363283,
        "prepayPrincipalPayment": 8943.394979,
        "scheduledPrincipalPayment": 10502.464743
    }
    {
        "date": "2045-01-25",
        "totalCashFlow": 19795.822771,
        "interestPayment": 501.641876,
        "principalBalance": 1184646.322667,
        "principalPayment": 19294.180894,
        "endPrincipalBalance": 1184646.322667,
        "beginPrincipalBalance": 1203940.503562,
        "prepayPrincipalPayment": 8858.29837,
        "scheduledPrincipalPayment": 10435.882525
    }
    {
        "date": "2045-02-25",
        "totalCashFlow": 17923.54704,
        "interestPayment": 493.602634,
        "principalBalance": 1167216.378262,
        "principalPayment": 17429.944405,
        "endPrincipalBalance": 1167216.378262,
        "beginPrincipalBalance": 1184646.322667,
        "prepayPrincipalPayment": 7060.727909,
        "scheduledPrincipalPayment": 10369.216496
    }
    {
        "date": "2045-03-25",
        "totalCashFlow": 17876.974969,
        "interestPayment": 486.340158,
        "principalBalance": 1149825.74345,
        "principalPayment": 17390.634812,
        "endPrincipalBalance": 1149825.74345,
        "beginPrincipalBalance": 1167216.378262,
        "prepayPrincipalPayment": 7073.030325,
        "scheduledPrincipalPayment": 10317.604487
    }
    {
        "date": "2045-04-25",
        "totalCashFlow": 19549.14613,
        "interestPayment": 479.09406,
        "principalBalance": 1130755.69138,
        "principalPayment": 19070.05207,
        "endPrincipalBalance": 1130755.69138,
        "beginPrincipalBalance": 1149825.74345,
        "prepayPrincipalPayment": 8804.845402,
        "scheduledPrincipalPayment": 10265.206669
    }
    {
        "date": "2045-05-25",
        "totalCashFlow": 19262.31343,
        "interestPayment": 471.148205,
        "principalBalance": 1111964.526155,
        "principalPayment": 18791.165226,
        "endPrincipalBalance": 1111964.526155,
        "beginPrincipalBalance": 1130755.69138,
        "prepayPrincipalPayment": 8594.66265,
        "scheduledPrincipalPayment": 10196.502575
    }
    {
        "date": "2045-06-25",
        "totalCashFlow": 20470.10121,
        "interestPayment": 463.318553,
        "principalBalance": 1091957.743497,
        "principalPayment": 20006.782657,
        "endPrincipalBalance": 1091957.743497,
        "beginPrincipalBalance": 1111964.526155,
        "prepayPrincipalPayment": 9877.947126,
        "scheduledPrincipalPayment": 10128.835531
    }
    {
        "date": "2045-07-25",
        "totalCashFlow": 20553.464291,
        "interestPayment": 454.982393,
        "principalBalance": 1071859.261599,
        "principalPayment": 20098.481898,
        "endPrincipalBalance": 1071859.261599,
        "beginPrincipalBalance": 1091957.743497,
        "prepayPrincipalPayment": 10049.995005,
        "scheduledPrincipalPayment": 10048.486893
    }
    {
        "date": "2045-08-25",
        "totalCashFlow": 19412.240776,
        "interestPayment": 446.608026,
        "principalBalance": 1052893.628849,
        "principalPayment": 18965.63275,
        "endPrincipalBalance": 1052893.628849,
        "beginPrincipalBalance": 1071859.261599,
        "prepayPrincipalPayment": 9000.117608,
        "scheduledPrincipalPayment": 9965.515142
    }
    {
        "date": "2045-09-25",
        "totalCashFlow": 19859.413809,
        "interestPayment": 438.705679,
        "principalBalance": 1033472.920718,
        "principalPayment": 19420.70813,
        "endPrincipalBalance": 1033472.920718,
        "beginPrincipalBalance": 1052893.628849,
        "prepayPrincipalPayment": 9529.363298,
        "scheduledPrincipalPayment": 9891.344832
    }
    {
        "date": "2045-10-25",
        "totalCashFlow": 18367.182342,
        "interestPayment": 430.613717,
        "principalBalance": 1015536.352093,
        "principalPayment": 17936.568625,
        "endPrincipalBalance": 1015536.352093,
        "beginPrincipalBalance": 1033472.920718,
        "prepayPrincipalPayment": 8125.386462,
        "scheduledPrincipalPayment": 9811.182163
    }
    {
        "date": "2045-11-25",
        "totalCashFlow": 18074.068613,
        "interestPayment": 423.140147,
        "principalBalance": 997885.423627,
        "principalPayment": 17650.928466,
        "endPrincipalBalance": 997885.423627,
        "beginPrincipalBalance": 1015536.352093,
        "prepayPrincipalPayment": 7907.484386,
        "scheduledPrincipalPayment": 9743.44408
    }
    {
        "date": "2045-12-25",
        "totalCashFlow": 17521.726637,
        "interestPayment": 415.785593,
        "principalBalance": 980779.482583,
        "principalPayment": 17105.941043,
        "endPrincipalBalance": 980779.482583,
        "beginPrincipalBalance": 997885.423627,
        "prepayPrincipalPayment": 7429.029718,
        "scheduledPrincipalPayment": 9676.911326
    }
    {
        "date": "2046-01-25",
        "totalCashFlow": 17122.460023,
        "interestPayment": 408.658118,
        "principalBalance": 964065.680678,
        "principalPayment": 16713.801905,
        "endPrincipalBalance": 964065.680678,
        "beginPrincipalBalance": 980779.482583,
        "prepayPrincipalPayment": 7099.63411,
        "scheduledPrincipalPayment": 9614.167795
    }
    {
        "date": "2046-02-25",
        "totalCashFlow": 16095.707746,
        "interestPayment": 401.694034,
        "principalBalance": 948371.666966,
        "principalPayment": 15694.013712,
        "endPrincipalBalance": 948371.666966,
        "beginPrincipalBalance": 964065.680678,
        "prepayPrincipalPayment": 6140.188052,
        "scheduledPrincipalPayment": 9553.82566
    }
    {
        "date": "2046-03-25",
        "totalCashFlow": 15842.52566,
        "interestPayment": 395.154861,
        "principalBalance": 932924.296167,
        "principalPayment": 15447.370799,
        "endPrincipalBalance": 932924.296167,
        "beginPrincipalBalance": 948371.666966,
        "prepayPrincipalPayment": 5945.115148,
        "scheduledPrincipalPayment": 9502.255651
    }
    {
        "date": "2046-04-25",
        "totalCashFlow": 16759.557413,
        "interestPayment": 388.718457,
        "principalBalance": 916553.457211,
        "principalPayment": 16370.838956,
        "endPrincipalBalance": 916553.457211,
        "beginPrincipalBalance": 932924.296167,
        "prepayPrincipalPayment": 6918.918046,
        "scheduledPrincipalPayment": 9451.92091
    }
    {
        "date": "2046-05-25",
        "totalCashFlow": 17090.740912,
        "interestPayment": 381.897274,
        "principalBalance": 899844.613573,
        "principalPayment": 16708.843638,
        "endPrincipalBalance": 899844.613573,
        "beginPrincipalBalance": 916553.457211,
        "prepayPrincipalPayment": 7317.967227,
        "scheduledPrincipalPayment": 9390.87641
    }
    {
        "date": "2046-06-25",
        "totalCashFlow": 17721.277861,
        "interestPayment": 374.935256,
        "principalBalance": 882498.270968,
        "principalPayment": 17346.342605,
        "endPrincipalBalance": 882498.270968,
        "beginPrincipalBalance": 899844.613573,
        "prepayPrincipalPayment": 8021.51797,
        "scheduledPrincipalPayment": 9324.824635
    }
    {
        "date": "2046-07-25",
        "totalCashFlow": 17462.819157,
        "interestPayment": 367.707613,
        "principalBalance": 865403.159424,
        "principalPayment": 17095.111544,
        "endPrincipalBalance": 865403.159424,
        "beginPrincipalBalance": 882498.270968,
        "prepayPrincipalPayment": 7844.656088,
        "scheduledPrincipalPayment": 9250.455456
    }
    {
        "date": "2046-08-25",
        "totalCashFlow": 17113.287736,
        "interestPayment": 360.58465,
        "principalBalance": 848650.456338,
        "principalPayment": 16752.703086,
        "endPrincipalBalance": 848650.456338,
        "beginPrincipalBalance": 865403.159424,
        "prepayPrincipalPayment": 7575.798013,
        "scheduledPrincipalPayment": 9176.905073
    }
    {
        "date": "2046-09-25",
        "totalCashFlow": 17148.362216,
        "interestPayment": 353.604357,
        "principalBalance": 831855.698479,
        "principalPayment": 16794.757859,
        "endPrincipalBalance": 831855.698479,
        "beginPrincipalBalance": 848650.456338,
        "prepayPrincipalPayment": 7689.574361,
        "scheduledPrincipalPayment": 9105.183498
    }
    {
        "date": "2046-10-25",
        "totalCashFlow": 15763.410586,
        "interestPayment": 346.606541,
        "principalBalance": 816438.894434,
        "principalPayment": 15416.804045,
        "endPrincipalBalance": 816438.894434,
        "beginPrincipalBalance": 831855.698479,
        "prepayPrincipalPayment": 6385.619171,
        "scheduledPrincipalPayment": 9031.184874
    }
    {
        "date": "2046-11-25",
        "totalCashFlow": 15944.739935,
        "interestPayment": 340.182873,
        "principalBalance": 800834.337372,
        "principalPayment": 15604.557062,
        "endPrincipalBalance": 800834.337372,
        "beginPrincipalBalance": 816438.894434,
        "prepayPrincipalPayment": 6634.125205,
        "scheduledPrincipalPayment": 8970.431857
    }
    {
        "date": "2046-12-25",
        "totalCashFlow": 15292.626009,
        "interestPayment": 333.680974,
        "principalBalance": 785875.392337,
        "principalPayment": 14958.945035,
        "endPrincipalBalance": 785875.392337,
        "beginPrincipalBalance": 800834.337372,
        "prepayPrincipalPayment": 6052.946421,
        "scheduledPrincipalPayment": 8905.998614
    }
    {
        "date": "2047-01-25",
        "totalCashFlow": 14965.158025,
        "interestPayment": 327.44808,
        "principalBalance": 771237.682392,
        "principalPayment": 14637.709944,
        "endPrincipalBalance": 771237.682392,
        "beginPrincipalBalance": 785875.392337,
        "prepayPrincipalPayment": 5790.576381,
        "scheduledPrincipalPayment": 8847.133563
    }
    {
        "date": "2047-02-25",
        "totalCashFlow": 14172.724877,
        "interestPayment": 321.349034,
        "principalBalance": 757386.30655,
        "principalPayment": 13851.375842,
        "endPrincipalBalance": 757386.30655,
        "beginPrincipalBalance": 771237.682392,
        "prepayPrincipalPayment": 5061.025874,
        "scheduledPrincipalPayment": 8790.349968
    }
    {
        "date": "2047-03-25",
        "totalCashFlow": 13958.021755,
        "interestPayment": 315.577628,
        "principalBalance": 743743.862423,
        "principalPayment": 13642.444127,
        "endPrincipalBalance": 743743.862423,
        "beginPrincipalBalance": 757386.30655,
        "prepayPrincipalPayment": 4901.347521,
        "scheduledPrincipalPayment": 8741.096606
    }
    {
        "date": "2047-04-25",
        "totalCashFlow": 14530.329715,
        "interestPayment": 309.893276,
        "principalBalance": 729523.425983,
        "principalPayment": 14220.436439,
        "endPrincipalBalance": 729523.425983,
        "beginPrincipalBalance": 743743.862423,
        "prepayPrincipalPayment": 5527.521714,
        "scheduledPrincipalPayment": 8692.914725
    }
    {
        "date": "2047-05-25",
        "totalCashFlow": 14920.817459,
        "interestPayment": 303.968094,
        "principalBalance": 714906.576619,
        "principalPayment": 14616.849364,
        "endPrincipalBalance": 714906.576619,
        "beginPrincipalBalance": 729523.425983,
        "prepayPrincipalPayment": 5980.317606,
        "scheduledPrincipalPayment": 8636.531758
    }
    {
        "date": "2047-06-25",
        "totalCashFlow": 15261.361701,
        "interestPayment": 297.87774,
        "principalBalance": 699943.092658,
        "principalPayment": 14963.483961,
        "endPrincipalBalance": 699943.092658,
        "beginPrincipalBalance": 714906.576619,
        "prepayPrincipalPayment": 6389.677197,
        "scheduledPrincipalPayment": 8573.806764
    }
    {
        "date": "2047-07-25",
        "totalCashFlow": 14829.787835,
        "interestPayment": 291.642955,
        "principalBalance": 685404.947778,
        "principalPayment": 14538.14488,
        "endPrincipalBalance": 685404.947778,
        "beginPrincipalBalance": 699943.092658,
        "prepayPrincipalPayment": 6033.048834,
        "scheduledPrincipalPayment": 8505.096046
    }
    {
        "date": "2047-08-25",
        "totalCashFlow": 14945.867692,
        "interestPayment": 285.585395,
        "principalBalance": 670744.66548,
        "principalPayment": 14660.282297,
        "endPrincipalBalance": 670744.66548,
        "beginPrincipalBalance": 685404.947778,
        "prepayPrincipalPayment": 6220.614145,
        "scheduledPrincipalPayment": 8439.668152
    }
    {
        "date": "2047-09-25",
        "totalCashFlow": 14562.998375,
        "interestPayment": 279.476944,
        "principalBalance": 656461.144049,
        "principalPayment": 14283.521431,
        "endPrincipalBalance": 656461.144049,
        "beginPrincipalBalance": 670744.66548,
        "prepayPrincipalPayment": 5912.694605,
        "scheduledPrincipalPayment": 8370.826826
    }
    {
        "date": "2047-10-25",
        "totalCashFlow": 13864.867191,
        "interestPayment": 273.525477,
        "principalBalance": 642869.802334,
        "principalPayment": 13591.341715,
        "endPrincipalBalance": 642869.802334,
        "beginPrincipalBalance": 656461.144049,
        "prepayPrincipalPayment": 5286.595482,
        "scheduledPrincipalPayment": 8304.746232
    }
    {
        "date": "2047-11-25",
        "totalCashFlow": 13800.222155,
        "interestPayment": 267.862418,
        "principalBalance": 629337.442597,
        "principalPayment": 13532.359738,
        "endPrincipalBalance": 629337.442597,
        "beginPrincipalBalance": 642869.802334,
        "prepayPrincipalPayment": 5286.769768,
        "scheduledPrincipalPayment": 8245.589969
    }
    {
        "date": "2047-12-25",
        "totalCashFlow": 13148.497926,
        "interestPayment": 262.223934,
        "principalBalance": 616451.168605,
        "principalPayment": 12886.273992,
        "endPrincipalBalance": 616451.168605,
        "beginPrincipalBalance": 629337.442597,
        "prepayPrincipalPayment": 4700.856732,
        "scheduledPrincipalPayment": 8185.41726
    }
    {
        "date": "2048-01-25",
        "totalCashFlow": 13163.849683,
        "interestPayment": 256.854654,
        "principalBalance": 603544.173575,
        "principalPayment": 12906.99503,
        "endPrincipalBalance": 603544.173575,
        "beginPrincipalBalance": 616451.168605,
        "prepayPrincipalPayment": 4775.062772,
        "scheduledPrincipalPayment": 8131.932258
    }
    {
        "date": "2048-02-25",
        "totalCashFlow": 12422.788069,
        "interestPayment": 251.476739,
        "principalBalance": 591372.862245,
        "principalPayment": 12171.31133,
        "endPrincipalBalance": 591372.862245,
        "beginPrincipalBalance": 603544.173575,
        "prepayPrincipalPayment": 4094.807218,
        "scheduledPrincipalPayment": 8076.504112
    }
    {
        "date": "2048-03-25",
        "totalCashFlow": 12239.743902,
        "interestPayment": 246.405359,
        "principalBalance": 579379.523702,
        "principalPayment": 11993.338542,
        "endPrincipalBalance": 579379.523702,
        "beginPrincipalBalance": 591372.862245,
        "prepayPrincipalPayment": 3964.01834,
        "scheduledPrincipalPayment": 8029.320202
    }
    {
        "date": "2048-04-25",
        "totalCashFlow": 12745.83395,
        "interestPayment": 241.408135,
        "principalBalance": 566875.097887,
        "principalPayment": 12504.425815,
        "endPrincipalBalance": 566875.097887,
        "beginPrincipalBalance": 579379.523702,
        "prepayPrincipalPayment": 4521.360543,
        "scheduledPrincipalPayment": 7983.065273
    }
    {
        "date": "2048-05-25",
        "totalCashFlow": 12938.293931,
        "interestPayment": 236.197957,
        "principalBalance": 554173.001913,
        "principalPayment": 12702.095974,
        "endPrincipalBalance": 554173.001913,
        "beginPrincipalBalance": 566875.097887,
        "prepayPrincipalPayment": 4773.949412,
        "scheduledPrincipalPayment": 7928.146562
    }
    {
        "date": "2048-06-25",
        "totalCashFlow": 12794.245399,
        "interestPayment": 230.905417,
        "principalBalance": 541609.661931,
        "principalPayment": 12563.339982,
        "endPrincipalBalance": 541609.661931,
        "beginPrincipalBalance": 554173.001913,
        "prepayPrincipalPayment": 4694.719536,
        "scheduledPrincipalPayment": 7868.620446
    }
    {
        "date": "2048-07-25",
        "totalCashFlow": 13039.998244,
        "interestPayment": 225.670692,
        "principalBalance": 528795.33438,
        "principalPayment": 12814.327551,
        "endPrincipalBalance": 528795.33438,
        "beginPrincipalBalance": 541609.661931,
        "prepayPrincipalPayment": 5005.200813,
        "scheduledPrincipalPayment": 7809.126738
    }
    {
        "date": "2048-08-25",
        "totalCashFlow": 12783.231483,
        "interestPayment": 220.331389,
        "principalBalance": 516232.434286,
        "principalPayment": 12562.900094,
        "endPrincipalBalance": 516232.434286,
        "beginPrincipalBalance": 528795.33438,
        "prepayPrincipalPayment": 4818.937693,
        "scheduledPrincipalPayment": 7743.962401
    }
    {
        "date": "2048-09-25",
        "totalCashFlow": 12348.20514,
        "interestPayment": 215.096848,
        "principalBalance": 504099.325994,
        "principalPayment": 12133.108292,
        "endPrincipalBalance": 504099.325994,
        "beginPrincipalBalance": 516232.434286,
        "prepayPrincipalPayment": 4452.773816,
        "scheduledPrincipalPayment": 7680.334476
    }
    {
        "date": "2048-10-25",
        "totalCashFlow": 12066.782383,
        "interestPayment": 210.041386,
        "principalBalance": 492242.584997,
        "principalPayment": 11856.740997,
        "endPrincipalBalance": 492242.584997,
        "beginPrincipalBalance": 504099.325994,
        "prepayPrincipalPayment": 4235.723595,
        "scheduledPrincipalPayment": 7621.017403
    }
    {
        "date": "2048-11-25",
        "totalCashFlow": 11764.140539,
        "interestPayment": 205.101077,
        "principalBalance": 480683.545535,
        "principalPayment": 11559.039462,
        "endPrincipalBalance": 480683.545535,
        "beginPrincipalBalance": 492242.584997,
        "prepayPrincipalPayment": 3995.170228,
        "scheduledPrincipalPayment": 7563.869234
    }
    {
        "date": "2048-12-25",
        "totalCashFlow": 11378.109399,
        "interestPayment": 200.284811,
        "principalBalance": 469505.720946,
        "principalPayment": 11177.824589,
        "endPrincipalBalance": 469505.720946,
        "beginPrincipalBalance": 480683.545535,
        "prepayPrincipalPayment": 3668.489676,
        "scheduledPrincipalPayment": 7509.334913
    }
    {
        "date": "2049-01-25",
        "totalCashFlow": 11453.754432,
        "interestPayment": 195.627384,
        "principalBalance": 458247.593898,
        "principalPayment": 11258.127048,
        "endPrincipalBalance": 458247.593898,
        "beginPrincipalBalance": 469505.720946,
        "prepayPrincipalPayment": 3799.249955,
        "scheduledPrincipalPayment": 7458.877094
    }
    {
        "date": "2049-02-25",
        "totalCashFlow": 10663.256962,
        "interestPayment": 190.936497,
        "principalBalance": 447775.273433,
        "principalPayment": 10472.320464,
        "endPrincipalBalance": 447775.273433,
        "beginPrincipalBalance": 458247.593898,
        "prepayPrincipalPayment": 3067.069338,
        "scheduledPrincipalPayment": 7405.251127
    }
    {
        "date": "2049-03-25",
        "totalCashFlow": 10694.369376,
        "interestPayment": 186.573031,
        "principalBalance": 437267.477088,
        "principalPayment": 10507.796345,
        "endPrincipalBalance": 437267.477088,
        "beginPrincipalBalance": 447775.273433,
        "prepayPrincipalPayment": 3145.261633,
        "scheduledPrincipalPayment": 7362.534712
    }
    {
        "date": "2049-04-25",
        "totalCashFlow": 11139.25986,
        "interestPayment": 182.194782,
        "principalBalance": 426310.41201,
        "principalPayment": 10957.065078,
        "endPrincipalBalance": 426310.41201,
        "beginPrincipalBalance": 437267.477088,
        "prepayPrincipalPayment": 3639.496275,
        "scheduledPrincipalPayment": 7317.568803
    }
    {
        "date": "2049-05-25",
        "totalCashFlow": 11144.657541,
        "interestPayment": 177.629338,
        "principalBalance": 415343.383807,
        "principalPayment": 10967.028203,
        "endPrincipalBalance": 415343.383807,
        "beginPrincipalBalance": 426310.41201,
        "prepayPrincipalPayment": 3703.844171,
        "scheduledPrincipalPayment": 7263.184032
    }
    {
        "date": "2049-06-25",
        "totalCashFlow": 11091.46839,
        "interestPayment": 173.059743,
        "principalBalance": 404424.97516,
        "principalPayment": 10918.408647,
        "endPrincipalBalance": 404424.97516,
        "beginPrincipalBalance": 415343.383807,
        "prepayPrincipalPayment": 3711.922973,
        "scheduledPrincipalPayment": 7206.485674
    }
    {
        "date": "2049-07-25",
        "totalCashFlow": 11256.591087,
        "interestPayment": 168.510406,
        "principalBalance": 393336.89448,
        "principalPayment": 11088.080681,
        "endPrincipalBalance": 393336.89448,
        "beginPrincipalBalance": 404424.97516,
        "prepayPrincipalPayment": 3939.698061,
        "scheduledPrincipalPayment": 7148.38262
    }
    {
        "date": "2049-08-25",
        "totalCashFlow": 10978.529285,
        "interestPayment": 163.890373,
        "principalBalance": 382522.255567,
        "principalPayment": 10814.638913,
        "endPrincipalBalance": 382522.255567,
        "beginPrincipalBalance": 393336.89448,
        "prepayPrincipalPayment": 3729.772724,
        "scheduledPrincipalPayment": 7084.866188
    }
    {
        "date": "2049-09-25",
        "totalCashFlow": 10855.913254,
        "interestPayment": 159.384273,
        "principalBalance": 371825.726586,
        "principalPayment": 10696.528981,
        "endPrincipalBalance": 371825.726586,
        "beginPrincipalBalance": 382522.255567,
        "prepayPrincipalPayment": 3672.767714,
        "scheduledPrincipalPayment": 7023.761267
    }
    {
        "date": "2049-10-25",
        "totalCashFlow": 10563.481652,
        "interestPayment": 154.927386,
        "principalBalance": 361417.17232,
        "principalPayment": 10408.554266,
        "endPrincipalBalance": 361417.17232,
        "beginPrincipalBalance": 371825.726586,
        "prepayPrincipalPayment": 3446.247869,
        "scheduledPrincipalPayment": 6962.306396
    }
    {
        "date": "2049-11-25",
        "totalCashFlow": 10275.200179,
        "interestPayment": 150.590488,
        "principalBalance": 351292.56263,
        "principalPayment": 10124.60969,
        "endPrincipalBalance": 351292.56263,
        "beginPrincipalBalance": 361417.17232,
        "prepayPrincipalPayment": 3220.88053,
        "scheduledPrincipalPayment": 6903.72916
    }
    {
        "date": "2049-12-25",
        "totalCashFlow": 10140.731031,
        "interestPayment": 146.371901,
        "principalBalance": 341298.2035,
        "principalPayment": 9994.359129,
        "endPrincipalBalance": 341298.2035,
        "beginPrincipalBalance": 351292.56263,
        "prepayPrincipalPayment": 3146.226752,
        "scheduledPrincipalPayment": 6848.132377
    }
    {
        "date": "2050-01-25",
        "totalCashFlow": 10040.562754,
        "interestPayment": 142.207585,
        "principalBalance": 331399.848331,
        "principalPayment": 9898.355169,
        "endPrincipalBalance": 331399.848331,
        "beginPrincipalBalance": 341298.2035,
        "prepayPrincipalPayment": 3105.706739,
        "scheduledPrincipalPayment": 6792.648431
    }
    {
        "date": "2050-02-25",
        "totalCashFlow": 9607.956675,
        "interestPayment": 138.08327,
        "principalBalance": 321929.974926,
        "principalPayment": 9469.873405,
        "endPrincipalBalance": 321929.974926,
        "beginPrincipalBalance": 331399.848331,
        "prepayPrincipalPayment": 2733.281132,
        "scheduledPrincipalPayment": 6736.592273
    }
    {
        "date": "2050-03-25",
        "totalCashFlow": 9532.773741,
        "interestPayment": 134.13749,
        "principalBalance": 312531.338675,
        "principalPayment": 9398.636251,
        "endPrincipalBalance": 312531.338675,
        "beginPrincipalBalance": 321929.974926,
        "prepayPrincipalPayment": 2711.799922,
        "scheduledPrincipalPayment": 6686.836329
    }
    {
        "date": "2050-04-25",
        "totalCashFlow": 9776.696332,
        "interestPayment": 130.221391,
        "principalBalance": 302884.863734,
        "principalPayment": 9646.47494,
        "endPrincipalBalance": 302884.863734,
        "beginPrincipalBalance": 312531.338675,
        "prepayPrincipalPayment": 3010.254905,
        "scheduledPrincipalPayment": 6636.220035
    }
    {
        "date": "2050-05-25",
        "totalCashFlow": 9666.339678,
        "interestPayment": 126.202027,
        "principalBalance": 293344.726083,
        "principalPayment": 9540.137651,
        "endPrincipalBalance": 293344.726083,
        "beginPrincipalBalance": 302884.863734,
        "prepayPrincipalPayment": 2962.378676,
        "scheduledPrincipalPayment": 6577.758975
    }
    {
        "date": "2050-06-25",
        "totalCashFlow": 9702.375823,
        "interestPayment": 122.226969,
        "principalBalance": 283764.577229,
        "principalPayment": 9580.148854,
        "endPrincipalBalance": 283764.577229,
        "beginPrincipalBalance": 293344.726083,
        "prepayPrincipalPayment": 3061.368769,
        "scheduledPrincipalPayment": 6518.780085
    }
    {
        "date": "2050-07-25",
        "totalCashFlow": 9686.77533,
        "interestPayment": 118.235241,
        "principalBalance": 274196.037139,
        "principalPayment": 9568.54009,
        "endPrincipalBalance": 274196.037139,
        "beginPrincipalBalance": 283764.577229,
        "prepayPrincipalPayment": 3112.618739,
        "scheduledPrincipalPayment": 6455.921351
    }
    {
        "date": "2050-08-25",
        "totalCashFlow": 9390.907533,
        "interestPayment": 114.248349,
        "principalBalance": 264919.377955,
        "principalPayment": 9276.659184,
        "endPrincipalBalance": 264919.377955,
        "beginPrincipalBalance": 274196.037139,
        "prepayPrincipalPayment": 2886.552136,
        "scheduledPrincipalPayment": 6390.107048
    }
    {
        "date": "2050-09-25",
        "totalCashFlow": 9373.635912,
        "interestPayment": 110.383074,
        "principalBalance": 255656.125117,
        "principalPayment": 9263.252838,
        "endPrincipalBalance": 255656.125117,
        "beginPrincipalBalance": 264919.377955,
        "prepayPrincipalPayment": 2935.437084,
        "scheduledPrincipalPayment": 6327.815754
    }
    {
        "date": "2050-10-25",
        "totalCashFlow": 9074.339851,
        "interestPayment": 106.523385,
        "principalBalance": 246688.308652,
        "principalPayment": 8967.816465,
        "endPrincipalBalance": 246688.308652,
        "beginPrincipalBalance": 255656.125117,
        "prepayPrincipalPayment": 2705.315117,
        "scheduledPrincipalPayment": 6262.501348
    }
    {
        "date": "2050-11-25",
        "totalCashFlow": 8837.856805,
        "interestPayment": 102.786795,
        "principalBalance": 237953.238642,
        "principalPayment": 8735.070009,
        "endPrincipalBalance": 237953.238642,
        "beginPrincipalBalance": 246688.308652,
        "prepayPrincipalPayment": 2534.048916,
        "scheduledPrincipalPayment": 6201.021094
    }
    {
        "date": "2050-12-25",
        "totalCashFlow": 8698.495155,
        "interestPayment": 99.147183,
        "principalBalance": 229353.89067,
        "principalPayment": 8599.347973,
        "endPrincipalBalance": 229353.89067,
        "beginPrincipalBalance": 237953.238642,
        "prepayPrincipalPayment": 2457.276591,
        "scheduledPrincipalPayment": 6142.071382
    }
    {
        "date": "2051-01-25",
        "totalCashFlow": 8581.065973,
        "interestPayment": 95.564121,
        "principalBalance": 220868.388817,
        "principalPayment": 8485.501852,
        "endPrincipalBalance": 220868.388817,
        "beginPrincipalBalance": 229353.89067,
        "prepayPrincipalPayment": 2402.208329,
        "scheduledPrincipalPayment": 6083.293523
    }
    {
        "date": "2051-02-25",
        "totalCashFlow": 8261.18641,
        "interestPayment": 92.028495,
        "principalBalance": 212699.230902,
        "principalPayment": 8169.157915,
        "endPrincipalBalance": 212699.230902,
        "beginPrincipalBalance": 220868.388817,
        "prepayPrincipalPayment": 2145.04705,
        "scheduledPrincipalPayment": 6024.110865
    }
    {
        "date": "2051-03-25",
        "totalCashFlow": 8161.650481,
        "interestPayment": 88.62468,
        "principalBalance": 204626.205101,
        "principalPayment": 8073.025801,
        "endPrincipalBalance": 204626.205101,
        "beginPrincipalBalance": 212699.230902,
        "prepayPrincipalPayment": 2102.848368,
        "scheduledPrincipalPayment": 5970.177434
    }
    {
        "date": "2051-04-25",
        "totalCashFlow": 8236.058159,
        "interestPayment": 85.260919,
        "principalBalance": 196475.407861,
        "principalPayment": 8150.79724,
        "endPrincipalBalance": 196475.407861,
        "beginPrincipalBalance": 204626.205101,
        "prepayPrincipalPayment": 2235.192788,
        "scheduledPrincipalPayment": 5915.604452
    }
    {
        "date": "2051-05-25",
        "totalCashFlow": 8109.596827,
        "interestPayment": 81.864753,
        "principalBalance": 188447.675786,
        "principalPayment": 8027.732074,
        "endPrincipalBalance": 188447.675786,
        "beginPrincipalBalance": 196475.407861,
        "prepayPrincipalPayment": 2172.576424,
        "scheduledPrincipalPayment": 5855.155651
    }
    {
        "date": "2051-06-25",
        "totalCashFlow": 8125.604164,
        "interestPayment": 78.519865,
        "principalBalance": 180400.591487,
        "principalPayment": 8047.084299,
        "endPrincipalBalance": 180400.591487,
        "beginPrincipalBalance": 188447.675786,
        "prepayPrincipalPayment": 2252.632629,
        "scheduledPrincipalPayment": 5794.45167
    }
    {
        "date": "2051-07-25",
        "totalCashFlow": 8014.069043,
        "interestPayment": 75.166913,
        "principalBalance": 172461.689357,
        "principalPayment": 7938.90213,
        "endPrincipalBalance": 172461.689357,
        "beginPrincipalBalance": 180400.591487,
        "prepayPrincipalPayment": 2209.951047,
        "scheduledPrincipalPayment": 5728.951084
    }
    {
        "date": "2051-08-25",
        "totalCashFlow": 7779.570463,
        "interestPayment": 71.859037,
        "principalBalance": 164753.977932,
        "principalPayment": 7707.711426,
        "endPrincipalBalance": 164753.977932,
        "beginPrincipalBalance": 172461.689357,
        "prepayPrincipalPayment": 2045.351055,
        "scheduledPrincipalPayment": 5662.36037
    }
    {
        "date": "2051-09-25",
        "totalCashFlow": 7724.810603,
        "interestPayment": 68.647491,
        "principalBalance": 157097.814819,
        "principalPayment": 7656.163112,
        "endPrincipalBalance": 157097.814819,
        "beginPrincipalBalance": 164753.977932,
        "prepayPrincipalPayment": 2057.410598,
        "scheduledPrincipalPayment": 5598.752514
    }
    {
        "date": "2051-10-25",
        "totalCashFlow": 7479.627963,
        "interestPayment": 65.457423,
        "principalBalance": 149683.644279,
        "principalPayment": 7414.17054,
        "endPrincipalBalance": 149683.644279,
        "beginPrincipalBalance": 157097.814819,
        "prepayPrincipalPayment": 1882.036844,
        "scheduledPrincipalPayment": 5532.133696
    }
    {
        "date": "2051-11-25",
        "totalCashFlow": 7352.634099,
        "interestPayment": 62.368185,
        "principalBalance": 142393.378365,
        "principalPayment": 7290.265914,
        "endPrincipalBalance": 142393.378365,
        "beginPrincipalBalance": 149683.644279,
        "prepayPrincipalPayment": 1821.13531,
        "scheduledPrincipalPayment": 5469.130604
    }
    {
        "date": "2051-12-25",
        "totalCashFlow": 7198.859824,
        "interestPayment": 59.330574,
        "principalBalance": 135253.849115,
        "principalPayment": 7139.529249,
        "endPrincipalBalance": 135253.849115,
        "beginPrincipalBalance": 142393.378365,
        "prepayPrincipalPayment": 1733.837546,
        "scheduledPrincipalPayment": 5405.691703
    }
    {
        "date": "2052-01-25",
        "totalCashFlow": 7060.07628,
        "interestPayment": 56.35577,
        "principalBalance": 128250.128606,
        "principalPayment": 7003.720509,
        "endPrincipalBalance": 128250.128606,
        "beginPrincipalBalance": 135253.849115,
        "prepayPrincipalPayment": 1660.888371,
        "scheduledPrincipalPayment": 5342.832138
    }
    {
        "date": "2052-02-25",
        "totalCashFlow": 6871.231669,
        "interestPayment": 53.437554,
        "principalBalance": 121432.33449,
        "principalPayment": 6817.794116,
        "endPrincipalBalance": 121432.33449,
        "beginPrincipalBalance": 128250.128606,
        "prepayPrincipalPayment": 1537.774803,
        "scheduledPrincipalPayment": 5280.019312
    }
    {
        "date": "2052-03-25",
        "totalCashFlow": 6761.016926,
        "interestPayment": 50.596806,
        "principalBalance": 114721.91437,
        "principalPayment": 6710.42012,
        "endPrincipalBalance": 114721.91437,
        "beginPrincipalBalance": 121432.33449,
        "prepayPrincipalPayment": 1490.99765,
        "scheduledPrincipalPayment": 5219.42247
    }
    {
        "date": "2052-04-25",
        "totalCashFlow": 6695.816595,
        "interestPayment": 47.800798,
        "principalBalance": 108073.898572,
        "principalPayment": 6648.015798,
        "endPrincipalBalance": 108073.898572,
        "beginPrincipalBalance": 114721.91437,
        "prepayPrincipalPayment": 1490.190746,
        "scheduledPrincipalPayment": 5157.825052
    }
    {
        "date": "2052-05-25",
        "totalCashFlow": 6616.98244,
        "interestPayment": 45.030791,
        "principalBalance": 101501.946923,
        "principalPayment": 6571.951649,
        "endPrincipalBalance": 101501.946923,
        "beginPrincipalBalance": 108073.898572,
        "prepayPrincipalPayment": 1478.978966,
        "scheduledPrincipalPayment": 5092.972683
    }
    {
        "date": "2052-06-25",
        "totalCashFlow": 6524.953569,
        "interestPayment": 42.292478,
        "principalBalance": 95019.285833,
        "principalPayment": 6482.661091,
        "endPrincipalBalance": 95019.285833,
        "beginPrincipalBalance": 101501.946923,
        "prepayPrincipalPayment": 1457.603057,
        "scheduledPrincipalPayment": 5025.058034
    }
    {
        "date": "2052-07-25",
        "totalCashFlow": 6358.253959,
        "interestPayment": 39.591369,
        "principalBalance": 88700.623243,
        "principalPayment": 6318.66259,
        "endPrincipalBalance": 88700.623243,
        "beginPrincipalBalance": 95019.285833,
        "prepayPrincipalPayment": 1364.369354,
        "scheduledPrincipalPayment": 4954.293235
    }
    {
        "date": "2052-08-25",
        "totalCashFlow": 6238.709137,
        "interestPayment": 36.958593,
        "principalBalance": 82498.872699,
        "principalPayment": 6201.750544,
        "endPrincipalBalance": 82498.872699,
        "beginPrincipalBalance": 88700.623243,
        "prepayPrincipalPayment": 1317.425966,
        "scheduledPrincipalPayment": 4884.324578
    }
    {
        "date": "2052-09-25",
        "totalCashFlow": 6075.539459,
        "interestPayment": 34.37453,
        "principalBalance": 76457.70777,
        "principalPayment": 6041.164929,
        "endPrincipalBalance": 76457.70777,
        "beginPrincipalBalance": 82498.872699,
        "prepayPrincipalPayment": 1228.604377,
        "scheduledPrincipalPayment": 4812.560551
    }
    {
        "date": "2052-10-25",
        "totalCashFlow": 5890.045364,
        "interestPayment": 31.857378,
        "principalBalance": 70599.519785,
        "principalPayment": 5858.187985,
        "endPrincipalBalance": 70599.519785,
        "beginPrincipalBalance": 76457.70777,
        "prepayPrincipalPayment": 1116.803989,
        "scheduledPrincipalPayment": 4741.383996
    }
    {
        "date": "2052-11-25",
        "totalCashFlow": 5754.532991,
        "interestPayment": 29.416467,
        "principalBalance": 64874.403261,
        "principalPayment": 5725.116524,
        "endPrincipalBalance": 64874.403261,
        "beginPrincipalBalance": 70599.519785,
        "prepayPrincipalPayment": 1052.705802,
        "scheduledPrincipalPayment": 4672.410722
    }
    {
        "date": "2052-12-25",
        "totalCashFlow": 5577.624124,
        "interestPayment": 27.031001,
        "principalBalance": 59323.810138,
        "principalPayment": 5550.593123,
        "endPrincipalBalance": 59323.810138,
        "beginPrincipalBalance": 64874.403261,
        "prepayPrincipalPayment": 948.000781,
        "scheduledPrincipalPayment": 4602.592341
    }
    {
        "date": "2053-01-25",
        "totalCashFlow": 5446.930399,
        "interestPayment": 24.718254,
        "principalBalance": 53901.597993,
        "principalPayment": 5422.212145,
        "endPrincipalBalance": 53901.597993,
        "beginPrincipalBalance": 59323.810138,
        "prepayPrincipalPayment": 887.293911,
        "scheduledPrincipalPayment": 4534.918234
    }
    {
        "date": "2053-02-25",
        "totalCashFlow": 5271.675988,
        "interestPayment": 22.458999,
        "principalBalance": 48652.381004,
        "principalPayment": 5249.216988,
        "endPrincipalBalance": 48652.381004,
        "beginPrincipalBalance": 53901.597993,
        "prepayPrincipalPayment": 783.093375,
        "scheduledPrincipalPayment": 4466.123613
    }
    {
        "date": "2053-03-25",
        "totalCashFlow": 5130.944302,
        "interestPayment": 20.271825,
        "principalBalance": 43541.708528,
        "principalPayment": 5110.672477,
        "endPrincipalBalance": 43541.708528,
        "beginPrincipalBalance": 48652.381004,
        "prepayPrincipalPayment": 710.716947,
        "scheduledPrincipalPayment": 4399.955529
    }
    {
        "date": "2053-04-25",
        "totalCashFlow": 5015.900748,
        "interestPayment": 18.142379,
        "principalBalance": 38543.950158,
        "principalPayment": 4997.758369,
        "endPrincipalBalance": 38543.950158,
        "beginPrincipalBalance": 43541.708528,
        "prepayPrincipalPayment": 663.958735,
        "scheduledPrincipalPayment": 4333.799634
    }
    {
        "date": "2053-05-25",
        "totalCashFlow": 4889.391645,
        "interestPayment": 16.059979,
        "principalBalance": 33670.618493,
        "principalPayment": 4873.331666,
        "endPrincipalBalance": 33670.618493,
        "beginPrincipalBalance": 38543.950158,
        "prepayPrincipalPayment": 608.483995,
        "scheduledPrincipalPayment": 4264.847671
    }
    {
        "date": "2053-06-25",
        "totalCashFlow": 4744.849254,
        "interestPayment": 14.029424,
        "principalBalance": 28939.798663,
        "principalPayment": 4730.819829,
        "endPrincipalBalance": 28939.798663,
        "beginPrincipalBalance": 33670.618493,
        "prepayPrincipalPayment": 537.313237,
        "scheduledPrincipalPayment": 4193.506592
    }
    {
        "date": "2053-07-25",
        "totalCashFlow": 4596.626896,
        "interestPayment": 12.058249,
        "principalBalance": 24355.230017,
        "principalPayment": 4584.568646,
        "endPrincipalBalance": 24355.230017,
        "beginPrincipalBalance": 28939.798663,
        "prepayPrincipalPayment": 463.213313,
        "scheduledPrincipalPayment": 4121.355333
    }
    {
        "date": "2053-08-25",
        "totalCashFlow": 4445.629553,
        "interestPayment": 10.148013,
        "principalBalance": 19919.748477,
        "principalPayment": 4435.48154,
        "endPrincipalBalance": 19919.748477,
        "beginPrincipalBalance": 24355.230017,
        "prepayPrincipalPayment": 386.834544,
        "scheduledPrincipalPayment": 4048.646996
    }
    {
        "date": "2053-09-25",
        "totalCashFlow": 4287.278501,
        "interestPayment": 8.299895,
        "principalBalance": 15640.769871,
        "principalPayment": 4278.978605,
        "endPrincipalBalance": 15640.769871,
        "beginPrincipalBalance": 19919.748477,
        "prepayPrincipalPayment": 303.320164,
        "scheduledPrincipalPayment": 3975.658441
    }
    {
        "date": "2053-10-25",
        "totalCashFlow": 4135.601416,
        "interestPayment": 6.516987,
        "principalBalance": 11511.685443,
        "principalPayment": 4129.084429,
        "endPrincipalBalance": 11511.685443,
        "beginPrincipalBalance": 15640.769871,
        "prepayPrincipalPayment": 224.996336,
        "scheduledPrincipalPayment": 3904.088093
    }
    {
        "date": "2053-11-25",
        "totalCashFlow": 3987.444772,
        "interestPayment": 4.796536,
        "principalBalance": 7529.037206,
        "principalPayment": 3982.648237,
        "endPrincipalBalance": 7529.037206,
        "beginPrincipalBalance": 11511.685443,
        "prepayPrincipalPayment": 149.414094,
        "scheduledPrincipalPayment": 3833.234142
    }
    {
        "date": "2053-12-25",
        "totalCashFlow": 3837.818275,
        "interestPayment": 3.137099,
        "principalBalance": 3694.35603,
        "principalPayment": 3834.681176,
        "endPrincipalBalance": 3694.35603,
        "beginPrincipalBalance": 7529.037206,
        "prepayPrincipalPayment": 72.122239,
        "scheduledPrincipalPayment": 3762.558937
    }
    {
        "date": "2054-01-25",
        "totalCashFlow": 3695.895345,
        "interestPayment": 1.539315,
        "principalBalance": 0.0,
        "principalPayment": 3694.35603,
        "endPrincipalBalance": 0.0,
        "beginPrincipalBalance": 3694.35603,
        "prepayPrincipalPayment": 0.0,
        "scheduledPrincipalPayment": 3694.35603
    }

    """

    try:
        logger.info("Calling post_cash_flow_async")

        response = Client().yield_book_rest.post_cash_flow_async(
            body=CashFlowRequestData(global_settings=global_settings, input=input, keywords=keywords),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
            content_type="application/json",
        )

        output = response
        logger.info("Called post_cash_flow_async")

        return output
    except Exception as err:
        logger.error("Error post_cash_flow_async.")
        check_exception_and_raise(err, logger)


def post_cash_flow_sync(
    *,
    global_settings: Optional[CashFlowGlobalSettings] = None,
    input: Optional[List[CashFlowInput]] = None,
    keywords: Optional[List[str]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Post cash flow sync.

    Parameters
    ----------
    global_settings : CashFlowGlobalSettings, optional

    input : List[CashFlowInput], optional

    keywords : List[str], optional
        Optional. Used to specify the keywords a user will retrieve in the response. All keywords are returned by default.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------
    >>> # Formulate API Request body parameters - Global Settings
    >>> global_settings = CashFlowGlobalSettings(
    >>>         )
    >>>
    >>> # Formulate API Request body parameters - Input
    >>> input = CashFlowInput(
    >>>             identifier="01F002628",
    >>>             par_amount="10000"
    >>>         )
    >>>
    >>> # Execute API Post sync request with prepared inputs
    >>> cf_async_get_response = post_cash_flow_sync(
    >>>                             global_settings=global_settings,
    >>>                             input=[input]
    >>>                         )
    >>>
    >>> # Print output to a file, as CF output is too long for terminal printout
    >>> # print(js.dumps(cf_async_get_response, indent=4), file=open('.CF_sync_post_output.json', 'w+'))
    >>>
    >>> # Print onyl payment information
    >>> for paymentInfo in cf_async_get_response["results"][0]["cashFlow"]["dataPaymentList"]:
    >>>     print(js.dumps(paymentInfo, indent=4))
    {
        "date": "2026-03-25",
        "totalCashFlow": 44637.115742,
        "interestPayment": 4166.666667,
        "principalBalance": 9959529.550924,
        "principalPayment": 40470.449076,
        "endPrincipalBalance": 9959529.550924,
        "beginPrincipalBalance": 10000000.0,
        "prepayPrincipalPayment": 15510.346058,
        "scheduledPrincipalPayment": 24960.103018
    }
    {
        "date": "2026-04-25",
        "totalCashFlow": 48170.979212,
        "interestPayment": 4149.80398,
        "principalBalance": 9915508.375692,
        "principalPayment": 44021.175232,
        "endPrincipalBalance": 9915508.375692,
        "beginPrincipalBalance": 9959529.550924,
        "prepayPrincipalPayment": 19073.923391,
        "scheduledPrincipalPayment": 24947.251841
    }
    {
        "date": "2026-05-25",
        "totalCashFlow": 50416.007165,
        "interestPayment": 4131.461823,
        "principalBalance": 9869223.83035,
        "principalPayment": 46284.545342,
        "endPrincipalBalance": 9869223.83035,
        "beginPrincipalBalance": 9915508.375692,
        "prepayPrincipalPayment": 21359.254205,
        "scheduledPrincipalPayment": 24925.291137
    }
    {
        "date": "2026-06-25",
        "totalCashFlow": 50868.01161,
        "interestPayment": 4112.176596,
        "principalBalance": 9822467.995335,
        "principalPayment": 46755.835014,
        "endPrincipalBalance": 9822467.995335,
        "beginPrincipalBalance": 9869223.83035,
        "prepayPrincipalPayment": 21858.46363,
        "scheduledPrincipalPayment": 24897.371385
    }
    {
        "date": "2026-07-25",
        "totalCashFlow": 53653.653613,
        "interestPayment": 4092.694998,
        "principalBalance": 9772907.036721,
        "principalPayment": 49560.958615,
        "endPrincipalBalance": 9772907.036721,
        "beginPrincipalBalance": 9822467.995335,
        "prepayPrincipalPayment": 24692.992484,
        "scheduledPrincipalPayment": 24867.966131
    }
    {
        "date": "2026-08-25",
        "totalCashFlow": 53661.320385,
        "interestPayment": 4072.044599,
        "principalBalance": 9723317.760935,
        "principalPayment": 49589.275786,
        "endPrincipalBalance": 9723317.760935,
        "beginPrincipalBalance": 9772907.036721,
        "prepayPrincipalPayment": 24758.145802,
        "scheduledPrincipalPayment": 24831.129984
    }
    {
        "date": "2026-09-25",
        "totalCashFlow": 52350.554473,
        "interestPayment": 4051.3824,
        "principalBalance": 9675018.588862,
        "principalPayment": 48299.172073,
        "endPrincipalBalance": 9675018.588862,
        "beginPrincipalBalance": 9723317.760935,
        "prepayPrincipalPayment": 23505.308082,
        "scheduledPrincipalPayment": 24793.863991
    }
    {
        "date": "2026-10-25",
        "totalCashFlow": 51710.109422,
        "interestPayment": 4031.257745,
        "principalBalance": 9627339.737185,
        "principalPayment": 47678.851677,
        "endPrincipalBalance": 9627339.737185,
        "beginPrincipalBalance": 9675018.588862,
        "prepayPrincipalPayment": 22919.313659,
        "scheduledPrincipalPayment": 24759.538018
    }
    {
        "date": "2026-11-25",
        "totalCashFlow": 50772.994289,
        "interestPayment": 4011.391557,
        "principalBalance": 9580578.134453,
        "principalPayment": 46761.602732,
        "endPrincipalBalance": 9580578.134453,
        "beginPrincipalBalance": 9627339.737185,
        "prepayPrincipalPayment": 22035.138553,
        "scheduledPrincipalPayment": 24726.464179
    }
    {
        "date": "2026-12-25",
        "totalCashFlow": 48984.768102,
        "interestPayment": 3991.907556,
        "principalBalance": 9535585.273907,
        "principalPayment": 44992.860546,
        "endPrincipalBalance": 9535585.273907,
        "beginPrincipalBalance": 9580578.134453,
        "prepayPrincipalPayment": 20297.438612,
        "scheduledPrincipalPayment": 24695.421935
    }
    {
        "date": "2027-01-25",
        "totalCashFlow": 50577.469607,
        "interestPayment": 3973.160531,
        "principalBalance": 9488980.964831,
        "principalPayment": 46604.309076,
        "endPrincipalBalance": 9488980.964831,
        "beginPrincipalBalance": 9535585.273907,
        "prepayPrincipalPayment": 21935.672382,
        "scheduledPrincipalPayment": 24668.636694
    }
    {
        "date": "2027-02-25",
        "totalCashFlow": 45557.230703,
        "interestPayment": 3953.742069,
        "principalBalance": 9447377.476196,
        "principalPayment": 41603.488635,
        "endPrincipalBalance": 9447377.476196,
        "beginPrincipalBalance": 9488980.964831,
        "prepayPrincipalPayment": 16966.109661,
        "scheduledPrincipalPayment": 24637.378974
    }
    {
        "date": "2027-03-25",
        "totalCashFlow": 46422.801029,
        "interestPayment": 3936.407282,
        "principalBalance": 9404891.082448,
        "principalPayment": 42486.393748,
        "endPrincipalBalance": 9404891.082448,
        "beginPrincipalBalance": 9447377.476196,
        "prepayPrincipalPayment": 17867.562661,
        "scheduledPrincipalPayment": 24618.831087
    }
    {
        "date": "2027-04-25",
        "totalCashFlow": 50509.820631,
        "interestPayment": 3918.704618,
        "principalBalance": 9358299.966435,
        "principalPayment": 46591.116014,
        "endPrincipalBalance": 9358299.966435,
        "beginPrincipalBalance": 9404891.082448,
        "prepayPrincipalPayment": 21993.3715,
        "scheduledPrincipalPayment": 24597.744514
    }
    {
        "date": "2027-05-25",
        "totalCashFlow": 52159.072279,
        "interestPayment": 3899.291653,
        "principalBalance": 9310040.185808,
        "principalPayment": 48259.780627,
        "endPrincipalBalance": 9310040.185808,
        "beginPrincipalBalance": 9358299.966435,
        "prepayPrincipalPayment": 23694.146291,
        "scheduledPrincipalPayment": 24565.634336
    }
    {
        "date": "2027-06-25",
        "totalCashFlow": 52278.297829,
        "interestPayment": 3879.183411,
        "principalBalance": 9261641.07139,
        "principalPayment": 48399.114418,
        "endPrincipalBalance": 9261641.07139,
        "beginPrincipalBalance": 9310040.185808,
        "prepayPrincipalPayment": 23870.316917,
        "scheduledPrincipalPayment": 24528.797501
    }
    {
        "date": "2027-07-25",
        "totalCashFlow": 54945.056444,
        "interestPayment": 3859.017113,
        "principalBalance": 9210555.032058,
        "principalPayment": 51086.039331,
        "endPrincipalBalance": 9210555.032058,
        "beginPrincipalBalance": 9261641.07139,
        "prepayPrincipalPayment": 26594.813002,
        "scheduledPrincipalPayment": 24491.226329
    }
    {
        "date": "2027-08-25",
        "totalCashFlow": 53578.170436,
        "interestPayment": 3837.731263,
        "principalBalance": 9160814.592885,
        "principalPayment": 49740.439173,
        "endPrincipalBalance": 9160814.592885,
        "beginPrincipalBalance": 9210555.032058,
        "prepayPrincipalPayment": 25294.287648,
        "scheduledPrincipalPayment": 24446.151525
    }
    {
        "date": "2027-09-25",
        "totalCashFlow": 53767.659416,
        "interestPayment": 3817.00608,
        "principalBalance": 9110863.939549,
        "principalPayment": 49950.653336,
        "endPrincipalBalance": 9110863.939549,
        "beginPrincipalBalance": 9160814.592885,
        "prepayPrincipalPayment": 25546.420563,
        "scheduledPrincipalPayment": 24404.232773
    }
    {
        "date": "2027-10-25",
        "totalCashFlow": 52136.840621,
        "interestPayment": 3796.193308,
        "principalBalance": 9062523.292237,
        "principalPayment": 48340.647313,
        "endPrincipalBalance": 9062523.292237,
        "beginPrincipalBalance": 9110863.939549,
        "prepayPrincipalPayment": 23979.301496,
        "scheduledPrincipalPayment": 24361.345817
    }
    {
        "date": "2027-11-25",
        "totalCashFlow": 50431.951306,
        "interestPayment": 3776.051372,
        "principalBalance": 9015867.392303,
        "principalPayment": 46655.899934,
        "endPrincipalBalance": 9015867.392303,
        "beginPrincipalBalance": 9062523.292237,
        "prepayPrincipalPayment": 22333.534332,
        "scheduledPrincipalPayment": 24322.365602
    }
    {
        "date": "2027-12-25",
        "totalCashFlow": 50234.767014,
        "interestPayment": 3756.611413,
        "principalBalance": 8969389.236702,
        "principalPayment": 46478.1556,
        "endPrincipalBalance": 8969389.236702,
        "beginPrincipalBalance": 9015867.392303,
        "prepayPrincipalPayment": 22190.617748,
        "scheduledPrincipalPayment": 24287.537853
    }
    {
        "date": "2028-01-25",
        "totalCashFlow": 50522.135786,
        "interestPayment": 3737.245515,
        "principalBalance": 8922604.346432,
        "principalPayment": 46784.89027,
        "endPrincipalBalance": 8922604.346432,
        "beginPrincipalBalance": 8969389.236702,
        "prepayPrincipalPayment": 22532.055356,
        "scheduledPrincipalPayment": 24252.834915
    }
    {
        "date": "2028-02-25",
        "totalCashFlow": 46489.472956,
        "interestPayment": 3717.751811,
        "principalBalance": 8879832.625287,
        "principalPayment": 42771.721145,
        "endPrincipalBalance": 8879832.625287,
        "beginPrincipalBalance": 8922604.346432,
        "prepayPrincipalPayment": 18554.777373,
        "scheduledPrincipalPayment": 24216.943772
    }
    {
        "date": "2028-03-25",
        "totalCashFlow": 47550.997068,
        "interestPayment": 3699.930261,
        "principalBalance": 8835981.558479,
        "principalPayment": 43851.066808,
        "endPrincipalBalance": 8835981.558479,
        "beginPrincipalBalance": 8879832.625287,
        "prepayPrincipalPayment": 19659.446443,
        "scheduledPrincipalPayment": 24191.620364
    }
    {
        "date": "2028-04-25",
        "totalCashFlow": 51883.964591,
        "interestPayment": 3681.658983,
        "principalBalance": 8787779.252871,
        "principalPayment": 48202.305608,
        "endPrincipalBalance": 8787779.252871,
        "beginPrincipalBalance": 8835981.558479,
        "prepayPrincipalPayment": 24039.24677,
        "scheduledPrincipalPayment": 24163.058838
    }
    {
        "date": "2028-05-25",
        "totalCashFlow": 51165.743375,
        "interestPayment": 3661.574689,
        "principalBalance": 8740275.084185,
        "principalPayment": 47504.168687,
        "endPrincipalBalance": 8740275.084185,
        "beginPrincipalBalance": 8787779.252871,
        "prepayPrincipalPayment": 23381.927147,
        "scheduledPrincipalPayment": 24122.24154
    }
    {
        "date": "2028-06-25",
        "totalCashFlow": 55719.097174,
        "interestPayment": 3641.781285,
        "principalBalance": 8688197.768295,
        "principalPayment": 52077.315889,
        "endPrincipalBalance": 8688197.768295,
        "beginPrincipalBalance": 8740275.084185,
        "prepayPrincipalPayment": 27994.373545,
        "scheduledPrincipalPayment": 24082.942344
    }
    {
        "date": "2028-07-25",
        "totalCashFlow": 56819.152259,
        "interestPayment": 3620.082403,
        "principalBalance": 8634998.69844,
        "principalPayment": 53199.069856,
        "endPrincipalBalance": 8634998.69844,
        "beginPrincipalBalance": 8688197.768295,
        "prepayPrincipalPayment": 29168.470472,
        "scheduledPrincipalPayment": 24030.599384
    }
    {
        "date": "2028-08-25",
        "totalCashFlow": 54323.025402,
        "interestPayment": 3597.916124,
        "principalBalance": 8584273.589162,
        "principalPayment": 50725.109278,
        "endPrincipalBalance": 8584273.589162,
        "beginPrincipalBalance": 8634998.69844,
        "prepayPrincipalPayment": 26750.462834,
        "scheduledPrincipalPayment": 23974.646444
    }
    {
        "date": "2028-09-25",
        "totalCashFlow": 56701.102664,
        "interestPayment": 3576.780662,
        "principalBalance": 8531149.26716,
        "principalPayment": 53124.322002,
        "endPrincipalBalance": 8531149.26716,
        "beginPrincipalBalance": 8584273.589162,
        "prepayPrincipalPayment": 29199.25767,
        "scheduledPrincipalPayment": 23925.064332
    }
    {
        "date": "2028-10-25",
        "totalCashFlow": 52805.220215,
        "interestPayment": 3554.645528,
        "principalBalance": 8481898.692473,
        "principalPayment": 49250.574687,
        "endPrincipalBalance": 8481898.692473,
        "beginPrincipalBalance": 8531149.26716,
        "prepayPrincipalPayment": 25382.281561,
        "scheduledPrincipalPayment": 23868.293126
    }
    {
        "date": "2028-11-25",
        "totalCashFlow": 52749.889863,
        "interestPayment": 3534.124455,
        "principalBalance": 8432682.927066,
        "principalPayment": 49215.765407,
        "endPrincipalBalance": 8432682.927066,
        "beginPrincipalBalance": 8481898.692473,
        "prepayPrincipalPayment": 25393.896978,
        "scheduledPrincipalPayment": 23821.868429
    }
    {
        "date": "2028-12-25",
        "totalCashFlow": 51593.187717,
        "interestPayment": 3513.617886,
        "principalBalance": 8384603.357235,
        "principalPayment": 48079.569831,
        "endPrincipalBalance": 8384603.357235,
        "beginPrincipalBalance": 8432682.927066,
        "prepayPrincipalPayment": 24304.482452,
        "scheduledPrincipalPayment": 23775.087379
    }
    {
        "date": "2029-01-25",
        "totalCashFlow": 50992.947468,
        "interestPayment": 3493.584732,
        "principalBalance": 8337103.9945,
        "principalPayment": 47499.362735,
        "endPrincipalBalance": 8337103.9945,
        "beginPrincipalBalance": 8384603.357235,
        "prepayPrincipalPayment": 23768.298968,
        "scheduledPrincipalPayment": 23731.063768
    }
    {
        "date": "2029-02-25",
        "totalCashFlow": 48009.60611,
        "interestPayment": 3473.793331,
        "principalBalance": 8292568.18172,
        "principalPayment": 44535.812779,
        "endPrincipalBalance": 8292568.18172,
        "beginPrincipalBalance": 8337103.9945,
        "prepayPrincipalPayment": 20847.562127,
        "scheduledPrincipalPayment": 23688.250652
    }
    {
        "date": "2029-03-25",
        "totalCashFlow": 47671.240019,
        "interestPayment": 3455.236742,
        "principalBalance": 8248352.178444,
        "principalPayment": 44216.003276,
        "endPrincipalBalance": 8248352.178444,
        "beginPrincipalBalance": 8292568.18172,
        "prepayPrincipalPayment": 20562.542294,
        "scheduledPrincipalPayment": 23653.460982
    }
    {
        "date": "2029-04-25",
        "totalCashFlow": 52059.845403,
        "interestPayment": 3436.813408,
        "principalBalance": 8199729.146448,
        "principalPayment": 48623.031996,
        "endPrincipalBalance": 8199729.146448,
        "beginPrincipalBalance": 8248352.178444,
        "prepayPrincipalPayment": 25003.812987,
        "scheduledPrincipalPayment": 23619.219008
    }
    {
        "date": "2029-05-25",
        "totalCashFlow": 54179.621946,
        "interestPayment": 3416.553811,
        "principalBalance": 8148966.078314,
        "principalPayment": 50763.068135,
        "endPrincipalBalance": 8148966.078314,
        "beginPrincipalBalance": 8199729.146448,
        "prepayPrincipalPayment": 27191.124789,
        "scheduledPrincipalPayment": 23571.943345
    }
    {
        "date": "2029-06-25",
        "totalCashFlow": 57827.768994,
        "interestPayment": 3395.402533,
        "principalBalance": 8094533.711853,
        "principalPayment": 54432.366461,
        "endPrincipalBalance": 8094533.711853,
        "beginPrincipalBalance": 8148966.078314,
        "prepayPrincipalPayment": 30914.342953,
        "scheduledPrincipalPayment": 23518.023508
    }
    {
        "date": "2029-07-25",
        "totalCashFlow": 57650.842821,
        "interestPayment": 3372.72238,
        "principalBalance": 8040255.591411,
        "principalPayment": 54278.120441,
        "endPrincipalBalance": 8040255.591411,
        "beginPrincipalBalance": 8094533.711853,
        "prepayPrincipalPayment": 30825.169632,
        "scheduledPrincipalPayment": 23452.95081
    }
    {
        "date": "2029-08-25",
        "totalCashFlow": 57097.963859,
        "interestPayment": 3350.106496,
        "principalBalance": 7986507.734048,
        "principalPayment": 53747.857363,
        "endPrincipalBalance": 7986507.734048,
        "beginPrincipalBalance": 8040255.591411,
        "prepayPrincipalPayment": 30360.141494,
        "scheduledPrincipalPayment": 23387.715868
    }
    {
        "date": "2029-09-25",
        "totalCashFlow": 58375.410503,
        "interestPayment": 3327.711556,
        "principalBalance": 7931460.035102,
        "principalPayment": 55047.698947,
        "endPrincipalBalance": 7931460.035102,
        "beginPrincipalBalance": 7986507.734048,
        "prepayPrincipalPayment": 31724.283182,
        "scheduledPrincipalPayment": 23323.415765
    }
    {
        "date": "2029-10-25",
        "totalCashFlow": 52710.07247,
        "interestPayment": 3304.775015,
        "principalBalance": 7882054.737646,
        "principalPayment": 49405.297456,
        "endPrincipalBalance": 7882054.737646,
        "beginPrincipalBalance": 7931460.035102,
        "prepayPrincipalPayment": 26150.600688,
        "scheduledPrincipalPayment": 23254.696768
    }
    {
        "date": "2029-11-25",
        "totalCashFlow": 54633.378368,
        "interestPayment": 3284.189474,
        "principalBalance": 7830705.548752,
        "principalPayment": 51349.188894,
        "endPrincipalBalance": 7830705.548752,
        "beginPrincipalBalance": 7882054.737646,
        "prepayPrincipalPayment": 28147.246474,
        "scheduledPrincipalPayment": 23201.94242
    }
    {
        "date": "2029-12-25",
        "totalCashFlow": 52174.521902,
        "interestPayment": 3262.793979,
        "principalBalance": 7781793.820829,
        "principalPayment": 48911.727923,
        "endPrincipalBalance": 7781793.820829,
        "beginPrincipalBalance": 7830705.548752,
        "prepayPrincipalPayment": 25768.803392,
        "scheduledPrincipalPayment": 23142.924532
    }
    {
        "date": "2030-01-25",
        "totalCashFlow": 51364.879127,
        "interestPayment": 3242.414092,
        "principalBalance": 7733671.355794,
        "principalPayment": 48122.465035,
        "endPrincipalBalance": 7733671.355794,
        "beginPrincipalBalance": 7781793.820829,
        "prepayPrincipalPayment": 25031.89591,
        "scheduledPrincipalPayment": 23090.569126
    }
    {
        "date": "2030-02-25",
        "totalCashFlow": 47981.274788,
        "interestPayment": 3222.363065,
        "principalBalance": 7688912.444071,
        "principalPayment": 44758.911723,
        "endPrincipalBalance": 7688912.444071,
        "beginPrincipalBalance": 7733671.355794,
        "prepayPrincipalPayment": 21718.8646,
        "scheduledPrincipalPayment": 23040.047123
    }
    {
        "date": "2030-03-25",
        "totalCashFlow": 47445.546842,
        "interestPayment": 3203.713518,
        "principalBalance": 7644670.610747,
        "principalPayment": 44241.833324,
        "endPrincipalBalance": 7644670.610747,
        "beginPrincipalBalance": 7688912.444071,
        "prepayPrincipalPayment": 21242.751639,
        "scheduledPrincipalPayment": 22999.081685
    }
    {
        "date": "2030-04-25",
        "totalCashFlow": 51484.524111,
        "interestPayment": 3185.279421,
        "principalBalance": 7596371.366058,
        "principalPayment": 48299.24469,
        "endPrincipalBalance": 7596371.366058,
        "beginPrincipalBalance": 7644670.610747,
        "prepayPrincipalPayment": 25340.003988,
        "scheduledPrincipalPayment": 22959.240701
    }
    {
        "date": "2030-05-25",
        "totalCashFlow": 54595.089219,
        "interestPayment": 3165.154736,
        "principalBalance": 7544941.431575,
        "principalPayment": 51429.934483,
        "endPrincipalBalance": 7544941.431575,
        "beginPrincipalBalance": 7596371.366058,
        "prepayPrincipalPayment": 28523.190308,
        "scheduledPrincipalPayment": 22906.744174
    }
    {
        "date": "2030-06-25",
        "totalCashFlow": 57656.339632,
        "interestPayment": 3143.725596,
        "principalBalance": 7490428.81754,
        "principalPayment": 54512.614035,
        "endPrincipalBalance": 7490428.81754,
        "beginPrincipalBalance": 7544941.431575,
        "prepayPrincipalPayment": 31668.369939,
        "scheduledPrincipalPayment": 22844.244097
    }
    {
        "date": "2030-07-25",
        "totalCashFlow": 56078.158764,
        "interestPayment": 3121.012007,
        "principalBalance": 7437471.670783,
        "principalPayment": 52957.146757,
        "endPrincipalBalance": 7437471.670783,
        "beginPrincipalBalance": 7490428.81754,
        "prepayPrincipalPayment": 30185.382058,
        "scheduledPrincipalPayment": 22771.764699
    }
    {
        "date": "2030-08-25",
        "totalCashFlow": 58017.552668,
        "interestPayment": 3098.946529,
        "principalBalance": 7382553.064645,
        "principalPayment": 54918.606138,
        "endPrincipalBalance": 7382553.064645,
        "beginPrincipalBalance": 7437471.670783,
        "prepayPrincipalPayment": 32215.263598,
        "scheduledPrincipalPayment": 22703.34254
    }
    {
        "date": "2030-09-25",
        "totalCashFlow": 56787.971437,
        "interestPayment": 3076.063777,
        "principalBalance": 7328841.156985,
        "principalPayment": 53711.90766,
        "endPrincipalBalance": 7328841.156985,
        "beginPrincipalBalance": 7382553.064645,
        "prepayPrincipalPayment": 31083.658746,
        "scheduledPrincipalPayment": 22628.248914
    }
    {
        "date": "2030-10-25",
        "totalCashFlow": 53207.628744,
        "interestPayment": 3053.683815,
        "principalBalance": 7278687.212056,
        "principalPayment": 50153.944929,
        "endPrincipalBalance": 7278687.212056,
        "beginPrincipalBalance": 7328841.156985,
        "prepayPrincipalPayment": 27597.791856,
        "scheduledPrincipalPayment": 22556.153073
    }
    {
        "date": "2030-11-25",
        "totalCashFlow": 53967.169068,
        "interestPayment": 3032.786338,
        "principalBalance": 7227752.829327,
        "principalPayment": 50934.38273,
        "endPrincipalBalance": 7227752.829327,
        "beginPrincipalBalance": 7278687.212056,
        "prepayPrincipalPayment": 28440.023035,
        "scheduledPrincipalPayment": 22494.359694
    }
    {
        "date": "2030-12-25",
        "totalCashFlow": 50291.138143,
        "interestPayment": 3011.563679,
        "principalBalance": 7180473.254863,
        "principalPayment": 47279.574464,
        "endPrincipalBalance": 7180473.254863,
        "beginPrincipalBalance": 7227752.829327,
        "prepayPrincipalPayment": 24850.039689,
        "scheduledPrincipalPayment": 22429.534775
    }
    {
        "date": "2031-01-25",
        "totalCashFlow": 51512.65407,
        "interestPayment": 2991.863856,
        "principalBalance": 7131952.46465,
        "principalPayment": 48520.790214,
        "endPrincipalBalance": 7131952.46465,
        "beginPrincipalBalance": 7180473.254863,
        "prepayPrincipalPayment": 26145.327897,
        "scheduledPrincipalPayment": 22375.462317
    }
    {
        "date": "2031-02-25",
        "totalCashFlow": 46947.429024,
        "interestPayment": 2971.64686,
        "principalBalance": 7087976.682486,
        "principalPayment": 43975.782163,
        "endPrincipalBalance": 7087976.682486,
        "beginPrincipalBalance": 7131952.46465,
        "prepayPrincipalPayment": 21658.824757,
        "scheduledPrincipalPayment": 22316.957406
    }
    {
        "date": "2031-03-25",
        "totalCashFlow": 46359.183705,
        "interestPayment": 2953.323618,
        "principalBalance": 7044570.822399,
        "principalPayment": 43405.860087,
        "endPrincipalBalance": 7044570.822399,
        "beginPrincipalBalance": 7087976.682486,
        "prepayPrincipalPayment": 21133.713146,
        "scheduledPrincipalPayment": 22272.146941
    }
    {
        "date": "2031-04-25",
        "totalCashFlow": 50463.570747,
        "interestPayment": 2935.237843,
        "principalBalance": 6997042.489494,
        "principalPayment": 47528.332905,
        "endPrincipalBalance": 6997042.489494,
        "beginPrincipalBalance": 7044570.822399,
        "prepayPrincipalPayment": 25299.671796,
        "scheduledPrincipalPayment": 22228.661109
    }
    {
        "date": "2031-05-25",
        "totalCashFlow": 53620.365013,
        "interestPayment": 2915.434371,
        "principalBalance": 6946337.558852,
        "principalPayment": 50704.930642,
        "endPrincipalBalance": 6946337.558852,
        "beginPrincipalBalance": 6997042.489494,
        "prepayPrincipalPayment": 28533.282182,
        "scheduledPrincipalPayment": 22171.64846
    }
    {
        "date": "2031-06-25",
        "totalCashFlow": 55448.337901,
        "interestPayment": 2894.307316,
        "principalBalance": 6893783.528267,
        "principalPayment": 52554.030585,
        "endPrincipalBalance": 6893783.528267,
        "beginPrincipalBalance": 6946337.558852,
        "prepayPrincipalPayment": 30450.082445,
        "scheduledPrincipalPayment": 22103.94814
    }
    {
        "date": "2031-07-25",
        "totalCashFlow": 56398.344454,
        "interestPayment": 2872.409803,
        "principalBalance": 6840257.593617,
        "principalPayment": 53525.93465,
        "endPrincipalBalance": 6840257.593617,
        "beginPrincipalBalance": 6893783.528267,
        "prepayPrincipalPayment": 31496.267374,
        "scheduledPrincipalPayment": 22029.667277
    }
    {
        "date": "2031-08-25",
        "totalCashFlow": 56966.188441,
        "interestPayment": 2850.107331,
        "principalBalance": 6786141.512507,
        "principalPayment": 54116.08111,
        "endPrincipalBalance": 6786141.512507,
        "beginPrincipalBalance": 6840257.593617,
        "prepayPrincipalPayment": 32164.543087,
        "scheduledPrincipalPayment": 21951.538023
    }
    {
        "date": "2031-09-25",
        "totalCashFlow": 54418.102498,
        "interestPayment": 2827.558964,
        "principalBalance": 6734550.968972,
        "principalPayment": 51590.543534,
        "endPrincipalBalance": 6734550.968972,
        "beginPrincipalBalance": 6786141.512507,
        "prepayPrincipalPayment": 29719.800949,
        "scheduledPrincipalPayment": 21870.742585
    }
    {
        "date": "2031-10-25",
        "totalCashFlow": 53142.252714,
        "interestPayment": 2806.062904,
        "principalBalance": 6684214.779162,
        "principalPayment": 50336.18981,
        "endPrincipalBalance": 6684214.779162,
        "beginPrincipalBalance": 6734550.968972,
        "prepayPrincipalPayment": 28538.857565,
        "scheduledPrincipalPayment": 21797.332245
    }
    {
        "date": "2031-11-25",
        "totalCashFlow": 52666.379229,
        "interestPayment": 2785.089491,
        "principalBalance": 6634333.489425,
        "principalPayment": 49881.289737,
        "endPrincipalBalance": 6634333.489425,
        "beginPrincipalBalance": 6684214.779162,
        "prepayPrincipalPayment": 28154.018481,
        "scheduledPrincipalPayment": 21727.271257
    }
    {
        "date": "2031-12-25",
        "totalCashFlow": 47826.131919,
        "interestPayment": 2764.305621,
        "principalBalance": 6589271.663127,
        "principalPayment": 45061.826299,
        "endPrincipalBalance": 6589271.663127,
        "beginPrincipalBalance": 6634333.489425,
        "prepayPrincipalPayment": 23403.832163,
        "scheduledPrincipalPayment": 21657.994136
    }
    {
        "date": "2032-01-25",
        "totalCashFlow": 51144.691418,
        "interestPayment": 2745.52986,
        "principalBalance": 6540872.501568,
        "principalPayment": 48399.161558,
        "endPrincipalBalance": 6540872.501568,
        "beginPrincipalBalance": 6589271.663127,
        "prepayPrincipalPayment": 26795.339653,
        "scheduledPrincipalPayment": 21603.821905
    }
    {
        "date": "2032-02-25",
        "totalCashFlow": 44622.959229,
        "interestPayment": 2725.363542,
        "principalBalance": 6498974.905882,
        "principalPayment": 41897.595686,
        "endPrincipalBalance": 6498974.905882,
        "beginPrincipalBalance": 6540872.501568,
        "prepayPrincipalPayment": 20359.502756,
        "scheduledPrincipalPayment": 21538.09293
    }
    {
        "date": "2032-03-25",
        "totalCashFlow": 44826.511946,
        "interestPayment": 2707.906211,
        "principalBalance": 6456856.300147,
        "principalPayment": 42118.605735,
        "endPrincipalBalance": 6456856.300147,
        "beginPrincipalBalance": 6498974.905882,
        "prepayPrincipalPayment": 20625.40957,
        "scheduledPrincipalPayment": 21493.196165
    }
    {
        "date": "2032-04-25",
        "totalCashFlow": 50427.549487,
        "interestPayment": 2690.356792,
        "principalBalance": 6409119.107452,
        "principalPayment": 47737.192695,
        "endPrincipalBalance": 6409119.107452,
        "beginPrincipalBalance": 6456856.300147,
        "prepayPrincipalPayment": 26290.117087,
        "scheduledPrincipalPayment": 21447.075609
    }
    {
        "date": "2032-05-25",
        "totalCashFlow": 52619.649872,
        "interestPayment": 2670.466295,
        "principalBalance": 6359169.923874,
        "principalPayment": 49949.183577,
        "endPrincipalBalance": 6359169.923874,
        "beginPrincipalBalance": 6409119.107452,
        "prepayPrincipalPayment": 28567.474736,
        "scheduledPrincipalPayment": 21381.708842
    }
    {
        "date": "2032-06-25",
        "totalCashFlow": 52580.811692,
        "interestPayment": 2649.654135,
        "principalBalance": 6309238.766318,
        "principalPayment": 49931.157557,
        "endPrincipalBalance": 6309238.766318,
        "beginPrincipalBalance": 6359169.923874,
        "prepayPrincipalPayment": 28622.899777,
        "scheduledPrincipalPayment": 21308.25778
    }
    {
        "date": "2032-07-25",
        "totalCashFlow": 56093.030919,
        "interestPayment": 2628.849486,
        "principalBalance": 6255774.584885,
        "principalPayment": 53464.181433,
        "endPrincipalBalance": 6255774.584885,
        "beginPrincipalBalance": 6309238.766318,
        "prepayPrincipalPayment": 32230.059639,
        "scheduledPrincipalPayment": 21234.121794
    }
    {
        "date": "2032-08-25",
        "totalCashFlow": 53947.916974,
        "interestPayment": 2606.572744,
        "principalBalance": 6204433.240655,
        "principalPayment": 51341.34423,
        "endPrincipalBalance": 6204433.240655,
        "beginPrincipalBalance": 6255774.584885,
        "prepayPrincipalPayment": 30194.055435,
        "scheduledPrincipalPayment": 21147.288795
    }
    {
        "date": "2032-09-25",
        "totalCashFlow": 53847.389446,
        "interestPayment": 2585.180517,
        "principalBalance": 6153171.031726,
        "principalPayment": 51262.208929,
        "endPrincipalBalance": 6153171.031726,
        "beginPrincipalBalance": 6204433.240655,
        "prepayPrincipalPayment": 30195.413881,
        "scheduledPrincipalPayment": 21066.795048
    }
    {
        "date": "2032-10-25",
        "totalCashFlow": 51277.783217,
        "interestPayment": 2563.821263,
        "principalBalance": 6104457.069772,
        "principalPayment": 48713.961954,
        "endPrincipalBalance": 6104457.069772,
        "beginPrincipalBalance": 6153171.031726,
        "prepayPrincipalPayment": 27728.205586,
        "scheduledPrincipalPayment": 20985.756368
    }
    {
        "date": "2032-11-25",
        "totalCashFlow": 48595.298593,
        "interestPayment": 2543.523779,
        "principalBalance": 6058405.294958,
        "principalPayment": 46051.774814,
        "endPrincipalBalance": 6058405.294958,
        "beginPrincipalBalance": 6104457.069772,
        "prepayPrincipalPayment": 25139.149462,
        "scheduledPrincipalPayment": 20912.625352
    }
    {
        "date": "2032-12-25",
        "totalCashFlow": 48041.352152,
        "interestPayment": 2524.33554,
        "principalBalance": 6012888.278345,
        "principalPayment": 45517.016612,
        "endPrincipalBalance": 6012888.278345,
        "beginPrincipalBalance": 6058405.294958,
        "prepayPrincipalPayment": 24669.114944,
        "scheduledPrincipalPayment": 20847.901668
    }
    {
        "date": "2033-01-25",
        "totalCashFlow": 48056.969105,
        "interestPayment": 2505.370116,
        "principalBalance": 5967336.679357,
        "principalPayment": 45551.598989,
        "endPrincipalBalance": 5967336.679357,
        "beginPrincipalBalance": 6012888.278345,
        "prepayPrincipalPayment": 24767.252825,
        "scheduledPrincipalPayment": 20784.346163
    }
    {
        "date": "2033-02-25",
        "totalCashFlow": 42614.232352,
        "interestPayment": 2486.390283,
        "principalBalance": 5927208.837288,
        "principalPayment": 40127.842069,
        "endPrincipalBalance": 5927208.837288,
        "beginPrincipalBalance": 5967336.679357,
        "prepayPrincipalPayment": 19407.843281,
        "scheduledPrincipalPayment": 20719.998787
    }
    {
        "date": "2033-03-25",
        "totalCashFlow": 42764.1775,
        "interestPayment": 2469.670349,
        "principalBalance": 5886914.330137,
        "principalPayment": 40294.507151,
        "endPrincipalBalance": 5886914.330137,
        "beginPrincipalBalance": 5927208.837288,
        "prepayPrincipalPayment": 19620.618882,
        "scheduledPrincipalPayment": 20673.88827
    }
    {
        "date": "2033-04-25",
        "totalCashFlow": 48683.518573,
        "interestPayment": 2452.880971,
        "principalBalance": 5840683.692535,
        "principalPayment": 46230.637602,
        "endPrincipalBalance": 5840683.692535,
        "beginPrincipalBalance": 5886914.330137,
        "prepayPrincipalPayment": 25603.96111,
        "scheduledPrincipalPayment": 20626.676492
    }
    {
        "date": "2033-05-25",
        "totalCashFlow": 48616.422493,
        "interestPayment": 2433.618205,
        "principalBalance": 5794500.888247,
        "principalPayment": 46182.804287,
        "endPrincipalBalance": 5794500.888247,
        "beginPrincipalBalance": 5840683.692535,
        "prepayPrincipalPayment": 25624.762511,
        "scheduledPrincipalPayment": 20558.041777
    }
    {
        "date": "2033-06-25",
        "totalCashFlow": 51426.402836,
        "interestPayment": 2414.37537,
        "principalBalance": 5745488.860781,
        "principalPayment": 49012.027466,
        "endPrincipalBalance": 5745488.860781,
        "beginPrincipalBalance": 5794500.888247,
        "prepayPrincipalPayment": 28523.177987,
        "scheduledPrincipalPayment": 20488.849479
    }
    {
        "date": "2033-07-25",
        "totalCashFlow": 53544.251451,
        "interestPayment": 2393.953692,
        "principalBalance": 5694338.563022,
        "principalPayment": 51150.297759,
        "endPrincipalBalance": 5694338.563022,
        "beginPrincipalBalance": 5745488.860781,
        "prepayPrincipalPayment": 30741.424508,
        "scheduledPrincipalPayment": 20408.873251
    }
    {
        "date": "2033-08-25",
        "totalCashFlow": 50151.212446,
        "interestPayment": 2372.641068,
        "principalBalance": 5646559.991644,
        "principalPayment": 47778.571379,
        "endPrincipalBalance": 5646559.991644,
        "beginPrincipalBalance": 5694338.563022,
        "prepayPrincipalPayment": 27458.140649,
        "scheduledPrincipalPayment": 20320.430729
    }
    {
        "date": "2033-09-25",
        "totalCashFlow": 52431.698349,
        "interestPayment": 2352.73333,
        "principalBalance": 5596481.026625,
        "principalPayment": 50078.965019,
        "endPrincipalBalance": 5596481.026625,
        "beginPrincipalBalance": 5646559.991644,
        "prepayPrincipalPayment": 29835.805784,
        "scheduledPrincipalPayment": 20243.159235
    }
    {
        "date": "2033-10-25",
        "totalCashFlow": 48708.549508,
        "interestPayment": 2331.867094,
        "principalBalance": 5550104.344211,
        "principalPayment": 46376.682414,
        "endPrincipalBalance": 5550104.344211,
        "beginPrincipalBalance": 5596481.026625,
        "prepayPrincipalPayment": 26219.895861,
        "scheduledPrincipalPayment": 20156.786553
    }
    {
        "date": "2033-11-25",
        "totalCashFlow": 46076.016207,
        "interestPayment": 2312.543477,
        "principalBalance": 5506340.871481,
        "principalPayment": 43763.47273,
        "endPrincipalBalance": 5506340.871481,
        "beginPrincipalBalance": 5550104.344211,
        "prepayPrincipalPayment": 23680.565531,
        "scheduledPrincipalPayment": 20082.907199
    }
    {
        "date": "2033-12-25",
        "totalCashFlow": 45511.715382,
        "interestPayment": 2294.308696,
        "principalBalance": 5463123.464795,
        "principalPayment": 43217.406686,
        "endPrincipalBalance": 5463123.464795,
        "beginPrincipalBalance": 5506340.871481,
        "prepayPrincipalPayment": 23199.668064,
        "scheduledPrincipalPayment": 20017.738622
    }
    {
        "date": "2034-01-25",
        "totalCashFlow": 45488.73479,
        "interestPayment": 2276.301444,
        "principalBalance": 5419911.031449,
        "principalPayment": 43212.433347,
        "endPrincipalBalance": 5419911.031449,
        "beginPrincipalBalance": 5463123.464795,
        "prepayPrincipalPayment": 23258.578835,
        "scheduledPrincipalPayment": 19953.854512
    }
    {
        "date": "2034-02-25",
        "totalCashFlow": 40221.694264,
        "interestPayment": 2258.296263,
        "principalBalance": 5381947.633447,
        "principalPayment": 37963.398001,
        "endPrincipalBalance": 5381947.633447,
        "beginPrincipalBalance": 5419911.031449,
        "prepayPrincipalPayment": 18074.109549,
        "scheduledPrincipalPayment": 19889.288453
    }
    {
        "date": "2034-03-25",
        "totalCashFlow": 40463.277906,
        "interestPayment": 2242.478181,
        "principalBalance": 5343726.833722,
        "principalPayment": 38220.799725,
        "endPrincipalBalance": 5343726.833722,
        "beginPrincipalBalance": 5381947.633447,
        "prepayPrincipalPayment": 18377.432929,
        "scheduledPrincipalPayment": 19843.366797
    }
    {
        "date": "2034-04-25",
        "totalCashFlow": 46275.377459,
        "interestPayment": 2226.552847,
        "principalBalance": 5299678.009111,
        "principalPayment": 44048.824611,
        "endPrincipalBalance": 5299678.009111,
        "beginPrincipalBalance": 5343726.833722,
        "prepayPrincipalPayment": 24252.867258,
        "scheduledPrincipalPayment": 19795.957353
    }
    {
        "date": "2034-05-25",
        "totalCashFlow": 45801.601667,
        "interestPayment": 2208.19917,
        "principalBalance": 5256084.606614,
        "principalPayment": 43593.402497,
        "endPrincipalBalance": 5256084.606614,
        "beginPrincipalBalance": 5299678.009111,
        "prepayPrincipalPayment": 23867.09766,
        "scheduledPrincipalPayment": 19726.304836
    }
    {
        "date": "2034-06-25",
        "totalCashFlow": 50385.740195,
        "interestPayment": 2190.035253,
        "principalBalance": 5207888.901671,
        "principalPayment": 48195.704943,
        "endPrincipalBalance": 5207888.901671,
        "beginPrincipalBalance": 5256084.606614,
        "prepayPrincipalPayment": 28538.114066,
        "scheduledPrincipalPayment": 19657.590877
    }
    {
        "date": "2034-07-25",
        "totalCashFlow": 51379.554878,
        "interestPayment": 2169.953709,
        "principalBalance": 5158679.300503,
        "principalPayment": 49209.601169,
        "endPrincipalBalance": 5158679.300503,
        "beginPrincipalBalance": 5207888.901671,
        "prepayPrincipalPayment": 29638.77755,
        "scheduledPrincipalPayment": 19570.823619
    }
    {
        "date": "2034-08-25",
        "totalCashFlow": 48200.548301,
        "interestPayment": 2149.449709,
        "principalBalance": 5112628.20191,
        "principalPayment": 46051.098593,
        "endPrincipalBalance": 5112628.20191,
        "beginPrincipalBalance": 5158679.300503,
        "prepayPrincipalPayment": 26571.805414,
        "scheduledPrincipalPayment": 19479.293179
    }
    {
        "date": "2034-09-25",
        "totalCashFlow": 50557.098665,
        "interestPayment": 2130.261751,
        "principalBalance": 5064201.364996,
        "principalPayment": 48426.836914,
        "endPrincipalBalance": 5064201.364996,
        "beginPrincipalBalance": 5112628.20191,
        "prepayPrincipalPayment": 29028.073779,
        "scheduledPrincipalPayment": 19398.763135
    }
    {
        "date": "2034-10-25",
        "totalCashFlow": 45906.208905,
        "interestPayment": 2110.083902,
        "principalBalance": 5020405.239993,
        "principalPayment": 43796.125003,
        "endPrincipalBalance": 5020405.239993,
        "beginPrincipalBalance": 5064201.364996,
        "prepayPrincipalPayment": 24487.830242,
        "scheduledPrincipalPayment": 19308.294761
    }
    {
        "date": "2034-11-25",
        "totalCashFlow": 45533.149661,
        "interestPayment": 2091.835517,
        "principalBalance": 4976963.925848,
        "principalPayment": 43441.314144,
        "endPrincipalBalance": 4976963.925848,
        "beginPrincipalBalance": 5020405.239993,
        "prepayPrincipalPayment": 24206.726357,
        "scheduledPrincipalPayment": 19234.587787
    }
    {
        "date": "2034-12-25",
        "totalCashFlow": 44056.327602,
        "interestPayment": 2073.734969,
        "principalBalance": 4934981.333216,
        "principalPayment": 41982.592633,
        "endPrincipalBalance": 4934981.333216,
        "beginPrincipalBalance": 4976963.925848,
        "prepayPrincipalPayment": 22821.165279,
        "scheduledPrincipalPayment": 19161.427354
    }
    {
        "date": "2035-01-25",
        "totalCashFlow": 43146.848584,
        "interestPayment": 2056.242222,
        "principalBalance": 4893890.726854,
        "principalPayment": 41090.606362,
        "endPrincipalBalance": 4893890.726854,
        "beginPrincipalBalance": 4934981.333216,
        "prepayPrincipalPayment": 21997.512661,
        "scheduledPrincipalPayment": 19093.0937
    }
    {
        "date": "2035-02-25",
        "totalCashFlow": 39760.399208,
        "interestPayment": 2039.121136,
        "principalBalance": 4856169.448782,
        "principalPayment": 37721.278071,
        "endPrincipalBalance": 4856169.448782,
        "beginPrincipalBalance": 4893890.726854,
        "prepayPrincipalPayment": 18693.822101,
        "scheduledPrincipalPayment": 19027.455971
    }
    {
        "date": "2035-03-25",
        "totalCashFlow": 39199.657889,
        "interestPayment": 2023.403937,
        "principalBalance": 4818993.194831,
        "principalPayment": 37176.253952,
        "endPrincipalBalance": 4818993.194831,
        "beginPrincipalBalance": 4856169.448782,
        "prepayPrincipalPayment": 18202.019023,
        "scheduledPrincipalPayment": 18974.234929
    }
    {
        "date": "2035-04-25",
        "totalCashFlow": 43511.716519,
        "interestPayment": 2007.913831,
        "principalBalance": 4777489.392143,
        "principalPayment": 41503.802688,
        "endPrincipalBalance": 4777489.392143,
        "beginPrincipalBalance": 4818993.194831,
        "prepayPrincipalPayment": 22581.275992,
        "scheduledPrincipalPayment": 18922.526696
    }
    {
        "date": "2035-05-25",
        "totalCashFlow": 45490.818419,
        "interestPayment": 1990.62058,
        "principalBalance": 4733989.194304,
        "principalPayment": 43500.197839,
        "endPrincipalBalance": 4733989.194304,
        "beginPrincipalBalance": 4777489.392143,
        "prepayPrincipalPayment": 24647.071344,
        "scheduledPrincipalPayment": 18853.126495
    }
    {
        "date": "2035-06-25",
        "totalCashFlow": 48903.394077,
        "interestPayment": 1972.495498,
        "principalBalance": 4687058.295724,
        "principalPayment": 46930.898579,
        "endPrincipalBalance": 4687058.295724,
        "beginPrincipalBalance": 4733989.194304,
        "prepayPrincipalPayment": 28155.883767,
        "scheduledPrincipalPayment": 18775.014812
    }
    {
        "date": "2035-07-25",
        "totalCashFlow": 48571.623578,
        "interestPayment": 1952.940957,
        "principalBalance": 4640439.613102,
        "principalPayment": 46618.682622,
        "endPrincipalBalance": 4640439.613102,
        "beginPrincipalBalance": 4687058.295724,
        "prepayPrincipalPayment": 27936.338233,
        "scheduledPrincipalPayment": 18682.344389
    }
    {
        "date": "2035-08-25",
        "totalCashFlow": 47850.688367,
        "interestPayment": 1933.516505,
        "principalBalance": 4594522.441241,
        "principalPayment": 45917.171862,
        "endPrincipalBalance": 4594522.441241,
        "beginPrincipalBalance": 4640439.613102,
        "prepayPrincipalPayment": 27327.281411,
        "scheduledPrincipalPayment": 18589.890451
    }
    {
        "date": "2035-09-25",
        "totalCashFlow": 48896.845914,
        "interestPayment": 1914.384351,
        "principalBalance": 4547539.979677,
        "principalPayment": 46982.461563,
        "endPrincipalBalance": 4547539.979677,
        "beginPrincipalBalance": 4594522.441241,
        "prepayPrincipalPayment": 28483.236258,
        "scheduledPrincipalPayment": 18499.225305
    }
    {
        "date": "2035-10-25",
        "totalCashFlow": 43203.988519,
        "interestPayment": 1894.808325,
        "principalBalance": 4506230.799483,
        "principalPayment": 41309.180194,
        "endPrincipalBalance": 4506230.799483,
        "beginPrincipalBalance": 4547539.979677,
        "prepayPrincipalPayment": 22905.952345,
        "scheduledPrincipalPayment": 18403.227849
    }
    {
        "date": "2035-11-25",
        "totalCashFlow": 44868.540734,
        "interestPayment": 1877.596166,
        "principalBalance": 4463239.854916,
        "principalPayment": 42990.944567,
        "endPrincipalBalance": 4463239.854916,
        "beginPrincipalBalance": 4506230.799483,
        "prepayPrincipalPayment": 24661.717329,
        "scheduledPrincipalPayment": 18329.227238
    }
    {
        "date": "2035-12-25",
        "totalCashFlow": 42387.678598,
        "interestPayment": 1859.683273,
        "principalBalance": 4422711.859591,
        "principalPayment": 40527.995325,
        "endPrincipalBalance": 4422711.859591,
        "beginPrincipalBalance": 4463239.854916,
        "prepayPrincipalPayment": 22280.502016,
        "scheduledPrincipalPayment": 18247.493309
    }
    {
        "date": "2036-01-25",
        "totalCashFlow": 41466.062345,
        "interestPayment": 1842.796608,
        "principalBalance": 4383088.593854,
        "principalPayment": 39623.265737,
        "endPrincipalBalance": 4383088.593854,
        "beginPrincipalBalance": 4422711.859591,
        "prepayPrincipalPayment": 21448.325367,
        "scheduledPrincipalPayment": 18174.940369
    }
    {
        "date": "2036-02-25",
        "totalCashFlow": 38140.993989,
        "interestPayment": 1826.286914,
        "principalBalance": 4346773.886779,
        "principalPayment": 36314.707075,
        "endPrincipalBalance": 4346773.886779,
        "beginPrincipalBalance": 4383088.593854,
        "prepayPrincipalPayment": 18209.431327,
        "scheduledPrincipalPayment": 18105.275748
    }
    {
        "date": "2036-03-25",
        "totalCashFlow": 38371.579163,
        "interestPayment": 1811.155786,
        "principalBalance": 4310213.463403,
        "principalPayment": 36560.423376,
        "endPrincipalBalance": 4310213.463403,
        "beginPrincipalBalance": 4346773.886779,
        "prepayPrincipalPayment": 18511.896548,
        "scheduledPrincipalPayment": 18048.526828
    }
    {
        "date": "2036-04-25",
        "totalCashFlow": 41278.4664,
        "interestPayment": 1795.922276,
        "principalBalance": 4270730.919279,
        "principalPayment": 39482.544123,
        "endPrincipalBalance": 4270730.919279,
        "beginPrincipalBalance": 4310213.463403,
        "prepayPrincipalPayment": 21492.4821,
        "scheduledPrincipalPayment": 17990.062024
    }
    {
        "date": "2036-05-25",
        "totalCashFlow": 44156.38456,
        "interestPayment": 1779.471216,
        "principalBalance": 4228354.005935,
        "principalPayment": 42376.913344,
        "endPrincipalBalance": 4228354.005935,
        "beginPrincipalBalance": 4270730.919279,
        "prepayPrincipalPayment": 24458.287279,
        "scheduledPrincipalPayment": 17918.626065
    }
    {
        "date": "2036-06-25",
        "totalCashFlow": 45782.200722,
        "interestPayment": 1761.814169,
        "principalBalance": 4184333.619383,
        "principalPayment": 44020.386552,
        "endPrincipalBalance": 4184333.619383,
        "beginPrincipalBalance": 4228354.005935,
        "prepayPrincipalPayment": 26186.254148,
        "scheduledPrincipalPayment": 17834.132404
    }
    {
        "date": "2036-07-25",
        "totalCashFlow": 46584.226476,
        "interestPayment": 1743.472341,
        "principalBalance": 4139492.865248,
        "principalPayment": 44840.754134,
        "endPrincipalBalance": 4139492.865248,
        "beginPrincipalBalance": 4184333.619383,
        "prepayPrincipalPayment": 27099.074882,
        "scheduledPrincipalPayment": 17741.679253
    }
    {
        "date": "2036-08-25",
        "totalCashFlow": 47008.05892,
        "interestPayment": 1724.788694,
        "principalBalance": 4094209.595022,
        "principalPayment": 45283.270227,
        "endPrincipalBalance": 4094209.595022,
        "beginPrincipalBalance": 4139492.865248,
        "prepayPrincipalPayment": 27638.620268,
        "scheduledPrincipalPayment": 17644.649958
    }
    {
        "date": "2036-09-25",
        "totalCashFlow": 44594.582354,
        "interestPayment": 1705.920665,
        "principalBalance": 4051320.933332,
        "principalPayment": 42888.66169,
        "endPrincipalBalance": 4051320.933332,
        "beginPrincipalBalance": 4094209.595022,
        "prepayPrincipalPayment": 25344.069479,
        "scheduledPrincipalPayment": 17544.592211
    }
    {
        "date": "2036-10-25",
        "totalCashFlow": 43370.619838,
        "interestPayment": 1688.050389,
        "principalBalance": 4009638.363883,
        "principalPayment": 41682.569449,
        "endPrincipalBalance": 4009638.363883,
        "beginPrincipalBalance": 4051320.933332,
        "prepayPrincipalPayment": 24228.887572,
        "scheduledPrincipalPayment": 17453.681878
    }
    {
        "date": "2036-11-25",
        "totalCashFlow": 42821.111555,
        "interestPayment": 1670.682652,
        "principalBalance": 3968487.934979,
        "principalPayment": 41150.428904,
        "endPrincipalBalance": 3968487.934979,
        "beginPrincipalBalance": 4009638.363883,
        "prepayPrincipalPayment": 23783.508529,
        "scheduledPrincipalPayment": 17366.920374
    }
    {
        "date": "2036-12-25",
        "totalCashFlow": 38502.608513,
        "interestPayment": 1653.53664,
        "principalBalance": 3931638.863106,
        "principalPayment": 36849.071874,
        "endPrincipalBalance": 3931638.863106,
        "beginPrincipalBalance": 3968487.934979,
        "prepayPrincipalPayment": 19567.630206,
        "scheduledPrincipalPayment": 17281.441667
    }
    {
        "date": "2037-01-25",
        "totalCashFlow": 41310.169207,
        "interestPayment": 1638.18286,
        "principalBalance": 3891966.876758,
        "principalPayment": 39671.986348,
        "endPrincipalBalance": 3891966.876758,
        "beginPrincipalBalance": 3931638.863106,
        "prepayPrincipalPayment": 22458.215519,
        "scheduledPrincipalPayment": 17213.770829
    }
    {
        "date": "2037-02-25",
        "totalCashFlow": 35529.217557,
        "interestPayment": 1621.652865,
        "principalBalance": 3858059.312066,
        "principalPayment": 33907.564692,
        "endPrincipalBalance": 3858059.312066,
        "beginPrincipalBalance": 3891966.876758,
        "prepayPrincipalPayment": 16774.726226,
        "scheduledPrincipalPayment": 17132.838466
    }
    {
        "date": "2037-03-25",
        "totalCashFlow": 35664.057136,
        "interestPayment": 1607.524713,
        "principalBalance": 3824002.779644,
        "principalPayment": 34056.532422,
        "endPrincipalBalance": 3824002.779644,
        "beginPrincipalBalance": 3858059.312066,
        "prepayPrincipalPayment": 16980.095087,
        "scheduledPrincipalPayment": 17076.437335
    }
    {
        "date": "2037-04-25",
        "totalCashFlow": 40020.742873,
        "interestPayment": 1593.334492,
        "principalBalance": 3785575.371263,
        "principalPayment": 38427.408381,
        "endPrincipalBalance": 3785575.371263,
        "beginPrincipalBalance": 3824002.779644,
        "prepayPrincipalPayment": 21408.752699,
        "scheduledPrincipalPayment": 17018.655682
    }
    {
        "date": "2037-05-25",
        "totalCashFlow": 42333.660262,
        "interestPayment": 1577.323071,
        "principalBalance": 3744819.034072,
        "principalPayment": 40756.33719,
        "endPrincipalBalance": 3744819.034072,
        "beginPrincipalBalance": 3785575.371263,
        "prepayPrincipalPayment": 23815.758638,
        "scheduledPrincipalPayment": 16940.578552
    }
    {
        "date": "2037-06-25",
        "totalCashFlow": 42252.44392,
        "interestPayment": 1560.341264,
        "principalBalance": 3704126.931417,
        "principalPayment": 40692.102656,
        "endPrincipalBalance": 3704126.931417,
        "beginPrincipalBalance": 3744819.034072,
        "prepayPrincipalPayment": 23841.044591,
        "scheduledPrincipalPayment": 16851.058065
    }
    {
        "date": "2037-07-25",
        "totalCashFlow": 45193.169141,
        "interestPayment": 1543.386221,
        "principalBalance": 3660477.148497,
        "principalPayment": 43649.78292,
        "endPrincipalBalance": 3660477.148497,
        "beginPrincipalBalance": 3704126.931417,
        "prepayPrincipalPayment": 26889.049557,
        "scheduledPrincipalPayment": 16760.733362
    }
    {
        "date": "2037-08-25",
        "totalCashFlow": 44355.462499,
        "interestPayment": 1525.198812,
        "principalBalance": 3617646.884809,
        "principalPayment": 42830.263687,
        "endPrincipalBalance": 3617646.884809,
        "beginPrincipalBalance": 3660477.148497,
        "prepayPrincipalPayment": 26174.421335,
        "scheduledPrincipalPayment": 16655.842353
    }
    {
        "date": "2037-09-25",
        "totalCashFlow": 42017.744527,
        "interestPayment": 1507.352869,
        "principalBalance": 3577136.493151,
        "principalPayment": 40510.391658,
        "endPrincipalBalance": 3577136.493151,
        "beginPrincipalBalance": 3617646.884809,
        "prepayPrincipalPayment": 23956.966912,
        "scheduledPrincipalPayment": 16553.424747
    }
    {
        "date": "2037-10-25",
        "totalCashFlow": 40813.005819,
        "interestPayment": 1490.473539,
        "principalBalance": 3537813.960871,
        "principalPayment": 39322.53228,
        "endPrincipalBalance": 3537813.960871,
        "beginPrincipalBalance": 3577136.493151,
        "prepayPrincipalPayment": 22862.103938,
        "scheduledPrincipalPayment": 16460.428342
    }
    {
        "date": "2037-11-25",
        "totalCashFlow": 39348.236222,
        "interestPayment": 1474.08915,
        "principalBalance": 3499939.8138,
        "principalPayment": 37874.147071,
        "endPrincipalBalance": 3499939.8138,
        "beginPrincipalBalance": 3537813.960871,
        "prepayPrincipalPayment": 21502.370343,
        "scheduledPrincipalPayment": 16371.776729
    }
    {
        "date": "2037-12-25",
        "totalCashFlow": 37050.01069,
        "interestPayment": 1458.308256,
        "principalBalance": 3464348.111365,
        "principalPayment": 35591.702434,
        "endPrincipalBalance": 3464348.111365,
        "beginPrincipalBalance": 3499939.8138,
        "prepayPrincipalPayment": 19302.944039,
        "scheduledPrincipalPayment": 16288.758395
    }
    {
        "date": "2038-01-25",
        "totalCashFlow": 38729.6068,
        "interestPayment": 1443.47838,
        "principalBalance": 3427061.982945,
        "principalPayment": 37286.12842,
        "endPrincipalBalance": 3427061.982945,
        "beginPrincipalBalance": 3464348.111365,
        "prepayPrincipalPayment": 21070.752753,
        "scheduledPrincipalPayment": 16215.375667
    }
    {
        "date": "2038-02-25",
        "totalCashFlow": 32632.516442,
        "interestPayment": 1427.942493,
        "principalBalance": 3395857.408996,
        "principalPayment": 31204.573949,
        "endPrincipalBalance": 3395857.408996,
        "beginPrincipalBalance": 3427061.982945,
        "prepayPrincipalPayment": 15071.498945,
        "scheduledPrincipalPayment": 16133.075004
    }
    {
        "date": "2038-03-25",
        "totalCashFlow": 33385.979992,
        "interestPayment": 1414.940587,
        "principalBalance": 3363886.369591,
        "principalPayment": 31971.039405,
        "endPrincipalBalance": 3363886.369591,
        "beginPrincipalBalance": 3395857.408996,
        "prepayPrincipalPayment": 15892.518826,
        "scheduledPrincipalPayment": 16078.520579
    }
    {
        "date": "2038-04-25",
        "totalCashFlow": 38192.34559,
        "interestPayment": 1401.619321,
        "principalBalance": 3327095.643322,
        "principalPayment": 36790.726269,
        "endPrincipalBalance": 3327095.643322,
        "beginPrincipalBalance": 3363886.369591,
        "prepayPrincipalPayment": 20771.140989,
        "scheduledPrincipalPayment": 16019.58528
    }
    {
        "date": "2038-05-25",
        "totalCashFlow": 39033.610028,
        "interestPayment": 1386.289851,
        "principalBalance": 3289448.323145,
        "principalPayment": 37647.320176,
        "endPrincipalBalance": 3289448.323145,
        "beginPrincipalBalance": 3327095.643322,
        "prepayPrincipalPayment": 21710.541535,
        "scheduledPrincipalPayment": 15936.778642
    }
    {
        "date": "2038-06-25",
        "totalCashFlow": 39369.923164,
        "interestPayment": 1370.603468,
        "principalBalance": 3251449.003449,
        "principalPayment": 37999.319696,
        "endPrincipalBalance": 3251449.003449,
        "beginPrincipalBalance": 3289448.323145,
        "prepayPrincipalPayment": 22150.543049,
        "scheduledPrincipalPayment": 15848.776647
    }
    {
        "date": "2038-07-25",
        "totalCashFlow": 42041.040751,
        "interestPayment": 1354.770418,
        "principalBalance": 3210762.733116,
        "principalPayment": 40686.270333,
        "endPrincipalBalance": 3210762.733116,
        "beginPrincipalBalance": 3251449.003449,
        "prepayPrincipalPayment": 24928.335699,
        "scheduledPrincipalPayment": 15757.934634
    }
    {
        "date": "2038-08-25",
        "totalCashFlow": 40209.930452,
        "interestPayment": 1337.817805,
        "principalBalance": 3171890.620469,
        "principalPayment": 38872.112647,
        "endPrincipalBalance": 3171890.620469,
        "beginPrincipalBalance": 3210762.733116,
        "prepayPrincipalPayment": 23219.291871,
        "scheduledPrincipalPayment": 15652.820776
    }
    {
        "date": "2038-09-25",
        "totalCashFlow": 39980.30513,
        "interestPayment": 1321.621092,
        "principalBalance": 3133231.936431,
        "principalPayment": 38658.684038,
        "endPrincipalBalance": 3133231.936431,
        "beginPrincipalBalance": 3171890.620469,
        "prepayPrincipalPayment": 23103.427877,
        "scheduledPrincipalPayment": 15555.256161
    }
    {
        "date": "2038-10-25",
        "totalCashFlow": 37879.767856,
        "interestPayment": 1305.513307,
        "principalBalance": 3096657.681882,
        "principalPayment": 36574.254549,
        "endPrincipalBalance": 3096657.681882,
        "beginPrincipalBalance": 3133231.936431,
        "prepayPrincipalPayment": 21116.773408,
        "scheduledPrincipalPayment": 15457.481141
    }
    {
        "date": "2038-11-25",
        "totalCashFlow": 35688.708609,
        "interestPayment": 1290.274034,
        "principalBalance": 3062259.247308,
        "principalPayment": 34398.434575,
        "endPrincipalBalance": 3062259.247308,
        "beginPrincipalBalance": 3096657.681882,
        "prepayPrincipalPayment": 19029.654899,
        "scheduledPrincipalPayment": 15368.779676
    }
    {
        "date": "2038-12-25",
        "totalCashFlow": 35201.301402,
        "interestPayment": 1275.941353,
        "principalBalance": 3028333.887259,
        "principalPayment": 33925.360049,
        "endPrincipalBalance": 3028333.887259,
        "beginPrincipalBalance": 3062259.247308,
        "prepayPrincipalPayment": 18635.58576,
        "scheduledPrincipalPayment": 15289.77429
    }
    {
        "date": "2039-01-25",
        "totalCashFlow": 35112.713994,
        "interestPayment": 1261.805786,
        "principalBalance": 2994482.979051,
        "principalPayment": 33850.908207,
        "endPrincipalBalance": 2994482.979051,
        "beginPrincipalBalance": 3028333.887259,
        "prepayPrincipalPayment": 18638.818347,
        "scheduledPrincipalPayment": 15212.08986
    }
    {
        "date": "2039-02-25",
        "totalCashFlow": 30888.95432,
        "interestPayment": 1247.701241,
        "principalBalance": 2964841.725972,
        "principalPayment": 29641.253079,
        "endPrincipalBalance": 2964841.725972,
        "beginPrincipalBalance": 2994482.979051,
        "prepayPrincipalPayment": 14507.515518,
        "scheduledPrincipalPayment": 15133.737561
    }
    {
        "date": "2039-03-25",
        "totalCashFlow": 30971.072463,
        "interestPayment": 1235.350719,
        "principalBalance": 2935106.004228,
        "principalPayment": 29735.721744,
        "endPrincipalBalance": 2935106.004228,
        "beginPrincipalBalance": 2964841.725972,
        "prepayPrincipalPayment": 14659.988209,
        "scheduledPrincipalPayment": 15075.733536
    }
    {
        "date": "2039-04-25",
        "totalCashFlow": 35368.658961,
        "interestPayment": 1222.960835,
        "principalBalance": 2900960.306103,
        "principalPayment": 34145.698126,
        "endPrincipalBalance": 2900960.306103,
        "beginPrincipalBalance": 2935106.004228,
        "prepayPrincipalPayment": 19129.263361,
        "scheduledPrincipalPayment": 15016.434765
    }
    {
        "date": "2039-05-25",
        "totalCashFlow": 35313.891682,
        "interestPayment": 1208.733461,
        "principalBalance": 2866855.147881,
        "principalPayment": 34105.158221,
        "endPrincipalBalance": 2866855.147881,
        "beginPrincipalBalance": 2900960.306103,
        "prepayPrincipalPayment": 19171.55522,
        "scheduledPrincipalPayment": 14933.603002
    }
    {
        "date": "2039-06-25",
        "totalCashFlow": 37367.218056,
        "interestPayment": 1194.522978,
        "principalBalance": 2830682.452804,
        "principalPayment": 36172.695077,
        "endPrincipalBalance": 2830682.452804,
        "beginPrincipalBalance": 2866855.147881,
        "prepayPrincipalPayment": 21322.841843,
        "scheduledPrincipalPayment": 14849.853235
    }
    {
        "date": "2039-07-25",
        "totalCashFlow": 38876.537232,
        "interestPayment": 1179.451022,
        "principalBalance": 2792985.366593,
        "principalPayment": 37697.08621,
        "endPrincipalBalance": 2792985.366593,
        "beginPrincipalBalance": 2830682.452804,
        "prepayPrincipalPayment": 22942.904041,
        "scheduledPrincipalPayment": 14754.182169
    }
    {
        "date": "2039-08-25",
        "totalCashFlow": 36266.22216,
        "interestPayment": 1163.743903,
        "principalBalance": 2757882.888336,
        "principalPayment": 35102.478257,
        "endPrincipalBalance": 2757882.888336,
        "beginPrincipalBalance": 2792985.366593,
        "prepayPrincipalPayment": 20453.26274,
        "scheduledPrincipalPayment": 14649.215517
    }
    {
        "date": "2039-09-25",
        "totalCashFlow": 37835.855237,
        "interestPayment": 1149.11787,
        "principalBalance": 2721196.150969,
        "principalPayment": 36686.737367,
        "endPrincipalBalance": 2721196.150969,
        "beginPrincipalBalance": 2757882.888336,
        "prepayPrincipalPayment": 22130.21764,
        "scheduledPrincipalPayment": 14556.519727
    }
    {
        "date": "2039-10-25",
        "totalCashFlow": 34999.316506,
        "interestPayment": 1133.83173,
        "principalBalance": 2687330.666193,
        "principalPayment": 33865.484777,
        "endPrincipalBalance": 2687330.666193,
        "beginPrincipalBalance": 2721196.150969,
        "prepayPrincipalPayment": 19411.350731,
        "scheduledPrincipalPayment": 14454.134046
    }
    {
        "date": "2039-11-25",
        "totalCashFlow": 32967.906702,
        "interestPayment": 1119.721111,
        "principalBalance": 2655482.480601,
        "principalPayment": 31848.185592,
        "endPrincipalBalance": 2655482.480601,
        "beginPrincipalBalance": 2687330.666193,
        "prepayPrincipalPayment": 17482.76069,
        "scheduledPrincipalPayment": 14365.424901
    }
    {
        "date": "2039-12-25",
        "totalCashFlow": 32497.382496,
        "interestPayment": 1106.451034,
        "principalBalance": 2624091.549138,
        "principalPayment": 31390.931463,
        "endPrincipalBalance": 2624091.549138,
        "beginPrincipalBalance": 2655482.480601,
        "prepayPrincipalPayment": 17104.598756,
        "scheduledPrincipalPayment": 14286.332706
    }
    {
        "date": "2040-01-25",
        "totalCashFlow": 32385.898891,
        "interestPayment": 1093.371479,
        "principalBalance": 2592799.021727,
        "principalPayment": 31292.527412,
        "endPrincipalBalance": 2592799.021727,
        "beginPrincipalBalance": 2624091.549138,
        "prepayPrincipalPayment": 17083.928923,
        "scheduledPrincipalPayment": 14208.598489
    }
    {
        "date": "2040-02-25",
        "totalCashFlow": 28534.837552,
        "interestPayment": 1080.332926,
        "principalBalance": 2565344.517101,
        "principalPayment": 27454.504626,
        "endPrincipalBalance": 2565344.517101,
        "beginPrincipalBalance": 2592799.021727,
        "prepayPrincipalPayment": 13324.209896,
        "scheduledPrincipalPayment": 14130.29473
    }
    {
        "date": "2040-03-25",
        "totalCashFlow": 29159.066126,
        "interestPayment": 1068.893549,
        "principalBalance": 2537254.344524,
        "principalPayment": 28090.172577,
        "endPrincipalBalance": 2537254.344524,
        "beginPrincipalBalance": 2565344.517101,
        "prepayPrincipalPayment": 14018.24733,
        "scheduledPrincipalPayment": 14071.925247
    }
    {
        "date": "2040-04-25",
        "totalCashFlow": 31516.8106,
        "interestPayment": 1057.18931,
        "principalBalance": 2506794.723234,
        "principalPayment": 30459.62129,
        "endPrincipalBalance": 2506794.723234,
        "beginPrincipalBalance": 2537254.344524,
        "prepayPrincipalPayment": 16450.438067,
        "scheduledPrincipalPayment": 14009.183223
    }
    {
        "date": "2040-05-25",
        "totalCashFlow": 32805.095436,
        "interestPayment": 1044.497801,
        "principalBalance": 2475034.1256,
        "principalPayment": 31760.597634,
        "endPrincipalBalance": 2475034.1256,
        "beginPrincipalBalance": 2506794.723234,
        "prepayPrincipalPayment": 17828.250306,
        "scheduledPrincipalPayment": 13932.347329
    }
    {
        "date": "2040-06-25",
        "totalCashFlow": 35056.954331,
        "interestPayment": 1031.264219,
        "principalBalance": 2441008.435487,
        "principalPayment": 34025.690112,
        "endPrincipalBalance": 2441008.435487,
        "beginPrincipalBalance": 2475034.1256,
        "prepayPrincipalPayment": 20178.573942,
        "scheduledPrincipalPayment": 13847.11617
    }
    {
        "date": "2040-07-25",
        "totalCashFlow": 34659.531714,
        "interestPayment": 1017.086848,
        "principalBalance": 2407365.990621,
        "principalPayment": 33642.444866,
        "endPrincipalBalance": 2407365.990621,
        "beginPrincipalBalance": 2441008.435487,
        "prepayPrincipalPayment": 19894.551452,
        "scheduledPrincipalPayment": 13747.893414
    }
    {
        "date": "2040-08-25",
        "totalCashFlow": 33981.391061,
        "interestPayment": 1003.069163,
        "principalBalance": 2374387.668723,
        "principalPayment": 32978.321898,
        "endPrincipalBalance": 2374387.668723,
        "beginPrincipalBalance": 2407365.990621,
        "prepayPrincipalPayment": 19328.906973,
        "scheduledPrincipalPayment": 13649.414924
    }
    {
        "date": "2040-09-25",
        "totalCashFlow": 34503.685984,
        "interestPayment": 989.328195,
        "principalBalance": 2340873.310934,
        "principalPayment": 33514.357789,
        "endPrincipalBalance": 2340873.310934,
        "beginPrincipalBalance": 2374387.668723,
        "prepayPrincipalPayment": 19961.056538,
        "scheduledPrincipalPayment": 13553.301251
    }
    {
        "date": "2040-10-25",
        "totalCashFlow": 30473.380558,
        "interestPayment": 975.36388,
        "principalBalance": 2311375.294256,
        "principalPayment": 29498.016679,
        "endPrincipalBalance": 2311375.294256,
        "beginPrincipalBalance": 2340873.310934,
        "prepayPrincipalPayment": 16045.311096,
        "scheduledPrincipalPayment": 13452.705582
    }
    {
        "date": "2040-11-25",
        "totalCashFlow": 31421.481934,
        "interestPayment": 963.073039,
        "principalBalance": 2280916.885361,
        "principalPayment": 30458.408895,
        "endPrincipalBalance": 2280916.885361,
        "beginPrincipalBalance": 2311375.294256,
        "prepayPrincipalPayment": 17084.530062,
        "scheduledPrincipalPayment": 13373.878833
    }
    {
        "date": "2040-12-25",
        "totalCashFlow": 29631.540699,
        "interestPayment": 950.382036,
        "principalBalance": 2252235.726697,
        "principalPayment": 28681.158664,
        "endPrincipalBalance": 2252235.726697,
        "beginPrincipalBalance": 2280916.885361,
        "prepayPrincipalPayment": 15392.880605,
        "scheduledPrincipalPayment": 13288.278059
    }
    {
        "date": "2041-01-25",
        "totalCashFlow": 28873.914182,
        "interestPayment": 938.431553,
        "principalBalance": 2224300.244067,
        "principalPayment": 27935.48263,
        "endPrincipalBalance": 2224300.244067,
        "beginPrincipalBalance": 2252235.726697,
        "prepayPrincipalPayment": 14723.658682,
        "scheduledPrincipalPayment": 13211.823948
    }
    {
        "date": "2041-02-25",
        "totalCashFlow": 26541.339358,
        "interestPayment": 926.791768,
        "principalBalance": 2198685.696478,
        "principalPayment": 25614.547589,
        "endPrincipalBalance": 2198685.696478,
        "beginPrincipalBalance": 2224300.244067,
        "prepayPrincipalPayment": 12475.93182,
        "scheduledPrincipalPayment": 13138.615769
    }
    {
        "date": "2041-03-25",
        "totalCashFlow": 26072.297824,
        "interestPayment": 916.11904,
        "principalBalance": 2173529.517695,
        "principalPayment": 25156.178783,
        "endPrincipalBalance": 2173529.517695,
        "beginPrincipalBalance": 2198685.696478,
        "prepayPrincipalPayment": 12078.085562,
        "scheduledPrincipalPayment": 13078.093222
    }
    {
        "date": "2041-04-25",
        "totalCashFlow": 28348.145042,
        "interestPayment": 905.637299,
        "principalBalance": 2146087.009951,
        "principalPayment": 27442.507743,
        "endPrincipalBalance": 2146087.009951,
        "beginPrincipalBalance": 2173529.517695,
        "prepayPrincipalPayment": 14423.138835,
        "scheduledPrincipalPayment": 13019.368908
    }
    {
        "date": "2041-05-25",
        "totalCashFlow": 30072.317963,
        "interestPayment": 894.202921,
        "principalBalance": 2116908.894909,
        "principalPayment": 29178.115042,
        "endPrincipalBalance": 2116908.894909,
        "beginPrincipalBalance": 2146087.009951,
        "prepayPrincipalPayment": 16232.189562,
        "scheduledPrincipalPayment": 12945.925481
    }
    {
        "date": "2041-06-25",
        "totalCashFlow": 31683.604979,
        "interestPayment": 882.045373,
        "principalBalance": 2086107.335303,
        "principalPayment": 30801.559606,
        "endPrincipalBalance": 2086107.335303,
        "beginPrincipalBalance": 2116908.894909,
        "prepayPrincipalPayment": 17940.763742,
        "scheduledPrincipalPayment": 12860.795864
    }
    {
        "date": "2041-07-25",
        "totalCashFlow": 30532.60437,
        "interestPayment": 869.21139,
        "principalBalance": 2056443.942323,
        "principalPayment": 29663.39298,
        "endPrincipalBalance": 2056443.942323,
        "beginPrincipalBalance": 2086107.335303,
        "prepayPrincipalPayment": 16898.975913,
        "scheduledPrincipalPayment": 12764.417067
    }
    {
        "date": "2041-08-25",
        "totalCashFlow": 31390.558456,
        "interestPayment": 856.851643,
        "principalBalance": 2025910.23551,
        "principalPayment": 30533.706813,
        "endPrincipalBalance": 2025910.23551,
        "beginPrincipalBalance": 2056443.942323,
        "prepayPrincipalPayment": 17860.139429,
        "scheduledPrincipalPayment": 12673.567384
    }
    {
        "date": "2041-09-25",
        "totalCashFlow": 30395.411418,
        "interestPayment": 844.129265,
        "principalBalance": 1996358.953357,
        "principalPayment": 29551.282153,
        "endPrincipalBalance": 1996358.953357,
        "beginPrincipalBalance": 2025910.23551,
        "prepayPrincipalPayment": 16975.380515,
        "scheduledPrincipalPayment": 12575.901638
    }
    {
        "date": "2041-10-25",
        "totalCashFlow": 28160.043807,
        "interestPayment": 831.816231,
        "principalBalance": 1969030.72578,
        "principalPayment": 27328.227577,
        "endPrincipalBalance": 1969030.72578,
        "beginPrincipalBalance": 1996358.953357,
        "prepayPrincipalPayment": 14845.369907,
        "scheduledPrincipalPayment": 12482.857669
    }
    {
        "date": "2041-11-25",
        "totalCashFlow": 28298.903862,
        "interestPayment": 820.429469,
        "principalBalance": 1941552.251388,
        "principalPayment": 27478.474393,
        "endPrincipalBalance": 1941552.251388,
        "beginPrincipalBalance": 1969030.72578,
        "prepayPrincipalPayment": 15076.12043,
        "scheduledPrincipalPayment": 12402.353963
    }
    {
        "date": "2041-12-25",
        "totalCashFlow": 26137.224473,
        "interestPayment": 808.980105,
        "principalBalance": 1916224.007019,
        "principalPayment": 25328.244368,
        "endPrincipalBalance": 1916224.007019,
        "beginPrincipalBalance": 1941552.251388,
        "prepayPrincipalPayment": 13008.632862,
        "scheduledPrincipalPayment": 12319.611506
    }
    {
        "date": "2042-01-25",
        "totalCashFlow": 26557.424257,
        "interestPayment": 798.42667,
        "principalBalance": 1890465.009432,
        "principalPayment": 25758.997587,
        "endPrincipalBalance": 1890465.009432,
        "beginPrincipalBalance": 1916224.007019,
        "prepayPrincipalPayment": 13509.709657,
        "scheduledPrincipalPayment": 12249.287931
    }
    {
        "date": "2042-02-25",
        "totalCashFlow": 23961.46663,
        "interestPayment": 787.693754,
        "principalBalance": 1867291.236555,
        "principalPayment": 23173.772876,
        "endPrincipalBalance": 1867291.236555,
        "beginPrincipalBalance": 1890465.009432,
        "prepayPrincipalPayment": 10998.730997,
        "scheduledPrincipalPayment": 12175.041879
    }
    {
        "date": "2042-03-25",
        "totalCashFlow": 23528.557055,
        "interestPayment": 778.038015,
        "principalBalance": 1844540.717516,
        "principalPayment": 22750.519039,
        "endPrincipalBalance": 1844540.717516,
        "beginPrincipalBalance": 1867291.236555,
        "prepayPrincipalPayment": 10634.162666,
        "scheduledPrincipalPayment": 12116.356374
    }
    {
        "date": "2042-04-25",
        "totalCashFlow": 25455.250177,
        "interestPayment": 768.558632,
        "principalBalance": 1819854.025971,
        "principalPayment": 24686.691545,
        "endPrincipalBalance": 1819854.025971,
        "beginPrincipalBalance": 1844540.717516,
        "prepayPrincipalPayment": 12627.239229,
        "scheduledPrincipalPayment": 12059.452316
    }
    {
        "date": "2042-05-25",
        "totalCashFlow": 27180.194391,
        "interestPayment": 758.272511,
        "principalBalance": 1793432.104091,
        "principalPayment": 26421.921881,
        "endPrincipalBalance": 1793432.104091,
        "beginPrincipalBalance": 1819854.025971,
        "prepayPrincipalPayment": 14433.093322,
        "scheduledPrincipalPayment": 11988.828559
    }
    {
        "date": "2042-06-25",
        "totalCashFlow": 27617.521486,
        "interestPayment": 747.263377,
        "principalBalance": 1766561.845982,
        "principalPayment": 26870.258109,
        "endPrincipalBalance": 1766561.845982,
        "beginPrincipalBalance": 1793432.104091,
        "prepayPrincipalPayment": 14964.753711,
        "scheduledPrincipalPayment": 11905.504398
    }
    {
        "date": "2042-07-25",
        "totalCashFlow": 27868.968949,
        "interestPayment": 736.067436,
        "principalBalance": 1739428.944468,
        "principalPayment": 27132.901513,
        "endPrincipalBalance": 1739428.944468,
        "beginPrincipalBalance": 1766561.845982,
        "prepayPrincipalPayment": 15315.105492,
        "scheduledPrincipalPayment": 11817.796021
    }
    {
        "date": "2042-08-25",
        "totalCashFlow": 27898.121784,
        "interestPayment": 724.76206,
        "principalBalance": 1712255.584745,
        "principalPayment": 27173.359724,
        "endPrincipalBalance": 1712255.584745,
        "beginPrincipalBalance": 1739428.944468,
        "prepayPrincipalPayment": 15446.504639,
        "scheduledPrincipalPayment": 11726.855085
    }
    {
        "date": "2042-09-25",
        "totalCashFlow": 26433.607346,
        "interestPayment": 713.439827,
        "principalBalance": 1686535.417226,
        "principalPayment": 25720.167519,
        "endPrincipalBalance": 1686535.417226,
        "beginPrincipalBalance": 1712255.584745,
        "prepayPrincipalPayment": 14086.050012,
        "scheduledPrincipalPayment": 11634.117507
    }
    {
        "date": "2042-10-25",
        "totalCashFlow": 25626.047114,
        "interestPayment": 702.723091,
        "principalBalance": 1661612.093203,
        "principalPayment": 24923.324024,
        "endPrincipalBalance": 1661612.093203,
        "beginPrincipalBalance": 1686535.417226,
        "prepayPrincipalPayment": 13373.552067,
        "scheduledPrincipalPayment": 11549.771956
    }
    {
        "date": "2042-11-25",
        "totalCashFlow": 25168.148641,
        "interestPayment": 692.338372,
        "principalBalance": 1637136.282934,
        "principalPayment": 24475.810269,
        "endPrincipalBalance": 1637136.282934,
        "beginPrincipalBalance": 1661612.093203,
        "prepayPrincipalPayment": 13006.319956,
        "scheduledPrincipalPayment": 11469.490313
    }
    {
        "date": "2042-12-25",
        "totalCashFlow": 22832.675494,
        "interestPayment": 682.140118,
        "principalBalance": 1614985.747557,
        "principalPayment": 22150.535376,
        "endPrincipalBalance": 1614985.747557,
        "beginPrincipalBalance": 1637136.282934,
        "prepayPrincipalPayment": 10759.593646,
        "scheduledPrincipalPayment": 11390.94173
    }
    {
        "date": "2043-01-25",
        "totalCashFlow": 24104.064402,
        "interestPayment": 672.910728,
        "principalBalance": 1591554.593883,
        "principalPayment": 23431.153674,
        "endPrincipalBalance": 1591554.593883,
        "beginPrincipalBalance": 1614985.747557,
        "prepayPrincipalPayment": 12103.813041,
        "scheduledPrincipalPayment": 11327.340633
    }
    {
        "date": "2043-02-25",
        "totalCashFlow": 21079.073088,
        "interestPayment": 663.147747,
        "principalBalance": 1571138.668543,
        "principalPayment": 20415.92534,
        "endPrincipalBalance": 1571138.668543,
        "beginPrincipalBalance": 1591554.593883,
        "prepayPrincipalPayment": 9162.368975,
        "scheduledPrincipalPayment": 11253.556365
    }
    {
        "date": "2043-03-25",
        "totalCashFlow": 21045.45834,
        "interestPayment": 654.641112,
        "principalBalance": 1550747.851315,
        "principalPayment": 20390.817228,
        "endPrincipalBalance": 1550747.851315,
        "beginPrincipalBalance": 1571138.668543,
        "prepayPrincipalPayment": 9190.852952,
        "scheduledPrincipalPayment": 11199.964276
    }
    {
        "date": "2043-04-25",
        "totalCashFlow": 22853.341552,
        "interestPayment": 646.144938,
        "principalBalance": 1528540.654701,
        "principalPayment": 22207.196613,
        "endPrincipalBalance": 1528540.654701,
        "beginPrincipalBalance": 1550747.851315,
        "prepayPrincipalPayment": 11061.622439,
        "scheduledPrincipalPayment": 11145.574175
    }
    {
        "date": "2043-05-25",
        "totalCashFlow": 24062.924974,
        "interestPayment": 636.891939,
        "principalBalance": 1505114.621667,
        "principalPayment": 23426.033034,
        "endPrincipalBalance": 1505114.621667,
        "beginPrincipalBalance": 1528540.654701,
        "prepayPrincipalPayment": 12349.010212,
        "scheduledPrincipalPayment": 11077.022823
    }
    {
        "date": "2043-06-25",
        "totalCashFlow": 23886.739779,
        "interestPayment": 627.131092,
        "principalBalance": 1481855.01298,
        "principalPayment": 23259.608686,
        "endPrincipalBalance": 1481855.01298,
        "beginPrincipalBalance": 1505114.621667,
        "prepayPrincipalPayment": 12261.285216,
        "scheduledPrincipalPayment": 10998.323471
    }
    {
        "date": "2043-07-25",
        "totalCashFlow": 25144.182171,
        "interestPayment": 617.439589,
        "principalBalance": 1457328.270398,
        "principalPayment": 24526.742582,
        "endPrincipalBalance": 1457328.270398,
        "beginPrincipalBalance": 1481855.01298,
        "prepayPrincipalPayment": 13607.312957,
        "scheduledPrincipalPayment": 10919.429625
    }
    {
        "date": "2043-08-25",
        "totalCashFlow": 24586.591638,
        "interestPayment": 607.220113,
        "principalBalance": 1433348.898873,
        "principalPayment": 23979.371525,
        "endPrincipalBalance": 1433348.898873,
        "beginPrincipalBalance": 1457328.270398,
        "prepayPrincipalPayment": 13149.686043,
        "scheduledPrincipalPayment": 10829.685483
    }
    {
        "date": "2043-09-25",
        "totalCashFlow": 23335.89403,
        "interestPayment": 597.228708,
        "principalBalance": 1410610.23355,
        "principalPayment": 22738.665323,
        "endPrincipalBalance": 1410610.23355,
        "beginPrincipalBalance": 1433348.898873,
        "prepayPrincipalPayment": 11996.250901,
        "scheduledPrincipalPayment": 10742.414421
    }
    {
        "date": "2043-10-25",
        "totalCashFlow": 22636.738643,
        "interestPayment": 587.754264,
        "principalBalance": 1388561.249171,
        "principalPayment": 22048.984379,
        "endPrincipalBalance": 1388561.249171,
        "beginPrincipalBalance": 1410610.23355,
        "prepayPrincipalPayment": 11386.060632,
        "scheduledPrincipalPayment": 10662.923747
    }
    {
        "date": "2043-11-25",
        "totalCashFlow": 21824.927341,
        "interestPayment": 578.567187,
        "principalBalance": 1367314.889017,
        "principalPayment": 21246.360154,
        "endPrincipalBalance": 1367314.889017,
        "beginPrincipalBalance": 1388561.249171,
        "prepayPrincipalPayment": 10659.143293,
        "scheduledPrincipalPayment": 10587.216861
    }
    {
        "date": "2043-12-25",
        "totalCashFlow": 20666.265555,
        "interestPayment": 569.714537,
        "principalBalance": 1347218.337999,
        "principalPayment": 20096.551018,
        "endPrincipalBalance": 1347218.337999,
        "beginPrincipalBalance": 1367314.889017,
        "prepayPrincipalPayment": 9580.287188,
        "scheduledPrincipalPayment": 10516.26383
    }
    {
        "date": "2044-01-25",
        "totalCashFlow": 21298.746235,
        "interestPayment": 561.340974,
        "principalBalance": 1326480.932738,
        "principalPayment": 20737.405261,
        "endPrincipalBalance": 1326480.932738,
        "beginPrincipalBalance": 1347218.337999,
        "prepayPrincipalPayment": 10284.519151,
        "scheduledPrincipalPayment": 10452.886111
    }
    {
        "date": "2044-02-25",
        "totalCashFlow": 18471.481598,
        "interestPayment": 552.700389,
        "principalBalance": 1308562.151529,
        "principalPayment": 17918.781209,
        "endPrincipalBalance": 1308562.151529,
        "beginPrincipalBalance": 1326480.932738,
        "prepayPrincipalPayment": 7535.510618,
        "scheduledPrincipalPayment": 10383.270591
    }
    {
        "date": "2044-03-25",
        "totalCashFlow": 19029.0846,
        "interestPayment": 545.23423,
        "principalBalance": 1290078.301158,
        "principalPayment": 18483.850371,
        "endPrincipalBalance": 1290078.301158,
        "beginPrincipalBalance": 1308562.151529,
        "prepayPrincipalPayment": 8149.276743,
        "scheduledPrincipalPayment": 10334.573628
    }
    {
        "date": "2044-04-25",
        "totalCashFlow": 20709.262734,
        "interestPayment": 537.532625,
        "principalBalance": 1269906.57105,
        "principalPayment": 20171.730108,
        "endPrincipalBalance": 1269906.57105,
        "beginPrincipalBalance": 1290078.301158,
        "prepayPrincipalPayment": 9891.3314,
        "scheduledPrincipalPayment": 10280.398708
    }
    {
        "date": "2044-05-25",
        "totalCashFlow": 20574.065341,
        "interestPayment": 529.127738,
        "principalBalance": 1249861.633447,
        "principalPayment": 20044.937603,
        "endPrincipalBalance": 1249861.633447,
        "beginPrincipalBalance": 1269906.57105,
        "prepayPrincipalPayment": 9833.368293,
        "scheduledPrincipalPayment": 10211.569309
    }
    {
        "date": "2044-06-25",
        "totalCashFlow": 21404.739174,
        "interestPayment": 520.775681,
        "principalBalance": 1228977.669953,
        "principalPayment": 20883.963494,
        "endPrincipalBalance": 1228977.669953,
        "beginPrincipalBalance": 1249861.633447,
        "prepayPrincipalPayment": 10741.55321,
        "scheduledPrincipalPayment": 10142.410283
    }
    {
        "date": "2044-07-25",
        "totalCashFlow": 21958.752112,
        "interestPayment": 512.074029,
        "principalBalance": 1207530.99187,
        "principalPayment": 21446.678083,
        "endPrincipalBalance": 1207530.99187,
        "beginPrincipalBalance": 1228977.669953,
        "prepayPrincipalPayment": 11381.673293,
        "scheduledPrincipalPayment": 10065.00479
    }
    {
        "date": "2044-08-25",
        "totalCashFlow": 20641.870813,
        "interestPayment": 503.137913,
        "principalBalance": 1187392.25897,
        "principalPayment": 20138.7329,
        "endPrincipalBalance": 1187392.25897,
        "beginPrincipalBalance": 1207530.99187,
        "prepayPrincipalPayment": 10157.32424,
        "scheduledPrincipalPayment": 9981.40866
    }
    {
        "date": "2044-09-25",
        "totalCashFlow": 21208.897022,
        "interestPayment": 494.746775,
        "principalBalance": 1166678.108723,
        "principalPayment": 20714.150247,
        "endPrincipalBalance": 1166678.108723,
        "beginPrincipalBalance": 1187392.25897,
        "prepayPrincipalPayment": 10807.092355,
        "scheduledPrincipalPayment": 9907.057893
    }
    {
        "date": "2044-10-25",
        "totalCashFlow": 19827.41613,
        "interestPayment": 486.115879,
        "principalBalance": 1147336.808471,
        "principalPayment": 19341.300251,
        "endPrincipalBalance": 1147336.808471,
        "beginPrincipalBalance": 1166678.108723,
        "prepayPrincipalPayment": 9514.945321,
        "scheduledPrincipalPayment": 9826.35493
    }
    {
        "date": "2044-11-25",
        "totalCashFlow": 18827.307099,
        "interestPayment": 478.057004,
        "principalBalance": 1128987.558375,
        "principalPayment": 18349.250096,
        "endPrincipalBalance": 1128987.558375,
        "beginPrincipalBalance": 1147336.808471,
        "prepayPrincipalPayment": 8593.563974,
        "scheduledPrincipalPayment": 9755.686121
    }
    {
        "date": "2044-12-25",
        "totalCashFlow": 18520.581927,
        "interestPayment": 470.411483,
        "principalBalance": 1110937.387931,
        "principalPayment": 18050.170444,
        "endPrincipalBalance": 1110937.387931,
        "beginPrincipalBalance": 1128987.558375,
        "prepayPrincipalPayment": 8358.095739,
        "scheduledPrincipalPayment": 9692.074706
    }
    {
        "date": "2045-01-25",
        "totalCashFlow": 18369.33144,
        "interestPayment": 462.890578,
        "principalBalance": 1093030.947069,
        "principalPayment": 17906.440862,
        "endPrincipalBalance": 1093030.947069,
        "beginPrincipalBalance": 1110937.387931,
        "prepayPrincipalPayment": 8276.719095,
        "scheduledPrincipalPayment": 9629.721767
    }
    {
        "date": "2045-02-25",
        "totalCashFlow": 16664.709001,
        "interestPayment": 455.429561,
        "principalBalance": 1076821.66763,
        "principalPayment": 16209.279439,
        "endPrincipalBalance": 1076821.66763,
        "beginPrincipalBalance": 1093030.947069,
        "prepayPrincipalPayment": 6641.972885,
        "scheduledPrincipalPayment": 9567.306554
    }
    {
        "date": "2045-03-25",
        "totalCashFlow": 16609.125637,
        "interestPayment": 448.675695,
        "principalBalance": 1060661.217688,
        "principalPayment": 16160.449942,
        "endPrincipalBalance": 1060661.217688,
        "beginPrincipalBalance": 1076821.66763,
        "prepayPrincipalPayment": 6641.889137,
        "scheduledPrincipalPayment": 9518.560806
    }
    {
        "date": "2045-04-25",
        "totalCashFlow": 18124.622835,
        "interestPayment": 441.942174,
        "principalBalance": 1042978.537027,
        "principalPayment": 17682.680661,
        "endPrincipalBalance": 1042978.537027,
        "beginPrincipalBalance": 1060661.217688,
        "prepayPrincipalPayment": 8213.500946,
        "scheduledPrincipalPayment": 9469.179714
    }
    {
        "date": "2045-05-25",
        "totalCashFlow": 17840.640834,
        "interestPayment": 434.57439,
        "principalBalance": 1025572.470583,
        "principalPayment": 17406.066444,
        "endPrincipalBalance": 1025572.470583,
        "beginPrincipalBalance": 1042978.537027,
        "prepayPrincipalPayment": 8001.087614,
        "scheduledPrincipalPayment": 9404.97883
    }
    {
        "date": "2045-06-25",
        "totalCashFlow": 18924.49206,
        "interestPayment": 427.321863,
        "principalBalance": 1007075.300386,
        "principalPayment": 18497.170197,
        "endPrincipalBalance": 1007075.300386,
        "beginPrincipalBalance": 1025572.470583,
        "prepayPrincipalPayment": 9155.276067,
        "scheduledPrincipalPayment": 9341.89413
    }
    {
        "date": "2045-07-25",
        "totalCashFlow": 18986.70377,
        "interestPayment": 419.614708,
        "principalBalance": 988508.211324,
        "principalPayment": 18567.089061,
        "endPrincipalBalance": 988508.211324,
        "beginPrincipalBalance": 1007075.300386,
        "prepayPrincipalPayment": 9299.713088,
        "scheduledPrincipalPayment": 9267.375974
    }
    {
        "date": "2045-08-25",
        "totalCashFlow": 17942.485873,
        "interestPayment": 411.878421,
        "principalBalance": 970977.603873,
        "principalPayment": 17530.607451,
        "endPrincipalBalance": 970977.603873,
        "beginPrincipalBalance": 988508.211324,
        "prepayPrincipalPayment": 8340.041208,
        "scheduledPrincipalPayment": 9190.566244
    }
    {
        "date": "2045-09-25",
        "totalCashFlow": 18346.23951,
        "interestPayment": 404.574002,
        "principalBalance": 953035.938364,
        "principalPayment": 17941.665509,
        "endPrincipalBalance": 953035.938364,
        "beginPrincipalBalance": 970977.603873,
        "prepayPrincipalPayment": 8819.875765,
        "scheduledPrincipalPayment": 9121.789743
    }
    {
        "date": "2045-10-25",
        "totalCashFlow": 16985.252215,
        "interestPayment": 397.098308,
        "principalBalance": 936447.784457,
        "principalPayment": 16588.153908,
        "endPrincipalBalance": 936447.784457,
        "beginPrincipalBalance": 953035.938364,
        "prepayPrincipalPayment": 7540.592997,
        "scheduledPrincipalPayment": 9047.560911
    }
    {
        "date": "2045-11-25",
        "totalCashFlow": 16718.289497,
        "interestPayment": 390.186577,
        "principalBalance": 920119.681536,
        "principalPayment": 16328.102921,
        "endPrincipalBalance": 920119.681536,
        "beginPrincipalBalance": 936447.784457,
        "prepayPrincipalPayment": 7343.4648,
        "scheduledPrincipalPayment": 8984.638121
    }
    {
        "date": "2045-12-25",
        "totalCashFlow": 16208.598558,
        "interestPayment": 383.383201,
        "principalBalance": 904294.466179,
        "principalPayment": 15825.215357,
        "endPrincipalBalance": 904294.466179,
        "beginPrincipalBalance": 920119.681536,
        "prepayPrincipalPayment": 6902.430881,
        "scheduledPrincipalPayment": 8922.784476
    }
    {
        "date": "2046-01-25",
        "totalCashFlow": 15843.11513,
        "interestPayment": 376.789361,
        "principalBalance": 888828.14041,
        "principalPayment": 15466.325769,
        "endPrincipalBalance": 888828.14041,
        "beginPrincipalBalance": 904294.466179,
        "prepayPrincipalPayment": 6601.908346,
        "scheduledPrincipalPayment": 8864.417424
    }
    {
        "date": "2046-02-25",
        "totalCashFlow": 14922.03337,
        "interestPayment": 370.345059,
        "principalBalance": 874276.452098,
        "principalPayment": 14551.688312,
        "endPrincipalBalance": 874276.452098,
        "beginPrincipalBalance": 888828.14041,
        "prepayPrincipalPayment": 5743.461585,
        "scheduledPrincipalPayment": 8808.226727
    }
    {
        "date": "2046-03-25",
        "totalCashFlow": 14682.009553,
        "interestPayment": 364.281855,
        "principalBalance": 859958.7244,
        "principalPayment": 14317.727698,
        "endPrincipalBalance": 859958.7244,
        "beginPrincipalBalance": 874276.452098,
        "prepayPrincipalPayment": 5557.872626,
        "scheduledPrincipalPayment": 8759.855073
    }
    {
        "date": "2046-04-25",
        "totalCashFlow": 15505.302097,
        "interestPayment": 358.316135,
        "principalBalance": 844811.738438,
        "principalPayment": 15146.985962,
        "endPrincipalBalance": 844811.738438,
        "beginPrincipalBalance": 859958.7244,
        "prepayPrincipalPayment": 6434.315617,
        "scheduledPrincipalPayment": 8712.670345
    }
    {
        "date": "2046-05-25",
        "totalCashFlow": 15792.622884,
        "interestPayment": 352.004891,
        "principalBalance": 829371.120446,
        "principalPayment": 15440.617993,
        "endPrincipalBalance": 829371.120446,
        "beginPrincipalBalance": 844811.738438,
        "prepayPrincipalPayment": 6784.797033,
        "scheduledPrincipalPayment": 8655.82096
    }
    {
        "date": "2046-06-25",
        "totalCashFlow": 16353.672491,
        "interestPayment": 345.5713,
        "principalBalance": 813363.019255,
        "principalPayment": 16008.101191,
        "endPrincipalBalance": 813363.019255,
        "beginPrincipalBalance": 829371.120446,
        "prepayPrincipalPayment": 7413.572604,
        "scheduledPrincipalPayment": 8594.528587
    }
    {
        "date": "2046-07-25",
        "totalCashFlow": 16112.401029,
        "interestPayment": 338.901258,
        "principalBalance": 797589.519483,
        "principalPayment": 15773.499771,
        "endPrincipalBalance": 797589.519483,
        "beginPrincipalBalance": 813363.019255,
        "prepayPrincipalPayment": 7247.72853,
        "scheduledPrincipalPayment": 8525.771241
    }
    {
        "date": "2046-08-25",
        "totalCashFlow": 15794.437938,
        "interestPayment": 332.328966,
        "principalBalance": 782127.410512,
        "principalPayment": 15462.108971,
        "endPrincipalBalance": 782127.410512,
        "beginPrincipalBalance": 797589.519483,
        "prepayPrincipalPayment": 7004.313055,
        "scheduledPrincipalPayment": 8457.795916
    }
    {
        "date": "2046-09-25",
        "totalCashFlow": 15827.366208,
        "interestPayment": 325.886421,
        "principalBalance": 766625.930725,
        "principalPayment": 15501.479787,
        "endPrincipalBalance": 766625.930725,
        "beginPrincipalBalance": 782127.410512,
        "prepayPrincipalPayment": 7110.023047,
        "scheduledPrincipalPayment": 8391.45674
    }
    {
        "date": "2046-10-25",
        "totalCashFlow": 14569.47294,
        "interestPayment": 319.427471,
        "principalBalance": 752375.885256,
        "principalPayment": 14250.045469,
        "endPrincipalBalance": 752375.885256,
        "beginPrincipalBalance": 766625.930725,
        "prepayPrincipalPayment": 5927.03882,
        "scheduledPrincipalPayment": 8323.006649
    }
    {
        "date": "2046-11-25",
        "totalCashFlow": 14737.637985,
        "interestPayment": 313.489952,
        "principalBalance": 737951.737223,
        "principalPayment": 14424.148033,
        "endPrincipalBalance": 737951.737223,
        "beginPrincipalBalance": 752375.885256,
        "prepayPrincipalPayment": 6157.593541,
        "scheduledPrincipalPayment": 8266.554492
    }
    {
        "date": "2046-12-25",
        "totalCashFlow": 14140.521232,
        "interestPayment": 307.479891,
        "principalBalance": 724118.695881,
        "principalPayment": 13833.041342,
        "endPrincipalBalance": 724118.695881,
        "beginPrincipalBalance": 737951.737223,
        "prepayPrincipalPayment": 5626.353838,
        "scheduledPrincipalPayment": 8206.687504
    }
    {
        "date": "2047-01-25",
        "totalCashFlow": 13841.764621,
        "interestPayment": 301.716123,
        "principalBalance": 710578.647384,
        "principalPayment": 13540.048498,
        "endPrincipalBalance": 710578.647384,
        "beginPrincipalBalance": 724118.695881,
        "prepayPrincipalPayment": 5388.152052,
        "scheduledPrincipalPayment": 8151.896446
    }
    {
        "date": "2047-02-25",
        "totalCashFlow": 13131.021677,
        "interestPayment": 296.074436,
        "principalBalance": 697743.700143,
        "principalPayment": 12834.94724,
        "endPrincipalBalance": 697743.700143,
        "beginPrincipalBalance": 710578.647384,
        "prepayPrincipalPayment": 4735.971875,
        "scheduledPrincipalPayment": 8098.975365
    }
    {
        "date": "2047-03-25",
        "totalCashFlow": 12927.22274,
        "interestPayment": 290.726542,
        "principalBalance": 685107.203945,
        "principalPayment": 12636.496198,
        "endPrincipalBalance": 685107.203945,
        "beginPrincipalBalance": 697743.700143,
        "prepayPrincipalPayment": 4583.742885,
        "scheduledPrincipalPayment": 8052.753313
    }
    {
        "date": "2047-04-25",
        "totalCashFlow": 13439.354995,
        "interestPayment": 285.461335,
        "principalBalance": 671953.310285,
        "principalPayment": 13153.89366,
        "endPrincipalBalance": 671953.310285,
        "beginPrincipalBalance": 685107.203945,
        "prepayPrincipalPayment": 5146.327074,
        "scheduledPrincipalPayment": 8007.566586
    }
    {
        "date": "2047-05-25",
        "totalCashFlow": 13783.660213,
        "interestPayment": 279.980546,
        "principalBalance": 658449.630618,
        "principalPayment": 13503.679667,
        "endPrincipalBalance": 658449.630618,
        "beginPrincipalBalance": 671953.310285,
        "prepayPrincipalPayment": 5548.697143,
        "scheduledPrincipalPayment": 7954.982524
    }
    {
        "date": "2047-06-25",
        "totalCashFlow": 14083.632741,
        "interestPayment": 274.354013,
        "principalBalance": 644640.35189,
        "principalPayment": 13809.278728,
        "endPrincipalBalance": 644640.35189,
        "beginPrincipalBalance": 658449.630618,
        "prepayPrincipalPayment": 5912.554762,
        "scheduledPrincipalPayment": 7896.723965
    }
    {
        "date": "2047-07-25",
        "totalCashFlow": 13685.482292,
        "interestPayment": 268.600147,
        "principalBalance": 631223.469744,
        "principalPayment": 13416.882146,
        "endPrincipalBalance": 631223.469744,
        "beginPrincipalBalance": 644640.35189,
        "prepayPrincipalPayment": 5583.776618,
        "scheduledPrincipalPayment": 7833.105527
    }
    {
        "date": "2047-08-25",
        "totalCashFlow": 13789.451675,
        "interestPayment": 263.009779,
        "principalBalance": 617697.027848,
        "principalPayment": 13526.441896,
        "endPrincipalBalance": 617697.027848,
        "beginPrincipalBalance": 631223.469744,
        "prepayPrincipalPayment": 5753.932182,
        "scheduledPrincipalPayment": 7772.509714
    }
    {
        "date": "2047-09-25",
        "totalCashFlow": 13441.639543,
        "interestPayment": 257.373762,
        "principalBalance": 604512.762066,
        "principalPayment": 13184.265782,
        "endPrincipalBalance": 604512.762066,
        "beginPrincipalBalance": 617697.027848,
        "prepayPrincipalPayment": 5475.468206,
        "scheduledPrincipalPayment": 7708.797576
    }
    {
        "date": "2047-10-25",
        "totalCashFlow": 12805.950815,
        "interestPayment": 251.880318,
        "principalBalance": 591958.691569,
        "principalPayment": 12554.070497,
        "endPrincipalBalance": 591958.691569,
        "beginPrincipalBalance": 604512.762066,
        "prepayPrincipalPayment": 4906.511874,
        "scheduledPrincipalPayment": 7647.558624
    }
    {
        "date": "2047-11-25",
        "totalCashFlow": 12749.073242,
        "interestPayment": 246.649455,
        "principalBalance": 579456.267781,
        "principalPayment": 12502.423787,
        "endPrincipalBalance": 579456.267781,
        "beginPrincipalBalance": 591958.691569,
        "prepayPrincipalPayment": 4909.830961,
        "scheduledPrincipalPayment": 7592.592826
    }
    {
        "date": "2047-12-25",
        "totalCashFlow": 12151.361628,
        "interestPayment": 241.440112,
        "principalBalance": 567546.346265,
        "principalPayment": 11909.921516,
        "endPrincipalBalance": 567546.346265,
        "beginPrincipalBalance": 579456.267781,
        "prepayPrincipalPayment": 4373.278986,
        "scheduledPrincipalPayment": 7536.64253
    }
    {
        "date": "2048-01-25",
        "totalCashFlow": 12164.666565,
        "interestPayment": 236.477644,
        "principalBalance": 555618.157345,
        "principalPayment": 11928.188921,
        "endPrincipalBalance": 555618.157345,
        "beginPrincipalBalance": 567546.346265,
        "prepayPrincipalPayment": 4441.385949,
        "scheduledPrincipalPayment": 7486.802972
    }
    {
        "date": "2048-02-25",
        "totalCashFlow": 11496.354147,
        "interestPayment": 231.507566,
        "principalBalance": 544353.310763,
        "principalPayment": 11264.846582,
        "endPrincipalBalance": 544353.310763,
        "beginPrincipalBalance": 555618.157345,
        "prepayPrincipalPayment": 3829.678571,
        "scheduledPrincipalPayment": 7435.168011
    }
    {
        "date": "2048-03-25",
        "totalCashFlow": 11321.968956,
        "interestPayment": 226.813879,
        "principalBalance": 533258.155686,
        "principalPayment": 11095.155077,
        "endPrincipalBalance": 533258.155686,
        "beginPrincipalBalance": 544353.310763,
        "prepayPrincipalPayment": 3704.23927,
        "scheduledPrincipalPayment": 7390.915807
    }
    {
        "date": "2048-04-25",
        "totalCashFlow": 11775.192455,
        "interestPayment": 222.190898,
        "principalBalance": 521705.154129,
        "principalPayment": 11553.001557,
        "endPrincipalBalance": 521705.154129,
        "beginPrincipalBalance": 533258.155686,
        "prepayPrincipalPayment": 4205.42628,
        "scheduledPrincipalPayment": 7347.575276
    }
    {
        "date": "2048-05-25",
        "totalCashFlow": 11941.567118,
        "interestPayment": 217.377148,
        "principalBalance": 509980.964158,
        "principalPayment": 11724.189971,
        "endPrincipalBalance": 509980.964158,
        "beginPrincipalBalance": 521705.154129,
        "prepayPrincipalPayment": 4427.776811,
        "scheduledPrincipalPayment": 7296.413159
    }
    {
        "date": "2048-06-25",
        "totalCashFlow": 11802.84422,
        "interestPayment": 212.492068,
        "principalBalance": 498390.612006,
        "principalPayment": 11590.352152,
        "endPrincipalBalance": 498390.612006,
        "beginPrincipalBalance": 509980.964158,
        "prepayPrincipalPayment": 4349.20791,
        "scheduledPrincipalPayment": 7241.144242
    }
    {
        "date": "2048-07-25",
        "totalCashFlow": 12021.675395,
        "interestPayment": 207.662755,
        "principalBalance": 486576.599366,
        "principalPayment": 11814.01264,
        "endPrincipalBalance": 486576.599366,
        "beginPrincipalBalance": 498390.612006,
        "prepayPrincipalPayment": 4628.034015,
        "scheduledPrincipalPayment": 7185.978626
    }
    {
        "date": "2048-08-25",
        "totalCashFlow": 11786.85144,
        "interestPayment": 202.74025,
        "principalBalance": 474992.488176,
        "principalPayment": 11584.11119,
        "endPrincipalBalance": 474992.488176,
        "beginPrincipalBalance": 486576.599366,
        "prepayPrincipalPayment": 4458.422582,
        "scheduledPrincipalPayment": 7125.688609
    }
    {
        "date": "2048-09-25",
        "totalCashFlow": 11390.634228,
        "interestPayment": 197.913537,
        "principalBalance": 463799.767485,
        "principalPayment": 11192.720691,
        "endPrincipalBalance": 463799.767485,
        "beginPrincipalBalance": 474992.488176,
        "prepayPrincipalPayment": 4125.940419,
        "scheduledPrincipalPayment": 7066.780272
    }
    {
        "date": "2048-10-25",
        "totalCashFlow": 11133.690513,
        "interestPayment": 193.249903,
        "principalBalance": 452859.326875,
        "principalPayment": 10940.440609,
        "endPrincipalBalance": 452859.326875,
        "beginPrincipalBalance": 463799.767485,
        "prepayPrincipalPayment": 3928.675433,
        "scheduledPrincipalPayment": 7011.765176
    }
    {
        "date": "2048-11-25",
        "totalCashFlow": 10858.685573,
        "interestPayment": 188.691386,
        "principalBalance": 442189.332689,
        "principalPayment": 10669.994187,
        "endPrincipalBalance": 442189.332689,
        "beginPrincipalBalance": 452859.326875,
        "prepayPrincipalPayment": 3711.293671,
        "scheduledPrincipalPayment": 6958.700516
    }
    {
        "date": "2048-12-25",
        "totalCashFlow": 10503.296595,
        "interestPayment": 184.245555,
        "principalBalance": 431870.281649,
        "principalPayment": 10319.05104,
        "endPrincipalBalance": 431870.281649,
        "beginPrincipalBalance": 442189.332689,
        "prepayPrincipalPayment": 3411.080453,
        "scheduledPrincipalPayment": 6907.970587
    }
    {
        "date": "2049-01-25",
        "totalCashFlow": 10571.923682,
        "interestPayment": 179.945951,
        "principalBalance": 421478.303918,
        "principalPayment": 10391.977731,
        "endPrincipalBalance": 421478.303918,
        "beginPrincipalBalance": 431870.281649,
        "prepayPrincipalPayment": 3531.002012,
        "scheduledPrincipalPayment": 6860.975719
    }
    {
        "date": "2049-02-25",
        "totalCashFlow": 9853.573361,
        "interestPayment": 175.61596,
        "principalBalance": 411800.346517,
        "principalPayment": 9677.957401,
        "endPrincipalBalance": 411800.346517,
        "beginPrincipalBalance": 421478.303918,
        "prepayPrincipalPayment": 2866.895594,
        "scheduledPrincipalPayment": 6811.061807
    }
    {
        "date": "2049-03-25",
        "totalCashFlow": 9879.264671,
        "interestPayment": 171.583478,
        "principalBalance": 402092.665325,
        "principalPayment": 9707.681193,
        "endPrincipalBalance": 402092.665325,
        "beginPrincipalBalance": 411800.346517,
        "prepayPrincipalPayment": 2936.663395,
        "scheduledPrincipalPayment": 6771.017798
    }
    {
        "date": "2049-04-25",
        "totalCashFlow": 10282.194265,
        "interestPayment": 167.538611,
        "principalBalance": 391978.00967,
        "principalPayment": 10114.655655,
        "endPrincipalBalance": 391978.00967,
        "beginPrincipalBalance": 402092.665325,
        "prepayPrincipalPayment": 3385.729087,
        "scheduledPrincipalPayment": 6728.926567
    }
    {
        "date": "2049-05-25",
        "totalCashFlow": 10281.027179,
        "interestPayment": 163.324171,
        "principalBalance": 381860.306661,
        "principalPayment": 10117.703009,
        "endPrincipalBalance": 381860.306661,
        "beginPrincipalBalance": 391978.00967,
        "prepayPrincipalPayment": 3439.45087,
        "scheduledPrincipalPayment": 6678.252139
    }
    {
        "date": "2049-06-25",
        "totalCashFlow": 10227.75619,
        "interestPayment": 159.108461,
        "principalBalance": 371791.658932,
        "principalPayment": 10068.647729,
        "endPrincipalBalance": 371791.658932,
        "beginPrincipalBalance": 381860.306661,
        "prepayPrincipalPayment": 3443.115852,
        "scheduledPrincipalPayment": 6625.531877
    }
    {
        "date": "2049-07-25",
        "totalCashFlow": 10375.595222,
        "interestPayment": 154.913191,
        "principalBalance": 361570.976901,
        "principalPayment": 10220.682031,
        "endPrincipalBalance": 361570.976901,
        "beginPrincipalBalance": 371791.658932,
        "prepayPrincipalPayment": 3649.107088,
        "scheduledPrincipalPayment": 6571.574943
    }
    {
        "date": "2049-08-25",
        "totalCashFlow": 10121.592848,
        "interestPayment": 150.654574,
        "principalBalance": 351600.038627,
        "principalPayment": 9970.938275,
        "endPrincipalBalance": 351600.038627,
        "beginPrincipalBalance": 361570.976901,
        "prepayPrincipalPayment": 3458.246419,
        "scheduledPrincipalPayment": 6512.691855
    }
    {
        "date": "2049-09-25",
        "totalCashFlow": 10010.07792,
        "interestPayment": 146.500016,
        "principalBalance": 341736.460723,
        "principalPayment": 9863.577904,
        "endPrincipalBalance": 341736.460723,
        "beginPrincipalBalance": 351600.038627,
        "prepayPrincipalPayment": 3407.6013,
        "scheduledPrincipalPayment": 6455.976604
    }
    {
        "date": "2049-10-25",
        "totalCashFlow": 9742.875058,
        "interestPayment": 142.390192,
        "principalBalance": 332135.975857,
        "principalPayment": 9600.484866,
        "endPrincipalBalance": 332135.975857,
        "beginPrincipalBalance": 341736.460723,
        "prepayPrincipalPayment": 3201.589426,
        "scheduledPrincipalPayment": 6398.89544
    }
    {
        "date": "2049-11-25",
        "totalCashFlow": 9480.049931,
        "interestPayment": 138.38999,
        "principalBalance": 322794.315915,
        "principalPayment": 9341.659941,
        "endPrincipalBalance": 322794.315915,
        "beginPrincipalBalance": 332135.975857,
        "prepayPrincipalPayment": 2997.2552,
        "scheduledPrincipalPayment": 6344.404741
    }
    {
        "date": "2049-12-25",
        "totalCashFlow": 9355.242103,
        "interestPayment": 134.497632,
        "principalBalance": 313573.571444,
        "principalPayment": 9220.744471,
        "endPrincipalBalance": 313573.571444,
        "beginPrincipalBalance": 322794.315915,
        "prepayPrincipalPayment": 2928.159768,
        "scheduledPrincipalPayment": 6292.584703
    }
    {
        "date": "2050-01-25",
        "totalCashFlow": 9262.977542,
        "interestPayment": 130.655655,
        "principalBalance": 304441.249557,
        "principalPayment": 9132.321887,
        "endPrincipalBalance": 304441.249557,
        "beginPrincipalBalance": 313573.571444,
        "prepayPrincipalPayment": 2891.459773,
        "scheduledPrincipalPayment": 6240.862114
    }
    {
        "date": "2050-02-25",
        "totalCashFlow": 8870.040255,
        "interestPayment": 126.850521,
        "principalBalance": 295698.059822,
        "principalPayment": 8743.189735,
        "endPrincipalBalance": 295698.059822,
        "beginPrincipalBalance": 304441.249557,
        "prepayPrincipalPayment": 2554.60341,
        "scheduledPrincipalPayment": 6188.586324
    }
    {
        "date": "2050-03-25",
        "totalCashFlow": 8797.546952,
        "interestPayment": 123.207525,
        "principalBalance": 287023.720395,
        "principalPayment": 8674.339427,
        "endPrincipalBalance": 287023.720395,
        "beginPrincipalBalance": 295698.059822,
        "prepayPrincipalPayment": 2532.368555,
        "scheduledPrincipalPayment": 6141.970872
    }
    {
        "date": "2050-04-25",
        "totalCashFlow": 9017.256529,
        "interestPayment": 119.593217,
        "principalBalance": 278126.057083,
        "principalPayment": 8897.663312,
        "endPrincipalBalance": 278126.057083,
        "beginPrincipalBalance": 287023.720395,
        "prepayPrincipalPayment": 2803.066297,
        "scheduledPrincipalPayment": 6094.597015
    }
    {
        "date": "2050-05-25",
        "totalCashFlow": 8910.705411,
        "interestPayment": 115.885857,
        "principalBalance": 269331.237529,
        "principalPayment": 8794.819554,
        "endPrincipalBalance": 269331.237529,
        "beginPrincipalBalance": 278126.057083,
        "prepayPrincipalPayment": 2754.748269,
        "scheduledPrincipalPayment": 6040.071285
    }
    {
        "date": "2050-06-25",
        "totalCashFlow": 8939.383459,
        "interestPayment": 112.221349,
        "principalBalance": 260504.075418,
        "principalPayment": 8827.16211,
        "endPrincipalBalance": 260504.075418,
        "beginPrincipalBalance": 269331.237529,
        "prepayPrincipalPayment": 2842.015791,
        "scheduledPrincipalPayment": 5985.146319
    }
    {
        "date": "2050-07-25",
        "totalCashFlow": 8922.020527,
        "interestPayment": 108.543365,
        "principalBalance": 251690.598256,
        "principalPayment": 8813.477162,
        "endPrincipalBalance": 251690.598256,
        "beginPrincipalBalance": 260504.075418,
        "prepayPrincipalPayment": 2886.754951,
        "scheduledPrincipalPayment": 5926.722211
    }
    {
        "date": "2050-08-25",
        "totalCashFlow": 8650.136345,
        "interestPayment": 104.871083,
        "principalBalance": 243145.332994,
        "principalPayment": 8545.265262,
        "endPrincipalBalance": 243145.332994,
        "beginPrincipalBalance": 251690.598256,
        "prepayPrincipalPayment": 2679.644874,
        "scheduledPrincipalPayment": 5865.620388
    }
    {
        "date": "2050-09-25",
        "totalCashFlow": 8633.621993,
        "interestPayment": 101.310555,
        "principalBalance": 234613.021557,
        "principalPayment": 8532.311438,
        "endPrincipalBalance": 234613.021557,
        "beginPrincipalBalance": 243145.332994,
        "prepayPrincipalPayment": 2724.586535,
        "scheduledPrincipalPayment": 5807.724903
    }
    {
        "date": "2050-10-25",
        "totalCashFlow": 8358.535002,
        "interestPayment": 97.755426,
        "principalBalance": 226352.24198,
        "principalPayment": 8260.779577,
        "endPrincipalBalance": 226352.24198,
        "beginPrincipalBalance": 234613.021557,
        "prepayPrincipalPayment": 2513.745888,
        "scheduledPrincipalPayment": 5747.033689
    }
    {
        "date": "2050-11-25",
        "totalCashFlow": 8141.38968,
        "interestPayment": 94.313434,
        "principalBalance": 218305.165734,
        "principalPayment": 8047.076246,
        "endPrincipalBalance": 218305.165734,
        "beginPrincipalBalance": 226352.24198,
        "prepayPrincipalPayment": 2357.244267,
        "scheduledPrincipalPayment": 5689.831978
    }
    {
        "date": "2050-12-25",
        "totalCashFlow": 8011.526875,
        "interestPayment": 90.960486,
        "principalBalance": 210384.599345,
        "principalPayment": 7920.56639,
        "endPrincipalBalance": 210384.599345,
        "beginPrincipalBalance": 218305.165734,
        "prepayPrincipalPayment": 2285.652914,
        "scheduledPrincipalPayment": 5634.913476
    }
    {
        "date": "2051-01-25",
        "totalCashFlow": 7902.56753,
        "interestPayment": 87.66025,
        "principalBalance": 202569.692064,
        "principalPayment": 7814.90728,
        "endPrincipalBalance": 202569.692064,
        "beginPrincipalBalance": 210384.599345,
        "prepayPrincipalPayment": 2234.747873,
        "scheduledPrincipalPayment": 5580.159407
    }
    {
        "date": "2051-02-25",
        "totalCashFlow": 7610.293261,
        "interestPayment": 84.404038,
        "principalBalance": 195043.802842,
        "principalPayment": 7525.889223,
        "endPrincipalBalance": 195043.802842,
        "beginPrincipalBalance": 202569.692064,
        "prepayPrincipalPayment": 2000.869145,
        "scheduledPrincipalPayment": 5525.020078
    }
    {
        "date": "2051-03-25",
        "totalCashFlow": 7515.740222,
        "interestPayment": 81.268251,
        "principalBalance": 187609.330871,
        "principalPayment": 7434.471971,
        "endPrincipalBalance": 187609.330871,
        "beginPrincipalBalance": 195043.802842,
        "prepayPrincipalPayment": 1959.858333,
        "scheduledPrincipalPayment": 5474.613638
    }
    {
        "date": "2051-04-25",
        "totalCashFlow": 7580.80624,
        "interestPayment": 78.170555,
        "principalBalance": 180106.695185,
        "principalPayment": 7502.635685,
        "endPrincipalBalance": 180106.695185,
        "beginPrincipalBalance": 187609.330871,
        "prepayPrincipalPayment": 2078.977497,
        "scheduledPrincipalPayment": 5423.658189
    }
    {
        "date": "2051-05-25",
        "totalCashFlow": 7460.570936,
        "interestPayment": 75.044456,
        "principalBalance": 172721.168706,
        "principalPayment": 7385.52648,
        "endPrincipalBalance": 172721.168706,
        "beginPrincipalBalance": 180106.695185,
        "prepayPrincipalPayment": 2018.174171,
        "scheduledPrincipalPayment": 5367.352309
    }
    {
        "date": "2051-06-25",
        "totalCashFlow": 7471.860173,
        "interestPayment": 71.967154,
        "principalBalance": 165321.275686,
        "principalPayment": 7399.893019,
        "endPrincipalBalance": 165321.275686,
        "beginPrincipalBalance": 172721.168706,
        "prepayPrincipalPayment": 2089.005208,
        "scheduledPrincipalPayment": 5310.887812
    }
    {
        "date": "2051-07-25",
        "totalCashFlow": 7366.99443,
        "interestPayment": 68.883865,
        "principalBalance": 158023.165121,
        "principalPayment": 7298.110565,
        "endPrincipalBalance": 158023.165121,
        "beginPrincipalBalance": 165321.275686,
        "prepayPrincipalPayment": 2048.030764,
        "scheduledPrincipalPayment": 5250.079801
    }
    {
        "date": "2051-08-25",
        "totalCashFlow": 7150.626545,
        "interestPayment": 65.842985,
        "principalBalance": 150938.381561,
        "principalPayment": 7084.78356,
        "endPrincipalBalance": 150938.381561,
        "beginPrincipalBalance": 158023.165121,
        "prepayPrincipalPayment": 1896.477037,
        "scheduledPrincipalPayment": 5188.306522
    }
    {
        "date": "2051-09-25",
        "totalCashFlow": 7099.631339,
        "interestPayment": 62.890992,
        "principalBalance": 143901.641214,
        "principalPayment": 7036.740347,
        "endPrincipalBalance": 143901.641214,
        "beginPrincipalBalance": 150938.381561,
        "prepayPrincipalPayment": 1907.476375,
        "scheduledPrincipalPayment": 5129.263972
    }
    {
        "date": "2051-10-25",
        "totalCashFlow": 6873.629641,
        "interestPayment": 59.959017,
        "principalBalance": 137087.970591,
        "principalPayment": 6813.670623,
        "endPrincipalBalance": 137087.970591,
        "beginPrincipalBalance": 143901.641214,
        "prepayPrincipalPayment": 1746.234649,
        "scheduledPrincipalPayment": 5067.435975
    }
    {
        "date": "2051-11-25",
        "totalCashFlow": 6756.478609,
        "interestPayment": 57.119988,
        "principalBalance": 130388.61197,
        "principalPayment": 6699.358621,
        "endPrincipalBalance": 130388.61197,
        "beginPrincipalBalance": 137087.970591,
        "prepayPrincipalPayment": 1690.447868,
        "scheduledPrincipalPayment": 5008.910753
    }
    {
        "date": "2051-12-25",
        "totalCashFlow": 6613.517654,
        "interestPayment": 54.328588,
        "principalBalance": 123829.422905,
        "principalPayment": 6559.189065,
        "endPrincipalBalance": 123829.422905,
        "beginPrincipalBalance": 130388.61197,
        "prepayPrincipalPayment": 1609.23531,
        "scheduledPrincipalPayment": 4949.953755
    }
    {
        "date": "2052-01-25",
        "totalCashFlow": 6484.771771,
        "interestPayment": 51.595593,
        "principalBalance": 117396.246727,
        "principalPayment": 6433.176178,
        "endPrincipalBalance": 117396.246727,
        "beginPrincipalBalance": 123829.422905,
        "prepayPrincipalPayment": 1541.634645,
        "scheduledPrincipalPayment": 4891.541532
    }
    {
        "date": "2052-02-25",
        "totalCashFlow": 6311.675134,
        "interestPayment": 48.915103,
        "principalBalance": 111133.486696,
        "principalPayment": 6262.760031,
        "endPrincipalBalance": 111133.486696,
        "beginPrincipalBalance": 117396.246727,
        "prepayPrincipalPayment": 1429.591779,
        "scheduledPrincipalPayment": 4833.168252
    }
    {
        "date": "2052-03-25",
        "totalCashFlow": 6208.033942,
        "interestPayment": 46.305619,
        "principalBalance": 104971.758373,
        "principalPayment": 6161.728323,
        "endPrincipalBalance": 104971.758373,
        "beginPrincipalBalance": 111133.486696,
        "prepayPrincipalPayment": 1384.972445,
        "scheduledPrincipalPayment": 4776.755878
    }
    {
        "date": "2052-04-25",
        "totalCashFlow": 6145.610057,
        "interestPayment": 43.738233,
        "principalBalance": 98869.886549,
        "principalPayment": 6101.871824,
        "endPrincipalBalance": 98869.886549,
        "beginPrincipalBalance": 104971.758373,
        "prepayPrincipalPayment": 1382.407648,
        "scheduledPrincipalPayment": 4719.464176
    }
    {
        "date": "2052-05-25",
        "totalCashFlow": 6070.627844,
        "interestPayment": 41.195786,
        "principalBalance": 92840.454491,
        "principalPayment": 6029.432058,
        "endPrincipalBalance": 92840.454491,
        "beginPrincipalBalance": 98869.886549,
        "prepayPrincipalPayment": 1370.197608,
        "scheduledPrincipalPayment": 4659.23445
    }
    {
        "date": "2052-06-25",
        "totalCashFlow": 5983.802483,
        "interestPayment": 38.683523,
        "principalBalance": 86895.335531,
        "principalPayment": 5945.11896,
        "endPrincipalBalance": 86895.335531,
        "beginPrincipalBalance": 92840.454491,
        "prepayPrincipalPayment": 1348.86553,
        "scheduledPrincipalPayment": 4596.25343
    }
    {
        "date": "2052-07-25",
        "totalCashFlow": 5828.974854,
        "interestPayment": 36.20639,
        "principalBalance": 81102.567067,
        "principalPayment": 5792.768464,
        "endPrincipalBalance": 81102.567067,
        "beginPrincipalBalance": 86895.335531,
        "prepayPrincipalPayment": 1262.056943,
        "scheduledPrincipalPayment": 4530.711521
    }
    {
        "date": "2052-08-25",
        "totalCashFlow": 5718.048543,
        "interestPayment": 33.792736,
        "principalBalance": 75418.31126,
        "principalPayment": 5684.255807,
        "endPrincipalBalance": 75418.31126,
        "beginPrincipalBalance": 81102.567067,
        "prepayPrincipalPayment": 1218.320313,
        "scheduledPrincipalPayment": 4465.935494
    }
    {
        "date": "2052-09-25",
        "totalCashFlow": 5567.223094,
        "interestPayment": 31.424296,
        "principalBalance": 69882.512462,
        "principalPayment": 5535.798797,
        "endPrincipalBalance": 69882.512462,
        "beginPrincipalBalance": 75418.31126,
        "prepayPrincipalPayment": 1136.281838,
        "scheduledPrincipalPayment": 4399.51696
    }
    {
        "date": "2052-10-25",
        "totalCashFlow": 5395.761705,
        "interestPayment": 29.117714,
        "principalBalance": 64515.868471,
        "principalPayment": 5366.643992,
        "endPrincipalBalance": 64515.868471,
        "beginPrincipalBalance": 69882.512462,
        "prepayPrincipalPayment": 1033.008628,
        "scheduledPrincipalPayment": 4333.635364
    }
    {
        "date": "2052-11-25",
        "totalCashFlow": 5270.499645,
        "interestPayment": 26.881612,
        "principalBalance": 59272.250437,
        "principalPayment": 5243.618034,
        "endPrincipalBalance": 59272.250437,
        "beginPrincipalBalance": 64515.868471,
        "prepayPrincipalPayment": 973.834945,
        "scheduledPrincipalPayment": 4269.783088
    }
    {
        "date": "2052-12-25",
        "totalCashFlow": 5106.540378,
        "interestPayment": 24.696771,
        "principalBalance": 54190.40683,
        "principalPayment": 5081.843607,
        "endPrincipalBalance": 54190.40683,
        "beginPrincipalBalance": 59272.250437,
        "prepayPrincipalPayment": 876.702717,
        "scheduledPrincipalPayment": 4205.140891
    }
    {
        "date": "2053-01-25",
        "totalCashFlow": 4985.49648,
        "interestPayment": 22.579336,
        "principalBalance": 49227.489686,
        "principalPayment": 4962.917144,
        "endPrincipalBalance": 49227.489686,
        "beginPrincipalBalance": 54190.40683,
        "prepayPrincipalPayment": 820.414101,
        "scheduledPrincipalPayment": 4142.503043
    }
    {
        "date": "2053-02-25",
        "totalCashFlow": 4824.035033,
        "interestPayment": 20.511454,
        "principalBalance": 44423.966107,
        "principalPayment": 4803.523579,
        "endPrincipalBalance": 44423.966107,
        "beginPrincipalBalance": 49227.489686,
        "prepayPrincipalPayment": 724.682463,
        "scheduledPrincipalPayment": 4078.841116
    }
    {
        "date": "2053-03-25",
        "totalCashFlow": 4693.225116,
        "interestPayment": 18.509986,
        "principalBalance": 39749.250977,
        "principalPayment": 4674.71513,
        "endPrincipalBalance": 39749.250977,
        "beginPrincipalBalance": 44423.966107,
        "prepayPrincipalPayment": 657.163034,
        "scheduledPrincipalPayment": 4017.552097
    }
    {
        "date": "2053-04-25",
        "totalCashFlow": 4586.236817,
        "interestPayment": 16.562188,
        "principalBalance": 35179.576348,
        "principalPayment": 4569.674629,
        "endPrincipalBalance": 35179.576348,
        "beginPrincipalBalance": 39749.250977,
        "prepayPrincipalPayment": 613.346428,
        "scheduledPrincipalPayment": 3956.328201
    }
    {
        "date": "2053-05-25",
        "totalCashFlow": 4468.76246,
        "interestPayment": 14.658157,
        "principalBalance": 30725.472045,
        "principalPayment": 4454.104303,
        "endPrincipalBalance": 30725.472045,
        "beginPrincipalBalance": 35179.576348,
        "prepayPrincipalPayment": 561.521066,
        "scheduledPrincipalPayment": 3892.583237
    }
    {
        "date": "2053-06-25",
        "totalCashFlow": 4334.905132,
        "interestPayment": 12.80228,
        "principalBalance": 26403.369193,
        "principalPayment": 4322.102852,
        "endPrincipalBalance": 26403.369193,
        "beginPrincipalBalance": 30725.472045,
        "prepayPrincipalPayment": 495.399473,
        "scheduledPrincipalPayment": 3826.703379
    }
    {
        "date": "2053-07-25",
        "totalCashFlow": 4197.96236,
        "interestPayment": 11.001404,
        "principalBalance": 22216.408237,
        "principalPayment": 4186.960956,
        "endPrincipalBalance": 22216.408237,
        "beginPrincipalBalance": 26403.369193,
        "prepayPrincipalPayment": 426.821927,
        "scheduledPrincipalPayment": 3760.139029
    }
    {
        "date": "2053-08-25",
        "totalCashFlow": 4058.719497,
        "interestPayment": 9.256837,
        "principalBalance": 18166.945578,
        "principalPayment": 4049.46266,
        "endPrincipalBalance": 18166.945578,
        "beginPrincipalBalance": 22216.408237,
        "prepayPrincipalPayment": 356.35878,
        "scheduledPrincipalPayment": 3693.10388
    }
    {
        "date": "2053-09-25",
        "totalCashFlow": 3912.786741,
        "interestPayment": 7.569561,
        "principalBalance": 14261.728398,
        "principalPayment": 3905.21718,
        "endPrincipalBalance": 14261.728398,
        "beginPrincipalBalance": 18166.945578,
        "prepayPrincipalPayment": 279.389744,
        "scheduledPrincipalPayment": 3625.827436
    }
    {
        "date": "2053-10-25",
        "totalCashFlow": 3773.017643,
        "interestPayment": 5.942387,
        "principalBalance": 10494.653141,
        "principalPayment": 3767.075256,
        "endPrincipalBalance": 10494.653141,
        "beginPrincipalBalance": 14261.728398,
        "prepayPrincipalPayment": 207.209311,
        "scheduledPrincipalPayment": 3559.865945
    }
    {
        "date": "2053-11-25",
        "totalCashFlow": 3636.548042,
        "interestPayment": 4.372772,
        "principalBalance": 6862.477871,
        "principalPayment": 3632.17527,
        "endPrincipalBalance": 6862.477871,
        "beginPrincipalBalance": 10494.653141,
        "prepayPrincipalPayment": 137.599004,
        "scheduledPrincipalPayment": 3494.576266
    }
    {
        "date": "2053-12-25",
        "totalCashFlow": 3498.692278,
        "interestPayment": 2.859366,
        "principalBalance": 3366.644959,
        "principalPayment": 3495.832912,
        "endPrincipalBalance": 3366.644959,
        "beginPrincipalBalance": 6862.477871,
        "prepayPrincipalPayment": 66.38015,
        "scheduledPrincipalPayment": 3429.452762
    }
    {
        "date": "2054-01-25",
        "totalCashFlow": 3368.047728,
        "interestPayment": 1.402769,
        "principalBalance": 0.0,
        "principalPayment": 3366.644959,
        "endPrincipalBalance": 0.0,
        "beginPrincipalBalance": 3366.644959,
        "prepayPrincipalPayment": 0.0,
        "scheduledPrincipalPayment": 3366.644959
    }

    """

    try:
        logger.info("Calling post_cash_flow_sync")

        response = Client().yield_book_rest.post_cash_flow_sync(
            body=CashFlowRequestData(global_settings=global_settings, input=input, keywords=keywords),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
            content_type="application/json",
        )

        output = response
        logger.info("Called post_cash_flow_sync")

        return output
    except Exception as err:
        logger.error("Error post_cash_flow_sync.")
        check_exception_and_raise(err, logger)


def post_csv_bulk_results_sync(
    *,
    ids: List[str],
    default_settings: Optional[BulkDefaultSettings] = None,
    global_settings: Optional[BulkGlobalSettings] = None,
    fields: Optional[List[ColumnDetail]] = None,
    job: Optional[str] = None,
) -> str:
    """
    Retrieve bulk result using request id or request name in csv format.

    Parameters
    ----------
    default_settings : BulkDefaultSettings, optional

    global_settings : BulkGlobalSettings, optional

    fields : List[ColumnDetail], optional

    ids : List[str]
          Ids can be provided comma separated. Different formats for id are:
          1) RequestId R-number
          2) Request name R:name. In this case also provide jobid (J-number) or jobname (J:name)
          3) Jobid J-number
          4) Job name J:name - only 1 active job with the jobname
          5) Tag name T:name. In this case also provide jobid (J-number) or jobname (J:name)
    job : str, optional
        Job reference. This can be of the form J-number or job name.

    Returns
    --------
    str
        A sequence of textual characters.

    Examples
    --------


    """

    try:
        logger.info("Calling post_csv_bulk_results_sync")

        response = Client().yield_book_rest.post_csv_bulk_results_sync(
            body=BulkResultRequest(
                default_settings=default_settings,
                global_settings=global_settings,
                fields=fields,
            ),
            ids=ids,
            job=job,
            content_type="application/json",
        )

        output = response
        logger.info("Called post_csv_bulk_results_sync")

        return output
    except Exception as err:
        logger.error("Error post_csv_bulk_results_sync.")
        check_exception_and_raise(err, logger)


def post_json_bulk_request_sync(
    *,
    ids: List[str],
    default_settings: Optional[BulkDefaultSettings] = None,
    global_settings: Optional[BulkGlobalSettings] = None,
    fields: Optional[List[ColumnDetail]] = None,
    job: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Retrieve bulk json result using request id or request name.

    Parameters
    ----------
    default_settings : BulkDefaultSettings, optional

    global_settings : BulkGlobalSettings, optional

    fields : List[ColumnDetail], optional

    ids : List[str]
          Ids can be provided comma separated. Different formats for id are:
          1) RequestId R-number
          2) Request name R:name. In this case also provide jobid (J-number) or jobname (J:name)
          3) Jobid J-number
          4) Job name J:name - only 1 active job with the jobname
          5) Tag name T:name. In this case also provide jobid (J-number) or jobname (J:name)
    job : str, optional
        Job reference. This can be of the form J-number or job name.

    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling post_json_bulk_request_sync")

        response = Client().yield_book_rest.post_json_bulk_request_sync(
            body=BulkResultRequest(
                default_settings=default_settings,
                global_settings=global_settings,
                fields=fields,
            ),
            ids=ids,
            job=job,
            content_type="application/json",
        )

        output = response
        logger.info("Called post_json_bulk_request_sync")

        return output
    except Exception as err:
        logger.error("Error post_json_bulk_request_sync.")
        check_exception_and_raise(err, logger)


def post_market_setting_sync(
    *,
    input: Optional[List[MarketSettingsRequestInfo]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Post Bond market setting.

    Parameters
    ----------
    input : List[MarketSettingsRequestInfo], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling post_market_setting_sync")

        response = Client().yield_book_rest.post_market_setting_sync(
            body=MarketSettingsRequest(input=input),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called post_market_setting_sync")

        return output
    except Exception as err:
        logger.error("Error post_market_setting_sync.")
        check_exception_and_raise(err, logger)


def request_actual_vs_projected_async(
    *,
    global_settings: Optional[ActualVsProjectedGlobalSettings] = None,
    input: Optional[List[ActualVsProjectedRequestItem]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """


    Parameters
    ----------
    global_settings : ActualVsProjectedGlobalSettings, optional

    input : List[ActualVsProjectedRequestItem], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling request_actual_vs_projected_async")

        response = Client().yield_book_rest.request_actual_vs_projected_async(
            body=ActualVsProjectedRequest(global_settings=global_settings, input=input),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_actual_vs_projected_async")

        return output
    except Exception as err:
        logger.error("Error request_actual_vs_projected_async.")
        check_exception_and_raise(err, logger)


def request_actual_vs_projected_async_get(
    *,
    id: str,
    id_type: Optional[str] = None,
    prepay_type: Optional[str] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """


    Parameters
    ----------
    id : str
        Security reference ID.
    id_type : str, optional
        A sequence of textual characters.
    prepay_type : str, optional
        A sequence of textual characters.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling request_actual_vs_projected_async_get")

        response = Client().yield_book_rest.request_actual_vs_projected_async_get(
            id=id,
            id_type=id_type,
            prepay_type=prepay_type,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_actual_vs_projected_async_get")

        return output
    except Exception as err:
        logger.error("Error request_actual_vs_projected_async_get.")
        check_exception_and_raise(err, logger)


def request_actual_vs_projected_sync(
    *,
    global_settings: Optional[ActualVsProjectedGlobalSettings] = None,
    input: Optional[List[ActualVsProjectedRequestItem]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """


    Parameters
    ----------
    global_settings : ActualVsProjectedGlobalSettings, optional

    input : List[ActualVsProjectedRequestItem], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling request_actual_vs_projected_sync")

        response = Client().yield_book_rest.request_actual_vs_projected_sync(
            body=ActualVsProjectedRequest(global_settings=global_settings, input=input),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_actual_vs_projected_sync")

        return output
    except Exception as err:
        logger.error("Error request_actual_vs_projected_sync.")
        check_exception_and_raise(err, logger)


def request_actual_vs_projected_sync_get(
    *,
    id: str,
    id_type: Optional[str] = None,
    prepay_type: Optional[str] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """


    Parameters
    ----------
    id : str
        Security reference ID.
    id_type : str, optional
        A sequence of textual characters.
    prepay_type : str, optional
        A sequence of textual characters.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling request_actual_vs_projected_sync_get")

        response = Client().yield_book_rest.request_actual_vs_projected_sync_get(
            id=id,
            id_type=id_type,
            prepay_type=prepay_type,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_actual_vs_projected_sync_get")

        return output
    except Exception as err:
        logger.error("Error request_actual_vs_projected_sync_get.")
        check_exception_and_raise(err, logger)


def request_bond_indic_async(
    *,
    input: Optional[List[IdentifierInfo]] = None,
    keywords: Optional[List[str]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Asynchronous Post method to retrieve the contractual information about the reference data of instruments, which will typically not need any further calculations. Retrieve a request ID by which, using subsequent API 'getResult' endpoint, instrument reference data can be obtained given a BondIndicRequest - 'Input' - parameter that includes the information of which security or list of securities to be queried by CUSIP, ISIN, or other identifier type to obtain basic contractual information such as security type, sector,  maturity, credit ratings, coupon, and specific information based on security type like current pool factor if the requested identifier is a mortgage. Recommended and preferred method for high-volume instrument queries (single requsts broken to recommended 100 items, up to 250 max).

    Parameters
    ----------
    input : List[IdentifierInfo], optional
        Single identifier or a list of identifiers to search instruments by.
    keywords : List[str], optional
        List of keywords from the MappedResponseRefData to be exposed in the result data set.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------
    >>> # Request bond indic with async post
    >>> response = request_bond_indic_async(input=[IdentifierInfo(identifier="999818YT")])
    >>>
    >>> # Get results by request_id
    >>> results_response = get_result(request_id_parameter=response.request_id)
    >>>
    >>> # Print results in json format
    >>> print(js.dumps(results_response, indent=4))
    {
        "meta": {
            "status": "DONE",
            "requestId": "R-20896",
            "timeStamp": "2025-08-18T22:30:54Z",
            "responseType": "BOND_INDIC",
            "resultsStatus": "ALL"
        },
        "results": [
            {
                "cusip": "999818YT8",
                "indic": {
                    "ltv": 90.0,
                    "wam": 196,
                    "figi": "BBG0033WXBV4",
                    "cusip": "999818YT8",
                    "moody": [
                        {
                            "value": "Aaa"
                        }
                    ],
                    "source": "CITI",
                    "ticker": "GNMA",
                    "country": "US",
                    "loanAge": 147,
                    "lockout": 0,
                    "putFlag": false,
                    "callFlag": false,
                    "cobsCode": "MTGE",
                    "country2": "US",
                    "country3": "USA",
                    "currency": "USD",
                    "dayCount": "30/360 eom",
                    "glicCode": "MBS",
                    "grossWAC": 4.0,
                    "ioPeriod": 0,
                    "poolCode": "NA",
                    "sinkFlag": false,
                    "cmaTicker": "N/A",
                    "datedDate": "2013-05-01",
                    "gnma2Flag": false,
                    "percentVA": 11.04,
                    "currentLTV": 27.5,
                    "extendFlag": "N",
                    "isoCountry": "US",
                    "marketType": "DOMC",
                    "percentDTI": 34.0,
                    "percentFHA": 80.91,
                    "percentInv": 0.0,
                    "percentPIH": 0.14,
                    "percentRHS": 7.9,
                    "securityID": "999818YT",
                    "serviceFee": 0.5,
                    "vPointType": "MPGNMA",
                    "adjustedLTV": 27.5,
                    "combinedLTV": 90.7,
                    "creditScore": 692,
                    "description": "30-YR GNMA-2013 PROD",
                    "esgBondFlag": false,
                    "indexRating": "AA+",
                    "issueAmount": 8597.24,
                    "lowerRating": "AA+",
                    "paymentFreq": 12,
                    "percentHARP": 0.0,
                    "percentRefi": 63.7,
                    "tierCapital": "NA",
                    "balloonMonth": 0,
                    "deliveryFlag": "N",
                    "indexCountry": "US",
                    "industryCode": "MT",
                    "issuerTicker": "GNMA",
                    "lowestRating": "AA+",
                    "maturityDate": "2041-12-01",
                    "middleRating": "AA+",
                    "modifiedDate": "2025-08-13",
                    "originalTerm": 360,
                    "parentTicker": "GNMA",
                    "percentHARP2": 0.0,
                    "percentJumbo": 0.0,
                    "securityType": "MORT",
                    "currentCoupon": 3.5,
                    "dataStateList": [
                        {
                            "state": "PR",
                            "percent": 17.13
                        },
                        {
                            "state": "TX",
                            "percent": 10.03
                        },
                        {
                            "state": "FL",
                            "percent": 5.66
                        },
                        {
                            "state": "CA",
                            "percent": 4.95
                        },
                        {
                            "state": "OH",
                            "percent": 4.77
                        },
                        {
                            "state": "NY",
                            "percent": 4.76
                        },
                        {
                            "state": "GA",
                            "percent": 4.41
                        },
                        {
                            "state": "PA",
                            "percent": 3.38
                        },
                        {
                            "state": "MI",
                            "percent": 3.08
                        },
                        {
                            "state": "NC",
                            "percent": 2.73
                        },
                        {
                            "state": "IL",
                            "percent": 2.68
                        },
                        {
                            "state": "VA",
                            "percent": 2.68
                        },
                        {
                            "state": "NJ",
                            "percent": 2.4
                        },
                        {
                            "state": "IN",
                            "percent": 2.37
                        },
                        {
                            "state": "MD",
                            "percent": 2.23
                        },
                        {
                            "state": "MO",
                            "percent": 2.11
                        },
                        {
                            "state": "AZ",
                            "percent": 1.72
                        },
                        {
                            "state": "TN",
                            "percent": 1.66
                        },
                        {
                            "state": "WA",
                            "percent": 1.49
                        },
                        {
                            "state": "AL",
                            "percent": 1.48
                        },
                        {
                            "state": "OK",
                            "percent": 1.23
                        },
                        {
                            "state": "LA",
                            "percent": 1.22
                        },
                        {
                            "state": "MN",
                            "percent": 1.18
                        },
                        {
                            "state": "SC",
                            "percent": 1.11
                        },
                        {
                            "state": "CT",
                            "percent": 1.08
                        },
                        {
                            "state": "CO",
                            "percent": 1.04
                        },
                        {
                            "state": "KY",
                            "percent": 1.04
                        },
                        {
                            "state": "WI",
                            "percent": 1.0
                        },
                        {
                            "state": "MS",
                            "percent": 0.96
                        },
                        {
                            "state": "NM",
                            "percent": 0.95
                        },
                        {
                            "state": "OR",
                            "percent": 0.89
                        },
                        {
                            "state": "AR",
                            "percent": 0.75
                        },
                        {
                            "state": "NV",
                            "percent": 0.7
                        },
                        {
                            "state": "MA",
                            "percent": 0.67
                        },
                        {
                            "state": "IA",
                            "percent": 0.61
                        },
                        {
                            "state": "UT",
                            "percent": 0.59
                        },
                        {
                            "state": "KS",
                            "percent": 0.58
                        },
                        {
                            "state": "DE",
                            "percent": 0.45
                        },
                        {
                            "state": "ID",
                            "percent": 0.4
                        },
                        {
                            "state": "NE",
                            "percent": 0.38
                        },
                        {
                            "state": "WV",
                            "percent": 0.27
                        },
                        {
                            "state": "ME",
                            "percent": 0.19
                        },
                        {
                            "state": "NH",
                            "percent": 0.16
                        },
                        {
                            "state": "HI",
                            "percent": 0.15
                        },
                        {
                            "state": "MT",
                            "percent": 0.13
                        },
                        {
                            "state": "AK",
                            "percent": 0.12
                        },
                        {
                            "state": "RI",
                            "percent": 0.12
                        },
                        {
                            "state": "WY",
                            "percent": 0.08
                        },
                        {
                            "state": "SD",
                            "percent": 0.07
                        },
                        {
                            "state": "VT",
                            "percent": 0.06
                        },
                        {
                            "state": "DC",
                            "percent": 0.04
                        },
                        {
                            "state": "ND",
                            "percent": 0.04
                        }
                    ],
                    "delinquencies": {
                        "del30Days": {
                            "percent": 3.14
                        },
                        "del60Days": {
                            "percent": 0.57
                        },
                        "del90Days": {
                            "percent": 0.21
                        },
                        "del90PlusDays": {
                            "percent": 0.59
                        },
                        "del120PlusDays": {
                            "percent": 0.38
                        }
                    },
                    "greenBondFlag": false,
                    "highestRating": "AAA",
                    "incomeCountry": "US",
                    "issuerCountry": "US",
                    "percentSecond": 0.0,
                    "poolAgeMethod": "Calculated",
                    "prepayEffDate": "2025-05-01",
                    "seniorityType": "NA",
                    "assetClassCode": "CO",
                    "cgmiSectorCode": "MTGE",
                    "cleanPayMonths": 0,
                    "collateralType": "GNMA",
                    "fullPledgeFlag": false,
                    "gpmPercentStep": 0.0,
                    "incomeCountry3": "USA",
                    "instrumentType": "NA",
                    "issuerCountry2": "US",
                    "issuerCountry3": "USA",
                    "lowestRatingNF": "AA+",
                    "poolIssuerName": "NA",
                    "vPointCategory": "RP",
                    "amortizedFHALTV": 63.0,
                    "bloombergTicker": "GNSF 3.5 2013",
                    "industrySubCode": "MT",
                    "originationDate": "2013-05-01",
                    "originationYear": 2013,
                    "percent2To4Unit": 2.7,
                    "percentHAMPMods": 0.9,
                    "percentPurchase": 31.8,
                    "percentStateHFA": 0.4,
                    "poolOriginalWAM": 0,
                    "preliminaryFlag": false,
                    "redemptionValue": 100.0,
                    "securitySubType": "MPGNMA",
                    "dataQuartileList": [
                        {
                            "ltvlow": 17.0,
                            "ltvhigh": 87.0,
                            "loanSizeLow": 22000.0,
                            "loanSizeHigh": 101000.0,
                            "percentDTILow": 10.0,
                            "creditScoreLow": 300.0,
                            "percentDTIHigh": 24.5,
                            "creditScoreHigh": 655.0,
                            "originalLoanAgeLow": 0,
                            "originationYearLow": 20101101,
                            "originalLoanAgeHigh": 0,
                            "originationYearHigh": 20130401
                        },
                        {
                            "ltvlow": 87.0,
                            "ltvhigh": 93.0,
                            "loanSizeLow": 101000.0,
                            "loanSizeHigh": 132000.0,
                            "percentDTILow": 24.5,
                            "creditScoreLow": 655.0,
                            "percentDTIHigh": 34.7,
                            "creditScoreHigh": 691.0,
                            "originalLoanAgeLow": 0,
                            "originationYearLow": 20130401,
                            "originalLoanAgeHigh": 0,
                            "originationYearHigh": 20130501
                        },
                        {
                            "ltvlow": 93.0,
                            "ltvhigh": 97.0,
                            "loanSizeLow": 132000.0,
                            "loanSizeHigh": 183000.0,
                            "percentDTILow": 34.7,
                            "creditScoreLow": 691.0,
                            "percentDTIHigh": 43.6,
                            "creditScoreHigh": 739.0,
                            "originalLoanAgeLow": 0,
                            "originationYearLow": 20130501,
                            "originalLoanAgeHigh": 1,
                            "originationYearHigh": 20130701
                        },
                        {
                            "ltvlow": 97.0,
                            "ltvhigh": 118.0,
                            "loanSizeLow": 183000.0,
                            "loanSizeHigh": 743000.0,
                            "percentDTILow": 43.6,
                            "creditScoreLow": 739.0,
                            "percentDTIHigh": 65.0,
                            "creditScoreHigh": 832.0,
                            "originalLoanAgeLow": 1,
                            "originationYearLow": 20130701,
                            "originalLoanAgeHigh": 43,
                            "originationYearHigh": 20141101
                        }
                    ],
                    "gpmNumberOfSteps": 0,
                    "percentHARPOwner": 0.0,
                    "percentPrincipal": 100.0,
                    "securityCalcType": "GNMA",
                    "assetClassSubCode": "MBS",
                    "forbearanceAmount": 0.0,
                    "modifiedTimeStamp": "2025-08-13T19:37:00Z",
                    "outstandingAmount": 1079.93,
                    "parentDescription": "NA",
                    "poolIsBalloonFlag": false,
                    "prepaymentOptions": {
                        "prepayType": [
                            "CPR",
                            "PSA",
                            "VEC"
                        ]
                    },
                    "reperformerMonths": 1,
                    "dataPPMHistoryList": [
                        {
                            "prepayType": "PSA",
                            "dataPPMHistoryDetailList": [
                                {
                                    "month": "1",
                                    "prepayRate": 104.2558
                                },
                                {
                                    "month": "3",
                                    "prepayRate": 101.9675
                                },
                                {
                                    "month": "6",
                                    "prepayRate": 101.3512
                                },
                                {
                                    "month": "12",
                                    "prepayRate": 101.4048
                                },
                                {
                                    "month": "24",
                                    "prepayRate": 0.0
                                }
                            ]
                        },
                        {
                            "prepayType": "CPR",
                            "dataPPMHistoryDetailList": [
                                {
                                    "month": "1",
                                    "prepayRate": 6.2554
                                },
                                {
                                    "month": "3",
                                    "prepayRate": 6.118
                                },
                                {
                                    "month": "6",
                                    "prepayRate": 6.0811
                                },
                                {
                                    "month": "12",
                                    "prepayRate": 6.0843
                                },
                                {
                                    "month": "24",
                                    "prepayRate": 0.0
                                }
                            ]
                        }
                    ],
                    "daysToFirstPayment": 44,
                    "issuerLowestRating": "NA",
                    "issuerMiddleRating": "NA",
                    "newCurrentLoanSize": 101863.0,
                    "originationChannel": {
                        "broker": 4.65,
                        "retail": 61.97,
                        "unknown": 0.0,
                        "unspecified": 0.0,
                        "correspondence": 33.37
                    },
                    "percentMultiFamily": 2.7,
                    "percentRefiCashout": 5.8,
                    "percentRegularMods": 3.6,
                    "percentReperformer": 0.5,
                    "relocationLoanFlag": false,
                    "socialDensityScore": 0.0,
                    "umbsfhlgPercentage": 0.0,
                    "umbsfnmaPercentage": 0.0,
                    "industryDescription": "Mortgage",
                    "issuerHighestRating": "NA",
                    "newOriginalLoanSize": 182051.0,
                    "socialCriteriaShare": 0.0,
                    "spreadAtOrigination": 22.3,
                    "weightedAvgLoanSize": 101863.0,
                    "poolOriginalLoanSize": 182051.0,
                    "cgmiSectorDescription": "Mortgage",
                    "cleanPayAverageMonths": 0,
                    "expModelAvailableFlag": true,
                    "fhfaImpliedCurrentLTV": 27.5,
                    "percentRefiNonCashout": 57.9,
                    "prepayPenaltySchedule": "0.000",
                    "defaultHorizonPYMethod": "OAS Change",
                    "industrySubDescription": "Mortgage Asset Backed",
                    "actualPrepayHistoryList": {
                        "date": "2025-10-01",
                        "genericValue": 0.9575
                    },
                    "adjustedCurrentLoanSize": 101863.0,
                    "forbearanceModification": 0.0,
                    "percentTwoPlusBorrowers": 44.0,
                    "poolAvgOriginalLoanTerm": 0,
                    "adjustedOriginalLoanSize": 182040.0,
                    "assetClassSubDescription": "Collateralized Asset Backed - Mortgage",
                    "mortgageInsurancePremium": {
                        "annual": {
                            "va": 0.0,
                            "fha": 0.797,
                            "pih": 0.0,
                            "rhs": 0.399
                        },
                        "upfront": {
                            "va": 0.5,
                            "fha": 0.693,
                            "pih": 1.0,
                            "rhs": 1.996
                        }
                    },
                    "percentReperformerAndMod": 0.1,
                    "reperformerMonthsForMods": 2,
                    "originalLoanSizeRemaining": 150891.0,
                    "percentFirstTimeHomeBuyer": 20.8,
                    "current3rdPartyOrigination": 38.02,
                    "adjustedSpreadAtOrigination": 22.3,
                    "dataPrepayModelServicerList": [
                        {
                            "percent": 23.84,
                            "servicer": "FREE"
                        },
                        {
                            "percent": 11.4,
                            "servicer": "NSTAR"
                        },
                        {
                            "percent": 11.39,
                            "servicer": "WELLS"
                        },
                        {
                            "percent": 11.15,
                            "servicer": "BCPOP"
                        },
                        {
                            "percent": 7.23,
                            "servicer": "QUICK"
                        },
                        {
                            "percent": 7.13,
                            "servicer": "PENNY"
                        },
                        {
                            "percent": 6.51,
                            "servicer": "LAKEV"
                        },
                        {
                            "percent": 6.34,
                            "servicer": "CARRG"
                        },
                        {
                            "percent": 5.5,
                            "servicer": "USB"
                        },
                        {
                            "percent": 2.41,
                            "servicer": "PNC"
                        },
                        {
                            "percent": 1.34,
                            "servicer": "MNTBK"
                        },
                        {
                            "percent": 1.17,
                            "servicer": "NWRES"
                        },
                        {
                            "percent": 0.95,
                            "servicer": "FIFTH"
                        },
                        {
                            "percent": 0.75,
                            "servicer": "DEPOT"
                        },
                        {
                            "percent": 0.6,
                            "servicer": "BOKF"
                        },
                        {
                            "percent": 0.51,
                            "servicer": "JPM"
                        },
                        {
                            "percent": 0.48,
                            "servicer": "TRUIS"
                        },
                        {
                            "percent": 0.42,
                            "servicer": "CITI"
                        },
                        {
                            "percent": 0.38,
                            "servicer": "GUILD"
                        },
                        {
                            "percent": 0.21,
                            "servicer": "REGNS"
                        },
                        {
                            "percent": 0.2,
                            "servicer": "CNTRL"
                        },
                        {
                            "percent": 0.09,
                            "servicer": "COLNL"
                        },
                        {
                            "percent": 0.06,
                            "servicer": "HFAGY"
                        },
                        {
                            "percent": 0.06,
                            "servicer": "MNSRC"
                        },
                        {
                            "percent": 0.03,
                            "servicer": "HOMBR"
                        }
                    ],
                    "nonWeightedOriginalLoanSize": 0.0,
                    "original3rdPartyOrigination": 0.0,
                    "percentHARPDec2010Extension": 0.0,
                    "percentHARPOneYearExtension": 0.0,
                    "percentDownPaymentAssistance": 5.6,
                    "percentAmortizedFHALTVUnder78": 95.4,
                    "loanPerformanceImpliedCurrentLTV": 44.8,
                    "reperformerMonthsForReperformers": 28
                },
                "ticker": "GNMA",
                "country": "US",
                "currency": "USD",
                "identifier": "999818YT",
                "description": "30-YR GNMA-2013 PROD",
                "issuerTicker": "GNMA",
                "maturityDate": "2041-12-01",
                "securityType": "MORT",
                "currentCoupon": 3.5,
                "securitySubType": "MPGNMA"
            }
        ]
    }


    >>> # Request bond indic with async post
    >>> response = request_bond_indic_async(input=[IdentifierInfo(identifier="999818YT",
    >>>                                                          id_type="CUSIP",
    >>>                                                          )])
    >>>
    >>> # Get results by request_id
    >>> results_response = get_result(request_id_parameter=response.request_id)
    >>>
    >>> # Print results in json format
    >>> print(js.dumps(results_response, indent=4))
    {
        "meta": {
            "status": "DONE",
            "requestId": "R-20897",
            "timeStamp": "2025-08-18T22:30:58Z",
            "responseType": "BOND_INDIC",
            "resultsStatus": "ALL"
        },
        "results": [
            {
                "cusip": "999818YT8",
                "indic": {
                    "ltv": 90.0,
                    "wam": 196,
                    "figi": "BBG0033WXBV4",
                    "cusip": "999818YT8",
                    "moody": [
                        {
                            "value": "Aaa"
                        }
                    ],
                    "source": "CITI",
                    "ticker": "GNMA",
                    "country": "US",
                    "loanAge": 147,
                    "lockout": 0,
                    "putFlag": false,
                    "callFlag": false,
                    "cobsCode": "MTGE",
                    "country2": "US",
                    "country3": "USA",
                    "currency": "USD",
                    "dayCount": "30/360 eom",
                    "glicCode": "MBS",
                    "grossWAC": 4.0,
                    "ioPeriod": 0,
                    "poolCode": "NA",
                    "sinkFlag": false,
                    "cmaTicker": "N/A",
                    "datedDate": "2013-05-01",
                    "gnma2Flag": false,
                    "percentVA": 11.04,
                    "currentLTV": 27.5,
                    "extendFlag": "N",
                    "isoCountry": "US",
                    "marketType": "DOMC",
                    "percentDTI": 34.0,
                    "percentFHA": 80.91,
                    "percentInv": 0.0,
                    "percentPIH": 0.14,
                    "percentRHS": 7.9,
                    "securityID": "999818YT",
                    "serviceFee": 0.5,
                    "vPointType": "MPGNMA",
                    "adjustedLTV": 27.5,
                    "combinedLTV": 90.7,
                    "creditScore": 692,
                    "description": "30-YR GNMA-2013 PROD",
                    "esgBondFlag": false,
                    "indexRating": "AA+",
                    "issueAmount": 8597.24,
                    "lowerRating": "AA+",
                    "paymentFreq": 12,
                    "percentHARP": 0.0,
                    "percentRefi": 63.7,
                    "tierCapital": "NA",
                    "balloonMonth": 0,
                    "deliveryFlag": "N",
                    "indexCountry": "US",
                    "industryCode": "MT",
                    "issuerTicker": "GNMA",
                    "lowestRating": "AA+",
                    "maturityDate": "2041-12-01",
                    "middleRating": "AA+",
                    "modifiedDate": "2025-08-13",
                    "originalTerm": 360,
                    "parentTicker": "GNMA",
                    "percentHARP2": 0.0,
                    "percentJumbo": 0.0,
                    "securityType": "MORT",
                    "currentCoupon": 3.5,
                    "dataStateList": [
                        {
                            "state": "PR",
                            "percent": 17.13
                        },
                        {
                            "state": "TX",
                            "percent": 10.03
                        },
                        {
                            "state": "FL",
                            "percent": 5.66
                        },
                        {
                            "state": "CA",
                            "percent": 4.95
                        },
                        {
                            "state": "OH",
                            "percent": 4.77
                        },
                        {
                            "state": "NY",
                            "percent": 4.76
                        },
                        {
                            "state": "GA",
                            "percent": 4.41
                        },
                        {
                            "state": "PA",
                            "percent": 3.38
                        },
                        {
                            "state": "MI",
                            "percent": 3.08
                        },
                        {
                            "state": "NC",
                            "percent": 2.73
                        },
                        {
                            "state": "IL",
                            "percent": 2.68
                        },
                        {
                            "state": "VA",
                            "percent": 2.68
                        },
                        {
                            "state": "NJ",
                            "percent": 2.4
                        },
                        {
                            "state": "IN",
                            "percent": 2.37
                        },
                        {
                            "state": "MD",
                            "percent": 2.23
                        },
                        {
                            "state": "MO",
                            "percent": 2.11
                        },
                        {
                            "state": "AZ",
                            "percent": 1.72
                        },
                        {
                            "state": "TN",
                            "percent": 1.66
                        },
                        {
                            "state": "WA",
                            "percent": 1.49
                        },
                        {
                            "state": "AL",
                            "percent": 1.48
                        },
                        {
                            "state": "OK",
                            "percent": 1.23
                        },
                        {
                            "state": "LA",
                            "percent": 1.22
                        },
                        {
                            "state": "MN",
                            "percent": 1.18
                        },
                        {
                            "state": "SC",
                            "percent": 1.11
                        },
                        {
                            "state": "CT",
                            "percent": 1.08
                        },
                        {
                            "state": "CO",
                            "percent": 1.04
                        },
                        {
                            "state": "KY",
                            "percent": 1.04
                        },
                        {
                            "state": "WI",
                            "percent": 1.0
                        },
                        {
                            "state": "MS",
                            "percent": 0.96
                        },
                        {
                            "state": "NM",
                            "percent": 0.95
                        },
                        {
                            "state": "OR",
                            "percent": 0.89
                        },
                        {
                            "state": "AR",
                            "percent": 0.75
                        },
                        {
                            "state": "NV",
                            "percent": 0.7
                        },
                        {
                            "state": "MA",
                            "percent": 0.67
                        },
                        {
                            "state": "IA",
                            "percent": 0.61
                        },
                        {
                            "state": "UT",
                            "percent": 0.59
                        },
                        {
                            "state": "KS",
                            "percent": 0.58
                        },
                        {
                            "state": "DE",
                            "percent": 0.45
                        },
                        {
                            "state": "ID",
                            "percent": 0.4
                        },
                        {
                            "state": "NE",
                            "percent": 0.38
                        },
                        {
                            "state": "WV",
                            "percent": 0.27
                        },
                        {
                            "state": "ME",
                            "percent": 0.19
                        },
                        {
                            "state": "NH",
                            "percent": 0.16
                        },
                        {
                            "state": "HI",
                            "percent": 0.15
                        },
                        {
                            "state": "MT",
                            "percent": 0.13
                        },
                        {
                            "state": "AK",
                            "percent": 0.12
                        },
                        {
                            "state": "RI",
                            "percent": 0.12
                        },
                        {
                            "state": "WY",
                            "percent": 0.08
                        },
                        {
                            "state": "SD",
                            "percent": 0.07
                        },
                        {
                            "state": "VT",
                            "percent": 0.06
                        },
                        {
                            "state": "DC",
                            "percent": 0.04
                        },
                        {
                            "state": "ND",
                            "percent": 0.04
                        }
                    ],
                    "delinquencies": {
                        "del30Days": {
                            "percent": 3.14
                        },
                        "del60Days": {
                            "percent": 0.57
                        },
                        "del90Days": {
                            "percent": 0.21
                        },
                        "del90PlusDays": {
                            "percent": 0.59
                        },
                        "del120PlusDays": {
                            "percent": 0.38
                        }
                    },
                    "greenBondFlag": false,
                    "highestRating": "AAA",
                    "incomeCountry": "US",
                    "issuerCountry": "US",
                    "percentSecond": 0.0,
                    "poolAgeMethod": "Calculated",
                    "prepayEffDate": "2025-05-01",
                    "seniorityType": "NA",
                    "assetClassCode": "CO",
                    "cgmiSectorCode": "MTGE",
                    "cleanPayMonths": 0,
                    "collateralType": "GNMA",
                    "fullPledgeFlag": false,
                    "gpmPercentStep": 0.0,
                    "incomeCountry3": "USA",
                    "instrumentType": "NA",
                    "issuerCountry2": "US",
                    "issuerCountry3": "USA",
                    "lowestRatingNF": "AA+",
                    "poolIssuerName": "NA",
                    "vPointCategory": "RP",
                    "amortizedFHALTV": 63.0,
                    "bloombergTicker": "GNSF 3.5 2013",
                    "industrySubCode": "MT",
                    "originationDate": "2013-05-01",
                    "originationYear": 2013,
                    "percent2To4Unit": 2.7,
                    "percentHAMPMods": 0.9,
                    "percentPurchase": 31.8,
                    "percentStateHFA": 0.4,
                    "poolOriginalWAM": 0,
                    "preliminaryFlag": false,
                    "redemptionValue": 100.0,
                    "securitySubType": "MPGNMA",
                    "dataQuartileList": [
                        {
                            "ltvlow": 17.0,
                            "ltvhigh": 87.0,
                            "loanSizeLow": 22000.0,
                            "loanSizeHigh": 101000.0,
                            "percentDTILow": 10.0,
                            "creditScoreLow": 300.0,
                            "percentDTIHigh": 24.5,
                            "creditScoreHigh": 655.0,
                            "originalLoanAgeLow": 0,
                            "originationYearLow": 20101101,
                            "originalLoanAgeHigh": 0,
                            "originationYearHigh": 20130401
                        },
                        {
                            "ltvlow": 87.0,
                            "ltvhigh": 93.0,
                            "loanSizeLow": 101000.0,
                            "loanSizeHigh": 132000.0,
                            "percentDTILow": 24.5,
                            "creditScoreLow": 655.0,
                            "percentDTIHigh": 34.7,
                            "creditScoreHigh": 691.0,
                            "originalLoanAgeLow": 0,
                            "originationYearLow": 20130401,
                            "originalLoanAgeHigh": 0,
                            "originationYearHigh": 20130501
                        },
                        {
                            "ltvlow": 93.0,
                            "ltvhigh": 97.0,
                            "loanSizeLow": 132000.0,
                            "loanSizeHigh": 183000.0,
                            "percentDTILow": 34.7,
                            "creditScoreLow": 691.0,
                            "percentDTIHigh": 43.6,
                            "creditScoreHigh": 739.0,
                            "originalLoanAgeLow": 0,
                            "originationYearLow": 20130501,
                            "originalLoanAgeHigh": 1,
                            "originationYearHigh": 20130701
                        },
                        {
                            "ltvlow": 97.0,
                            "ltvhigh": 118.0,
                            "loanSizeLow": 183000.0,
                            "loanSizeHigh": 743000.0,
                            "percentDTILow": 43.6,
                            "creditScoreLow": 739.0,
                            "percentDTIHigh": 65.0,
                            "creditScoreHigh": 832.0,
                            "originalLoanAgeLow": 1,
                            "originationYearLow": 20130701,
                            "originalLoanAgeHigh": 43,
                            "originationYearHigh": 20141101
                        }
                    ],
                    "gpmNumberOfSteps": 0,
                    "percentHARPOwner": 0.0,
                    "percentPrincipal": 100.0,
                    "securityCalcType": "GNMA",
                    "assetClassSubCode": "MBS",
                    "forbearanceAmount": 0.0,
                    "modifiedTimeStamp": "2025-08-13T19:37:00Z",
                    "outstandingAmount": 1079.93,
                    "parentDescription": "NA",
                    "poolIsBalloonFlag": false,
                    "prepaymentOptions": {
                        "prepayType": [
                            "CPR",
                            "PSA",
                            "VEC"
                        ]
                    },
                    "reperformerMonths": 1,
                    "dataPPMHistoryList": [
                        {
                            "prepayType": "PSA",
                            "dataPPMHistoryDetailList": [
                                {
                                    "month": "1",
                                    "prepayRate": 104.2558
                                },
                                {
                                    "month": "3",
                                    "prepayRate": 101.9675
                                },
                                {
                                    "month": "6",
                                    "prepayRate": 101.3512
                                },
                                {
                                    "month": "12",
                                    "prepayRate": 101.4048
                                },
                                {
                                    "month": "24",
                                    "prepayRate": 0.0
                                }
                            ]
                        },
                        {
                            "prepayType": "CPR",
                            "dataPPMHistoryDetailList": [
                                {
                                    "month": "1",
                                    "prepayRate": 6.2554
                                },
                                {
                                    "month": "3",
                                    "prepayRate": 6.118
                                },
                                {
                                    "month": "6",
                                    "prepayRate": 6.0811
                                },
                                {
                                    "month": "12",
                                    "prepayRate": 6.0843
                                },
                                {
                                    "month": "24",
                                    "prepayRate": 0.0
                                }
                            ]
                        }
                    ],
                    "daysToFirstPayment": 44,
                    "issuerLowestRating": "NA",
                    "issuerMiddleRating": "NA",
                    "newCurrentLoanSize": 101863.0,
                    "originationChannel": {
                        "broker": 4.65,
                        "retail": 61.97,
                        "unknown": 0.0,
                        "unspecified": 0.0,
                        "correspondence": 33.37
                    },
                    "percentMultiFamily": 2.7,
                    "percentRefiCashout": 5.8,
                    "percentRegularMods": 3.6,
                    "percentReperformer": 0.5,
                    "relocationLoanFlag": false,
                    "socialDensityScore": 0.0,
                    "umbsfhlgPercentage": 0.0,
                    "umbsfnmaPercentage": 0.0,
                    "industryDescription": "Mortgage",
                    "issuerHighestRating": "NA",
                    "newOriginalLoanSize": 182051.0,
                    "socialCriteriaShare": 0.0,
                    "spreadAtOrigination": 22.3,
                    "weightedAvgLoanSize": 101863.0,
                    "poolOriginalLoanSize": 182051.0,
                    "cgmiSectorDescription": "Mortgage",
                    "cleanPayAverageMonths": 0,
                    "expModelAvailableFlag": true,
                    "fhfaImpliedCurrentLTV": 27.5,
                    "percentRefiNonCashout": 57.9,
                    "prepayPenaltySchedule": "0.000",
                    "defaultHorizonPYMethod": "OAS Change",
                    "industrySubDescription": "Mortgage Asset Backed",
                    "actualPrepayHistoryList": {
                        "date": "2025-10-01",
                        "genericValue": 0.9575
                    },
                    "adjustedCurrentLoanSize": 101863.0,
                    "forbearanceModification": 0.0,
                    "percentTwoPlusBorrowers": 44.0,
                    "poolAvgOriginalLoanTerm": 0,
                    "adjustedOriginalLoanSize": 182040.0,
                    "assetClassSubDescription": "Collateralized Asset Backed - Mortgage",
                    "mortgageInsurancePremium": {
                        "annual": {
                            "va": 0.0,
                            "fha": 0.797,
                            "pih": 0.0,
                            "rhs": 0.399
                        },
                        "upfront": {
                            "va": 0.5,
                            "fha": 0.693,
                            "pih": 1.0,
                            "rhs": 1.996
                        }
                    },
                    "percentReperformerAndMod": 0.1,
                    "reperformerMonthsForMods": 2,
                    "originalLoanSizeRemaining": 150891.0,
                    "percentFirstTimeHomeBuyer": 20.8,
                    "current3rdPartyOrigination": 38.02,
                    "adjustedSpreadAtOrigination": 22.3,
                    "dataPrepayModelServicerList": [
                        {
                            "percent": 23.84,
                            "servicer": "FREE"
                        },
                        {
                            "percent": 11.4,
                            "servicer": "NSTAR"
                        },
                        {
                            "percent": 11.39,
                            "servicer": "WELLS"
                        },
                        {
                            "percent": 11.15,
                            "servicer": "BCPOP"
                        },
                        {
                            "percent": 7.23,
                            "servicer": "QUICK"
                        },
                        {
                            "percent": 7.13,
                            "servicer": "PENNY"
                        },
                        {
                            "percent": 6.51,
                            "servicer": "LAKEV"
                        },
                        {
                            "percent": 6.34,
                            "servicer": "CARRG"
                        },
                        {
                            "percent": 5.5,
                            "servicer": "USB"
                        },
                        {
                            "percent": 2.41,
                            "servicer": "PNC"
                        },
                        {
                            "percent": 1.34,
                            "servicer": "MNTBK"
                        },
                        {
                            "percent": 1.17,
                            "servicer": "NWRES"
                        },
                        {
                            "percent": 0.95,
                            "servicer": "FIFTH"
                        },
                        {
                            "percent": 0.75,
                            "servicer": "DEPOT"
                        },
                        {
                            "percent": 0.6,
                            "servicer": "BOKF"
                        },
                        {
                            "percent": 0.51,
                            "servicer": "JPM"
                        },
                        {
                            "percent": 0.48,
                            "servicer": "TRUIS"
                        },
                        {
                            "percent": 0.42,
                            "servicer": "CITI"
                        },
                        {
                            "percent": 0.38,
                            "servicer": "GUILD"
                        },
                        {
                            "percent": 0.21,
                            "servicer": "REGNS"
                        },
                        {
                            "percent": 0.2,
                            "servicer": "CNTRL"
                        },
                        {
                            "percent": 0.09,
                            "servicer": "COLNL"
                        },
                        {
                            "percent": 0.06,
                            "servicer": "HFAGY"
                        },
                        {
                            "percent": 0.06,
                            "servicer": "MNSRC"
                        },
                        {
                            "percent": 0.03,
                            "servicer": "HOMBR"
                        }
                    ],
                    "nonWeightedOriginalLoanSize": 0.0,
                    "original3rdPartyOrigination": 0.0,
                    "percentHARPDec2010Extension": 0.0,
                    "percentHARPOneYearExtension": 0.0,
                    "percentDownPaymentAssistance": 5.6,
                    "percentAmortizedFHALTVUnder78": 95.4,
                    "loanPerformanceImpliedCurrentLTV": 44.8,
                    "reperformerMonthsForReperformers": 28
                },
                "ticker": "GNMA",
                "country": "US",
                "currency": "USD",
                "identifier": "999818YT",
                "description": "30-YR GNMA-2013 PROD",
                "issuerTicker": "GNMA",
                "maturityDate": "2041-12-01",
                "securityType": "MORT",
                "currentCoupon": 3.5,
                "securitySubType": "MPGNMA"
            }
        ]
    }

    """

    try:
        logger.info("Calling request_bond_indic_async")

        response = Client().yield_book_rest.request_bond_indic_async(
            body=BondIndicRequest(input=input, keywords=keywords),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_bond_indic_async")

        return output
    except Exception as err:
        logger.error("Error request_bond_indic_async.")
        check_exception_and_raise(err, logger)


def request_bond_indic_async_get(
    *,
    id: str,
    id_type: Optional[Union[str, IdTypeEnum]] = None,
    keywords: Optional[List[str]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Asynchronous Get method to retrieve the contractual information about the reference data of instruments, which will typically not need any further calculations. Retrieve a request ID by which, using subsequent API 'getResult' endpoint, instrument reference data can be obtained given a BondIndicRequest - 'Input' - parameter that includes the information of which security or list of securities to be queried by CUSIP, ISIN, or other identifier type to obtain basic contractual information such as security type, sector,  maturity, credit ratings, coupon, and specific information based on security type like current pool factor if the requested identifier is a mortgage.

    Parameters
    ----------
    id : str
        A sequence of textual characters.
    id_type : Union[str, IdTypeEnum], optional

    keywords : List[str], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------
    >>> # Request bond indic with async get
    >>> response = request_bond_indic_async_get(id="999818YT", id_type=IdTypeEnum.CUSIP)
    >>>
    >>> # Get results by request_id
    >>> results_response = get_result(request_id_parameter=response.request_id)
    >>>
    >>> # Due to async nature, code Will perform the fetch 10 times, as result is not always ready instantly, with 3 second lapse between attempts
    >>> attempt = 1
    >>>
    >>> if not results_response:
    >>>     while attempt < 10:
    >>>         print(f"Attempt " + str(attempt) + " resulted in error retrieving results from:" + response.request_id)
    >>>
    >>>         time.sleep(10)
    >>>
    >>>         results_response = get_result(request_id_parameter=response.request_id)
    >>>
    >>>         if not results_response:
    >>>             attempt += 1
    >>>         else:
    >>>             break
    >>>
    >>> # Print results in json format
    >>> print(js.dumps(results_response, indent=4))
    {
        "data": {
            "cusip": "999818YT8",
            "indic": {
                "ltv": 90.0,
                "wam": 196,
                "figi": "BBG0033WXBV4",
                "cusip": "999818YT8",
                "moody": [
                    {
                        "value": "Aaa"
                    }
                ],
                "source": "CITI",
                "ticker": "GNMA",
                "country": "US",
                "loanAge": 147,
                "lockout": 0,
                "putFlag": false,
                "callFlag": false,
                "cobsCode": "MTGE",
                "country2": "US",
                "country3": "USA",
                "currency": "USD",
                "dayCount": "30/360 eom",
                "glicCode": "MBS",
                "grossWAC": 4.0,
                "ioPeriod": 0,
                "poolCode": "NA",
                "sinkFlag": false,
                "cmaTicker": "N/A",
                "datedDate": "2013-05-01",
                "gnma2Flag": false,
                "percentVA": 11.04,
                "currentLTV": 27.5,
                "extendFlag": "N",
                "isoCountry": "US",
                "marketType": "DOMC",
                "percentDTI": 34.0,
                "percentFHA": 80.91,
                "percentInv": 0.0,
                "percentPIH": 0.14,
                "percentRHS": 7.9,
                "securityID": "999818YT",
                "serviceFee": 0.5,
                "vPointType": "MPGNMA",
                "adjustedLTV": 27.5,
                "combinedLTV": 90.7,
                "creditScore": 692,
                "description": "30-YR GNMA-2013 PROD",
                "esgBondFlag": false,
                "indexRating": "AA+",
                "issueAmount": 8597.24,
                "lowerRating": "AA+",
                "paymentFreq": 12,
                "percentHARP": 0.0,
                "percentRefi": 63.7,
                "tierCapital": "NA",
                "balloonMonth": 0,
                "deliveryFlag": "N",
                "indexCountry": "US",
                "industryCode": "MT",
                "issuerTicker": "GNMA",
                "lowestRating": "AA+",
                "maturityDate": "2041-12-01",
                "middleRating": "AA+",
                "modifiedDate": "2025-08-13",
                "originalTerm": 360,
                "parentTicker": "GNMA",
                "percentHARP2": 0.0,
                "percentJumbo": 0.0,
                "securityType": "MORT",
                "currentCoupon": 3.5,
                "dataStateList": [
                    {
                        "state": "PR",
                        "percent": 17.13
                    },
                    {
                        "state": "TX",
                        "percent": 10.03
                    },
                    {
                        "state": "FL",
                        "percent": 5.66
                    },
                    {
                        "state": "CA",
                        "percent": 4.95
                    },
                    {
                        "state": "OH",
                        "percent": 4.77
                    },
                    {
                        "state": "NY",
                        "percent": 4.76
                    },
                    {
                        "state": "GA",
                        "percent": 4.41
                    },
                    {
                        "state": "PA",
                        "percent": 3.38
                    },
                    {
                        "state": "MI",
                        "percent": 3.08
                    },
                    {
                        "state": "NC",
                        "percent": 2.73
                    },
                    {
                        "state": "IL",
                        "percent": 2.68
                    },
                    {
                        "state": "VA",
                        "percent": 2.68
                    },
                    {
                        "state": "NJ",
                        "percent": 2.4
                    },
                    {
                        "state": "IN",
                        "percent": 2.37
                    },
                    {
                        "state": "MD",
                        "percent": 2.23
                    },
                    {
                        "state": "MO",
                        "percent": 2.11
                    },
                    {
                        "state": "AZ",
                        "percent": 1.72
                    },
                    {
                        "state": "TN",
                        "percent": 1.66
                    },
                    {
                        "state": "WA",
                        "percent": 1.49
                    },
                    {
                        "state": "AL",
                        "percent": 1.48
                    },
                    {
                        "state": "OK",
                        "percent": 1.23
                    },
                    {
                        "state": "LA",
                        "percent": 1.22
                    },
                    {
                        "state": "MN",
                        "percent": 1.18
                    },
                    {
                        "state": "SC",
                        "percent": 1.11
                    },
                    {
                        "state": "CT",
                        "percent": 1.08
                    },
                    {
                        "state": "CO",
                        "percent": 1.04
                    },
                    {
                        "state": "KY",
                        "percent": 1.04
                    },
                    {
                        "state": "WI",
                        "percent": 1.0
                    },
                    {
                        "state": "MS",
                        "percent": 0.96
                    },
                    {
                        "state": "NM",
                        "percent": 0.95
                    },
                    {
                        "state": "OR",
                        "percent": 0.89
                    },
                    {
                        "state": "AR",
                        "percent": 0.75
                    },
                    {
                        "state": "NV",
                        "percent": 0.7
                    },
                    {
                        "state": "MA",
                        "percent": 0.67
                    },
                    {
                        "state": "IA",
                        "percent": 0.61
                    },
                    {
                        "state": "UT",
                        "percent": 0.59
                    },
                    {
                        "state": "KS",
                        "percent": 0.58
                    },
                    {
                        "state": "DE",
                        "percent": 0.45
                    },
                    {
                        "state": "ID",
                        "percent": 0.4
                    },
                    {
                        "state": "NE",
                        "percent": 0.38
                    },
                    {
                        "state": "WV",
                        "percent": 0.27
                    },
                    {
                        "state": "ME",
                        "percent": 0.19
                    },
                    {
                        "state": "NH",
                        "percent": 0.16
                    },
                    {
                        "state": "HI",
                        "percent": 0.15
                    },
                    {
                        "state": "MT",
                        "percent": 0.13
                    },
                    {
                        "state": "AK",
                        "percent": 0.12
                    },
                    {
                        "state": "RI",
                        "percent": 0.12
                    },
                    {
                        "state": "WY",
                        "percent": 0.08
                    },
                    {
                        "state": "SD",
                        "percent": 0.07
                    },
                    {
                        "state": "VT",
                        "percent": 0.06
                    },
                    {
                        "state": "DC",
                        "percent": 0.04
                    },
                    {
                        "state": "ND",
                        "percent": 0.04
                    }
                ],
                "delinquencies": {
                    "del30Days": {
                        "percent": 3.14
                    },
                    "del60Days": {
                        "percent": 0.57
                    },
                    "del90Days": {
                        "percent": 0.21
                    },
                    "del90PlusDays": {
                        "percent": 0.59
                    },
                    "del120PlusDays": {
                        "percent": 0.38
                    }
                },
                "greenBondFlag": false,
                "highestRating": "AAA",
                "incomeCountry": "US",
                "issuerCountry": "US",
                "percentSecond": 0.0,
                "poolAgeMethod": "Calculated",
                "prepayEffDate": "2025-05-01",
                "seniorityType": "NA",
                "assetClassCode": "CO",
                "cgmiSectorCode": "MTGE",
                "cleanPayMonths": 0,
                "collateralType": "GNMA",
                "fullPledgeFlag": false,
                "gpmPercentStep": 0.0,
                "incomeCountry3": "USA",
                "instrumentType": "NA",
                "issuerCountry2": "US",
                "issuerCountry3": "USA",
                "lowestRatingNF": "AA+",
                "poolIssuerName": "NA",
                "vPointCategory": "RP",
                "amortizedFHALTV": 63.0,
                "bloombergTicker": "GNSF 3.5 2013",
                "industrySubCode": "MT",
                "originationDate": "2013-05-01",
                "originationYear": 2013,
                "percent2To4Unit": 2.7,
                "percentHAMPMods": 0.9,
                "percentPurchase": 31.8,
                "percentStateHFA": 0.4,
                "poolOriginalWAM": 0,
                "preliminaryFlag": false,
                "redemptionValue": 100.0,
                "securitySubType": "MPGNMA",
                "dataQuartileList": [
                    {
                        "ltvlow": 17.0,
                        "ltvhigh": 87.0,
                        "loanSizeLow": 22000.0,
                        "loanSizeHigh": 101000.0,
                        "percentDTILow": 10.0,
                        "creditScoreLow": 300.0,
                        "percentDTIHigh": 24.5,
                        "creditScoreHigh": 655.0,
                        "originalLoanAgeLow": 0,
                        "originationYearLow": 20101101,
                        "originalLoanAgeHigh": 0,
                        "originationYearHigh": 20130401
                    },
                    {
                        "ltvlow": 87.0,
                        "ltvhigh": 93.0,
                        "loanSizeLow": 101000.0,
                        "loanSizeHigh": 132000.0,
                        "percentDTILow": 24.5,
                        "creditScoreLow": 655.0,
                        "percentDTIHigh": 34.7,
                        "creditScoreHigh": 691.0,
                        "originalLoanAgeLow": 0,
                        "originationYearLow": 20130401,
                        "originalLoanAgeHigh": 0,
                        "originationYearHigh": 20130501
                    },
                    {
                        "ltvlow": 93.0,
                        "ltvhigh": 97.0,
                        "loanSizeLow": 132000.0,
                        "loanSizeHigh": 183000.0,
                        "percentDTILow": 34.7,
                        "creditScoreLow": 691.0,
                        "percentDTIHigh": 43.6,
                        "creditScoreHigh": 739.0,
                        "originalLoanAgeLow": 0,
                        "originationYearLow": 20130501,
                        "originalLoanAgeHigh": 1,
                        "originationYearHigh": 20130701
                    },
                    {
                        "ltvlow": 97.0,
                        "ltvhigh": 118.0,
                        "loanSizeLow": 183000.0,
                        "loanSizeHigh": 743000.0,
                        "percentDTILow": 43.6,
                        "creditScoreLow": 739.0,
                        "percentDTIHigh": 65.0,
                        "creditScoreHigh": 832.0,
                        "originalLoanAgeLow": 1,
                        "originationYearLow": 20130701,
                        "originalLoanAgeHigh": 43,
                        "originationYearHigh": 20141101
                    }
                ],
                "gpmNumberOfSteps": 0,
                "percentHARPOwner": 0.0,
                "percentPrincipal": 100.0,
                "securityCalcType": "GNMA",
                "assetClassSubCode": "MBS",
                "forbearanceAmount": 0.0,
                "modifiedTimeStamp": "2025-08-13T19:37:00Z",
                "outstandingAmount": 1079.93,
                "parentDescription": "NA",
                "poolIsBalloonFlag": false,
                "prepaymentOptions": {
                    "prepayType": [
                        "CPR",
                        "PSA",
                        "VEC"
                    ]
                },
                "reperformerMonths": 1,
                "dataPPMHistoryList": [
                    {
                        "prepayType": "PSA",
                        "dataPPMHistoryDetailList": [
                            {
                                "month": "1",
                                "prepayRate": 104.2558
                            },
                            {
                                "month": "3",
                                "prepayRate": 101.9675
                            },
                            {
                                "month": "6",
                                "prepayRate": 101.3512
                            },
                            {
                                "month": "12",
                                "prepayRate": 101.4048
                            },
                            {
                                "month": "24",
                                "prepayRate": 0.0
                            }
                        ]
                    },
                    {
                        "prepayType": "CPR",
                        "dataPPMHistoryDetailList": [
                            {
                                "month": "1",
                                "prepayRate": 6.2554
                            },
                            {
                                "month": "3",
                                "prepayRate": 6.118
                            },
                            {
                                "month": "6",
                                "prepayRate": 6.0811
                            },
                            {
                                "month": "12",
                                "prepayRate": 6.0843
                            },
                            {
                                "month": "24",
                                "prepayRate": 0.0
                            }
                        ]
                    }
                ],
                "daysToFirstPayment": 44,
                "issuerLowestRating": "NA",
                "issuerMiddleRating": "NA",
                "newCurrentLoanSize": 101863.0,
                "originationChannel": {
                    "broker": 4.65,
                    "retail": 61.97,
                    "unknown": 0.0,
                    "unspecified": 0.0,
                    "correspondence": 33.37
                },
                "percentMultiFamily": 2.7,
                "percentRefiCashout": 5.8,
                "percentRegularMods": 3.6,
                "percentReperformer": 0.5,
                "relocationLoanFlag": false,
                "socialDensityScore": 0.0,
                "umbsfhlgPercentage": 0.0,
                "umbsfnmaPercentage": 0.0,
                "industryDescription": "Mortgage",
                "issuerHighestRating": "NA",
                "newOriginalLoanSize": 182051.0,
                "socialCriteriaShare": 0.0,
                "spreadAtOrigination": 22.3,
                "weightedAvgLoanSize": 101863.0,
                "poolOriginalLoanSize": 182051.0,
                "cgmiSectorDescription": "Mortgage",
                "cleanPayAverageMonths": 0,
                "expModelAvailableFlag": true,
                "fhfaImpliedCurrentLTV": 27.5,
                "percentRefiNonCashout": 57.9,
                "prepayPenaltySchedule": "0.000",
                "defaultHorizonPYMethod": "OAS Change",
                "industrySubDescription": "Mortgage Asset Backed",
                "actualPrepayHistoryList": {
                    "date": "2025-10-01",
                    "genericValue": 0.9575
                },
                "adjustedCurrentLoanSize": 101863.0,
                "forbearanceModification": 0.0,
                "percentTwoPlusBorrowers": 44.0,
                "poolAvgOriginalLoanTerm": 0,
                "adjustedOriginalLoanSize": 182040.0,
                "assetClassSubDescription": "Collateralized Asset Backed - Mortgage",
                "mortgageInsurancePremium": {
                    "annual": {
                        "va": 0.0,
                        "fha": 0.797,
                        "pih": 0.0,
                        "rhs": 0.399
                    },
                    "upfront": {
                        "va": 0.5,
                        "fha": 0.693,
                        "pih": 1.0,
                        "rhs": 1.996
                    }
                },
                "percentReperformerAndMod": 0.1,
                "reperformerMonthsForMods": 2,
                "originalLoanSizeRemaining": 150891.0,
                "percentFirstTimeHomeBuyer": 20.8,
                "current3rdPartyOrigination": 38.02,
                "adjustedSpreadAtOrigination": 22.3,
                "dataPrepayModelServicerList": [
                    {
                        "percent": 23.84,
                        "servicer": "FREE"
                    },
                    {
                        "percent": 11.4,
                        "servicer": "NSTAR"
                    },
                    {
                        "percent": 11.39,
                        "servicer": "WELLS"
                    },
                    {
                        "percent": 11.15,
                        "servicer": "BCPOP"
                    },
                    {
                        "percent": 7.23,
                        "servicer": "QUICK"
                    },
                    {
                        "percent": 7.13,
                        "servicer": "PENNY"
                    },
                    {
                        "percent": 6.51,
                        "servicer": "LAKEV"
                    },
                    {
                        "percent": 6.34,
                        "servicer": "CARRG"
                    },
                    {
                        "percent": 5.5,
                        "servicer": "USB"
                    },
                    {
                        "percent": 2.41,
                        "servicer": "PNC"
                    },
                    {
                        "percent": 1.34,
                        "servicer": "MNTBK"
                    },
                    {
                        "percent": 1.17,
                        "servicer": "NWRES"
                    },
                    {
                        "percent": 0.95,
                        "servicer": "FIFTH"
                    },
                    {
                        "percent": 0.75,
                        "servicer": "DEPOT"
                    },
                    {
                        "percent": 0.6,
                        "servicer": "BOKF"
                    },
                    {
                        "percent": 0.51,
                        "servicer": "JPM"
                    },
                    {
                        "percent": 0.48,
                        "servicer": "TRUIS"
                    },
                    {
                        "percent": 0.42,
                        "servicer": "CITI"
                    },
                    {
                        "percent": 0.38,
                        "servicer": "GUILD"
                    },
                    {
                        "percent": 0.21,
                        "servicer": "REGNS"
                    },
                    {
                        "percent": 0.2,
                        "servicer": "CNTRL"
                    },
                    {
                        "percent": 0.09,
                        "servicer": "COLNL"
                    },
                    {
                        "percent": 0.06,
                        "servicer": "HFAGY"
                    },
                    {
                        "percent": 0.06,
                        "servicer": "MNSRC"
                    },
                    {
                        "percent": 0.03,
                        "servicer": "HOMBR"
                    }
                ],
                "nonWeightedOriginalLoanSize": 0.0,
                "original3rdPartyOrigination": 0.0,
                "percentHARPDec2010Extension": 0.0,
                "percentHARPOneYearExtension": 0.0,
                "percentDownPaymentAssistance": 5.6,
                "percentAmortizedFHALTVUnder78": 95.4,
                "loanPerformanceImpliedCurrentLTV": 44.8,
                "reperformerMonthsForReperformers": 28
            },
            "ticker": "GNMA",
            "country": "US",
            "currency": "USD",
            "identifier": "999818YT",
            "description": "30-YR GNMA-2013 PROD",
            "issuerTicker": "GNMA",
            "maturityDate": "2041-12-01",
            "securityType": "MORT",
            "currentCoupon": 3.5,
            "securitySubType": "MPGNMA"
        },
        "meta": {
            "status": "DONE",
            "requestId": "R-20894",
            "timeStamp": "2025-08-18T22:30:44Z",
            "responseType": "BOND_INDIC"
        }
    }


    >>> # Request bond indic with async get
    >>> response = request_bond_indic_async_get(
    >>>                                     id="999818YT",
    >>>                                     id_type=IdTypeEnum.CUSIP
    >>>                                     )
    >>>
    >>> # Get results by request_id
    >>> results_response = get_result(request_id_parameter=response.request_id)
    >>>
    >>> # Due to async nature, code Will perform the fetch 10 times, as result is not always ready instantly, with 3 second lapse between attempts
    >>> attempt = 1
    >>>
    >>> if not results_response:
    >>>     while attempt < 10:
    >>>         print(f"Attempt " + str(attempt) + " resulted in error retrieving results from:" + response.request_id)
    >>>
    >>>         time.sleep(10)
    >>>
    >>>         results_response = get_result(request_id_parameter=response.request_id)
    >>>
    >>>         if not results_response:
    >>>             attempt += 1
    >>>         else:
    >>>             break
    >>>
    >>> # Print results in json format
    >>> print(js.dumps(results_response, indent=4))
    {
        "data": {
            "cusip": "999818YT8",
            "indic": {
                "ltv": 90.0,
                "wam": 196,
                "figi": "BBG0033WXBV4",
                "cusip": "999818YT8",
                "moody": [
                    {
                        "value": "Aaa"
                    }
                ],
                "source": "CITI",
                "ticker": "GNMA",
                "country": "US",
                "loanAge": 147,
                "lockout": 0,
                "putFlag": false,
                "callFlag": false,
                "cobsCode": "MTGE",
                "country2": "US",
                "country3": "USA",
                "currency": "USD",
                "dayCount": "30/360 eom",
                "glicCode": "MBS",
                "grossWAC": 4.0,
                "ioPeriod": 0,
                "poolCode": "NA",
                "sinkFlag": false,
                "cmaTicker": "N/A",
                "datedDate": "2013-05-01",
                "gnma2Flag": false,
                "percentVA": 11.04,
                "currentLTV": 27.5,
                "extendFlag": "N",
                "isoCountry": "US",
                "marketType": "DOMC",
                "percentDTI": 34.0,
                "percentFHA": 80.91,
                "percentInv": 0.0,
                "percentPIH": 0.14,
                "percentRHS": 7.9,
                "securityID": "999818YT",
                "serviceFee": 0.5,
                "vPointType": "MPGNMA",
                "adjustedLTV": 27.5,
                "combinedLTV": 90.7,
                "creditScore": 692,
                "description": "30-YR GNMA-2013 PROD",
                "esgBondFlag": false,
                "indexRating": "AA+",
                "issueAmount": 8597.24,
                "lowerRating": "AA+",
                "paymentFreq": 12,
                "percentHARP": 0.0,
                "percentRefi": 63.7,
                "tierCapital": "NA",
                "balloonMonth": 0,
                "deliveryFlag": "N",
                "indexCountry": "US",
                "industryCode": "MT",
                "issuerTicker": "GNMA",
                "lowestRating": "AA+",
                "maturityDate": "2041-12-01",
                "middleRating": "AA+",
                "modifiedDate": "2025-08-13",
                "originalTerm": 360,
                "parentTicker": "GNMA",
                "percentHARP2": 0.0,
                "percentJumbo": 0.0,
                "securityType": "MORT",
                "currentCoupon": 3.5,
                "dataStateList": [
                    {
                        "state": "PR",
                        "percent": 17.13
                    },
                    {
                        "state": "TX",
                        "percent": 10.03
                    },
                    {
                        "state": "FL",
                        "percent": 5.66
                    },
                    {
                        "state": "CA",
                        "percent": 4.95
                    },
                    {
                        "state": "OH",
                        "percent": 4.77
                    },
                    {
                        "state": "NY",
                        "percent": 4.76
                    },
                    {
                        "state": "GA",
                        "percent": 4.41
                    },
                    {
                        "state": "PA",
                        "percent": 3.38
                    },
                    {
                        "state": "MI",
                        "percent": 3.08
                    },
                    {
                        "state": "NC",
                        "percent": 2.73
                    },
                    {
                        "state": "IL",
                        "percent": 2.68
                    },
                    {
                        "state": "VA",
                        "percent": 2.68
                    },
                    {
                        "state": "NJ",
                        "percent": 2.4
                    },
                    {
                        "state": "IN",
                        "percent": 2.37
                    },
                    {
                        "state": "MD",
                        "percent": 2.23
                    },
                    {
                        "state": "MO",
                        "percent": 2.11
                    },
                    {
                        "state": "AZ",
                        "percent": 1.72
                    },
                    {
                        "state": "TN",
                        "percent": 1.66
                    },
                    {
                        "state": "WA",
                        "percent": 1.49
                    },
                    {
                        "state": "AL",
                        "percent": 1.48
                    },
                    {
                        "state": "OK",
                        "percent": 1.23
                    },
                    {
                        "state": "LA",
                        "percent": 1.22
                    },
                    {
                        "state": "MN",
                        "percent": 1.18
                    },
                    {
                        "state": "SC",
                        "percent": 1.11
                    },
                    {
                        "state": "CT",
                        "percent": 1.08
                    },
                    {
                        "state": "CO",
                        "percent": 1.04
                    },
                    {
                        "state": "KY",
                        "percent": 1.04
                    },
                    {
                        "state": "WI",
                        "percent": 1.0
                    },
                    {
                        "state": "MS",
                        "percent": 0.96
                    },
                    {
                        "state": "NM",
                        "percent": 0.95
                    },
                    {
                        "state": "OR",
                        "percent": 0.89
                    },
                    {
                        "state": "AR",
                        "percent": 0.75
                    },
                    {
                        "state": "NV",
                        "percent": 0.7
                    },
                    {
                        "state": "MA",
                        "percent": 0.67
                    },
                    {
                        "state": "IA",
                        "percent": 0.61
                    },
                    {
                        "state": "UT",
                        "percent": 0.59
                    },
                    {
                        "state": "KS",
                        "percent": 0.58
                    },
                    {
                        "state": "DE",
                        "percent": 0.45
                    },
                    {
                        "state": "ID",
                        "percent": 0.4
                    },
                    {
                        "state": "NE",
                        "percent": 0.38
                    },
                    {
                        "state": "WV",
                        "percent": 0.27
                    },
                    {
                        "state": "ME",
                        "percent": 0.19
                    },
                    {
                        "state": "NH",
                        "percent": 0.16
                    },
                    {
                        "state": "HI",
                        "percent": 0.15
                    },
                    {
                        "state": "MT",
                        "percent": 0.13
                    },
                    {
                        "state": "AK",
                        "percent": 0.12
                    },
                    {
                        "state": "RI",
                        "percent": 0.12
                    },
                    {
                        "state": "WY",
                        "percent": 0.08
                    },
                    {
                        "state": "SD",
                        "percent": 0.07
                    },
                    {
                        "state": "VT",
                        "percent": 0.06
                    },
                    {
                        "state": "DC",
                        "percent": 0.04
                    },
                    {
                        "state": "ND",
                        "percent": 0.04
                    }
                ],
                "delinquencies": {
                    "del30Days": {
                        "percent": 3.14
                    },
                    "del60Days": {
                        "percent": 0.57
                    },
                    "del90Days": {
                        "percent": 0.21
                    },
                    "del90PlusDays": {
                        "percent": 0.59
                    },
                    "del120PlusDays": {
                        "percent": 0.38
                    }
                },
                "greenBondFlag": false,
                "highestRating": "AAA",
                "incomeCountry": "US",
                "issuerCountry": "US",
                "percentSecond": 0.0,
                "poolAgeMethod": "Calculated",
                "prepayEffDate": "2025-05-01",
                "seniorityType": "NA",
                "assetClassCode": "CO",
                "cgmiSectorCode": "MTGE",
                "cleanPayMonths": 0,
                "collateralType": "GNMA",
                "fullPledgeFlag": false,
                "gpmPercentStep": 0.0,
                "incomeCountry3": "USA",
                "instrumentType": "NA",
                "issuerCountry2": "US",
                "issuerCountry3": "USA",
                "lowestRatingNF": "AA+",
                "poolIssuerName": "NA",
                "vPointCategory": "RP",
                "amortizedFHALTV": 63.0,
                "bloombergTicker": "GNSF 3.5 2013",
                "industrySubCode": "MT",
                "originationDate": "2013-05-01",
                "originationYear": 2013,
                "percent2To4Unit": 2.7,
                "percentHAMPMods": 0.9,
                "percentPurchase": 31.8,
                "percentStateHFA": 0.4,
                "poolOriginalWAM": 0,
                "preliminaryFlag": false,
                "redemptionValue": 100.0,
                "securitySubType": "MPGNMA",
                "dataQuartileList": [
                    {
                        "ltvlow": 17.0,
                        "ltvhigh": 87.0,
                        "loanSizeLow": 22000.0,
                        "loanSizeHigh": 101000.0,
                        "percentDTILow": 10.0,
                        "creditScoreLow": 300.0,
                        "percentDTIHigh": 24.5,
                        "creditScoreHigh": 655.0,
                        "originalLoanAgeLow": 0,
                        "originationYearLow": 20101101,
                        "originalLoanAgeHigh": 0,
                        "originationYearHigh": 20130401
                    },
                    {
                        "ltvlow": 87.0,
                        "ltvhigh": 93.0,
                        "loanSizeLow": 101000.0,
                        "loanSizeHigh": 132000.0,
                        "percentDTILow": 24.5,
                        "creditScoreLow": 655.0,
                        "percentDTIHigh": 34.7,
                        "creditScoreHigh": 691.0,
                        "originalLoanAgeLow": 0,
                        "originationYearLow": 20130401,
                        "originalLoanAgeHigh": 0,
                        "originationYearHigh": 20130501
                    },
                    {
                        "ltvlow": 93.0,
                        "ltvhigh": 97.0,
                        "loanSizeLow": 132000.0,
                        "loanSizeHigh": 183000.0,
                        "percentDTILow": 34.7,
                        "creditScoreLow": 691.0,
                        "percentDTIHigh": 43.6,
                        "creditScoreHigh": 739.0,
                        "originalLoanAgeLow": 0,
                        "originationYearLow": 20130501,
                        "originalLoanAgeHigh": 1,
                        "originationYearHigh": 20130701
                    },
                    {
                        "ltvlow": 97.0,
                        "ltvhigh": 118.0,
                        "loanSizeLow": 183000.0,
                        "loanSizeHigh": 743000.0,
                        "percentDTILow": 43.6,
                        "creditScoreLow": 739.0,
                        "percentDTIHigh": 65.0,
                        "creditScoreHigh": 832.0,
                        "originalLoanAgeLow": 1,
                        "originationYearLow": 20130701,
                        "originalLoanAgeHigh": 43,
                        "originationYearHigh": 20141101
                    }
                ],
                "gpmNumberOfSteps": 0,
                "percentHARPOwner": 0.0,
                "percentPrincipal": 100.0,
                "securityCalcType": "GNMA",
                "assetClassSubCode": "MBS",
                "forbearanceAmount": 0.0,
                "modifiedTimeStamp": "2025-08-13T19:37:00Z",
                "outstandingAmount": 1079.93,
                "parentDescription": "NA",
                "poolIsBalloonFlag": false,
                "prepaymentOptions": {
                    "prepayType": [
                        "CPR",
                        "PSA",
                        "VEC"
                    ]
                },
                "reperformerMonths": 1,
                "dataPPMHistoryList": [
                    {
                        "prepayType": "PSA",
                        "dataPPMHistoryDetailList": [
                            {
                                "month": "1",
                                "prepayRate": 104.2558
                            },
                            {
                                "month": "3",
                                "prepayRate": 101.9675
                            },
                            {
                                "month": "6",
                                "prepayRate": 101.3512
                            },
                            {
                                "month": "12",
                                "prepayRate": 101.4048
                            },
                            {
                                "month": "24",
                                "prepayRate": 0.0
                            }
                        ]
                    },
                    {
                        "prepayType": "CPR",
                        "dataPPMHistoryDetailList": [
                            {
                                "month": "1",
                                "prepayRate": 6.2554
                            },
                            {
                                "month": "3",
                                "prepayRate": 6.118
                            },
                            {
                                "month": "6",
                                "prepayRate": 6.0811
                            },
                            {
                                "month": "12",
                                "prepayRate": 6.0843
                            },
                            {
                                "month": "24",
                                "prepayRate": 0.0
                            }
                        ]
                    }
                ],
                "daysToFirstPayment": 44,
                "issuerLowestRating": "NA",
                "issuerMiddleRating": "NA",
                "newCurrentLoanSize": 101863.0,
                "originationChannel": {
                    "broker": 4.65,
                    "retail": 61.97,
                    "unknown": 0.0,
                    "unspecified": 0.0,
                    "correspondence": 33.37
                },
                "percentMultiFamily": 2.7,
                "percentRefiCashout": 5.8,
                "percentRegularMods": 3.6,
                "percentReperformer": 0.5,
                "relocationLoanFlag": false,
                "socialDensityScore": 0.0,
                "umbsfhlgPercentage": 0.0,
                "umbsfnmaPercentage": 0.0,
                "industryDescription": "Mortgage",
                "issuerHighestRating": "NA",
                "newOriginalLoanSize": 182051.0,
                "socialCriteriaShare": 0.0,
                "spreadAtOrigination": 22.3,
                "weightedAvgLoanSize": 101863.0,
                "poolOriginalLoanSize": 182051.0,
                "cgmiSectorDescription": "Mortgage",
                "cleanPayAverageMonths": 0,
                "expModelAvailableFlag": true,
                "fhfaImpliedCurrentLTV": 27.5,
                "percentRefiNonCashout": 57.9,
                "prepayPenaltySchedule": "0.000",
                "defaultHorizonPYMethod": "OAS Change",
                "industrySubDescription": "Mortgage Asset Backed",
                "actualPrepayHistoryList": {
                    "date": "2025-10-01",
                    "genericValue": 0.9575
                },
                "adjustedCurrentLoanSize": 101863.0,
                "forbearanceModification": 0.0,
                "percentTwoPlusBorrowers": 44.0,
                "poolAvgOriginalLoanTerm": 0,
                "adjustedOriginalLoanSize": 182040.0,
                "assetClassSubDescription": "Collateralized Asset Backed - Mortgage",
                "mortgageInsurancePremium": {
                    "annual": {
                        "va": 0.0,
                        "fha": 0.797,
                        "pih": 0.0,
                        "rhs": 0.399
                    },
                    "upfront": {
                        "va": 0.5,
                        "fha": 0.693,
                        "pih": 1.0,
                        "rhs": 1.996
                    }
                },
                "percentReperformerAndMod": 0.1,
                "reperformerMonthsForMods": 2,
                "originalLoanSizeRemaining": 150891.0,
                "percentFirstTimeHomeBuyer": 20.8,
                "current3rdPartyOrigination": 38.02,
                "adjustedSpreadAtOrigination": 22.3,
                "dataPrepayModelServicerList": [
                    {
                        "percent": 23.84,
                        "servicer": "FREE"
                    },
                    {
                        "percent": 11.4,
                        "servicer": "NSTAR"
                    },
                    {
                        "percent": 11.39,
                        "servicer": "WELLS"
                    },
                    {
                        "percent": 11.15,
                        "servicer": "BCPOP"
                    },
                    {
                        "percent": 7.23,
                        "servicer": "QUICK"
                    },
                    {
                        "percent": 7.13,
                        "servicer": "PENNY"
                    },
                    {
                        "percent": 6.51,
                        "servicer": "LAKEV"
                    },
                    {
                        "percent": 6.34,
                        "servicer": "CARRG"
                    },
                    {
                        "percent": 5.5,
                        "servicer": "USB"
                    },
                    {
                        "percent": 2.41,
                        "servicer": "PNC"
                    },
                    {
                        "percent": 1.34,
                        "servicer": "MNTBK"
                    },
                    {
                        "percent": 1.17,
                        "servicer": "NWRES"
                    },
                    {
                        "percent": 0.95,
                        "servicer": "FIFTH"
                    },
                    {
                        "percent": 0.75,
                        "servicer": "DEPOT"
                    },
                    {
                        "percent": 0.6,
                        "servicer": "BOKF"
                    },
                    {
                        "percent": 0.51,
                        "servicer": "JPM"
                    },
                    {
                        "percent": 0.48,
                        "servicer": "TRUIS"
                    },
                    {
                        "percent": 0.42,
                        "servicer": "CITI"
                    },
                    {
                        "percent": 0.38,
                        "servicer": "GUILD"
                    },
                    {
                        "percent": 0.21,
                        "servicer": "REGNS"
                    },
                    {
                        "percent": 0.2,
                        "servicer": "CNTRL"
                    },
                    {
                        "percent": 0.09,
                        "servicer": "COLNL"
                    },
                    {
                        "percent": 0.06,
                        "servicer": "HFAGY"
                    },
                    {
                        "percent": 0.06,
                        "servicer": "MNSRC"
                    },
                    {
                        "percent": 0.03,
                        "servicer": "HOMBR"
                    }
                ],
                "nonWeightedOriginalLoanSize": 0.0,
                "original3rdPartyOrigination": 0.0,
                "percentHARPDec2010Extension": 0.0,
                "percentHARPOneYearExtension": 0.0,
                "percentDownPaymentAssistance": 5.6,
                "percentAmortizedFHALTVUnder78": 95.4,
                "loanPerformanceImpliedCurrentLTV": 44.8,
                "reperformerMonthsForReperformers": 28
            },
            "ticker": "GNMA",
            "country": "US",
            "currency": "USD",
            "identifier": "999818YT",
            "description": "30-YR GNMA-2013 PROD",
            "issuerTicker": "GNMA",
            "maturityDate": "2041-12-01",
            "securityType": "MORT",
            "currentCoupon": 3.5,
            "securitySubType": "MPGNMA"
        },
        "meta": {
            "status": "DONE",
            "requestId": "R-20895",
            "timeStamp": "2025-08-18T22:30:49Z",
            "responseType": "BOND_INDIC"
        }
    }

    """

    try:
        logger.info("Calling request_bond_indic_async_get")

        response = Client().yield_book_rest.request_bond_indic_async_get(
            id=id,
            id_type=id_type,
            keywords=keywords,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_bond_indic_async_get")

        return output
    except Exception as err:
        logger.error("Error request_bond_indic_async_get.")
        check_exception_and_raise(err, logger)


def request_bond_indic_sync(
    *,
    input: Optional[List[IdentifierInfo]] = None,
    keywords: Optional[List[str]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> MappedResponseRefData:
    """
    Synchronous Post method to retrieve the contractual information about the reference data of instruments, which will typically not need any further calculations. Retrieve instrument reference data given a BondIndicRequest - 'Input' - parameter that includes the information of which security or list of securities to be queried by CUSIP, ISIN, or other identifier type to obtain basic contractual information in the MappedResponseRefData such as security type, sector,  maturity, credit ratings, coupon, and specific information based on security type like current pool factor if the requested identifier is a mortgage. Recommended and preferred method for single or low-volume instrument queries (up to 50-70 per request, 250 max).

    Parameters
    ----------
    input : List[IdentifierInfo], optional
        Single identifier or a list of identifiers to search instruments by.
    keywords : List[str], optional
        List of keywords from the MappedResponseRefData to be exposed in the result data set.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    MappedResponseRefData
        Bond indicative response data from the server. It returns a generic container of data contaning a combined dataset of all available instrument types, with only dedicated data filled out. For more information check 'Results' model documentation.

    Examples
    --------
    >>> # Request bond indic with sync post
    >>> response = request_bond_indic_sync(input=[IdentifierInfo(identifier="999818YT")])
    >>>
    >>> # Print results
    >>> print(js.dumps(response.as_dict(), indent=4))
    {
        "meta": {
            "status": "DONE",
            "requestId": "R-60841",
            "timeStamp": "2025-09-18T04:57:18Z",
            "responseType": "BOND_INDIC",
            "resultsStatus": "ALL"
        },
        "results": [
            {
                "cusip": "999818YT8",
                "indic": {
                    "ltv": 90.0,
                    "wam": 195,
                    "figi": "BBG0033WXBV4",
                    "cusip": "999818YT8",
                    "moody": [
                        {
                            "value": "Aaa"
                        }
                    ],
                    "source": "CITI",
                    "ticker": "GNMA",
                    "country": "US",
                    "loanAge": 148,
                    "lockout": 0,
                    "putFlag": false,
                    "callFlag": false,
                    "cobsCode": "MTGE",
                    "country2": "US",
                    "country3": "USA",
                    "currency": "USD",
                    "dayCount": "30/360 eom",
                    "glicCode": "MBS",
                    "grossWAC": 4.0,
                    "ioPeriod": 0,
                    "poolCode": "NA",
                    "sinkFlag": false,
                    "cmaTicker": "N/A",
                    "datedDate": "2013-05-01",
                    "gnma2Flag": false,
                    "percentVA": 11.03,
                    "currentLTV": 27.8,
                    "extendFlag": "N",
                    "isoCountry": "US",
                    "marketType": "DOMC",
                    "percentDTI": 34.0,
                    "percentFHA": 80.91,
                    "percentInv": 0.0,
                    "percentPIH": 0.15,
                    "percentRHS": 7.91,
                    "securityID": "999818YT",
                    "serviceFee": 0.5,
                    "vPointType": "MPGNMA",
                    "adjustedLTV": 27.8,
                    "combinedLTV": 90.7,
                    "creditScore": 692,
                    "description": "30-YR GNMA-2013 PROD",
                    "esgBondFlag": false,
                    "indexRating": "AA+",
                    "issueAmount": 8597.24,
                    "lowerRating": "AA+",
                    "paymentFreq": 12,
                    "percentHARP": 0.0,
                    "percentRefi": 63.7,
                    "tierCapital": "NA",
                    "balloonMonth": 0,
                    "deliveryFlag": "N",
                    "indexCountry": "US",
                    "industryCode": "MT",
                    "issuerTicker": "GNMA",
                    "lowestRating": "AA+",
                    "maturityDate": "2041-12-01",
                    "middleRating": "AA+",
                    "modifiedDate": "2025-09-14",
                    "originalTerm": 360,
                    "parentTicker": "GNMA",
                    "percentHARP2": 0.0,
                    "percentJumbo": 0.0,
                    "securityType": "MORT",
                    "currentCoupon": 3.5,
                    "dataStateList": [
                        {
                            "state": "PR",
                            "percent": 17.15
                        },
                        {
                            "state": "TX",
                            "percent": 10.03
                        },
                        {
                            "state": "FL",
                            "percent": 5.67
                        },
                        {
                            "state": "CA",
                            "percent": 4.97
                        },
                        {
                            "state": "NY",
                            "percent": 4.77
                        },
                        {
                            "state": "OH",
                            "percent": 4.77
                        },
                        {
                            "state": "GA",
                            "percent": 4.41
                        },
                        {
                            "state": "PA",
                            "percent": 3.39
                        },
                        {
                            "state": "MI",
                            "percent": 3.07
                        },
                        {
                            "state": "NC",
                            "percent": 2.72
                        },
                        {
                            "state": "IL",
                            "percent": 2.68
                        },
                        {
                            "state": "VA",
                            "percent": 2.68
                        },
                        {
                            "state": "NJ",
                            "percent": 2.4
                        },
                        {
                            "state": "IN",
                            "percent": 2.37
                        },
                        {
                            "state": "MD",
                            "percent": 2.22
                        },
                        {
                            "state": "MO",
                            "percent": 2.11
                        },
                        {
                            "state": "AZ",
                            "percent": 1.71
                        },
                        {
                            "state": "TN",
                            "percent": 1.66
                        },
                        {
                            "state": "WA",
                            "percent": 1.48
                        },
                        {
                            "state": "AL",
                            "percent": 1.46
                        },
                        {
                            "state": "LA",
                            "percent": 1.22
                        },
                        {
                            "state": "OK",
                            "percent": 1.2
                        },
                        {
                            "state": "MN",
                            "percent": 1.19
                        },
                        {
                            "state": "SC",
                            "percent": 1.11
                        },
                        {
                            "state": "CT",
                            "percent": 1.09
                        },
                        {
                            "state": "CO",
                            "percent": 1.04
                        },
                        {
                            "state": "KY",
                            "percent": 1.04
                        },
                        {
                            "state": "WI",
                            "percent": 1.01
                        },
                        {
                            "state": "MS",
                            "percent": 0.96
                        },
                        {
                            "state": "NM",
                            "percent": 0.95
                        },
                        {
                            "state": "OR",
                            "percent": 0.9
                        },
                        {
                            "state": "AR",
                            "percent": 0.75
                        },
                        {
                            "state": "NV",
                            "percent": 0.7
                        },
                        {
                            "state": "MA",
                            "percent": 0.67
                        },
                        {
                            "state": "IA",
                            "percent": 0.61
                        },
                        {
                            "state": "KS",
                            "percent": 0.58
                        },
                        {
                            "state": "UT",
                            "percent": 0.58
                        },
                        {
                            "state": "DE",
                            "percent": 0.45
                        },
                        {
                            "state": "ID",
                            "percent": 0.4
                        },
                        {
                            "state": "NE",
                            "percent": 0.38
                        },
                        {
                            "state": "WV",
                            "percent": 0.28
                        },
                        {
                            "state": "ME",
                            "percent": 0.19
                        },
                        {
                            "state": "HI",
                            "percent": 0.16
                        },
                        {
                            "state": "NH",
                            "percent": 0.16
                        },
                        {
                            "state": "MT",
                            "percent": 0.13
                        },
                        {
                            "state": "AK",
                            "percent": 0.12
                        },
                        {
                            "state": "RI",
                            "percent": 0.12
                        },
                        {
                            "state": "WY",
                            "percent": 0.08
                        },
                        {
                            "state": "SD",
                            "percent": 0.07
                        },
                        {
                            "state": "VT",
                            "percent": 0.06
                        },
                        {
                            "state": "DC",
                            "percent": 0.04
                        },
                        {
                            "state": "ND",
                            "percent": 0.04
                        }
                    ],
                    "delinquencies": {
                        "del30Days": {
                            "percent": 2.78
                        },
                        "del60Days": {
                            "percent": 0.65
                        },
                        "del90Days": {
                            "percent": 0.2
                        },
                        "del90PlusDays": {
                            "percent": 0.59
                        },
                        "del120PlusDays": {
                            "percent": 0.39
                        }
                    },
                    "greenBondFlag": false,
                    "highestRating": "AAA",
                    "incomeCountry": "US",
                    "issuerCountry": "US",
                    "percentSecond": 0.0,
                    "poolAgeMethod": "Calculated",
                    "prepayEffDate": "2025-08-01",
                    "seniorityType": "NA",
                    "assetClassCode": "CO",
                    "cgmiSectorCode": "MTGE",
                    "cleanPayMonths": 0,
                    "collateralType": "GNMA",
                    "fullPledgeFlag": false,
                    "gpmPercentStep": 0.0,
                    "incomeCountry3": "USA",
                    "instrumentType": "NA",
                    "issuerCountry2": "US",
                    "issuerCountry3": "USA",
                    "lowestRatingNF": "AA+",
                    "poolIssuerName": "NA",
                    "vPointCategory": "RP",
                    "amortizedFHALTV": 62.6,
                    "bloombergTicker": "GNSF 3.5 2013",
                    "industrySubCode": "MT",
                    "originationDate": "2013-05-01",
                    "originationYear": 2013,
                    "percent2To4Unit": 2.7,
                    "percentHAMPMods": 0.9,
                    "percentPurchase": 31.9,
                    "percentStateHFA": 0.4,
                    "poolOriginalWAM": 0,
                    "preliminaryFlag": false,
                    "redemptionValue": 100.0,
                    "securitySubType": "MPGNMA",
                    "dataQuartileList": [
                        {
                            "ltvlow": 17.0,
                            "ltvhigh": 87.0,
                            "loanSizeLow": 22000.0,
                            "loanSizeHigh": 101000.0,
                            "percentDTILow": 10.0,
                            "creditScoreLow": 300.0,
                            "percentDTIHigh": 24.5,
                            "creditScoreHigh": 655.0,
                            "originalLoanAgeLow": 0,
                            "originationYearLow": 20101101,
                            "originalLoanAgeHigh": 0,
                            "originationYearHigh": 20130401
                        },
                        {
                            "ltvlow": 87.0,
                            "ltvhigh": 93.0,
                            "loanSizeLow": 101000.0,
                            "loanSizeHigh": 132000.0,
                            "percentDTILow": 24.5,
                            "creditScoreLow": 655.0,
                            "percentDTIHigh": 34.7,
                            "creditScoreHigh": 691.0,
                            "originalLoanAgeLow": 0,
                            "originationYearLow": 20130401,
                            "originalLoanAgeHigh": 0,
                            "originationYearHigh": 20130501
                        },
                        {
                            "ltvlow": 93.0,
                            "ltvhigh": 97.0,
                            "loanSizeLow": 132000.0,
                            "loanSizeHigh": 183000.0,
                            "percentDTILow": 34.7,
                            "creditScoreLow": 691.0,
                            "percentDTIHigh": 43.6,
                            "creditScoreHigh": 739.0,
                            "originalLoanAgeLow": 0,
                            "originationYearLow": 20130501,
                            "originalLoanAgeHigh": 1,
                            "originationYearHigh": 20130701
                        },
                        {
                            "ltvlow": 97.0,
                            "ltvhigh": 118.0,
                            "loanSizeLow": 183000.0,
                            "loanSizeHigh": 743000.0,
                            "percentDTILow": 43.6,
                            "creditScoreLow": 739.0,
                            "percentDTIHigh": 65.0,
                            "creditScoreHigh": 832.0,
                            "originalLoanAgeLow": 1,
                            "originationYearLow": 20130701,
                            "originalLoanAgeHigh": 43,
                            "originationYearHigh": 20141101
                        }
                    ],
                    "gpmNumberOfSteps": 0,
                    "percentHARPOwner": 0.0,
                    "percentPrincipal": 100.0,
                    "securityCalcType": "GNMA",
                    "assetClassSubCode": "MBS",
                    "forbearanceAmount": 0.0,
                    "modifiedTimeStamp": "2025-09-15T03:34:00Z",
                    "outstandingAmount": 1070.28,
                    "parentDescription": "NA",
                    "poolIsBalloonFlag": false,
                    "prepaymentOptions": {
                        "prepayType": [
                            "CPR",
                            "PSA",
                            "VEC"
                        ]
                    },
                    "reperformerMonths": 1,
                    "dataPPMHistoryList": [
                        {
                            "prepayType": "PSA",
                            "dataPPMHistoryDetailList": [
                                {
                                    "month": "1",
                                    "prepayRate": 115.6992
                                },
                                {
                                    "month": "3",
                                    "prepayRate": 107.3431
                                },
                                {
                                    "month": "6",
                                    "prepayRate": 104.1902
                                },
                                {
                                    "month": "12",
                                    "prepayRate": 101.8431
                                },
                                {
                                    "month": "24",
                                    "prepayRate": 0.0
                                }
                            ]
                        },
                        {
                            "prepayType": "CPR",
                            "dataPPMHistoryDetailList": [
                                {
                                    "month": "1",
                                    "prepayRate": 6.9419
                                },
                                {
                                    "month": "3",
                                    "prepayRate": 6.4406
                                },
                                {
                                    "month": "6",
                                    "prepayRate": 6.2514
                                },
                                {
                                    "month": "12",
                                    "prepayRate": 6.1106
                                },
                                {
                                    "month": "24",
                                    "prepayRate": 0.0
                                }
                            ]
                        }
                    ],
                    "daysToFirstPayment": 44,
                    "issuerLowestRating": "NA",
                    "issuerMiddleRating": "NA",
                    "newCurrentLoanSize": 101518.0,
                    "originationChannel": {
                        "broker": 4.67,
                        "retail": 61.93,
                        "unknown": 0.0,
                        "unspecified": 0.0,
                        "correspondence": 33.39
                    },
                    "percentMultiFamily": 2.7,
                    "percentRefiCashout": 5.8,
                    "percentRegularMods": 3.6,
                    "percentReperformer": 0.5,
                    "relocationLoanFlag": false,
                    "socialDensityScore": 0.0,
                    "umbsfhlgPercentage": 0.0,
                    "umbsfnmaPercentage": 0.0,
                    "industryDescription": "Mortgage",
                    "issuerHighestRating": "NA",
                    "newOriginalLoanSize": 182051.0,
                    "socialCriteriaShare": 0.0,
                    "spreadAtOrigination": 23.0,
                    "weightedAvgLoanSize": 101518.0,
                    "poolOriginalLoanSize": 182051.0,
                    "cgmiSectorDescription": "Mortgage",
                    "cleanPayAverageMonths": 0,
                    "expModelAvailableFlag": true,
                    "fhfaImpliedCurrentLTV": 27.8,
                    "percentRefiNonCashout": 57.9,
                    "prepayPenaltySchedule": "0.000",
                    "defaultHorizonPYMethod": "OAS Change",
                    "industrySubDescription": "Mortgage Asset Backed",
                    "actualPrepayHistoryList": {
                        "date": "2025-11-01",
                        "genericValue": 0.8934
                    },
                    "adjustedCurrentLoanSize": 101518.0,
                    "forbearanceModification": 0.0,
                    "percentTwoPlusBorrowers": 43.9,
                    "poolAvgOriginalLoanTerm": 0,
                    "adjustedOriginalLoanSize": 182040.0,
                    "assetClassSubDescription": "Collateralized Asset Backed - Mortgage",
                    "mortgageInsurancePremium": {
                        "annual": {
                            "va": 0.0,
                            "fha": 0.797,
                            "pih": 0.0,
                            "rhs": 0.399
                        },
                        "upfront": {
                            "va": 0.5,
                            "fha": 0.694,
                            "pih": 1.0,
                            "rhs": 1.996
                        }
                    },
                    "percentReperformerAndMod": 0.1,
                    "reperformerMonthsForMods": 2,
                    "originalLoanSizeRemaining": 150986.0,
                    "percentFirstTimeHomeBuyer": 20.9,
                    "current3rdPartyOrigination": 38.06,
                    "adjustedSpreadAtOrigination": 23.0,
                    "dataPrepayModelServicerList": [
                        {
                            "percent": 23.86,
                            "servicer": "FREE"
                        },
                        {
                            "percent": 11.4,
                            "servicer": "NSTAR"
                        },
                        {
                            "percent": 11.15,
                            "servicer": "BCPOP"
                        },
                        {
                            "percent": 7.22,
                            "servicer": "QUICK"
                        },
                        {
                            "percent": 7.14,
                            "servicer": "PENNY"
                        },
                        {
                            "percent": 6.48,
                            "servicer": "LAKEV"
                        },
                        {
                            "percent": 6.37,
                            "servicer": "CARRG"
                        },
                        {
                            "percent": 5.5,
                            "servicer": "USB"
                        },
                        {
                            "percent": 3.65,
                            "servicer": "WELLS"
                        },
                        {
                            "percent": 2.41,
                            "servicer": "PNC"
                        },
                        {
                            "percent": 1.34,
                            "servicer": "MNTBK"
                        },
                        {
                            "percent": 1.15,
                            "servicer": "NWRES"
                        },
                        {
                            "percent": 0.95,
                            "servicer": "FIFTH"
                        },
                        {
                            "percent": 0.75,
                            "servicer": "DEPOT"
                        },
                        {
                            "percent": 0.6,
                            "servicer": "BOKF"
                        },
                        {
                            "percent": 0.5,
                            "servicer": "JPM"
                        },
                        {
                            "percent": 0.47,
                            "servicer": "TRUIS"
                        },
                        {
                            "percent": 0.43,
                            "servicer": "CITI"
                        },
                        {
                            "percent": 0.39,
                            "servicer": "GUILD"
                        },
                        {
                            "percent": 0.21,
                            "servicer": "REGNS"
                        },
                        {
                            "percent": 0.2,
                            "servicer": "CNTRL"
                        },
                        {
                            "percent": 0.09,
                            "servicer": "COLNL"
                        },
                        {
                            "percent": 0.06,
                            "servicer": "HFAGY"
                        },
                        {
                            "percent": 0.06,
                            "servicer": "MNSRC"
                        }
                    ],
                    "nonWeightedOriginalLoanSize": 0.0,
                    "original3rdPartyOrigination": 0.0,
                    "percentHARPDec2010Extension": 0.0,
                    "percentHARPOneYearExtension": 0.0,
                    "percentDownPaymentAssistance": 5.6,
                    "percentAmortizedFHALTVUnder78": 95.4,
                    "loanPerformanceImpliedCurrentLTV": 44.2,
                    "reperformerMonthsForReperformers": 28
                },
                "ticker": "GNMA",
                "country": "US",
                "currency": "USD",
                "identifier": "999818YT",
                "description": "30-YR GNMA-2013 PROD",
                "issuerTicker": "GNMA",
                "maturityDate": "2041-12-01",
                "securityType": "MORT",
                "currentCoupon": 3.5,
                "securitySubType": "MPGNMA"
            }
        ]
    }


    >>> # Request bond indic with sync post
    >>> response = request_bond_indic_sync(input=[IdentifierInfo(identifier="999818YT",
    >>>                                                          id_type="CUSIP",
    >>>                                                          )])
    >>>
    >>> # Print results
    >>> print(js.dumps(response.as_dict(), indent=4))
    {
        "meta": {
            "status": "DONE",
            "requestId": "R-60842",
            "timeStamp": "2025-09-18T04:57:18Z",
            "responseType": "BOND_INDIC",
            "resultsStatus": "ALL"
        },
        "results": [
            {
                "cusip": "999818YT8",
                "indic": {
                    "ltv": 90.0,
                    "wam": 195,
                    "figi": "BBG0033WXBV4",
                    "cusip": "999818YT8",
                    "moody": [
                        {
                            "value": "Aaa"
                        }
                    ],
                    "source": "CITI",
                    "ticker": "GNMA",
                    "country": "US",
                    "loanAge": 148,
                    "lockout": 0,
                    "putFlag": false,
                    "callFlag": false,
                    "cobsCode": "MTGE",
                    "country2": "US",
                    "country3": "USA",
                    "currency": "USD",
                    "dayCount": "30/360 eom",
                    "glicCode": "MBS",
                    "grossWAC": 4.0,
                    "ioPeriod": 0,
                    "poolCode": "NA",
                    "sinkFlag": false,
                    "cmaTicker": "N/A",
                    "datedDate": "2013-05-01",
                    "gnma2Flag": false,
                    "percentVA": 11.03,
                    "currentLTV": 27.8,
                    "extendFlag": "N",
                    "isoCountry": "US",
                    "marketType": "DOMC",
                    "percentDTI": 34.0,
                    "percentFHA": 80.91,
                    "percentInv": 0.0,
                    "percentPIH": 0.15,
                    "percentRHS": 7.91,
                    "securityID": "999818YT",
                    "serviceFee": 0.5,
                    "vPointType": "MPGNMA",
                    "adjustedLTV": 27.8,
                    "combinedLTV": 90.7,
                    "creditScore": 692,
                    "description": "30-YR GNMA-2013 PROD",
                    "esgBondFlag": false,
                    "indexRating": "AA+",
                    "issueAmount": 8597.24,
                    "lowerRating": "AA+",
                    "paymentFreq": 12,
                    "percentHARP": 0.0,
                    "percentRefi": 63.7,
                    "tierCapital": "NA",
                    "balloonMonth": 0,
                    "deliveryFlag": "N",
                    "indexCountry": "US",
                    "industryCode": "MT",
                    "issuerTicker": "GNMA",
                    "lowestRating": "AA+",
                    "maturityDate": "2041-12-01",
                    "middleRating": "AA+",
                    "modifiedDate": "2025-09-14",
                    "originalTerm": 360,
                    "parentTicker": "GNMA",
                    "percentHARP2": 0.0,
                    "percentJumbo": 0.0,
                    "securityType": "MORT",
                    "currentCoupon": 3.5,
                    "dataStateList": [
                        {
                            "state": "PR",
                            "percent": 17.15
                        },
                        {
                            "state": "TX",
                            "percent": 10.03
                        },
                        {
                            "state": "FL",
                            "percent": 5.67
                        },
                        {
                            "state": "CA",
                            "percent": 4.97
                        },
                        {
                            "state": "NY",
                            "percent": 4.77
                        },
                        {
                            "state": "OH",
                            "percent": 4.77
                        },
                        {
                            "state": "GA",
                            "percent": 4.41
                        },
                        {
                            "state": "PA",
                            "percent": 3.39
                        },
                        {
                            "state": "MI",
                            "percent": 3.07
                        },
                        {
                            "state": "NC",
                            "percent": 2.72
                        },
                        {
                            "state": "IL",
                            "percent": 2.68
                        },
                        {
                            "state": "VA",
                            "percent": 2.68
                        },
                        {
                            "state": "NJ",
                            "percent": 2.4
                        },
                        {
                            "state": "IN",
                            "percent": 2.37
                        },
                        {
                            "state": "MD",
                            "percent": 2.22
                        },
                        {
                            "state": "MO",
                            "percent": 2.11
                        },
                        {
                            "state": "AZ",
                            "percent": 1.71
                        },
                        {
                            "state": "TN",
                            "percent": 1.66
                        },
                        {
                            "state": "WA",
                            "percent": 1.48
                        },
                        {
                            "state": "AL",
                            "percent": 1.46
                        },
                        {
                            "state": "LA",
                            "percent": 1.22
                        },
                        {
                            "state": "OK",
                            "percent": 1.2
                        },
                        {
                            "state": "MN",
                            "percent": 1.19
                        },
                        {
                            "state": "SC",
                            "percent": 1.11
                        },
                        {
                            "state": "CT",
                            "percent": 1.09
                        },
                        {
                            "state": "CO",
                            "percent": 1.04
                        },
                        {
                            "state": "KY",
                            "percent": 1.04
                        },
                        {
                            "state": "WI",
                            "percent": 1.01
                        },
                        {
                            "state": "MS",
                            "percent": 0.96
                        },
                        {
                            "state": "NM",
                            "percent": 0.95
                        },
                        {
                            "state": "OR",
                            "percent": 0.9
                        },
                        {
                            "state": "AR",
                            "percent": 0.75
                        },
                        {
                            "state": "NV",
                            "percent": 0.7
                        },
                        {
                            "state": "MA",
                            "percent": 0.67
                        },
                        {
                            "state": "IA",
                            "percent": 0.61
                        },
                        {
                            "state": "KS",
                            "percent": 0.58
                        },
                        {
                            "state": "UT",
                            "percent": 0.58
                        },
                        {
                            "state": "DE",
                            "percent": 0.45
                        },
                        {
                            "state": "ID",
                            "percent": 0.4
                        },
                        {
                            "state": "NE",
                            "percent": 0.38
                        },
                        {
                            "state": "WV",
                            "percent": 0.28
                        },
                        {
                            "state": "ME",
                            "percent": 0.19
                        },
                        {
                            "state": "HI",
                            "percent": 0.16
                        },
                        {
                            "state": "NH",
                            "percent": 0.16
                        },
                        {
                            "state": "MT",
                            "percent": 0.13
                        },
                        {
                            "state": "AK",
                            "percent": 0.12
                        },
                        {
                            "state": "RI",
                            "percent": 0.12
                        },
                        {
                            "state": "WY",
                            "percent": 0.08
                        },
                        {
                            "state": "SD",
                            "percent": 0.07
                        },
                        {
                            "state": "VT",
                            "percent": 0.06
                        },
                        {
                            "state": "DC",
                            "percent": 0.04
                        },
                        {
                            "state": "ND",
                            "percent": 0.04
                        }
                    ],
                    "delinquencies": {
                        "del30Days": {
                            "percent": 2.78
                        },
                        "del60Days": {
                            "percent": 0.65
                        },
                        "del90Days": {
                            "percent": 0.2
                        },
                        "del90PlusDays": {
                            "percent": 0.59
                        },
                        "del120PlusDays": {
                            "percent": 0.39
                        }
                    },
                    "greenBondFlag": false,
                    "highestRating": "AAA",
                    "incomeCountry": "US",
                    "issuerCountry": "US",
                    "percentSecond": 0.0,
                    "poolAgeMethod": "Calculated",
                    "prepayEffDate": "2025-08-01",
                    "seniorityType": "NA",
                    "assetClassCode": "CO",
                    "cgmiSectorCode": "MTGE",
                    "cleanPayMonths": 0,
                    "collateralType": "GNMA",
                    "fullPledgeFlag": false,
                    "gpmPercentStep": 0.0,
                    "incomeCountry3": "USA",
                    "instrumentType": "NA",
                    "issuerCountry2": "US",
                    "issuerCountry3": "USA",
                    "lowestRatingNF": "AA+",
                    "poolIssuerName": "NA",
                    "vPointCategory": "RP",
                    "amortizedFHALTV": 62.6,
                    "bloombergTicker": "GNSF 3.5 2013",
                    "industrySubCode": "MT",
                    "originationDate": "2013-05-01",
                    "originationYear": 2013,
                    "percent2To4Unit": 2.7,
                    "percentHAMPMods": 0.9,
                    "percentPurchase": 31.9,
                    "percentStateHFA": 0.4,
                    "poolOriginalWAM": 0,
                    "preliminaryFlag": false,
                    "redemptionValue": 100.0,
                    "securitySubType": "MPGNMA",
                    "dataQuartileList": [
                        {
                            "ltvlow": 17.0,
                            "ltvhigh": 87.0,
                            "loanSizeLow": 22000.0,
                            "loanSizeHigh": 101000.0,
                            "percentDTILow": 10.0,
                            "creditScoreLow": 300.0,
                            "percentDTIHigh": 24.5,
                            "creditScoreHigh": 655.0,
                            "originalLoanAgeLow": 0,
                            "originationYearLow": 20101101,
                            "originalLoanAgeHigh": 0,
                            "originationYearHigh": 20130401
                        },
                        {
                            "ltvlow": 87.0,
                            "ltvhigh": 93.0,
                            "loanSizeLow": 101000.0,
                            "loanSizeHigh": 132000.0,
                            "percentDTILow": 24.5,
                            "creditScoreLow": 655.0,
                            "percentDTIHigh": 34.7,
                            "creditScoreHigh": 691.0,
                            "originalLoanAgeLow": 0,
                            "originationYearLow": 20130401,
                            "originalLoanAgeHigh": 0,
                            "originationYearHigh": 20130501
                        },
                        {
                            "ltvlow": 93.0,
                            "ltvhigh": 97.0,
                            "loanSizeLow": 132000.0,
                            "loanSizeHigh": 183000.0,
                            "percentDTILow": 34.7,
                            "creditScoreLow": 691.0,
                            "percentDTIHigh": 43.6,
                            "creditScoreHigh": 739.0,
                            "originalLoanAgeLow": 0,
                            "originationYearLow": 20130501,
                            "originalLoanAgeHigh": 1,
                            "originationYearHigh": 20130701
                        },
                        {
                            "ltvlow": 97.0,
                            "ltvhigh": 118.0,
                            "loanSizeLow": 183000.0,
                            "loanSizeHigh": 743000.0,
                            "percentDTILow": 43.6,
                            "creditScoreLow": 739.0,
                            "percentDTIHigh": 65.0,
                            "creditScoreHigh": 832.0,
                            "originalLoanAgeLow": 1,
                            "originationYearLow": 20130701,
                            "originalLoanAgeHigh": 43,
                            "originationYearHigh": 20141101
                        }
                    ],
                    "gpmNumberOfSteps": 0,
                    "percentHARPOwner": 0.0,
                    "percentPrincipal": 100.0,
                    "securityCalcType": "GNMA",
                    "assetClassSubCode": "MBS",
                    "forbearanceAmount": 0.0,
                    "modifiedTimeStamp": "2025-09-15T03:34:00Z",
                    "outstandingAmount": 1070.28,
                    "parentDescription": "NA",
                    "poolIsBalloonFlag": false,
                    "prepaymentOptions": {
                        "prepayType": [
                            "CPR",
                            "PSA",
                            "VEC"
                        ]
                    },
                    "reperformerMonths": 1,
                    "dataPPMHistoryList": [
                        {
                            "prepayType": "PSA",
                            "dataPPMHistoryDetailList": [
                                {
                                    "month": "1",
                                    "prepayRate": 115.6992
                                },
                                {
                                    "month": "3",
                                    "prepayRate": 107.3431
                                },
                                {
                                    "month": "6",
                                    "prepayRate": 104.1902
                                },
                                {
                                    "month": "12",
                                    "prepayRate": 101.8431
                                },
                                {
                                    "month": "24",
                                    "prepayRate": 0.0
                                }
                            ]
                        },
                        {
                            "prepayType": "CPR",
                            "dataPPMHistoryDetailList": [
                                {
                                    "month": "1",
                                    "prepayRate": 6.9419
                                },
                                {
                                    "month": "3",
                                    "prepayRate": 6.4406
                                },
                                {
                                    "month": "6",
                                    "prepayRate": 6.2514
                                },
                                {
                                    "month": "12",
                                    "prepayRate": 6.1106
                                },
                                {
                                    "month": "24",
                                    "prepayRate": 0.0
                                }
                            ]
                        }
                    ],
                    "daysToFirstPayment": 44,
                    "issuerLowestRating": "NA",
                    "issuerMiddleRating": "NA",
                    "newCurrentLoanSize": 101518.0,
                    "originationChannel": {
                        "broker": 4.67,
                        "retail": 61.93,
                        "unknown": 0.0,
                        "unspecified": 0.0,
                        "correspondence": 33.39
                    },
                    "percentMultiFamily": 2.7,
                    "percentRefiCashout": 5.8,
                    "percentRegularMods": 3.6,
                    "percentReperformer": 0.5,
                    "relocationLoanFlag": false,
                    "socialDensityScore": 0.0,
                    "umbsfhlgPercentage": 0.0,
                    "umbsfnmaPercentage": 0.0,
                    "industryDescription": "Mortgage",
                    "issuerHighestRating": "NA",
                    "newOriginalLoanSize": 182051.0,
                    "socialCriteriaShare": 0.0,
                    "spreadAtOrigination": 23.0,
                    "weightedAvgLoanSize": 101518.0,
                    "poolOriginalLoanSize": 182051.0,
                    "cgmiSectorDescription": "Mortgage",
                    "cleanPayAverageMonths": 0,
                    "expModelAvailableFlag": true,
                    "fhfaImpliedCurrentLTV": 27.8,
                    "percentRefiNonCashout": 57.9,
                    "prepayPenaltySchedule": "0.000",
                    "defaultHorizonPYMethod": "OAS Change",
                    "industrySubDescription": "Mortgage Asset Backed",
                    "actualPrepayHistoryList": {
                        "date": "2025-11-01",
                        "genericValue": 0.8934
                    },
                    "adjustedCurrentLoanSize": 101518.0,
                    "forbearanceModification": 0.0,
                    "percentTwoPlusBorrowers": 43.9,
                    "poolAvgOriginalLoanTerm": 0,
                    "adjustedOriginalLoanSize": 182040.0,
                    "assetClassSubDescription": "Collateralized Asset Backed - Mortgage",
                    "mortgageInsurancePremium": {
                        "annual": {
                            "va": 0.0,
                            "fha": 0.797,
                            "pih": 0.0,
                            "rhs": 0.399
                        },
                        "upfront": {
                            "va": 0.5,
                            "fha": 0.694,
                            "pih": 1.0,
                            "rhs": 1.996
                        }
                    },
                    "percentReperformerAndMod": 0.1,
                    "reperformerMonthsForMods": 2,
                    "originalLoanSizeRemaining": 150986.0,
                    "percentFirstTimeHomeBuyer": 20.9,
                    "current3rdPartyOrigination": 38.06,
                    "adjustedSpreadAtOrigination": 23.0,
                    "dataPrepayModelServicerList": [
                        {
                            "percent": 23.86,
                            "servicer": "FREE"
                        },
                        {
                            "percent": 11.4,
                            "servicer": "NSTAR"
                        },
                        {
                            "percent": 11.15,
                            "servicer": "BCPOP"
                        },
                        {
                            "percent": 7.22,
                            "servicer": "QUICK"
                        },
                        {
                            "percent": 7.14,
                            "servicer": "PENNY"
                        },
                        {
                            "percent": 6.48,
                            "servicer": "LAKEV"
                        },
                        {
                            "percent": 6.37,
                            "servicer": "CARRG"
                        },
                        {
                            "percent": 5.5,
                            "servicer": "USB"
                        },
                        {
                            "percent": 3.65,
                            "servicer": "WELLS"
                        },
                        {
                            "percent": 2.41,
                            "servicer": "PNC"
                        },
                        {
                            "percent": 1.34,
                            "servicer": "MNTBK"
                        },
                        {
                            "percent": 1.15,
                            "servicer": "NWRES"
                        },
                        {
                            "percent": 0.95,
                            "servicer": "FIFTH"
                        },
                        {
                            "percent": 0.75,
                            "servicer": "DEPOT"
                        },
                        {
                            "percent": 0.6,
                            "servicer": "BOKF"
                        },
                        {
                            "percent": 0.5,
                            "servicer": "JPM"
                        },
                        {
                            "percent": 0.47,
                            "servicer": "TRUIS"
                        },
                        {
                            "percent": 0.43,
                            "servicer": "CITI"
                        },
                        {
                            "percent": 0.39,
                            "servicer": "GUILD"
                        },
                        {
                            "percent": 0.21,
                            "servicer": "REGNS"
                        },
                        {
                            "percent": 0.2,
                            "servicer": "CNTRL"
                        },
                        {
                            "percent": 0.09,
                            "servicer": "COLNL"
                        },
                        {
                            "percent": 0.06,
                            "servicer": "HFAGY"
                        },
                        {
                            "percent": 0.06,
                            "servicer": "MNSRC"
                        }
                    ],
                    "nonWeightedOriginalLoanSize": 0.0,
                    "original3rdPartyOrigination": 0.0,
                    "percentHARPDec2010Extension": 0.0,
                    "percentHARPOneYearExtension": 0.0,
                    "percentDownPaymentAssistance": 5.6,
                    "percentAmortizedFHALTVUnder78": 95.4,
                    "loanPerformanceImpliedCurrentLTV": 44.2,
                    "reperformerMonthsForReperformers": 28
                },
                "ticker": "GNMA",
                "country": "US",
                "currency": "USD",
                "identifier": "999818YT",
                "description": "30-YR GNMA-2013 PROD",
                "issuerTicker": "GNMA",
                "maturityDate": "2041-12-01",
                "securityType": "MORT",
                "currentCoupon": 3.5,
                "securitySubType": "MPGNMA"
            }
        ]
    }

    """

    try:
        logger.info("Calling request_bond_indic_sync")

        response = Client().yield_book_rest.request_bond_indic_sync(
            body=BondIndicRequest(input=input, keywords=keywords),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_bond_indic_sync")

        return output
    except Exception as err:
        logger.error("Error request_bond_indic_sync.")
        check_exception_and_raise(err, logger)


def request_bond_indic_sync_get(
    *,
    id: str,
    id_type: Optional[Union[str, IdTypeEnum]] = None,
    keywords: Optional[List[str]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Synchronous Get method to retrieve the contractual information about the reference data of an instrument, which will typically not need any further calculations. Retrieve instrument reference data given an instrument ID and optionaly an ID type as input parameters to obtain basic contractual information in the Record structure with information such as security type, sector,  maturity, credit ratings, coupon, and specific information based on security type like current pool factor if the requested identifier is a mortgage.

    Parameters
    ----------
    id : str
        A sequence of textual characters.
    id_type : Union[str, IdTypeEnum], optional

    keywords : List[str], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------
    >>> # Request bond indic with sync get
    >>> response = request_bond_indic_sync_get(id="999818YT")
    >>>
    >>> # Print results in json format
    >>> print(js.dumps(response, indent=4))
    {
        "data": {
            "cusip": "999818YT8",
            "indic": {
                "ltv": 90.0,
                "wam": 195,
                "figi": "BBG0033WXBV4",
                "cusip": "999818YT8",
                "moody": [
                    {
                        "value": "Aaa"
                    }
                ],
                "source": "CITI",
                "ticker": "GNMA",
                "country": "US",
                "loanAge": 148,
                "lockout": 0,
                "putFlag": false,
                "callFlag": false,
                "cobsCode": "MTGE",
                "country2": "US",
                "country3": "USA",
                "currency": "USD",
                "dayCount": "30/360 eom",
                "glicCode": "MBS",
                "grossWAC": 4.0,
                "ioPeriod": 0,
                "poolCode": "NA",
                "sinkFlag": false,
                "cmaTicker": "N/A",
                "datedDate": "2013-05-01",
                "gnma2Flag": false,
                "percentVA": 11.03,
                "currentLTV": 27.8,
                "extendFlag": "N",
                "isoCountry": "US",
                "marketType": "DOMC",
                "percentDTI": 34.0,
                "percentFHA": 80.91,
                "percentInv": 0.0,
                "percentPIH": 0.15,
                "percentRHS": 7.91,
                "securityID": "999818YT",
                "serviceFee": 0.5,
                "vPointType": "MPGNMA",
                "adjustedLTV": 27.8,
                "combinedLTV": 90.7,
                "creditScore": 692,
                "description": "30-YR GNMA-2013 PROD",
                "esgBondFlag": false,
                "indexRating": "AA+",
                "issueAmount": 8597.24,
                "lowerRating": "AA+",
                "paymentFreq": 12,
                "percentHARP": 0.0,
                "percentRefi": 63.7,
                "tierCapital": "NA",
                "balloonMonth": 0,
                "deliveryFlag": "N",
                "indexCountry": "US",
                "industryCode": "MT",
                "issuerTicker": "GNMA",
                "lowestRating": "AA+",
                "maturityDate": "2041-12-01",
                "middleRating": "AA+",
                "modifiedDate": "2025-09-14",
                "originalTerm": 360,
                "parentTicker": "GNMA",
                "percentHARP2": 0.0,
                "percentJumbo": 0.0,
                "securityType": "MORT",
                "currentCoupon": 3.5,
                "dataStateList": [
                    {
                        "state": "PR",
                        "percent": 17.15
                    },
                    {
                        "state": "TX",
                        "percent": 10.03
                    },
                    {
                        "state": "FL",
                        "percent": 5.67
                    },
                    {
                        "state": "CA",
                        "percent": 4.97
                    },
                    {
                        "state": "NY",
                        "percent": 4.77
                    },
                    {
                        "state": "OH",
                        "percent": 4.77
                    },
                    {
                        "state": "GA",
                        "percent": 4.41
                    },
                    {
                        "state": "PA",
                        "percent": 3.39
                    },
                    {
                        "state": "MI",
                        "percent": 3.07
                    },
                    {
                        "state": "NC",
                        "percent": 2.72
                    },
                    {
                        "state": "IL",
                        "percent": 2.68
                    },
                    {
                        "state": "VA",
                        "percent": 2.68
                    },
                    {
                        "state": "NJ",
                        "percent": 2.4
                    },
                    {
                        "state": "IN",
                        "percent": 2.37
                    },
                    {
                        "state": "MD",
                        "percent": 2.22
                    },
                    {
                        "state": "MO",
                        "percent": 2.11
                    },
                    {
                        "state": "AZ",
                        "percent": 1.71
                    },
                    {
                        "state": "TN",
                        "percent": 1.66
                    },
                    {
                        "state": "WA",
                        "percent": 1.48
                    },
                    {
                        "state": "AL",
                        "percent": 1.46
                    },
                    {
                        "state": "LA",
                        "percent": 1.22
                    },
                    {
                        "state": "OK",
                        "percent": 1.2
                    },
                    {
                        "state": "MN",
                        "percent": 1.19
                    },
                    {
                        "state": "SC",
                        "percent": 1.11
                    },
                    {
                        "state": "CT",
                        "percent": 1.09
                    },
                    {
                        "state": "CO",
                        "percent": 1.04
                    },
                    {
                        "state": "KY",
                        "percent": 1.04
                    },
                    {
                        "state": "WI",
                        "percent": 1.01
                    },
                    {
                        "state": "MS",
                        "percent": 0.96
                    },
                    {
                        "state": "NM",
                        "percent": 0.95
                    },
                    {
                        "state": "OR",
                        "percent": 0.9
                    },
                    {
                        "state": "AR",
                        "percent": 0.75
                    },
                    {
                        "state": "NV",
                        "percent": 0.7
                    },
                    {
                        "state": "MA",
                        "percent": 0.67
                    },
                    {
                        "state": "IA",
                        "percent": 0.61
                    },
                    {
                        "state": "KS",
                        "percent": 0.58
                    },
                    {
                        "state": "UT",
                        "percent": 0.58
                    },
                    {
                        "state": "DE",
                        "percent": 0.45
                    },
                    {
                        "state": "ID",
                        "percent": 0.4
                    },
                    {
                        "state": "NE",
                        "percent": 0.38
                    },
                    {
                        "state": "WV",
                        "percent": 0.28
                    },
                    {
                        "state": "ME",
                        "percent": 0.19
                    },
                    {
                        "state": "HI",
                        "percent": 0.16
                    },
                    {
                        "state": "NH",
                        "percent": 0.16
                    },
                    {
                        "state": "MT",
                        "percent": 0.13
                    },
                    {
                        "state": "AK",
                        "percent": 0.12
                    },
                    {
                        "state": "RI",
                        "percent": 0.12
                    },
                    {
                        "state": "WY",
                        "percent": 0.08
                    },
                    {
                        "state": "SD",
                        "percent": 0.07
                    },
                    {
                        "state": "VT",
                        "percent": 0.06
                    },
                    {
                        "state": "DC",
                        "percent": 0.04
                    },
                    {
                        "state": "ND",
                        "percent": 0.04
                    }
                ],
                "delinquencies": {
                    "del30Days": {
                        "percent": 2.78
                    },
                    "del60Days": {
                        "percent": 0.65
                    },
                    "del90Days": {
                        "percent": 0.2
                    },
                    "del90PlusDays": {
                        "percent": 0.59
                    },
                    "del120PlusDays": {
                        "percent": 0.39
                    }
                },
                "greenBondFlag": false,
                "highestRating": "AAA",
                "incomeCountry": "US",
                "issuerCountry": "US",
                "percentSecond": 0.0,
                "poolAgeMethod": "Calculated",
                "prepayEffDate": "2025-08-01",
                "seniorityType": "NA",
                "assetClassCode": "CO",
                "cgmiSectorCode": "MTGE",
                "cleanPayMonths": 0,
                "collateralType": "GNMA",
                "fullPledgeFlag": false,
                "gpmPercentStep": 0.0,
                "incomeCountry3": "USA",
                "instrumentType": "NA",
                "issuerCountry2": "US",
                "issuerCountry3": "USA",
                "lowestRatingNF": "AA+",
                "poolIssuerName": "NA",
                "vPointCategory": "RP",
                "amortizedFHALTV": 62.6,
                "bloombergTicker": "GNSF 3.5 2013",
                "industrySubCode": "MT",
                "originationDate": "2013-05-01",
                "originationYear": 2013,
                "percent2To4Unit": 2.7,
                "percentHAMPMods": 0.9,
                "percentPurchase": 31.9,
                "percentStateHFA": 0.4,
                "poolOriginalWAM": 0,
                "preliminaryFlag": false,
                "redemptionValue": 100.0,
                "securitySubType": "MPGNMA",
                "dataQuartileList": [
                    {
                        "ltvlow": 17.0,
                        "ltvhigh": 87.0,
                        "loanSizeLow": 22000.0,
                        "loanSizeHigh": 101000.0,
                        "percentDTILow": 10.0,
                        "creditScoreLow": 300.0,
                        "percentDTIHigh": 24.5,
                        "creditScoreHigh": 655.0,
                        "originalLoanAgeLow": 0,
                        "originationYearLow": 20101101,
                        "originalLoanAgeHigh": 0,
                        "originationYearHigh": 20130401
                    },
                    {
                        "ltvlow": 87.0,
                        "ltvhigh": 93.0,
                        "loanSizeLow": 101000.0,
                        "loanSizeHigh": 132000.0,
                        "percentDTILow": 24.5,
                        "creditScoreLow": 655.0,
                        "percentDTIHigh": 34.7,
                        "creditScoreHigh": 691.0,
                        "originalLoanAgeLow": 0,
                        "originationYearLow": 20130401,
                        "originalLoanAgeHigh": 0,
                        "originationYearHigh": 20130501
                    },
                    {
                        "ltvlow": 93.0,
                        "ltvhigh": 97.0,
                        "loanSizeLow": 132000.0,
                        "loanSizeHigh": 183000.0,
                        "percentDTILow": 34.7,
                        "creditScoreLow": 691.0,
                        "percentDTIHigh": 43.6,
                        "creditScoreHigh": 739.0,
                        "originalLoanAgeLow": 0,
                        "originationYearLow": 20130501,
                        "originalLoanAgeHigh": 1,
                        "originationYearHigh": 20130701
                    },
                    {
                        "ltvlow": 97.0,
                        "ltvhigh": 118.0,
                        "loanSizeLow": 183000.0,
                        "loanSizeHigh": 743000.0,
                        "percentDTILow": 43.6,
                        "creditScoreLow": 739.0,
                        "percentDTIHigh": 65.0,
                        "creditScoreHigh": 832.0,
                        "originalLoanAgeLow": 1,
                        "originationYearLow": 20130701,
                        "originalLoanAgeHigh": 43,
                        "originationYearHigh": 20141101
                    }
                ],
                "gpmNumberOfSteps": 0,
                "percentHARPOwner": 0.0,
                "percentPrincipal": 100.0,
                "securityCalcType": "GNMA",
                "assetClassSubCode": "MBS",
                "forbearanceAmount": 0.0,
                "modifiedTimeStamp": "2025-09-15T03:34:00Z",
                "outstandingAmount": 1070.28,
                "parentDescription": "NA",
                "poolIsBalloonFlag": false,
                "prepaymentOptions": {
                    "prepayType": [
                        "CPR",
                        "PSA",
                        "VEC"
                    ]
                },
                "reperformerMonths": 1,
                "dataPPMHistoryList": [
                    {
                        "prepayType": "PSA",
                        "dataPPMHistoryDetailList": [
                            {
                                "month": "1",
                                "prepayRate": 115.6992
                            },
                            {
                                "month": "3",
                                "prepayRate": 107.3431
                            },
                            {
                                "month": "6",
                                "prepayRate": 104.1902
                            },
                            {
                                "month": "12",
                                "prepayRate": 101.8431
                            },
                            {
                                "month": "24",
                                "prepayRate": 0.0
                            }
                        ]
                    },
                    {
                        "prepayType": "CPR",
                        "dataPPMHistoryDetailList": [
                            {
                                "month": "1",
                                "prepayRate": 6.9419
                            },
                            {
                                "month": "3",
                                "prepayRate": 6.4406
                            },
                            {
                                "month": "6",
                                "prepayRate": 6.2514
                            },
                            {
                                "month": "12",
                                "prepayRate": 6.1106
                            },
                            {
                                "month": "24",
                                "prepayRate": 0.0
                            }
                        ]
                    }
                ],
                "daysToFirstPayment": 44,
                "issuerLowestRating": "NA",
                "issuerMiddleRating": "NA",
                "newCurrentLoanSize": 101518.0,
                "originationChannel": {
                    "broker": 4.67,
                    "retail": 61.93,
                    "unknown": 0.0,
                    "unspecified": 0.0,
                    "correspondence": 33.39
                },
                "percentMultiFamily": 2.7,
                "percentRefiCashout": 5.8,
                "percentRegularMods": 3.6,
                "percentReperformer": 0.5,
                "relocationLoanFlag": false,
                "socialDensityScore": 0.0,
                "umbsfhlgPercentage": 0.0,
                "umbsfnmaPercentage": 0.0,
                "industryDescription": "Mortgage",
                "issuerHighestRating": "NA",
                "newOriginalLoanSize": 182051.0,
                "socialCriteriaShare": 0.0,
                "spreadAtOrigination": 23.0,
                "weightedAvgLoanSize": 101518.0,
                "poolOriginalLoanSize": 182051.0,
                "cgmiSectorDescription": "Mortgage",
                "cleanPayAverageMonths": 0,
                "expModelAvailableFlag": true,
                "fhfaImpliedCurrentLTV": 27.8,
                "percentRefiNonCashout": 57.9,
                "prepayPenaltySchedule": "0.000",
                "defaultHorizonPYMethod": "OAS Change",
                "industrySubDescription": "Mortgage Asset Backed",
                "actualPrepayHistoryList": {
                    "date": "2025-11-01",
                    "genericValue": 0.8934
                },
                "adjustedCurrentLoanSize": 101518.0,
                "forbearanceModification": 0.0,
                "percentTwoPlusBorrowers": 43.9,
                "poolAvgOriginalLoanTerm": 0,
                "adjustedOriginalLoanSize": 182040.0,
                "assetClassSubDescription": "Collateralized Asset Backed - Mortgage",
                "mortgageInsurancePremium": {
                    "annual": {
                        "va": 0.0,
                        "fha": 0.797,
                        "pih": 0.0,
                        "rhs": 0.399
                    },
                    "upfront": {
                        "va": 0.5,
                        "fha": 0.694,
                        "pih": 1.0,
                        "rhs": 1.996
                    }
                },
                "percentReperformerAndMod": 0.1,
                "reperformerMonthsForMods": 2,
                "originalLoanSizeRemaining": 150986.0,
                "percentFirstTimeHomeBuyer": 20.9,
                "current3rdPartyOrigination": 38.06,
                "adjustedSpreadAtOrigination": 23.0,
                "dataPrepayModelServicerList": [
                    {
                        "percent": 23.86,
                        "servicer": "FREE"
                    },
                    {
                        "percent": 11.4,
                        "servicer": "NSTAR"
                    },
                    {
                        "percent": 11.15,
                        "servicer": "BCPOP"
                    },
                    {
                        "percent": 7.22,
                        "servicer": "QUICK"
                    },
                    {
                        "percent": 7.14,
                        "servicer": "PENNY"
                    },
                    {
                        "percent": 6.48,
                        "servicer": "LAKEV"
                    },
                    {
                        "percent": 6.37,
                        "servicer": "CARRG"
                    },
                    {
                        "percent": 5.5,
                        "servicer": "USB"
                    },
                    {
                        "percent": 3.65,
                        "servicer": "WELLS"
                    },
                    {
                        "percent": 2.41,
                        "servicer": "PNC"
                    },
                    {
                        "percent": 1.34,
                        "servicer": "MNTBK"
                    },
                    {
                        "percent": 1.15,
                        "servicer": "NWRES"
                    },
                    {
                        "percent": 0.95,
                        "servicer": "FIFTH"
                    },
                    {
                        "percent": 0.75,
                        "servicer": "DEPOT"
                    },
                    {
                        "percent": 0.6,
                        "servicer": "BOKF"
                    },
                    {
                        "percent": 0.5,
                        "servicer": "JPM"
                    },
                    {
                        "percent": 0.47,
                        "servicer": "TRUIS"
                    },
                    {
                        "percent": 0.43,
                        "servicer": "CITI"
                    },
                    {
                        "percent": 0.39,
                        "servicer": "GUILD"
                    },
                    {
                        "percent": 0.21,
                        "servicer": "REGNS"
                    },
                    {
                        "percent": 0.2,
                        "servicer": "CNTRL"
                    },
                    {
                        "percent": 0.09,
                        "servicer": "COLNL"
                    },
                    {
                        "percent": 0.06,
                        "servicer": "HFAGY"
                    },
                    {
                        "percent": 0.06,
                        "servicer": "MNSRC"
                    }
                ],
                "nonWeightedOriginalLoanSize": 0.0,
                "original3rdPartyOrigination": 0.0,
                "percentHARPDec2010Extension": 0.0,
                "percentHARPOneYearExtension": 0.0,
                "percentDownPaymentAssistance": 5.6,
                "percentAmortizedFHALTVUnder78": 95.4,
                "loanPerformanceImpliedCurrentLTV": 44.2,
                "reperformerMonthsForReperformers": 28
            },
            "ticker": "GNMA",
            "country": "US",
            "currency": "USD",
            "identifier": "999818YT",
            "description": "30-YR GNMA-2013 PROD",
            "issuerTicker": "GNMA",
            "maturityDate": "2041-12-01",
            "securityType": "MORT",
            "currentCoupon": 3.5,
            "securitySubType": "MPGNMA"
        },
        "meta": {
            "status": "DONE",
            "requestId": "R-60839",
            "timeStamp": "2025-09-18T04:57:16Z",
            "responseType": "BOND_INDIC"
        }
    }


    >>> # Request bond indic with sync get
    >>> response = request_bond_indic_sync_get(
    >>>                                     id="01F002628",
    >>>                                     id_type=IdTypeEnum.CUSIP,
    >>>                                     keywords=["keyword1", "keyword2"],
    >>>                                     job="JobName",
    >>>                                     name="Name",
    >>>                                     pri=0,
    >>>                                     tags=["tag1", "tag2"]
    >>>                                     )
    >>>
    >>> # Print results in json format
    >>> print(js.dumps(response, indent=4))
    {
        "data": {
            "cusip": "01F002628",
            "indic": {},
            "ticker": "FNMA",
            "country": "US",
            "currency": "USD",
            "identifier": "01F00262",
            "description": "30-YR UMBS-TBA PROD FEB",
            "issuerTicker": "UMBS",
            "maturityDate": "2054-01-01",
            "securityType": "MORT",
            "currentCoupon": 0.5,
            "securitySubType": "FNTBA"
        },
        "meta": {
            "status": "DONE",
            "requestId": "R-60840",
            "timeStamp": "2025-09-18T04:57:17Z",
            "responseType": "BOND_INDIC"
        }
    }

    """

    try:
        logger.info("Calling request_bond_indic_sync_get")

        response = Client().yield_book_rest.request_bond_indic_sync_get(
            id=id,
            id_type=id_type,
            keywords=keywords,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_bond_indic_sync_get")

        return output
    except Exception as err:
        logger.error("Error request_bond_indic_sync_get.")
        check_exception_and_raise(err, logger)


def request_collateral_details_async(
    *,
    input: Optional[List[CollateralDetailsRequestInfo]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """


    Parameters
    ----------
    input : List[CollateralDetailsRequestInfo], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling request_collateral_details_async")

        response = Client().yield_book_rest.request_collateral_details_async(
            body=CollateralDetailsRequest(input=input),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_collateral_details_async")

        return output
    except Exception as err:
        logger.error("Error request_collateral_details_async.")
        check_exception_and_raise(err, logger)


def request_collateral_details_async_get(
    *,
    id: str,
    id_type: Optional[str] = None,
    user_tag: Optional[str] = None,
    data_items: Optional[List[Union[str, DataItems]]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """


    Parameters
    ----------
    id : str
        Security reference ID.
    id_type : str, optional
        A sequence of textual characters.
    user_tag : str, optional
        A sequence of textual characters.
    data_items : List[Union[str, DataItems]], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling request_collateral_details_async_get")

        response = Client().yield_book_rest.request_collateral_details_async_get(
            id=id,
            id_type=id_type,
            user_tag=user_tag,
            data_items=data_items,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_collateral_details_async_get")

        return output
    except Exception as err:
        logger.error("Error request_collateral_details_async_get.")
        check_exception_and_raise(err, logger)


def request_collateral_details_sync(
    *,
    input: Optional[List[CollateralDetailsRequestInfo]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """


    Parameters
    ----------
    input : List[CollateralDetailsRequestInfo], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling request_collateral_details_sync")

        response = Client().yield_book_rest.request_collateral_details_sync(
            body=CollateralDetailsRequest(input=input),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_collateral_details_sync")

        return output
    except Exception as err:
        logger.error("Error request_collateral_details_sync.")
        check_exception_and_raise(err, logger)


def request_collateral_details_sync_get(
    *,
    id: str,
    id_type: Optional[str] = None,
    user_tag: Optional[str] = None,
    data_items: Optional[List[Union[str, DataItems]]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """


    Parameters
    ----------
    id : str
        Security reference ID.
    id_type : str, optional
        A sequence of textual characters.
    user_tag : str, optional
        A sequence of textual characters.
    data_items : List[Union[str, DataItems]], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling request_collateral_details_sync_get")

        response = Client().yield_book_rest.request_collateral_details_sync_get(
            id=id,
            id_type=id_type,
            user_tag=user_tag,
            data_items=data_items,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_collateral_details_sync_get")

        return output
    except Exception as err:
        logger.error("Error request_collateral_details_sync_get.")
        check_exception_and_raise(err, logger)


def request_curve_async(
    *,
    date: Union[str, datetime.date],
    currency: str,
    curve_type: Union[str, YbRestCurveType],
    cds_ticker: Optional[str] = None,
    expand_curve: Optional[bool] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Request curve async.

    Parameters
    ----------
    date : Union[str, datetime.date]
        A date on a calendar without a time zone, e.g. "April 10th"
    currency : str
        A sequence of textual characters.
    curve_type : Union[str, YbRestCurveType]

    cds_ticker : str, optional
        A sequence of textual characters.
    expand_curve : bool, optional
        Boolean with `true` and `false` values.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling request_curve_async")

        response = Client().yield_book_rest.request_curve_async(
            date=date,
            currency=currency,
            curve_type=curve_type,
            cds_ticker=cds_ticker,
            expand_curve=expand_curve,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_curve_async")

        return output
    except Exception as err:
        logger.error("Error request_curve_async.")
        check_exception_and_raise(err, logger)


def request_curve_sync(
    *,
    date: Union[str, datetime.date],
    currency: str,
    curve_type: Union[str, YbRestCurveType],
    cds_ticker: Optional[str] = None,
    expand_curve: Optional[bool] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Request curve sync.

    Parameters
    ----------
    date : Union[str, datetime.date]
        A date on a calendar without a time zone, e.g. "April 10th"
    currency : str
        A sequence of textual characters.
    curve_type : Union[str, YbRestCurveType]

    cds_ticker : str, optional
        A sequence of textual characters.
    expand_curve : bool, optional
        Boolean with `true` and `false` values.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling request_curve_sync")

        response = Client().yield_book_rest.request_curve_sync(
            date=date,
            currency=currency,
            curve_type=curve_type,
            cds_ticker=cds_ticker,
            expand_curve=expand_curve,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_curve_sync")

        return output
    except Exception as err:
        logger.error("Error request_curve_sync.")
        check_exception_and_raise(err, logger)


def request_curves_async(
    *,
    curves: Optional[List[CurveSearch]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Request curves async.

    Parameters
    ----------
    curves : List[CurveSearch], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling request_curves_async")

        response = Client().yield_book_rest.request_curves_async(
            body=CurveDetailsRequest(curves=curves),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
            content_type="application/json",
        )

        output = response
        logger.info("Called request_curves_async")

        return output
    except Exception as err:
        logger.error("Error request_curves_async.")
        check_exception_and_raise(err, logger)


def request_curves_sync(
    *,
    curves: Optional[List[CurveSearch]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Request curves sync.

    Parameters
    ----------
    curves : List[CurveSearch], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling request_curves_sync")

        response = Client().yield_book_rest.request_curves_sync(
            body=CurveDetailsRequest(curves=curves),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
            content_type="application/json",
        )

        output = response
        logger.info("Called request_curves_sync")

        return output
    except Exception as err:
        logger.error("Error request_curves_sync.")
        check_exception_and_raise(err, logger)


def request_get_scen_calc_sys_scen_async(
    *,
    id: str,
    level: str,
    pricing_date: str,
    curve_type: Union[str, YbRestCurveType],
    h_py_method: str,
    scenario: str,
    id_type: Optional[str] = None,
    h_days: Optional[int] = None,
    h_months: Optional[int] = None,
    currency: Optional[str] = None,
    volatility: Optional[str] = None,
    prepay_type: Optional[str] = None,
    prepay_rate: Optional[float] = None,
    h_level: Optional[str] = None,
    h_prepay_rate: Optional[float] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Request get scenario calculation system scenario async.

    Parameters
    ----------
    id : str
        Security reference ID.
    id_type : str, optional
        A sequence of textual characters.
    level : str
        A sequence of textual characters.
    pricing_date : str
        A sequence of textual characters.
    h_days : int, optional
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    h_months : int, optional
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    curve_type : Union[str, YbRestCurveType]

    currency : str, optional
        A sequence of textual characters.
    volatility : str, optional
        A sequence of textual characters.
    prepay_type : str, optional
        A sequence of textual characters.
    prepay_rate : float, optional
        A 64 bit floating point number. (`±5.0 × 10^−324` to `±1.7 × 10^308`)
    h_level : str, optional
        A sequence of textual characters.
    h_py_method : str
        A sequence of textual characters.
    h_prepay_rate : float, optional
        A 64 bit floating point number. (`±5.0 × 10^−324` to `±1.7 × 10^308`)
    scenario : str
        A sequence of textual characters.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------
    >>> # Formulate and execute the get request by using instrument ID, Par_amount and job in which the calculation will be done
    >>> sa_async_get_response = request_get_scen_calc_sys_scen_async(
    >>>             id='US742718AV11',
    >>>             scenario="/sys/scenario/Par/50",
    >>>             pricing_date="2025-01-01",
    >>>             curve_type="GVT",
    >>>             h_py_method="OAS",
    >>>             level="100"
    >>>         )
    >>>
    >>> async_get_results_response = {}
    >>>
    >>> attempt = 1
    >>>
    >>> while attempt < 10:
    >>>
    >>>     from lseg_analytics.exceptions import ServerError
    >>>     try:
    >>>         time.sleep(10)
    >>>         # Request bond indic with async post
    >>>         async_get_results_response = get_result(request_id_parameter=sa_async_get_response.request_id)
    >>>         break
    >>>     except Exception as err:
    >>>         print(f"Attempt " + str(
    >>>             attempt) + " resulted in error retrieving results from:" + sa_async_get_response.request_id)
    >>>         if (isinstance(err, ServerError)
    >>>                 and f"The result is not ready yet for requestID:{sa_async_get_response.request_id}" in str(err)):
    >>>
    >>>             attempt += 1
    >>>         else:
    >>>             raise err
    >>>
    >>> print(js.dumps(async_get_results_response, indent=4))
    {
        "data": {
            "isin": "US742718AV11",
            "cusip": "742718AV1",
            "ticker": "PG",
            "scenario": {
                "horizon": [
                    {
                        "oas": 361.951,
                        "wal": 4.8139,
                        "price": 98.053324,
                        "yield": 8.4961,
                        "balance": 1.0,
                        "duration": 3.8584,
                        "fullPrice": 99.542213,
                        "returnCode": 0,
                        "scenarioID": "/sys/scenario/Par/50",
                        "spreadDV01": 0.0,
                        "volatility": 16.0,
                        "actualPrice": 98.053,
                        "grossSpread": 361.3423,
                        "horizonDays": 0,
                        "marketValue": 99.542213,
                        "optionValue": 0.0,
                        "totalReturn": -1.91811763,
                        "dollarReturn": -1.94667627,
                        "convexityCost": 0.0,
                        "nominalSpread": 361.3423,
                        "effectiveYield": 0.0,
                        "interestReturn": 0.0,
                        "settlementDate": "2025-01-03",
                        "spreadDuration": 0.0,
                        "accruedInterest": 1.488889,
                        "actualFullPrice": 99.542,
                        "horizonPYMethod": "OAS",
                        "interestPayment": 0.0,
                        "principalReturn": -1.91811763,
                        "underlyingPrice": 0.0,
                        "principalPayment": 0.0,
                        "reinvestmentRate": 4.829956,
                        "yieldCurveMargin": 361.951,
                        "effectiveCallDate": "0",
                        "reinvestmentAmount": 0.0,
                        "actualAccruedInterest": 1.489
                    }
                ],
                "settlement": {
                    "oas": 361.951,
                    "psa": 0.0,
                    "wal": 4.8139,
                    "price": 100.0,
                    "yield": 7.9953,
                    "fullPrice": 101.488889,
                    "volatility": 13.0,
                    "grossSpread": 361.2649,
                    "optionValue": 0.0,
                    "pricingDate": "2024-12-31",
                    "forwardYield": 0.0,
                    "staticSpread": 0.0,
                    "effectiveDV01": 0.039405887,
                    "nominalSpread": 0.0,
                    "settlementDate": "2025-01-03",
                    "accruedInterest": 1.488889,
                    "reinvestmentRate": 4.329956,
                    "yieldCurveMargin": 0.0,
                    "effectiveDuration": 3.8828,
                    "effectiveConvexity": 0.1873
                }
            },
            "returnCode": 0,
            "securityID": "742718AV",
            "description": "PROCTER & GAMBLE CO",
            "maturityDate": "2029-10-26",
            "securityType": "BOND",
            "currentCoupon": 8.0
        },
        "meta": {
            "status": "DONE",
            "requestId": "R-21319",
            "timeStamp": "2025-08-19T02:16:32Z",
            "responseType": "SCENARIO_CALC"
        }
    }

    """

    try:
        logger.info("Calling request_get_scen_calc_sys_scen_async")

        response = Client().yield_book_rest.request_get_scen_calc_sys_scen_async(
            id=id,
            id_type=id_type,
            level=level,
            pricing_date=pricing_date,
            h_days=h_days,
            h_months=h_months,
            curve_type=curve_type,
            currency=currency,
            volatility=volatility,
            prepay_type=prepay_type,
            prepay_rate=prepay_rate,
            h_level=h_level,
            h_py_method=h_py_method,
            h_prepay_rate=h_prepay_rate,
            scenario=scenario,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_get_scen_calc_sys_scen_async")

        return output
    except Exception as err:
        logger.error("Error request_get_scen_calc_sys_scen_async.")
        check_exception_and_raise(err, logger)


def request_get_scen_calc_sys_scen_sync(
    *,
    id: str,
    level: str,
    pricing_date: str,
    curve_type: Union[str, YbRestCurveType],
    h_py_method: str,
    scenario: str,
    id_type: Optional[str] = None,
    h_days: Optional[int] = None,
    h_months: Optional[int] = None,
    currency: Optional[str] = None,
    volatility: Optional[str] = None,
    prepay_type: Optional[str] = None,
    prepay_rate: Optional[float] = None,
    h_level: Optional[str] = None,
    h_prepay_rate: Optional[float] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Request get scenario calculation system scenario sync.

    Parameters
    ----------
    id : str
        Security reference ID.
    id_type : str, optional
        A sequence of textual characters.
    level : str
        A sequence of textual characters.
    pricing_date : str
        A sequence of textual characters.
    h_days : int, optional
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    h_months : int, optional
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    curve_type : Union[str, YbRestCurveType]

    currency : str, optional
        A sequence of textual characters.
    volatility : str, optional
        A sequence of textual characters.
    prepay_type : str, optional
        A sequence of textual characters.
    prepay_rate : float, optional
        A 64 bit floating point number. (`±5.0 × 10^−324` to `±1.7 × 10^308`)
    h_level : str, optional
        A sequence of textual characters.
    h_py_method : str
        A sequence of textual characters.
    h_prepay_rate : float, optional
        A 64 bit floating point number. (`±5.0 × 10^−324` to `±1.7 × 10^308`)
    scenario : str
        A sequence of textual characters.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------
    >>> sa_sync_get_response = request_get_scen_calc_sys_scen_sync(
    >>>             id='US742718AV11',
    >>>             level="100",
    >>>             scenario="/sys/scenario/Par/50",
    >>>             curve_type="GVT",
    >>>             pricing_date="2025-01-01",
    >>>             h_py_method="OAS",
    >>>         )
    >>>
    >>> print(js.dumps(sa_sync_get_response, indent=4))
    {
        "data": {
            "isin": "US742718AV11",
            "cusip": "742718AV1",
            "ticker": "PG",
            "scenario": {
                "horizon": [
                    {
                        "oas": 361.951,
                        "wal": 4.8139,
                        "price": 98.053324,
                        "yield": 8.4961,
                        "balance": 1.0,
                        "duration": 3.8584,
                        "fullPrice": 99.542213,
                        "returnCode": 0,
                        "scenarioID": "/sys/scenario/Par/50",
                        "spreadDV01": 0.0,
                        "volatility": 16.0,
                        "actualPrice": 98.053,
                        "grossSpread": 361.3423,
                        "horizonDays": 0,
                        "marketValue": 99.542213,
                        "optionValue": 0.0,
                        "totalReturn": -1.91811763,
                        "dollarReturn": -1.94667627,
                        "convexityCost": 0.0,
                        "nominalSpread": 361.3423,
                        "effectiveYield": 0.0,
                        "interestReturn": 0.0,
                        "settlementDate": "2025-01-03",
                        "spreadDuration": 0.0,
                        "accruedInterest": 1.488889,
                        "actualFullPrice": 99.542,
                        "horizonPYMethod": "OAS",
                        "interestPayment": 0.0,
                        "principalReturn": -1.91811763,
                        "underlyingPrice": 0.0,
                        "principalPayment": 0.0,
                        "reinvestmentRate": 4.829956,
                        "yieldCurveMargin": 361.951,
                        "effectiveCallDate": "0",
                        "reinvestmentAmount": 0.0,
                        "actualAccruedInterest": 1.489
                    }
                ],
                "settlement": {
                    "oas": 361.951,
                    "psa": 0.0,
                    "wal": 4.8139,
                    "price": 100.0,
                    "yield": 7.9953,
                    "fullPrice": 101.488889,
                    "volatility": 13.0,
                    "grossSpread": 361.2649,
                    "optionValue": 0.0,
                    "pricingDate": "2024-12-31",
                    "forwardYield": 0.0,
                    "staticSpread": 0.0,
                    "effectiveDV01": 0.039405887,
                    "nominalSpread": 0.0,
                    "settlementDate": "2025-01-03",
                    "accruedInterest": 1.488889,
                    "reinvestmentRate": 4.329956,
                    "yieldCurveMargin": 0.0,
                    "effectiveDuration": 3.8828,
                    "effectiveConvexity": 0.1873
                }
            },
            "returnCode": 0,
            "securityID": "742718AV",
            "description": "PROCTER & GAMBLE CO",
            "maturityDate": "2029-10-26",
            "securityType": "BOND",
            "currentCoupon": 8.0
        },
        "meta": {
            "status": "DONE",
            "requestId": "R-60847",
            "timeStamp": "2025-09-18T04:57:26Z",
            "responseType": "SCENARIO_CALC"
        }
    }

    """

    try:
        logger.info("Calling request_get_scen_calc_sys_scen_sync")

        response = Client().yield_book_rest.request_get_scen_calc_sys_scen_sync(
            id=id,
            id_type=id_type,
            level=level,
            pricing_date=pricing_date,
            h_days=h_days,
            h_months=h_months,
            curve_type=curve_type,
            currency=currency,
            volatility=volatility,
            prepay_type=prepay_type,
            prepay_rate=prepay_rate,
            h_level=h_level,
            h_py_method=h_py_method,
            h_prepay_rate=h_prepay_rate,
            scenario=scenario,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_get_scen_calc_sys_scen_sync")

        return output
    except Exception as err:
        logger.error("Error request_get_scen_calc_sys_scen_sync.")
        check_exception_and_raise(err, logger)


def request_historical_data_async(
    *,
    id: str,
    id_type: Optional[str] = None,
    keyword: Optional[List[str]] = None,
    start_date: Optional[Union[str, datetime.date]] = None,
    end_date: Optional[Union[str, datetime.date]] = None,
    frequency: Optional[Union[str, YbRestFrequency]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Request Historical Data async by Security reference ID.

    Parameters
    ----------
    id : str
        Security reference ID.
    id_type : str, optional
        A sequence of textual characters.
    keyword : List[str], optional

    start_date : Union[str, datetime.date], optional
        A date on a calendar without a time zone, e.g. "April 10th"
    end_date : Union[str, datetime.date], optional
        A date on a calendar without a time zone, e.g. "April 10th"
    frequency : Union[str, YbRestFrequency], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling request_historical_data_async")

        response = Client().yield_book_rest.request_historical_data_async(
            id=id,
            id_type=id_type,
            keyword=keyword,
            start_date=start_date,
            end_date=end_date,
            frequency=frequency,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_historical_data_async")

        return output
    except Exception as err:
        logger.error("Error request_historical_data_async.")
        check_exception_and_raise(err, logger)


def request_historical_data_sync(
    *,
    id: str,
    id_type: Optional[str] = None,
    keyword: Optional[List[str]] = None,
    start_date: Optional[Union[str, datetime.date]] = None,
    end_date: Optional[Union[str, datetime.date]] = None,
    frequency: Optional[Union[str, YbRestFrequency]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Request Historical Data sync by Security reference ID.

    Parameters
    ----------
    id : str
        Security reference ID.
    id_type : str, optional
        A sequence of textual characters.
    keyword : List[str], optional

    start_date : Union[str, datetime.date], optional
        A date on a calendar without a time zone, e.g. "April 10th"
    end_date : Union[str, datetime.date], optional
        A date on a calendar without a time zone, e.g. "April 10th"
    frequency : Union[str, YbRestFrequency], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling request_historical_data_sync")

        response = Client().yield_book_rest.request_historical_data_sync(
            id=id,
            id_type=id_type,
            keyword=keyword,
            start_date=start_date,
            end_date=end_date,
            frequency=frequency,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_historical_data_sync")

        return output
    except Exception as err:
        logger.error("Error request_historical_data_sync.")
        check_exception_and_raise(err, logger)


def request_index_catalogue_info_async(
    *,
    provider: str,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """


    Parameters
    ----------
    provider : str
        A sequence of textual characters.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling request_index_catalogue_info_async")

        response = Client().yield_book_rest.request_index_catalogue_info_async(
            provider=provider, job=job, name=name, pri=pri, tags=tags
        )

        output = response
        logger.info("Called request_index_catalogue_info_async")

        return output
    except Exception as err:
        logger.error("Error request_index_catalogue_info_async.")
        check_exception_and_raise(err, logger)


def request_index_catalogue_info_sync(
    *,
    provider: str,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """


    Parameters
    ----------
    provider : str
        A sequence of textual characters.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling request_index_catalogue_info_sync")

        response = Client().yield_book_rest.request_index_catalogue_info_sync(
            provider=provider, job=job, name=name, pri=pri, tags=tags
        )

        output = response
        logger.info("Called request_index_catalogue_info_sync")

        return output
    except Exception as err:
        logger.error("Error request_index_catalogue_info_sync.")
        check_exception_and_raise(err, logger)


def request_index_data_by_ticker_async(
    *,
    ticker: str,
    asof_date: Union[str, datetime.date],
    pricing_date: Optional[Union[str, datetime.date]] = None,
    base_currency: Optional[str] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """


    Parameters
    ----------
    ticker : str
        A sequence of textual characters.
    asof_date : Union[str, datetime.date]
        A date on a calendar without a time zone, e.g. "April 10th"
    pricing_date : Union[str, datetime.date], optional
        A date on a calendar without a time zone, e.g. "April 10th"
    base_currency : str, optional
        A sequence of textual characters.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling request_index_data_by_ticker_async")

        response = Client().yield_book_rest.request_index_data_by_ticker_async(
            ticker=ticker,
            asof_date=asof_date,
            pricing_date=pricing_date,
            base_currency=base_currency,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_index_data_by_ticker_async")

        return output
    except Exception as err:
        logger.error("Error request_index_data_by_ticker_async.")
        check_exception_and_raise(err, logger)


def request_index_data_by_ticker_sync(
    *,
    ticker: str,
    asof_date: Union[str, datetime.date],
    pricing_date: Optional[Union[str, datetime.date]] = None,
    base_currency: Optional[str] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """


    Parameters
    ----------
    ticker : str
        A sequence of textual characters.
    asof_date : Union[str, datetime.date]
        A date on a calendar without a time zone, e.g. "April 10th"
    pricing_date : Union[str, datetime.date], optional
        A date on a calendar without a time zone, e.g. "April 10th"
    base_currency : str, optional
        A sequence of textual characters.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling request_index_data_by_ticker_sync")

        response = Client().yield_book_rest.request_index_data_by_ticker_sync(
            ticker=ticker,
            asof_date=asof_date,
            pricing_date=pricing_date,
            base_currency=base_currency,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_index_data_by_ticker_sync")

        return output
    except Exception as err:
        logger.error("Error request_index_data_by_ticker_sync.")
        check_exception_and_raise(err, logger)


def request_index_providers_async(
    *,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """


    Parameters
    ----------
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling request_index_providers_async")

        response = Client().yield_book_rest.request_index_providers_async(job=job, name=name, pri=pri, tags=tags)

        output = response
        logger.info("Called request_index_providers_async")

        return output
    except Exception as err:
        logger.error("Error request_index_providers_async.")
        check_exception_and_raise(err, logger)


def request_index_providers_sync(
    *,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """


    Parameters
    ----------
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling request_index_providers_sync")

        response = Client().yield_book_rest.request_index_providers_sync(job=job, name=name, pri=pri, tags=tags)

        output = response
        logger.info("Called request_index_providers_sync")

        return output
    except Exception as err:
        logger.error("Error request_index_providers_sync.")
        check_exception_and_raise(err, logger)


def request_mbs_history_async(
    *,
    id: str,
    id_type: Optional[str] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """


    Parameters
    ----------
    id : str
        Security reference ID.
    id_type : str, optional
        A sequence of textual characters.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling request_mbs_history_async")

        response = Client().yield_book_rest.request_mbs_history_async(
            id=id, id_type=id_type, job=job, name=name, pri=pri, tags=tags
        )

        output = response
        logger.info("Called request_mbs_history_async")

        return output
    except Exception as err:
        logger.error("Error request_mbs_history_async.")
        check_exception_and_raise(err, logger)


def request_mbs_history_sync(
    *,
    id: str,
    id_type: Optional[str] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """


    Parameters
    ----------
    id : str
        Security reference ID.
    id_type : str, optional
        A sequence of textual characters.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling request_mbs_history_sync")

        response = Client().yield_book_rest.request_mbs_history_sync(
            id=id, id_type=id_type, job=job, name=name, pri=pri, tags=tags
        )

        output = response
        logger.info("Called request_mbs_history_sync")

        return output
    except Exception as err:
        logger.error("Error request_mbs_history_sync.")
        check_exception_and_raise(err, logger)


def request_mortgage_model_async(
    *,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """


    Parameters
    ----------
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling request_mortgage_model_async")

        response = Client().yield_book_rest.request_mortgage_model_async(job=job, name=name, pri=pri, tags=tags)

        output = response
        logger.info("Called request_mortgage_model_async")

        return output
    except Exception as err:
        logger.error("Error request_mortgage_model_async.")
        check_exception_and_raise(err, logger)


def request_mortgage_model_sync(
    *,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """


    Parameters
    ----------
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling request_mortgage_model_sync")

        response = Client().yield_book_rest.request_mortgage_model_sync(job=job, name=name, pri=pri, tags=tags)

        output = response
        logger.info("Called request_mortgage_model_sync")

        return output
    except Exception as err:
        logger.error("Error request_mortgage_model_sync.")
        check_exception_and_raise(err, logger)


def request_py_calculation_async(
    *,
    global_settings: Optional[PyCalcGlobalSettings] = None,
    input: Optional[List[PyCalcInput]] = None,
    keywords: Optional[List[str]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Request PY calculation async.

    Parameters
    ----------
    global_settings : PyCalcGlobalSettings, optional

    input : List[PyCalcInput], optional

    keywords : List[str], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------
    >>> # request_py_calculation_sync
    >>> global_settings = PyCalcGlobalSettings(
    >>>             pricing_date=date(2025, 1, 17),
    >>>         )
    >>>
    >>> input = [
    >>>             PyCalcInput(
    >>>                 identifier="29874QEL",
    >>>                 level="100",
    >>>                 curve=CurveTypeAndCurrency(
    >>>                     curve_type="GVT",
    >>>                     currency="USD"
    >>>                 )
    >>>             )
    >>>         ]
    >>>
    >>> py_async_post_response = request_py_calculation_async(
    >>>             global_settings=global_settings,
    >>>             input=input,
    >>>         )
    >>>
    >>> # provide a window of time for job to finish
    >>> time.sleep(10)
    >>>
    >>> py_async_post_result = get_result(request_id_parameter=py_async_post_response.request_id)
    >>>
    >>> print(js.dumps(py_async_post_result, indent=4))
    {
        "meta": {
            "status": "DONE",
            "requestId": "R-20906",
            "timeStamp": "2025-08-18T22:36:37Z",
            "responseType": "PY_CALC",
            "resultsStatus": "ALL"
        },
        "results": [
            {
                "py": {
                    "oas": -373.0749,
                    "wal": 0.841096,
                    "dv01": 0.00838988,
                    "isin": "US29874QEL41",
                    "cusip": "29874QEL4",
                    "price": 100.0,
                    "yield": 0.499919,
                    "ticker": "EBRD",
                    "cSpread": 7.672,
                    "cdYield": 0.493835,
                    "pyLevel": "100",
                    "zSpread": -373.074889,
                    "duration": 0.838324,
                    "recovery": 37.4,
                    "ziSpread": -374.496164,
                    "znSpread": -378.43626,
                    "assetSwap": -395.112,
                    "benchmark": "US 3.875 07/27",
                    "convexity": 0.0112,
                    "curveDate": "2025-01-17",
                    "curveType": "Govt",
                    "fullPrice": 100.07916667,
                    "securityID": "29874QEL",
                    "spreadDV01": 0.008389905,
                    "tsyCurveID": "USDp0117",
                    "volatility": 13.0,
                    "accruedDays": 57,
                    "description": "EUROPEAN BANK FOR RECON AND DEV",
                    "grossSpread": -374.4927,
                    "optionValue": 0.0,
                    "pricingDate": "2025-01-17",
                    "swapCurveID": "SUSp117Q2",
                    "currentYield": 0.5,
                    "effectiveWAL": 0.8417,
                    "maturityDate": "2025-11-25",
                    "securityType": "BOND",
                    "volModelType": "Single",
                    "yieldToWorst": 0.499919,
                    "convexityCost": 0.0,
                    "currentCoupon": 0.5,
                    "discountYield": 0.0,
                    "effectiveCV01": 0.000112198,
                    "effectiveDV01": 0.008388666,
                    "worstCallDate": "2025-11-25",
                    "cdsAdjustedOAS": -380.657,
                    "effectiveYield": 0.496,
                    "marketSettings": {
                        "settlementDate": "2025-01-22"
                    },
                    "settlementDate": "2025-01-22",
                    "spreadDuration": 0.838327,
                    "walToWorstCall": 0.841096,
                    "zSpreadToWorst": -378.436,
                    "accruedInterest": 0.07916667,
                    "annualizedYield": 0.501,
                    "assetSwapSpread": -371.247,
                    "cdsImpliedPrice": 96.879,
                    "compoundingFreq": 2,
                    "convexityEffect": 0.0,
                    "dv01ToWorstCall": 0.00839,
                    "spreadConvexity": 0.011,
                    "yearsToMaturity": 0.8411,
                    "ziWorstCallDate": "2025-11-25",
                    "znWorstCallDate": "2025-11-25",
                    "assetSwapToLibor": {
                        "type": "PAR",
                        "value": -395.1121
                    },
                    "cdsAdjustedYield": 0.424,
                    "economicExposure": 100.079167,
                    "macaulayDuration": 0.8404,
                    "spreadToActCurve": -373.3523,
                    "spreadToNextCall": -374.4927,
                    "spreadToTsyCurve": -374.5047,
                    "yearsToWorstCall": 0.842,
                    "yieldCurveMargin": -373.0749,
                    "yieldToWorstCall": 0.499919,
                    "effectiveDuration": 0.838203073,
                    "macaulayConvexity": 0.7069,
                    "spreadToBenchmark": -377.2128,
                    "spreadToSwapCurve": -400.5193,
                    "spreadToWorstCall": -374,
                    "effectiveConvexity": 0.011210883,
                    "ffndSpreadDuration": 0.0,
                    "optionModelCurveID": "USDp0117",
                    "yieldCurveDuration": 0.8382,
                    "durationToWorstCall": 0.8383,
                    "durationToWorstCase": 0.838324,
                    "indexSpreadDuration": 0.0,
                    "semiAnnualizedYield": 0.499919,
                    "ziSpreadToWorstCall": -374.496,
                    "znSpreadToWorstCall": -378.436,
                    "benchmarkToWorstCall": "US 3.875 07/27",
                    "spreadToRFRSwapCurve": -371.6566,
                    "yearsToFinalMaturity": 0.842,
                    "gnmafnmaSpreadDuration": 0.0,
                    "spreadDurationTreasury": 0.838327,
                    "fundedEffectiveDuration": 0.838203,
                    "effectiveDurationPriceUp": 99.8698,
                    "fundedEffectiveConvexity": 0.011211,
                    "effectiveDurationPriceDown": 100.289234,
                    "spreadToActCurveToWorstCall": -373.3523,
                    "currentCouponSpreadConvexity": 0.0,
                    "spreadToBenchmarkToWorstCall": -377.2128,
                    "currentCouponSpreadSensitivity": 0.0,
                    "spreadToTsyCurveAtBenchmarkTenor": -371.1762
                },
                "securityID": "29874QEL"
            }
        ]
    }

    """

    try:
        logger.info("Calling request_py_calculation_async")

        response = Client().yield_book_rest.request_py_calculation_async(
            body=PyCalcRequest(global_settings=global_settings, input=input, keywords=keywords),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
            content_type="application/json",
        )

        output = response
        logger.info("Called request_py_calculation_async")

        return output
    except Exception as err:
        logger.error("Error request_py_calculation_async.")
        check_exception_and_raise(err, logger)


def request_py_calculation_async_by_id(
    *,
    id: str,
    level: str,
    curve_type: Union[str, YbRestCurveType],
    id_type: Optional[str] = None,
    pricing_date: Optional[Union[str, datetime.date]] = None,
    currency: Optional[str] = None,
    prepay_type: Optional[str] = None,
    prepay_rate: Optional[float] = None,
    option_model: Optional[Union[str, OptionModel]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Request PY calculation async by ID.

    Parameters
    ----------
    id : str
        A sequence of textual characters.
    id_type : str, optional
        A sequence of textual characters.
    level : str
        A sequence of textual characters.
    pricing_date : Union[str, datetime.date], optional
        A date on a calendar without a time zone, e.g. "April 10th"
    curve_type : Union[str, YbRestCurveType]

    currency : str, optional
        A sequence of textual characters.
    prepay_type : str, optional
        A sequence of textual characters.
    prepay_rate : float, optional
        A 64 bit floating point number. (`±5.0 × 10^−324` to `±1.7 × 10^308`)
    option_model : Union[str, OptionModel], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------
    >>> # request_py_calculation_sync_by_id
    >>> py_async_get_response = request_py_calculation_async_by_id(
    >>>             id="01F002628",
    >>>             level="100",
    >>>             curve_type="GVT"
    >>>         )
    >>>
    >>> # provide a window of time for job to finish
    >>> time.sleep(10)
    >>>
    >>> py_async_get_result = get_result(request_id_parameter=py_async_get_response.request_id)
    >>>
    >>> print(js.dumps(py_async_get_result, indent=4))
    {
        "data": {
            "py": {
                "ltv": 67.0,
                "oas": -435.6297,
                "wal": 10.098174,
                "dv01": 0.097250231,
                "cusip": "01F002628",
                "price": 100.0,
                "yield": 0.497093,
                "ticker": "FNMA",
                "cmmType": 100,
                "pyLevel": "100",
                "zSpread": -416.336945,
                "duration": 9.723537,
                "loanSize": 290000.0,
                "modelLTV": 51.6,
                "ziSpread": -416.336945,
                "znSpread": -353.877594,
                "benchmark": "10 yr",
                "convexity": 1.4255,
                "curveDate": "2025-08-15",
                "curveType": "Govt",
                "fullPrice": 100.01527778,
                "modelCode": 2501,
                "prepayRate": 100.0,
                "prepayType": "VEC",
                "securityID": "01F00262",
                "spreadDV01": 0.100176565,
                "tsyCurveID": "USDp0815",
                "accruedDays": 11,
                "creditScore": 760,
                "description": "30-YR UMBS-TBA PROD FEB",
                "grossSpread": -383.4278,
                "pricingDate": "2025-08-15",
                "swapCurveID": "SUSp815Q2",
                "currentYield": 0.5,
                "effectiveWAL": 10.7124,
                "maturityDate": "2054-01-01",
                "securityType": "MORT",
                "volModelType": "LMMSOFRFLAT",
                "yieldToWorst": 0.497093,
                "convexityCost": 27.4846,
                "currentCoupon": 0.5,
                "effectiveCV01": 0.001154157,
                "effectiveDV01": 0.094492547,
                "modelLoanSize": 361200.0,
                "mortgageYield": 0.4966,
                "remainingTerm": 335,
                "effectiveYield": 0.0105,
                "marketSettings": {
                    "settlementDate": "2026-02-12"
                },
                "settlementDate": "2026-02-12",
                "spreadDuration": 10.016126,
                "accruedInterest": 0.01527778,
                "annualizedYield": 0.498,
                "compoundingFreq": 2,
                "convexityEffect": -27.4846,
                "dataPpmProjList": [
                    {
                        "oneYear": 40.879,
                        "longTerm": 73.5063,
                        "oneMonth": 32.433,
                        "sixMonth": 41.584,
                        "prepayType": "PSA",
                        "threeMonth": 38.005
                    },
                    {
                        "oneYear": 2.3847,
                        "longTerm": 4.3945,
                        "oneMonth": 1.693,
                        "sixMonth": 2.357,
                        "prepayType": "CPR",
                        "threeMonth": 2.052
                    },
                    {
                        "oneYear": 2.3217,
                        "longTerm": 3.7992,
                        "oneMonth": 1.665,
                        "sixMonth": 2.311,
                        "prepayType": "FwdCPR",
                        "threeMonth": 2.016
                    },
                    {
                        "oneYear": 0.0,
                        "longTerm": 0.0,
                        "oneMonth": 0.0,
                        "sixMonth": 0.0,
                        "prepayType": "FwdCDR",
                        "threeMonth": 0.0
                    },
                    {
                        "oneYear": 0.0,
                        "longTerm": 0.0,
                        "oneMonth": 0.0,
                        "sixMonth": 0.0,
                        "prepayType": "FwdVPR",
                        "threeMonth": 0.0
                    },
                    {
                        "oneYear": 0.0,
                        "longTerm": 0.0,
                        "oneMonth": 0.0,
                        "sixMonth": 0.0,
                        "prepayType": "FwdVPRTurnover",
                        "threeMonth": 0.0
                    },
                    {
                        "oneYear": 0.0,
                        "longTerm": 0.0,
                        "oneMonth": 0.0,
                        "sixMonth": 0.0,
                        "prepayType": "FwdVPRCurtail",
                        "threeMonth": 0.0
                    },
                    {
                        "oneYear": 0.0,
                        "longTerm": 0.0,
                        "oneMonth": 0.0,
                        "sixMonth": 0.0,
                        "prepayType": "FwdVPRRefi",
                        "threeMonth": 0.0
                    },
                    {
                        "oneYear": 0.0,
                        "longTerm": 0.0,
                        "oneMonth": 0.0,
                        "sixMonth": 0.0,
                        "prepayType": "FwdVPRRefiRateterm",
                        "threeMonth": 0.0
                    },
                    {
                        "oneYear": 0.0,
                        "longTerm": 0.0,
                        "oneMonth": 0.0,
                        "sixMonth": 0.0,
                        "prepayType": "FwdVPRRefiCashout",
                        "threeMonth": 0.0
                    }
                ],
                "forwardMeasures": {
                    "wal": 10.57462,
                    "yield": 0.497224,
                    "margin": -408.145
                },
                "spreadConvexity": 1.522,
                "yearsToMaturity": 27.8861,
                "economicExposure": 100.015278,
                "macaulayDuration": 9.7477,
                "modelCreditScore": 763.4,
                "spreadToActCurve": -383.4915,
                "spreadToNextCall": -442.2918,
                "spreadToTsyCurve": -383.4278,
                "yieldCurveMargin": -408.1451,
                "yieldToWorstCall": 0.497093,
                "effectiveDuration": 9.447811127,
                "spreadToBenchmark": -382.8623,
                "spreadToSwapCurve": -359.0922,
                "spreadToWorstCall": -383,
                "effectiveConvexity": 0.115398034,
                "moatsCurrentCoupon": 5.406,
                "optionModelCurveID": "USDp0815",
                "yieldCurveDuration": 9.4478,
                "durationToWorstCase": 9.723537,
                "semiAnnualizedYield": 0.497093,
                "spreadToRFRSwapCurve": -330.6714,
                "yearsToFinalMaturity": 27.886,
                "spreadDurationTreasury": 10.016126,
                "fundedEffectiveDuration": 9.447811,
                "effectiveDurationPriceUp": 97.641293,
                "fundedEffectiveConvexity": 0.115398,
                "lastPrincipalPaymentDate": "2054-01-25",
                "effectiveDurationPriceDown": 102.36592,
                "spreadToTsyCurveAtBenchmarkTenor": -382.8623
            },
            "securityID": "01F00262"
        },
        "meta": {
            "status": "DONE",
            "requestId": "R-20905",
            "timeStamp": "2025-08-18T22:35:49Z",
            "responseType": "PY_CALC"
        }
    }

    """

    try:
        logger.info("Calling request_py_calculation_async_by_id")

        response = Client().yield_book_rest.request_py_calculation_async_by_id(
            id=id,
            id_type=id_type,
            level=level,
            pricing_date=pricing_date,
            curve_type=curve_type,
            currency=currency,
            prepay_type=prepay_type,
            prepay_rate=prepay_rate,
            option_model=option_model,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_py_calculation_async_by_id")

        return output
    except Exception as err:
        logger.error("Error request_py_calculation_async_by_id.")
        check_exception_and_raise(err, logger)


def request_py_calculation_sync(
    *,
    global_settings: Optional[PyCalcGlobalSettings] = None,
    input: Optional[List[PyCalcInput]] = None,
    keywords: Optional[List[str]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Request PY calculation sync.

    Parameters
    ----------
    global_settings : PyCalcGlobalSettings, optional

    input : List[PyCalcInput], optional

    keywords : List[str], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------
    >>> # request_py_calculation_sync
    >>> global_settings = PyCalcGlobalSettings(
    >>>             pricing_date=date(2025, 1, 17),
    >>>         )
    >>>
    >>> input = [
    >>>             PyCalcInput(
    >>>                 identifier="29874QEL",
    >>>                 level="100",
    >>>                 curve=CurveTypeAndCurrency(
    >>>                     curve_type="GVT",
    >>>                     currency="USD",
    >>>                     retrieve_curve=True,
    >>>                     snapshot="EOD",
    >>>                 ),
    >>>             )
    >>>         ]
    >>>
    >>> # request_py_calculation_sync
    >>> py_sync_post_response = request_py_calculation_sync(
    >>>             global_settings=global_settings,
    >>>             input=input
    >>>         )
    >>>
    >>> print(js.dumps(py_sync_post_response, indent=4))
    {
        "meta": {
            "status": "DONE",
            "requestId": "R-60844",
            "timeStamp": "2025-09-18T04:57:22Z",
            "responseType": "PY_CALC",
            "resultsStatus": "ALL"
        },
        "extra": {
            "curves": [
                {
                    "points": [
                        {
                            "rate": 4.3116,
                            "term": 0.25
                        },
                        {
                            "rate": 4.3164,
                            "term": 0.5
                        },
                        {
                            "rate": 4.264,
                            "term": 0.75
                        },
                        {
                            "rate": 4.2117,
                            "term": 1.0
                        },
                        {
                            "rate": 4.2268,
                            "term": 1.25
                        },
                        {
                            "rate": 4.2419,
                            "term": 1.5
                        },
                        {
                            "rate": 4.257,
                            "term": 1.75
                        },
                        {
                            "rate": 4.272,
                            "term": 2.0
                        },
                        {
                            "rate": 4.2873,
                            "term": 2.25
                        },
                        {
                            "rate": 4.3025,
                            "term": 2.5
                        },
                        {
                            "rate": 4.3177,
                            "term": 2.75
                        },
                        {
                            "rate": 4.3329,
                            "term": 3.0
                        },
                        {
                            "rate": 4.3431,
                            "term": 3.25
                        },
                        {
                            "rate": 4.3533,
                            "term": 3.5
                        },
                        {
                            "rate": 4.3635,
                            "term": 3.75
                        },
                        {
                            "rate": 4.3737,
                            "term": 4.0
                        },
                        {
                            "rate": 4.3839,
                            "term": 4.25
                        },
                        {
                            "rate": 4.394,
                            "term": 4.5
                        },
                        {
                            "rate": 4.4042,
                            "term": 4.75
                        },
                        {
                            "rate": 4.4144,
                            "term": 5.0
                        },
                        {
                            "rate": 4.427,
                            "term": 5.25
                        },
                        {
                            "rate": 4.4395,
                            "term": 5.5
                        },
                        {
                            "rate": 4.4521,
                            "term": 5.75
                        },
                        {
                            "rate": 4.4646,
                            "term": 6.0
                        },
                        {
                            "rate": 4.4771,
                            "term": 6.25
                        },
                        {
                            "rate": 4.4897,
                            "term": 6.5
                        },
                        {
                            "rate": 4.5022,
                            "term": 6.75
                        },
                        {
                            "rate": 4.5148,
                            "term": 7.0
                        },
                        {
                            "rate": 4.5226,
                            "term": 7.25
                        },
                        {
                            "rate": 4.5304,
                            "term": 7.5
                        },
                        {
                            "rate": 4.5383,
                            "term": 7.75
                        },
                        {
                            "rate": 4.5461,
                            "term": 8.0
                        },
                        {
                            "rate": 4.5539,
                            "term": 8.25
                        },
                        {
                            "rate": 4.5618,
                            "term": 8.5
                        },
                        {
                            "rate": 4.5696,
                            "term": 8.75
                        },
                        {
                            "rate": 4.5774,
                            "term": 9.0
                        },
                        {
                            "rate": 4.5853,
                            "term": 9.25
                        },
                        {
                            "rate": 4.5931,
                            "term": 9.5
                        },
                        {
                            "rate": 4.6009,
                            "term": 9.75
                        },
                        {
                            "rate": 4.6087,
                            "term": 10.0
                        },
                        {
                            "rate": 4.6164,
                            "term": 10.25
                        },
                        {
                            "rate": 4.6241,
                            "term": 10.5
                        },
                        {
                            "rate": 4.6318,
                            "term": 10.75
                        },
                        {
                            "rate": 4.6395,
                            "term": 11.0
                        },
                        {
                            "rate": 4.6472,
                            "term": 11.25
                        },
                        {
                            "rate": 4.6549,
                            "term": 11.5
                        },
                        {
                            "rate": 4.6626,
                            "term": 11.75
                        },
                        {
                            "rate": 4.6703,
                            "term": 12.0
                        },
                        {
                            "rate": 4.678,
                            "term": 12.25
                        },
                        {
                            "rate": 4.6857,
                            "term": 12.5
                        },
                        {
                            "rate": 4.6934,
                            "term": 12.75
                        },
                        {
                            "rate": 4.7011,
                            "term": 13.0
                        },
                        {
                            "rate": 4.7088,
                            "term": 13.25
                        },
                        {
                            "rate": 4.7165,
                            "term": 13.5
                        },
                        {
                            "rate": 4.7242,
                            "term": 13.75
                        },
                        {
                            "rate": 4.7319,
                            "term": 14.0
                        },
                        {
                            "rate": 4.7396,
                            "term": 14.25
                        },
                        {
                            "rate": 4.7473,
                            "term": 14.5
                        },
                        {
                            "rate": 4.755,
                            "term": 14.75
                        },
                        {
                            "rate": 4.7627,
                            "term": 15.0
                        },
                        {
                            "rate": 4.7704,
                            "term": 15.25
                        },
                        {
                            "rate": 4.7781,
                            "term": 15.5
                        },
                        {
                            "rate": 4.7858,
                            "term": 15.75
                        },
                        {
                            "rate": 4.7934,
                            "term": 16.0
                        },
                        {
                            "rate": 4.8011,
                            "term": 16.25
                        },
                        {
                            "rate": 4.8088,
                            "term": 16.5
                        },
                        {
                            "rate": 4.8165,
                            "term": 16.75
                        },
                        {
                            "rate": 4.8242,
                            "term": 17.0
                        },
                        {
                            "rate": 4.8319,
                            "term": 17.25
                        },
                        {
                            "rate": 4.8396,
                            "term": 17.5
                        },
                        {
                            "rate": 4.8473,
                            "term": 17.75
                        },
                        {
                            "rate": 4.855,
                            "term": 18.0
                        },
                        {
                            "rate": 4.8627,
                            "term": 18.25
                        },
                        {
                            "rate": 4.8704,
                            "term": 18.5
                        },
                        {
                            "rate": 4.8781,
                            "term": 18.75
                        },
                        {
                            "rate": 4.8858,
                            "term": 19.0
                        },
                        {
                            "rate": 4.8935,
                            "term": 19.25
                        },
                        {
                            "rate": 4.9012,
                            "term": 19.5
                        },
                        {
                            "rate": 4.9089,
                            "term": 19.75
                        },
                        {
                            "rate": 4.9166,
                            "term": 20.0
                        },
                        {
                            "rate": 4.9148,
                            "term": 20.25
                        },
                        {
                            "rate": 4.913,
                            "term": 20.5
                        },
                        {
                            "rate": 4.9112,
                            "term": 20.75
                        },
                        {
                            "rate": 4.9094,
                            "term": 21.0
                        },
                        {
                            "rate": 4.9077,
                            "term": 21.25
                        },
                        {
                            "rate": 4.9059,
                            "term": 21.5
                        },
                        {
                            "rate": 4.9041,
                            "term": 21.75
                        },
                        {
                            "rate": 4.9023,
                            "term": 22.0
                        },
                        {
                            "rate": 4.9005,
                            "term": 22.25
                        },
                        {
                            "rate": 4.8987,
                            "term": 22.5
                        },
                        {
                            "rate": 4.897,
                            "term": 22.75
                        },
                        {
                            "rate": 4.8952,
                            "term": 23.0
                        },
                        {
                            "rate": 4.8934,
                            "term": 23.25
                        },
                        {
                            "rate": 4.8916,
                            "term": 23.5
                        },
                        {
                            "rate": 4.8898,
                            "term": 23.75
                        },
                        {
                            "rate": 4.888,
                            "term": 24.0
                        },
                        {
                            "rate": 4.8863,
                            "term": 24.25
                        },
                        {
                            "rate": 4.8845,
                            "term": 24.5
                        },
                        {
                            "rate": 4.8827,
                            "term": 24.75
                        },
                        {
                            "rate": 4.8809,
                            "term": 25.0
                        },
                        {
                            "rate": 4.8791,
                            "term": 25.25
                        },
                        {
                            "rate": 4.8773,
                            "term": 25.5
                        },
                        {
                            "rate": 4.8756,
                            "term": 25.75
                        },
                        {
                            "rate": 4.8738,
                            "term": 26.0
                        },
                        {
                            "rate": 4.872,
                            "term": 26.25
                        },
                        {
                            "rate": 4.8702,
                            "term": 26.5
                        },
                        {
                            "rate": 4.8684,
                            "term": 26.75
                        },
                        {
                            "rate": 4.8666,
                            "term": 27.0
                        },
                        {
                            "rate": 4.8649,
                            "term": 27.25
                        },
                        {
                            "rate": 4.8631,
                            "term": 27.5
                        },
                        {
                            "rate": 4.8613,
                            "term": 27.75
                        },
                        {
                            "rate": 4.8595,
                            "term": 28.0
                        },
                        {
                            "rate": 4.8577,
                            "term": 28.25
                        },
                        {
                            "rate": 4.8559,
                            "term": 28.5
                        },
                        {
                            "rate": 4.8542,
                            "term": 28.75
                        },
                        {
                            "rate": 4.8524,
                            "term": 29.0
                        },
                        {
                            "rate": 4.8506,
                            "term": 29.25
                        },
                        {
                            "rate": 4.8488,
                            "term": 29.5
                        },
                        {
                            "rate": 4.847,
                            "term": 29.75
                        },
                        {
                            "rate": 4.8452,
                            "term": 30.0
                        }
                    ],
                    "source": "SSB",
                    "curveId": "USDp0117",
                    "currency": "USD",
                    "pricingDate": "2025-01-17",
                    "curveEffDate": "2025-01-17",
                    "curveYieldFreq": 2
                }
            ]
        },
        "results": [
            {
                "py": {
                    "oas": -373.0749,
                    "wal": 0.841096,
                    "dv01": 0.00838988,
                    "isin": "US29874QEL41",
                    "cusip": "29874QEL4",
                    "price": 100.0,
                    "yield": 0.499919,
                    "ticker": "EBRD",
                    "cSpread": 7.672,
                    "cdYield": 0.493835,
                    "pyLevel": "100",
                    "zSpread": -373.074889,
                    "duration": 0.838324,
                    "recovery": 37.4,
                    "ziSpread": -374.496164,
                    "znSpread": -378.43626,
                    "assetSwap": -395.112,
                    "benchmark": "US 3.625 08/27",
                    "convexity": 0.0112,
                    "curveDate": "2025-01-17",
                    "curveType": "Govt",
                    "fullPrice": 100.07916667,
                    "securityID": "29874QEL",
                    "spreadDV01": 0.008389905,
                    "tsyCurveID": "USDp0117",
                    "volatility": 13.0,
                    "accruedDays": 57,
                    "description": "EUROPEAN BANK FOR RECON AND DEV",
                    "grossSpread": -374.4927,
                    "optionValue": 0.0,
                    "pricingDate": "2025-01-17",
                    "swapCurveID": "SUSp117Q2",
                    "currentYield": 0.5,
                    "effectiveWAL": 0.8417,
                    "maturityDate": "2025-11-25",
                    "securityType": "BOND",
                    "volModelType": "Single",
                    "yieldToWorst": 0.499919,
                    "convexityCost": 0.0,
                    "currentCoupon": 0.5,
                    "discountYield": 0.0,
                    "effectiveCV01": 0.000112198,
                    "effectiveDV01": 0.008388666,
                    "worstCallDate": "2025-11-25",
                    "cdsAdjustedOAS": -380.657,
                    "effectiveYield": 0.496,
                    "marketSettings": {
                        "settlementDate": "2025-01-22"
                    },
                    "settlementDate": "2025-01-22",
                    "spreadDuration": 0.838327,
                    "walToWorstCall": 0.841096,
                    "zSpreadToWorst": -378.436,
                    "accruedInterest": 0.07916667,
                    "annualizedYield": 0.501,
                    "assetSwapSpread": -371.247,
                    "cdsImpliedPrice": 96.879,
                    "compoundingFreq": 2,
                    "convexityEffect": 0.0,
                    "dv01ToWorstCall": 0.00839,
                    "spreadConvexity": 0.011,
                    "yearsToMaturity": 0.8411,
                    "ziWorstCallDate": "2025-11-25",
                    "znWorstCallDate": "2025-11-25",
                    "assetSwapToLibor": {
                        "type": "PAR",
                        "value": -395.1121
                    },
                    "cdsAdjustedYield": 0.424,
                    "economicExposure": 100.079167,
                    "macaulayDuration": 0.8404,
                    "spreadToActCurve": -373.3523,
                    "spreadToNextCall": -374.4927,
                    "spreadToTsyCurve": -374.5047,
                    "yearsToWorstCall": 0.842,
                    "yieldCurveMargin": -373.0749,
                    "yieldToWorstCall": 0.499919,
                    "effectiveDuration": 0.838203073,
                    "macaulayConvexity": 0.7069,
                    "spreadToBenchmark": -377.2128,
                    "spreadToSwapCurve": -400.5193,
                    "spreadToWorstCall": -374,
                    "effectiveConvexity": 0.011210883,
                    "ffndSpreadDuration": 0.0,
                    "optionModelCurveID": "USDp0117",
                    "yieldCurveDuration": 0.8382,
                    "durationToWorstCall": 0.8383,
                    "durationToWorstCase": 0.838324,
                    "indexSpreadDuration": 0.0,
                    "semiAnnualizedYield": 0.499919,
                    "ziSpreadToWorstCall": -374.496,
                    "znSpreadToWorstCall": -378.436,
                    "benchmarkToWorstCall": "US 3.625 08/27",
                    "spreadToRFRSwapCurve": -371.6566,
                    "yearsToFinalMaturity": 0.842,
                    "gnmafnmaSpreadDuration": 0.0,
                    "spreadDurationTreasury": 0.838327,
                    "fundedEffectiveDuration": 0.838203,
                    "effectiveDurationPriceUp": 99.8698,
                    "fundedEffectiveConvexity": 0.011211,
                    "effectiveDurationPriceDown": 100.289234,
                    "spreadToActCurveToWorstCall": -373.3523,
                    "currentCouponSpreadConvexity": 0.0,
                    "spreadToBenchmarkToWorstCall": -377.2128,
                    "currentCouponSpreadSensitivity": 0.0,
                    "spreadToTsyCurveAtBenchmarkTenor": -371.1762
                },
                "securityID": "29874QEL"
            }
        ]
    }

    """

    try:
        logger.info("Calling request_py_calculation_sync")

        response = Client().yield_book_rest.request_py_calculation_sync(
            body=PyCalcRequest(global_settings=global_settings, input=input, keywords=keywords),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
            content_type="application/json",
        )

        output = response
        logger.info("Called request_py_calculation_sync")

        return output
    except Exception as err:
        logger.error("Error request_py_calculation_sync.")
        check_exception_and_raise(err, logger)


def request_py_calculation_sync_by_id(
    *,
    id: str,
    level: str,
    curve_type: Union[str, YbRestCurveType],
    id_type: Optional[str] = None,
    pricing_date: Optional[Union[str, datetime.date]] = None,
    currency: Optional[str] = None,
    prepay_type: Optional[str] = None,
    prepay_rate: Optional[float] = None,
    option_model: Optional[Union[str, OptionModel]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Request PY calculation sync by ID.

    Parameters
    ----------
    id : str
        A sequence of textual characters.
    id_type : str, optional
        A sequence of textual characters.
    level : str
        A sequence of textual characters.
    pricing_date : Union[str, datetime.date], optional
        A date on a calendar without a time zone, e.g. "April 10th"
    curve_type : Union[str, YbRestCurveType]

    currency : str, optional
        A sequence of textual characters.
    prepay_type : str, optional
        A sequence of textual characters.
    prepay_rate : float, optional
        A 64 bit floating point number. (`±5.0 × 10^−324` to `±1.7 × 10^308`)
    option_model : Union[str, OptionModel], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------
    >>> # request_py_calculation_sync_by_id
    >>> py_sync_get_response = request_py_calculation_sync_by_id(
    >>>             id="912810FP",
    >>>             level="100",
    >>>             curve_type="GVT",
    >>>         )
    >>>
    >>> print(js.dumps(py_sync_get_response, indent=4))
    {
        "data": {
            "py": {
                "oas": 169.2877,
                "wal": 5.408219,
                "dv01": 0.046384446,
                "isin": "US912810FP85",
                "cusip": "912810FP8",
                "price": 100.0,
                "yield": 5.37382,
                "ticker": "US",
                "cSpread": 34.297,
                "cdYield": 5.293174,
                "pyLevel": "100",
                "zSpread": 169.287747,
                "cdsShift": 158.149,
                "duration": 4.614853,
                "recovery": 37.4,
                "ziSpread": 169.521112,
                "znSpread": 202.445505,
                "assetSwap": 174.845,
                "benchmark": "US 1.125 02/31",
                "convexity": 0.2538,
                "curveDate": "2025-09-17",
                "curveType": "Govt",
                "fullPrice": 100.51120924,
                "securityID": "912810FP",
                "spreadDV01": 0.0,
                "tsyCurveID": "USDp0917",
                "accruedDays": 35,
                "description": "US TREASURY",
                "grossSpread": 169.0009,
                "optionValue": 0.0,
                "pricingDate": "2025-09-17",
                "swapCurveID": "SUSp917Q2",
                "currentYield": 5.375,
                "effectiveWAL": 5.4056,
                "maturityDate": "2031-02-15",
                "securityType": "BOND",
                "volModelType": "MarketWSkew",
                "yieldToWorst": 5.37382,
                "convexityCost": 0.0,
                "currentCoupon": 5.375,
                "effectiveCV01": 0.002560125,
                "effectiveDV01": 0.046486836,
                "worstCallDate": "2031-02-15",
                "cdsAdjustedOAS": 134.759,
                "effectiveYield": 5.3499,
                "marketSettings": {
                    "settlementDate": "2025-09-19"
                },
                "settlementDate": "2025-09-19",
                "spreadDuration": 0.0,
                "walToWorstCall": 5.408219,
                "zSpreadToWorst": 202.446,
                "accruedInterest": 0.51120924,
                "annualizedYield": 5.446,
                "assetSwapSpread": 203.799,
                "cdsImpliedPrice": 108.322,
                "compoundingFreq": 2,
                "convexityEffect": 0.0,
                "dv01ToWorstCall": 0.046384,
                "spreadConvexity": 0.254,
                "yearsToMaturity": 5.4082,
                "ziWorstCallDate": "2031-02-15",
                "znWorstCallDate": "2031-02-15",
                "assetSwapToLibor": {
                    "type": "PAR",
                    "value": 174.8451
                },
                "cdsAdjustedYield": 5.031,
                "economicExposure": 100.511209,
                "macaulayDuration": 4.7389,
                "spreadToActCurve": 168.5152,
                "spreadToNextCall": 169.0009,
                "spreadToTsyCurve": 168.9763,
                "yearsToWorstCall": 5.406,
                "yieldCurveMargin": 169.2877,
                "yieldToWorstCall": 5.37382,
                "effectiveDuration": 4.625040054,
                "macaulayConvexity": 24.3962,
                "spreadToBenchmark": 173.5282,
                "spreadToSwapCurve": 178.8393,
                "spreadToWorstCall": 169,
                "effectiveConvexity": 0.254710436,
                "ffndSpreadDuration": 0.0,
                "optionModelCurveID": "USDp0917",
                "yieldCurveDuration": 4.625,
                "durationToWorstCall": 4.6149,
                "durationToWorstCase": 4.614853,
                "indexSpreadDuration": 0.0,
                "semiAnnualizedYield": 5.37382,
                "ziSpreadToWorstCall": 169.521,
                "znSpreadToWorstCall": 202.446,
                "benchmarkToWorstCall": "US 1.125 02/31",
                "spreadToRFRSwapCurve": 207.4469,
                "yearsToFinalMaturity": 5.406,
                "gnmafnmaSpreadDuration": 0.0,
                "spreadDurationTreasury": 4.615075,
                "fundedEffectiveDuration": 4.62504,
                "effectiveDurationPriceUp": 99.357039,
                "fundedEffectiveConvexity": 0.25471,
                "effectiveDurationPriceDown": 101.681381,
                "spreadToActCurveToWorstCall": 168.5152,
                "currentCouponSpreadConvexity": 0.0,
                "spreadToBenchmarkToWorstCall": 173.5282,
                "currentCouponSpreadSensitivity": 0.0,
                "spreadToTsyCurveAtBenchmarkTenor": 172.7405
            },
            "securityID": "912810FP"
        },
        "meta": {
            "status": "DONE",
            "requestId": "R-60843",
            "timeStamp": "2025-09-18T04:57:21Z",
            "responseType": "PY_CALC"
        }
    }

    """

    try:
        logger.info("Calling request_py_calculation_sync_by_id")

        response = Client().yield_book_rest.request_py_calculation_sync_by_id(
            id=id,
            id_type=id_type,
            level=level,
            pricing_date=pricing_date,
            curve_type=curve_type,
            currency=currency,
            prepay_type=prepay_type,
            prepay_rate=prepay_rate,
            option_model=option_model,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_py_calculation_sync_by_id")

        return output
    except Exception as err:
        logger.error("Error request_py_calculation_sync_by_id.")
        check_exception_and_raise(err, logger)


def request_return_attribution_async(
    *,
    global_settings: Optional[ReturnAttributionGlobalSettings] = None,
    input: Optional[List[ReturnAttributionInput]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Request return attribution async.

    Parameters
    ----------
    global_settings : ReturnAttributionGlobalSettings, optional

    input : List[ReturnAttributionInput], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling request_return_attribution_async")

        response = Client().yield_book_rest.request_return_attribution_async(
            body=ReturnAttributionRequest(global_settings=global_settings, input=input),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_return_attribution_async")

        return output
    except Exception as err:
        logger.error("Error request_return_attribution_async.")
        check_exception_and_raise(err, logger)


def request_return_attribution_sync(
    *,
    global_settings: Optional[ReturnAttributionGlobalSettings] = None,
    input: Optional[List[ReturnAttributionInput]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Request return attribution sync.

    Parameters
    ----------
    global_settings : ReturnAttributionGlobalSettings, optional

    input : List[ReturnAttributionInput], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling request_return_attribution_sync")

        response = Client().yield_book_rest.request_return_attribution_sync(
            body=ReturnAttributionRequest(global_settings=global_settings, input=input),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_return_attribution_sync")

        return output
    except Exception as err:
        logger.error("Error request_return_attribution_sync.")
        check_exception_and_raise(err, logger)


def request_scenario_calculation_async(
    *,
    global_settings: Optional[ScenarioCalcGlobalSettings] = None,
    keywords: Optional[List[str]] = None,
    scenarios: Optional[List[Scenario]] = None,
    input: Optional[List[ScenarioCalcInput]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Request scenario calculation async.

    Parameters
    ----------
    global_settings : ScenarioCalcGlobalSettings, optional

    keywords : List[str], optional

    scenarios : List[Scenario], optional

    input : List[ScenarioCalcInput], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------
    >>> # request_scenario_calculation_async
    >>> global_settings = ScenarioCalcGlobalSettings(
    >>>             pricing_date="2025-01-01",
    >>>         )
    >>>
    >>> scenario = Scenario(
    >>>             scenario_id="ScenID1",
    >>>             definition=ScenarioDefinition(
    >>>                 system_scenario=SystemScenario(name="BEARFLAT100")
    >>>             ),
    >>>         )
    >>>
    >>> input = ScenarioCalcInput(
    >>>             identifier="US742718AV11",
    >>>             id_type="ISIN",
    >>>             curve=CurveTypeAndCurrency(
    >>>                 curve_type="GVT",
    >>>                 currency="USD",
    >>>             ),
    >>>             settlement_info=SettlementInfo(
    >>>                 level="100",
    >>>             ),
    >>>             horizon_info=[
    >>>                 HorizonInfo(
    >>>                     scenario_id="ScenID1",
    >>>                     level="100",
    >>>                 )
    >>>             ],
    >>>             horizon_py_method="OAS",
    >>>         )
    >>>
    >>> # Request bond CF with async post
    >>> sa_async_post_response = request_scenario_calculation_async(
    >>>                             global_settings=global_settings,
    >>>                             scenarios=[scenario],
    >>>                             input=[input],
    >>>                         )
    >>>
    >>> async_post_results_response = {}
    >>>
    >>> attempt = 1
    >>>
    >>> while attempt < 10:
    >>>
    >>>     from lseg_analytics.exceptions import ServerError
    >>>     try:
    >>>         time.sleep(10)
    >>>         # Request bond indic with async post
    >>>         async_post_results_response = get_result(request_id_parameter=sa_async_post_response.request_id)
    >>>         break
    >>>     except Exception as err:
    >>>         print(f"Attempt " + str(
    >>>             attempt) + " resulted in error retrieving results from:" + sa_async_post_response.request_id)
    >>>         if (isinstance(err, ServerError)
    >>>                 and f"The result is not ready yet for requestID:{sa_async_post_response.request_id}" in str(err)):
    >>>
    >>>             attempt += 1
    >>>         else:
    >>>             raise err
    >>>
    >>> print(js.dumps(async_post_results_response, indent=4))
    {
        "meta": {
            "status": "DONE",
            "requestId": "R-21320",
            "timeStamp": "2025-08-19T02:17:06Z",
            "responseType": "SCENARIO_CALC",
            "resultsStatus": "ALL"
        },
        "results": [
            {
                "isin": "US742718AV11",
                "cusip": "742718AV1",
                "ticker": "PG",
                "scenario": {
                    "horizon": [
                        {
                            "oas": 100.0,
                            "wal": 4.8139,
                            "price": 104.89765,
                            "yield": 6.7865,
                            "balance": 1.0,
                            "pylevel": "100.000000",
                            "duration": 3.9209,
                            "fullPrice": 106.386538,
                            "returnCode": 0,
                            "scenarioID": "ScenID1",
                            "spreadDV01": 0.0,
                            "volatility": 16.0,
                            "actualPrice": 104.898,
                            "grossSpread": 99.9335,
                            "horizonDays": 0,
                            "marketValue": 106.386538,
                            "optionValue": 0.0,
                            "totalReturn": 4.8257988,
                            "dollarReturn": 4.89764958,
                            "convexityCost": 0.0,
                            "nominalSpread": 99.9335,
                            "effectiveYield": 0.0,
                            "interestReturn": 0.0,
                            "settlementDate": "2025-01-03",
                            "spreadDuration": 0.0,
                            "accruedInterest": 1.488889,
                            "actualFullPrice": 106.387,
                            "horizonPYMethod": "OAS",
                            "interestPayment": 0.0,
                            "principalReturn": 4.8257988,
                            "underlyingPrice": 0.0,
                            "principalPayment": 0.0,
                            "reinvestmentRate": 5.145556,
                            "yieldCurveMargin": 100.0,
                            "effectiveCallDate": "0",
                            "reinvestmentAmount": 0.0,
                            "actualAccruedInterest": 1.489
                        }
                    ],
                    "settlement": {
                        "oas": 361.951,
                        "psa": 0.0,
                        "wal": 4.8139,
                        "price": 100.0,
                        "yield": 7.9953,
                        "fullPrice": 101.488889,
                        "volatility": 13.0,
                        "grossSpread": 361.2649,
                        "optionValue": 0.0,
                        "pricingDate": "2024-12-31",
                        "forwardYield": 0.0,
                        "staticSpread": 0.0,
                        "effectiveDV01": 0.039405887,
                        "nominalSpread": 0.0,
                        "settlementDate": "2025-01-03",
                        "accruedInterest": 1.488889,
                        "reinvestmentRate": 4.329956,
                        "yieldCurveMargin": 0.0,
                        "effectiveDuration": 3.8828,
                        "effectiveConvexity": 0.1873
                    }
                },
                "returnCode": 0,
                "securityID": "742718AV",
                "description": "PROCTER & GAMBLE CO",
                "maturityDate": "2029-10-26",
                "securityType": "BOND",
                "currentCoupon": 8.0
            }
        ]
    }

    """

    try:
        logger.info("Calling request_scenario_calculation_async")

        response = Client().yield_book_rest.request_scenario_calculation_async(
            body=ScenarioCalcRequest(
                global_settings=global_settings,
                keywords=keywords,
                scenarios=scenarios,
                input=input,
            ),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
            content_type="application/json",
        )

        output = response
        logger.info("Called request_scenario_calculation_async")

        return output
    except Exception as err:
        logger.error("Error request_scenario_calculation_async.")
        check_exception_and_raise(err, logger)


def request_scenario_calculation_sync(
    *,
    global_settings: Optional[ScenarioCalcGlobalSettings] = None,
    keywords: Optional[List[str]] = None,
    scenarios: Optional[List[Scenario]] = None,
    input: Optional[List[ScenarioCalcInput]] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Request scenario calculation sync.

    Parameters
    ----------
    global_settings : ScenarioCalcGlobalSettings, optional

    keywords : List[str], optional

    scenarios : List[Scenario], optional

    input : List[ScenarioCalcInput], optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------
    >>> # request_scenario_calculation_async
    >>> global_settings = ScenarioCalcGlobalSettings(
    >>>             pricing_date="2025-01-01",
    >>>         )
    >>>
    >>> scenario = Scenario(
    >>>             scenario_id="ScenID1",
    >>>             definition=ScenarioDefinition(
    >>>                 system_scenario=SystemScenario(name="BEARFLAT100")
    >>>             ),
    >>>         )
    >>>
    >>> input = ScenarioCalcInput(
    >>>             identifier="US742718AV11",
    >>>             id_type="ISIN",
    >>>             curve=CurveTypeAndCurrency(
    >>>                 curve_type="GVT",
    >>>                 currency="USD",
    >>>             ),
    >>>             settlement_info=SettlementInfo(
    >>>                 level="100",
    >>>             ),
    >>>             horizon_info=[
    >>>                 HorizonInfo(
    >>>                     scenario_id="ScenID1",
    >>>                     level="100",
    >>>                 )
    >>>             ],
    >>>             horizon_py_method="OAS",
    >>>         )
    >>>
    >>> # Execute Post sync request with prepared inputs
    >>> sa_sync_post_response = request_scenario_calculation_sync(
    >>>                             global_settings=global_settings,
    >>>                             scenarios=[scenario],
    >>>                             input=[input],
    >>>                         )
    >>>
    >>> print(js.dumps(sa_sync_post_response, indent=4))
    {
        "meta": {
            "status": "DONE",
            "requestId": "R-60848",
            "timeStamp": "2025-09-18T04:57:27Z",
            "responseType": "SCENARIO_CALC",
            "resultsStatus": "ALL"
        },
        "results": [
            {
                "isin": "US742718AV11",
                "cusip": "742718AV1",
                "ticker": "PG",
                "scenario": {
                    "horizon": [
                        {
                            "oas": 100.0,
                            "wal": 4.8139,
                            "price": 104.89765,
                            "yield": 6.7865,
                            "balance": 1.0,
                            "pylevel": "100.000000",
                            "duration": 3.9209,
                            "fullPrice": 106.386538,
                            "returnCode": 0,
                            "scenarioID": "ScenID1",
                            "spreadDV01": 0.0,
                            "volatility": 16.0,
                            "actualPrice": 104.898,
                            "grossSpread": 99.9335,
                            "horizonDays": 0,
                            "marketValue": 106.386538,
                            "optionValue": 0.0,
                            "totalReturn": 4.8257988,
                            "dollarReturn": 4.89764958,
                            "convexityCost": 0.0,
                            "nominalSpread": 99.9335,
                            "effectiveYield": 0.0,
                            "interestReturn": 0.0,
                            "settlementDate": "2025-01-03",
                            "spreadDuration": 0.0,
                            "accruedInterest": 1.488889,
                            "actualFullPrice": 106.387,
                            "horizonPYMethod": "OAS",
                            "interestPayment": 0.0,
                            "principalReturn": 4.8257988,
                            "underlyingPrice": 0.0,
                            "principalPayment": 0.0,
                            "reinvestmentRate": 5.145556,
                            "yieldCurveMargin": 100.0,
                            "effectiveCallDate": "0",
                            "reinvestmentAmount": 0.0,
                            "actualAccruedInterest": 1.489
                        }
                    ],
                    "settlement": {
                        "oas": 361.951,
                        "psa": 0.0,
                        "wal": 4.8139,
                        "price": 100.0,
                        "yield": 7.9953,
                        "fullPrice": 101.488889,
                        "volatility": 13.0,
                        "grossSpread": 361.2649,
                        "optionValue": 0.0,
                        "pricingDate": "2024-12-31",
                        "forwardYield": 0.0,
                        "staticSpread": 0.0,
                        "effectiveDV01": 0.039405887,
                        "nominalSpread": 0.0,
                        "settlementDate": "2025-01-03",
                        "accruedInterest": 1.488889,
                        "reinvestmentRate": 4.329956,
                        "yieldCurveMargin": 0.0,
                        "effectiveDuration": 3.8828,
                        "effectiveConvexity": 0.1873
                    }
                },
                "returnCode": 0,
                "securityID": "742718AV",
                "description": "PROCTER & GAMBLE CO",
                "maturityDate": "2029-10-26",
                "securityType": "BOND",
                "currentCoupon": 8.0
            }
        ]
    }

    """

    try:
        logger.info("Calling request_scenario_calculation_sync")

        response = Client().yield_book_rest.request_scenario_calculation_sync(
            body=ScenarioCalcRequest(
                global_settings=global_settings,
                keywords=keywords,
                scenarios=scenarios,
                input=input,
            ),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
            content_type="application/json",
        )

        output = response
        logger.info("Called request_scenario_calculation_sync")

        return output
    except Exception as err:
        logger.error("Error request_scenario_calculation_sync.")
        check_exception_and_raise(err, logger)


def request_volatility_async(
    *,
    currency: str,
    date: str,
    quote_type: str,
    vol_model: Optional[str] = None,
    vol_type: Optional[str] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Request volatility async.

    Parameters
    ----------
    currency : str
        Currency should be a 3 letter upper case string
    date : str
        A sequence of textual characters.
    quote_type : str
        Should be one of the following - Calibrated, SOFRMarket, LIBORMarket.
    vol_model : str, optional
        Should be one of the following - Default, LMMSOFR, LMMSOFRNEW, LMMSOFRFLAT, LMMDL, LMMDDNEW, LMMDD. To be provided when quoteType is Calibrated
    vol_type : str, optional
        Should be one of the following - NORM, BLACK, To be provided when quoteType is SOFRMarket or LIBORMarket.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling request_volatility_async")

        response = Client().yield_book_rest.request_volatility_async(
            currency=currency,
            date=date,
            quote_type=quote_type,
            vol_model=vol_model,
            vol_type=vol_type,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_volatility_async")

        return output
    except Exception as err:
        logger.error("Error request_volatility_async.")
        check_exception_and_raise(err, logger)


def request_volatility_sync(
    *,
    currency: str,
    date: str,
    quote_type: str,
    vol_model: Optional[str] = None,
    vol_type: Optional[str] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Request volatility sync.

    Parameters
    ----------
    currency : str
        Currency should be a 3 letter upper case string
    date : str
        A sequence of textual characters.
    quote_type : str
        Should be one of the following - Calibrated, SOFRMarket, LIBORMarket.
    vol_model : str, optional
        Should be one of the following - Default, LMMSOFR, LMMSOFRNEW, LMMSOFRFLAT, LMMDL, LMMDDNEW, LMMDD. To be provided when quoteType is Calibrated
    vol_type : str, optional
        Should be one of the following - NORM, BLACK, To be provided when quoteType is SOFRMarket or LIBORMarket.
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling request_volatility_sync")

        response = Client().yield_book_rest.request_volatility_sync(
            currency=currency,
            date=date,
            quote_type=quote_type,
            vol_model=vol_model,
            vol_type=vol_type,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_volatility_sync")

        return output
    except Exception as err:
        logger.error("Error request_volatility_sync.")
        check_exception_and_raise(err, logger)


def request_wal_sensitivity_asyn_get(
    *,
    id: str,
    prepay_type: Union[str, WalSensitivityPrepayType],
    prepay_rate_start: int,
    prepay_rate_end: int,
    prepay_rate_step: int,
    tolerance: float,
    id_type: Optional[str] = None,
    horizon_date: Optional[Union[str, datetime.date]] = None,
    prepay_rate: Optional[int] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """


    Parameters
    ----------
    id : str
        Security reference ID.
    id_type : str, optional
        A sequence of textual characters.
    prepay_type : Union[str, WalSensitivityPrepayType]

    prepay_rate_start : int
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    prepay_rate_end : int
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    prepay_rate_step : int
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    tolerance : float
        A 64 bit floating point number. (`±5.0 × 10^−324` to `±1.7 × 10^308`)
    horizon_date : Union[str, datetime.date], optional
        A date on a calendar without a time zone, e.g. "April 10th"
    prepay_rate : int, optional
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling request_wal_sensitivity_asyn_get")

        response = Client().yield_book_rest.request_wal_sensitivity_asyn_get(
            id=id,
            id_type=id_type,
            prepay_type=prepay_type,
            prepay_rate_start=prepay_rate_start,
            prepay_rate_end=prepay_rate_end,
            prepay_rate_step=prepay_rate_step,
            tolerance=tolerance,
            horizon_date=horizon_date,
            prepay_rate=prepay_rate,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_wal_sensitivity_asyn_get")

        return output
    except Exception as err:
        logger.error("Error request_wal_sensitivity_asyn_get.")
        check_exception_and_raise(err, logger)


def request_wal_sensitivity_async(
    *,
    input: Optional[WalSensitivityInput] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """


    Parameters
    ----------
    input : WalSensitivityInput, optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling request_wal_sensitivity_async")

        response = Client().yield_book_rest.request_wal_sensitivity_async(
            body=WalSensitivityRequest(input=input),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_wal_sensitivity_async")

        return output
    except Exception as err:
        logger.error("Error request_wal_sensitivity_async.")
        check_exception_and_raise(err, logger)


def request_wal_sensitivity_sync(
    *,
    input: Optional[WalSensitivityInput] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """


    Parameters
    ----------
    input : WalSensitivityInput, optional

    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling request_wal_sensitivity_sync")

        response = Client().yield_book_rest.request_wal_sensitivity_sync(
            body=WalSensitivityRequest(input=input),
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_wal_sensitivity_sync")

        return output
    except Exception as err:
        logger.error("Error request_wal_sensitivity_sync.")
        check_exception_and_raise(err, logger)


def request_wal_sensitivity_sync_get(
    *,
    id: str,
    prepay_type: Union[str, WalSensitivityPrepayType],
    prepay_rate_start: int,
    prepay_rate_end: int,
    prepay_rate_step: int,
    tolerance: float,
    id_type: Optional[str] = None,
    horizon_date: Optional[Union[str, datetime.date]] = None,
    prepay_rate: Optional[int] = None,
    job: Optional[str] = None,
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """


    Parameters
    ----------
    id : str
        Security reference ID.
    id_type : str, optional
        A sequence of textual characters.
    prepay_type : Union[str, WalSensitivityPrepayType]

    prepay_rate_start : int
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    prepay_rate_end : int
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    prepay_rate_step : int
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    tolerance : float
        A 64 bit floating point number. (`±5.0 × 10^−324` to `±1.7 × 10^308`)
    horizon_date : Union[str, datetime.date], optional
        A date on a calendar without a time zone, e.g. "April 10th"
    prepay_rate : int, optional
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    job : str, optional
        Job reference. This can be of the form J-number or job name.
    name : str, optional
        User provided name.
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling request_wal_sensitivity_sync_get")

        response = Client().yield_book_rest.request_wal_sensitivity_sync_get(
            id=id,
            id_type=id_type,
            prepay_type=prepay_type,
            prepay_rate_start=prepay_rate_start,
            prepay_rate_end=prepay_rate_end,
            prepay_rate_step=prepay_rate_step,
            tolerance=tolerance,
            horizon_date=horizon_date,
            prepay_rate=prepay_rate,
            job=job,
            name=name,
            pri=pri,
            tags=tags,
        )

        output = response
        logger.info("Called request_wal_sensitivity_sync_get")

        return output
    except Exception as err:
        logger.error("Error request_wal_sensitivity_sync_get.")
        check_exception_and_raise(err, logger)


def resubmit_job(
    *,
    job_ref: str,
    scope: Optional[Literal["OK", "ERROR", "ABORTED", "FAILED", "ALL"]] = None,
    ids: Optional[List[str]] = None,
) -> JobResponse:
    """
    Resubmit a job

    Parameters
    ----------
    scope : Literal["OK","ERROR","ABORTED","FAILED","ALL"], optional

    ids : List[str], optional

    job_ref : str
        Job reference. This can be of the form J-number or job name.

    Returns
    --------
    JobResponse


    Examples
    --------
    >>> # create temp job
    >>> job_response = create_job(
    >>>     name="close_Job"
    >>> )
    >>>
    >>> # link a request to the job
    >>> indic_response = request_bond_indic_async_get(id="999818YT",
    >>>                                               id_type=IdTypeEnum.CUSIP,
    >>>                                               job=job_response.id
    >>>         )
    >>>
    >>> # close job
    >>> close_job_response = close_job(job_ref="close_Job")
    >>>
    >>> # provide a window of time for job to finish
    >>> time.sleep(10)
    >>>
    >>> # resubmit job
    >>> response = resubmit_job(job_ref=job_response.name, ids=[job_response.id], scope='OK')
    >>>
    >>> print(js.dumps(response.as_dict(), indent=4))
    {
        "id": "J-3640",
        "sequence": 0,
        "asOf": "2025-08-19",
        "closed": true,
        "onHold": false,
        "aborted": false,
        "actualHold": false,
        "name": "close_Job",
        "priority": 0,
        "order": "FAST",
        "requestCount": 1,
        "pendingCount": 1,
        "runningCount": 0,
        "okCount": 0,
        "errorCount": 0,
        "abortedCount": 0,
        "skipCount": 0,
        "startAfter": "2025-08-19T02:32:47.696Z",
        "stopAfter": "2025-08-20T02:32:47.696Z",
        "createdAt": "2025-08-19T02:32:47.698Z",
        "updatedAt": "2025-08-19T02:32:58.769Z"
    }

    """

    try:
        logger.info("Calling resubmit_job")

        response = Client().yield_book_rest.resubmit_job(
            body=JobResubmissionRequest(scope=scope, ids=ids), job_ref=job_ref
        )

        output = response
        logger.info("Called resubmit_job")

        return output
    except Exception as err:
        logger.error("Error resubmit_job.")
        check_exception_and_raise(err, logger)


def upload_csv_job_data_async(
    *,
    data: str,
    job: str,
    store_type: Union[str, StoreType],
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Async upload csv job data.

    Parameters
    ----------
    data : str
        A sequence of textual characters.
    job : str
        Job reference. This can be of the form J-number or job name.
    store_type : Union[str, StoreType]
        Job store object type. Should be one of the enumerated types.
    name : str, optional
        A sequence of textual characters.
    pri : int, optional
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling upload_csv_job_data_async")

        response = Client().yield_book_rest.upload_csv_job_data_async(
            job=job,
            store_type=store_type,
            name=name,
            pri=pri,
            tags=tags,
            content_type="text/csv",
            data=data,
        )

        output = response
        logger.info("Called upload_csv_job_data_async")

        return output
    except Exception as err:
        logger.error("Error upload_csv_job_data_async.")
        check_exception_and_raise(err, logger)


def upload_csv_job_data_sync(
    *,
    data: str,
    job: str,
    store_type: Union[str, StoreType],
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Sync upload csv job data.

    Parameters
    ----------
    data : str
        A sequence of textual characters.
    job : str
        Job reference. This can be of the form J-number or job name.
    store_type : Union[str, StoreType]
        Job store object type. Should be one of the enumerated types.
    name : str, optional
        A sequence of textual characters.
    pri : int, optional
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling upload_csv_job_data_sync")

        response = Client().yield_book_rest.upload_csv_job_data_sync(
            job=job,
            store_type=store_type,
            name=name,
            pri=pri,
            tags=tags,
            content_type="text/csv",
            data=data,
        )

        output = response
        logger.info("Called upload_csv_job_data_sync")

        return output
    except Exception as err:
        logger.error("Error upload_csv_job_data_sync.")
        check_exception_and_raise(err, logger)


def upload_csv_job_data_with_name_async(
    *,
    data: str,
    job: str,
    store_type: Union[str, StoreType],
    request_name: str,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Async upload csv job data with a user-provided name.

    Parameters
    ----------
    data : str
        A sequence of textual characters.
    job : str
        Job reference. This can be of the form J-number or job name.
    store_type : Union[str, StoreType]
        Job store object type. Should be one of the enumerated types.
    request_name : str
        User provided name for the request
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling upload_csv_job_data_with_name_async")

        response = Client().yield_book_rest.upload_csv_job_data_with_name_async(
            job=job,
            store_type=store_type,
            request_name=request_name,
            pri=pri,
            tags=tags,
            content_type="text/csv",
            data=data,
        )

        output = response
        logger.info("Called upload_csv_job_data_with_name_async")

        return output
    except Exception as err:
        logger.error("Error upload_csv_job_data_with_name_async.")
        check_exception_and_raise(err, logger)


def upload_csv_job_data_with_name_sync(
    *,
    data: str,
    job: str,
    store_type: Union[str, StoreType],
    request_name: str,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Sync upload csv job with a user-provided name.

    Parameters
    ----------
    data : str
        A sequence of textual characters.
    job : str
        Job reference. This can be of the form J-number or job name.
    store_type : Union[str, StoreType]
        Job store object type. Should be one of the enumerated types.
    request_name : str
        User provided name for the request
    pri : int, optional
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling upload_csv_job_data_with_name_sync")

        response = Client().yield_book_rest.upload_csv_job_data_with_name_sync(
            job=job,
            store_type=store_type,
            request_name=request_name,
            pri=pri,
            tags=tags,
            content_type="text/csv",
            data=data,
        )

        output = response
        logger.info("Called upload_csv_job_data_with_name_sync")

        return output
    except Exception as err:
        logger.error("Error upload_csv_job_data_with_name_sync.")
        check_exception_and_raise(err, logger)


def upload_json_job_data_async(
    *,
    data: JobStoreInputData,
    job: str,
    store_type: Union[str, StoreType],
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Async upload json job data.

    Parameters
    ----------
    data : JobStoreInputData

    job : str
        Job reference. This can be of the form J-number or job name.
    store_type : Union[str, StoreType]
        Job store object type. Should be one of the enumerated types.
    name : str, optional
        A sequence of textual characters.
    pri : int, optional
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling upload_json_job_data_async")

        response = Client().yield_book_rest.upload_json_job_data_async(
            job=job,
            store_type=store_type,
            name=name,
            pri=pri,
            tags=tags,
            content_type="application/json",
            data=data,
        )

        output = response
        logger.info("Called upload_json_job_data_async")

        return output
    except Exception as err:
        logger.error("Error upload_json_job_data_async.")
        check_exception_and_raise(err, logger)


def upload_json_job_data_sync(
    *,
    data: JobStoreInputData,
    job: str,
    store_type: Union[str, StoreType],
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Sync upload json job data.

    Parameters
    ----------
    data : JobStoreInputData

    job : str
        Job reference. This can be of the form J-number or job name.
    store_type : Union[str, StoreType]
        Job store object type. Should be one of the enumerated types.
    name : str, optional
        A sequence of textual characters.
    pri : int, optional
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling upload_json_job_data_sync")

        response = Client().yield_book_rest.upload_json_job_data_sync(
            job=job,
            store_type=store_type,
            name=name,
            pri=pri,
            tags=tags,
            content_type="application/json",
            data=data,
        )

        output = response
        logger.info("Called upload_json_job_data_sync")

        return output
    except Exception as err:
        logger.error("Error upload_json_job_data_sync.")
        check_exception_and_raise(err, logger)


def upload_json_job_data_with_name_async(
    *,
    data: JobStoreInputData,
    job: str,
    store_type: Union[str, StoreType],
    request_name: str,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Async upload json job data with a user-provided name.

    Parameters
    ----------
    data : JobStoreInputData

    job : str
        Job reference. This can be of the form J-number or job name.
    store_type : Union[str, StoreType]
        Job store object type. Should be one of the enumerated types.
    request_name : str
        User provided name for the request
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling upload_json_job_data_with_name_async")

        response = Client().yield_book_rest.upload_json_job_data_with_name_async(
            job=job,
            store_type=store_type,
            request_name=request_name,
            pri=pri,
            tags=tags,
            content_type="application/json",
            data=data,
        )

        output = response
        logger.info("Called upload_json_job_data_with_name_async")

        return output
    except Exception as err:
        logger.error("Error upload_json_job_data_with_name_async.")
        check_exception_and_raise(err, logger)


def upload_json_job_data_with_name_sync(
    *,
    data: JobStoreInputData,
    job: str,
    store_type: Union[str, StoreType],
    request_name: str,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Sync upload json job data with a user-provided name.

    Parameters
    ----------
    data : JobStoreInputData

    job : str
        Job reference. This can be of the form J-number or job name.
    store_type : Union[str, StoreType]
        Job store object type. Should be one of the enumerated types.
    request_name : str
        User provided name for the request
    pri : int, optional
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling upload_json_job_data_with_name_sync")

        response = Client().yield_book_rest.upload_json_job_data_with_name_sync(
            job=job,
            store_type=store_type,
            request_name=request_name,
            pri=pri,
            tags=tags,
            content_type="application/json",
            data=data,
        )

        output = response
        logger.info("Called upload_json_job_data_with_name_sync")

        return output
    except Exception as err:
        logger.error("Error upload_json_job_data_with_name_sync.")
        check_exception_and_raise(err, logger)


def upload_text_job_data_async(
    *,
    data: str,
    job: str,
    store_type: Union[str, StoreType],
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Async upload text job data.

    Parameters
    ----------
    data : str
        A sequence of textual characters.
    job : str
        Job reference. This can be of the form J-number or job name.
    store_type : Union[str, StoreType]
        Job store object type. Should be one of the enumerated types.
    name : str, optional
        A sequence of textual characters.
    pri : int, optional
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling upload_text_job_data_async")

        response = Client().yield_book_rest.upload_text_job_data_async(
            job=job,
            store_type=store_type,
            name=name,
            pri=pri,
            tags=tags,
            content_type="text/plain",
            data=data,
        )

        output = response
        logger.info("Called upload_text_job_data_async")

        return output
    except Exception as err:
        logger.error("Error upload_text_job_data_async.")
        check_exception_and_raise(err, logger)


def upload_text_job_data_sync(
    *,
    data: str,
    job: str,
    store_type: Union[str, StoreType],
    name: Optional[str] = None,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Sync upload text job data.

    Parameters
    ----------
    data : str
        A sequence of textual characters.
    job : str
        Job reference. This can be of the form J-number or job name.
    store_type : Union[str, StoreType]
        Job store object type. Should be one of the enumerated types.
    name : str, optional
        A sequence of textual characters.
    pri : int, optional
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling upload_text_job_data_sync")

        response = Client().yield_book_rest.upload_text_job_data_sync(
            job=job,
            store_type=store_type,
            name=name,
            pri=pri,
            tags=tags,
            content_type="text/plain",
            data=data,
        )

        output = response
        logger.info("Called upload_text_job_data_sync")

        return output
    except Exception as err:
        logger.error("Error upload_text_job_data_sync.")
        check_exception_and_raise(err, logger)


def upload_text_job_data_with_name_async(
    *,
    data: str,
    job: str,
    store_type: Union[str, StoreType],
    request_name: str,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> RequestId:
    """
    Async upload text job data with a user-provided name.

    Parameters
    ----------
    data : str
        A sequence of textual characters.
    job : str
        Job reference. This can be of the form J-number or job name.
    store_type : Union[str, StoreType]
        Job store object type. Should be one of the enumerated types.
    request_name : str
        User provided name for the request
    pri : int, optional
        Priority for this request in the queue.
    tags : List[str], optional


    Returns
    --------
    RequestId


    Examples
    --------


    """

    try:
        logger.info("Calling upload_text_job_data_with_name_async")

        response = Client().yield_book_rest.upload_text_job_data_with_name_async(
            job=job,
            store_type=store_type,
            request_name=request_name,
            pri=pri,
            tags=tags,
            content_type="text/plain",
            data=data,
        )

        output = response
        logger.info("Called upload_text_job_data_with_name_async")

        return output
    except Exception as err:
        logger.error("Error upload_text_job_data_with_name_async.")
        check_exception_and_raise(err, logger)


def upload_text_job_data_with_name_sync(
    *,
    data: str,
    job: str,
    store_type: Union[str, StoreType],
    request_name: str,
    pri: Optional[int] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Sync upload text job data with a user-provided name.

    Parameters
    ----------
    data : str
        A sequence of textual characters.
    job : str
        Job reference. This can be of the form J-number or job name.
    store_type : Union[str, StoreType]
        Job store object type. Should be one of the enumerated types.
    request_name : str
        User provided name for the request
    pri : int, optional
        A 32-bit integer. (`-2,147,483,648` to `2,147,483,647`)
    tags : List[str], optional


    Returns
    --------
    Dict[str, Any]


    Examples
    --------


    """

    try:
        logger.info("Calling upload_text_job_data_with_name_sync")

        response = Client().yield_book_rest.upload_text_job_data_with_name_sync(
            job=job,
            store_type=store_type,
            request_name=request_name,
            pri=pri,
            tags=tags,
            content_type="text/plain",
            data=data,
        )

        output = response
        logger.info("Called upload_text_job_data_with_name_sync")

        return output
    except Exception as err:
        logger.error("Error upload_text_job_data_with_name_sync.")
        check_exception_and_raise(err, logger)
