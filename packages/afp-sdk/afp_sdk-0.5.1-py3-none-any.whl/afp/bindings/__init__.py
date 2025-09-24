"""Typed bindings around the smart contracts of the Autonomous Futures Protocol."""

from .auctioneer_facet import AuctionConfig, AuctionData, BidData
from .bankruptcy_facet import LAAData, PositionLossData
from .clearing_facet import ClearingConfig, Config, Intent, IntentData, Side, Trade
from .facade import (
    ClearingDiamond,
    MarginAccountRegistry,
    OracleProvider,
    ProductRegistry,
    SystemViewer,
)
from .margin_account import MarginAccount, PositionData, Settlement
from .product_registry import (
    OracleSpecification,
    Product,
    ProductMetadata,
    ProductState,
)
from .system_viewer import UserMarginAccountData
from .trading_protocol import TradingProtocol

__all__ = (
    # Contract bindings
    "ClearingDiamond",
    "MarginAccount",
    "MarginAccountRegistry",
    "OracleProvider",
    "ProductRegistry",
    "SystemViewer",
    "TradingProtocol",
    # Structures
    "AuctionConfig",
    "AuctionData",
    "BidData",
    "ClearingConfig",
    "Config",
    "Intent",
    "IntentData",
    "LAAData",
    "OracleSpecification",
    "PositionData",
    "PositionLossData",
    "Product",
    "ProductMetadata",
    "Settlement",
    "Trade",
    "UserMarginAccountData",
    # Enumerations
    "ProductState",
    "Side",
)
