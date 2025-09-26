"""Factories for API object."""

import factory.fuzzy
import factory

from cyberfusion.ClusterSupport.clusters import LoadBalancingMethod
from cyberfusion.ClusterSupport.haproxy_listens import HAProxyListen
from cyberfusion.ClusterSupport.nodes import NodeGroup
from cyberfusion.ClusterSupport.tests_factories import BaseBackendFactory


class _HAProxyListenFactory(BaseBackendFactory):
    """Factory for specific object."""

    class Meta:
        """Settings."""

        model = HAProxyListen

    name = factory.Faker(
        "password", special_chars=False, upper_case=False, digits=False
    )


class _HAProxyListenMariaDBFactory(_HAProxyListenFactory):
    """Factory for specific object."""

    class Meta:
        """Settings."""

        exclude = (
            "cluster",
            "destination_cluster",
        )

    cluster = factory.SubFactory(
        "cyberfusion.ClusterSupport.tests_factories.clusters.ClusterFactory"
    )
    cluster_id = factory.SelfAttribute("cluster.id")
    destination_cluster = factory.SubFactory(
        "cyberfusion.ClusterSupport.tests_factories.clusters.ClusterDatabaseFactory"
    )
    destination_cluster_id = factory.SelfAttribute("destination_cluster.id")
    load_balancing_method = factory.fuzzy.FuzzyChoice(LoadBalancingMethod)
    nodes_group = NodeGroup.MARIADB


class _HAProxyListenMeilisearchFactory(_HAProxyListenFactory):
    """Factory for specific object."""

    class Meta:
        """Settings."""

        exclude = (
            "cluster",
            "destination_cluster",
        )

    cluster = factory.SubFactory(
        "cyberfusion.ClusterSupport.tests_factories.clusters.ClusterFactory"
    )
    cluster_id = factory.SelfAttribute("cluster.id")
    destination_cluster = factory.SubFactory(
        "cyberfusion.ClusterSupport.tests_factories.clusters.ClusterDatabaseFactory"
    )
    destination_cluster_id = factory.SelfAttribute("destination_cluster.id")
    load_balancing_method = factory.fuzzy.FuzzyChoice(LoadBalancingMethod)
    nodes_group = NodeGroup.MEILISEARCH


class _HAProxyListenPostgreSQLFactory(_HAProxyListenFactory):
    """Factory for specific object."""

    class Meta:
        """Settings."""

        exclude = (
            "cluster",
            "destination_cluster",
        )

    cluster = factory.SubFactory(
        "cyberfusion.ClusterSupport.tests_factories.clusters.ClusterFactory"
    )
    cluster_id = factory.SelfAttribute("cluster.id")
    destination_cluster = factory.SubFactory(
        "cyberfusion.ClusterSupport.tests_factories.clusters.ClusterDatabaseFactory"
    )
    destination_cluster_id = factory.SelfAttribute("destination_cluster.id")
    load_balancing_method = factory.fuzzy.FuzzyChoice(LoadBalancingMethod)
    nodes_group = NodeGroup.POSTGRESQL


class _HAProxyListenRabbitMQFactory(_HAProxyListenFactory):
    """Factory for specific object."""

    class Meta:
        """Settings."""

        exclude = (
            "cluster",
            "destination_cluster",
        )

    cluster = factory.SubFactory(
        "cyberfusion.ClusterSupport.tests_factories.clusters.ClusterFactory"
    )
    cluster_id = factory.SelfAttribute("cluster.id")
    destination_cluster = factory.SubFactory(
        "cyberfusion.ClusterSupport.tests_factories.clusters.ClusterDatabaseFactory"
    )
    destination_cluster_id = factory.SelfAttribute("destination_cluster.id")
    load_balancing_method = factory.fuzzy.FuzzyChoice(LoadBalancingMethod)
    nodes_group = NodeGroup.RABBITMQ


