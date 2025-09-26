"""Helper classes for scripts for cluster support packages."""

from typing import Optional, List

from cyberfusion.ClusterSupport._interfaces import (
    APIObjectInterface,
    sort_lists,
)
from cyberfusion.ClusterSupport.clusters import LoadBalancingMethod
from cyberfusion.ClusterSupport.nodes import NodeGroup

ENDPOINT_HAPROXY_LISTENS = "/api/v1/haproxy-listens"
MODEL_HAPROXY_LISTENS = "haproxy_listens"


class HAProxyListen(APIObjectInterface):
    """Represents object."""

    _TABLE_HEADERS = [
        "ID",
        "Name",
        "Nodes Group",
        "Nodes",
        "Port",
        "Socket Path",
        "Load Balancing Method",
        "Destination Cluster",
        "Cluster",
    ]
    _TABLE_HEADERS_DETAILED: list = []

    _TABLE_FIELDS = [
        "id",
        "name",
        "nodes_group",
        "_nodes_hostnames",
        "port",
        "socket_path",
        "load_balancing_method",
        "_destination_cluster_label",
        "_cluster_label",
    ]
    _TABLE_FIELDS_DETAILED: list = []

    @sort_lists  # type: ignore[misc]
    def _set_attributes_from_model(
        self,
        obj: dict,
    ) -> None:
        """Set class attributes from API output."""
        self.json_body = obj

        self.id = obj["id"]
        self.name = obj["name"]
        self.nodes_group = obj["nodes_group"]
        self.nodes_ids = obj["nodes_ids"]
        self.port = obj["port"]
        self.socket_path = obj["socket_path"]
        self.destination_cluster_id = obj["destination_cluster_id"]
        self.load_balancing_method = obj["load_balancing_method"]
        self.cluster_id: int = obj["cluster_id"]
        self.created_at = obj["created_at"]
        self.updated_at = obj["updated_at"]

        self.cluster = self.support.get_clusters(id_=self.cluster_id)[0]
        self._cluster_label = self.cluster._label

        self.destination_cluster = None
        self._destination_cluster_label = None

        if self.destination_cluster_id in self.support.accessible_core_api_clusters:
            self.destination_cluster = self.support.get_clusters(
                id_=self.destination_cluster_id
            )[0]
            self._destination_cluster_label = self.destination_cluster._label

        self.nodes = None
        self._nodes_hostnames = None

        if self.nodes_ids:
            self.nodes = [
                self.support.get_nodes(id_=id_)[0] for id_ in obj["nodes_ids"]
            ]
            self._nodes_hostnames = [node.hostname for node in self.nodes]

    def create(
        self,
        *,
        name: str,
        nodes_group: NodeGroup,
        nodes_ids: Optional[List[int]] = None,
        port: Optional[int],
        socket_path: Optional[str],
        destination_cluster_id: int,
        cluster_id: int,
        load_balancing_method: Optional[
            LoadBalancingMethod
        ] = LoadBalancingMethod.ROUND_ROBIN,
    ) -> None:
        """Create object."""
        url = ENDPOINT_HAPROXY_LISTENS
        data = {
            "name": name,
            "nodes_group": nodes_group,
            "nodes_ids": nodes_ids,
            "port": port,
            "socket_path": socket_path,
            "destination_cluster_id": destination_cluster_id,
            "load_balancing_method": load_balancing_method,
            "cluster_id": cluster_id,
        }

        self.support.request.POST(url, data)
        response = self.support.request.execute()

        self._set_attributes_from_model(response)

        self.support.haproxy_listens.append(self)

    def delete(self) -> None:
        """Delete object."""
        url = f"{ENDPOINT_HAPROXY_LISTENS}/{self.id}"

        self.support.request.DELETE(url)
        self.support.request.execute()

        self.support.haproxy_listens.remove(self)
