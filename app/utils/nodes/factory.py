from core.protocol import NETWORK_BITCOIN, NETWORK_ETHEREUM
from bitcoin.node import BitcoinNode
from ethereum.node import EthereumNode


class NodeFactory:
    @classmethod
    def create_node(cls, network: str):
        node_class = {
            NETWORK_BITCOIN: BitcoinNode,
            NETWORK_ETHEREUM: EthereumNode
            # Add other networks and their corresponding classes as needed
        }.get(network)

        if node_class is None:
            raise ValueError(f"Unsupported network: {network}")

        return node_class()