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
from lseg_analytics_basic_client.models import (
    CrossCurencySwapOverride,
    CurencyBasisSwapOverride,
    Description,
    IrPricingParameters,
    IrSwapAsCollectionItem,
    IrSwapDefinition,
    IrSwapDefinitionInstrument,
    IrSwapInstrumentSolveResponseFieldsOnResourceResponseData,
    IrSwapInstrumentSolveResponseFieldsResponseData,
    IrSwapInstrumentValuationResponseFieldsOnResourceResponseData,
    IrSwapInstrumentValuationResponseFieldsResponseData,
    Location,
    MarketData,
    ResourceType,
    SortingOrderEnum,
    TenorBasisSwapOverride,
    VanillaIrsOverride,
)

from ._logger import logger


class IrSwap(ResourceBase):
    """
    IrSwap object.

    Contains all the necessary information to identify and define a IrSwap instance.

    Attributes
    ----------
    type : Union[str, ResourceType], optional
        Property defining the type of the resource.
    id : str, optional
        Unique identifier of the IrSwap.
    location : Location
        Object defining the location of the IrSwap in the platform.
    description : Description, optional
        Object defining metadata for the IrSwap.
    definition : IrSwapDefinition
        Object defining the IrSwap.

    See Also
    --------
    IrSwap.solve : Calculate analytics for an interest rate swap stored on the platform, by solving a variable parameter (e.g., fixed rate) provided in the request,
        so that a specified property (e.g., market value, duration) matches a target value.
        Provide an instrument ID in the request to perform the solving.
    IrSwap.value : Calculate analytics for an interest rate swap stored on the platform, including valuation results, risk metrics, and other relevant measures.
        Provide an instrument ID in the request to perform the valuation.

    Examples
    --------


    """

    _definition_class = IrSwapDefinition

    def __init__(self, definition: IrSwapDefinition, description: Optional[Description] = None):
        """
        IrSwap constructor

        Parameters
        ----------
        definition : IrSwapDefinition
            Object defining the IrSwap.
        description : Description, optional
            Object defining metadata for the IrSwap.

        Examples
        --------


        """
        self.definition: IrSwapDefinition = definition
        self.type: Optional[Union[str, ResourceType]] = "IrSwap"
        if description is None:
            self.description: Optional[Description] = Description(tags=[])
        else:
            self.description: Optional[Description] = description
        self._location: Location = Location(name="")
        self._id: Optional[str] = None

    @property
    def id(self):
        """
        Returns the IrSwap id

        Parameters
        ----------


        Returns
        --------
        str
            Unique identifier of the IrSwap.

        Examples
        --------


        """
        return self._id

    @id.setter
    def id(self, value):
        raise AttributeError("id is read only")

    @property
    def location(self):
        """
        Returns the IrSwap location

        Parameters
        ----------


        Returns
        --------
        Location
            Object defining the location of the IrSwap in the platform.

        Examples
        --------


        """
        return self._location

    @location.setter
    def location(self, value):
        raise AttributeError("location is read only")

    def _create(self, location: Location) -> None:
        """
        Save a new IrSwap in the platform

        Parameters
        ----------
        location : Location
            Object defining the location of the IrSwap in the platform.

        Returns
        --------
        None


        Examples
        --------


        """

        try:
            logger.info("Creating IrSwap")

            response = Client().ir_swaps_resource.create(
                location=location,
                description=self.description,
                definition=self.definition,
            )

            self._id = response.data.id

            self._location = response.data.location
            logger.info(f"IrSwap created with id: {self._id}")
        except Exception as err:
            logger.error("Error creating IrSwap:")
            raise err

    def _overwrite(self) -> None:
        """
        Overwrite a IrSwap that exists in the platform. The IrSwap can be identified either by its unique ID (GUID format) or by its location path (space/name).

        Parameters
        ----------


        Returns
        --------
        None


        Examples
        --------


        """
        logger.info(f"Overwriting IrSwap with id: {self._id}")
        Client().ir_swap_resource.overwrite(
            instrument_id=self._id,
            location=self._location,
            description=self.description,
            definition=self.definition,
        )

    def solve(
        self,
        *,
        pricing_preferences: Optional[IrPricingParameters] = None,
        market_data: Optional[MarketData] = None,
        return_market_data: Optional[bool] = None,
        fields: Optional[str] = None,
    ) -> IrSwapInstrumentSolveResponseFieldsOnResourceResponseData:
        """
        Calculate analytics for an interest rate swap stored on the platform, by solving a variable parameter (e.g., fixed rate) provided in the request,
        so that a specified property (e.g., market value, duration) matches a target value.
        Provide an instrument ID in the request to perform the solving.

        Parameters
        ----------
        pricing_preferences : IrPricingParameters, optional
            The parameters that control the computation of the analytics.
        market_data : MarketData, optional
            The market data used to compute the analytics.
        return_market_data : bool, optional
            Boolean property to determine if undelying market data used for calculation should be returned in the response
        fields : str, optional
            A parameter used to select the fields to return in response. If not provided, all fields will be returned.
            Some usage examples:
            1. Simply enumerating the fields, separating them by ',', e.g. 'fields=//please insert the selected fields here, e.g., field1, field2 //'
            2. Using parentheses to indicate nesting, e.g. 'fields= //please insert the selected field and subfields here, e.g., field1(subfield1, subfield2), field2(subfield3)//’
            3. Using forward slash '/' to indicate nesting, e.g. 'fields=//please insert the selected field and subfields here, e.g.,  field1/subfield1, field1/subfield2, field2/subfield3//’ (same result as example above)
            4. Operators can even be combined (forward slashes in brackets, not the way around), e.g. 'fields=//please insert the selected field and subfields here, e.g.,  field1(subfield1/subsubfield1), field2/subfield2//'

        Returns
        --------
        IrSwapInstrumentSolveResponseFieldsOnResourceResponseData


        Examples
        --------
        >>> # build the swap from 'LSEG/OIS_SOFR' template
        >>> fwd_start_sofr = create_from_vanilla_irs_template(template_reference = "LSEG/OIS_SOFR")
        >>>
        >>> # Swap needs to be saved in order for the solve class method to be executable
        >>> fwd_start_sofr.save(name="sofr_fwd_start_swap_exm")
        >>>
        >>> # set a solving variable between first and second leg and Fixed Rate or Spread
        >>> solving_variable = IrSwapSolvingVariable(leg='FirstLeg', name='FixedRate')
        >>>
        >>> # Apply solving target(s)
        >>> solving_target=IrSwapSolvingTarget(market_value=IrMeasure(value=0.0))
        >>>
        >>> # Setup the solving parameter object
        >>> solving_parameters = IrSwapSolvingParameters(variable=solving_variable, target=solving_target)
        >>>
        >>> # instantiate pricing parameters
        >>> pricing_parameters = IrPricingParameters(solving_parameters=solving_parameters)
        >>>
        >>> # solve the swap par rate
        >>> solving_response_object = fwd_start_sofr.solve(pricing_preferences=pricing_parameters)
        >>>
        >>> delete(name="sofr_fwd_start_swap_exm")
        >>>
        >>> print(js.dumps(solving_response_object.analytics.as_dict(), indent=4))
        {
            "solving": {
                "result": 3.5328390419751576
            },
            "description": {
                "instrumentTag": "",
                "instrumentDescription": "Pay USD Annual 3.53% vs Receive USD Annual +0bp SOFR 2035-09-24",
                "startDate": "2025-09-22",
                "endDate": "2035-09-24",
                "tenor": "10Y"
            },
            "valuation": {
                "accrued": {
                    "value": 0.0,
                    "percent": 0.0,
                    "dealCurrency": {
                        "value": 0.0,
                        "currency": "USD"
                    },
                    "reportCurrency": {
                        "value": 0.0,
                        "currency": "USD"
                    }
                },
                "marketValue": {
                    "value": 0.0,
                    "dealCurrency": {
                        "value": 0.0,
                        "currency": "USD"
                    },
                    "reportCurrency": {
                        "value": 0.0,
                        "currency": "USD"
                    }
                },
                "cleanMarketValue": {
                    "value": 0.0,
                    "dealCurrency": {
                        "value": 0.0,
                        "currency": "USD"
                    },
                    "reportCurrency": {
                        "value": 0.0,
                        "currency": "USD"
                    }
                }
            },
            "risk": {
                "duration": {
                    "value": -8.57545690242625
                },
                "modifiedDuration": {
                    "value": -8.27445117125687
                },
                "benchmarkHedgeNotional": {
                    "value": -9877797.16301786,
                    "currency": "USD"
                },
                "annuity": {
                    "value": -8460.29262626451,
                    "dealCurrency": {
                        "value": -8460.29262626451,
                        "currency": "USD"
                    },
                    "reportCurrency": {
                        "value": -8460.29262626451,
                        "currency": "USD"
                    }
                },
                "dv01": {
                    "value": -8269.26340721175,
                    "bp": -8.26926340721175,
                    "dealCurrency": {
                        "value": -8269.26340721175,
                        "currency": "USD"
                    },
                    "reportCurrency": {
                        "value": -8269.26340721175,
                        "currency": "USD"
                    }
                },
                "pv01": {
                    "value": -8269.26340721454,
                    "bp": -8.26926340721454,
                    "dealCurrency": {
                        "value": -8269.26340721454,
                        "currency": "USD"
                    },
                    "reportCurrency": {
                        "value": -8269.26340721454,
                        "currency": "USD"
                    }
                },
                "br01": {
                    "value": 0.0,
                    "dealCurrency": {
                        "value": 0.0,
                        "currency": "USD"
                    },
                    "reportCurrency": {
                        "value": 0.0,
                        "currency": "USD"
                    }
                }
            },
            "firstLeg": {
                "description": {
                    "legTag": "PaidLeg",
                    "legDescription": "Pay USD Annual 3.53%",
                    "interestType": "Fixed",
                    "currency": "USD",
                    "startDate": "2025-09-22",
                    "endDate": "2035-09-24",
                    "index": ""
                },
                "valuation": {
                    "accrued": {
                        "value": 0.0,
                        "percent": 0.0,
                        "dealCurrency": {
                            "value": 0.0,
                            "currency": "USD"
                        },
                        "reportCurrency": {
                            "value": 0.0,
                            "currency": "USD"
                        }
                    },
                    "marketValue": {
                        "value": 2988885.209660194,
                        "dealCurrency": {
                            "value": 2988885.209660194,
                            "currency": "USD"
                        },
                        "reportCurrency": {
                            "value": 2988885.209660194,
                            "currency": "USD"
                        }
                    },
                    "cleanMarketValue": {
                        "value": 2988885.209660194,
                        "dealCurrency": {
                            "value": 2988885.209660194,
                            "currency": "USD"
                        },
                        "reportCurrency": {
                            "value": 2988885.209660194,
                            "currency": "USD"
                        }
                    }
                },
                "risk": {
                    "duration": {
                        "value": 8.575456902426252
                    },
                    "modifiedDuration": {
                        "value": 8.289251274671441
                    },
                    "benchmarkHedgeNotional": {
                        "value": 0.0,
                        "currency": "USD"
                    },
                    "annuity": {
                        "value": 8460.292626264505,
                        "dealCurrency": {
                            "value": 8460.292626264505,
                            "currency": "USD"
                        },
                        "reportCurrency": {
                            "value": 8460.292626264505,
                            "currency": "USD"
                        }
                    },
                    "dv01": {
                        "value": 8284.054231528193,
                        "bp": 8.284054231528193,
                        "dealCurrency": {
                            "value": 8284.054231528193,
                            "currency": "USD"
                        },
                        "reportCurrency": {
                            "value": 8284.054231528193,
                            "currency": "USD"
                        }
                    },
                    "pv01": {
                        "value": 1510.757442836184,
                        "bp": 1.510757442836184,
                        "dealCurrency": {
                            "value": 1510.757442836184,
                            "currency": "USD"
                        },
                        "reportCurrency": {
                            "value": 1510.757442836184,
                            "currency": "USD"
                        }
                    },
                    "br01": {
                        "value": 0.0,
                        "dealCurrency": {
                            "value": 0.0,
                            "currency": "USD"
                        },
                        "reportCurrency": {
                            "value": 0.0,
                            "currency": "USD"
                        }
                    }
                },
                "cashflows": [
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.5328390419751576,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.9643554183463504,
                        "startDate": "2025-09-22",
                        "endDate": "2026-09-22",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FixedRate",
                        "zeroRate": {
                            "value": 3.6353574893679186,
                            "unit": "Percentage"
                        },
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2026-09-24"
                        },
                        "amount": {
                            "value": -358190.6250891479,
                            "currency": "USD"
                        },
                        "payer": "Party1",
                        "receiver": "Party2",
                        "occurrence": "Future"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.5328390419751576,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.9360884457461076,
                        "startDate": "2026-09-22",
                        "endDate": "2027-09-22",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FixedRate",
                        "zeroRate": {
                            "value": 3.329574916283895,
                            "unit": "Percentage"
                        },
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2027-09-24"
                        },
                        "amount": {
                            "value": -358190.6250891479,
                            "currency": "USD"
                        },
                        "payer": "Party1",
                        "receiver": "Party2",
                        "occurrence": "Future"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.5328390419751576,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.9074217195314633,
                        "startDate": "2027-09-22",
                        "endDate": "2028-09-22",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FixedRate",
                        "zeroRate": {
                            "value": 3.26701112972283,
                            "unit": "Percentage"
                        },
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2028-09-26"
                        },
                        "amount": {
                            "value": -359171.9692674744,
                            "currency": "USD"
                        },
                        "payer": "Party1",
                        "receiver": "Party2",
                        "occurrence": "Future"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.5328390419751576,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.8786862602921595,
                        "startDate": "2028-09-22",
                        "endDate": "2029-09-24",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FixedRate",
                        "zeroRate": {
                            "value": 3.2700862871802627,
                            "unit": "Percentage"
                        },
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2029-09-25"
                        },
                        "amount": {
                            "value": -360153.3134458008,
                            "currency": "USD"
                        },
                        "payer": "Party1",
                        "receiver": "Party2",
                        "occurrence": "Future"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.5328390419751576,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.8495203665317632,
                        "startDate": "2029-09-24",
                        "endDate": "2030-09-23",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FixedRate",
                        "zeroRate": {
                            "value": 3.304400781488259,
                            "unit": "Percentage"
                        },
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2030-09-24"
                        },
                        "amount": {
                            "value": -357209.28091082146,
                            "currency": "USD"
                        },
                        "payer": "Party1",
                        "receiver": "Party2",
                        "occurrence": "Future"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.5328390419751576,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.8198176135559454,
                        "startDate": "2030-09-23",
                        "endDate": "2031-09-22",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FixedRate",
                        "zeroRate": {
                            "value": 3.357302997591338,
                            "unit": "Percentage"
                        },
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2031-09-24"
                        },
                        "amount": {
                            "value": -357209.28091082146,
                            "currency": "USD"
                        },
                        "payer": "Party1",
                        "receiver": "Party2",
                        "occurrence": "Future"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.5328390419751576,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.7897892210034109,
                        "startDate": "2031-09-22",
                        "endDate": "2032-09-22",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FixedRate",
                        "zeroRate": {
                            "value": 3.420576604330039,
                            "unit": "Percentage"
                        },
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2032-09-24"
                        },
                        "amount": {
                            "value": -359171.9692674744,
                            "currency": "USD"
                        },
                        "payer": "Party1",
                        "receiver": "Party2",
                        "occurrence": "Future"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.5328390419751576,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.7596696254623827,
                        "startDate": "2032-09-22",
                        "endDate": "2033-09-22",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FixedRate",
                        "zeroRate": {
                            "value": 3.4858889232466828,
                            "unit": "Percentage"
                        },
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2033-09-26"
                        },
                        "amount": {
                            "value": -358190.6250891479,
                            "currency": "USD"
                        },
                        "payer": "Party1",
                        "receiver": "Party2",
                        "occurrence": "Future"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.5328390419751576,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.7298356640943585,
                        "startDate": "2033-09-22",
                        "endDate": "2034-09-22",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FixedRate",
                        "zeroRate": {
                            "value": 3.552429625512943,
                            "unit": "Percentage"
                        },
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2034-09-26"
                        },
                        "amount": {
                            "value": -358190.6250891479,
                            "currency": "USD"
                        },
                        "payer": "Party1",
                        "receiver": "Party2",
                        "occurrence": "Future"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.5328390419751576,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.7004845173252519,
                        "startDate": "2034-09-22",
                        "endDate": "2035-09-24",
                        "remainingNotional": 0.0,
                        "interestRateType": "FixedRate",
                        "zeroRate": {
                            "value": 3.6168900107566238,
                            "unit": "Percentage"
                        },
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2035-09-25"
                        },
                        "amount": {
                            "value": -360153.3134458008,
                            "currency": "USD"
                        },
                        "payer": "Party1",
                        "receiver": "Party2",
                        "occurrence": "Future"
                    }
                ]
            },
            "secondLeg": {
                "description": {
                    "legTag": "ReceivedLeg",
                    "legDescription": "Receive USD Annual +0bp SOFR",
                    "interestType": "Float",
                    "currency": "USD",
                    "startDate": "2025-09-22",
                    "endDate": "2035-09-24",
                    "index": "SOFR"
                },
                "valuation": {
                    "accrued": {
                        "value": 0.0,
                        "percent": 0.0,
                        "dealCurrency": {
                            "value": 0.0,
                            "currency": "USD"
                        },
                        "reportCurrency": {
                            "value": 0.0,
                            "currency": "USD"
                        }
                    },
                    "marketValue": {
                        "value": 2988885.209660194,
                        "dealCurrency": {
                            "value": 2988885.209660194,
                            "currency": "USD"
                        },
                        "reportCurrency": {
                            "value": 2988885.209660194,
                            "currency": "USD"
                        }
                    },
                    "cleanMarketValue": {
                        "value": 2988885.209660194,
                        "dealCurrency": {
                            "value": 2988885.209660194,
                            "currency": "USD"
                        },
                        "reportCurrency": {
                            "value": 2988885.209660194,
                            "currency": "USD"
                        }
                    }
                },
                "risk": {
                    "duration": {
                        "value": 0.0
                    },
                    "modifiedDuration": {
                        "value": 0.01480010341456817
                    },
                    "benchmarkHedgeNotional": {
                        "value": 0.0,
                        "currency": "USD"
                    },
                    "annuity": {
                        "value": 0.0,
                        "dealCurrency": {
                            "value": 0.0,
                            "currency": "USD"
                        },
                        "reportCurrency": {
                            "value": 0.0,
                            "currency": "USD"
                        }
                    },
                    "dv01": {
                        "value": 14.790824316442013,
                        "bp": 0.014790824316442013,
                        "dealCurrency": {
                            "value": 14.790824316442013,
                            "currency": "USD"
                        },
                        "reportCurrency": {
                            "value": 14.790824316442013,
                            "currency": "USD"
                        }
                    },
                    "pv01": {
                        "value": -6758.505964378361,
                        "bp": -6.75850596437836,
                        "dealCurrency": {
                            "value": -6758.505964378361,
                            "currency": "USD"
                        },
                        "reportCurrency": {
                            "value": -6758.505964378361,
                            "currency": "USD"
                        }
                    },
                    "br01": {
                        "value": 0.0,
                        "dealCurrency": {
                            "value": 0.0,
                            "currency": "USD"
                        },
                        "reportCurrency": {
                            "value": 0.0,
                            "currency": "USD"
                        }
                    }
                },
                "cashflows": [
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.5789998785724,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.9643554183463504,
                        "startDate": "2025-09-22",
                        "endDate": "2026-09-22",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FloatingRate",
                        "zeroRate": {
                            "value": 3.6353574893679186,
                            "unit": "Percentage"
                        },
                        "indexFixings": [
                            {
                                "accrualEndDate": "2026-09-22",
                                "accrualStartDate": "2025-09-22",
                                "couponRate": {
                                    "value": 3.579,
                                    "unit": "Percentage"
                                },
                                "fixingDate": "2025-09-22",
                                "forwardSource": "ZcCurve",
                                "referenceRate": {
                                    "value": 3.579,
                                    "unit": "Percentage"
                                },
                                "spreadBp": 0.0
                            }
                        ],
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2026-09-24"
                        },
                        "amount": {
                            "value": 362870.8210219239,
                            "currency": "USD"
                        },
                        "payer": "Party2",
                        "receiver": "Party1",
                        "occurrence": "Projected"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 2.9790768151301004,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.9360884457461076,
                        "startDate": "2026-09-22",
                        "endDate": "2027-09-22",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FloatingRate",
                        "zeroRate": {
                            "value": 3.329574916283895,
                            "unit": "Percentage"
                        },
                        "indexFixings": [
                            {
                                "accrualEndDate": "2027-09-22",
                                "accrualStartDate": "2026-09-22",
                                "couponRate": {
                                    "value": 2.9790769,
                                    "unit": "Percentage"
                                },
                                "fixingDate": "2026-09-22",
                                "forwardSource": "ZcCurve",
                                "referenceRate": {
                                    "value": 2.9790769,
                                    "unit": "Percentage"
                                },
                                "spreadBp": 0.0
                            }
                        ],
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2027-09-24"
                        },
                        "amount": {
                            "value": 302045.2882006907,
                            "currency": "USD"
                        },
                        "payer": "Party2",
                        "receiver": "Party1",
                        "occurrence": "Projected"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.0889174786622,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.9074217195314633,
                        "startDate": "2027-09-22",
                        "endDate": "2028-09-22",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FloatingRate",
                        "zeroRate": {
                            "value": 3.26701112972283,
                            "unit": "Percentage"
                        },
                        "indexFixings": [
                            {
                                "accrualEndDate": "2028-09-22",
                                "accrualStartDate": "2027-09-22",
                                "couponRate": {
                                    "value": 3.0889175,
                                    "unit": "Percentage"
                                },
                                "fixingDate": "2027-09-22",
                                "forwardSource": "ZcCurve",
                                "referenceRate": {
                                    "value": 3.0889175,
                                    "unit": "Percentage"
                                },
                                "spreadBp": 0.0
                            }
                        ],
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2028-09-26"
                        },
                        "amount": {
                            "value": 314039.94366399036,
                            "currency": "USD"
                        },
                        "payer": "Party2",
                        "receiver": "Party1",
                        "occurrence": "Projected"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.2337980302786,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.8786862602921595,
                        "startDate": "2028-09-22",
                        "endDate": "2029-09-24",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FloatingRate",
                        "zeroRate": {
                            "value": 3.2700862871802627,
                            "unit": "Percentage"
                        },
                        "indexFixings": [
                            {
                                "accrualEndDate": "2029-09-24",
                                "accrualStartDate": "2028-09-22",
                                "couponRate": {
                                    "value": 3.233798,
                                    "unit": "Percentage"
                                },
                                "fixingDate": "2028-09-22",
                                "forwardSource": "ZcCurve",
                                "referenceRate": {
                                    "value": 3.233798,
                                    "unit": "Percentage"
                                },
                                "spreadBp": 0.0
                            }
                        ],
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2029-09-25"
                        },
                        "amount": {
                            "value": 329667.7436422906,
                            "currency": "USD"
                        },
                        "payer": "Party2",
                        "receiver": "Party1",
                        "occurrence": "Projected"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.3950135440994003,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.8495203665317632,
                        "startDate": "2029-09-24",
                        "endDate": "2030-09-23",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FloatingRate",
                        "zeroRate": {
                            "value": 3.304400781488259,
                            "unit": "Percentage"
                        },
                        "indexFixings": [
                            {
                                "accrualEndDate": "2030-09-23",
                                "accrualStartDate": "2029-09-24",
                                "couponRate": {
                                    "value": 3.3950136,
                                    "unit": "Percentage"
                                },
                                "fixingDate": "2029-09-24",
                                "forwardSource": "ZcCurve",
                                "referenceRate": {
                                    "value": 3.3950136,
                                    "unit": "Percentage"
                                },
                                "spreadBp": 0.0
                            }
                        ],
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2030-09-24"
                        },
                        "amount": {
                            "value": 343273.5916811616,
                            "currency": "USD"
                        },
                        "payer": "Party2",
                        "receiver": "Party1",
                        "occurrence": "Projected"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.572568388904,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.8198176135559454,
                        "startDate": "2030-09-23",
                        "endDate": "2031-09-22",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FloatingRate",
                        "zeroRate": {
                            "value": 3.357302997591338,
                            "unit": "Percentage"
                        },
                        "indexFixings": [
                            {
                                "accrualEndDate": "2031-09-22",
                                "accrualStartDate": "2030-09-23",
                                "couponRate": {
                                    "value": 3.5725684,
                                    "unit": "Percentage"
                                },
                                "fixingDate": "2030-09-23",
                                "forwardSource": "ZcCurve",
                                "referenceRate": {
                                    "value": 3.5725684,
                                    "unit": "Percentage"
                                },
                                "spreadBp": 0.0
                            }
                        ],
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2031-09-24"
                        },
                        "amount": {
                            "value": 361226.35932251555,
                            "currency": "USD"
                        },
                        "payer": "Party2",
                        "receiver": "Party1",
                        "occurrence": "Projected"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.7388975365785004,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.7897892210034109,
                        "startDate": "2031-09-22",
                        "endDate": "2032-09-22",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FloatingRate",
                        "zeroRate": {
                            "value": 3.420576604330039,
                            "unit": "Percentage"
                        },
                        "indexFixings": [
                            {
                                "accrualEndDate": "2032-09-22",
                                "accrualStartDate": "2031-09-22",
                                "couponRate": {
                                    "value": 3.7388976,
                                    "unit": "Percentage"
                                },
                                "fixingDate": "2031-09-22",
                                "forwardSource": "ZcCurve",
                                "referenceRate": {
                                    "value": 3.7388976,
                                    "unit": "Percentage"
                                },
                                "spreadBp": 0.0
                            }
                        ],
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2032-09-24"
                        },
                        "amount": {
                            "value": 380121.24955214746,
                            "currency": "USD"
                        },
                        "payer": "Party2",
                        "receiver": "Party1",
                        "occurrence": "Projected"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 3.887571332702201,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.7596696254623827,
                        "startDate": "2032-09-22",
                        "endDate": "2033-09-22",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FloatingRate",
                        "zeroRate": {
                            "value": 3.4858889232466828,
                            "unit": "Percentage"
                        },
                        "indexFixings": [
                            {
                                "accrualEndDate": "2033-09-22",
                                "accrualStartDate": "2032-09-22",
                                "couponRate": {
                                    "value": 3.8875713,
                                    "unit": "Percentage"
                                },
                                "fixingDate": "2032-09-22",
                                "forwardSource": "ZcCurve",
                                "referenceRate": {
                                    "value": 3.8875713,
                                    "unit": "Percentage"
                                },
                                "spreadBp": 0.0
                            }
                        ],
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2033-09-26"
                        },
                        "amount": {
                            "value": 394156.5378989731,
                            "currency": "USD"
                        },
                        "payer": "Party2",
                        "receiver": "Party1",
                        "occurrence": "Projected"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 4.0303711464608005,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.7298356640943585,
                        "startDate": "2033-09-22",
                        "endDate": "2034-09-22",
                        "remainingNotional": 10000000.0,
                        "interestRateType": "FloatingRate",
                        "zeroRate": {
                            "value": 3.552429625512943,
                            "unit": "Percentage"
                        },
                        "indexFixings": [
                            {
                                "accrualEndDate": "2034-09-22",
                                "accrualStartDate": "2033-09-22",
                                "couponRate": {
                                    "value": 4.030371,
                                    "unit": "Percentage"
                                },
                                "fixingDate": "2033-09-22",
                                "forwardSource": "ZcCurve",
                                "referenceRate": {
                                    "value": 4.030371,
                                    "unit": "Percentage"
                                },
                                "spreadBp": 0.0
                            }
                        ],
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2034-09-26"
                        },
                        "amount": {
                            "value": 408634.8523494978,
                            "currency": "USD"
                        },
                        "payer": "Party2",
                        "receiver": "Party1",
                        "occurrence": "Projected"
                    },
                    {
                        "paymentType": "Interest",
                        "annualRate": {
                            "value": 4.1440420754293,
                            "unit": "Percentage"
                        },
                        "discountFactor": 0.7004845173252519,
                        "startDate": "2034-09-22",
                        "endDate": "2035-09-24",
                        "remainingNotional": 0.0,
                        "interestRateType": "FloatingRate",
                        "zeroRate": {
                            "value": 3.6168900107566238,
                            "unit": "Percentage"
                        },
                        "indexFixings": [
                            {
                                "accrualEndDate": "2035-09-24",
                                "accrualStartDate": "2034-09-22",
                                "couponRate": {
                                    "value": 4.144042,
                                    "unit": "Percentage"
                                },
                                "fixingDate": "2034-09-22",
                                "forwardSource": "ZcCurve",
                                "referenceRate": {
                                    "value": 4.144042,
                                    "unit": "Percentage"
                                },
                                "spreadBp": 0.0
                            }
                        ],
                        "date": {
                            "dateType": "AdjustableDate",
                            "date": "2035-09-25"
                        },
                        "amount": {
                            "value": 422462.06713404256,
                            "currency": "USD"
                        },
                        "payer": "Party2",
                        "receiver": "Party1",
                        "occurrence": "Projected"
                    }
                ]
            }
        }

        """

        try:
            logger.info("Calling solve for irSwap with id")
            check_id(self._id)

            response = Client().ir_swap_resource.solve(
                instrument_id=self._id,
                fields=fields,
                pricing_preferences=pricing_preferences,
                market_data=market_data,
                return_market_data=return_market_data,
            )

            output = response.data
            logger.info("Called solve for irSwap with id")

            return output
        except Exception as err:
            logger.error("Error solve for irSwap with id.")
            check_exception_and_raise(err, logger)

    def value(
        self,
        *,
        pricing_preferences: Optional[IrPricingParameters] = None,
        market_data: Optional[MarketData] = None,
        return_market_data: Optional[bool] = None,
        fields: Optional[str] = None,
    ) -> IrSwapInstrumentValuationResponseFieldsOnResourceResponseData:
        """
        Calculate analytics for an interest rate swap stored on the platform, including valuation results, risk metrics, and other relevant measures.
        Provide an instrument ID in the request to perform the valuation.

        Parameters
        ----------
        pricing_preferences : IrPricingParameters, optional
            The parameters that control the computation of the analytics.
        market_data : MarketData, optional
            The market data used to compute the analytics.
        return_market_data : bool, optional
            Boolean property to determine if undelying market data used for calculation should be returned in the response
        fields : str, optional
            A parameter used to select the fields to return in response. If not provided, all fields will be returned.
            Some usage examples:
            1. Simply enumerating the fields, separating them by ',', e.g. 'fields=//please insert the selected fields here, e.g., field1, field2 //'
            2. Using parentheses to indicate nesting, e.g. 'fields= //please insert the selected field and subfields here, e.g., field1(subfield1, subfield2), field2(subfield3)//’
            3. Using forward slash '/' to indicate nesting, e.g. 'fields=//please insert the selected field and subfields here, e.g.,  field1/subfield1, field1/subfield2, field2/subfield3//’ (same result as example above)
            4. Operators can even be combined (forward slashes in brackets, not the way around), e.g. 'fields=//please insert the selected field and subfields here, e.g.,  field1(subfield1/subsubfield1), field2/subfield2//'

        Returns
        --------
        IrSwapInstrumentValuationResponseFieldsOnResourceResponseData


        Examples
        --------
        >>> # build the swap from 'LSEG/OIS_SOFR' template
        >>> fwd_start_sofr = create_from_vanilla_irs_template(template_reference = "LSEG/OIS_SOFR")
        >>>
        >>> # Swap needs to be saved in order for the value class method to be executable
        >>> fwd_start_sofr.save(name="sofr_fwd_start_swap_exm")
        >>>
        >>> # instantiate pricing parameters
        >>> pricing_parameters = IrPricingParameters()
        >>>
        >>> # solve the swap par rate
        >>> valuing_response_object = fwd_start_sofr.value(pricing_preferences=pricing_parameters)
        >>>
        >>> delete(name="sofr_fwd_start_swap_exm")
        >>>
        >>> print(js.dumps(valuation_response.analytics[0].valuation.as_dict(), indent=4))
        {
            "accrued": {
                "value": 0.0,
                "percent": 0.0,
                "dealCurrency": {
                    "value": 0.0,
                    "currency": "USD"
                },
                "reportCurrency": {
                    "value": 0.0,
                    "currency": "USD"
                }
            },
            "marketValue": {
                "value": 2988913.29413629,
                "dealCurrency": {
                    "value": 2988913.29413629,
                    "currency": "USD"
                },
                "reportCurrency": {
                    "value": 2988913.29413629,
                    "currency": "USD"
                }
            },
            "cleanMarketValue": {
                "value": 2988913.29413629,
                "dealCurrency": {
                    "value": 2988913.29413629,
                    "currency": "USD"
                },
                "reportCurrency": {
                    "value": 2988913.29413629,
                    "currency": "USD"
                }
            }
        }

        """

        try:
            logger.info("Calling value for irSwap with id")
            check_id(self._id)

            response = Client().ir_swap_resource.value(
                instrument_id=self._id,
                fields=fields,
                pricing_preferences=pricing_preferences,
                market_data=market_data,
                return_market_data=return_market_data,
            )

            output = response.data
            logger.info("Called value for irSwap with id")

            return output
        except Exception as err:
            logger.error("Error value for irSwap with id.")
            check_exception_and_raise(err, logger)

    def save(self, *, name: Optional[str] = None, space: Optional[str] = None) -> bool:
        """
        Save IrSwap instance in the platform store.

        Parameters
        ----------
        name : str, optional
            The IrSwap name. The name parameter must be specified when the object is first created. Thereafter it is optional. For first creation, name must follow the pattern '^[A-Za-z0-9_]{1,50}$'.
        space : str, optional
            The space where the IrSwap is stored. Space is like a namespace where resources are stored. By default there are two spaces:
            LSEG is reserved for LSEG maintained resources, HOME is reserved for user's default space. If space is not specified, HOME will be used.

        Returns
        --------
        bool, optional
            True, if saved successfully, otherwise None


        Examples
        --------
        >>> # build the swap from 'LSEG/OIS_SOFR' template
        >>> fwd_start_sofr = create_from_vanilla_irs_template(template_reference = "LSEG/OIS_SOFR")
        >>>
        >>> swap_id = "SOFR_OIS_1Y2Y"
        >>>
        >>> swap_space = "HOME"
        >>>
        >>> try:
        >>>     # If the instrument does not exist in HOME space, we can save it
        >>>     fwd_start_sofr.save(name=swap_id, space=swap_space)
        >>>     print(f"Instrument {swap_id} saved in {swap_space} space.")
        >>> except:
        >>>     # Check if the instrument already exists in HOME space
        >>>     fwd_start_sofr = load(name=swap_id, space=swap_space)
        >>>     print(f"Instrument {swap_id} already exists in {swap_space} space.")
        Instrument SOFR_OIS_1Y2Y saved in HOME space.

        """
        try:
            logger.info("Saving IrSwap")
            if self._id:
                if name and name != self._location.name or (space and space != self._location.space):
                    raise LibraryException("When saving an existing resource, you may not change the name or space")
                self._overwrite()
                logger.info("IrSwap saved")
            elif name:
                location = Location(name=name, space=space)
                self._create(location=location)
                logger.info(f"IrSwap saved to space: {self._location.space} name: {self._location.name}")
            else:
                raise LibraryException("When saving for the first time, name must be defined.")
            return True
        except Exception as err:
            logger.info("IrSwap save failed")
            check_exception_and_raise(err, logger)

    def clone(self) -> "IrSwap":
        """
        Return the same object, without id, name and space

        Parameters
        ----------


        Returns
        --------
        IrSwap
            The cloned IrSwap object


        Examples
        --------


        """
        definition = self._definition_class()
        definition._data = copy.deepcopy(self.definition._data)
        description = None
        if self.description:
            description = Description()
            description._data = copy.deepcopy(self.description._data)
        return self.__class__(definition=definition, description=description)
