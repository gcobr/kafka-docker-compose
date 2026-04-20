# Kafka Docker Compose

This project provides a Docker Compose setup for running a local Apache Kafka cluster using KRaft mode (without Zookeeper). It includes three Kafka brokers configured as a highly available cluster and a web-based UI for managing and monitoring the cluster.

## Services

The [docker-compose.yaml](./docker-compose.yaml) file spins up the following services:

### Kafka Brokers
- **kafka-1**: Kafka broker/controller node 1, accessible on host ports `9094` (plaintext) and `9097` (mTLS)
- **kafka-2**: Kafka broker/controller node 2, accessible on host ports `9095` (plaintext) and `9098` (mTLS)
- **kafka-3**: Kafka broker/controller node 3, accessible on host ports `9096` (plaintext) and `9099` (mTLS)

All brokers are configured to run in KRaft mode with:
- Shared cluster ID: `abcdefghijklmnopqrstuv`.
- 3-node controller quorum for fault tolerance.
- Replication factors set for high availability (default replication factor: 3, min in-sync replicas: 2).
- Plaintext and mTLS listeners for local development.
- Automatic topic creation disabled.

### Kafka UI
<img src="readme/kafka-ui.jpeg" width="70%">

- **kafka-ui**: Web-based UI for browsing topics, messages, partitions, and consumer groups.
- Accessible at http://localhost:8078.
- Connected to all three Kafka brokers for cluster management.

### AKHQ
<img src="readme/akhq.jpeg" width="70%">

- **akhq**: Alternative web-based UI for Kafka management and monitoring.
- Accessible at http://localhost:8079.
- Provides similar functionality to kafka-ui with a different interface.

**AKHQ API:** See [AKHQ](./readme/akhq/README.md)

## Usage

### Starting the Cluster
To start all services in detached mode:
```bash
docker-compose up -d
```

### Stopping the Cluster
To stop and remove all containers:
```bash
docker-compose down
```

To stop and remove containers along with volumes (this will delete persisted data):
```bash
docker-compose down -v
```

### Accessing Kafka
- **Bootstrap servers** for external clients:
  - Plaintext: `localhost:9094,localhost:9095,localhost:9096`
  - mTLS: `localhost:9097,localhost:9098,localhost:9099`
- Use any of the host ports to connect to the cluster.
- For Docker-internal communication, use `kafka-1:9092`, `kafka-2:9092`, `kafka-3:9092`.

### Accessing the UI
Open your browser and navigate to http://localhost:8078 to access the Kafka UI or http://localhost:8079 for AKHQ.

## Introspection Utility
This project includes a Python-based introspection utility in the `instrospection` folder. It connects to the local Kafka brokers and generates a Markdown report with broker metadata, topic partition details, and broker configuration.

To use it:
1. Create a Python virtual environment in the project root:
   ```bash
   python3 -m venv .venv
   ```
2. Activate the virtual environment:
   ```bash
   . .venv/bin/activate
   ```
3. Install the Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the introspection script:
   ```bash
   python instrospection/introspection.py
   ```

The report is written to [instrospection/kafka-introspection-report.md](./instrospection/kafka-introspection-report.md).

## Configuration Notes

- **KRaft Mode**: This setup uses Apache Kafka's KRaft (Kafka Raft) metadata mode, eliminating the need for Zookeeper.
- **No Schema Registry**: This Compose file does not include a schema registry because the standard Apache Kafka images do not provide one.
- **Schema handling**: The brokers do not require messages to include a schema ID.
- **Schema ID behavior**: If a producer includes a schema ID, Kafka itself will not validate it against any registry or schema store.
- **Persistence**: Data is persisted in named Docker volumes (`kafka_1_`, `kafka_2_`, `kafka_3_`).
- **Security**: Plaintext listeners are used for local development only. mTLS listeners are also available for secure connections. Do not use plaintext in production.
- **mTLS Configuration**: The cluster includes mTLS listeners using self-signed certificates. Client certificates are required for mTLS connections. See the [certs](./certs/) directory for certificate generation details.
- **Ports**: Host ports 9094-9096 are exposed for Kafka brokers (plaintext), 9097-9099 for mTLS, 8078 for Kafka UI, and 8079 for AKHQ.

## Prerequisites

- Docker and Docker Compose installed on your system.
- At least 4GB of available RAM (recommended for running 3 Kafka brokers).

## Troubleshooting

- If containers fail to start, ensure no other services are using ports 9094-9096, 8078, or 8079.
- Check container logs with `docker-compose logs <service-name>`.
- For Kafka connection issues, verify the bootstrap servers configuration in your client applications.