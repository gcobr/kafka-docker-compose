from kafka import KafkaConsumer
from kafka.admin import KafkaAdminClient, ConfigResource, ConfigResourceType
from kafka.errors import KafkaError
from kafka.structs import TopicPartition

BOOTSTRAP_SERVERS = ["localhost:9094", "localhost:9095", "localhost:9096"]


def format_config_entry(entry):
    if hasattr(entry, "name"):
        return {
            "name": entry.name,
            "value": entry.value,
            "source": entry.source,
            "is_default": entry.is_default,
            "is_read_only": entry.is_read_only,
            "is_sensitive": entry.is_sensitive,
        }

    name, value, read_only, source, is_sensitive, synonyms = entry
    return {
        "name": name,
        "value": value,
        "source": source,
        "is_default": False,
        "is_read_only": read_only,
        "is_sensitive": is_sensitive,
    }


def get_cluster_metadata(bootstrap_servers):
    consumer = KafkaConsumer(
        bootstrap_servers=bootstrap_servers,
        api_version_auto_timeout_ms=10000,
        request_timeout_ms=10000,
        consumer_timeout_ms=1000,
    )

    try:
        # Trigger metadata refresh.
        consumer.topics()
        cluster = consumer._client.cluster

        brokers = []
        for broker in cluster.brokers():
            brokers.append({
                "node_id": broker.nodeId,
                "host": broker.host,
                "port": broker.port,
                "rack": broker.rack,
            })

        topics = []
        for topic in sorted(cluster.topics()):
            partitions = []
            for partition in sorted(cluster.partitions_for_topic(topic) or []):
                topic_partition = TopicPartition(topic, partition)
                leader = cluster.leader_for_partition(topic_partition)
                partition_metadata = cluster._partitions[topic][partition]
                replicas = partition_metadata.replicas
                isrs = partition_metadata.isr
                partitions.append({
                    "partition": partition,
                    "leader": leader if leader is not None else None,
                    "replicas": replicas,
                    "isr": isrs,
                })

            topics.append({
                "name": topic,
                "partitions": partitions,
            })

        return {
            "cluster_id": cluster.cluster_id,
            "controller_id": cluster.controller.nodeId if cluster.controller else None,
            "brokers": brokers,
            "topics": topics,
        }
    finally:
        consumer.close()


def describe_broker_configs(bootstrap_servers, broker_ids):
    admin = KafkaAdminClient(bootstrap_servers=bootstrap_servers, client_id="introspection-admin")
    try:
        resources = [ConfigResource(ConfigResourceType.BROKER, str(broker_id)) for broker_id in broker_ids]
        configs = admin.describe_configs(resources)

        broker_configs = {}
        for response in configs:
            for resource_response in response.resources:
                _, _, _, resource_name, entries = resource_response
                broker_configs[resource_name] = [format_config_entry(entry) for entry in entries]

        return broker_configs
    finally:
        admin.close()


def escape_markdown(value):
    if value is None:
        return ""

    text = str(value)
    text = text.replace("|", "\\|")
    text = text.replace("\n", "<br>")
    text = text.replace("\r", "")
    return text


def markdown_table(headers, rows):
    header_line = "| " + " | ".join(headers) + " |"
    separator_line = "| " + " | ".join(["---"] * len(headers)) + " |"
    lines = [header_line, separator_line]

    for row in rows:
        values = [escape_markdown(row.get(header, "")) for header in headers]
        lines.append("| " + " | ".join(values) + " |")

    return "\n".join(lines)


def build_markdown_report(metadata, configs):
    lines = ["# Kafka Introspection Report", ""]

    lines.extend([
        "## Cluster",
        "",
        f"- **Cluster ID:** `{escape_markdown(metadata.get('cluster_id'))}`",
        f"- **Controller ID:** `{escape_markdown(metadata.get('controller_id'))}`",
        f"- **Bootstrap servers:** `{escape_markdown(', '.join(BOOTSTRAP_SERVERS))}`",
        ""
    ])

    lines.append("## Brokers")
    lines.append("")
    brokers = metadata.get("brokers", [])
    if brokers:
        broker_rows = [
            {
                "node_id": broker["node_id"],
                "host": broker["host"],
                "port": broker["port"],
                "rack": broker["rack"],
            }
            for broker in brokers
        ]
        lines.append(markdown_table(["node_id", "host", "port", "rack"], broker_rows))
    else:
        lines.append("No brokers discovered.")

    lines.extend(["", "## Topics", ""])
    topics = metadata.get("topics", [])
    if topics:
        for topic in topics:
            lines.extend([f"### `{escape_markdown(topic['name'])}`", ""])
            topic_rows = [
                {
                    "partition": partition["partition"],
                    "leader": partition["leader"],
                    "replicas": ", ".join(str(r) for r in partition["replicas"]),
                    "isr": ", ".join(str(i) for i in partition["isr"]),
                }
                for partition in topic["partitions"]
            ]
            lines.append(markdown_table(["partition", "leader", "replicas", "isr"], topic_rows))
            lines.append("")
    else:
        lines.append("No topics discovered.")
        lines.append("")

    lines.append("## Broker Configs")
    lines.append("")
    if configs:
        for broker_id in sorted(configs, key=lambda x: str(x)):
            lines.extend([f"### Broker `{escape_markdown(broker_id)}`", ""])
            config_rows = [
                {
                    "name": entry["name"],
                    "value": entry["value"],
                    "source": entry["source"],
                    "default": str(entry["is_default"]).lower(),
                    "readonly": str(entry["is_read_only"]).lower(),
                    "sensitive": str(entry["is_sensitive"]).lower(),
                }
                for entry in sorted(configs[broker_id], key=lambda x: x["name"])
            ]
            lines.append(markdown_table(["name", "value", "source", "default", "readonly", "sensitive"], config_rows))
            lines.append("")
    else:
        lines.append("No broker configs available.")

    return "\n".join(lines)


def write_markdown_report(file_path, metadata, configs):
    report = build_markdown_report(metadata, configs)
    with open(file_path, "w", encoding="utf-8") as report_file:
        report_file.write(report)


def main():
    try:
        metadata = get_cluster_metadata(BOOTSTRAP_SERVERS)
        broker_ids = [broker["node_id"] for broker in metadata.get("brokers", [])]
        configs = {}
        if broker_ids:
            configs = describe_broker_configs(BOOTSTRAP_SERVERS, broker_ids)

        report_file = "instrospection/kafka-introspection-report.md"
        write_markdown_report(report_file, metadata, configs)
        print(f"Wrote Kafka introspection report to {report_file}")
    except KafkaError as exc:
        print("Failed to introspect Kafka cluster:", exc)


if __name__ == "__main__":
    main()
