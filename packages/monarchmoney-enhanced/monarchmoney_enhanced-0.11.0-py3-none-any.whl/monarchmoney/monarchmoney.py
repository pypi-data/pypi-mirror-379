import asyncio
import calendar
import getpass
import json
import os
import pickle
import random
import re
import time
import uuid
from datetime import date, datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple, Union

import oathtool
from aiohttp import ClientSession, FormData
from aiohttp.client import DEFAULT_TIMEOUT
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from graphql import DocumentNode

from .exceptions import (  # Legacy aliases for backward compatibility
    AuthenticationError,
    ClientError,
    ConfigurationError,
    DataError,
    GraphQLError,
    InvalidMFAError,
    LoginFailedException,
    MFARequiredError,
    MonarchMoneyError,
    NetworkError,
    RateLimitError,
    RequestFailedException,
    RequireMFAException,
    ServerError,
    SessionExpiredError,
    ValidationError,
    handle_graphql_errors,
    handle_http_response,
)
from .logging_config import logger
from .session_storage import LegacyPickleSession, SecureSessionStorage
from .validators import validate_login_credentials, validate_mfa_credentials

AUTH_HEADER_KEY = "authorization"
CSRF_KEY = "csrftoken"
DEFAULT_RECORD_LIMIT = 100
ERRORS_KEY = "error_code"
SESSION_DIR = ".mm"
SESSION_FILE = f"{SESSION_DIR}/mm_session.pickle"


class MonarchMoneyEndpoints(object):
    BASE_URL = "https://api.monarchmoney.com"

    @classmethod
    def getLoginEndpoint(cls) -> str:
        return cls.BASE_URL + "/auth/login/"

    @classmethod
    def getGraphQL(cls) -> str:
        return cls.BASE_URL + "/graphql"

    @classmethod
    def getAccountBalanceHistoryUploadEndpoint(cls) -> str:
        return cls.BASE_URL + "/account-balance-history/upload/"


async def retry_with_backoff(func, max_retries=3, base_delay=1.0, max_delay=60.0):
    """
    Retry function with exponential backoff using proper exception hierarchy.

    Args:
        func: Async function to retry
        max_retries: Maximum number of retry attempts
        base_delay: Base delay in seconds
        max_delay: Maximum delay in seconds

    Returns:
        Result of successful function call

    Raises:
        Original exception if all retries exhausted or non-retryable error
    """
    for attempt in range(max_retries + 1):
        try:
            return await func()
        except (AuthenticationError, ValidationError, ConfigurationError):
            # Don't retry authentication, validation, or config errors
            raise
        except RateLimitError as e:
            if attempt == max_retries:
                raise

            # Use retry_after from exception if available, otherwise calculate
            delay = e.retry_after or min(
                base_delay * (2**attempt) + random.uniform(0, 1), max_delay
            )
            logger.warning(
                "Rate limit exceeded, retrying",
                delay=delay,
                attempt=attempt + 1,
                max_retries=max_retries,
            )
            await asyncio.sleep(delay)
        except ServerError as e:
            if attempt == max_retries:
                raise

            # Shorter delay for server errors
            delay = min(
                base_delay * (1.5**attempt) + random.uniform(0, 0.5), max_delay / 2
            )
            logger.warning(
                "Server error, retrying",
                status_code=e.status_code,
                delay=delay,
                attempt=attempt + 1,
                max_retries=max_retries,
            )
            await asyncio.sleep(delay)
        except NetworkError as e:
            if attempt == max_retries:
                raise

            delay = min(base_delay * (2**attempt), max_delay)
            logger.warning(
                "Network error, retrying",
                delay=delay,
                attempt=attempt + 1,
                max_retries=max_retries,
            )
            await asyncio.sleep(delay)
        except Exception as e:
            # Convert unknown exceptions to appropriate types and handle retries
            error_str = str(e).lower()

            if any(code in error_str for code in ["401", "unauthorized"]):
                raise AuthenticationError("Authentication failed") from e
            elif "403" in error_str or "forbidden" in error_str:
                raise AuthenticationError("Access forbidden") from e
            elif "429" in error_str or "rate limit" in error_str:
                # Convert to RateLimitError but handle retry logic here
                if attempt == max_retries:
                    raise RateLimitError("Rate limit exceeded") from e

                delay = min(base_delay * (2**attempt) + random.uniform(0, 1), max_delay)
                logger.warning(
                    "Rate limit exceeded, retrying",
                    delay=delay,
                    attempt=attempt + 1,
                    max_retries=max_retries,
                )
                await asyncio.sleep(delay)
            elif any(code in error_str for code in ["500", "502", "503", "504"]):
                # Extract status code if possible
                status_match = re.search(r"\b(50[0-9])\b", error_str)
                status_code = int(status_match.group(1)) if status_match else 500

                if attempt == max_retries:
                    raise ServerError("Server error occurred", status_code) from e

                # Shorter delay for server errors
                delay = min(
                    base_delay * (1.5**attempt) + random.uniform(0, 0.5), max_delay / 2
                )
                logger.warning(
                    "Server error, retrying",
                    status_code=status_code,
                    delay=delay,
                    attempt=attempt + 1,
                    max_retries=max_retries,
                )
                await asyncio.sleep(delay)
            else:
                # Don't retry unknown errors
                raise


# Exception classes moved to exceptions.py
# Legacy classes are imported from exceptions.py for backward compatibility