class _HAProxyListenSingleStoreFactory(_HAProxyListenFactory):
    """Factory for specific object."""

    class Meta:
        """Settings."""

        exclude = (
            "cluster",
            "destination_cluster",
        )

    cluster = factory.SubFactory(
        "cyberfusion.ClusterSupport.tests_factories.clusters.ClusterFactory"
    )
    cluster_id = factory.SelfAttribute("cluster.id")
    destination_cluster = factory.SubFactory(
        "cyberfusion.ClusterSupport.tests_factories.clusters.ClusterDatabaseFactory"
    )
    destination_cluster_id = factory.SelfAttribute("destination_cluster.id")
    load_balancing_method = factory.fuzzy.FuzzyChoice(LoadBalancingMethod)
    nodes_group = NodeGroup.SINGLESTORE


class _HAProxyListenWithNodesIdsFactory(_HAProxyListenFactory):
    """Factory for specific object with nodes_ids."""

    class Meta:
        """Settings."""

        exclude = (
            "cluster",
            "destination_cluster",
            "node",
        )

    cluster = factory.SubFactory(
        "cyberfusion.ClusterSupport.tests_factories.clusters.ClusterFactory"
    )
    cluster_id = factory.SelfAttribute("cluster.id")
    destination_cluster = factory.SelfAttribute("node.cluster")
    destination_cluster_id = factory.SelfAttribute("destination_cluster.id")
    load_balancing_method = factory.fuzzy.FuzzyChoice(LoadBalancingMethod)
    node = factory.SubFactory(
        "cyberfusion.ClusterSupport.tests_factories.nodes.NodeMariaDBFactory"
    )
    nodes_ids = factory.LazyAttribute(lambda o: [o.node.id])
    nodes_group = factory.LazyAttribute(lambda o: o.node.groups[0])


class HAProxyListenMariaDBPortFactory(_HAProxyListenMariaDBFactory):
    """Factory for specific object."""

    socket_path = None
    port = 3306


class HAProxyListenMariaDBPortNodesIdsFactory(_HAProxyListenWithNodesIdsFactory):
    """Factory for specific object."""

    socket_path = None
    port = 3306


class HAProxyListenMariaDBSocketPathFactory(_HAProxyListenMariaDBFactory):
    """Factory for specific object."""

    socket_path = "/run/mysqld/mysql.sock"
    port = None


class HAProxyListenMeilisearchPortFactory(_HAProxyListenMeilisearchFactory):
    """Factory for specific object."""

    socket_path = None
    port = 7700


class HAProxyListenMeilisearchSocketPathFactory(_HAProxyListenMeilisearchFactory):
    """Factory for specific object."""

    socket_path = "/run/meilisearch/meilisearch.sock"
    port = None


class HAProxyListenPostgreSQLPortFactory(_HAProxyListenPostgreSQLFactory):
    """Factory for specific object."""

    socket_path = None
    port = 5432


class HAProxyListenPostgreSQLSocketPathFactory(_HAProxyListenPostgreSQLFactory):
    """Factory for specific object."""

    socket_path = "/run/postgresql/.s.PGSQL.5432"
    port = None


class HAProxyListenRabbitMQPortFactory(_HAProxyListenRabbitMQFactory):
    """Factory for specific object."""

    socket_path = None
    port = 5672


class HAProxyListenRabbitMQSocketPathFactory(_HAProxyListenRabbitMQFactory):
    """Factory for specific object."""

    socket_path = "/run/rabbitmq/rabbitmq.sock"
    port = None


class HAProxyListenSingleStorePortFactory(_HAProxyListenSingleStoreFactory):
    """Factory for specific object."""

    socket_path = None
    port = 3306


class HAProxyListenSingleStoreSocketPathFactory(_HAProxyListenSingleStoreFactory):
    """Factory for specific object."""

    socket_path = "/run/singlestore/singlestore.sock"
    port = None