class MonarchMoney(object):
    """
    Main MonarchMoney client for accessing Monarch Money API.

    Args:
        session_file: Path to session file for storing authentication tokens
        timeout: HTTP request timeout in seconds
        token: Optional pre-existing authentication token
        session_password: Password for session encryption
        use_encryption: Whether to encrypt session files
        debug: Enable enhanced debug logging for GraphQL requests and responses.
               When True, logs detailed information about all GraphQL operations
               including request variables, response data, and error details.
               Useful for troubleshooting API issues.

    Example:
        >>> # Enable debug logging for troubleshooting
        >>> mm = MonarchMoney(debug=True)
        >>> await mm.login_with_email("user@example.com", "password")
        >>> # All GraphQL operations will now log detailed debug information
    """

    def __init__(
        self,
        session_file: str = SESSION_FILE,
        timeout: int = 10,
        token: Optional[str] = None,
        session_password: Optional[str] = None,
        use_encryption: bool = True,
        debug: bool = False,
    ) -> None:
        self._headers = {
            "Accept": "application/json",
            "Client-Platform": "web",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "device-uuid": str(uuid.uuid4()),
            "Origin": "https://app.monarchmoney.com",
            "x-cio-client-platform": "web",
            "x-cio-site-id": "2598be4aa410159198b2",
            "x-gist-user-anonymous": "false",
        }
        if token:
            self._headers["Authorization"] = f"Token {token}"

        # Auto-detect the correct session file format
        self._session_file = self._resolve_session_file(session_file)
        self._token = token
        self._timeout = timeout
        self._csrf_token = None
        self._last_used = None
        self._session_password = session_password
        self._use_encryption = use_encryption
        self._debug = debug

        # Initialize secure session storage
        self._secure_storage = SecureSessionStorage(session_password, use_encryption)

        # Session metadata for validation and refresh
        self._session_created_at: Optional[float] = None
        self._session_last_validated: Optional[float] = None
        self._session_validation_interval = 7200  # Validate every 2 hours (conservative optimization)
        self._api_call_count_since_validation = 0  # Track activity for smart validation

        # Initialize services for service-oriented architecture
        from .services import (
            AccountService,
            AuthenticationService,
            BudgetService,
            GraphQLClient,
            InsightService,
            InvestmentService,
            SettingsService,
            TransactionService,
        )

        # Initialize advanced GraphQL client for performance optimizations
        self._graphql_client = GraphQLClient(self)

        # Initialize services
        self._auth_service = AuthenticationService(self)
        self._account_service = AccountService(self)
        self._transaction_service = TransactionService(self)
        self._settings_service = SettingsService(self)
        self._budget_service = BudgetService(self)
        self._investment_service = InvestmentService(self)
        self._insight_service = InsightService(self)

        # Initialize cache preloader for intelligent data preloading (lazy import to avoid circular import)
        self._cache_preloader = None

    @property
    def timeout(self) -> int:
        """The timeout, in seconds, for GraphQL calls."""
        return self._timeout

    def set_timeout(self, timeout_secs: int) -> None:
        """Sets the default timeout on GraphQL API calls, in seconds."""
        self._timeout = timeout_secs

    @property
    def token(self) -> Optional[str]:
        return self._token

    def set_token(self, token: str) -> None:
        self._token = token
        if self._headers is not None:
            self._headers["Authorization"] = f"Token {token}"

        # Initialize session metadata when token is set
        current_time = time.time()
        if not self._session_created_at:
            self._session_created_at = current_time
        self._session_last_validated = current_time

    def get_version(self) -> Dict[str, str]:
        """Get version information for the MonarchMoney library."""
        # Import version here to avoid circular imports
        from . import __version__

        return {
            "library_version": __version__,
            "library_name": "monarchmoney-enhanced",
            "session_active": self._token is not None,
            "session_file": self._session_file,
        }

    async def interactive_login(
        self, use_saved_session: bool = True, save_session: bool = True
    ) -> None:
        """Performs an interactive login for iPython and similar environments."""
        email = input("Email: ")
        passwd = getpass.getpass("Password: ")
        try:
            await self.login(email, passwd, use_saved_session, save_session)
        except RequireMFAException:
            await self.multi_factor_authenticate(
                email, passwd, input("Two Factor Code: ")
            )

        # Save session consistently regardless of MFA requirement
        if save_session:
            self.save_session(self._session_file)

    async def login(
        self,
        email: Optional[str] = None,
        password: Optional[str] = None,
        use_saved_session: bool = True,
        save_session: bool = True,
        mfa_secret_key: Optional[str] = None,
    ) -> None:
        """Logs into a Monarch Money account."""
        # Delegate to AuthenticationService
        await self._auth_service.login(
            email=email,
            password=password,
            use_saved_session=use_saved_session,
            save_session=save_session,
            mfa_secret_key=mfa_secret_key,
            session_file=self._session_file,
        )

    async def multi_factor_authenticate(
        self, email: str, password: str, code: str
    ) -> None:
        """Performs multi-factor authentication to access a Monarch Money account."""
        # Delegate to AuthenticationService
        await self._auth_service.multi_factor_authenticate(email, password, code)

    async def get_accounts(self) -> Dict[str, Any]:
        """
        Gets the list of accounts configured in the Monarch Money account.
        """
        # Delegate to AccountService
        return await self._account_service.get_accounts()

    async def get_accounts_basic(self) -> Dict[str, Any]:
        """
        Gets basic account information optimized for quick loading.
        Returns minimal account data for performance-critical scenarios.

        Returns:
            List of accounts with just essential fields (id, name, balance, type)
        """
        return await self._account_service.get_accounts_basic()

    async def get_accounts_balance_only(self) -> Dict[str, Any]:
        """
        Gets account balance information optimized for financial summaries.
        Returns account balances and essential metadata for net worth calculations.

        Returns:
            List of accounts with balance and net worth fields
        """
        return await self._account_service.get_accounts_balance_only()

    async def get_me(self) -> Dict[str, Any]:
        """
        Gets the current user's profile information including timezone, email, name, and authentication status.
        """
        # Delegate to SettingsService
        return await self._settings_service.get_me()

    async def get_merchants(self) -> Dict[str, Any]:
        """
        Gets the list of merchants that have transactions in the Monarch Money account.
        """
        query = gql(
            """
            query GetMerchantsSearch($search: String, $limit: Int, $includeIds: [ID!]) {
                merchants(
                    search: $search
                    limit: $limit
                    orderBy: TRANSACTION_COUNT
                    includeIds: $includeIds
                ) {
                    id
                    name
                    transactionCount
                    __typename
                }
            }
            """
        )
        return await self.gql_call(
            operation="GetMerchantsSearch",
            graphql_query=query,
            variables={"search": "", "limit": 100},
        )

    async def get_edit_merchant(self, merchant_id: str) -> Dict[str, Any]:
        """
        Get merchant information for editing, including recurring transaction settings.

        This method provides merchant information specifically designed for editing
        merchant settings, including whether the merchant has active recurring
        transaction streams and the details of those streams.

        Args:
            merchant_id: ID of the merchant to get edit information for

        Returns:
            Merchant edit information including:
            - Basic details (id, name, logoUrl)
            - Transaction and rule counts
            - Whether merchant can be deleted
            - Active recurring stream status and details

        Raises:
            LoginFailedException: If not authenticated
            ValidationError: If merchant_id is invalid

        Example:
            # Get merchant edit information
            edit_info = await mm.get_edit_merchant("104754400339336479")
            merchant = edit_info["merchant"]

            print(f"Merchant: {merchant['name']}")
            print(f"Transactions: {merchant['transactionCount']}")

            if merchant["hasActiveRecurringStreams"]:
                stream = merchant["recurringTransactionStream"]
                print(f"Recurring: {stream['frequency']} - ${stream['amount']}")
                # Can then mark as not recurring using the stream ID
                await mm.mark_stream_as_not_recurring(stream['id'])
        """
        return await self._transaction_service.get_edit_merchant(merchant_id)

    async def get_account_type_options(self) -> Dict[str, Any]:
        """
        Retrieves a list of available account types and their subtypes.
        """
        query = gql(
            """
            query GetAccountTypeOptions {
                accountTypeOptions {
                    type {
                        name
                        display
                        group
                        possibleSubtypes {
                            display
                            name
                            __typename
                        }
                        __typename
                    }
                    subtype {
                        name
                        display
                        __typename
                    }
                    __typename
                }
            }
        """
        )
        return await self.gql_call(
            operation="GetAccountTypeOptions",
            graphql_query=query,
        )

    async def get_recent_account_balances(
        self, start_date: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Retrieves the daily balance for all accounts starting from `start_date`.
        `start_date` is an ISO formatted datestring, e.g. YYYY-MM-DD.
        If `start_date` is None, then the last 31 days are requested.
        """
        if start_date is None:
            start_date = (date.today() - timedelta(days=31)).isoformat()

        query = gql(
            """
            query GetAccountRecentBalances($startDate: Date!) {
                accounts {
                    id
                    recentBalances(startDate: $startDate)
                    __typename
                }
            }
        """
        )
        return await self.gql_call(
            operation="GetAccountRecentBalances",
            graphql_query=query,
            variables={"startDate": start_date},
        )

    async def get_account_snapshots_by_type(self, start_date: str, timeframe: str):
        """
        Retrieves snapshots of the net values of all accounts of a given type, with either a yearly
        monthly granularity.
        `start_date` is an ISO datestring in the format YYYY-MM-DD, e.g. 2024-04-01,
        containing the date to begin the snapshots from
        `timeframe` is one of "year" or "month".

        Note, `month` in the snapshot results is not a full ISO datestring, as it doesn't include the day.
        Instead, it looks like, e.g., 2023-01
        """
        if timeframe not in ("year", "month"):
            raise ValidationError(
                f'Unknown timeframe "{timeframe}"',
                field="timeframe",
                details={"valid_values": ["year", "month"], "provided": timeframe},
            )

        query = gql(
            """
            query GetSnapshotsByAccountType($startDate: Date!, $timeframe: Timeframe!) {
                snapshotsByAccountType(startDate: $startDate, timeframe: $timeframe) {
                    accountType
                    month
                    balance
                    __typename
                }
                accountTypes {
                    name
                    group
                    __typename
                }
            }
        """
        )
        return await self.gql_call(
            operation="GetSnapshotsByAccountType",
            graphql_query=query,
            variables={"startDate": start_date, "timeframe": timeframe},
        )

    async def get_aggregate_snapshots(
        self,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        account_type: Optional[str] = None,
    ) -> dict:
        """
        Retrieves the daily net value of all accounts, optionally between `start_date` and `end_date`,
        and optionally only for accounts of type `account_type`.
        Both `start_date` and `end_date` are ISO datestrings, formatted as YYYY-MM-DD
        """
        query = gql(
            """
            query GetAggregateSnapshots($filters: AggregateSnapshotFilters) {
                aggregateSnapshots(filters: $filters) {
                    date
                    balance
                    __typename
                }
            }
        """
        )

        if start_date is None:
            # The mobile app defaults to 150 years ago today
            # The mobile app might have a leap year bug, so instead default to setting day=1
            today = date.today()
            start_date = date(
                year=today.year - 150, month=today.month, day=1
            ).isoformat()

        return await self.gql_call(
            operation="GetAggregateSnapshots",
            graphql_query=query,
            variables={
                "filters": {
                    "startDate": start_date,
                    "endDate": end_date,
                    "accountType": account_type,
                }
            },
        )

    async def get_net_worth_history(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        timeframe: str = "monthly",
    ) -> Dict[str, Any]:
        """
        Get net worth tracking over time with detailed breakdown.

        :param start_date: Start date in "yyyy-mm-dd" format (defaults to 1 year ago)
        :param end_date: End date in "yyyy-mm-dd" format (defaults to today)
        :param timeframe: Data aggregation timeframe ('daily', 'weekly', 'monthly', 'yearly')
        """
        query = gql(
            """
            query Web_GetAggregateSnapshots($filters: AggregateSnapshotFilters) {
                aggregateSnapshots(filters: $filters) {
                    date
                    balance
                    assetsBalance
                    liabilitiesBalance
                    __typename
                }
            }
            """
        )

        # Set default dates if not provided
        if not start_date:
            start_date = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")

        if not end_date:
            end_date = datetime.now().strftime("%Y-%m-%d")

        return await self.gql_call(
            operation="Web_GetAggregateSnapshots",
            graphql_query=query,
            variables={
                "filters": {
                    "startDate": start_date,
                    "endDate": end_date,
                    "accountType": None,
                    "useAdaptiveGranularity": True,
                }
            },
        )

    async def create_manual_account(
        self,
        account_type: str,
        account_sub_type: str,
        is_in_net_worth: bool,
        account_name: str,
        account_balance: float = 0,
    ) -> Dict[str, Any]:
        """
        Creates a new manual account

        :param account_type: The string of account group type (i.e. loan, other_liability, other_asset, etc)
        :param account_sub_type: The string sub type of the account (i.e. auto, commercial, mortgage, line_of_credit, etc)
        :param is_in_net_worth: A boolean if the account should be considered in the net worth calculation
        :param account_name: The string of the account name
        :param display_balance: a float of the amount of the account balance when the account is created
        """
        query = gql(
            """
            mutation Web_CreateManualAccount($input: CreateManualAccountMutationInput!) {
                createManualAccount(input: $input) {
                    account {
                        id
                        __typename
                    }
                    errors {
                        ...PayloadErrorFields
                        __typename
                    }
                __typename
               }
            }
            fragment PayloadErrorFields on PayloadError {
                fieldErrors {
                    field
                    messages
                    __typename
                }
                message
                code
                __typename
            }
            """
        )
        variables = {
            "input": {
                "type": account_type,
                "subtype": account_sub_type,
                "includeInNetWorth": is_in_net_worth,
                "name": account_name,
                "displayBalance": account_balance,
            },
        }

        return await self.gql_call(
            operation="Web_CreateManualAccount",
            graphql_query=query,
            variables=variables,
        )

    #
    async def update_account(
        self,
        account_id: str,
        account_name: Optional[str] = None,
        account_balance: Optional[float] = None,
        account_type: Optional[str] = None,
        account_sub_type: Optional[str] = None,
        include_in_net_worth: Optional[bool] = None,
        hide_from_summary_list: Optional[bool] = None,
        hide_transactions_from_reports: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """
        Updates the details of an account.

        With the exception of the account_balance parameter, the only available parameters currently are those
        that are valid for both synced and manual accounts.

        :param account_id: The string ID of the account to update
        :param account_name: The string of the account name
        :param account_balance: a float of the amount to update the account balance to
        :param account_type: The string of account group type (i.e. loan, other_liability, other_asset, etc)
        :param account_sub_type: The string sub type of the account (i.e. auto, commercial, mortgage, line_of_credit, etc)
        :param include_in_net_worth: A boolean if the account should be considered in the net worth calculation
        :param hide_from_summary_list: A boolean if the account should be hidden in the "Accounts" view
        :param hide_transactions_from_reports: A boolean if the account should be excluded from budgets and reports
        """
        query = gql(
            """
            mutation Common_UpdateAccount($input: UpdateAccountMutationInput!) {
                updateAccount(input: $input) {
                    account {
                        ...AccountFields
                        __typename
                    }
                    errors {
                        ...PayloadErrorFields
                        __typename
                    }
                    __typename
                }
            }

            fragment AccountFields on Account {
                id
                displayName
                syncDisabled
                deactivatedAt
                isHidden
                isAsset
                mask
                createdAt
                updatedAt
                displayLastUpdatedAt
                currentBalance
                displayBalance
                includeInNetWorth
                hideFromList
                hideTransactionsFromReports
                includeBalanceInNetWorth
                includeInGoalBalance
                dataProvider
                dataProviderAccountId
                isManual
                transactionsCount
                holdingsCount
                manualInvestmentsTrackingMethod
                order
                icon
                logoUrl
                deactivatedAt
                type {
                    name
                    display
                    group
                    __typename
                }
                subtype {
                    name
                    display
                    __typename
                }
                credential {
                    id
                    updateRequired
                    disconnectedFromDataProviderAt
                    dataProvider
                    institution {
                        id
                        plaidInstitutionId
                        name
                        status
                        __typename
                    }
                    __typename
                }
                institution {
                    id
                    name
                    primaryColor
                    url
                    __typename
                }
                __typename
            }

            fragment PayloadErrorFields on PayloadError {
                fieldErrors {
                    field
                    messages
                    __typename
                }
                message
                code
                __typename
            }
            """
        )

        variables = {
            "id": str(account_id),
        }

        if account_type is not None:
            variables["type"] = account_type
        if account_sub_type is not None:
            variables["subtype"] = account_sub_type
        if include_in_net_worth is not None:
            variables["includeInNetWorth"] = include_in_net_worth
        if hide_from_summary_list is not None:
            variables["hideFromList"] = hide_from_summary_list
        if hide_transactions_from_reports is not None:
            variables["hideTransactionsFromReports"] = hide_transactions_from_reports
        if account_name is not None:
            variables["name"] = account_name
        if account_balance is not None:
            variables["displayBalance"] = account_balance

        return await self.gql_call(
            operation="Common_UpdateAccount",
            graphql_query=query,
            variables={"input": variables},
        )

    async def delete_account(
        self,
        account_id: str,
    ) -> Dict[str, Any]:
        """
        Deletes an account
        """
        query = gql(
            """
            mutation Common_DeleteAccount($id: UUID!) {
                deleteAccount(id: $id) {
                    deleted
                    errors {
                    ...PayloadErrorFields
                    __typename
                }
                __typename
                }
            }
            fragment PayloadErrorFields on PayloadError {
                fieldErrors {
                    field
                    messages
                    __typename
                }
                message
                code
                __typename
            }
            """
        )

        variables = {"id": account_id}

        return await self.gql_call(
            operation="Common_DeleteAccount",
            graphql_query=query,
            variables=variables,
        )

    async def request_accounts_refresh(self, account_ids: List[str]) -> bool:
        """
        Requests Monarch to refresh account balances and transactions with
        source institutions.  Returns True if request was successfully started.

        Otherwise, throws a `RequestFailedException`.
        """
        query = gql(
            """
          mutation Common_ForceRefreshAccountsMutation($input: ForceRefreshAccountsInput!) {
            forceRefreshAccounts(input: $input) {
              success
              errors {
                ...PayloadErrorFields
                __typename
              }
              __typename
            }
          }

          fragment PayloadErrorFields on PayloadError {
            fieldErrors {
              field
              messages
              __typename
            }
            message
            code
            __typename
          }
          """
        )

        variables = {
            "input": {
                "accountIds": account_ids,
            },
        }

        response = await self.gql_call(
            operation="Common_ForceRefreshAccountsMutation",
            graphql_query=query,
            variables=variables,
        )

        if not response["forceRefreshAccounts"]["success"]:
            errors = response["forceRefreshAccounts"]["errors"]
            raise DataError(
                "Failed to refresh accounts",
                data_type="account_refresh",
                details={"errors": errors},
            )

        return True

    async def is_accounts_refresh_complete(
        self, account_ids: Optional[List[str]] = None
    ) -> bool:
        """
        Checks on the status of a prior request to refresh account balances.

        Returns:
          - True if refresh request is completed.
          - False if refresh request still in progress.

        Otherwise, throws a `RequestFailedException`.

        :param account_ids: The list of accounts IDs to check on the status of.
          If set to None, all account IDs will be checked.
        """
        query = gql(
            """
          query ForceRefreshAccountsQuery {
            accounts {
              id
              hasSyncInProgress
              __typename
            }
          }
          """
        )

        response = await self.gql_call(
            operation="ForceRefreshAccountsQuery",
            graphql_query=query,
            variables={},
        )

        if "accounts" not in response:
            raise RequestFailedException("Unable to request status of refresh")

        if account_ids:
            return all(
                [
                    not x["hasSyncInProgress"]
                    for x in response["accounts"]
                    if x["id"] in account_ids
                ]
            )
        else:
            return all([not x["hasSyncInProgress"] for x in response["accounts"]])

    async def request_accounts_refresh_and_wait(
        self,
        account_ids: Optional[List[str]] = None,
        timeout: int = 300,
        delay: int = 10,
    ) -> bool:
        """
        Convenience method for forcing an accounts refresh on Monarch, as well
        as waiting for the refresh to complete.

        Returns True if all accounts are refreshed within the timeout specified, False otherwise.

        :param account_ids: The list of accounts IDs to refresh.
          If set to None, all account IDs will be implicitly fetched.
        :param timeout: The number of seconds to wait for the refresh to complete
        :param delay: The number of seconds to wait for each check on the refresh request
        """
        if account_ids is None:
            account_data = await self.get_accounts()
            account_ids = [x["id"] for x in account_data["accounts"]]
        await self.request_accounts_refresh(account_ids)
        start = time.time()
        refreshed = False
        while not refreshed and (time.time() <= (start + timeout)):
            await asyncio.sleep(delay)
            refreshed = await self.is_accounts_refresh_complete(account_ids)
        return refreshed

    async def get_account_holdings(self, account_id: int) -> Dict[str, Any]:
        """
        Get the holdings information for a brokerage or similar type of account.
        """
        query = gql(
            """
          query Web_GetHoldings($input: PortfolioInput) {
            portfolio(input: $input) {
              aggregateHoldings {
                edges {
                  node {
                    id
                    quantity
                    basis
                    totalValue
                    securityPriceChangeDollars
                    securityPriceChangePercent
                    lastSyncedAt
                    holdings {
                      id
                      type
                      typeDisplay
                      name
                      ticker
                      closingPrice
                      isManual
                      closingPriceUpdatedAt
                      __typename
                    }
                    security {
                      id
                      name
                      type
                      ticker
                      typeDisplay
                      currentPrice
                      currentPriceUpdatedAt
                      closingPrice
                      closingPriceUpdatedAt
                      oneDayChangePercent
                      oneDayChangeDollars
                      __typename
                    }
                    __typename
                  }
                  __typename
                }
                __typename
              }
              __typename
            }
          }
        """
        )

        variables = {
            "input": {
                "accountIds": [str(account_id)],
                "endDate": datetime.today().strftime("%Y-%m-%d"),
                "includeHiddenHoldings": True,
                "startDate": (datetime.today() - timedelta(days=30)).strftime("%Y-%m-%d"),
            },
        }

        return await self.gql_call(
            operation="Web_GetHoldings",
            graphql_query=query,
            variables=variables,
        )

    async def get_security_details(self, ticker: str) -> Dict[str, Any]:
        """
        Get security details including the securityId needed for manual holdings.

        :param ticker: The stock ticker symbol to search for
        """
        query = gql(
            """
            query SecuritySearch($search: String!, $limit: Int, $orderByPopularity: Boolean) {
                securities(
                    search: $search
                    limit: $limit
                    orderByPopularity: $orderByPopularity
                ) {
                    id
                    name
                    ticker
                    currentPrice
                    __typename
                }
            }
            """
        )

        variables = {"search": ticker, "limit": 5, "orderByPopularity": True}

        return await self.gql_call(
            operation="SecuritySearch",
            graphql_query=query,
            variables=variables,
        )

    async def create_manual_holding(
        self,
        account_id: str,
        security_id: str,
        quantity: float,
    ) -> Dict[str, Any]:
        """
        Create a manual holding for an investment account.

        :param account_id: The account ID to add the holding to
        :param security_id: The security ID for the holding
        :param quantity: The quantity/number of shares
        """
        query = gql(
            """
            mutation Common_CreateManualHolding($input: CreateManualHoldingInput!) {
                createManualHolding(input: $input) {
                    holding {
                        id
                        ticker
                        __typename
                    }
                    errors {
                        message
                        code
                        __typename
                    }
                    __typename
                }
            }
            """
        )

        variables = {
            "input": {
                "accountId": account_id,
                "securityId": security_id,
                "quantity": quantity,
            }
        }

        return await self.gql_call(
            operation="Common_CreateManualHolding",
            graphql_query=query,
            variables=variables,
        )

    async def create_manual_holding_by_ticker(
        self,
        account_id: str,
        ticker: str,
        quantity: float,
    ) -> Dict[str, Any]:
        """
        Create a manual holding using a stock ticker symbol.

        :param account_id: The account ID to add the holding to
        :param ticker: The stock ticker symbol (e.g., 'AAPL', 'MSFT')
        :param quantity: The quantity/number of shares
        """
        try:
            security_response = await self.get_security_details(ticker)
            securities = security_response.get("securities", [])

            security = next(
                (sec for sec in securities if sec.get("ticker") == ticker), None
            )

            if not security:
                return {
                    "errors": [{"message": f"Security not found for ticker: {ticker}"}]
                }

            security_id = security.get("id")
            if not security_id:
                return {
                    "errors": [
                        {"message": f"Security ID not found for ticker: {ticker}"}
                    ]
                }

            return await self.create_manual_holding(account_id, security_id, quantity)

        except Exception as e:
            return {
                "errors": [
                    {"message": f"Failed to create holding for {ticker}: {str(e)}"}
                ]
            }

    async def delete_manual_holding(self, holding_id: str) -> bool:
        """
        Delete a manual holding.

        :param holding_id: The ID of the holding to delete
        :return: True if successfully deleted
        """
        query = gql(
            """
            mutation Common_DeleteHolding($id: ID!) {
                deleteHolding(id: $id) {
                    deleted
                    errors {
                        message
                        code
                        __typename
                    }
                    __typename
                }
            }
            """
        )

        variables = {"id": holding_id}

        response = await self.gql_call(
            operation="Common_DeleteHolding",
            graphql_query=query,
            variables=variables,
        )

        if not response["deleteHolding"]["deleted"]:
            raise RequestFailedException(str(response["deleteHolding"]["errors"]))

        return True

    async def get_account_history(self, account_id: int) -> Dict[str, Any]:
        """
        Gets historical account snapshot data for the requested account

        Args:
          account_id: Monarch account ID as an integer

        Returns:
          json object with all historical snapshots of requested account's balances
        """

        query = gql(
            """
            query AccountDetails_getAccount($id: UUID!, $filters: TransactionFilterInput) {
              account(id: $id) {
                id
                ...AccountFields
                ...EditAccountFormFields
                isLiability
                credential {
                  id
                  hasSyncInProgress
                  canBeForceRefreshed
                  disconnectedFromDataProviderAt
                  dataProvider
                  institution {
                    id
                    plaidInstitutionId
                    url
                    ...InstitutionStatusFields
                    __typename
                  }
                  __typename
                }
                institution {
                  id
                  plaidInstitutionId
                  url
                  ...InstitutionStatusFields
                  __typename
                }
                __typename
              }
              transactions: allTransactions(filters: $filters) {
                totalCount
                results(limit: 20) {
                  id
                  ...TransactionsListFields
                  __typename
                }
                __typename
              }
              snapshots: snapshotsForAccount(accountId: $id) {
                date
                signedBalance
                __typename
              }
            }

            fragment AccountFields on Account {
              id
              displayName
              syncDisabled
              deactivatedAt
              isHidden
              isAsset
              mask
              createdAt
              updatedAt
              displayLastUpdatedAt
              currentBalance
              displayBalance
              includeInNetWorth
              hideFromList
              hideTransactionsFromReports
              includeBalanceInNetWorth
              includeInGoalBalance
              dataProvider
              dataProviderAccountId
              isManual
              transactionsCount
              holdingsCount
              manualInvestmentsTrackingMethod
              order
              logoUrl
              type {
                name
                display
                group
                __typename
              }
              subtype {
                name
                display
                __typename
              }
              credential {
                id
                updateRequired
                disconnectedFromDataProviderAt
                dataProvider
                institution {
                  id
                  plaidInstitutionId
                  name
                  status
                  __typename
                }
                __typename
              }
              institution {
                id
                name
                primaryColor
                url
                __typename
              }
              __typename
            }

            fragment EditAccountFormFields on Account {
              id
              displayName
              deactivatedAt
              displayBalance
              includeInNetWorth
              hideFromList
              hideTransactionsFromReports
              dataProvider
              dataProviderAccountId
              isManual
              manualInvestmentsTrackingMethod
              isAsset
              invertSyncedBalance
              canInvertBalance
              type {
                name
                display
                __typename
              }
              subtype {
                name
                display
                __typename
              }
              __typename
            }

            fragment InstitutionStatusFields on Institution {
              id
              hasIssuesReported
              hasIssuesReportedMessage
              plaidStatus
              status
              balanceStatus
              transactionsStatus
              __typename
            }

            fragment TransactionsListFields on Transaction {
              id
              ...TransactionOverviewFields
              __typename
            }

            fragment TransactionOverviewFields on Transaction {
              id
              amount
              pending
              date
              hideFromReports
              plaidName
              notes
              isRecurring
              reviewStatus
              needsReview
              dataProviderDescription
              attachments {
                id
                __typename
              }
              isSplitTransaction
              category {
                id
                name
                group {
                  id
                  type
                  __typename
                }
                __typename
              }
              merchant {
                name
                id
                transactionsCount
                __typename
              }
              tags {
                id
                name
                color
                order
                __typename
              }
              __typename
            }
            """
        )

        variables = {"id": str(account_id)}

        account_details = await self.gql_call(
            operation="AccountDetails_getAccount",
            graphql_query=query,
            variables=variables,
        )

        # Parse JSON
        account_name = account_details["account"]["displayName"]
        account_balance_history = account_details["snapshots"]

        # Append account identification data to account balance history
        for i in account_balance_history:
            i.update(dict(accountId=str(account_id)))
            i.update(dict(accountName=account_name))

        return account_balance_history

    async def get_institutions(self) -> Dict[str, Any]:
        """
        Gets institution data from the account.
        """

        query = gql(
            """
            query Web_GetInstitutionSettings {
              credentials {
                id
                ...CredentialSettingsCardFields
                __typename
              }
              accounts(filters: {includeDeleted: true}) {
                id
                displayName
                subtype {
                  display
                  __typename
                }
                mask
                credential {
                  id
                  __typename
                }
                deletedAt
                __typename
              }
              subscription {
                isOnFreeTrial
                hasPremiumEntitlement
                __typename
              }
            }

            fragment CredentialSettingsCardFields on Credential {
              id
              updateRequired
              disconnectedFromDataProviderAt
              ...InstitutionInfoFields
              institution {
                id
                name
                url
                __typename
              }
              __typename
            }

            fragment InstitutionInfoFields on Credential {
              id
              displayLastUpdatedAt
              dataProvider
              updateRequired
              disconnectedFromDataProviderAt
              ...InstitutionLogoWithStatusFields
              institution {
                id
                name
                hasIssuesReported
                hasIssuesReportedMessage
                __typename
              }
              __typename
            }

            fragment InstitutionLogoWithStatusFields on Credential {
              dataProvider
              updateRequired
              institution {
                hasIssuesReported
                status
                balanceStatus
                transactionsStatus
                __typename
              }
              __typename
            }
        """
        )
        return await self.gql_call(
            operation="Web_GetInstitutionSettings",
            graphql_query=query,
        )

    async def get_budgets(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        use_legacy_goals: Optional[bool] = False,
        use_v2_goals: Optional[bool] = True,
    ) -> Dict[str, Any]:
        """
        Get your budgets and corresponding actual amounts from the account.

        When no date arguments given:
            | `start_date` will default to last month based on todays date
            | `end_date` will default to next month based on todays date

        :param start_date:
            the earliest date to get budget data, in "yyyy-mm-dd" format (default: last month)
        :param end_date:
            the latest date to get budget data, in "yyyy-mm-dd" format (default: next month)
        :param use_legacy_goals:
            Inoperative (plan to remove)
        :param use_v2_goals:
            Inoperative (paln to remove)
        """
        query = gql(
            """
            query Common_GetJointPlanningData($startDate: Date!, $endDate: Date!) {
              budgetSystem
              budgetData(startMonth: $startDate, endMonth: $endDate) {
                ...BudgetDataFields
                __typename
              }
              categoryGroups {
                ...BudgetCategoryGroupFields
                __typename
              }
              goalsV2 {
                ...BudgetDataGoalsV2Fields
                __typename
              }
            }

            fragment BudgetDataMonthlyAmountsFields on BudgetMonthlyAmounts {
              month
              plannedCashFlowAmount
              plannedSetAsideAmount
              actualAmount
              remainingAmount
              previousMonthRolloverAmount
              rolloverType
              cumulativeActualAmount
              rolloverTargetAmount
              __typename
            }

            fragment BudgetMonthlyAmountsByCategoryFields on BudgetCategoryMonthlyAmounts {
              category {
                id
                __typename
              }
              monthlyAmounts {
                ...BudgetDataMonthlyAmountsFields
                __typename
              }
              __typename
            }

            fragment BudgetMonthlyAmountsByCategoryGroupFields on BudgetCategoryGroupMonthlyAmounts {
              categoryGroup {
                id
                __typename
              }
              monthlyAmounts {
                ...BudgetDataMonthlyAmountsFields
                __typename
              }
              __typename
            }

            fragment BudgetMonthlyAmountsForFlexExpenseFields on BudgetFlexMonthlyAmounts {
              budgetVariability
              monthlyAmounts {
                ...BudgetDataMonthlyAmountsFields
                __typename
              }
              __typename
            }

            fragment BudgetDataTotalsByMonthFields on BudgetTotals {
              actualAmount
              plannedAmount
              previousMonthRolloverAmount
              remainingAmount
              __typename
            }

            fragment BudgetTotalsByMonthFields on BudgetMonthTotals {
              month
              totalIncome {
                ...BudgetDataTotalsByMonthFields
                __typename
              }
              totalExpenses {
                ...BudgetDataTotalsByMonthFields
                __typename
              }
              totalFixedExpenses {
                ...BudgetDataTotalsByMonthFields
                __typename
              }
              totalNonMonthlyExpenses {
                ...BudgetDataTotalsByMonthFields
                __typename
              }
              totalFlexibleExpenses {
                ...BudgetDataTotalsByMonthFields
                __typename
              }
              __typename
            }

            fragment BudgetRolloverPeriodFields on BudgetRolloverPeriod {
              id
              startMonth
              endMonth
              startingBalance
              targetAmount
              frequency
              type
              __typename
            }

            fragment BudgetCategoryFields on Category {
              id
              name
              icon
              order
              budgetVariability
              excludeFromBudget
              isSystemCategory
              updatedAt
              group {
                id
                type
                budgetVariability
                groupLevelBudgetingEnabled
                __typename
              }
              rolloverPeriod {
                ...BudgetRolloverPeriodFields
                __typename
              }
              __typename
            }

            fragment BudgetDataFields on BudgetData {
              monthlyAmountsByCategory {
                ...BudgetMonthlyAmountsByCategoryFields
                __typename
              }
              monthlyAmountsByCategoryGroup {
                ...BudgetMonthlyAmountsByCategoryGroupFields
                __typename
              }
              monthlyAmountsForFlexExpense {
                ...BudgetMonthlyAmountsForFlexExpenseFields
                __typename
              }
              totalsByMonth {
                ...BudgetTotalsByMonthFields
                __typename
              }
              __typename
            }

            fragment BudgetCategoryGroupFields on CategoryGroup {
              id
              name
              order
              type
              budgetVariability
              updatedAt
              groupLevelBudgetingEnabled
              categories {
                ...BudgetCategoryFields
                __typename
              }
              rolloverPeriod {
                id
                type
                startMonth
                endMonth
                startingBalance
                frequency
                targetAmount
                __typename
              }
              __typename
            }

            fragment BudgetDataGoalsV2Fields on GoalV2 {
              id
              name
              archivedAt
              completedAt
              priority
              imageStorageProvider
              imageStorageProviderId
              plannedContributions(startMonth: $startDate, endMonth: $endDate) {
                id
                month
                amount
                __typename
              }
              monthlyContributionSummaries(startMonth: $startDate, endMonth: $endDate) {
                month
                sum
                __typename
              }
              __typename
            }
            """
        )

        variables = {
            "startDate": start_date,
            "endDate": end_date,
        }

        if not start_date and not end_date:
            # Default start_date to last month and end_date to next month
            today = datetime.today()

            # Get the first day of last month
            last_month = today.month - 1
            last_month_year = today.year
            first_day_of_last_month = 1
            if last_month < 1:
                last_month_year -= 1
                last_month = 12
            variables["startDate"] = datetime(
                last_month_year, last_month, first_day_of_last_month
            ).strftime("%Y-%m-%d")

            # Get the last day of next month
            next_month = today.month + 1
            next_month_year = today.year
            if next_month > 12:
                next_month_year += 1
                next_month = 1
            last_day_of_next_month = calendar.monthrange(next_month_year, next_month)[1]
            variables["endDate"] = datetime(
                next_month_year, next_month, last_day_of_next_month
            ).strftime("%Y-%m-%d")

        elif bool(start_date) != bool(end_date):
            raise Exception(
                "You must specify both a startDate and endDate, not just one of them."
            )

        return await self.gql_call(
            operation="Common_GetJointPlanningData",
            graphql_query=query,
            variables=variables,
        )

    async def get_goals(self) -> Dict[str, Any]:
        """
        Get financial goals and targets from the account.
        """
        query = gql(
            """
            query GetGoalsV2 {
              goalsV2 {
                id
                name
                imageStorageProvider
                imageStorageProviderId
                __typename
              }
            }
            """
        )

        return await self.gql_call(
            operation="GetGoalsV2",
            graphql_query=query,
        )

    async def create_goal(
        self,
        name: str,
        target_amount: float,
        target_date: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Create a new financial goal.

        :param name: Goal name
        :param target_amount: Target amount for the goal
        :param target_date: Target date (YYYY-MM-DD format)
        :param description: Optional goal description
        :return: Created goal data
        """
        query = gql(
            """
            mutation CreateGoal($input: CreateGoalInput!) {
                createGoal(input: $input) {
                    goal {
                        id
                        name
                        targetAmount
                        currentAmount
                        targetDate
                        description
                        createdAt
                        __typename
                    }
                    errors {
                        ...PayloadErrorFields
                        __typename
                    }
                    __typename
                }
            }

            fragment PayloadErrorFields on PayloadError {
                fieldErrors {
                    field
                    messages
                    __typename
                }
                message
                code
                __typename
            }
            """
        )

        goal_input = {
            "name": name,
            "targetAmount": target_amount,
        }
        if target_date:
            goal_input["targetDate"] = target_date
        if description:
            goal_input["description"] = description

        variables = {"input": goal_input}

        result = await self.gql_call(
            operation="CreateGoal",
            graphql_query=query,
            variables=variables,
        )

        # Check for errors
        if result.get("createGoal", {}).get("errors"):
            errors = result["createGoal"]["errors"]
            if errors.get("message"):
                raise Exception(f"Goal creation failed: {errors['message']}")
            elif errors.get("fieldErrors"):
                field_errors = []
                for field_error in errors["fieldErrors"]:
                    field_errors.append(
                        f"{field_error['field']}: {', '.join(field_error['messages'])}"
                    )
                raise Exception(f"Goal creation failed: {'; '.join(field_errors)}")

        return result

    async def update_goal(
        self,
        goal_id: str,
        name: Optional[str] = None,
        target_amount: Optional[float] = None,
        target_date: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Update an existing financial goal.

        :param goal_id: ID of the goal to update
        :param name: New goal name
        :param target_amount: New target amount
        :param target_date: New target date (YYYY-MM-DD format)
        :param description: New description
        :return: Updated goal data
        """
        query = gql(
            """
            mutation UpdateGoal($input: UpdateGoalInput!) {
                updateGoal(input: $input) {
                    goal {
                        id
                        name
                        targetAmount
                        currentAmount
                        targetDate
                        description
                        updatedAt
                        __typename
                    }
                    errors {
                        ...PayloadErrorFields
                        __typename
                    }
                    __typename
                }
            }

            fragment PayloadErrorFields on PayloadError {
                fieldErrors {
                    field
                    messages
                    __typename
                }
                message
                code
                __typename
            }
            """
        )

        goal_input = {"id": goal_id}
        if name is not None:
            goal_input["name"] = name
        if target_amount is not None:
            goal_input["targetAmount"] = target_amount
        if target_date is not None:
            goal_input["targetDate"] = target_date
        if description is not None:
            goal_input["description"] = description

        variables = {"input": goal_input}

        result = await self.gql_call(
            operation="UpdateGoal",
            graphql_query=query,
            variables=variables,
        )

        # Check for errors
        if result.get("updateGoal", {}).get("errors"):
            errors = result["updateGoal"]["errors"]
            if errors.get("message"):
                raise Exception(f"Goal update failed: {errors['message']}")
            elif errors.get("fieldErrors"):
                field_errors = []
                for field_error in errors["fieldErrors"]:
                    field_errors.append(
                        f"{field_error['field']}: {', '.join(field_error['messages'])}"
                    )
                raise Exception(f"Goal update failed: {'; '.join(field_errors)}")

        return result

    async def delete_goal(self, goal_id: str) -> bool:
        """
        Delete a financial goal.

        :param goal_id: ID of the goal to delete
        :return: True if successfully deleted
        """
        query = gql(
            """
            mutation DeleteGoal($id: ID!) {
                deleteGoal(id: $id) {
                    deleted
                    errors {
                        ...PayloadErrorFields
                        __typename
                    }
                    __typename
                }
            }

            fragment PayloadErrorFields on PayloadError {
                fieldErrors {
                    field
                    messages
                    __typename
                }
                message
                code
                __typename
            }
            """
        )

        variables = {"id": goal_id}

        result = await self.gql_call(
            operation="DeleteGoal",
            graphql_query=query,
            variables=variables,
        )

        # Check for errors
        if result.get("deleteGoal", {}).get("errors"):
            errors = result["deleteGoal"]["errors"]
            if errors.get("message"):
                raise Exception(f"Goal deletion failed: {errors['message']}")

        return result.get("deleteGoal", {}).get("deleted", False)

    async def update_transaction_rule_retroactive(
        self,
        rule_data: Dict[str, Any],
        apply_to_existing_transactions: bool = True,
    ) -> Dict[str, Any]:
        """
        Update an existing transaction rule to apply retroactively.

        :param rule_data: Complete rule data from get_transaction_rules()
        :param apply_to_existing_transactions: Apply rule to existing transactions
        :return: Updated rule data
        """
        query = gql(
            """
            mutation Common_UpdateTransactionRuleMutationV2($input: UpdateTransactionRuleInput!) {
                updateTransactionRuleV2(input: $input) {
                    errors {
                        ...PayloadErrorFields
                        __typename
                    }
                    transactionRule {
                        id
                        name
                        categoryIds
                        accountIds
                        merchantCriteria {
                            operator
                            value
                            __typename
                        }
                        amountCriteria {
                            operator
                            value
                            isExpense
                            valueRange {
                                lower
                                upper
                                __typename
                            }
                            __typename
                        }
                        setCategoryAction
                        addTagsAction
                        applyToExistingTransactions
                        merchantCriteriaUseOriginalStatement
                        __typename
                    }
                    __typename
                }
            }

            fragment PayloadErrorFields on PayloadError {
                fieldErrors {
                    field
                    messages
                    __typename
                }
                message
                code
                __typename
            }
            """
        )

        # Clean function to remove __typename fields
        def clean_graphql_data(obj):
            if isinstance(obj, dict):
                return {
                    k: clean_graphql_data(v)
                    for k, v in obj.items()
                    if k != "__typename"
                }
            elif isinstance(obj, list):
                return [clean_graphql_data(item) for item in obj]
            return obj

        # Build rule input using existing rule data
        rule_input = {
            "id": rule_data.get("id"),
            "merchantCriteriaUseOriginalStatement": rule_data.get(
                "merchantCriteriaUseOriginalStatement", False
            ),
            "merchantCriteria": clean_graphql_data(
                rule_data.get("merchantCriteria", [])
            ),
            "amountCriteria": clean_graphql_data(rule_data.get("amountCriteria")),
            "categoryIds": rule_data.get("categoryIds"),
            "accountIds": rule_data.get("accountIds"),
            "reviewStatusAction": rule_data.get("reviewStatusAction"),
            "splitTransactionsAction": rule_data.get("splitTransactionsAction"),
            "applyToExistingTransactions": apply_to_existing_transactions,
        }

        # Handle setCategoryAction - it's returned as an object but needs to be sent as just the ID
        set_category_action = rule_data.get("setCategoryAction")
        if set_category_action:
            if isinstance(set_category_action, dict) and "id" in set_category_action:
                rule_input["setCategoryAction"] = set_category_action["id"]
            else:
                rule_input["setCategoryAction"] = set_category_action
        else:
            rule_input["setCategoryAction"] = None

        variables = {"input": rule_input}

        result = await self.gql_call(
            operation="Common_UpdateTransactionRuleMutationV2",
            graphql_query=query,
            variables=variables,
        )

        # Check for errors in the response
        errors = result.get("updateTransactionRuleV2", {}).get("errors")
        if errors and (errors.get("message") or errors.get("fieldErrors")):
            if errors.get("message"):
                raise Exception(f"Rule update failed: {errors['message']}")
            elif errors.get("fieldErrors"):
                field_errors = []
                for field_error in errors["fieldErrors"]:
                    field_errors.append(
                        f"{field_error['field']}: {', '.join(field_error['messages'])}"
                    )
                raise Exception(f"Rule update failed: {'; '.join(field_errors)}")

        # Return the updated transaction rule data
        rule_data = result.get("updateTransactionRuleV2", {}).get("transactionRule")
        if rule_data:
            return {"transactionRule": rule_data}
        else:
            return result

    async def apply_rules_to_existing_transactions(
        self, limit: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Apply all transaction rules to existing transactions retroactively.

        This works by updating each rule to set applyToExistingTransactions=true,
        which triggers the MonarchMoney backend to apply the rule retroactively.

        :param limit: Maximum number of rules to process (default: all)
        :return: Results of rule application
        """
        logger.info("Applying rules to existing transactions")

        # Step 1: Get all transaction rules
        logger.debug("Fetching transaction rules")
        rules_response = await self.get_transaction_rules()
        rules = rules_response.get("transactionRules", [])
        logger.info("Found transaction rules", rule_count=len(rules))

        if not rules:
            return {"processed": 0, "applied": 0, "message": "No rules to apply"}

        # Step 2: Apply each rule retroactively by updating it
        applied_count = 0
        processed_count = min(len(rules), limit) if limit else len(rules)

        logger.info(
            "Updating rules to apply retroactively", processed_count=processed_count
        )

        for i, rule in enumerate(rules[:processed_count]):
            rule_id = rule.get("id")
            if not rule_id:
                continue

            try:
                # Update the rule with applyToExistingTransactions=true
                await self.update_transaction_rule_retroactive(
                    rule_data=rule, apply_to_existing_transactions=True
                )
                applied_count += 1

                if i % 10 == 0:  # Progress update every 10 rules
                    logger.debug(
                        "Rule update progress", updated=i + 1, total=processed_count
                    )

            except Exception as e:
                logger.error("Failed to update rule", rule_id=rule_id, exc_info=e)
                continue

        logger.info(
            "Successfully applied rules to existing transactions",
            applied=applied_count,
            processed=processed_count,
        )

        return {
            "processed": processed_count,
            "applied": applied_count,
            "rules_count": len(rules),
            "message": f"Successfully applied {applied_count} rules to existing transactions using MonarchMoney API",
        }

    async def preview_transaction_rule(
        self, rule_config: Dict[str, Any], offset: int = 0, limit: int = 30
    ) -> Dict[str, Any]:
        """
        Preview which transactions would be affected by a transaction rule.

        Alternative implementation using existing working operations since the direct
        PreviewTransactionRule GraphQL operation has schema validation issues.

        :param rule_config: Rule configuration dict with criteria and actions
        :param offset: Pagination offset for results
        :param limit: Maximum results to return (default 30)
        :return: Preview of transactions that would be affected by the rule
        """
        logger.info("Previewing transaction rule matches using client-side logic")

        # Get recent transactions to match against
        transactions_response = await self.get_transactions(
            limit=limit * 5
        )  # Get more to filter
        transactions = transactions_response.get("transactions", [])

        matches = []

        # Simple client-side rule matching
        merchant_criteria = rule_config.get("merchantCriteria", [])
        amount_criteria = rule_config.get("amountCriteria")

        for transaction in transactions:
            match_found = True

            # Check merchant criteria
            if merchant_criteria:
                merchant_name = transaction.get("merchant", {}).get("name", "").lower()
                merchant_match = False

                for criteria in merchant_criteria:
                    if criteria.get("operator") == "contains":
                        search_value = criteria.get("value", "").lower()
                        if search_value in merchant_name:
                            merchant_match = True
                            break

                if not merchant_match:
                    match_found = False

            # Check amount criteria
            if amount_criteria and match_found:
                transaction_amount = abs(transaction.get("amount", 0))
                criteria_amount = amount_criteria.get("value", 0)
                operator = amount_criteria.get("operator", "eq")

                if operator == "eq" and transaction_amount != criteria_amount:
                    match_found = False
                elif operator == "gt" and transaction_amount <= criteria_amount:
                    match_found = False
                elif operator == "lt" and transaction_amount >= criteria_amount:
                    match_found = False

            if match_found:
                # Build preview result similar to what the API would return
                new_category = None
                if rule_config.get("setCategoryAction"):
                    # We'd need to lookup the category name, for now just use ID
                    new_category = {
                        "id": rule_config["setCategoryAction"],
                        "name": "New Category",
                        "icon": None,
                    }

                match_result = {
                    "transaction": transaction,
                    "newCategory": new_category,
                    "newTags": None,
                    "newGoal": None,
                    "newHideFromReports": None,
                    "newSplitTransactions": None,
                }

                matches.append(match_result)

                if len(matches) >= limit:
                    break

        # Apply offset
        matches = matches[offset : offset + limit] if offset < len(matches) else []

        result = {
            "transactionRulePreview": {"totalCount": len(matches), "results": matches}
        }

        logger.info("Found matching transactions", match_count=len(matches))
        return result

    async def get_investment_performance(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        account_ids: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        Get investment performance metrics and analytics using the real MonarchMoney API.

        Uses the Web_GetPortfolio GraphQL operation discovered from HAR analysis.

        :param start_date: Start date for performance analysis (YYYY-MM-DD, defaults to 30 days ago)
        :param end_date: End date for performance analysis (YYYY-MM-DD, defaults to today)
        :param account_ids: List of account IDs to include (default: all investment accounts)
        :return: Complete investment performance data from MonarchMoney API
        """
        from datetime import date, timedelta

        # Set default dates if not provided (30 days back)
        if not end_date:
            end_date = date.today().isoformat()
        if not start_date:
            start_date = (date.today() - timedelta(days=30)).isoformat()

        # Use the real Web_GetPortfolio GraphQL operation from HAR file
        query = gql(
            """
            query Web_GetPortfolio($portfolioInput: PortfolioInput) {
              portfolio(input: $portfolioInput) {
                performance {
                  totalValue
                  totalBasis
                  totalChangePercent
                  totalChangeDollars
                  oneDayChangePercent
                  historicalChart {
                    date
                    returnPercent
                    __typename
                  }
                  benchmarks {
                    security {
                      id
                      ticker
                      name
                      oneDayChangePercent
                      __typename
                    }
                    historicalChart {
                      date
                      returnPercent
                      __typename
                    }
                    __typename
                  }
                  __typename
                }
                aggregateHoldings {
                  edges {
                    node {
                      id
                      quantity
                      basis
                      totalValue
                      securityPriceChangeDollars
                      securityPriceChangePercent
                      lastSyncedAt
                      holdings {
                        id
                        type
                        typeDisplay
                        name
                        ticker
                        closingPrice
                        closingPriceUpdatedAt
                        quantity
                        value
                        account {
                          id
                          mask
                          icon
                          logoUrl
                          institution {
                            id
                            name
                            __typename
                          }
                          type {
                            name
                            display
                            __typename
                          }
                          subtype {
                            name
                            display
                            __typename
                          }
                          displayName
                          currentBalance
                          __typename
                        }
                        __typename
                      }
                      security {
                        id
                        name
                        ticker
                        currentPrice
                        currentPriceUpdatedAt
                        closingPrice
                        type
                        typeDisplay
                        __typename
                      }
                      __typename
                    }
                    __typename
                  }
                  __typename
                }
                __typename
              }
            }
        """
        )

        # Build portfolio input with date range
        variables = {"portfolioInput": {"startDate": start_date, "endDate": end_date}}

        # Add account filtering if specified
        if account_ids:
            variables["portfolioInput"]["accountIds"] = account_ids

        return await self.gql_call(
            operation="Web_GetPortfolio",
            graphql_query=query,
            variables=variables,
        )

    async def get_insights(self) -> Dict[str, Any]:
        """
        Get financial insights and recommendations.

        :return: Financial insights data
        """
        query = gql(
            """
            query GetInsights {
                insights {
                    id
                    type
                    title
                    description
                    category
                    priority
                    actionRequired
                    createdAt
                    dismissedAt
                    metadata
                    __typename
                }
            }
            """
        )

        return await self.gql_call(
            operation="GetInsights",
            graphql_query=query,
        )

    async def get_notifications(self) -> Dict[str, Any]:
        """
        Get account notifications and alerts.

        :return: Notifications data
        """
        query = gql(
            """
            query GetNotifications {
                notifications {
                    id
                    type
                    title
                    message
                    read
                    createdAt
                    updatedAt
                    actionUrl
                    metadata
                    __typename
                }
            }
            """
        )

        return await self.gql_call(
            operation="GetNotifications",
            graphql_query=query,
        )

    async def get_credit_score(self) -> Dict[str, Any]:
        """
        Get credit score monitoring data.

        :return: Credit score information
        """
        query = gql(
            """
            query GetCreditScore {
                creditScore {
                    score
                    provider
                    lastUpdated
                    trend
                    factors {
                        factor
                        impact
                        description
                        __typename
                    }
                    history {
                        date
                        score
                        __typename
                    }
                    __typename
                }
            }
            """
        )

        return await self.gql_call(
            operation="GetCreditScore",
            graphql_query=query,
        )

    async def get_settings(self) -> Dict[str, Any]:
        """
        Get user account settings and preferences.

        :return: User settings data
        """
        query = gql(
            """
            query GetSettings {
                settings {
                    timezone
                    currency
                    dateFormat
                    notifications {
                        email
                        push
                        sms
                        __typename
                    }
                    privacy {
                        dataSharing
                        analytics
                        __typename
                    }
                    __typename
                }
            }
            """
        )

        return await self.gql_call(
            operation="GetSettings",
            graphql_query=query,
        )

    async def update_settings(
        self,
        timezone: Optional[str] = None,
        currency: Optional[str] = None,
        date_format: Optional[str] = None,
        email_notifications: Optional[bool] = None,
        push_notifications: Optional[bool] = None,
        sms_notifications: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """
        Update user account settings and preferences.

        :param timezone: User timezone (e.g., "America/New_York")
        :param currency: Default currency (e.g., "USD")
        :param date_format: Date format preference
        :param email_notifications: Enable email notifications
        :param push_notifications: Enable push notifications
        :param sms_notifications: Enable SMS notifications
        :return: Updated settings data
        """
        query = gql(
            """
            mutation UpdateSettings($input: UpdateSettingsInput!) {
                updateSettings(input: $input) {
                    settings {
                        timezone
                        currency
                        dateFormat
                        notifications {
                            email
                            push
                            sms
                            __typename
                        }
                        __typename
                    }
                    errors {
                        ...PayloadErrorFields
                        __typename
                    }
                    __typename
                }
            }

            fragment PayloadErrorFields on PayloadError {
                fieldErrors {
                    field
                    messages
                    __typename
                }
                message
                code
                __typename
            }
            """
        )

        settings_input = {}
        if timezone is not None:
            settings_input["timezone"] = timezone
        if currency is not None:
            settings_input["currency"] = currency
        if date_format is not None:
            settings_input["dateFormat"] = date_format

        notifications = {}
        if email_notifications is not None:
            notifications["email"] = email_notifications
        if push_notifications is not None:
            notifications["push"] = push_notifications
        if sms_notifications is not None:
            notifications["sms"] = sms_notifications

        if notifications:
            settings_input["notifications"] = notifications

        variables = {"input": settings_input}

        result = await self.gql_call(
            operation="UpdateSettings",
            graphql_query=query,
            variables=variables,
        )

        # Check for errors
        if result.get("updateSettings", {}).get("errors"):
            errors = result["updateSettings"]["errors"]
            if errors.get("message"):
                raise Exception(f"Settings update failed: {errors['message']}")

        return result

    async def get_subscription_details(self) -> Dict[str, Any]:
        """
        The type of subscription for the Monarch Money account.
        """
        query = gql(
            """
          query GetSubscriptionDetails {
            subscription {
              id
              paymentSource
              referralCode
              isOnFreeTrial
              hasPremiumEntitlement
              __typename
            }
          }
        """
        )
        return await self.gql_call(
            operation="GetSubscriptionDetails",
            graphql_query=query,
        )

    async def get_transactions_summary(self) -> Dict[str, Any]:
        """
        Gets transactions summary from the account.
        """

        query = gql(
            """
            query GetTransactionsPage($filters: TransactionFilterInput) {
              aggregates(filters: $filters) {
                summary {
                  ...TransactionsSummaryFields
                  __typename
                }
                __typename
              }
            }

            fragment TransactionsSummaryFields on TransactionsSummary {
              avg
              count
              max
              maxExpense
              sum
              sumIncome
              sumExpense
              first
              last
              __typename
            }
        """
        )
        return await self.gql_call(
            operation="GetTransactionsPage",
            graphql_query=query,
        )

    async def get_transactions_summary_card(self) -> Dict[str, Any]:
        """
        Gets transactions summary card data from the account.
        This provides total transaction count information that may differ
        from get_transactions_summary due to different filtering logic.
        """
        query = gql(
            """
            query Web_GetTransactionsSummaryCard {
              transactionsSummaryCard {
                totalCount
                __typename
              }
            }
            """
        )

        return await self.gql_call(
            operation="Web_GetTransactionsSummaryCard",
            graphql_query=query,
        )

    async def get_transactions_list_dashboard(self) -> Dict[str, Any]:
        """
        Gets comprehensive transaction dashboard data from the account.
        This provides detailed transaction information with pagination, filtering,
        and aggregated summary data. More comprehensive than get_transactions_summary_card.

        Returns:
            Dict containing aggregates data with transaction summaries.
        """
        query = gql(
            """
            query GetTransactionsListDashboard($offset: Int, $limit: Int, $filters: TransactionFilterInput) {
              allTransactions(filters: $filters) {
                totalCount
                totalSelectableCount
                results(offset: $offset, limit: $limit) {
                  id
                  ...TransactionsListFields
                  __typename
                }
                __typename
              }
              transactionRules {
                id
                __typename
              }
              aggregates(filters: $filters) {
                summary {
                  count
                  __typename
                }
                __typename
              }
            }

            fragment TransactionOverviewFields on Transaction {
              id
              amount
              pending
              date
              hideFromReports
              hiddenByAccount
              plaidName
              notes
              isRecurring
              reviewStatus
              needsReview
              isSplitTransaction
              dataProviderDescription
              attachments {
                id
                __typename
              }
              goal {
                id
                name
                __typename
              }
              category {
                id
                name
                icon
                group {
                  id
                  type
                  __typename
                }
                __typename
              }
              merchant {
                name
                id
                transactionsCount
                logoUrl
                recurringTransactionStream {
                  frequency
                  isActive
                  __typename
                }
                __typename
              }
              tags {
                id
                name
                color
                order
                __typename
              }
              account {
                id
                displayName
                icon
                logoUrl
                __typename
              }
              __typename
            }

            fragment TransactionsListFields on Transaction {
              id
              ...TransactionOverviewFields
              __typename
            }
            """
        )
        response = await self.gql_call(
            operation="GetTransactionsListDashboard",
            graphql_query=query,
        )
        return response.get("data", response).get("aggregates")

    async def get_transactions(
        self,
        limit: int = DEFAULT_RECORD_LIMIT,
        offset: Optional[int] = 0,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        search: str = "",
        category_ids: Optional[List[str]] = None,
        account_ids: Optional[List[str]] = None,
        tag_ids: Optional[List[str]] = None,
        has_attachments: Optional[bool] = None,
        has_notes: Optional[bool] = None,
        hidden_from_reports: Optional[bool] = None,
        is_split: Optional[bool] = None,
        is_recurring: Optional[bool] = None,
        imported_from_mint: Optional[bool] = None,
        synced_from_institution: Optional[bool] = None,
        is_credit: Optional[bool] = None,
        abs_amount_range: Optional[Tuple[Optional[float], Optional[float]]] = None,
    ) -> Dict[str, Any]:
        """
        Gets transaction data from the account.

        :param limit: the maximum number of transactions to download, defaults to DEFAULT_RECORD_LIMIT.
        :param offset: the number of transactions to skip (offset) before retrieving results.
        :param start_date: the earliest date to get transactions from, in "yyyy-mm-dd" format.
        :param end_date: the latest date to get transactions from, in "yyyy-mm-dd" format.
        :param search: a string to filter transactions. use empty string for all results.
        :param category_ids: a list of category ids to filter.
        :param account_ids: a list of account ids to filter.
        :param tag_ids: a list of tag ids to filter.
        :param has_attachments: a bool to filter for whether the transactions have attachments.
        :param has_notes: a bool to filter for whether the transactions have notes.
        :param hidden_from_reports: a bool to filter for whether the transactions are hidden from reports.
        :param is_split: a bool to filter for whether the transactions are split.
        :param is_recurring: a bool to filter for whether the transactions are recurring.
        :param imported_from_mint: a bool to filter for whether the transactions were imported from mint.
        :param synced_from_institution: a bool to filter for whether the transactions were synced from an institution.
        :param is_credit: a bool to filter for credit transactions (positive amounts) vs debit transactions (negative amounts).
        :param abs_amount_range: a tuple of optional floats to filter by absolute amount range.
            Format: (min_amount, max_amount) where either value can be None.
            Example: (10.0, None) for amounts >= $10, (None, 100.0) for amounts <= $100.
        """

        query = gql(
            """
          query GetTransactionsList($offset: Int, $limit: Int, $filters: TransactionFilterInput, $orderBy: TransactionOrdering) {
            allTransactions(filters: $filters) {
              totalCount
              results(offset: $offset, limit: $limit, orderBy: $orderBy) {
                id
                ...TransactionOverviewFields
                __typename
              }
              __typename
            }
            transactionRules {
              id
              __typename
            }
          }

          fragment TransactionOverviewFields on Transaction {
            id
            amount
            pending
            date
            hideFromReports
            plaidName
            notes
            isRecurring
            reviewStatus
            needsReview
            attachments {
              id
              extension
              filename
              originalAssetUrl
              publicId
              sizeBytes
              __typename
            }
            isSplitTransaction
            createdAt
            updatedAt
            category {
              id
              name
              __typename
            }
            merchant {
              name
              id
              transactionsCount
              __typename
            }
            account {
              id
              displayName
              __typename
            }
            tags {
              id
              name
              color
              order
              __typename
            }
            __typename
          }
        """
        )

        variables = {
            "offset": offset,
            "limit": limit,
            "orderBy": "date",
            "filters": {
                "search": search,
                "categories": category_ids or [],
                "accounts": account_ids or [],
                "tags": tag_ids or [],
            },
        }

        # If bool filters are not defined (i.e. None), then it should not apply the filter
        if has_attachments is not None:
            variables["filters"]["hasAttachments"] = has_attachments

        if has_notes is not None:
            variables["filters"]["hasNotes"] = has_notes

        if hidden_from_reports is not None:
            variables["filters"]["hideFromReports"] = hidden_from_reports

        if is_recurring is not None:
            variables["filters"]["isRecurring"] = is_recurring

        if is_split is not None:
            variables["filters"]["isSplit"] = is_split

        if imported_from_mint is not None:
            variables["filters"]["importedFromMint"] = imported_from_mint

        if synced_from_institution is not None:
            variables["filters"]["syncedFromInstitution"] = synced_from_institution

        if is_credit is not None:
            variables["filters"]["isCredit"] = is_credit

        if abs_amount_range is not None:
            if len(abs_amount_range) != 2:
                raise ValueError(
                    "abs_amount_range must be a tuple of exactly 2 elements"
                )
            min_amount, max_amount = abs_amount_range
            if min_amount is not None:
                variables["filters"]["absAmountGte"] = min_amount
            if max_amount is not None:
                variables["filters"]["absAmountLte"] = max_amount

        if start_date and end_date:
            variables["filters"]["startDate"] = start_date
            variables["filters"]["endDate"] = end_date
        elif bool(start_date) != bool(end_date):
            raise Exception(
                "You must specify both a startDate and endDate, not just one of them."
            )

        return await self.gql_call(
            operation="GetTransactionsList", graphql_query=query, variables=variables
        )

    async def create_transaction(
        self,
        date: str,
        account_id: str,
        amount: float,
        merchant_name: str,
        category_id: str,
        notes: str = "",
        update_balance: bool = False,
    ) -> Dict[str, Any]:
        """
        Creates a transaction with the given parameters
        """
        query = gql(
            """
          mutation Common_CreateTransactionMutation($input: CreateTransactionMutationInput!) {
            createTransaction(input: $input) {
              errors {
                ...PayloadErrorFields
                __typename
              }
              transaction {
                id
              }
              __typename
            }
          }

          fragment PayloadErrorFields on PayloadError {
            fieldErrors {
              field
              messages
              __typename
            }
            message
            code
            __typename
          }
        """
        )

        variables = {
            "input": {
                "date": date,
                "accountId": account_id,
                "amount": round(amount, 2),
                "merchantName": merchant_name,
                "categoryId": category_id,
                "notes": notes,
                "shouldUpdateBalance": update_balance,
            }
        }

        return await self.gql_call(
            operation="Common_CreateTransactionMutation",
            graphql_query=query,
            variables=variables,
        )

    async def delete_transaction(self, transaction_id: str) -> bool:
        """
        Deletes the given transaction.

        :param transaction_id: the ID of the transaction targeted for deletion.
        """
        query = gql(
            """
          mutation Common_DeleteTransactionMutation($input: DeleteTransactionMutationInput!) {
            deleteTransaction(input: $input) {
              deleted
              errors {
                ...PayloadErrorFields
                __typename
              }
              __typename
            }
          }

          fragment PayloadErrorFields on PayloadError {
            fieldErrors {
              field
              messages
              __typename
            }
            message
            code
            __typename
          }
        """
        )

        variables = {
            "input": {
                "transactionId": transaction_id,
            },
        }

        response = await self.gql_call(
            operation="Common_DeleteTransactionMutation",
            graphql_query=query,
            variables=variables,
        )

        if not response["deleteTransaction"]["deleted"]:
            raise RequestFailedException(response["deleteTransaction"]["errors"])

        return True

    async def get_transaction_rules(self) -> Dict[str, Any]:
        """
        Gets all transaction rules configured in the account.
        Rules are returned in their priority order.
        """
        query = gql(
            """
            query GetTransactionRules {
                transactionRules {
                    id
                    order
                    ...TransactionRuleFields
                    __typename
                }
            }

            fragment TransactionRuleFields on TransactionRuleV2 {
                id
                merchantCriteriaUseOriginalStatement
                merchantCriteria {
                    operator
                    value
                    __typename
                }
                amountCriteria {
                    operator
                    isExpense
                    value
                    valueRange {
                        lower
                        upper
                        __typename
                    }
                    __typename
                }
                categoryIds
                accountIds
                categories {
                    id
                    name
                    icon
                    __typename
                }
                accounts {
                    id
                    displayName
                    icon
                    logoUrl
                    __typename
                }
                setMerchantAction {
                    id
                    name
                    __typename
                }
                setCategoryAction {
                    id
                    name
                    icon
                    __typename
                }
                addTagsAction {
                    id
                    name
                    color
                    __typename
                }
                linkGoalAction {
                    id
                    name
                    imageStorageProvider
                    imageStorageProviderId
                    __typename
                }
                needsReviewByUserAction {
                    id
                    name
                    __typename
                }
                unassignNeedsReviewByUserAction
                sendNotificationAction
                setHideFromReportsAction
                reviewStatusAction
                recentApplicationCount
                lastAppliedAt
                splitTransactionsAction {
                    amountType
                    splitsInfo {
                        categoryId
                        merchantName
                        amount
                        goalId
                        tags
                        hideFromReports
                        reviewStatus
                        needsReviewByUserId
                        __typename
                    }
                    __typename
                }
                __typename
            }
            """
        )

        return await self.gql_call(
            operation="GetTransactionRules",
            graphql_query=query,
        )

    async def create_transaction_rule(
        self,
        merchant_criteria: Optional[List[Dict[str, str]]] = None,
        amount_criteria: Optional[Dict[str, Any]] = None,
        category_ids: Optional[List[str]] = None,
        account_ids: Optional[List[str]] = None,
        set_category_action: Optional[str] = None,
        add_tags_action: Optional[List[str]] = None,
        set_merchant_action: Optional[str] = None,
        split_transactions_action: Optional[Dict[str, Any]] = None,
        apply_to_existing_transactions: bool = False,
        merchant_criteria_use_original_statement: bool = False,
        # New advanced action parameters
        set_hide_from_reports_action: Optional[bool] = None,
        needs_review_by_user_action: Optional[str] = None,
        unassign_needs_review_by_user_action: Optional[bool] = None,
        send_notification_action: Optional[bool] = None,
        review_status_action: Optional[str] = None,
        link_goal_action: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Creates a new transaction rule for automatic categorization and actions.

        :param merchant_criteria: List of merchant criteria [{"operator": "contains", "value": "amazon"}]
        :param amount_criteria: Amount criteria {"operator": "eq", "isExpense": True, "value": 115.32}
                               For exact amounts: {"operator": "eq", "value": 115.32}
                               For ranges: {"operator": "between", "valueRange": {"lower": 100, "upper": 200}}
        :param category_ids: List of category IDs to match
        :param account_ids: List of account IDs to match
        :param set_category_action: Category ID to set when rule matches
        :param add_tags_action: List of tag IDs to add when rule matches
        :param set_merchant_action: Merchant ID to set when rule matches
        :param split_transactions_action: Split action configuration
        :param apply_to_existing_transactions: Whether to apply to existing transactions
        :param merchant_criteria_use_original_statement: Use original statement text
        :param set_hide_from_reports_action: Hide transactions from reports (True/False)
        :param needs_review_by_user_action: User ID to assign for review
        :param unassign_needs_review_by_user_action: Remove review assignment (True/False)
        :param send_notification_action: Send notification when rule applies (True/False)
        :param review_status_action: Set review status (e.g., "tax_deductible")
        :param link_goal_action: Goal ID to link transactions to
        :return: The created rule data
        """
        query = gql(
            """
            mutation Common_CreateTransactionRuleMutationV2($input: CreateTransactionRuleInput!) {
                createTransactionRuleV2(input: $input) {
                    errors {
                        ...PayloadErrorFields
                        __typename
                    }
                    transactionRule {
                        id
                        __typename
                    }
                    __typename
                }
            }

            fragment PayloadErrorFields on PayloadError {
                fieldErrors {
                    field
                    messages
                    __typename
                }
                message
                code
                __typename
            }
            """
        )

        # Build rule input matching the exact structure from working HAR file
        rule_input = {
            "categoryIds": category_ids,
            "accountIds": account_ids,
            "merchantCriteria": merchant_criteria,
            "amountCriteria": amount_criteria,
            "merchantCriteriaUseOriginalStatement": merchant_criteria_use_original_statement,
            "addTagsAction": add_tags_action,
            "splitTransactionsAction": split_transactions_action,
            "applyToExistingTransactions": apply_to_existing_transactions,
            "setCategoryAction": set_category_action,
        }

        variables = {"input": rule_input}

        result = await self.gql_call(
            operation="Common_CreateTransactionRuleMutationV2",
            graphql_query=query,
            variables=variables,
        )

        # Check for GraphQL errors in the response
        errors = result.get("createTransactionRuleV2", {}).get("errors")
        if errors:
            # Only treat as error if there are actual error messages
            if errors.get("message"):
                raise Exception(
                    f"Transaction rule creation failed: {errors['message']}"
                )
            elif errors.get("fieldErrors"):
                field_errors = []
                for field_error in errors["fieldErrors"]:
                    field_errors.append(
                        f"{field_error['field']}: {', '.join(field_error['messages'])}"
                    )
                raise Exception(
                    f"Transaction rule creation failed: {'; '.join(field_errors)}"
                )
            # If errors object exists but all fields are None/empty, it means success

        # Return the created transaction rule data
        rule_data = result.get("createTransactionRuleV2", {}).get("transactionRule")
        if rule_data:
            return {"transactionRule": rule_data}
        else:
            return result

    async def update_transaction_rule(
        self,
        rule_id: str,
        merchant_criteria: Optional[List[Dict[str, str]]] = None,
        amount_criteria: Optional[Dict[str, Any]] = None,
        category_ids: Optional[List[str]] = None,
        account_ids: Optional[List[str]] = None,
        set_category_action: Optional[str] = None,
        add_tags_action: Optional[List[str]] = None,
        set_merchant_action: Optional[str] = None,
        split_transactions_action: Optional[Dict[str, Any]] = None,
        apply_to_existing_transactions: Optional[bool] = None,
        merchant_criteria_use_original_statement: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """
        Updates an existing transaction rule.

        :param rule_id: The ID of the rule to update
        :param merchant_criteria: List of merchant criteria [{"operator": "contains", "value": "amazon"}]
        :param amount_criteria: Amount criteria {"operator": "gt", "isExpense": True, "value": 20}
        :param category_ids: List of category IDs to match
        :param account_ids: List of account IDs to match
        :param set_category_action: Category ID to set when rule matches
        :param add_tags_action: List of tag IDs to add when rule matches
        :param set_merchant_action: Merchant ID to set when rule matches
        :param split_transactions_action: Split action configuration
        :param apply_to_existing_transactions: Whether to apply to existing transactions
        :param merchant_criteria_use_original_statement: Use original statement text
        :return: The updated rule data
        """
        query = gql(
            """
            mutation Common_UpdateTransactionRuleMutationV2($input: UpdateTransactionRuleInput!) {
                updateTransactionRuleV2(input: $input) {
                    errors {
                        ...PayloadErrorFields
                        __typename
                    }
                    transactionRule {
                        id
                        name
                        categoryIds
                        accountIds
                        merchantCriteria {
                            operator
                            value
                            __typename
                        }
                        amountCriteria {
                            operator
                            value
                            isExpense
                            valueRange {
                                lower
                                upper
                                __typename
                            }
                            __typename
                        }
                        setCategoryAction
                        addTagsAction
                        applyToExistingTransactions
                        merchantCriteriaUseOriginalStatement
                        __typename
                    }
                    __typename
                }
            }

            fragment PayloadErrorFields on PayloadError {
                fieldErrors {
                    field
                    messages
                    __typename
                }
                message
                code
                __typename
            }
            """
        )

        rule_input = {"id": rule_id}

        if merchant_criteria is not None:
            rule_input["merchantCriteria"] = merchant_criteria
        if amount_criteria is not None:
            rule_input["amountCriteria"] = amount_criteria
        if category_ids is not None:
            rule_input["categoryIds"] = category_ids
        if account_ids is not None:
            rule_input["accountIds"] = account_ids
        if set_category_action is not None:
            rule_input["setCategoryAction"] = set_category_action
        if add_tags_action is not None:
            rule_input["addTagsAction"] = add_tags_action
        if set_merchant_action is not None:
            rule_input["setMerchantAction"] = set_merchant_action
        if split_transactions_action is not None:
            rule_input["splitTransactionsAction"] = split_transactions_action
        if apply_to_existing_transactions is not None:
            rule_input["applyToExistingTransactions"] = apply_to_existing_transactions
        if merchant_criteria_use_original_statement is not None:
            rule_input["merchantCriteriaUseOriginalStatement"] = (
                merchant_criteria_use_original_statement
            )

        variables = {"input": rule_input}

        result = await self.gql_call(
            operation="Common_UpdateTransactionRuleMutationV2",
            graphql_query=query,
            variables=variables,
        )

        # Check for errors in the response
        errors = result.get("updateTransactionRuleV2", {}).get("errors")
        if errors and (errors.get("message") or errors.get("fieldErrors")):
            if errors.get("message"):
                raise Exception(f"Rule update failed: {errors['message']}")
            elif errors.get("fieldErrors"):
                field_errors = []
                for field_error in errors["fieldErrors"]:
                    field_errors.append(
                        f"{field_error['field']}: {', '.join(field_error['messages'])}"
                    )
                raise Exception(f"Rule update failed: {'; '.join(field_errors)}")

        # Return the updated transaction rule data
        rule_data = result.get("updateTransactionRuleV2", {}).get("transactionRule")
        if rule_data:
            return {"transactionRule": rule_data}
        else:
            return result

    async def delete_transaction_rule(self, rule_id: str) -> bool:
        """
        Deletes a transaction rule.

        :param rule_id: The ID of the rule to delete
        :return: True if successfully deleted
        """
        query = gql(
            """
            mutation Common_DeleteTransactionRule($id: ID!) {
                deleteTransactionRule(id: $id) {
                    deleted
                    errors {
                        ...PayloadErrorFields
                        __typename
                    }
                    __typename
                }
            }

            fragment PayloadErrorFields on PayloadError {
                fieldErrors {
                    field
                    messages
                    __typename
                }
                message
                code
                __typename
            }
            """
        )

        variables = {"id": rule_id}

        result = await self.gql_call(
            operation="Common_DeleteTransactionRule",
            graphql_query=query,
            variables=variables,
        )

        return result.get("deleteTransactionRule", {}).get("deleted", False)

    async def reorder_transaction_rules(
        self, rule_id: str, new_order: int
    ) -> Dict[str, Any]:
        """
        Updates the order of a transaction rule.

        :param rule_id: The ID of the rule to reorder
        :param new_order: The new order position for the rule
        :return: The updated rules data
        """
        query = gql(
            """
            mutation Web_UpdateRuleOrderMutation($id: ID!, $order: Int!) {
                updateTransactionRuleOrderV2(id: $id, order: $order) {
                    transactionRules {
                        id
                        order
                        merchantCriteria {
                            operator
                            value
                            __typename
                        }
                        setCategoryAction {
                            id
                            name
                            icon
                            __typename
                        }
                        __typename
                    }
                    __typename
                }
            }
            """
        )

        variables = {"id": rule_id, "order": new_order}

        return await self.gql_call(
            operation="Web_UpdateRuleOrderMutation",
            graphql_query=query,
            variables=variables,
        )

    async def create_categorization_rule(
        self,
        merchant_contains: str,
        category_name: str,
        apply_to_existing: bool = False,
    ) -> Dict[str, Any]:
        """
        Helper method to create a simple categorization rule.

        :param merchant_contains: Merchant name pattern to match (case-insensitive contains)
        :param category_name: Name of the category to assign
        :param apply_to_existing: Whether to apply to existing transactions
        :return: The created rule data
        """
        categories = await self.get_transaction_categories()
        category_id = None

        for cat in categories.get("categories", []):
            if cat.get("name", "").lower() == category_name.lower():
                category_id = cat.get("id")
                break

        if not category_id:
            raise ValueError(f"Category '{category_name}' not found")

        merchant_criteria = [{"operator": "contains", "value": merchant_contains}]

        return await self.create_transaction_rule(
            merchant_criteria=merchant_criteria,
            set_category_action=category_id,
            apply_to_existing_transactions=apply_to_existing,
        )

    async def create_amount_rule(
        self,
        amount: float,
        operator: str = "eq",
        is_expense: bool = True,
        category_name: Optional[str] = None,
        set_category_action: Optional[str] = None,
        apply_to_existing: bool = False,
    ) -> Dict[str, Any]:
        """
        Helper method to create an amount-based rule.

        :param amount: Exact amount to match (e.g., 115.32)
        :param operator: Amount operator ("eq" for exact, "gt", "lt", "between")
        :param is_expense: True for expenses (negative), False for income (positive)
        :param category_name: Name of category to assign (alternative to set_category_action)
        :param set_category_action: Category ID to assign directly
        :param apply_to_existing: Whether to apply to existing transactions
        :return: Created rule data
        """
        if category_name and not set_category_action:
            categories = await self.get_transaction_categories()
            for cat in categories.get("categories", []):
                if cat.get("name", "").lower() == category_name.lower():
                    set_category_action = cat.get("id")
                    break
            if not set_category_action:
                raise ValueError(f"Category '{category_name}' not found")

        amount_criteria = {
            "operator": operator,
            "isExpense": is_expense,
            "value": amount,
        }

        return await self.create_transaction_rule(
            amount_criteria=amount_criteria,
            set_category_action=set_category_action,
            apply_to_existing_transactions=apply_to_existing,
        )

    async def create_combined_rule(
        self,
        merchant_contains: str,
        amount: Optional[float] = None,
        amount_operator: str = "gt",
        category_name: Optional[str] = None,
        set_category_action: Optional[str] = None,
        apply_to_existing: bool = False,
    ) -> Dict[str, Any]:
        """
        Helper method to create combined merchant + amount rules.

        :param merchant_contains: Merchant name pattern to match
        :param amount: Amount threshold (e.g., 200 for "> $200")
        :param amount_operator: Amount comparison ("gt", "lt", "eq", "greater_than", "less_than", "equals")
        :param category_name: Name of category to assign
        :param set_category_action: Category ID to assign directly
        :param apply_to_existing: Whether to apply to existing transactions
        :return: Created rule data
        """
        if category_name and not set_category_action:
            categories = await self.get_transaction_categories()
            for cat in categories.get("categories", []):
                if cat.get("name", "").lower() == category_name.lower():
                    set_category_action = cat.get("id")
                    break
            if not set_category_action:
                raise ValueError(f"Category '{category_name}' not found")

        # Map user-friendly operator names to GraphQL operators
        operator_mapping = {
            "greater_than": "gt",
            "less_than": "lt",
            "equals": "eq",
            "equal": "eq",
            "gt": "gt",
            "lt": "lt",
            "eq": "eq",
        }

        mapped_operator = operator_mapping.get(amount_operator.lower(), amount_operator)

        merchant_criteria = [{"operator": "contains", "value": merchant_contains}]
        amount_criteria = None
        if amount:
            amount_criteria = {
                "operator": mapped_operator,
                "isExpense": True,
                "value": amount,
            }

        return await self.create_transaction_rule(
            merchant_criteria=merchant_criteria,
            amount_criteria=amount_criteria,
            set_category_action=set_category_action,
            apply_to_existing_transactions=apply_to_existing,
        )

    async def create_tax_deductible_rule(
        self,
        merchant_contains: Optional[str] = None,
        amount: Optional[float] = None,
        amount_operator: str = "gt",
        apply_to_existing: bool = False,
    ) -> Dict[str, Any]:
        """
        Helper method to create tax-deductible marking rules.

        :param merchant_contains: Merchant pattern to match
        :param amount: Amount threshold
        :param amount_operator: Amount comparison operator
        :param apply_to_existing: Whether to apply to existing transactions
        :return: Created rule data
        """
        merchant_criteria = None
        if merchant_contains:
            merchant_criteria = [{"operator": "contains", "value": merchant_contains}]

        amount_criteria = None
        if amount:
            amount_criteria = {
                "operator": amount_operator,
                "isExpense": True,
                "value": amount,
            }

        # Tax deductible functionality requires a tag rather than review status
        # For now, create the rule without the tax deductible marking
        # Users can manually add tags after rule creation
        return await self.create_transaction_rule(
            merchant_criteria=merchant_criteria,
            amount_criteria=amount_criteria,
            apply_to_existing_transactions=apply_to_existing,
        )

    async def create_ignore_rule(
        self,
        merchant_contains: Optional[str] = None,
        amount: Optional[float] = None,
        amount_operator: str = "eq",
        apply_to_existing: bool = False,
    ) -> Dict[str, Any]:
        """
        Helper method to create "ignore from everything" rules.

        :param merchant_contains: Merchant pattern to match
        :param amount: Exact amount to match
        :param amount_operator: Amount comparison operator
        :param apply_to_existing: Whether to apply to existing transactions
        :return: Created rule data
        """
        merchant_criteria = None
        if merchant_contains:
            merchant_criteria = [{"operator": "contains", "value": merchant_contains}]

        amount_criteria = None
        if amount:
            amount_criteria = {
                "operator": amount_operator,
                "isExpense": True,
                "value": amount,
            }

        return await self.create_transaction_rule(
            merchant_criteria=merchant_criteria,
            amount_criteria=amount_criteria,
            set_hide_from_reports_action=True,
            apply_to_existing_transactions=apply_to_existing,
        )

    async def preview_transaction_rule(
        self,
        merchant_criteria: Optional[List[Dict[str, str]]] = None,
        amount_criteria: Optional[Dict[str, Any]] = None,
        category_ids: Optional[List[str]] = None,
        account_ids: Optional[List[str]] = None,
        set_category_action: Optional[str] = None,
        add_tags_action: Optional[List[str]] = None,
        set_merchant_action: Optional[str] = None,
        split_transactions_action: Optional[Dict[str, Any]] = None,
        apply_to_existing_transactions: bool = False,
        merchant_criteria_use_original_statement: bool = False,
        offset: int = 0,
    ) -> Dict[str, Any]:
        """
        Previews what transactions would be affected by a rule before creating it.

        :param merchant_criteria: List of merchant criteria [{"operator": "contains", "value": "amazon"}]
        :param amount_criteria: Amount criteria {"operator": "gt", "isExpense": True, "value": 20}
        :param category_ids: List of category IDs to match
        :param account_ids: List of account IDs to match
        :param set_category_action: Category ID to set when rule matches
        :param add_tags_action: List of tag IDs to add when rule matches
        :param set_merchant_action: Merchant ID to set when rule matches
        :param split_transactions_action: Split action configuration
        :param apply_to_existing_transactions: Whether to apply to existing transactions
        :param merchant_criteria_use_original_statement: Use original statement text
        :param offset: Pagination offset for results
        :return: Preview results showing affected transactions
        """
        query = gql(
            """
            query PreviewTransactionRule($rule: TransactionRulePreviewInput!, $offset: Int) {
                transactionRulePreview(input: $rule) {
                    totalCount
                    results(offset: $offset, limit: 30) {
                        newName
                        newSplitTransactions
                        newCategory {
                            id
                            icon
                            name
                            __typename
                        }
                        newHideFromReports
                        newTags {
                            id
                            name
                            color
                            order
                            __typename
                        }
                        newGoal {
                            id
                            name
                            imageStorageProvider
                            imageStorageProviderId
                            __typename
                        }
                        transaction {
                            id
                            date
                            amount
                            merchant {
                                id
                                name
                                __typename
                            }
                            category {
                                id
                                name
                                icon
                                __typename
                            }
                            __typename
                        }
                        __typename
                    }
                    __typename
                }
            }
            """
        )

        rule_input = {
            "merchantCriteriaUseOriginalStatement": merchant_criteria_use_original_statement,
            "applyToExistingTransactions": apply_to_existing_transactions,
            "merchantCriteria": merchant_criteria,
            "amountCriteria": amount_criteria,
            "categoryIds": category_ids,
            "accountIds": account_ids,
            "setCategoryAction": set_category_action,
            "addTagsAction": add_tags_action,
            "setMerchantAction": set_merchant_action,
            "splitTransactionsAction": split_transactions_action,
        }

        variables = {"rule": rule_input, "offset": offset}

        return await self.gql_call(
            operation="PreviewTransactionRule",
            graphql_query=query,
            variables=variables,
        )

    async def delete_all_transaction_rules(self) -> bool:
        """
        Deletes all transaction rules.

        :return: True if all rules were deleted successfully
        """
        query = gql(
            """
            mutation Web_DeleteAllTransactionRulesMutation {
                deleteAllTransactionRules {
                    deleted
                    __typename
                }
            }
            """
        )

        result = await self.gql_call(
            operation="Web_DeleteAllTransactionRulesMutation",
            graphql_query=query,
            variables={},
        )

        return result.get("deleteAllTransactionRules", {}).get("deleted", False)

    async def get_transaction_categories(self) -> Dict[str, Any]:
        """
        Gets all the categories configured in the account.
        """
        query = gql(
            """
          query GetCategories {
            categories {
              ...CategoryFields
              __typename
            }
          }

          fragment CategoryFields on Category {
            id
            order
            name
            systemCategory
            isSystemCategory
            isDisabled
            updatedAt
            createdAt
            group {
              id
              name
              type
              __typename
            }
            __typename
          }
        """
        )
        return await self.gql_call(operation="GetCategories", graphql_query=query)

    async def delete_transaction_category(self, category_id: str) -> bool:
        query = gql(
            """
          mutation Web_DeleteCategory($id: UUID!, $moveToCategoryId: UUID) {
            deleteCategory(id: $id, moveToCategoryId: $moveToCategoryId) {
              errors {
                ...PayloadErrorFields
                __typename
              }
              deleted
              __typename
            }
          }

          fragment PayloadErrorFields on PayloadError {
            fieldErrors {
              field
              messages
              __typename
            }
            message
            code
            __typename
          }
        """
        )

        variables = {
            "id": category_id,
        }

        response = await self.gql_call(
            operation="Web_DeleteCategory", graphql_query=query, variables=variables
        )

        if not response["deleteCategory"]["deleted"]:
            raise RequestFailedException(response["deleteCategory"]["errors"])

        return True

    async def delete_transaction_categories(
        self, category_ids: List[str]
    ) -> List[Union[bool, BaseException]]:
        """
        Deletes a list of transaction categories.
        """
        return await asyncio.gather(
            *[self.delete_transaction_category(id) for id in category_ids],
            return_exceptions=True,
        )

    async def get_transaction_category_groups(self) -> Dict[str, Any]:
        """
        Gets all the category groups configured in the account.
        """
        query = gql(
            """
          query ManageGetCategoryGroups {
              categoryGroups {
                  id
                  name
                  order
                  type
                  updatedAt
                  createdAt
                  __typename
              }
          }
        """
        )
        return await self.gql_call(
            operation="ManageGetCategoryGroups", graphql_query=query
        )

    async def create_transaction_category(
        self,
        group_id: str,
        transaction_category_name: str,
        rollover_start_month: Optional[datetime] = None,
        icon: str = "\U00002753",
        rollover_enabled: bool = False,
        rollover_type: str = "monthly",
    ):
        """
        Creates a new transaction category
        :param group_id: The transaction category group id
        :param transaction_category_name: The name of the transaction category being created
        :param icon: The icon of the transaction category. This accepts the unicode string or emoji.
        :param rollover_start_month: The datetime of the rollover start month
        :param rollover_enabled: A bool whether the transaction category should be rolled over or not
        :param rollover_type: The budget roll over type
        """

        query = gql(
            """
            mutation Web_CreateCategory($input: CreateCategoryInput!) {
                createCategory(input: $input) {
                    errors {
                        ...PayloadErrorFields
                        __typename
                    }
                    category {
                        id
                        ...CategoryFormFields
                        __typename
                    }
                    __typename
                }
            }
            fragment PayloadErrorFields on PayloadError {
                fieldErrors {
                    field
                    messages
                    __typename
                }
                message
                code
                __typename
            }
            fragment CategoryFormFields on Category {
                id
                order
                name
                systemCategory
                systemCategoryDisplayName
                budgetVariability
                isSystemCategory
                isDisabled
                group {
                    id
                    type
                    groupLevelBudgetingEnabled
                    __typename
                }
                rolloverPeriod {
                    id
                    startMonth
                    startingBalance
                    __typename
                }
                __typename
            }
            """
        )
        
        # Set default rollover_start_month if not provided
        if rollover_start_month is None:
            rollover_start_month = datetime.today().replace(day=1)
        
        variables = {
            "input": {
                "group": group_id,
                "name": transaction_category_name,
                "icon": icon,
                "rolloverEnabled": rollover_enabled,
                "rolloverType": rollover_type,
                "rolloverStartMonth": rollover_start_month.strftime("%Y-%m-%d"),
            },
        }

        return await self.gql_call(
            operation="Web_CreateCategory",
            graphql_query=query,
            variables=variables,
        )

    async def update_transaction_category(
        self,
        category_id: str,
        name: Optional[str] = None,
        icon: Optional[str] = None,
        group_id: Optional[str] = None,
        rollover_enabled: Optional[bool] = None,
        rollover_type: Optional[str] = None,
        rollover_start_month: Optional[datetime] = None,
    ) -> Dict[str, Any]:
        """
        Updates an existing transaction category.

        :param category_id: The ID of the category to update
        :param name: New name for the category
        :param icon: New icon for the category (unicode string or emoji)
        :param group_id: New group ID for the category
        :param rollover_enabled: Whether rollover should be enabled
        :param rollover_type: The budget rollover type
        :param rollover_start_month: The datetime of the rollover start month
        """
        query = gql(
            """
            mutation Web_UpdateCategory($input: UpdateCategoryInput!) {
                updateCategory(input: $input) {
                    errors {
                        ...PayloadErrorFields
                        __typename
                    }
                    category {
                        id
                        ...CategoryFormFields
                        __typename
                    }
                    __typename
                }
            }

            fragment PayloadErrorFields on PayloadError {
                fieldErrors {
                    field
                    messages
                    __typename
                }
                message
                code
                __typename
            }

            fragment CategoryFormFields on Category {
                id
                name
                icon
                group {
                    id
                    name
                    __typename
                }
                rolloverEnabled
                rolloverType
                rolloverStartMonth
                order
                __typename
            }
            """
        )

        # Build input with only provided parameters
        input_data = {"id": category_id}

        if name is not None:
            input_data["name"] = name
        if icon is not None:
            input_data["icon"] = icon
        if group_id is not None:
            input_data["group"] = group_id
        if rollover_enabled is not None:
            input_data["rolloverEnabled"] = rollover_enabled
        if rollover_type is not None:
            input_data["rolloverType"] = rollover_type
        if rollover_start_month is not None:
            input_data["rolloverStartMonth"] = rollover_start_month.strftime("%Y-%m-%d")

        variables = {"input": input_data}

        return await self.gql_call(
            operation="Web_UpdateCategory",
            graphql_query=query,
            variables=variables,
        )

    async def create_transaction_tag(self, name: str, color: str) -> Dict[str, Any]:
        """
        Creates a new transaction tag.
        :param name: The name of the tag
        :param color: The color of the tag.
          The observed format is six-digit RGB hexadecimal, including the leading number sign.
          Example: color="#19D2A5".
          More information can be found https://en.wikipedia.org/wiki/Web_colors#Hex_triplet.
          Does not appear to be limited to the color selections in the dashboard.
        """
        mutation = gql(
            """
            mutation Common_CreateTransactionTag($input: CreateTransactionTagInput!) {
              createTransactionTag(input: $input) {
                tag {
                  id
                  name
                  color
                  order
                  transactionCount
                  __typename
                }
                errors {
                  message
                  __typename
                }
                __typename
              }
            }
            """
        )
        variables = {"input": {"name": name, "color": color}}

        return await self.gql_call(
            operation="Common_CreateTransactionTag",
            graphql_query=mutation,
            variables=variables,
        )

    async def get_transaction_tags(self) -> Dict[str, Any]:
        """
        Gets all the tags configured in the account.
        """
        query = gql(
            """
          query GetHouseholdTransactionTags($search: String, $limit: Int, $bulkParams: BulkTransactionDataParams) {
            householdTransactionTags(
              search: $search
              limit: $limit
              bulkParams: $bulkParams
            ) {
              id
              name
              color
              order
              transactionCount
              __typename
            }
          }
        """
        )
        return await self.gql_call(
            operation="GetHouseholdTransactionTags", graphql_query=query
        )

    async def set_transaction_tags(
        self,
        transaction_id: str,
        tag_ids: List[str],
    ) -> Dict[str, Any]:
        """
        Sets the tags on a transaction
        :param transaction_id: The transaction id
        :param tag_ids: The list of tag ids to set on the transaction.
          Overwrites existing tags. Empty list removes all tags.
        """

        query = gql(
            """
          mutation Web_SetTransactionTags($input: SetTransactionTagsInput!) {
            setTransactionTags(input: $input) {
              errors {
                ...PayloadErrorFields
                __typename
              }
              transaction {
                id
                tags {
                  id
                  __typename
                }
                __typename
              }
              __typename
            }
          }

          fragment PayloadErrorFields on PayloadError {
            fieldErrors {
              field
              messages
              __typename
            }
            message
            code
            __typename
          }
          """
        )

        variables = {
            "input": {"transactionId": transaction_id, "tagIds": tag_ids},
        }

        return await self.gql_call(
            operation="Web_SetTransactionTags",
            graphql_query=query,
            variables=variables,
        )

    async def get_transaction_details(
        self, transaction_id: str, redirect_posted: bool = True
    ) -> Dict[str, Any]:
        """
        Returns detailed information about a transaction.

        :param transaction_id: the transaction to fetch.
        :param redirect_posted: whether to redirect posted transactions. Defaults to True.
        """
        query = gql(
            """
          query GetTransactionDrawer($id: UUID!, $redirectPosted: Boolean) {
            getTransaction(id: $id, redirectPosted: $redirectPosted) {
              id
              amount
              pending
              isRecurring
              date
              originalDate
              hideFromReports
              needsReview
              reviewedAt
              reviewedByUser {
                id
                name
                __typename
              }
              plaidName
              notes
              hasSplitTransactions
              isSplitTransaction
              isManual
              splitTransactions {
                id
                ...TransactionDrawerSplitMessageFields
                __typename
              }
              originalTransaction {
                id
                ...OriginalTransactionFields
                __typename
              }
              attachments {
                id
                publicId
                extension
                sizeBytes
                filename
                originalAssetUrl
                __typename
              }
              account {
                id
                ...TransactionDrawerAccountSectionFields
                __typename
              }
              category {
                id
                __typename
              }
              goal {
                id
                __typename
              }
              merchant {
                id
                name
                transactionCount
                logoUrl
                recurringTransactionStream {
                  id
                  __typename
                }
                __typename
              }
              tags {
                id
                name
                color
                order
                __typename
              }
              needsReviewByUser {
                id
                __typename
              }
              __typename
            }
            myHousehold {
              users {
                id
                name
                __typename
              }
              __typename
            }
          }

          fragment TransactionDrawerSplitMessageFields on Transaction {
            id
            amount
            merchant {
              id
              name
              __typename
            }
            category {
              id
              name
              __typename
            }
            __typename
          }

          fragment OriginalTransactionFields on Transaction {
            id
            date
            amount
            merchant {
              id
              name
              __typename
            }
            __typename
          }

          fragment TransactionDrawerAccountSectionFields on Account {
            id
            displayName
            logoUrl
            id
            mask
            subtype {
              display
              __typename
            }
            __typename
          }
        """
        )

        variables = {
            "id": transaction_id,
            "redirectPosted": redirect_posted,
        }

        return await self.gql_call(
            operation="GetTransactionDrawer", variables=variables, graphql_query=query
        )

    async def get_transaction_splits(self, transaction_id: str) -> Dict[str, Any]:
        """
        Returns the transaction split information for a transaction.

        :param transaction_id: the transaction to query.
        """
        query = gql(
            """
          query TransactionSplitQuery($id: UUID!) {
            getTransaction(id: $id) {
              id
              amount
              category {
                id
                name
                __typename
              }
              merchant {
                id
                name
                __typename
              }
              splitTransactions {
                id
                merchant {
                  id
                  name
                  __typename
                }
                category {
                  id
                  name
                  __typename
                }
                amount
                notes
                __typename
              }
              __typename
            }
          }
        """
        )

        variables = {"id": transaction_id}

        return await self.gql_call(
            operation="TransactionSplitQuery", variables=variables, graphql_query=query
        )

    async def update_transaction_splits(
        self, transaction_id: str, split_data: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Creates, modifies, or deletes the splits for a given transaction.

        Returns the split information for the update transaction.

        :param transaction_id: the original transaction to modify.
        :param split_data: the splits to create, modify, or delete.
          If empty list or None is given, all splits will be deleted.
          If split_data is given, all existing splits for transaction_id will be replaced with the new splits.
          split_data takes the shape: [{"merchantName": "...", "amount": -12.34, "categoryId": "231"}, split2, split3, ...]
          sum([split.amount for split in split_data]) must equal transaction_id.amount.
        """
        query = gql(
            """
          mutation Common_SplitTransactionMutation($input: UpdateTransactionSplitMutationInput!) {
            updateTransactionSplit(input: $input) {
              errors {
                ...PayloadErrorFields
                __typename
              }
              transaction {
                id
                hasSplitTransactions
                splitTransactions {
                  id
                  merchant {
                    id
                    name
                    __typename
                  }
                  category {
                    id
                    name
                    __typename
                  }
                  amount
                  notes
                  __typename
                }
                __typename
              }
              __typename
            }
          }

          fragment PayloadErrorFields on PayloadError {
            fieldErrors {
              field
              messages
              __typename
            }
            message
            code
            __typename
          }
        """
        )

        if split_data is None:
            split_data = []

        variables = {
            "input": {"transactionId": transaction_id, "splitData": split_data}
        }

        return await self.gql_call(
            operation="Common_SplitTransactionMutation",
            variables=variables,
            graphql_query=query,
        )

    async def get_cashflow(
        self,
        limit: int = DEFAULT_RECORD_LIMIT,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Gets all the categories configured in the account.
        """
        query = gql(
            """
          query Web_GetCashFlowPage($filters: TransactionFilterInput) {
            byCategory: aggregates(filters: $filters, groupBy: ["category"]) {
              groupBy {
                category {
                  id
                  name
                  group {
                    id
                    type
                    __typename
                  }
                  __typename
                }
                __typename
              }
              summary {
                sum
                __typename
              }
              __typename
            }
            byCategoryGroup: aggregates(filters: $filters, groupBy: ["categoryGroup"]) {
              groupBy {
                categoryGroup {
                  id
                  name
                  type
                  __typename
                }
                __typename
              }
              summary {
                sum
                __typename
              }
              __typename
            }
            byMerchant: aggregates(filters: $filters, groupBy: ["merchant"]) {
              groupBy {
                merchant {
                  id
                  name
                  logoUrl
                  __typename
                }
                __typename
              }
              summary {
                sumIncome
                sumExpense
                __typename
              }
              __typename
            }
            summary: aggregates(filters: $filters, fillEmptyValues: true) {
              summary {
                sumIncome
                sumExpense
                savings
                savingsRate
                __typename
              }
              __typename
            }
          }
        """
        )

        variables = {
            "limit": limit,
            "orderBy": "date",
            "filters": {
                "search": "",
                "categories": [],
                "accounts": [],
                "tags": [],
            },
        }

        if start_date and end_date:
            variables["filters"]["startDate"] = start_date
            variables["filters"]["endDate"] = end_date
        elif (start_date is None) ^ (end_date is None):
            raise Exception(
                "You must specify both a startDate and endDate, not just one of them."
            )
        else:
            variables["filters"]["startDate"] = self._get_start_of_current_month()
            variables["filters"]["endDate"] = self._get_end_of_current_month()

        return await self.gql_call(
            operation="Web_GetCashFlowPage", variables=variables, graphql_query=query
        )

    async def get_cashflow_summary(
        self,
        limit: int = DEFAULT_RECORD_LIMIT,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Gets all the categories configured in the account.
        """
        query = gql(
            """
          query Web_GetCashFlowPage($filters: TransactionFilterInput) {
            summary: aggregates(filters: $filters, fillEmptyValues: true) {
              summary {
                sumIncome
                sumExpense
                savings
                savingsRate
                __typename
              }
              __typename
            }
          }
        """
        )

        variables = {
            "limit": limit,
            "orderBy": "date",
            "filters": {
                "search": "",
                "categories": [],
                "accounts": [],
                "tags": [],
            },
        }

        if start_date and end_date:
            variables["filters"]["startDate"] = start_date
            variables["filters"]["endDate"] = end_date
        elif bool(start_date) != bool(end_date):
            raise Exception(
                "You must specify both a startDate and endDate, not just one of them."
            )
        else:
            variables["filters"]["startDate"] = self._get_start_of_current_month()
            variables["filters"]["endDate"] = self._get_end_of_current_month()

        return await self.gql_call(
            operation="Web_GetCashFlowPage", variables=variables, graphql_query=query
        )

    async def update_transaction(
        self,
        transaction_id: str,
        category_id: Optional[str] = None,
        merchant_name: Optional[str] = None,
        goal_id: Optional[str] = None,
        amount: Optional[float] = None,
        date: Optional[str] = None,
        hide_from_reports: Optional[bool] = None,
        needs_review: Optional[bool] = None,
        notes: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Updates a single existing transaction as identified by the transaction_id
        The only required attribute is transaction_id. Calling this function with
        only the transaction_id will have no effect on the existing transaction data
        but will not cause an error.

        Comments on parameters:
        - transaction_id: Must match an existing transaction_id returned from Monarch
        - category_id: This parameter is only needed when the user wants to change the
            current category. When provided, it must match an existing category_id returned
            from Monarch. An empty string is equivalent to the parameter not being passed.
        - merchant_name: This parameter is only needed when the user wants to change
            the existing merchant name. Empty strings are ignored by the Monarch API
            when passed since a non-empty merchant name is required for all transactions
        - goal_id: This parameter is only needed when the user wants to change
            the existing goal.  When provided, it must match an existing goal_id returned
            from Monarch.  An empty string can be passed to clear out existing goal associations.
        - amount:  This parameter is only needed when the user wants to update
            the existing transaction amount. Empty strings are explicitly ignored by this code
            to avoid errors in the API.
        - date:  This parameter is only needed when the user wants to update
            the existing transaction date. Empty strings are explicitly ignored by this code
            to avoid errors in the API.  Required format is "2023-10-30"
        - hide_from_reports: This parameter is only needed when the user wants to update the
            existing transaction's hide-from-reports value.  If passed, the parameter is cast to
            Booleans to avoid API issues.
        - needs_review: This parameter is only needed when the user wants to update the
            existing transaction's needs-review value.  If passed, the parameter is cast to
            Booleans to avoid API issues.
        - notes: This parameter is only needed when the user wants to change
            the existing note.  An empty string can be passed to clear out existing notes.

        Examples:
        - To update a note: mm.update_transaction(
            transaction_id="160820461792094418",
            notes="my note")

        - To clear a note: mm.update_transaction(
            transaction_id="160820461792094418",
            notes="")

        - To update all items:
            mm.update_transaction(
                transaction_id="160820461792094418",
                category_id="160185840107743863",
                merchant_name="Amazon",
                goal_id="160826408575920275",
                amount=123.45,
                date="2023-11-09",
                hide_from_reports=False,
                needs_review="ThisWillBeCastToTrue",
                notes=f'Updated On: {datetime.now().strftime("%m/%d/%Y %H:%M:%S")}',
            )
        """
        query = gql(
            """
        mutation Web_TransactionDrawerUpdateTransaction($input: UpdateTransactionMutationInput!) {
            updateTransaction(input: $input) {
            transaction {
                id
                amount
                pending
                date
                hideFromReports
                needsReview
                reviewedAt
                reviewedByUser {
                id
                name
                __typename
                }
                plaidName
                notes
                isRecurring
                category {
                id
                __typename
                }
                goal {
                id
                __typename
                }
                merchant {
                id
                name
                __typename
                }
                __typename
            }
            errors {
                ...PayloadErrorFields
                __typename
            }
            __typename
            }
        }

        fragment PayloadErrorFields on PayloadError {
            fieldErrors {
            field
            messages
            __typename
            }
            message
            code
            __typename
        }
        """
        )

        variables: dict[str, Any] = {
            "input": {
                "id": transaction_id,
            }
        }

        # Within Monarch, these values cannot be empty. Monarch will simply ignore updates
        # to category and merchant name that are empty strings or None.
        # As such, no need to avoid adding to variables
        variables["input"].update({"category": category_id})
        variables["input"].update({"name": merchant_name})

        # Monarch will not accept nulls for amount and date.
        # Don't update values if an empty string is passed or if parameter is None
        if amount:
            variables["input"].update({"amount": amount})
        if date:
            variables["input"].update({"date": date})

        # Don't update values if the parameter is not passed or explicitly set to None.
        # Passed values must be cast to bool to avoid API errors
        if hide_from_reports is not None:
            variables["input"].update({"hideFromReports": bool(hide_from_reports)})
        if needs_review is not None:
            variables["input"].update({"needsReview": bool(needs_review)})

        # We want an empty string to clear the goal and notes parameters but the values should not
        # be cleared if the parameter isn't passed
        # Don't update values if the parameter is not passed or explicitly set to None.
        if goal_id is not None:
            variables["input"].update({"goalId": goal_id})
        if notes is not None:
            variables["input"].update({"notes": notes})

        return await self.gql_call(
            operation="Web_TransactionDrawerUpdateTransaction",
            variables=variables,
            graphql_query=query,
        )

    async def bulk_update_transactions(
        self,
        transaction_ids: List[str],
        updates: Dict[str, Any],
        excluded_transaction_ids: Optional[List[str]] = None,
        all_selected: bool = False,
        filters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Bulk update multiple transactions with specified changes.

        This method allows you to efficiently update many transactions at once
        with the same set of changes, such as hiding/unhiding from reports,
        changing categories, or updating other transaction properties.

        Args:
            transaction_ids: List of transaction IDs to update
            updates: Dictionary of updates to apply (e.g., {"hide": False})
            excluded_transaction_ids: Optional list of transaction IDs to exclude from updates
            all_selected: Whether all transactions are selected (for large bulk operations)
            filters: Optional filters that were used to select the transactions

        Returns:
            Result of bulk update operation with success status and affected count

        Raises:
            ValidationError: If inputs are invalid
            ValueError: If bulk update operation fails

        Examples:
            # Unhide specific transactions
            result = await mm.bulk_update_transactions(
                transaction_ids=["123", "456", "789"],
                updates={"hide": False}
            )

            # Hide transactions from reports
            result = await mm.bulk_update_transactions(
                transaction_ids=["123", "456"],
                updates={"hide": True}
            )

            # Update category for multiple transactions
            result = await mm.bulk_update_transactions(
                transaction_ids=["123", "456"],
                updates={"categoryId": "category_id_here"}
            )
        """
        return await self._transaction_service.bulk_update_transactions(
            transaction_ids=transaction_ids,
            updates=updates,
            excluded_transaction_ids=excluded_transaction_ids,
            all_selected=all_selected,
            filters=filters,
        )

    async def bulk_unhide_transactions(
        self, transaction_ids: List[str], filters: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Bulk unhide transactions (set hideFromReports to false).

        This is a convenience method that unhides multiple transactions at once,
        making them visible in reports again. This is particularly useful when
        you have many transactions that were accidentally hidden or need to be
        shown in reports again.

        Args:
            transaction_ids: List of transaction IDs to unhide
            filters: Optional filters that were used to select the transactions

        Returns:
            Result of bulk unhide operation with success status and affected count

        Raises:
            ValidationError: If transaction_ids is invalid
            ValueError: If bulk unhide operation fails

        Examples:
            # Unhide specific transactions
            result = await mm.bulk_unhide_transactions([
                "220716668609011425",
                "220716668609011424",
                "220716668609011423"
            ])
            
            if result["success"]:
                print(f"Successfully unhid {result['affectedCount']} transactions")

            # Get hidden transactions and unhide them all
            hidden = await mm.get_hidden_transactions(limit=100)
            transaction_ids = [t["id"] for t in hidden["allTransactions"]["results"]]
            
            if transaction_ids:
                result = await mm.bulk_unhide_transactions(
                    transaction_ids,
                    filters={"hideFromReports": True}
                )
                print(f"Unhid {result['affectedCount']} transactions")
        """
        return await self._transaction_service.bulk_unhide_transactions(
            transaction_ids=transaction_ids, filters=filters
        )

    async def bulk_hide_transactions(
        self, transaction_ids: List[str], filters: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Bulk hide transactions (set hideFromReports to true).

        This is a convenience method that hides multiple transactions from reports
        at once. Hidden transactions won't appear in spending reports or budget
        calculations, which is useful for internal transfers or transactions
        you don't want to track.

        Args:
            transaction_ids: List of transaction IDs to hide
            filters: Optional filters that were used to select the transactions

        Returns:
            Result of bulk hide operation with success status and affected count

        Raises:
            ValidationError: If transaction_ids is invalid
            ValueError: If bulk hide operation fails

        Examples:
            # Hide specific transactions from reports
            result = await mm.bulk_hide_transactions([
                "220716668609011425",
                "220716668609011424"
            ])
            
            if result["success"]:
                print(f"Successfully hid {result['affectedCount']} transactions")
        """
        return await self._transaction_service.bulk_hide_transactions(
            transaction_ids=transaction_ids, filters=filters
        )

    async def get_hidden_transactions(
        self,
        limit: Optional[int] = 100,
        offset: Optional[int] = 0,
        order_by: str = "date",
    ) -> Dict[str, Any]:
        """
        Get transactions that are hidden from reports.

        This method retrieves transactions where hideFromReports is true,
        making it easy to see what transactions are currently hidden and
        potentially bulk unhide them.

        Args:
            limit: Maximum number of transactions to return (default: 100)
            offset: Number of transactions to skip (default: 0)
            order_by: Field to order by (default: "date")

        Returns:
            List of hidden transactions with full transaction details including:
            - Transaction IDs, amounts, dates, merchants
            - Category and account information
            - Tags and other metadata
            - Total count of hidden transactions

        Examples:
            # Get first 50 hidden transactions
            hidden = await mm.get_hidden_transactions(limit=50)
            print(f"Found {hidden['allTransactions']['totalCount']} hidden transactions")
            
            # Extract transaction IDs for bulk operations
            transaction_ids = [t["id"] for t in hidden["allTransactions"]["results"]]
            
            # Unhide them all
            if transaction_ids:
                await mm.bulk_unhide_transactions(transaction_ids)
        """
        return await self._transaction_service.get_hidden_transactions(
            limit=limit, offset=offset, order_by=order_by
        )

    async def set_budget_amount(
        self,
        amount: float,
        category_id: Optional[str] = None,
        category_group_id: Optional[str] = None,
        timeframe: str = "month",  # I believe this is the only valid value right now
        start_date: Optional[str] = None,
        apply_to_future: bool = False,
    ) -> Dict[str, Any]:
        """
        Updates the budget amount for the given category.

        :param category_id:
            The ID of the category to set the budget for (cannot be provided w/ category_group_id)
        :param category_group_id:
            The ID of the category group to set the budget for (cannot be provided w/ category_id)
        :param amount:
            The amount to set the budget to. Can be negative (to indicate over-budget). A zero
            value will "unset" or "clear" the budget for the given category.
        :param timeframe:
            The timeframe of the budget. As of writing, it is believed that `month` is the
            only valid value for this parameter.
        :param start_date:
            The beginning of the given timeframe (ex: 2023-12-01). If not specified, then the
            beginning of today's month will be used.
        :param apply_to_future:
            Whether to apply the new budget amount to all proceeding timeframes
        """

        # Will be true if neither of the parameters are set, or both are
        if (category_id is None) is (category_group_id is None):
            raise Exception(
                "You must specify either a category_id OR category_group_id; not both"
            )

        query = gql(
            """
          mutation Common_UpdateBudgetItem($input: UpdateOrCreateBudgetItemMutationInput!) {
            updateOrCreateBudgetItem(input: $input) {
              budgetItem {
                id
                budgetAmount
                __typename
              }
              __typename
            }
          }
        """
        )

        variables = {
            "input": {
                "startDate": start_date,
                "timeframe": timeframe,
                "categoryId": category_id,
                "categoryGroupId": category_group_id,
                "amount": amount,
                "applyToFuture": apply_to_future,
            }
        }

        if start_date is None:
            variables["input"]["startDate"] = self._get_start_of_current_month()

        return await self.gql_call(
            operation="Common_UpdateBudgetItem",
            variables=variables,
            graphql_query=query,
        )

    async def upload_account_balance_history(
        self, account_id: str, csv_content: str
    ) -> None:
        """
        Uploads the account balance history csv for a given account.

        :param account_id: The account ID to apply the history to.
        :param csv_content: CSV representation of the balance history.
        """
        if not account_id or not csv_content:
            raise RequestFailedException("account_id and csv_content cannot be empty")

        filename = "upload.csv"
        form = FormData()
        form.add_field("files", csv_content, filename=filename, content_type="text/csv")
        form.add_field("account_files_mapping", json.dumps({filename: account_id}))

        async with ClientSession(headers=self._headers) as session:
            resp = await session.post(
                MonarchMoneyEndpoints.getAccountBalanceHistoryUploadEndpoint(),
                json=form,
            )
            if resp.status != 200:
                raise RequestFailedException(f"HTTP Code {resp.status}: {resp.reason}")

    async def get_recurring_transactions(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Fetches upcoming recurring transactions from Monarch Money's API.  This includes
        all merchant data, as well as the accounts where the charge will take place.
        """
        query = gql(
            """
            query Web_GetUpcomingRecurringTransactionItems($startDate: Date!, $endDate: Date!, $filters: RecurringTransactionFilter) {
              recurringTransactionItems(
                startDate: $startDate
                endDate: $endDate
                filters: $filters
              ) {
                stream {
                  id
                  frequency
                  amount
                  isApproximate
                  merchant {
                    id
                    name
                    logoUrl
                    __typename
                  }
                  __typename
                }
                date
                isPast
                transactionId
                amount
                amountDiff
                category {
                  id
                  name
                  __typename
                }
                account {
                  id
                  displayName
                  logoUrl
                  __typename
                }
                __typename
              }
            }
        """
        )

        variables = {"startDate": start_date, "endDate": end_date}

        if (start_date is None) ^ (end_date is None):
            raise Exception(
                "You must specify both a start_date and end_date, not just one of them."
            )
        elif start_date is None and end_date is None:
            variables["startDate"] = self._get_start_of_current_month()
            variables["endDate"] = self._get_end_of_current_month()

        return await self.gql_call(
            "Web_GetUpcomingRecurringTransactionItems", query, variables
        )

    async def mark_stream_as_not_recurring(self, stream_id: str) -> bool:
        """
        Mark a recurring transaction stream as not recurring (disable it).

        This stops Monarch Money from treating transactions from this merchant
        as part of a recurring pattern, which can be useful when:
        - A subscription has been cancelled but old transactions still exist
        - One-time purchases from a merchant are being incorrectly grouped as recurring
        - You want to remove predictive forecasting for a specific merchant

        Args:
            stream_id: ID of the recurring stream to disable

        Returns:
            True if successfully marked as not recurring, False otherwise

        Raises:
            LoginFailedException: If not authenticated
            ValidationError: If stream_id is invalid

        Example:
            # Mark Amazon purchases as not recurring
            success = await mm.mark_stream_as_not_recurring("135553558010567728")
            if success:
                print("Stream marked as not recurring")
        """
        return await self._transaction_service.mark_stream_as_not_recurring(stream_id)

    async def get_bills(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        limit: int = 100,
    ) -> Dict[str, Any]:
        """
        Get upcoming bills and payments.

        :param start_date: Start date in "yyyy-mm-dd" format (defaults to today)
        :param end_date: End date in "yyyy-mm-dd" format (defaults to 30 days from now)
        :param limit: Maximum number of bills to return
        """
        query = gql(
            """
            query GetBills($startDate: Date!, $endDate: Date!, $limit: Int!) {
              bills: upcomingRecurringTransactionItems(
                startDate: $startDate,
                endDate: $endDate,
                limit: $limit
              ) {
                id
                name: description
                amount
                dueDate: date
                isPast
                transactionId
                merchant {
                  id
                  name
                  __typename
                }
                category {
                  id
                  name
                  icon
                  __typename
                }
                account {
                  id
                  displayName
                  logoUrl
                  __typename
                }
                __typename
              }
            }
            """
        )

        # Set default dates if not provided
        if not start_date:
            start_date = datetime.now().strftime("%Y-%m-%d")

        if not end_date:
            end_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")

        variables = {"startDate": start_date, "endDate": end_date, "limit": limit}

        return await self.gql_call(
            operation="GetBills",
            graphql_query=query,
            variables=variables,
        )

    def _get_current_date(self) -> str:
        """
        Returns the current date as a string formatted like %Y-%m-%d.
        """
        return datetime.now().strftime("%Y-%m-%d")

    def _get_start_of_current_month(self) -> str:
        """
        Returns the date for the first day of the current month as a string formatted as %Y-%m-%d.
        """
        now = datetime.now()
        start_of_month = now.replace(day=1)
        return start_of_month.strftime("%Y-%m-%d")

    def _get_end_of_current_month(self) -> str:
        """
        Returns the date for the last day of the current month as a string formatted as %Y-%m-%d.
        """
        now = datetime.now()
        _, last_day = calendar.monthrange(now.year, now.month)
        end_of_month = now.replace(day=last_day)
        return end_of_month.strftime("%Y-%m-%d")

    async def gql_call(
        self,
        operation: str,
        graphql_query: DocumentNode,
        variables: Dict[str, Any] = {},
    ) -> Dict[str, Any]:
        """
        Makes a GraphQL call to Monarch Money's API with retry logic.
        """
        # Enhanced debug logging when debug flag is enabled
        if self._debug:
            import json
            logger.debug(
                "🚀 GraphQL Request",
                operation=operation,
                variables=variables,
                query_str=str(graphql_query)[:200] + "..." if len(str(graphql_query)) > 200 else str(graphql_query)
            )

        async def _execute():
            try:
                result = await self._get_graphql_client().execute_async(
                    graphql_query, variable_values=variables, operation_name=operation
                )
                if self._debug:
                    logger.debug("✅ GraphQL Response received", operation=operation, result_keys=list(result.keys()) if isinstance(result, dict) else "non-dict")
                return result
            except Exception as e:
                if self._debug:
                    logger.error(
                        "❌ GraphQL Request Failed",
                        operation=operation,
                        variables=variables,
                        error=str(e),
                        error_type=type(e).__name__
                    )
                    # Log additional details for specific error types
                    if hasattr(e, 'response'):
                        logger.error("HTTP Response details", status=getattr(e.response, 'status', 'unknown'))
                    if hasattr(e, 'errors') and e.errors:
                        logger.error("GraphQL Error details", graphql_errors=e.errors)
                raise

        return await retry_with_backoff(_execute)

    def save_session(self, filename: Optional[str] = None) -> None:
        """
        Saves the auth token and session metadata needed to access a Monarch Money account.
        Uses secure JSON storage instead of unsafe pickle format.

        Note: This method is synchronous for backward compatibility but delegates to
        the authentication service internally.
        """
        if filename is None:
            filename = self._session_file

        # Use authentication service for comprehensive session saving
        from .services.authentication_service import AuthenticationService
        auth_service = AuthenticationService(self)

        # Run the async method synchronously for backward compatibility
        import asyncio
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # If we're already in an async context, we can't use run_until_complete
                # Fall back to the legacy method to avoid blocking
                filename = os.path.abspath(filename)
                session_data = {
                    "token": self._token,
                    "csrf_token": self._csrf_token,  # Include CSRF token
                    "created_at": self._session_created_at or time.time(),
                    "last_validated": self._session_last_validated or time.time(),
                    "headers": dict(self._headers),
                    "version": "0.10.0",
                }
                self._secure_storage.save_session(session_data, filename)
                logger.info("Session saved securely (legacy mode)", session_file=filename)
            else:
                loop.run_until_complete(auth_service.save_session(filename))
        except RuntimeError:
            # If no event loop exists, create one
            asyncio.run(auth_service.save_session(filename))

    def load_session(self, filename: Optional[str] = None) -> None:
        """
        Loads pre-existing auth token from session file.
        Supports both new secure JSON format and legacy pickle format (with migration).

        Note: This method is synchronous for backward compatibility but delegates to
        the authentication service internally for comprehensive session loading.
        """
        if filename is None:
            filename = self._session_file

        # Check if this is a legacy pickle file
        if LegacyPickleSession.detect_pickle_file(filename):
            logger.warning(
                "Detected legacy pickle session file. Migrating to secure format.",
                session_file=filename,
            )

            # Create new filename for JSON version
            json_filename = filename.replace(".pickle", ".json")

            # Migrate the session
            if self._secure_storage.migrate_pickle_session(filename, json_filename):
                # Update session file path to new JSON version
                self._session_file = json_filename
                filename = json_filename
            else:
                # If migration fails, load pickle with warning
                data = LegacyPickleSession.load_with_warning(filename)
                self._load_session_data(data)
                return

        # Use authentication service for comprehensive session loading
        from .services.authentication_service import AuthenticationService
        auth_service = AuthenticationService(self)

        # Run the async method synchronously for backward compatibility
        import asyncio
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # If we're already in an async context, fall back to legacy method with enhanced loading
                try:
                    data = self._secure_storage.load_session(filename)
                    # Manually load session data using the enhanced method
                    # We can't await here since we're in a sync context, so do it synchronously
                    self._token = data.get("token")
                    self._csrf_token = data.get("csrf_token")
                    self._last_used = data.get("last_used")

                    # Load session metadata
                    if "created_at" in data:
                        self._session_created_at = data["created_at"]
                    if "last_validated" in data:
                        self._session_last_validated = data["last_validated"]

                    # Set Authorization header (essential for API calls)
                    if self._token:
                        self._headers["Authorization"] = f"Token {self._token}"

                    # Update headers with additional session data
                    headers = data.get("headers", {})
                    if "csrftoken" in headers:
                        self._headers["csrftoken"] = headers["csrftoken"]

                    logger.info("Session loaded securely (legacy mode)", session_file=filename)
                except FileNotFoundError:
                    raise FileNotFoundError(f"Session file not found: {filename}")
                except ValueError as e:
                    raise ValueError(f"Invalid session file format: {e}")
            else:
                loop.run_until_complete(auth_service.load_session(filename))
        except RuntimeError:
            # If no event loop exists, create one
            asyncio.run(auth_service.load_session(filename))

    def _resolve_session_file(self, session_file: str) -> str:
        """
        Auto-detect the correct session file format.
        
        If the default pickle file is requested but a migrated JSON version exists,
        use the JSON version instead to prevent load_session() failures.
        """
        # If user provided explicit non-default file, use as-is
        if session_file != SESSION_FILE:
            return session_file
            
        # Check if JSON version exists (from migration)
        json_filename = session_file.replace(".pickle", ".json")
        if os.path.exists(json_filename):
            return json_filename
            
        # Fall back to original filename
        return session_file

    def _load_session_data(self, data: Any) -> None:
        """Load session data from parsed session file."""
        # Handle legacy session format (just token string or {"token": "..."})
        if isinstance(data, str):
            self.set_token(data)
        elif isinstance(data, dict) and "token" in data:
            self.set_token(data["token"])
            # Store session metadata if available
            if "created_at" in data:
                self._session_created_at = data["created_at"]
            if "last_validated" in data:
                self._session_last_validated = data["last_validated"]
        else:
            raise ValueError("Invalid session file format")

        self._headers["Authorization"] = f"Token {self._token}"

    def delete_session(self, filename: Optional[str] = None) -> None:
        """
        Deletes the session file.
        """
        if filename is None:
            filename = self._session_file

        if os.path.exists(filename):
            os.remove(filename)

    async def validate_session(self) -> bool:
        """
        Validates the current session by making a lightweight API call.

        Returns:
            True if session is valid, False if invalid/expired
        """
        if not self._token:
            return False

        try:
            # Use get_me() as a lightweight validation call
            await self.get_me()

            # Update last validated timestamp
            self._session_last_validated = time.time()

            # Save updated session metadata
            if self._session_file:
                self.save_session()

            return True
        except Exception:
            # Session is invalid
            return False

    def is_session_stale(self) -> bool:
        """
        Checks if the session needs validation based on time elapsed and API activity.
        Uses conservative smart validation that's safe for tests.

        Returns:
            True if session should be validated, False if recently validated
        """
        if not self._session_last_validated:
            return True

        elapsed = time.time() - self._session_last_validated

        # Conservative smart validation: if we've had successful API calls recently,
        # we can slightly extend the validation interval (safe approach)
        if hasattr(self, '_api_call_count_since_validation') and self._api_call_count_since_validation > 0:
            # Only extend by 50% max for safety
            extended_interval = min(self._session_validation_interval * 1.5, 10800)  # Max 3 hours
            return elapsed > extended_interval

        return elapsed > self._session_validation_interval

    async def ensure_valid_session(self) -> None:
        """
        Ensures the session is valid, validating if stale or refreshing if invalid.

        Raises:
            RequestFailedException: If session is invalid and cannot be refreshed
        """
        if not self._token:
            raise RequestFailedException(
                "No session token available. Please login first."
            )

        # Check if validation is needed
        if self.is_session_stale():
            is_valid = await self.validate_session()
            if not is_valid:
                raise RequestFailedException(
                    "Session has expired. Please login again or use refresh_session() if credentials are available."
                )

    def get_session_info(self) -> Dict[str, Any]:
        """
        Gets information about the current session.

        Returns:
            Dictionary with session metadata including creation time, last validation, and staleness
        """
        if not self._token:
            return {"valid": False, "message": "No session token"}

        current_time = time.time()
        session_age = None
        if self._session_created_at:
            session_age = current_time - self._session_created_at

        time_since_validation = None
        if self._session_last_validated:
            time_since_validation = current_time - self._session_last_validated

        return {
            "valid": bool(self._token),
            "token_present": bool(self._token),
            "created_at": self._session_created_at,
            "last_validated": self._session_last_validated,
            "session_age_seconds": session_age,
            "time_since_validation_seconds": time_since_validation,
            "is_stale": self.is_session_stale(),
            "validation_interval_seconds": self._session_validation_interval,
        }

    async def preload_cache(self, context: str = "general") -> Dict[str, bool]:
        """
        Intelligently preload commonly accessed data to reduce API calls.

        Args:
            context: Usage context ("general", "dashboard", "investments", "transactions")

        Returns:
            Dict indicating which preloads succeeded

        Example:
            >>> mm = MonarchMoney()
            >>> await mm.login("user@example.com", "password")
            >>> results = await mm.preload_cache("dashboard")
            >>> print(f"Preloaded {sum(results.values())} out of {len(results)} data types")
        """
        try:
            if self._cache_preloader is None:
                from .cache_preloader import CachePreloader
                self._cache_preloader = CachePreloader(self)
            return await self._cache_preloader.smart_preload(context)
        except Exception as e:
            # Graceful fallback if preloading fails
            self.logger.debug("Cache preloading failed, continuing without preload", error=str(e))
            return {"preloading_failed": True, "error": str(e)}

    def get_cache_metrics(self) -> Dict[str, Any]:
        """
        Get cache performance metrics.

        Returns:
            Dict with cache hit rates, API calls saved, etc.
        """
        try:
            if self._cache_preloader is None:
                from .cache_preloader import CachePreloader
                self._cache_preloader = CachePreloader(self)
            return self._cache_preloader.get_preload_metrics()
        except Exception as e:
            # Graceful fallback if metrics fail
            return {"cache_metrics_failed": True, "error": str(e)}

    async def _login_user(
        self, email: str, password: str, mfa_secret_key: Optional[str]
    ) -> None:
        """
        Performs the initial login to a Monarch Money account.
        Uses GraphQL authentication as fallback if REST endpoint fails.
        """
        data = {
            "username": email,
            "password": password,
            "trusted_device": True,
            "supports_mfa": True,
            "supports_email_otp": True,
            "supports_recaptcha": True,
        }

        if mfa_secret_key:
            data["totp"] = oathtool.generate_otp(mfa_secret_key)

        async def _attempt_login():
            async with ClientSession(headers=self._headers) as session:
                async with session.post(
                    MonarchMoneyEndpoints.getLoginEndpoint(), json=data
                ) as resp:
                    if resp.status == 403:
                        raise MFARequiredError("Multi-factor authentication required")
                    elif resp.status == 404:
                        # REST endpoint not found, try GraphQL authentication
                        await self._login_user_graphql(
                            email, password, mfa_secret_key, session
                        )
                        return
                    elif resp.status == 429:
                        # Rate limited - will be retried by retry_with_backoff
                        raise RateLimitError("API rate limit exceeded during login")
                    elif resp.status != 200:
                        raise LoginFailedException(
                            f"HTTP Code {resp.status}: {resp.reason}"
                        )

                    response = await resp.json()
                    self.set_token(response["token"])
                    self._headers["Authorization"] = f"Token {self._token}"

        await retry_with_backoff(_attempt_login)

    async def _login_user_graphql(
        self,
        email: str,
        password: str,
        mfa_secret_key: Optional[str],
        session: ClientSession,
    ) -> None:
        """
        Performs GraphQL-based login when REST endpoint is not available.
        """
        mutation = gql(
            """
            mutation Login($email: String!, $password: String!, $totp: String) {
                login(email: $email, password: $password, totp: $totp) {
                    token
                    user {
                        id
                        email
                    }
                    errors {
                        field
                        messages
                    }
                }
            }
        """
        )

        variables = {"email": email, "password": password}

        if mfa_secret_key:
            variables["totp"] = oathtool.generate_otp(mfa_secret_key)

        # Create a temporary GraphQL client without authentication
        transport = AIOHTTPTransport(
            url=MonarchMoneyEndpoints.getGraphQL(),
            headers={"Content-Type": "application/json"},
            timeout=self._timeout,
            ssl=True,
        )
        client = Client(transport=transport, fetch_schema_from_transport=False)

        try:
            result = await client.execute_async(mutation, variable_values=variables)

            # Handle GraphQL-level errors
            if "errors" in result and result["errors"]:
                error_messages = [str(error) for error in result["errors"]]
                if any(
                    "mfa" in msg.lower() or "totp" in msg.lower()
                    for msg in error_messages
                ):
                    raise RequireMFAException("Multi-Factor Auth Required")
                raise LoginFailedException(
                    f"GraphQL Login Error: {'; '.join(error_messages)}"
                )

            # Handle login-specific errors
            login_data = result.get("login", {})
            if not login_data:
                raise LoginFailedException("No login data in GraphQL response")

            login_errors = login_data.get("errors", [])
            if login_errors:
                error_msgs = []
                for err in login_errors:
                    if isinstance(err, dict):
                        field = err.get("field", "unknown")
                        messages = err.get("messages", ["unknown error"])
                        error_msgs.append(f"{field}: {', '.join(messages)}")
                    else:
                        error_msgs.append(str(err))
                raise LoginFailedException(f"Login failed: {'; '.join(error_msgs)}")

            token = login_data.get("token")
            if not token:
                raise LoginFailedException("No token received from GraphQL login")

            self.set_token(token)
            self._headers["Authorization"] = f"Token {self._token}"

        except Exception as e:
            if isinstance(e, (RequireMFAException, LoginFailedException)):
                raise
            raise LoginFailedException(f"GraphQL authentication failed: {str(e)}")

    async def _mfa_graphql(
        self, email: str, password: str, code: str, session: ClientSession
    ) -> None:
        """
        Performs GraphQL-based MFA authentication when REST endpoint is not available.
        """
        mutation = gql(
            """
            mutation Login($email: String!, $password: String!, $totp: String) {
                login(email: $email, password: $password, totp: $totp) {
                    token
                    user {
                        id
                        email
                    }
                    errors {
                        field
                        messages
                    }
                }
            }
        """
        )

        variables = {"email": email, "password": password, "totp": code}

        # Create a temporary GraphQL client without authentication
        transport = AIOHTTPTransport(
            url=MonarchMoneyEndpoints.getGraphQL(),
            headers={"Content-Type": "application/json"},
            timeout=self._timeout,
            ssl=True,
        )
        client = Client(transport=transport, fetch_schema_from_transport=False)

        try:
            result = await client.execute_async(mutation, variable_values=variables)

            # Handle GraphQL-level errors
            if "errors" in result and result["errors"]:
                error_messages = [str(error) for error in result["errors"]]
                raise LoginFailedException(
                    f"GraphQL MFA Error: {'; '.join(error_messages)}"
                )

            # Handle login-specific errors
            login_data = result.get("login", {})
            if not login_data:
                raise LoginFailedException("No login data in GraphQL MFA response")

            login_errors = login_data.get("errors", [])
            if login_errors:
                error_msgs = []
                for err in login_errors:
                    if isinstance(err, dict):
                        field = err.get("field", "unknown")
                        messages = err.get("messages", ["unknown error"])
                        error_msgs.append(f"{field}: {', '.join(messages)}")
                    else:
                        error_msgs.append(str(err))
                raise LoginFailedException(f"MFA failed: {'; '.join(error_msgs)}")

            token = login_data.get("token")
            if not token:
                raise LoginFailedException("No token received from GraphQL MFA login")

            self.set_token(token)
            self._headers["Authorization"] = f"Token {self._token}"

        except Exception as e:
            if isinstance(e, LoginFailedException):
                raise
            raise LoginFailedException(f"GraphQL MFA authentication failed: {str(e)}")

    async def _multi_factor_authenticate(
        self, email: str, password: str, code: str
    ) -> None:
        """
        Performs the MFA step of login.
        Uses GraphQL authentication as fallback if REST endpoint fails.
        """
        # Try email_otp field first (for email OTP codes)
        # Fall back to totp field (for authenticator app codes)
        data = {
            "username": email,
            "password": password,
            "trusted_device": True,
            "supports_mfa": True,
            "supports_email_otp": True,
            "supports_recaptcha": True,
        }

        # Add the MFA code - try email_otp first, then totp
        if len(code) == 6 and code.isdigit():
            # Likely email OTP (6 digits)
            data["email_otp"] = code
        else:
            # Likely TOTP from authenticator app
            data["totp"] = code

        async def _attempt_mfa():
            async with ClientSession(headers=self._headers) as session:
                async with session.post(
                    MonarchMoneyEndpoints.getLoginEndpoint(), json=data
                ) as resp:
                    if resp.status == 404:
                        # REST endpoint not found, try GraphQL authentication with MFA code
                        await self._mfa_graphql(email, password, code, session)
                        return
                    elif resp.status == 429:
                        # Rate limited - will be retried by retry_with_backoff
                        raise RateLimitError("API rate limit exceeded during login")
                    elif resp.status != 200:
                        try:
                            response = await resp.json()
                            if "detail" in response:
                                error_message = response["detail"]
                                raise RequireMFAException(error_message)
                            elif "error_code" in response:
                                error_message = response["error_code"]
                            else:
                                error_message = (
                                    f"Unrecognized error message: '{response}'"
                                )
                            raise LoginFailedException(error_message)
                        except:
                            raise LoginFailedException(
                                f"HTTP Code {resp.status}: {resp.reason}\nRaw response: {resp.text}"
                            )
                    response = await resp.json()
                    self.set_token(response["token"])
                    self._headers["Authorization"] = f"Token {self._token}"

        await retry_with_backoff(_attempt_mfa)

    def _get_graphql_client(self) -> Client:
        """
        Creates a correctly configured GraphQL client for connecting to Monarch Money.
        """
        if not self._token or "Authorization" not in self._headers:
            raise LoginFailedException(
                "Make sure you call login() first or provide a session token!"
            )
        transport = AIOHTTPTransport(
            url=MonarchMoneyEndpoints.getGraphQL(),
            headers=self._headers,
            timeout=self._timeout,
            ssl=True,
        )
        return Client(
            transport=transport,
            fetch_schema_from_transport=False,
            execute_timeout=self._timeout,
        )

    # Performance and monitoring methods
    def get_performance_stats(self) -> Dict[str, Any]:
        """
        Get performance statistics for GraphQL operations.

        Returns:
            Performance statistics including operation timings and cache metrics
        """
        if hasattr(self, "_graphql_client") and self._graphql_client:
            return self._graphql_client.get_performance_stats()
        return {"error": "Advanced GraphQL client not available"}

    def clear_cache(self) -> None:
        """Clear the GraphQL operation cache."""
        if hasattr(self, "_graphql_client") and self._graphql_client:
            self._graphql_client.clear_cache()
            logger.info("GraphQL cache cleared")

    async def close(self) -> None:
        """
        Close the MonarchMoney client and cleanup resources.

        This should be called when you're done using the client to ensure
        proper cleanup of connections and resources.
        """
        if hasattr(self, "_graphql_client") and self._graphql_client:
            await self._graphql_client.close()
            logger.debug("GraphQL client resources cleaned up")

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit with cleanup."""
        await self.close()
